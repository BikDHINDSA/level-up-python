import os
import sys
import subprocess

# defining local directory containing challenge logic!
CHALLENGES_DIR = "challenges"
# hardcoded index map for the challenges and their corrensponding scripts.
CHALLENGE_MAP = {
    1: ("Find Prime Factors","my_sol_primefac.py"),
    2: ("Identify a Palindrome","my_sol_palindrome.py"),
    3: ("Sort a String","my_sol_sortW.py"),
    4: ("Find All List Items","my_sol_index_all.py"),
    5: ("Play the Waiting Game","my_sol_WG.py"),
    6: ("Save a Dictionary","my_sol_dictionary.py"),
    7: ("Schedule a Function","my_solv_schedule.py"),
    8: ("Send an Email","my_sol_send_email.py"),
    9: ("Simulate Dice","my_sol_dice.py"),
    10: ("Count Unique Words","my_sol_count_words.py"),
    11: ("Generate a Password","my_sol_diceware.py"),
    12: ("Merge CSV Files","my_sol_merge_csv.py"),
    13: ("Solve a Sudoku","my_sol_Sudoku.py"),
    14: ("Build a Zip Archive","zip_all.py"),
    15: ("Download Sequential Files","download_files.py")
}
def display_menu():
    print(f"\n{'=' * 55}")
    print("LEVEL UP: PYTHON - SECURE TOOLKIT ROUTER")
    print(f"{'=' * 55}")
    for num, (name,) in CHALLENGE_MAP.items():
        print(f"[{num:2d}] {name}")
    print(f"[ 0] Exit Dashboard")
    print(f"{'=' * 55}")

def run_script(script_name):
    script_path = os.path.join(CHALLENGES_DIR,script_name)
    if not os.path.exits(script_path):
        print(f"\n[Vulnerability/Error]: Operational file target not found: {script_path}")
        print("Verify your file name inside your 'challenges/' folder matches the router settings")
        return
    print(f"\n Initializing: {script_name}...")
    print(f"{'_' * 45}")
    try:
        # Executes target code block under an isolated system fork with native telemetry pass-through
        subprocess.run([sys.executable,script_path],check=True)
    except subprocess.CalledProcessError as e:
        print(f"Process raised an error:{e}")
    except KeyboardInterrupt:
        print("\n Execution terminated by operator interface command!")
    print("Script successfully executed!!!")
    print(f"{'_'} * 45")

def main():
    while True:
        display_menu()
        try:
            choice = input("Select rotine profile to execute (0-15):").strip()
            if not choice.isdigit() or not(0<= int(choice) <=15):
                print("Invalid Input! Enter an integer value from 0 to 15 only!")
                continue
            selection = int(choice)
            if selection == 0:
                print("Session context closed securely, Goodbye!")
                break
            elif selection in CHALLENGE_MAP:
                run_script(CHALLENGE_MAP[selection][1])
        except (KeyboardInterrupt,EOFError):
            print("\n System Escape Initiated. Closing Engine!")
            break

if __name__ == "__main__":
    main()