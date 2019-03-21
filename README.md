# Ebay Multilocation Item Finder

Searches the ebay API for items located within a set of postcodes using the [ebaysdk-python](https://github.com/timotheus/ebaysdk-python).

Search keywords and location postcodes are definted within `itemfinder.py`.


## Set-up

This is built using python 3.6.

```
# Clone the repository
git clone https://github.com/dalepotter/ebay-multilocation-item-finder.git
cd ebay-multilocation-item-finder

# Set up and activate a virtual environment
python3 -m venv pyenv
source pyenv/bin/activate

# Download requirements
pip install -r requirements.txt

# Set environment variables
export OFFICE_POSTCODE='ENTER POSTCODE'
export HOME_POSTCODE='ENTER POSTCODE'
```

## Running the item finder
```
python itemfinder.py
```


## Future work

### Release 1:
Email a list of found items to a given email address - possible email template in `email-template.txt`.

### Release 2:
Add distance from station to seller postcode after the item title - approaches here: https://stackoverflow.com/questions/44176381/calculate-road-travel-distance-between-postcodes-zipcodes-python

### Release 3:
Show new items only - implies storing item nos parsed

### Release 4:
Remove duplicate locations, only showing the item associated with the closest station.
