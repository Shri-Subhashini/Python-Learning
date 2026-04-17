import subprocess

res = subprocess.run(["dir"], shell = True, capture_output = True, text = True)

print(res.stdout)
