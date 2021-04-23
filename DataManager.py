import json

class DataManager():
	data = {}
	def read(self, db_name, value):
		try:
			db = self.data[db_name]
			try:
				return db[value]
			except:
				raise RuntimeError('Unkown value: '+str(value)+' in data table: '+str(db_name))
		except:
			raise RuntimeError('Unkown data table: '+str(db_name))
	def new(self, db_name):
		self.data[db_name] = {}
	def write(self, db_name, value, new_value):
		try:
			db = self.data[db_name]
			try:
				db[value] = new_value
			except:
				raise RuntimeError('Unkown value: '+str(value)+' in data table: '+str(db_name))
		except:
			raise RuntimeError('Unkown data table: '+str(db_name))
	def get(self, db_name, value, new_value):
		try:
			return self.data[db_name]
		except:
			raise RuntimeError('Unkown data table: '+str(db_name))
	def getValues(self, db_name):
		try:
			return (self.data[db_name]).values()
		except:
			raise RuntimeError('Unkown data table: '+str(db_name))
	def getCopy(self, db_name):
		try:
			return (self.data[db_name]).copy()
		except:
			raise RuntimeError('Unkown data table: '+str(db_name))
	def migrate(self, db_name, db2_name, createNew=False):
		dbcopy = self.getCopy(db_name)
		if createNew:
			try:
				self.new(db2_name)
				self.data[db2_name] = dbcopy
			except:
				raise RuntimeError('An error has ocured while migrating DT: '+str(db_name)+' to '+str(db2_name))
		else:
			try:
				self.data[db2_name] = dbcopy
			except:
				raise RuntimeError('An error has ocured while migrating DT: '+str(db_name)+' to '+str(db2_name))
	def save(self, db_name, path='./'):
		DataTable = open(path+db_name+'.json', 'w')
		DataTable.write(json.dumps(self.getCopy(db_name)))
		DataTable.close()
	def load(self, db_name, path='./', toAnotherDT=False, anotherDT=''):
		try:
			DataTable = open(path+db_name+'.json')
			dump = DataTable.read()
			DataTable.close()
			dt = json.loads(dump)
			if toAnotherDT:
				self.new(anotherDT)
				self.data[anotherDT] = dt
			else:
				self.new(db_name)
				self.data[db_name] = dt
			return dt
		except:
			raise RuntimeError('An error has ocured while loading DT: '+str(db_name))
