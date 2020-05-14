import urllib.request,json
from .models import Food
# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def process_results(food_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        food_list: A list of dictionaries that contain food details
    Returns :
        food_results: A list of food objects
    '''
    food_results = []
    for food_item in food_list:
        id = food_item.get('id')
        name = food_item.get('name')
        description = food_item.get('description')
        image = food_item.get('image')
       

        if image:
            food_object = Food(id,name,description,image)
            food_results.append(food_object)

    return food_results