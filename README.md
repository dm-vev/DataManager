# DataManager
Easy and faster python manage/storage data tool

# Features
Now in DM:
- Speed
- DataManager server
- Native python support

In develop:
  - Native MySQL client support
  - Plugin system for DMServer
  - Add user system for DMServer

# How it use?
Lib:

    from libDataManager import DataManager
    
    dm= DataManager()

    new = input('Set new DT name: ')
    dm.new(new)

    data = input('Set value for write to WriteValue: ')
    dm.write(new, 'WriteValue', data)

    print(new+' WriteValue = '+dm.read(new, 'WriteValue'))

    dm.migrate(new,'MigrateExample', createNew=True) #Now your DT = MigrateExample DT

    print(dm.getCopy('MigrateExample'))
    
Network:
  Send commands as format over UDP protocol:
  
  If auth need:
  
    Auth key;Command arguments
    
  If auth didnt need:
  
    Command arguments
  All commands:
  
    new db_name
    
    read db_name table
    
    getCopy db_name
    
    getValues db_name
    
    migrate db_name db_name2
    
    get db_name
    
    save db_name
    
    load db_name
    
    newTemaplate string_template template name
    
    saveTemplate template_name
    
    loadTemplate template_name
