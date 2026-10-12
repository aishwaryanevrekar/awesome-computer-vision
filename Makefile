.PHONY: setup check test render links demo clean

PY ?= python3

setup:
	$(PY) -m pip install -r examples/requirements.txt

render:
	$(PY) scripts/catalog.py render

check:
	$(PY) scripts/check_repository.py

test:
	$(PY) -m unittest discover -s tests -v

links:
	$(PY) scripts/check_external_links.py

demo:
	$(PY) examples/image_processing.py
	$(PY) examples/digits_baseline.py
	$(PY) examples/image_retrieval.py --demo

clean:
	rm -rf outputs .pytest_cache
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
