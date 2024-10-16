#!/usr/bin/env python3
import subprocess
import base64
import tempfile

try:
	b64 = input("base64 input: ")
	decoded = base64.b64decode(b64)

	if (len(decoded) > 10240):
		print("Too long!")
		exit(1)

	with tempfile.NamedTemporaryFile() as f:
		f.write(decoded)
		f.flush()
		try:
			subprocess.check_call(["ls", "lol"])
		except subprocess.CalledProcessError as e:
			print(f"Command failed with return code: {e.returncode}")

except:
	print("Error!")
	exit(1)
