from github import Github
import getpass

"""
TODO:
    - list all notes
    - create new note
    - edit note
    - delete note
"""


class user:
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

    def delete_note(self, nome):
        repo = self.auth.get_user().get_repo("octomemo_" + self._login)
        repo.delete_file(nome, message="deleting file", sha)

    def edit_note(self, path, sha, message="Removing file"):
        pass


def main():
    login = input("please enter your login:")
    password = getpass.getpass("Enter your password: ")
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
    while 1:
        option = int(input(">"))
        if option == 1:
            new_user.list_all_notes()
        elif option == 2:
            name = input("name of note:")
            text = input("text:")
            new_user.create_note(name, content=text)
            print("Sucessfully created note!")
        elif option == 3:
            new_user.edit_note()
        elif option == 4:
            new_user.delete_note()
        elif option == 5:
            exit()
        else:
            print("Invalid input, try again.")


if __name__ == "__main__":
    main()
