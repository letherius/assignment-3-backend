from flask import Flask
import json
from config import me
from mock_data import catalog

app = Flask("server")


@app.get("/")
def home():
    return "Hello from Flask"


@app.get("/test")
def test():
    return "This is another endpoint"

@app.get("/about")
def about():
    return "Letherius Miller"    



#############################################
###########   Catalog API ###################
#############################################

@app.get("/api/version")
def version():
    version = {
        "v": "v1.0.4",
        "name": "zombie rabbit"
    }

    # parse a dict into json string
    return json.dumps(version)



# get /api/about
# return me as json

@app.get("/api/about")
def api_about():
    return json.dumps(me)

@app.get("/api/catalog")
def get_catalog():
    return json.dumps(catalog)

# Get /api/test/count
# return the number of products in the list

@app.get("/api/test/count")
def num_of_products():
    return len(catalog)

# GET /api/catalog/<category>
# return all the products that belong to specified category

@app.get("/api/catalog/<category>")
def by_category(category):
    results = []
    category = category.lower()
    for product in catalog:
        if product["category"].lower() == category:
            results.append(product)

    return json.dumps(results)


@app.get("/api/catalog/search/<text>")
def search_by_text(text):
    text = text.lower()
    results = []

    for product in catalog:
        if text in product["title"].lower() or text in product["category"].lower():
            results.append(product)

    return json.dumps(results)


@app.get("/api/categories")
def get_categories():
    results = []
    for product in catalog:
        cat = product["category"]
        if cat not in results:
            results.append(cat)

    return json.dumps(results)



@app.get("/api/test/value")
def total_value():
    total = 0
    for product in catalog:
        total = total + product["price"]

    return json.dumps(total)


@app.get("/api/product/<id>")
def search_by_id(_id):
    for product in catalog:
        if product["_id"] == _id:
            return json.dumps(product)

    return "Error: Product not found"



app.run(debug=True)