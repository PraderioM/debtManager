from backend.utils.get_data_utils import get_groups_data
from backend.utils.get_path_utils import get_group_data_file_path


def remove_group_data(name: str,
                      mailgun_1: str,
                      mailgun_2: str,
                      line: int):

    get_groups_data().remove(line)







