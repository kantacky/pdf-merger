.PHONY: install
install:
	python -m venv venv && \
	. ./venv/bin/activate && \
	pip install -Ur requirements.txt

.PHONY: merge
merge:
	. ./venv/bin/activate && \
	python main.py --odd $(ODD) --even $(EVEN) --out $(OUT)
