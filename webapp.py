from app import app,db
from app.models import User,Poll,Option,Behaviour

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Poll': Poll,'Option':Option,'Behaviour':Behaviour}
