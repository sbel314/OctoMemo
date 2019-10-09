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


if __name__ == "__main__":
    main()
