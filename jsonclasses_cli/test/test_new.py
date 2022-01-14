from __future__ import annotations
from unittest.mock import patch
from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
from ..new import new


class TestNew(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.temp_dir = TemporaryDirectory()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp_dir.cleanup()

    def setUp(self) -> None:
        self.temp_path = Path(str(self.temp_dir.name)) / "new_app"


    def test_new_create_all_filed(self) -> None:
        new(self.temp_path, None, None, None, None, None, True)
        app = Path(self.temp_path) / 'app.py'
        requirements = Path(self.temp_path) / 'requirements.txt'
        config = Path(self.temp_path) / 'config.json'
        mypy = Path(self.temp_path) / 'mypy.ini'
        gitignore = Path(self.temp_path) / '.gitignore'
        read_me = Path(self.temp_path) / 'README.md'
        self.assertTrue(app.is_file(), app.name)
        self.assertTrue(requirements.is_file(), requirements.name)
        self.assertTrue(config.is_file(), config.name)
        self.assertTrue(mypy.is_file(), mypy.name)
        self.assertTrue(gitignore.is_file(), gitignore.name)
        self.assertTrue(read_me.is_file(), read_me.name)

    # @patch('builtins.input', side_effect=['Yes', 'Yes', 'Yes', 'Yes'])
    # def test_new_create_app_filed_without_user_and_admin(self, stdout) -> None:
    #     chdir(Path(str(self.temp_dir.name)))
    #     runner = CliRunner()
    #     result = runner.invoke(command_new, ["name"])
    #     print(result.stderr_bytes, stdout.gevalue())
