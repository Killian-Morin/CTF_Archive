# Clue / Information
Note: Access the database from High Tower.

We need to determine which device had the longest running connection out of the towers with the following coordinates:

    (41.639642, -79.220682)
    (40.598271, -78.801089)
    (41.045892, -79.068358)
    (41.257279, -77.529468)

Additionally, let’s focus on only finding the longest running connection with a dBm greater than -100.

Submit the flag as flag{device_imei}. Example: flag{123456789012345}.

# Resolution
Connect with ssh:
```bash
> ssh skywave.deadface.io -l skywave
skywave@skywave.deadface.io's password: d34df4c3
```
or if you have sshpass: `sshpass -p d34df4c3 ssh -l skywave skywave.deadface.io` (didn't tested)

```sql
SELECT * FROM Towers WHERE latitude IN ('41.639642', '40.598271', '41.045892', '41.257279');
+----------+---------------+-----------+------------+-----------+--------------+-------------+--------+--------------+-----------------------+
| tower_id | location_name | latitude  | longitude  | elevation | tower_height | operator_id | status | install_date | last_maintenance_date |
+----------+---------------+-----------+------------+-----------+--------------+-------------+--------+--------------+-----------------------+
|      105 | PA            | 41.639642 | -79.220682 |     62.97 |       126.24 |          36 | active | 2016-03-22   | 2020-06-26            |
|      123 | PA            | 40.598271 | -78.801089 |    193.47 |        74.66 |         119 | active | 2000-10-11   | 2021-02-15            |
|      187 | PA            | 41.045892 | -79.068358 |     97.85 |       147.16 |          60 | active | 2010-04-07   | 2018-11-24            |
|      200 | PA            | 41.257279 | -77.529468 |    135.44 |       143.88 |          46 | active | 2009-02-01   | 2020-03-01            |
+----------+---------------+-----------+------------+-----------+--------------+-------------+--------+--------------+-----------------------+
```

Now we have the tower_id's of the four towers that interests us.

```sql
SELECT * FROM Connections LIMIT 5;
+---------------+-----------+----------+-----------+---------------------+-----------------+---------------------+
| connection_id | device_id | tower_id | sector_id | connection_time     | signal_strength | connection_duration |
+---------------+-----------+----------+-----------+---------------------+-----------------+---------------------+
|             1 |      2329 |       30 |       177 | 2024-09-07 17:38:55 |         -116.51 |                9074 |
|             2 |      1213 |      169 |      1019 | 2024-09-08 01:30:20 |          -98.31 |               14616 |
|             3 |      1606 |       41 |       248 | 2024-09-06 21:57:27 |         -106.18 |               47891 |
|             4 |       207 |       84 |       508 | 2024-09-07 21:20:19 |          -85.71 |               13691 |
|             5 |      1498 |       56 |       334 | 2024-09-06 10:08:28 |         -115.11 |               18494 |
+---------------+-----------+----------+-----------+---------------------+-----------------+---------------------+
```

```sql
SELECT * FROM Connections WHERE tower_id IN ('105', '123', '187', '200');
```

```sql
SELECT device_id, tower_id, MAX(connection_duration) AS longest_connection FROM Connections WHERE tower_id IN ('105', '123', '187', '200') AND signal_strength > -100 GROUP BY device_id, tower_id ORDER BY longest_connection DESC LIMIT 1;
+-----------+----------+--------------------+
| device_id | tower_id | longest_connection |
+-----------+----------+--------------------+
|       344 |      200 |              85709 |
+-----------+----------+--------------------+
```

We have the device_id, know to get the `device_imei`:

```sql
SELECT * FROM Devices WHERE device_id = 344;
+-----------+-----------------+----------------+--------------+---------+------------+
| device_id | device_imei     | device_type_id | manufacturer | model   | carrier_id |
+-----------+-----------------+----------------+--------------+---------+------------+
|       344 | 845303290931675 |              2 | CosmoTech    | Nova 15 |          4 |
+-----------+-----------------+----------------+--------------+---------+------------+
```

The flag is `flag{845303290931675}`
