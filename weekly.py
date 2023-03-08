import operations
import utils

operations.initializeTimetable('common', 7, 8, 24)
operations.taskList = utils.getDataFromJson()['tasks']

while True:
    operations.printRootMenu()