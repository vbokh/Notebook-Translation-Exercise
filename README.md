# Notebook-Translation-Exercise
Setup
Create virtual environment:

conda create -n ump-env python=3.11
Activate the environment:

conda activate ump-env
Install packages:

#pip install requests
#pip install plotly
#pip install python-dotenv

# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt
Obtain an API Key from Alphavantage. Then create a ".env" file in the root directory of the repo, and paste some contents in like this, but using your own api key:

# this is the ".env" file:

ALPHAVANTAGE_API_KEY="__________"
Usage
Unemployment report:

python -m app.unemployment
Stocks report:

python -m app.stocks
Run the web app (then view in the browser at http://localhost:5000/):

# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
Testing
Run tests:

pytest
