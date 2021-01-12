from model.group_stations import Stations
from model.station_22_in_ukr_lang import station_list_22
import random
import os.path
import jsonpickle



testdata = [
    Stations(from_station=random.choice(station_list_22), to_station=random.choice(station_list_22))
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

#with open(file, "w", encoding='utf-8') as out:
#    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2, ensure_ascii=False))

with open(file, "w", encoding='utf-8') as out:
    jsonpickle.set_encoder_options("json", indent=2, ensure_ascii=False)
    out.write(jsonpickle.encode(testdata))



words_list = {

}