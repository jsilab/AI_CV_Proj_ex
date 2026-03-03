import subprocess
import os
import sys

# get the project root (going up one level)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("=" * 40)
print("Select Mode:")
print("\t1) Image - using img 004545.jpg")
print("\t2) Camera - self-explanatory")
print("=" * 40)

print()

choice = input("Enter choice: ").strip()

if choice == "1":
    script = "main_still.py"
elif choice == "2":
    script = "main_vid.py"
else:
    print("Invalid choice")
    sys.exit(1)

script_path = os.path.join(base_dir, "windows", script)

subprocess.run([sys.executable, script_path])