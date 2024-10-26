linter:
	poetry run flake8

Setup:
	poetry install

start-debug:
	flask --app flesk-unit-converter/app --debug run --port 8000

start:
	poetry run gunicorn --workers=2 --bind=127.0.0.1:8000 'flesk-unit-converter.wsgi-gunicorn:create_app()'