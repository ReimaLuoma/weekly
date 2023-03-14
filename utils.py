import json

def generateSubMenu(menu):

    '''
    Generates submenu with 5 options (Add, Modify, Remove, Show, Main menu)
    :param menu: name of the sub menu
    '''

    print('*** {} MENU ***'.format(menu))
    print('')

    print('Choose action:')
    print ('[1] Add {}'.format(menu))
    print ('[2] Modify {}'.format(menu))
    print ('[3] Remove {}'.format(menu))
    print ('[4] Show {}s'.format(menu))
    print ('[5] MAIN MENU')

def writeToJson(type, object):

    '''
    Writes given object to JSON
    :param type: type of data [timetable, task, person]
    :param object: object to write to JSON file
    '''

    filename = 'data.json'

    # open file and read
    with open(filename, 'r') as file:
        data = json.load(file)

    # add new data to correct level
    data[type].append(object)

    # overwrite with new data
    with open(filename, 'w') as file:
        json.dump(data, file)

def getDataFromJson():

    '''
    Reads data from JSON
    '''

    filename = 'data.json'

    # open file and read
    with open(filename, 'r') as file:
        data = json.load(file)

    return data

def removeDataFromJson(type, item):

    '''
    Removes data from JSON
    :param type: type of data [timetable, task, person]
    :param item: item to be removed from the list
    '''

    filename = 'data.json'

    # open file and read
    with open(filename, 'r') as file:
        data = json.load(file)

    # remove data from json
    data[type].pop(item)

    # overwrite with new data
    with open(filename, 'w') as file:
        json.dump(data, file)