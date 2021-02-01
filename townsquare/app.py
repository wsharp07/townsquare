from flask import Flask, render_template
from townsquare.services.scoreboard import Scoreboard

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        model = Scoreboard().generate()
        return render_template('index.html', model=model)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()

