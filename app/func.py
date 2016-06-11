from pymongo import MongoClient
import json
from flask import jsonify

client = MongoClient()

db = client.tdlsch

class func(object):
	
	def insDB(self, tdl):
		insertDb = {'activity' : tdl}
		inside = db.tdltbl.insert_one(insertDb)
		return(tdl)

	def selDB(self, tdl):
		queryDb = db.tdltbl.find()
		qlist = []
		for a in queryDb:
			qlist.append(a)
		return(str(qlist))

	def updDB(self, tdl, ptdl):
		result = db.tdltbl.update_one( #upate_many/replace_one/replace_many
			{"activity": ptdl},
			{
				"$set": {
					"activity": tdl
				}
			}
		)
		return(ptdl + tdl)

	def delDB(self, tdl):
		result = db.tdltbl.delete_one({'activity': tdl})
		return(tdl)


