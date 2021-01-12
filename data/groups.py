
from model.group_stations import Stations
from model.station_22_in_ukr_lang import station_list_22
import random


testdata = [
    Stations(from_station=random.choice(station_list_22), to_station=random.choice(station_list_22))
]

