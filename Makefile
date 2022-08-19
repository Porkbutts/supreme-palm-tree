run:
	uvicorn app.main:app --reload

lint:
	pylint $$(git ls-files '*.py')

test:
	pytest

.PHONY: run lint test