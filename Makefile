install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	pylint --disable=R,C,line-too-long --ignore-patterns=test_.*?py *.py 
	#ruff linting is 10-100X faster than pylint
	#ruff check *.py
	

build_docker:
	docker build -t flask-app:latest .

run_docker:
	docker run -p 5000:5000 flask-app:latest

stop_docker:
	docker stop flask-app

clean_docker:
	docker rm flask-app
	docker rmi flask-app:latest

deploy: build_docker run_docker open