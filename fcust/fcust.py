"""Main module.

Dev Notes:

https://stackabuse.com/python-check-if-file-or-directory-is-empty/
from pathlib import Path
print(Path(emptydirectory).iterdir()) # <generator object Path.iterdir at 0x7f2cf6f584a0>
# Using next(), we are trying to fetch next available item.
# With None as the default return item, next() won't raise a StopIteration exception
# in case there is no item in the collection:
print(next(Path(emptydirectory).iterdir(), None))
# None
print(next(Path(nonemptydirectory).iterdir(), None))
# /mnt/f/code.books/articles/python/code/file_dir.py


https://docs.python.org/3/library/stat.html#module-stat
stat.S_ISDIR(mode): Return non-zero if the mode is from a directory.


https://stackoverflow.com/a/61328376/1904901
from pathlib import Path
fl = Path("file_name")
fl.chmod(0o444)

"""

from pathlib import PosixPath  # , Path


class CommonFolder:
    """

    Main class regarding management of a folder that is commonly used across many users.

    :param folder_path: Path where the common folder is located.
    :param common_group: Group name regarding the common folder.
      If not passed the existing group of the folder will be assumed to be the proper folder.
    """

    def __init__(self, folder_path: PosixPath, common_group: str = ""):
        """
        Initialize CommonFolder class.
        """

        if not isinstance(folder_path, PosixPath):
            raise TypeError(f"Expected PosixPath object instead of {type(folder_path)}")

        if not folder_path.exists():
            raise FileNotFoundError(
                "Folder is expected to be present when the class is initialized."
            )

        self.path: PosixPath = folder_path

        if common_group == "":
            # TODO: Add warning when logging gets added.
            self.group: str = self.path.group()
        else:
            self.group = common_group


def enforce_content_permissions():
    """
    We read the contents of a specified directory and enforce unix permissions.

    Files should have 664 permissions
    Folders should have 2775 permisions (ie also setguid bit)
    Group should be common golder's group.
    """
