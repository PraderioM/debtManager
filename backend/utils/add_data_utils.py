from backend.models.group import Group
from backend.utils.get_path_utils import get_group_data_file_path


def add_group_data(name: str, mailgun_1: str, mailgun_2: str ):
    with open(get_group_data_file_path(), 'a') as data_file:
        database = Group.to_database(name, mailgun_1, mailgun_2)
        data_file.writerow(database)
