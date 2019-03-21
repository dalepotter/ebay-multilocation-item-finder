import datetime
import os
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

search_keywords = [
    'brompton',
    '(bike, cycle) trailer',
    'sack truck',
    'tile cutter'
]

stations = [
    ('Office', os.environ['OFFICE_POSTCODE'], 20),
    ('Plymouth', 'PL4 6AB', 20),
    ('Ivybridge', 'PL21 0DQ'),
    ('Totnes', 'TQ9 5JR'),
    ('Newton Abbot', 'TQ12 2JE'),
    ('Teignmouth', 'TQ14 8PG'),
    ('Dawlish', 'EX7 9PJ'),
    ('Dawlish Warren', 'EX7 0NF'),
    ('Starcross', 'EX6 8PA'),
    ('Exeter St Thomas', 'EX4 1AJ'),
    ('Exeter St Davids', 'EX4 4NT', 20),
    ('Tiverton Parkway', 'EX16 7EH'),
    ('Taunton', 'TA1 1QP'),
    ('Bridgwater', 'TA6 5HB'),
    ('Highbridge & Burnham', 'TA9 3BT'),
    ('Weston-super-Mare', 'BS23 1XY'),
    ('Weston Milton', 'BS22 8PF'),
    ('Worle', 'BS22 6WA'),
    ('Yatton', 'BS49 4AJ'),
    ('Nailsea & Backwell', 'BS48 3LH'),
    ('Parson Street', 'BS3 5PU'),
    ('Bedminster', 'BS3 4LU'),
    ('Bristol Temple Meads', 'BS1 6QF', 20),
    ('Home', os.environ['HOME_POSTCODE'], 20)
]


api = Connection(
        appid='DP1dc611a-5511-41c1-b35e-99291acf532',
        siteid='EBAY-GB',
        config_file=None
)

for keyword in search_keywords:
    for station in stations:
        station_name = station[0]
        postcode = station[1]
        max_distance = '5'
        try:
            max_distance = str(station[2])
        except IndexError:
            pass

        try:
            api_payload = {
                    'keywords': keyword,
                    'itemFilter': [
                        {'name': 'Condition',
                         'value': 'Used'},
                        {'name': 'ListingType',
                         'value': 'Auction'},
                        {'name': 'MaxDistance',
                         'value': max_distance},
                        {'name': 'LocalPickupOnly',
                         'value': True},
                        # {'name': 'SoldItemsOnly',
                        #  'value': True}
                    ],
                    'buyerPostalCode': postcode
                }

            # Search for listings
            response = api.execute('findItemsAdvanced', api_payload)
            #  findCompletedItems

            assert(response.reply.ack == 'Success')
            assert(type(response.reply.timestamp) == datetime.datetime)
            assert(type(response.dict()) == dict)

        except ConnectionError as e:
            print(e)
            print(e.response.dict())

        print("Search keyword: {} - Station: {} - Results {}".format(
            keyword,
            station,
            response.reply.searchResult._count
        ))

        if int(response.reply.searchResult._count) > 0:
            print(response.reply.itemSearchURL)
