# Clue / Information
Note: Access the database from High Tower.

We can assume that d34th used some kind of smart device or computer to conduct his attacks. How many devices in the database are either a smart phone, a computer, or a tablet?

Submit the flag as flag{number}. Example: flag{10}.

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

The tables that would interest us might be 'Devices' and/or 'Device_Types'
```sql
SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'Devices';
+----------------+
| COLUMN_NAME    |
+----------------+
| device_id      |
| device_imei    |
| device_type_id |
| manufacturer   |
| model          |
| carrier_id     |
+----------------+

SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'Device_Types';
+------------------+
| COLUMN_NAME      |
+------------------+
| device_type_id   |
| device_type_name |
+------------------+

SELECT device_type_name FROM Device_Types;
+---------------------------+
| device_type_name          |
+---------------------------+
| smartphone                |
| mobile phone              |
| tablet                    |
| computer                  |
| iot                       |
| modem                     |
| gps fleet tracking device |
| health monitoring device  |
| point of sale             |
| vehicle                   |
+---------------------------+
```

We have to get the amount of 'either' a smart phone, a computer, or a tablet.
```sql
SELECT device_type_name, device_type_id FROM Device_Types WHERE device_type_name IN ('smartphone', 'tablet', 'computer');
+------------------+----------------+
| device_type_name | device_type_id |
+------------------+----------------+
| smartphone       |              1 |
| tablet           |              3 |
| computer         |              4 |
+------------------+----------------+
```

Now that we have the id's, we can use the `Devices` table to get the number of entry for those type of devices using the `device_type_id` column

query where all rows matching are printed out:
```sql
SELECT device_type_id FROM Devices WHERE device_type_id IN ('1', '3', '4');
...
714 rows in set (0.001 sec)
```

query where we have only the total amount of rows matching:
```sql
SELECT COUNT(*) AS total_rows FROM Devices WHERE device_type_id IN ('1', '3', '4');
+------------+
| total_rows |
+------------+
|        714 |
+------------+
```
The flag is: `flag{714}`
