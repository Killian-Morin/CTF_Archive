# Clue / Information
Note: Access the database from High Tower.

Which devices switched between towers within a 5 to 10 minute timespan? Submit the number of connections and the IMEI of the device with the earliest connection time.

Submit the flag as flag{number_IMEI}. Example: flag{100_123456789012345}.

# Resolution
Connect with ssh:
```bash
> ssh skywave.deadface.io -l skywave
skywave@skywave.deadface.io's password:d34df4c3
```
or if you have sshpass: `sshpass -p d34df4c3 ssh -l skywave skywave.deadface.io` (didn't tested)

```sql
WITH Connections AS (
    SELECT d.device_imei, c.tower_id, c.connection_time,
           LAG(c.connection_time) OVER (PARTITION BY d.device_id ORDER BY c.connection_time) AS prev_connection_time
    FROM Connections c
    JOIN Devices d ON c.device_id = d.device_id
),
Switches AS (
    SELECT device_imei, COUNT(*) AS num_switches, MIN(connection_time) AS earliest_connection
    FROM Connections
    WHERE prev_connection_time IS NOT NULL
    AND connection_time > prev_connection_time
    AND TIMESTAMPDIFF(MINUTE, prev_connection_time, connection_time) BETWEEN 5 AND 10
    GROUP BY device_imei
)
SELECT num_switches, device_imei, earliest_connection
FROM Switches
ORDER BY earliest_connection
LIMIT 1;
```

```sql
WITH DeviceConnections AS (
    SELECT d.device_imei, c.device_id, c.tower_id, c.connection_time,
           LAG(c.tower_id) OVER (PARTITION BY c.device_id ORDER BY c.connection_time) AS prev_tower_id,
           LAG(c.connection_time) OVER (PARTITION BY c.device_id ORDER BY c.connection_time) AS prev_connection_time
    FROM Connections c
    JOIN Devices d ON c.device_id = d.device_id
),
Switches AS (
    SELECT device_imei, COUNT(*) AS num_switches, MIN(connection_time) AS earliest_connection
    FROM DeviceConnections
    WHERE prev_connection_time IS NOT NULL
    AND prev_tower_id IS NOT NULL
    AND tower_id != prev_tower_id  -- This ensures it's a tower switch
    AND TIMESTAMPDIFF(MINUTE, prev_connection_time, connection_time) BETWEEN 5 AND 10
    GROUP BY device_imei
)
SELECT num_switches, device_imei, earliest_connection
FROM Switches
ORDER BY earliest_connection
LIMIT 1;

WITH DeviceConnections AS (SELECT d.device_imei, c.device_id, c.tower_id, c.connection_time, LAG(c.tower_id) OVER (PARTITION BY c.device_id ORDER BY c.connection_time) AS prev_tower_id, LAG(c.connection_time) OVER (PARTITION BY c.device_id ORDER BY c.connection_time) AS prev_connection_time FROM Connections c JOIN Devices d ON c.device_id = d.device_id
), Switches AS (SELECT device_imei, COUNT(*) AS num_switches, MIN(connection_time) AS earliest_connection FROM DeviceConnections WHERE prev_connection_time IS NOT NULL AND prev_tower_id IS NOT NULL AND tower_id != prev_tower_id AND TIMESTAMPDIFF(MINUTE, prev_connection_time, connection_time) BETWEEN 5 AND 10 GROUP BY device_imei) SELECT num_switches, device_imei, earliest_connection FROM Switches ORDER BY earliest_connection LIMIT 1;
```

```sql
SELECT d.device_imei, COUNT(*) AS num_switches, MIN(c1.connection_time) AS earliest_connection
FROM Connections c1
JOIN Connections c2
  ON c1.device_id = c2.device_id
  AND c1.connection_time > c2.connection_time
  AND TIMESTAMPDIFF(MINUTE, c2.connection_time, c1.connection_time) BETWEEN 5 AND 10
  AND c1.tower_id != c2.tower_id
JOIN Devices d
  ON c1.device_id = d.device_id
GROUP BY d.device_imei
ORDER BY earliest_connection
LIMIT 1;
```

```sql
WITH DeviceConnections AS (
    SELECT
        d.device_imei,
        c.device_id,
        c.tower_id,
        c.connection_time,
        LAG(c.tower_id) OVER (PARTITION BY c.device_id ORDER BY c.connection_time) AS prev_tower,
        LAG(c.connection_time) OVER (PARTITION BY c.device_id ORDER BY c.connection_time) AS prev_time
    FROM
        Connections c
    JOIN
        Devices d ON c.device_id = d.device_id
),
HandoffDevices AS (
    SELECT
        dc.device_imei,
        dc.device_id,
        dc.connection_time,
        TIMESTAMPDIFF(MINUTE, dc.prev_time, dc.connection_time) AS time_diff
    FROM
        DeviceConnections dc
    WHERE
        dc.prev_tower IS NOT NULL
        AND dc.tower_id <> dc.prev_tower
        AND TIMESTAMPDIFF(MINUTE, dc.prev_time, dc.connection_time) BETWEEN 5 AND 10
)
-- Count devices that performed a handoff and find the device with the earliest connection
SELECT
    COUNT(DISTINCT hd.device_imei) AS num_devices,
    hd.device_imei AS earliest_device_imei,
    MIN(hd.connection_time) AS earliest_connection
FROM
    HandoffDevices hd
ORDER BY
    earliest_connection
LIMIT 1;
```

```sql
-- Step 1: Create a temporary table for DeviceConnections
CREATE TEMPORARY TABLE DeviceConnections AS
    SELECT
        d.device_imei,
        c.device_id,
        c.tower_id,
        c.connection_time,
        LAG(c.tower_id) OVER (PARTITION BY c.device_id ORDER BY c.connection_time) AS prev_tower,
        LAG(c.connection_time) OVER (PARTITION BY c.device_id ORDER BY c.connection_time) AS prev_time
    FROM
        Connections c
    JOIN
        Devices d ON c.device_id = d.device_id;

-- Step 2: Create a temporary table for HandoffDevices
CREATE TEMPORARY TABLE HandoffDevices AS
    SELECT
        dc.device_imei,
        dc.device_id,
        dc.connection_time,
        TIMESTAMPDIFF(MINUTE, dc.prev_time, dc.connection_time) AS time_diff
    FROM
        DeviceConnections dc
    WHERE
        dc.prev_tower IS NOT NULL
        AND dc.tower_id <> dc.prev_tower
        AND TIMESTAMPDIFF(MINUTE, dc.prev_time, dc.connection_time) BETWEEN 5 AND 10;

-- Step 3: Query to get the final result
SELECT
    COUNT(DISTINCT hd.device_imei) AS num_devices,
    hd.device_imei AS earliest_device_imei,
    MIN(hd.connection_time) AS earliest_connection
FROM
    HandoffDevices hd
ORDER BY
    earliest_connection
LIMIT 1;
```

WITH TestCTE AS (SELECT 1 AS 1) SELECT * FROM Devices;


Tried flag:
    flag{042813788700728}
    flag{1_042813788700728}
    flag{15_022972952317680}
