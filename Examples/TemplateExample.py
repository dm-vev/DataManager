from libDataManager import *

dm = DataManager()
tm = Template()

TestTemplate = {
				'API': 3.17,
				'Value1': 9,
				'Value2': 8
				}
tm.set(TestTemplate, 'TestTemplate')

dm.new('TestDTFromTemplate', 'TestTemplate')
dm.write('TestDTFromTemplate', 'Value3', 17)
print(dm.getCopy('TestDTFromTemplate'))
