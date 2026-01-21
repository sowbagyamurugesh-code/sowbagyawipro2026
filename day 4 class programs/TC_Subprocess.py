import subprocess
result=subprocess.run(
    "echo hello",
    shell=True,
    capture_output=True,
    text=True,
)
print(result.stdout)

subprocess.run(("python","TC_Classes.py"))
subprocess.run(("python","TC_AbstractClass.py"))