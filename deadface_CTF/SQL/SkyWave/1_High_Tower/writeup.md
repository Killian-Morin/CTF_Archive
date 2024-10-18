# Clue / Information
We need your help tracking down d34th, the leader of DEADFACE. He recently conducted an attack against SkyWave Telecommunications. We’ve received cell tower data that might help us pinpoint d34th’s device and potentially lead us to his identity.

But first, we need to assess your familiarity with SQL and the data you’re being provided.

What is the tower_id of the cell tower that sits at an approximate elevation of 220 ft?

Submit the flag as flag{tower_id}. Example: flag{10}.

Access the database via SSH at skywave.deadface.io.
Username: skywave
Password: d34df4c3

# Resolution
Connect with ssh:
```bash
> ssh skywave.deadface.io -l skywave
skywave@skywave.deadface.io's password:d34df4c3
```
or if you have sshpass: `sshpass -p d34df4c3 ssh -l skywave skywave.deadface.io` (didn't tested)

We end up with the following prompt: `MySQL [cell_tower_db]>`
The base table is `cell_tower_db`

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

The one that I suppose interest us is the table `Towers`, so we need to get the name of the columns that we will use to affine our query:
(dumb way)
```sql
SELECT * FROM Towers;
+----------+---------------+-----------+------------+-----------+--------------+-------------+--------+--------------+-----------------------+
| tower_id | location_name | latitude  | longitude  | elevation | tower_height | operator_id | status | install_date | last_maintenance_date |
+----------+---------------+-----------+------------+-----------+--------------+-------------+--------+--------------+-----------------------+
```
(chad way)
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
```

We want the `tower_id` of the tower with the elevation 'that sits at an approximate elevation of 220 ft'
```sql
SELECT tower_id, elevation FROM Towers WHERE elevation BETWEEN 218 and 222;
+----------+-----------+
| tower_id | elevation |
+----------+-----------+
|      215 |    220.32 |
+----------+-----------+
```

The flag is `flag{215}`
