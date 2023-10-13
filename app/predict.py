import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

def get_model():
        dataset = pd.read_csv(os.path.join(BASE_DIR, 'app/data/food_prices_encoded.csv'))

        X = dataset.drop(['price(MZN)'], axis=1)
        y = dataset['price(MZN)']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        return model

def predict_food_price(model, data):

    # create a DataFrame with the commodity's data
    commodity_df = pd.DataFrame.from_dict(data)

    # make the prediction based on the commodity's data
    predicted_price = model.predict(commodity_df)

    return predicted_price[0]


def get_commodity_data(params):

    commodity_data = {}

    year = int(params['year'])
    month = int(params['month'])
    province = int(params['province'])
    category = int(params['category'])
    product = int(params['product'])

    pronvices = [
        'province_Cabo_Delgado',
        'province_Gaza',
        'province_Inhambane',
        'province_Manica',
        'province_Maputo',
        'province_Maputo City',
        'province_Nampula',
        'province_Niassa',
        'province_Sofala',
        'province_Tete',
        'province_Zambezia',
    ]

    categories = [
        'category_cereals and tubers',
        'category_meat, fish and eggs',
        'category_miscellaneous food',
        'category_oil and fats',
        'category_pulses and nuts',
        'category_vegetables and fruits',
    ]

    products = [
        'commodity_Beans (butter)_KG',
        'commodity_Beans (catarino)_KG',
        'commodity_Beans (dry)_KG',
        'commodity_Beans (magnum)_KG',
        'commodity_Cabbage_KG',
        'commodity_Carrots_KG',
        'commodity_Cassava (dry)_KG',
        'commodity_Cassava flour_KG',
        'commodity_Cassava leaves_KG',
        'commodity_Coconut_Unit',
        'commodity_Cowpeas_KG',
        'commodity_Eggs_30 pcs',
        'commodity_Fish_500 G',
        'commodity_Garlic_KG',
        'commodity_Groundnuts (Mix)_KG',
        'commodity_Groundnuts (large, shelled)_KG',
        'commodity_Groundnuts (small, shelled)_KG',
        'commodity_Groundnuts_KG',
        'commodity_Kale_KG',
        'commodity_Maize (white)_KG',
        'commodity_Maize meal (white, first grade)_KG',
        'commodity_Maize meal (white, with bran)_KG',
        'commodity_Maize meal (white, without bran)_KG',
        'commodity_Maize meal_25 KG',
        'commodity_Oil (vegetable)_5 L',
        'commodity_Oil (vegetable, imported)_L',
        'commodity_Oil (vegetable, local)_L',
        'commodity_Onions_KG',
        'commodity_Potatoes_KG',
        'commodity_Rice (imported)_KG',
        'commodity_Rice (local)_KG',
        'commodity_Rice_25 KG',
        'commodity_Rice_KG',
        'commodity_Salt (iodised)_KG',
        'commodity_Sugar (brown, imported)_KG',
        'commodity_Sugar (brown, local)_KG',
        'commodity_Sugar_KG',
        'commodity_Sweet potatoes_KG',
        'commodity_Tomatoes_KG',
        'commodity_Wheat flour (local)_KG',
    ]

    #
    commodity_data = {
        'year': [year],
        'month': [month],
    }

    for i in range(len(pronvices)):
        if (i + 1) == province:
            commodity_data[pronvices[i]] = [1]
        else:
            commodity_data[pronvices[i]] = [0]

    for i in range(len(categories)):
        if (i + 1) == category:
            commodity_data[categories[i]] = [1]
        else:
            commodity_data[categories[i]] = [0]

    for i in range(len(products)):
        if (i + 1) == product:
            commodity_data[products[i]] = [1]
        else:
            commodity_data[products[i]] = [0]

    return commodity_data
