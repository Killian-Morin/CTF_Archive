# Clue / Information
Note: Access the database from High Tower.

We’re running with an assumption that d34th drove around and connected to various cell towers the day leading up to the attack.

We need you to determine which device IMEI connected to the most unique towers on September 7 from 16:10 to 18:54.

Submit the flag as flag{device_imei}. Example: flag{123456789012345}.

# Resolution
Connect with ssh:
```bash
> ssh skywave.deadface.io -l skywave
skywave@skywave.deadface.io's password:d34df4c3
```
or if you have sshpass: `sshpass -p d34df4c3 ssh -l skywave skywave.deadface.io` (didn't tested)

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
SELECT DISTINCT tower_id, device_id FROM Connections WHERE connection_time BETWEEN '2024-09-07 16:10:00' AND '2024-09-07 18:54:00';
...
191 rows in set
```

```sql
SELECT d.device_imei, COUNT(DISTINCT c.tower_id) AS unique_tower_count FROM Connections c JOIN Devices d ON c.device_id = d.device_id WHERE c.connection_time BETWEEN '2024-09-07 16:10:00' AND '2024-09-07 18:54:00' GROUP BY d.device_imei ORDER BY unique_tower_count DESC LIMIT 1;
```

The flag is: `flag{377494868035375}`

Tried flag:
	flag{643366592089524}