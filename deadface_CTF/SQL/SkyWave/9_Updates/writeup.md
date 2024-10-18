# Clue / Information
Note: Access the database from High Tower.

How many towers received software updates?

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

The table `Towers` has a column `install_date` and `last_maintenance_date`.

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

Let's what is inside those columns
```sql
SELECT install_date, last_maintenance_date FROM Towers LIMIT 10;
+--------------+-----------------------+
| install_date | last_maintenance_date |
+--------------+-----------------------+
| 2013-08-25   | 2020-09-02            |
| 2006-01-29   | 2021-08-19            |
| 2004-04-30   | 2018-12-09            |
| 2015-08-18   | 2023-05-03            |
| 2001-09-27   | 2021-05-04            |
| 2008-04-01   | 2018-12-17            |
| 2014-01-05   | 2022-12-07            |
| 2012-03-28   | 2018-05-22            |
| 2007-08-12   | 2019-02-19            |
| 2016-08-31   | 2022-03-27            |
+--------------+-----------------------+
```

After checking all of the columns they all have differents dates, in itself logical since `last_maintenance_date` does not mean there is a software update.

So this track is not the right one.

Let's check the `Tower_Maintenance` table:
```sql
SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME = 'Tower_Maintenance';
+------------------+
| COLUMN_NAME      |
+------------------+
| maintenance_id   |
| tower_id         |
| maintenance_type |
| maintenance_date |
| technician_id    |
+------------------+
```

After seing what the column `maintenance_type` consists of, we can find `Software updates` entry, so this is the right track.

We have to get `tower_id` and `maintenance_type` where the maintenance type was a `Software updates`. The `DISTINCT` is important since we do not want duplicates, i.e. towers that were updated multiple times.

```sql
SELECT DISTINCT tower_id, maintenance_type FROM Tower_Maintenance WHERE maintenance_type = 'Software updates';
...
70 rows in set (0.002 sec)
```

```sql
SELECT tower_id, maintenance_type FROM Tower_Maintenance WHERE maintenance_type = 'Software updates';
...
96 rows in set (0.002 sec)
```

The flag is: `flag{70}`
