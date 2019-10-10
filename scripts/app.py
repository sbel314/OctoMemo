from github import Github

"""
TODO:
    - list all notes
    - create new note
    - edit note
    - delete note
"""


class user:
    def __init__(self, login, password):
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

    def create_note(self, path, content, message="none"):
        repo = self.auth.get_user().get_repo("octomemo_" + self._login)
        repo.create_file(path, message, content)

    def remove_note(self):
        repo = self.auth.get_user().get_repo("octomemo_" + self._login)
        repo.delete_file(path, message, sha)

    def edit_note(self, path, sha, message="Removing file"):
        pass


def main():
    print(
        """
        | GitNote |
        | ---o--- |
        | ------- |
        | ---m--- |
        | ------- |
        | ---g--- |
    """
    )
    login = input("please enter your login:")
    password = input("please enter your password:")
    new_user = user(login, password)
    print(
        """
    1 - List all notes
    2 - Create new note
    3 - Edit note
    4 - Delete note
    5 - Exit
    """
    )
    option = input(">")


if __name__ == "__main__":
    main()
