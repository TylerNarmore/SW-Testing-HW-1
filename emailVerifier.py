import re

def emailVerifier(email):
   #print(re.findall('.',email))

    #@ check
    if re.search('@', email) == None:
        return False

    #TopLevel Domain Check
    elif re.search('\.[a-zA-Z]?[a-zA-Z]?[a-zA-Z]$',email) == None:
        return False

    #Domain Check
    elif re.search('@.+\.',email) == None:
        return False

    #Username Check
    elif re.search('.+@', email) == None:
        return False

    #Restricted Character Check
    elif re.search('[()\/\]\[{}]', email) != None:
        return False

    #@ in username
    elif re.search('^.*@+.*@.*$',email) != None:
        return False

    #. in domain name
    elif re.search('@.*\.+.*\.',email) != None:
        return False
    
    else:
        return True
    
