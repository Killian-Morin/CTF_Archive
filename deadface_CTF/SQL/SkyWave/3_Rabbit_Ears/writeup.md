# Clue / Information
Note: Access the database from High Tower.

Florian Olyff operates several towers. What is the most commonly used antenna type on the towers she manages?

Submit the flag as flag{antenna_type number}. Example: flag{Long Antenna 5}. (it is the name and useage count)

# Resolution
Connect with ssh:
```bash
> ssh skywave.deadface.io -l skywave
skywave@skywave.deadface.io's password: d34df4c3
```
or if you have sshpass: `sshpass -p d34df4c3 ssh -l skywave skywave.deadface.io` (didn't tested)

To know all the tables present:
```sql
MySQL [cell_tower_db]> SHOW TABLES;
+-------------------------+
| Tables_in_cell_tower_db |
+-------------------------+
| Antennas                |
| Carriers                |
| Connections             |
| Device_Types            |
| Devices                 |
| Operators               |
| Technicians             |
| Tower_Maintenance       |
| Tower_Sectors           |
| Towers                  |
+-------------------------+
```

We have to find the `operator_id` or the `technician_id` of Florian Olyff.
```sql
SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'Operators';
+-----------------+
| COLUMN_NAME     |
+-----------------+
| operator_id     |
| first_name      |
| last_name       |
| employee_number |
+-----------------+

SELECT first_name, last_name, operator_id, employee_number FROM Operators WHERE first_name = 'Florian' AND last_name = 'Olyff';
+------------+-----------+-------------+-----------------+
| first_name | last_name | operator_id | employee_number |
+------------+-----------+-------------+-----------------+
| Florian    | Olyff     |           4 | 3223634520      |
+------------+-----------+-------------+-----------------+

SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'Technicians';
+-----------------+
| COLUMN_NAME     |
+-----------------+
| technician_id   |
| first_name      |
| last_name       |
| contact_number  |
| street          |
| city            |
| state           |
| postal_code     |
| employee_number |
+-----------------+

SELECT first_name, last_name, technician_id, employee_number FROM Technicians WHERE first_name = 'Florian' AND last_name = 'Olyff';
Empty set
```

Good news, Florian Olyff is _only_ an operator, this narrow down the research.

Next step, find the towers on which the operator with `operator_id = 4` is assigned
```sql
SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'Towers';
+-----------------------+
| COLUMN_NAME           |
+-----------------------+
| tower_id              |
| location_name         |
| latitude              |
| longitude             |
| elevation             |
| tower_height          |
| operator_id           |
| status                |
| install_date          |
| last_maintenance_date |
+-----------------------+

SELECT operator_id, tower_id FROM Towers WHERE operator_id = 4;
+-------------+----------+
| operator_id | tower_id |
+-------------+----------+
|           4 |      189 |
+-------------+----------+
```

```sql
SELECT * FROM Towers WHERE operator_id = 4;
+----------+---------------+-----------+------------+-----------+--------------+-------------+--------+--------------+-----------------------+
| tower_id | location_name | latitude  | longitude  | elevation | tower_height | operator_id | status | install_date | last_maintenance_date |
+----------+---------------+-----------+------------+-----------+--------------+-------------+--------+--------------+-----------------------+
|      189 | PA            | 40.725061 | -76.969425 |     36.19 |        88.71 |           4 | active | 2011-02-09   | 2023-08-24            |
+----------+---------------+-----------+------------+-----------+--------------+-------------+--------+--------------+-----------------------+

SELECT * FROM Tower_Sectors WHERE tower_id = 189;
+-----------+----------+---------+------------+----------------+--------------+
| sector_id | tower_id | azimuth | antenna_id | frequency_band | power_output |
+-----------+----------+---------+------------+----------------+--------------+
|      1140 |      189 |    0.00 |          9 | 850 MHz        |         5.06 |
|      1141 |      189 |   45.00 |          4 | 700 MHz        |         4.73 |
|      1142 |      189 |   90.00 |          2 | C-band         |         4.31 |
|      1143 |      189 |  135.00 |          9 | 3.45 GHz       |         9.17 |
|      1144 |      189 |  180.00 |          6 | 2.5 GHz        |         4.54 |
|      1145 |      189 |  225.00 |          9 | 700 MHz        |         5.89 |
|      1146 |      189 |  270.00 |          5 | C-band         |         7.83 |
|      1147 |      189 |  315.00 |          4 | 2.5 GHz        |         7.42 |
+-----------+----------+---------+------------+----------------+--------------+
8 rows in set (0.001 sec)

SELECT antenna_id, COUNT(*) AS count FROM Tower_Sectors WHERE tower_id = 189 GROUP BY antenna_id ORDER BY count DESC LIMIT 1;
+------------+-------+
| antenna_id | count |
+------------+-------+
|          9 |     3 |
+------------+-------+

SELECT * FROM Antennas WHERE antenna_id = 9;
+------------+---------------------------------------+
| antenna_id | antenna_name                          |
+------------+---------------------------------------+
|          9 | Multiple Input Multiple Output (MIMO) |
+------------+---------------------------------------+
```

So flag could be `flag{Multiple Input Multiple Output (MIMO) 3}` and it is !!
