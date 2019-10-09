from github import Github

"""
list all notes
create new note
edit note
delete note
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
    guser = user(login, password)
    guser.list_all_notes()


if __name__ == "__main__":
    main()
