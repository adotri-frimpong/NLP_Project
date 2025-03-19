.PHONY: help setup
.DEFAULT_GOAL = help



help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Install the project's dependencies
	@echo "\nCreating virtual environment...\n"
	@python3 -m venv .venv
	@echo "\nInstalling python dependencies...\n"
	source .venv/bin/activate && pip install --no-cache-dir -r requirements.txt
	@echo "\nInstalling SpaCy and NLTK packages...\n"
	source .venv/bin/activate && python -m spacy download en_core_web_sm
	source .venv/bin/activate && python -m nltk.downloader stopwords
	source .venv/bin/activate && python -m nltk.downloader punkt
	source .venv/bin/activate && python -m nltk.downloader averaged_perceptron_tagger
	source .venv/bin/activate && python -m nltk.downloader brown
	