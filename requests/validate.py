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

