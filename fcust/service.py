"""
Utilities for Folder Custodian Service.
"""

from pathlib import Path, PosixPath


def create_fcust_service_unit(folder_path: PosixPath, unit_path: PosixPath):
    """
    Create a systemd user unit for folder cutodian.
    Use predefined template and modify where needed.

    :param folder_path: Path where the common folder is located.
    :param unit_path: Path where the common folder is located.
    """

    if not isinstance(folder_path, PosixPath):
        raise TypeError(f"Expected PosixPath object instead of {type(folder_path)}")
    if not isinstance(unit_path, PosixPath):
        raise TypeError(f"Expected PosixPath object instead of {type(unit_path)}")

    template = """
    [Unit]
    Description=Folder Custodian Service

    [Service]
    Type=oneshot
    ExecStart=/bin/true
    ExecStop=fcust run $COMMON_FOLDER_PATH

    [Install]
    WantedBy=multi-user.target
    """

    template.replace("$COMMON_FOLDER_PATH", str(folder_path))

    with open(unit_path, "w") as fh:
        fh.write(template)


def create_user_unit_path(create_folder: bool = False):
    """
    We want to add a systemd user unit to run fcust on certain times. In order to do
    this we want to crete a unit at a proper location. According to:
    https://wiki.archlinux.org/index.php/Systemd/User
    our options are:
    - /usr/lib/systemd/user/ where units provided by installed packages belong.
    - ~/.local/share/systemd/user/
      where units of packages that have been installed in the home directory belong.
    - /etc/systemd/user/ where system-wide user units are placed by the system administrator.
    - ~/.config/systemd/user/ where the user puts their own units.
    We opt to use the latter choice.

    This function constructs the proper systemd user unit path where it will be installed.
    It also creates the necessary folder if it doesn't exist.

    :param create_folder: If true create the folder that the unit service will be installed.
    :returns: Path object for the location the unit service will be installed.

    """

    home = Path.home()
    unit_folder_path = home.joinpath(".config", "systemd", "user")
    if create_folder and not unit_folder_path.exists:
        unit_folder_path.mkdir()

    unit_path = unit_folder_path.joinpath("fcust.service")
    return unit_path


# Add function to set up the user service properly
# https://wiki.archlinux.org/index.php/Systemd/User
# https://superuser.com/questions/1037466/how-to-start-a-systemd-service-after-user-login-and-stop-it-before-user-logout/1269158
# https://askubuntu.com/questions/293312/execute-a-script-upon-logout-reboot-shutdown-in-ubuntu/796157#796157

# Add function to start the service

# Add CLI commands for the last two functions
