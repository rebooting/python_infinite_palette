.PHONY: restore

run:
	python3 main.py ./sample/hats.png > export_palette.clrs
restore:
	pip install -r requirements.txt
test:
	python3 -m unittest ./main_test.py