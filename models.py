import csv
from pathlib import Path


class UserEntry:
    __slots__ = ('last_name', 'first_name', 'middle_name', 'organization', 'work_phone', 'personal_phone')
    data_file = 'phonebook_entries.csv'

    def __init__(self, last_name="", first_name="",
                 middle_name="", organization="", work_phone="", personal_phone=""):
        self.last_name: str = last_name
        self.first_name: str = first_name
        self.middle_name: str = middle_name
        self.organization: str = organization
        self.work_phone: str = work_phone
        self.personal_phone: str = personal_phone

        if not Path(f"./{UserEntry.data_file}").is_file():
            with open(self.data_file, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=UserEntry.__slots__)
                writer.writeheader()

    def already_exists(self) -> bool:
        """
        This method uses personal_phone as primary key to check if the user entry already exists.
        """
        personal_phone_set = set()
        with open(self.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                personal_phone_set.add(row["personal_phone"])
        if self.personal_phone in personal_phone_set:
            return True
        return False

    @classmethod
    def delete_entry(cls, args) -> None:
        updated_entries = []
        entry_found = False

        with open(cls.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row == row | args:
                    entry_found = True
                else:
                    updated_entries.append(row)

        if not entry_found:
            raise ValueError("Entry not found. Process has been cancelled.")
        with open(cls.data_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=UserEntry.__slots__)
            writer.writeheader()
            writer.writerows(updated_entries)
        print("Entry successfully deleted.")

    @classmethod
    def edit_entry(cls, args):
        updated_entries = []
        entry_found = False
        search_phone_part = {'personal_phone': args['personal_phone']}
        with open(cls.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row == row | search_phone_part:
                    entry_found = True
                    updated_entries.append(args)
                else:
                    updated_entries.append(row)

        if not entry_found:
            raise ValueError('Entry with this personal phone not found. Process has been cancelled.')
        with open(cls.data_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=UserEntry.__slots__)
            writer.writeheader()
            writer.writerows(updated_entries)
        print("Entry successfully edited.")

    @classmethod
    def print_all_entries(cls) -> None:
        with open(cls.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)

    @classmethod
    def print_filtered_entries(cls, filtered_args) -> None:
        with open(cls.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row == row | filtered_args:
                    print(row)

    def save_to_file(self) -> None:
        with open(self.data_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([getattr(self, attr) for attr in UserEntry.__slots__])
            print("Entry successfully created.")

