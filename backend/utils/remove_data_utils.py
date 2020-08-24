from backend.utils.get_data_utils import get_groups_data
from backend.utils.get_path_utils import get_group_data_file_path


def remove_group_data(line: int):

    get_groups_data().remove(get_groups_data()[line])







