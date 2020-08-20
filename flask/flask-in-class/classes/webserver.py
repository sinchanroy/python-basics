from flask import make_response, jsonify
from flask.views import MethodView


inventory = {
    "apple": {
        "description": "Crunchy and delicious",
        "qty": 30
    },
    "cherry": {
        "description": "Red and juicy",
        "qty": 500
    },
    "mango": {
        "description": "Red and juicy",
        "qty": 500
    }
}

class serveRequests(MethodView):
    """ /api/get/<list_ids> """

    error = {
        "itemNotFound": {
            "errorCode": "itemNotFound",
            "errorMessage": "Item not found"
        }
    }

    def get(self, list_ids):
        """ Get an item """
        if not inventory.get(list_ids, None):
            return make_response(jsonify(self.error["itemNotFound"]), 400)
        return make_response(jsonify(inventory[list_ids]), 200)



