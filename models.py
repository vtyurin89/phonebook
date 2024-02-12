import csv
import os
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
            with open(UserEntry.data_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(UserEntry.__slots__)

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

    def get_entry(self, args):
        pass

    @classmethod
    def return_all_entries(cls):
        with open(cls.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)

    @classmethod
    def return_filtered_entries(cls, filtered_args):
        with open(cls.data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row == row | filtered_args:
                    print(row)

    def save_to_file(self):
        with open(self.data_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([getattr(self, attr) for attr in UserEntry.__slots__])
            print("Entry successfully created.")

