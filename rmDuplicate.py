# using Python 2 to run
#
import bson
import sys
from pymongo import MongoClient

client = MongoClient()
db = client['xlo'].todos

pipeline = [ { "$group": { "_id": { "Date": "$Date", "Team": "$Team", "Role": "$Role" }, "dups": { "$push": "$_id" }, "count": { "$sum": 1 } }}, { "$match": { "count": { "$gt": 1 } }}]

result = db.todos.aggregate(pipeline).forEach(
	function(doc) {
		doc.dups.shift() 
		db.todos.remove({ "_id": {"$in": doc.dups }}) 
	}
)
