from datetime import datetime

def date_check(startDate, endDate):

    date_format_check(startDate)
    date_format_check(endDate)

    startDate = datetime.strptime(startDate, '%Y-%m-%d')
    endDate = datetime.strptime(endDate, '%Y-%m-%d')

    if startDate > endDate:
        raise Exception('starDate parameter has to be less than endDate parameter!')
    else:
        pass

def date_format_check(date):

    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Date format should be YYYY-MM-DD ')

def uevcb_eic_check(code):
    
    if code != None:

        key_w = code[2]
        
        if key_w == 'W' and len(code) == 16:
            pass
        else:
            raise Exception('EIC Code should be include W and 16 characters long E.g: 40W000000026808R')
    else:
        pass

def org_eic_check(code):
    
    if code != None:
        
        key_x = code[2]
        
        if key_x == 'X' and len(code) == 16:
            pass
        else:
            raise Exception('EIC Code should be include X and 16 characters long E.g: 40X000000003585Y')
    else:
        pass


