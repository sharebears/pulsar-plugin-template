lint:
	isort -rc .

tests:
	flake8
	mypy --no-strict-optional plugin_name/
	pytest --cov-report term-missing --cov-branch --cov=plugin_name tests/

.PHONY: lint tests
