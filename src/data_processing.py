import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

nyc_res = pd.read_csv('data/NYC_restaurants_orders/food_order.csv')
food_delivery = pd.read_csv('data/food_delivery/test.csv')
print(nyc_res.info())
print(food_delivery.info())

