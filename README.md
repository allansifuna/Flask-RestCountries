[![Requirements Status](https://requires.io/github/allansifuna/Flask-RestCountries/requirements.svg?branch=main)](https://requires.io/github/allansifuna/Flask-RestCountries/requirements/?branch=main)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/95668732c0014077abf06e7826c1becf)](https://www.codacy.com/manual/allansifuna/Flask-RestCountries?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=allansifuna/Flask-RestCountries&amp;utm_campaign=Badge_Grade)
[![Coverage Status](https://coveralls.io/repos/github/allansifuna/Flask-RestCountries/badge.svg?branch=main)](https://coveralls.io/github/allansifuna/Flask-RestCountries?branch=main)
![Top language](https://img.shields.io/github/languages/top/allansifuna/Flask-RestCountries)
![Code size](https://img.shields.io/github/languages/code-size/allansifuna/Flask-RestCountries?color=dark-green)
![GitHub](https://img.shields.io/github/license/allansifuna/Flask-RestCountries?color=dark-green)
![PyPI](https://img.shields.io/pypi/v/Flask-RestCountries)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Flask-RestCountries?color=dark-green)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/Flask-RestCountries?color=blue)
![PyPI - Status](https://img.shields.io/pypi/status/Flask-RestCountries)
# Flask-RestCountries
[Flask-RestCountries](https://pypi.org/project/Flask-RestCountries/) provides a simple intergration for [restcountries.eu](https://restcountries.eu) API with Flask Applications.

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

## Other Useful Methods

### Get Countries By Calling Code string of a country. E.g. '254'.
```python
countries=rc.get_countries_by_calling_code("+254")
```

### Get a Country By Alpha code string of a country. E.g. 'ke'.
```python
countries=rc.get_country_by_country_code("ke")
```

### Get Countries By Capital string of a country. E.g. 'Nairobi'
```python
countries=rc.get_countries_by_capital("Nairobi")
```

### Get Countries By Currency string of a country. E.g. 'KES'.
```python
countries=rc.get_countries_by_currency("KES")
```

### Get Countries By Language string of a country. E.g. 'sw'.
```python
countries=rc.get_countries_by_language("sw")
```

### Get Countries By Name string of a country. E.g. 'Kenya'.
```python
countries=rc.get_countries_by_name("Kenya")
```

### Get Countries By Region string of a country. E.g. 'Africa'.
```python
countries=rc.get_countries_by_region("Africa")
```

### Get Countries By Subregion string of a country. E.g. 'Eastern Africa'
```python
countries=rc.get_countries_by_subregion("Eastern Africa")
```

## Response Filtering
To make the response return only afew selected fields, you can filter the response by passing a list
of field to be returned in the filters keyword as a kwarg to the methods above. ie:-

```python
countries=rc.get_countries_by_calling_code("+254",filters=["name","currencies","capital"])
```

## Attributes that can be passed to the filters keyword
    - topLevelDomain
    - alpha2Code
    - alpha3Code
    - currencies
    - capital
    - callingCodes
    - altSpellings
    - relevance
    - region
    - subregion
    - translations
    - population
    - latlng
    - demonym
    - area
    - gini
    - timezones
    - borders
    - nativeName
    - name
    - numericCode
    - languages
    - flag
    - regionalBlocs
    - cioc


## Attributes of the Country object returned per each request
    - top_level_domain
    - alpha2_code
    - alpha3_code
    - currencies
    - capital
    - calling_codes
    - alt_spellings
    - relevance
    - region
    - subregion
    - translations
    - population
    - latlng
    - demonym
    - area
    - gini
    - timezones
    - borders
    - native_name
    - name
    - numeric_code
    - languages
    - flag
    - regional_blocs
    - cioc

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
## Tests and Examples

Examples are comming soon!.
# License
[MIT](https://github.com/allansifuna/Flask-RestCountries/blob/main/LICENSE)
