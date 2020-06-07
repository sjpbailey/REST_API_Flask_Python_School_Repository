from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
        )

  
  
   #@jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'messane': 'Items not found'}, 404
    
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))  
        row = result.fetchone()
        connection.close()

        if row:
            return {'item':{'name': row[0], 'price': row[1]}}
#####CREATE#####
    def post(self, name): 
        if self.find_by_name(name):
            return{'message': "An item with name '{}' already exisits".format(name)}, 400 #check duplication

        data = Item.parser.parse_args()    #parce the data using the parcer checks for price

        item = {'name': name, 'price': data['price']} #creat a JSON of the item
        
        try:
            Item.insert(item)
        except:
            return {"message": "An error occurred inserting the item."}, 500 # Internal server error    

        return item, 201 

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db') #opens connection to data.db
        cursor = connection.cursor()            #gives ability to write to data.db

        query = "INSERT INTO items VALUES (?, ?)"             #gets specific parced data
        cursor.execute(query, (item['name'], item['price']))  #used to insert into the database

        connection.commit() #writes to data.db
        connection.close()  #closes connection
 
#####DELETE#####
    #@jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('data.db') #opens connection to data.db
        cursor = connection.cursor()            #gives ability to write to data.db

        query = "DELETE FROM items WHERE name=?" #deletes called item in database
        cursor.execute(query, (name,))  #used to the item to delete in database

        connection.commit() #writes to data.db
        connection.close()  #closes connection
        
        return {'message': 'Item deleted'}
#####PUT#####
    #@jwt_required()
    def put(self, name):    
        data = self.parser.parse_args()
        item = self.find_by_name(name)   #define item
        updated_item = {'name': name, 'price': data['price']} #JSON for items to update
        if item is None:
            try:
                Item.insert(updated_item)
            except:
                return {"message": "An error occured inserting the item."}, 500
        else:
            try:
                Item.update(updated_item)
            except:
                return {"message": "An error occured updating the item."}, 500
        return updated_item
#####UPDATE#####
    @classmethod
    def update(cls, item):    
       connection = sqlite3.connect('data.db') #opens connection to data.db
       cursor = connection.cursor()            #gives ability to write to data.db

       query = "UPDATE items SET price=? WHERE name=?" #updates item in database
       cursor.execute(query, (item['price'], item['name']))  #used update in database

       connection.commit() #writes to data.db
       connection.close()  #closes connection

#####READ#####
class ItemList(Resource):   
    def get(self):
        connection = sqlite3.connect('data.db') #opens connection to data.db
        cursor = connection.cursor()            #gives ability to write to data.db

        query = "SELECT * FROM items" #return all items in database
        result = cursor.execute(query)  #grab data in database
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})    

        connection.close()  #closes connection

        return {'items': items}