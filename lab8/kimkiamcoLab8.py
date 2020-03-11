from ftplib import FTP


  #domain name or server ip:
is_logged_in = False
try:
    ftp = FTP('ftp.ibiblio.org')
    ftp.login()
    is_logged_in = True
    print("login successful")
    print(ftp.getwelcome())
except :
    print('login failed')
    
try:
    if is_logged_in == True:
        print('Current working directory: ' + ftp.pwd())
        ftp.cwd('pub/linux') 
        print('Current working directory: ' + ftp.pwd())
        
        with open('welcome.html', 'wb') as fp:
            ftp.retrbinary('RETR README', fp.write)
        print('download complete')
        ftp.quit()
except:
    print('something went wrong')
    

    
"""------------- run --------------
login successful
220 ProFTPD Server
Current working directory: /
Current working directory: /pub/linux
download complete
"""
