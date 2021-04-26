from DataManager import DataManager

dm= DataManager()

new = input('Set new DT name: ')
dm.new(new) #Creating new dt

data = input('Set value for write to WriteValue: ')
dm.write(new, 'WriteValue', data) #Write to dt

print(new+' WriteValue = '+dm.read(new, 'WriteValue')) #Get value from dt

dm.migrate(new,'MigrateExample', createNew=True) #Now your DT = MigrateExample DT

print(dm.getCopy('MigrateExample')) #Print dt
