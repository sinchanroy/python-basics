import configparser

config = configparser.ConfigParser()
print(config.read('module/variable.ini'))

def parser():
    print("inside parser")
    if config.has_option("book", "title"):
        title = config.get("book", "title")
    else:
        title = None
    if config.has_option("book", "email"):
        email = config.get("book", "email")
    else:
        email = None

    values = {'title' : title, 'email' : email}


    return values


