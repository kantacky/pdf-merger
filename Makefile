.PHONY: install
install:
	python -m venv venv && \
	. ./venv/bin/activate && \
	pip install -Ur requirements.txt

.PHONY: reverse
reverse:
	. ./venv/bin/activate && \
	python main.py reverse $(IN) $(OUT)

.PHONY: merge
merge:
	. ./venv/bin/activate && \
	python main.py merge $(ODD) $(EVEN) $(OUT)
