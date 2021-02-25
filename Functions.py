import pandas as pd
import time
from datetime import datetime

in_Core_ = []
MS_In_Core_ =[]
Not_In_Core_ = []
Core_Routen_ = []
MS_Routen_ = []
Index_In_Core_File = []
#Core_R = Core_Routen()
#MS_R = MS_Routen()
def Core_Routen():
    with open('Routen_nach_172.20.1.144.txt') as Core_:#read from Text File, here are Static Routs in Core Router
      for i in Core_:
        Core_Routen_.append((i.strip()).rstrip())
    return Core_Routen_
#=========================================================================
#=========================================================================
def MS_Routen():
    data = pd.read_excel('O365_IP_only_ohne_Duplikate.xlsx') #read from Excel File,here are Ips in Text File
    IPs= data['MS_IP'].tolist()
    for i in IPs:
        MS_Routen_.append((i.strip()).rstrip())
    return  MS_Routen_
#=========================================================================
#=========================================================================
Core_R = Core_Routen()
MS_R = MS_Routen()
#=========================================================================
#=========================================================================
def compare_MS_With_CoreR():#Function to check which Ip is routed in Core Router MS:Microsoft Ips
    index =0
    for i in MS_R:
      index = 0
      for x in Core_R :
        if i in x :
          in_Core_.append(x)
          MS_In_Core_.append(i)
          Index_In_Core_File.append(Core_R.index(x))
          index +=1
          break
      if index == 0 :
         Not_In_Core_.append(i)
    return Core_R
#================================================================
#================================================================
def OS365_Im_Core_File():#create a Text File and put the  the Result in it
       filename1 = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")#Creat a File with Date in the name
       f = open("O365_Im_Core_" + str(filename1) + ".txt", "w")
       counter = 0
       f.write('======================================'+"\n")
       f.write('Zhal den Routen im Core =  '+ str(len(Core_R))+"\n")
       f.write('Zhal den O365 IPs = '+str(len(MS_R))+"\n")
       f.write('O365 geroutet im Core = '+str(len(in_Core_))+"\n")
       #f.write(len(MS_In_Core_))
       f.write('O365 IPs  NICHT geroutet im Core = '+str(len(Not_In_Core_))+"\n")
       f.write('======================================'+"\n"+"\n")
       f.write('IP in O365 Datei'+'\t\t'+'Zeile im Core Datei '+'\t\t\t\t'+'Routing Im Core'+"\n")
       f.write('================'+'\t\t'+'=================== '+'\t\t\t\t'+'==============='+"\n\n")
       for i in in_Core_:
          f.write(str(MS_In_Core_[counter])+'  '+'  '+'\t\t\t'+ str(Index_In_Core_File[counter]+1)+'\t\t\t\t'+str(i).rstrip())
          counter += 1
          f.write('\n')
       f.close()
#========================================================================
#========================================================================
def OS365_NICHT_Im_Core_File():#create a Text File and put the  the Result in it IPs are not routed in core
       filename1 = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")#Creat a File with Date in the name
       f = open("OS_Nicht_Im_Core_" + str(filename1) + ".txt", "w")
       #counter = 0
       f.write('======================================'+"\n")
       f.write('Zhal den Routen im Core =  '+ str(len(Core_R))+"\n")
       f.write('Zhal den O365 IPs = '+str(len(MS_R))+"\n")
       f.write('O365 geroutet im Core = '+str(len(in_Core_))+"\n")
       #f.write(len(MS_In_Core_))
       f.write('O365 IPs  NICHT geroutet im Core = '+str(len(Not_In_Core_))+"\n")
       f.write('======================================'+"\n\n")
       f.write('IP in O365 Datei nicht geroutet im Core\n')
       f.write('=======================================\n\n')
       for i in Not_In_Core_:
          f.write(str(str(i).rstrip()))
          f.write('\n')
       f.close()


 