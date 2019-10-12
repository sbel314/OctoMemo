import click
from user import User


@click.group()
def cli():
    context = click.get_current_context()
    context.obj = {}
    login = input("login:")
    password = input("password:")
    memouser = User(login, password)
    context.obj["memouser"] = memouser


@cli.command()
@click.pass_context
def lnote(context):
    user = context.obj[u"memouser"]
    user.list_all_notes()


@cli.command()
@click.pass_context
def cnote(context):
    user = context.obj[u"memouser"]
    filename = input("filename:")
    text = input("text:")
    user.create_note(filename, text)


if __name__ == "__main__":
    cli()
