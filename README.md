# DataManager
Easy and faster python manage/storage data tool

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
    
Network:\n
  Send commands as format over UDP protocol:\n
  If auth need:\n
    Auth key;Command arguments\n
  If auth didnt need:\n
    Command arguments\n
  All commands:\n
    new db_name\n
    read db_name table\n
    getCopy db_name\n
    getValues db_name\n
    migrate db_name db_name2\n
    get db_name\n
    save db_name\n
    load db_name
