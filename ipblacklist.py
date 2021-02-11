import sys
import os.path
import csv


urlpercentage = 0.05
weblogfileName = None
apachelogsfields = ['ip', 'identd', 'frank', 'time_part0', 'time_part1', 'request', 'status', 'size', 'referer', 'user_agent']

def analyze_weblog(filename):

    uniqueurlcount = 0                    
    urls = []                             
    uniqueipcount = []                   
    uniqueuseragentscount = []            
    iplist = []                           
    useragentlist = []                    
    
    print("The weblog file to analyze is %s" % filename)
    with open(filename, mode='r') as csv_file:                    
        csv_reader = csv.reader(csv_file, delimiter=' ')
        for row in csv_reader:
     
             
            if (row[0][0] != '#'):        
                                                                    
               ipaddress = row[apachelogsfields.index('ip')]         
               request = row[apachelogsfields.index('request')]      
               status = row[apachelogsfields.index('status')]      
               user_agent = row[apachelogsfields.index('user_agent')]
    
               url = (request.partition(' ')[2]).partition(' ')[0] 

               if (status >= '200' and status <= '299'):           
               
                   if (url not in urls):                       
                       uniqueurlcount += 1                     
                       urls.append(url)                        
                       uniqueipcount.append(0)                  
                       uniqueuseragentscount.append(0)          
                       newiplist = []                           
                       iplist.append(newiplist)                
                       newuseragentlist = []                    
                       useragentlist.append(newuseragentlist)   

                   if (user_agent not in useragentlist[urls.index(url)]):  
                       useragentlist[urls.index(url)].append(user_agent)   
                       temp = uniqueuseragentscount[urls.index(url)] + 1   
                       uniqueuseragentscount[urls.index(url)] = temp
                   if (ipaddress not in iplist[urls.index(url)]):              
                       iplist[urls.index(url)].append(ipaddress)               
                       temp = uniqueipcount[urls.index(url)] + 1               
                       uniqueipcount[urls.index(url)] = temp                       
               
           
        numberofurltodisplay = urlpercentage * uniqueurlcount       
        intnumberofurltodisplay = int(numberofurltodisplay)
        if (numberofurltodisplay > intnumberofurltodisplay):        
            intnumberofurltodisplay += 1
        tempuniqueuseragentscount = uniqueuseragentscount.copy()    
        tempuniqueuseragentscount.sort()
                                                                    
        useragentcounttodisplay = tempuniqueuseragentscount[(intnumberofurltodisplay -1)] 
        tempuniqueipcount = uniqueipcount.copy()                    
        tempuniqueipcount.sort()
                                                                    
        ipcounttodisplay = tempuniqueipcount[(intnumberofurltodisplay -1)]                
    
        print('URL with least user agents')
        print('--------------------------')
        
        for count in range (0, (useragentcounttodisplay + 1)):  
            index = 0
            for elementuseragentcount in uniqueuseragentscount:        
               if (elementuseragentcount == count):                     
                   print(urls[index])
               index += 1
               
        print('URL with least IP address')         
        print('-------------------------')           
        
        for count in range (0, (ipcounttodisplay + 1)):    
            index = 0
            for elementipcount in uniqueipcount:                        
               if (elementipcount == count):                           
                   print(urls[index])
               index += 1           
        
if __name__ == '__main__':
   try:
       if len(sys.argv) == 2:                                              
           weblogfileName=sys.argv[1]
           print ("Web log file to read is %s" % weblogfileName)
           if(os.path.isfile(weblogfileName)):
                analyze_weblog(weblogfileName)             
       else:
           print ('Usage: python3 %s <weblogfile>' % sys.argv[0])         
   except Exception as e:
        print("You must provide a valid filename (path) of a web logfile")
        raise