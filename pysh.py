import os
import Utils
import Prompt

os.system('cls' if os.name == 'nt' else 'clear')
commandList = []

while True:
    user_input = Prompt.prompt()
    Prompt.run_command(user_input)
