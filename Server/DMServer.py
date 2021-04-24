import socketserver
import json

AuthNeed = False
Host = "localhost"
Port = 9087 
key = ''
def_path = (json.loads((open('server.json')).read()))['DefaultStorage']
only_localhost = False

def load_settings():
	Sfile = open('server.json')
	st = json.loads(Sfile.read())
	key = st['Key']
	AuthNeed = st['Auth']
	only_localhost = st['Only_localhost']
	Sfile.close()

class DMServer(socketserver.BaseRequestHandler):
	
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
	def get(self, db_name, value):
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
	def save(self, db_name, path=def_path):
		DataTable = open(path+db_name+'.json', 'w')
		DataTable.write(json.dumps(self.getCopy(db_name)))
		DataTable.close()
	def load(self, db_name, path=def_path, toAnotherDT=False, anotherDT=''):
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
	
	def log(self, txt):
		print('[ DMServer ] :: '+txt)
	def execute(self, com):
		command = com.split(' ')[0]
		if command == 'new':
			self.new(com.split(' ')[1])
			return 'OK'
		elif command == 'write':
			self.write(com.split(' ')[1], com.split(' ')[2], com.split(' ')[3])
			return 'OK'
		elif command == 'load':
			self.load(com.split(' ')[1])
			return 'OK'
		elif command == 'save':
			self.save(com.split(' ')[1])
			return 'OK'
		elif command == 'migrate':
			self.save(com.split(' ')[1], com.split(' ')[2])
			return 'OK'
		elif command == 'read':
			dt = self.read(com.split(' ')[1], com.split(' ')[2])
			return 'OK:'+dt
		elif command == 'getCopy':
			dt = self.getCopy(com.split(' ')[1])
			return 'OK:'+str(dt)
		elif command == 'getValues':
			dt = self.getValues(com.split(' ')[1])
			return 'OK:'+str(dt)
	def handle(self):
		data = (self.request[0]).decode('UTF-32')
		socket = self.request[1]
		if AuthNeed:
			com = data.split(';')
			if com[0] == key:
				if only_localhost:
					if self.client_address[0] == '127.0.0.1' or self.client_address[0] == 'localhost':
						self.log(self.client_address[0]+' execute '+data)
						socket.sendto(((self.execute(data)).encode('UTF-32')), self.client_address)
					else:
						self.log(self.client_address[0]+' tried connect!')
						socket.sendto(("FAILED").encode('UTF-32')), self.client_address)
				else:
					self.log(self.client_address[0]+' execute '+data)
					socket.sendto(((self.execute(data)).encode('UTF-32')), self.client_address)
			else:
				self.log(self.client_address[0]+' failed auth!')
				socket.sendto(("FAILED").encode('UTF-32')), self.client_address)
		else:
			if only_localhost:
				if self.client_address[0] == '127.0.0.1' or self.client_address[0] == 'localhost':
					self.log(self.client_address[0]+' execute '+data)
					socket.sendto(((self.execute(data)).encode('UTF-32')), self.client_address)
				else:
					self.log(self.client_address[0]+' tried connect!')
					socket.sendto(("FAILED").encode('UTF-32')), self.client_address)
			else:
				self.log(self.client_address[0]+' execute '+data)
				socket.sendto(((self.execute(data)).encode('UTF-32')), self.client_address)

if __name__ == "__main__":
	print('[ DMServer ] :: Server started')
	with socketserver.UDPServer((Host, Port), DMServer) as server:
		server.serve_forever()
