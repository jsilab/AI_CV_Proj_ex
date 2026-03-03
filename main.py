import subprocess
import os
import sys

def main():
    print("=" * 40)
    print("  Welcome to Image Tracker (WIP)")
    print("=" * 40)
    
    print()

    print("Please select your platform:")
    print("\t1) Mac")
    print("\t2) Windows\n")

    choice = input("Please, enter 1 or 2: ").strip()

    if choice == "1":
        platform_dir = "mac"
    elif choice == "2":
        platform_dir = "windows"
    else:
        print("INVALID ! ! !")
        print("Please run again, and enter the correct number!")
        sys.exit(1)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = os.path.join(base_dir, platform_dir, "run.py")

    ### edge case: 
    if not os.path.exists(script_dir):
        print("Could not find script in:", script_dir)
        sys.exit(1)

    subprocess.run([sys.executable, script_dir])

if __name__ == "__main__":
    main()
