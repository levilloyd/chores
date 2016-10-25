import datetime
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from config import CHORES

"""
Simple app to fetch chores. Requires config.py which contains a dictionary
like the following:

CHORES = {'chore1' : {'Sunday':'person1',
                      'Monday':'person2',
                      ...
                      'Saturday':'person3'},
          'chore2' : {'Sunday':'person2',
                      'Monday':'person3',
                      ...
                      'Saturday':'person1'}
}
"""

app = Flask(__name__)
api = Api(app)

def abort_if_chore_doesnt_exist(chore):
    if chore not in CHORES:
        abort(404, message="Chore {} doesn't exist".format(chore))

class Chore(Resource):
    """Defines Chore resource"""
    def get(self, chore):
        abort_if_chore_doesnt_exist(chore)
        weekday = datetime.datetime.today().strftime("%A")
        return CHORES[chore][weekday]

class ChoreList(Resource):
    """Defines ChoreList resource"""
    def get(self):
        return CHORES

api.add_resource(ChoreList, '/chores/')
api.add_resource(Chore, '/chores/<chore>/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
