import configparser

config = configparser.ConfigParser()

print(config.read('variable.ini'))

print(config.sections())

print(config['book'])

if config.has_option('book', 'title'):
    title = 'mybook'
else:
    title = 'None'

if config.has_option('book', 'email'):
    email = 'myemail'
else:
    email = 'None'


print(title)
print(email)








