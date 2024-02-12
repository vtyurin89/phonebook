import argparse

from models import UserEntry


def get_creation_and_editing_arguments() -> argparse.ArgumentParser:
    base_user_arguments = argparse.ArgumentParser(add_help=False)
    for argument in UserEntry.__slots__:
        base_user_arguments.add_argument(f'--{argument}', required=True)
    base_user_arguments.add_argument('--edit', action='store_const', const=True, default=False,
                                     help='edit entry (default: create new entry)')
    return base_user_arguments


def get_search_arguments() -> argparse.ArgumentParser:
    base_user_arguments = argparse.ArgumentParser(add_help=False)
    for argument in UserEntry.__slots__:
        base_user_arguments.add_argument(f'--{argument}')
    return base_user_arguments


def get_deletion_arguments() -> argparse.ArgumentParser:
    base_user_arguments = argparse.ArgumentParser(add_help=False)
    base_user_arguments.add_argument('personal_phone')
    return base_user_arguments


class CommandParser:
    def __init__(self):

        self.parser = argparse.ArgumentParser(description="Phone book management")
        self.subparsers = self.parser.add_subparsers(title="commands", dest="command")

        creation_and_editing_arguments = get_creation_and_editing_arguments()
        search_arguments = get_search_arguments()
        deletion_arguments = get_deletion_arguments()
        self.subparsers.add_parser("addentry", parents=[creation_and_editing_arguments],
                                                   help="Add a new entry to the phonebook.")
        self.subparsers.add_parser("editentry", parents=[deletion_arguments],
                                                   help="Edit entry with specified personal phone number.")
        self.subparsers.add_parser("filter", parents=[search_arguments],
                                                   help="Search for entries in the phonebook.")
        self.subparsers.add_parser("listentries", help="List all entries in the phonebook.")
        self.subparsers.add_parser("deleteentry", parents=[edit_and_delete_arguments],
                                                   help="Delete an entry with specified personal phone number.")

    @staticmethod
    def filter_args(args):
        return {key: value for key, value in args.items() if value is not None}

    def _add_user_entry(self, args) -> None:
        user_entry = UserEntry(**args)
        if user_entry.already_exists():
            raise ValueError("Entry with this personal phone already exists.")
        user_entry.save_to_file()

    def _edit_user_entry(self, args) -> None:
        if args['personal_phone'] is None:
            raise ValueError('Please provide the personal_phone number of the entry you want to delete.')
        UserEntry.delete_entry(args)

    def _filter_user_entries(self, args) -> None:
        filtered_args = self.filter_args(args)
        if len(filtered_args) == 0:
            raise ValueError("No filters provided!")
        print("Filtering users based on specified parameters:", filtered_args)
        UserEntry.print_filtered_entries(filtered_args)

    def _list_user_entries(self) -> None:
        UserEntry.print_all_entries()

    def _delete_user_entry(self, args) -> None:
        if args['personal_phone'] is None:
            raise ValueError('Please provide the personal_phone number of the entry you want to delete.')
        UserEntry.delete_entry(args)

    def run(self) -> None:
        args = self.parser.parse_args()
        self.args = vars(args)
        command = self.args.pop("command")
        if command == 'addentry':
            self._add_user_entry(self.args)
        elif command == 'editentry':
            self._edit_user_entry(self.args)
        elif command == 'filter':
            self._filter_user_entries(self.args)
        elif command == 'listentries':
            self._list_user_entries()
        elif command == 'deleteentry':
            self._delete_user_entry(self.args)


