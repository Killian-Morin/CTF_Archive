# I believe you can't fly

## Clue / Information

In the world of Featherstone Airways, where airships dominate the skies and steam-powered engines hum in harmony with the winds, disaster strikes aboard Flight 404. A cacophony of alarms blares through the cabin, and an automated voice pierces the tension:
"Alert: Navigation systems compromised. Manual override unavailable."

The captain, drenched in sweat, confesses that the ship’s intricate steam-core systems have been infiltrated by rogue machinists. The autopilot is spewing erratic commands, and the controls have been rendered useless. Amid the chaos, your gaze falls upon a forgotten device—a mechanical tablet left behind by the ship’s chief engineer. Its dimly glowing screen is your only hope to uncover the secrets of this sabotage and reclaim control of the vessel.

The tablet appears to hold critical files containing traces of the hackers’ interference. To restore the autopilot and prevent the airship from plunging into the abyss, you must uncover the password hidden within these files. As the last passenger with a keen mind for cyber-steam security, it falls to you to analyze these files, piece together the password, and save the airship before it’s too late. Time is of the essence, and the lives of everyone aboard rest in your hands. Will you rise to the challenge and prove yourself the hero of the skies?

## Resolution

Reorganized chronogically the plane_logs.txt.

"System alert reset by User-ID: Admin123".

There are five entries with "encoded word detected", chronogically it results in:
- [2025-01-22 14:00:07] [...] ercbafr
- [2025-01-22 14:01:18] [...] KDFNGD\~dPbCbiU6H
- [2025-01-22 14:03:49] [...] 636c6566
- [2025-01-22 14:05:56] [...] 0110001011111011011000110110100001100101
- [2025-01-22 14:09:36] [...] c29sdXRpb24=

The binary number converted to hex gives: 62FB636865

If we combine them: `ercbafrKDFNGD\~dPbCbiU6H636c656662FB636865c29sdXRpb24=`

From Base64: `z·iúÊSF
ÓÛ	¸è~·éÎ¹ë®¶·ëÎ¹solution`

Flags attempted:
- `HACKDAY{Admin123}`
- `HACKDAY{ercbafr}`
- `HACKDAY{ercbafrKDFNGD\~dPbCbiU6H636c656662FB636865c29sdXRpb24=}`
- `HACKDAY{solution}`
- `HACKDAY{z·iúÊSF
ÓÛ	¸è~·éÎ¹ë®¶·ëÎ¹solution}`

### author => [@komorebi](https://github.com/Killian-Morin)

## Write-Up

[Official Write-Up](https://github.com/ChallengeHackDay/qualif-2025/blob/main/FORENSIC/I%20believe%20you%20can't%20fly/solve/Write-Up.pdf)
