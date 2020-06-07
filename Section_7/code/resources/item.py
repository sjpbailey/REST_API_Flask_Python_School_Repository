from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item need a store id."
    )
  
  
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'messane': 'Items not found'}, 404    

    def post(self, name): 
        if ItemModel.find_by_name(name):
            return{'message': "An item with name '{}' already exisits".format(name)}, 400 

        data = Item.parser.parse_args()    

        item = ItemModel(name, **data) #or ItemModel(name, data['price'], data['store_id']) 
        
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500     

        return item.json(), 201  

    #@jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item Deleted'}      
        return{'message': 'Item not found.'}, 404


    #@jwt_required()
    def put(self, name):    
        data = Item.parser.parse_args()
        
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data) #or ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price'], data['store_id']
        #if item:
            item.price = data['price']
        #else:
        #    item = ItemModel(name, **data)    
        
        item.save_to_db() 

        return item.json()


class ItemList(Resource):   
    def get(self):
        return {'items': [x.json() for x in ItemModel.query.all()]} # List comprehention
        #return {'items': list(map(lambda  x: x.json(), ItemModel.query.all())) } # Lambda 'map is used in other languages'