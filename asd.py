import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def interpret_line(line):
    line = line.strip()
    if not line or line.startswith('#'):
        return  # Skip comments or empty lines

    parts = line.split()

    cmd = parts[0]
    args = parts[1:]

    if cmd == "START_WSL":
        user = args[0] if args else "default"
        run_command(f'wsl -u {user}')
    elif cmd == "EXECUTE":
        command = " ".join(args)
        run_command(command)
    elif cmd == "EXIT":
        print("Exiting script.")
        exit()
    else:
        print(f"Unknown command: {cmd}")

def run_script(filename):
    with open(filename, 'r') as f:
        for line in f:
            interpret_line(line)

if __name__ == "__main__":
    script_file = "myscript.np"  # Your custom script file
    run_script(script_file)