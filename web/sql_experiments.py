import sqlite3

conn = sqlite3.connect('/Users/seanrussell/Documents/Computing/web/database.db')

c = conn.cursor()

def create_task_table(c):
    '''Things maybe need a unique identifyier that isn't description? although
    description should be unique'''
    c.execute('CREATE TABLE tasks (Priority int, Description text, Complete bool)')

def add_task(c, description):
    '''adds a new incomplete task as the highest priority item'''
    c.execute('INSERT INTO tasks VALUES (1, "' + description + '", FALSE)')

def complete_task(c, description):
    c.execute('UPDATE tasks SET Complete = TRUE WHERE Description = "' + description + '"')
    
complete_task(c, 'Learn SQL')
add_task(c, 'Use SQL')

for row in c.execute('SELECT * FROM tasks'):
    print(row)

conn.commit()



conn.close()
