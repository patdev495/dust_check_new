import pickle
from datetime import datetime

def dump_pickle_products():
    data = {
    'sum_ok': 0,
    'day_reset': False,
    'night_reset': False,
    # 'last_day_reset': datetime.now().date(),
    }

    with open('data_products.pkl', 'wb') as f:
        pickle.dump(data, f)