import controller
import unittest 
import schema
import seed
import os

class TestModelFunctions(unittest.TestCase):
	# if writing unit tests for something that uses a database
	# it's recommended to have a dummy database and paramaterize 
	# your schema/seed files
	def setUp(self):
		# runs before any tests
		pass
		
	def tearDown(self):
		# runs after any tests
		pass
		
	def testLookupPrice(self):
		price = model.lookup_price('tsla')
		self.assertGreater(price, 0.01, "TSLA's price is greater than one cent")         #field, value to be gt, error message
		
		
		
class TestAccountCreateAndLoad(unittest.TestCase):

	def setUp(self):
		schema.run("test.db")
		seed.run("test.db")
		model.opencursor.setDB("test.db")
		
	def tearDown(self):
		os.remove("test.db")
		
	def testAccountLoad(self):
		a = model.account(username="Carter", password="password!")
		self.assertEquals(a.username, "Carter", "User loaded from username, password")

unittest.main()