import ftplib  #imports the ftplib library

def returnDefault(ftp):  #starts a module called returnDefault, this takes the arguement ftp

    try:  #starts a try except stack
    
        dirList = ftp.nlst()  #this command gets a list of file names from the provided ftp, probably best looking into this more because there are three alternatives
    
    except:  #this code below only happens if an error of any type occurs above
    
        dirList = []  #dirlist is set to an empty list
        
        print '[-] xxxxxxxxxx’  #outputs the enclosed data
        
        return  #not sure why this is here? Probably just to end the function if nothing is assigned to dirList
    
    retList = []  #retlist is initialised as an empty list
    
    for fileName in dirList:  #starts a for loop for every element in dirlist
    
        fn = fileName.lower()  #sets fn to the lowercase version of fileName
        
        if '.php' in fn or '.htm' in fn or '.asp' in fn:  #checks if php/htm/asp file types are in dislist, if any of them are then it triggers the if statement
            
            print '[+] Found default page: ' + fileName  #outputs the enclosed data and also appends filename to the end of it
            
            retList.append(fileName)  #the list retList has the variable fileName added to the end of it as a new element of the list
            
    return retList  #after the for loop has finished retList is returned, this can then be used later on

host = '192.168.95.179'  #assigning the ip address into host

userName = 'guest’  #again both of these lines assign the value into the variable

passWord = ‘guest’

ftp = ftplib.FTP(host)  #uses the provided ip address to assign an ftp to the variable ftp, basically initialising the system

ftp.login(userName, passWord)  #logs into the ftp chosen on the previous line using the username and password provided

returnDefault(ftp)  #starts the function at the top called returnDefault


