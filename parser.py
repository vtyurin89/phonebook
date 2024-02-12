import argparse

from models import UserEntry


def get_creation_arguments() -> argparse.ArgumentParser:
    base_user_arguments = argparse.ArgumentParser(add_help=False)
    for argument in UserEntry.__slots__:
        base_user_arguments.add_argument(f'--{argument}', required=True)
    return base_user_arguments


def get_search_arguments() -> argparse.ArgumentParser:
    base_user_arguments = argparse.ArgumentParser(add_help=False)
    for argument in UserEntry.__slots__:
        base_user_arguments.add_argument(f'--{argument}')
    return base_user_arguments


def get_edit_and_delete_arguments() -> argparse.ArgumentParser:
    base_user_arguments = argparse.ArgumentParser(add_help=False)
    base_user_arguments.add_argument('--personal_phone')
    return base_user_arguments


class CommandParser:
    def __init__(self):

        self.parser = argparse.ArgumentParser(description="Phone book management")
        self.subparsers = self.parser.add_subparsers(title="commands", dest="command")

        creation_arguments = get_creation_arguments()
        search_arguments = get_search_arguments()
        create_and_delete_arguments = get_edit_and_delete_arguments()
        self.user_add = self.subparsers.add_parser("adduser", parents=[creation_arguments],
                                                   help="Add a new entry to the phonebook.")
        self.user_add = self.subparsers.add_parser("edituser", parents=[search_arguments],
                                                   help="Edit entry with specified personal phone number.")
        self.user_add = self.subparsers.add_parser("filter", parents=[search_arguments],
                                                   help="Search for entries in the phonebook.")
        self.user_add = self.subparsers.add_parser("listusers", help="List all entries in the phonebook.")
        self.user_add = self.subparsers.add_parser("deleteuser", parents=[create_and_delete_arguments],
                                                   help="Delete an entry with specified personal phone number.")

    @staticmethod
    def filter_args(args):
        return {key: value for key, value in args.items() if value is not None}

    def _add_user_entry(self, args):
        user_entry = UserEntry(**args)
        if user_entry.already_exists():
            raise ValueError("Entry with this personal phone already exists.")
        user_entry.save_to_file()

    def _edit_user_entry(self, args):
        filtered_args = self.filter_args(args)
        if len(filtered_args) == 0:
            raise ValueError("No filters provided!")
        user_entry = UserEntry(**args)
        print("Editing user:", filtered_args)

    def _filter_user_entries(self, args):
        filtered_args = self.filter_args(args)
        if len(filtered_args) == 0:
            raise ValueError("No filters provided!")
        print("Filtering users based on specified parameters:", filtered_args)
        UserEntry.return_filtered_entries(filtered_args)

    def _list_user_entries(self) -> None:
        UserEntry.return_all_entries()

    def _delete_user(self, args) -> None:
        if args['personal_phone'] is None:
            raise ValueError('Please provide the personal_phone number of the entry you want to delete.')
        print("Deleting user: ", args)

    def run(self):
        args = self.parser.parse_args()
        self.args = vars(args)
        command = self.args.pop("command")
        if command == 'adduser':
            self._add_user_entry(self.args)
        elif command == 'edituser':
            self._edit_user_entry(self.args)
        elif command == 'filter':
            self._filter_user_entries(self.args)
        elif command == 'listusers':
            self._list_user_entries()
        elif command == 'deleteuser':
            self._delete_user(self.args)


