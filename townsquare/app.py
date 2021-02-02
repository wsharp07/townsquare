from flask import Flask, render_template
from townsquare.services.scoreboard import Scoreboard

def create_app():
    application = Flask(__name__)

    @application.route('/')
    def index():
        model = Scoreboard().generate()
        return render_template('index.html', model=model)

    return application

if __name__ == "__main__":
    application = create_app()
    application.run()

