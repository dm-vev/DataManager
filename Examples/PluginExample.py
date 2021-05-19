from Plugin import *

class TestPlugin():
    name = 'TestPlugin'
    description = 'Your description'
    api = '1.0'
    version = '1.0'
    def onEvent(event):
        if (event == 'enable'):
            print('Enable plugin..')
        if (event == 'stop'):
            print('Bye!')
    
Plugin.regPlugin(TestPlugin)
