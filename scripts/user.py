from github import Github
import getpass

"""
TODO:
    - list all notes
    - create new note
    - edit note
    - delete note
"""


class User:
    def __init__(self, login, password):
        """dale."""
        self._login = login
        self._password = password
        self.auth = Github(login, password)

    def create_repo(self):
        self.auth.get_user().create_repo("octomemo_" + self._login, private=True)

    def list_all_notes(self):
        repo = self.auth.get_user().get_repo("octomemo_" + self._login)
        print("Avaiable notes:")
        for file in repo.get_dir_contents(""):
            print(file.name)

    def create_note(self, name, message="none", content=""):
        repo = self.auth.get_user().get_repo("octomemo_" + self._login)
        repo.create_file(name, message, content)

    # def delete_note(self, nome):
    #     repo = self.auth.get_user().get_repo("octomemo_" + self._login)
    #     repo.delete_file(nome, message="deleting file", sha)

    def edit_note(self, path, message="Removing file"):
        pass
