# Ebay Multilocation Item Notifier

Searches the ebay API for items located within a set of postcodes using the [ebaysdk-python](https://github.com/timotheus/ebaysdk-python) and sends an email summarising results.

Search keywords and location postcodes are definted within `ebay_multilocation_item_notifier/itemfinder.py`.


## Set-up

This is built using python 3.6.

```
# Clone the repository
git clone https://github.com/dalepotter/ebay_multilocation_item_notifier.git
cd ebay_multilocation_item_notifier

# Set up and activate a virtual environment
python3 -m venv pyenv
source pyenv/bin/activate

# Install as a package
pip install -r requirements.txt

# Set environment variables
export OFFICE_POSTCODE='<Enter postcode>'
export HOME_POSTCODE='<Enter postcode>'
export EMAIL_SENDER_NAME='<Enter sender name>'
export EMAIL_SENDER_ADDRESS='<Enter email sender address>'
export EMAIL_RECIPIENT_NAME='<Enter email recipient name>'
export EMAIL_RECIPIENT_ADDRESS='<Enter email recipient address>'
export EMAIL_SMTP_HOST='<Enter email stmp host>'
export EMAIL_SMTP_USERNAME='<Enter email smtp username>'
export EMAIL_SMTP_PASSWORD='<Enter email smtp password>'
```

## Running the item notifier
```
python ebay_multilocation_item_notifier/itemfinder.py
```


## Tests

Unit tests can be run using Pytest:

```
# Install dev requirements
pip install -r requirements_dev.txt

# Run the tests
pytest
```


## Future work

### Iteration 2:
Add distance from station to seller postcode after the item title - approaches here: https://stackoverflow.com/questions/44176381/calculate-road-travel-distance-between-postcodes-zipcodes-python

### Iteration 3:
Show new items only - implies storing item nos parsed

### Iteration 4:
Remove duplicate locations, only showing the item associated with the closest station.
