import click


@click.group()
def main():
    pass


@main.command()
def login():
    pass


@main.command()
def logout():
    pass


@main.command('id')
def identity():
    pass


@main.command()
def serve():
    from .jellygram import serve_bot
    serve_bot()


@main.command()
def bootstrap():
    pass
