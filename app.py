from flask import Flask
from models import db
from config import DevelopmentConfig, ProductionConfig
 
app = Flask(__name__)
db.init_app(app)
app.config.from_object(DevelopmentConfig)
 
@app.route('/')
def hello_whale():
    return 'Whale, Hello there!'
 
if __name__ == '__main__':

    with app.app_context():
        db.drop_all()
        db.create_all()

    app.run(debug=True, host='0.0.0.0', port=8080)