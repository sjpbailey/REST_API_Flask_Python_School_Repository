from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
    {
          'name': 'My Wonderful Store',
          'items': [
              {
              'name': 'My Item',
              'price': 15.99,
              
              }    
         ]   
    }

]

@app.route('/') #'http://www.google.com/'  
def home():
    return render_template('index.html')

# POST - Used to receive data         # A browser will use POST to send us data and GET to receive data
# GET - Used to send back data only   # A Server will use POST to receive data (to deal with) and GET to send data

# POST /store data: {name:}                       # creates a new store with a given name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'item':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>                        # is going to GET a store with a given name and return data about it
@app.route('/store/<string:name>')                # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
   
   for store in stores:                              # iterate over stores
       if store['name'] == name:                     # if store name matches, return it
           return jsonify(store)
   return jsonify({'message': 'Store not found'})    # if none match, return an error message       

    

# GET /store                                      # is going to give a list of all the stores
@app.route('/store')                
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {namer:, price:} # create an item inside a specific store with a given name
@app.route('/store/<string:name>/item', methods=['POST'])                
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']

            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found'})

# GET - /store/<string:name>/item                 # GET all items in a store 
@app.route('/store/<string:name>/item', methods=['GET'])                
def get_item_in_store(name):
    for store in stores:
           if store['name'] == name:
               return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'})       



app.run(port=5000)
