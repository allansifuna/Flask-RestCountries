[![Requirements Status](https://requires.io/github/allansifuna/Flask-RestCountries/requirements.svg?branch=main)](https://requires.io/github/allansifuna/Flask-RestCountries/requirements/?branch=main)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/95668732c0014077abf06e7826c1becf)](https://www.codacy.com/manual/allansifuna/Flask-RestCountries?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=allansifuna/Flask-RestCountries&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/allansifuna/Flask-RestCountries/badge.svg?branch=main)](https://coveralls.io/github/allansifuna/Flask-RestCountries?branch=main)

# Flask-RestCountries
Flask - RestCountries provides a simple intergration for [restcountries.eu](https://restcountries.eu) API with Flask Applications.

# Installation

Use the package manager[pip](https://pip.pypa.io/en/stable/) to install flask-restcountries.

```bash
pip install Flask-RestCountries
```

# Usage

```python
from flask import Flask
from flask_restcountries import CountriesAPI

app = Flask(__name__)


rc = CountriesAPI(app)
```


# if you are using blueprints
```python
from flask_restcountries import CountriesAPI
rc = CountriesAPI()

rc.init_app(app)
```

## Usage in App
```python


@app.route('/get-all')
def get_all_countries():
    """all_countries is a list of Country Objects"""
    all_countries = rc.get_all()
    return render_template("example.html", all_countries=all_countries)


```
# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## Tests and Examples

Examples are comming soon!.
# License
[MIT](https://github.com/allansifuna/Flask-RestCountries/blob/main/LICENSE)
