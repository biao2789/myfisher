import json
from app import create_app
app = create_app()

if __name__ == '__main__':
	#生产环境    nginx+uwsgi
	#如果没有if语句，在生产模式下，会使用nginx+uwsgi启动一个web服务，app.run也会启动一个，导致冲突
	app.run(debug=True)
