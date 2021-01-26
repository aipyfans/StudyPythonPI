from app import create_app, db
from app.model import User, Post, Category

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Category': Category}
