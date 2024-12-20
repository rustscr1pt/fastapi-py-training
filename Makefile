HOST ?= localhost
PORT ?= 8000

run:
	uvicorn main:app --host ${HOST} --port ${PORT} --reload
generate:
	pip freeze > requirements.txt