from datetime import datetime

def clean_currency(item: str) -> float:
    '''
    remove anything from the item that prevents it from being converted to a float
    '''    
    return float(item.replace('$', '').replace(',', ''))

def extract_year_mdy(timestamp):
    '''
    use the datatime.strptime to parse the date and then extract the year
    hms includes
    '''
    return datetime.strptime(timestamp, '%m/%d/%Y %H:%M:%S').year

def clean_country_usa(item: str) ->str:
    '''
    This function should replace any combination of 'United States of America', USA' etc.
    with 'United States' need to check lower case
    '''
    possibilities = [
        'united states of america', 'usa', 'us', 'united states', 'u.s.'
    ]
    return 'United States' if item.strip().lower() in possibilities else item


if __name__=='__main__':
    print("""
        Add code here if you need to test your functions
        comment out the code below this like before sumbitting
        to improve your code similarity score.""")
    #print(clean_currency('$123,456,789'))
    #print(clean_currency('$123.456.789'))
    #print(clean_currency('123,456,789'))
    #print(clean_currency('123.456.789'))
    #print(clean_currency('123456789'))
    #print(clean_currency('123456789.00'))

    #print(extract_year_mdy('01/01/2019'))
    #print(extract_year_mdy('01/01/1999'))
    #print(extract_year_mdy('01/01/1999', '%m/%d/%y'))
    #print(extract_year_mdy('01/01/1999', '%m/%d/%Y'))

    #print(clean_country_usa('United States of America'))
    #print(clean_country_usa('USA'))
    #print(clean_country_usa('us'))
    #print(clean_country_usa('u.s.'))
    #print(clean_country_usa('United States'))
    #print(clean_country_usa('United States of America'))

    
