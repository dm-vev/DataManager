from DataManager import DataManager

dm= DataManager()

new = input('Set new DT name: ')
dm.new(new)

data = input('Set value for write to WriteValue: ')
dm.write(new, 'WriteValue', data)

print(new+' WriteValue = '+dm.read(new, 'WriteValue'))

dm.migrate(new,'MigrateExample', createNew=True) #Now your DT = MigrateExample DT

print(dm.getCopy('MigrateExample'))
