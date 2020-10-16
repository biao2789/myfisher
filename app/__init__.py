
from flask import Flask


def create_app():
	app = Flask(__name__)
	app.config.from_object("app.secure")
	app.config.from_object("app.setting")
	# print(app.config["DEBUG"])

	register_blueprint(app)
	return app

def register_blueprint(app):
	from app.blueprint.book import book_bp
	app.register_blueprint(book_bp)