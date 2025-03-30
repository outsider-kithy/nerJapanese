from flask import Flask

app = Flask(__name__)

def create_app():
	
	from hello import views as hello_views
	app.register_blueprint(hello_views.hello, url_prefix="/hello")

	from api import views as api_views
	app.register_blueprint(api_views.api, url_prefix="/api")

	return app

