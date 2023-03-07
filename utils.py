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