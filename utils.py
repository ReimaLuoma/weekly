import json
import math

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
    Reads data from JSON and returns it
    '''

    filename = 'data.json'

    # open file and read
    with open(filename, 'r') as file:
        data = json.load(file)

    return data

def updateDataInJson(type, index, object):

    '''
    Updates data in json with given data.
    :param type: type of data [str: timetable, task, person]
    :param index: index of data slot that will be updated [int]
    :param object: object to update the json with [object]
    '''

    filename = 'data.json'

    # open file and read
    with open(filename, 'r') as file:
        data = json.load(file)

    # update data from json
    data[type][index] = object

    # overwrite with new data
    with open(filename, 'w') as file:
        json.dump(data, file)

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

def checkMaxEntryLen(currentTimetable, type):

    '''
    Return the character lenght of the longest object of type in timetable.
    :param currentTimetable: current timetable to use as base of search
    :param type: item to check for lenght [str]
    '''

    max_entry_len = 0

    if type == 'task':

        for day in currentTimetable:
            tasks = currentTimetable[day]
            for entry in tasks:
                entry_len = len(entry['task']['task'])
                if entry_len > max_entry_len:
                    max_entry_len = entry_len

        float(max_entry_len)

    if type == 'person':
        for day in currentTimetable:
            tasks = currentTimetable[day]
            for entry in tasks:
                entry_len = len(entry['person']['name'])
                if entry_len > max_entry_len:
                    max_entry_len = entry_len

        float(max_entry_len)

    if type == 'status':
        for day in currentTimetable:
            tasks = currentTimetable[day]
            for entry in tasks:
                entry_len = len(entry['status'])
                if entry_len > max_entry_len:
                    max_entry_len = entry_len

        float(max_entry_len)

    return max_entry_len

def printTextWithMinLen(text, minLenght, header = True):

    '''
    Returns string with given text and add empty around it until the lenght matches min lenght given.
    :param text: the text to be printed
    :param minLenght: min lenght of the print
    :param heaeder: is the text header [bool, default True]
    '''

    text_len = len(text)
    even = False

    # check if lenght is even or odd number
    if text_len %2 == 0:
        even = True

    # handle header elements

    if header:
        if text_len > minLenght:
            return text
        if text_len < minLenght:
            minLenght -= text_len
            minLenght /= 2
            minLenght = math.ceil(minLenght)
            if not even:
                newText = (minLenght * ' ') + text + ((minLenght + 1) * ' ')
            else:
                newText = (minLenght * ' ') + text + (minLenght * ' ')

        return newText
    

    # handle non-header elements

    if not header:
        minLenght -= text_len
        minLenght /= 2
        minLenght = math.floor(minLenght)
        if not even:
            newText = (minLenght * ' ') + text + ((minLenght + 1) * ' ')
        else:
            newText = (minLenght * ' ') + text + (minLenght * ' ')
            
        return newText