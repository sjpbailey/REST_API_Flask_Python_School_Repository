from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not Found'}, 404
        
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A Store with that name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'A error occured while creating the Store.'}, 500

        return store.json(), 201 
             

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store Deleted'}, 200    


class StoreList(Resource):
    def get(self):
        #return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
        return {'stores': [x.json() for x in StoreModel.find_all()]} #or list and map


