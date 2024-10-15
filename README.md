## Steps to run the publish/subscribe tests


# First activate virtual environment:
.\venv\Scripts\activate

# Second install the required packages by running:
pip install -r ./requirements.txt

# Third run the end to end test:
pytest .\tests\test_message.py

# Finally deactivate the virtual env:
.\venv\Scripts\deactivate