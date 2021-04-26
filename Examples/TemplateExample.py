from libDataManager import *

dm = DataManager()
tm = Template() 

TestTemplate = {
				'API': 3.17,
				'Value1': 9,
				'Value2': 8
				} #Template example
tm.set(TestTemplate, 'TestTemplate') #Add to templates array new template

dm.new('TestDTFromTemplate', 'TestTemplate') #Creating new dt from TestTemplate template
dm.write('TestDTFromTemplate', 'Value3', 17) #Write to dt
print(dm.getCopy('TestDTFromTemplate')) #Print testdt

tm.save('TestTemplate') #Save template
tm.load('TestTamplate') #Load template
