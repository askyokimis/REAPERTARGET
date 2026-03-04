import json
import time

COMMAND_FILE = "commands.json"

def get_commands():
    try:
        with open(COMMAND_FILE, "r") as f:
            data = json.load(f)
        return data.get("commands", [])
    except Exception as e:
        print("Error reading commands.json:", e)
        return []

def clear_commands():
    with open(COMMAND_FILE, "w") as f:
        json.dump({"commands": []}, f)

def process_command(command):
    print(f"Processing command: {command}")
    # Burada MCP veya Reaper API'ye komut gönderme kodu gelecek

while True:
    commands = get_commands()
    if commands:
        for cmd in commands:
            process_command(cmd)
        clear_commands()
    time.sleep(1)
