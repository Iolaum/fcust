#!/usr/bin/env python3

"""Tests for `fcust` package."""

import pytest

# import mock
import tempfile
from pathlib import Path, PurePath
from click.testing import CliRunner
from fcust.fcust import CommonFolder
from fcust import cli


class TestCommonFolder:
    def setup_class(cls):
        cls.folder = Path(tempfile.mkdtemp())
        # populate folder
        f1 = PurePath.joinpath(cls.folder, "file1.txt")
        with f1.open(mode="w") as fh:
            fh.write("file1")
        f2 = PurePath.joinpath(cls.folder, "file2.txt")
        with f2.open(mode="w") as fh:
            fh.write("file2")
        PurePath.joinpath(cls.folder, "folder").mkdir()
        f3 = PurePath.joinpath(cls.folder, "folder", "file3.txt")
        with f3.open(mode="w") as fh:
            fh.write("file3")
        cls.group = cls.folder.group()
        cls.owner = cls.folder.owner()

    def test_init_folder_type(self):
        """
        Basic testing.
        """

        with pytest.raises(TypeError) as exc:
            test_path = "hi"
            CommonFolder(folder_path=test_path)

        assert str(exc.value) == (
            f"Expected PosixPath object instead of {type(test_path)}"
        )

    def test_init_folder_exists(self):
        """
        Basic testing.
        """

        with pytest.raises(FileNotFoundError) as exc:
            test_path = Path("nothere")
            CommonFolder(folder_path=test_path)

        assert str(exc.value) == (
            "Folder is expected to be present when the class is initialized."
        )

    def test_init_group(self):
        """
        Basic testing.
        """

        cf = CommonFolder(self.folder)
        assert cf.group == self.group


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "fcust.cli.main" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
