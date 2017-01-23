# using Python 2 to run
#
from pymongo import MongoClient

client = MongoClient()
db = client['xlo'].todos

pipe = [
	{ '$project': {'_id': { 'teamleague': { '$concat': [ '$Team', ',', '$league' ] } } } },
	{ '$group': {'_id': '$_id.teamleague'}} 
	]

out = db.todos.aggregate(pipe)

#print(out)

for r in out:
	print(r)

#while(out.fetch_next):
#	doc = out.next_object()
#	print(doc)
