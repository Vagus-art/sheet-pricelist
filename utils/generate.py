from categoriesService import getCategories
from itemsService import getItems

def generate():
    categories = getCategories()
    generated = []
    for category in categories:
        items = getItems(category['id'])
        generated.append({category['name']:items})
    return generated