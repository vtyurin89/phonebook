import argparse

parser = argparse.ArgumentParser(description="Use the phonebook!")
parser.add_argument("command", metavar='main_command', type=str, help='choose the command for the phonebook')
args = parser.parse_args()

command = args.command
print(command)