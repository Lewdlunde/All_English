#This code will grab the 6-digit number of every English result from NH

from bs4 import BeautifulSoup, SoupStrainer
import requests

scan = 4
curpage = 1
curpagestr = str(curpage)
comburl =                                                                                                                                                                     "https://nhentai.net/search/?q=english&page="+curpagestr
url = comburl
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
h1 = ''
hfinal = ""
filled = 0
curchar = 0
charcheck = ""
endpage = "</script></body></html>"
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')
scan = 0



while scan == 0:
        curchar = curchar + 1
        charcheck = data[curchar]
        
        
        
        
        if charcheck == "<":  #Checks if we have hit the end of the webpage's code so we can go to the next page of results.
            charcheck = charcheck+data[curchar+1]
            charcheck = charcheck+data[curchar+2]
            charcheck = charcheck+data[curchar+3]
            charcheck = charcheck+data[curchar+4]
            charcheck = charcheck+data[curchar+5]
            charcheck = charcheck+data[curchar+6]
            charcheck = charcheck+data[curchar+7]
            charcheck = charcheck+data[curchar+8]
            charcheck = charcheck+data[curchar+9]
            charcheck = charcheck+data[curchar+10]
            charcheck = charcheck+data[curchar+11]
            charcheck = charcheck+data[curchar+12]
            charcheck = charcheck+data[curchar+13]
            charcheck = charcheck+data[curchar+14]
            charcheck = charcheck+data[curchar+15]
            charcheck = charcheck+data[curchar+16]
            charcheck = charcheck+data[curchar+17]
            charcheck = charcheck+data[curchar+18]
            charcheck = charcheck+data[curchar+19]
            charcheck = charcheck+data[curchar+20]
            charcheck = charcheck+data[curchar+21]
            charcheck = charcheck+data[curchar+22]
            if charcheck == endpage:
                #hfinal = hfinal + h1 #Combines all six digit numbers on the page into a single variable.
                if filled <= 200: #Proceding just writes the numbers to a text file. It uses 16 text files because there's too much data to be sotred in one text file, because I'm too lazy to code it to remove duplicates.
                    with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng1.txt", "a") as file:
                        file.write(h1)
                        file.close
                        h1 = ''
                else:
                    if filled <= 400:
                        with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng2.txt", "a") as file:
                            file.write(h1)
                            file.close
                            h1 = ''
                    else:
                        if filled <= 600:
                            with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng3.txt", "a") as file:
                                file.write(h1)
                                file.close
                                h1 = ''
                        else:
                            if filled <= 800:
                                with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng4.txt", "a") as file:
                                    file.write(h1)
                                    file.close
                                    h1 = ''
                            else:
                                if filled <= 1000:
                                    with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng5.txt", "a") as file:
                                        file.write(h1)
                                        file.close
                                        h1 = ''
                                else:
                                    if filled <= 1200:
                                        with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng6.txt", "a") as file:
                                            file.write(h1)
                                            file.close
                                            h1 = ''
                                    else:
                                        if filled <= 1400:
                                            with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng7.txt", "a") as file:
                                                file.write(h1)
                                                file.close
                                                h1 = ''
                                        else:
                                            if filled <= 1600:
                                                with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng8.txt", "a") as file:
                                                    file.write(h1)
                                                    file.close
                                                    h1 = ''
                                            else:
                                                if filled <= 1800:
                                                    with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng9.txt", "a") as file:
                                                        file.write(h1)
                                                        file.close
                                                        h1 = ''
                                                else:
                                                    if filled <= 2000:
                                                        with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng10.txt", "a") as file:
                                                            file.write(h1)
                                                            file.close
                                                            h1 = ''
                                                    else:
                                                        if filled <= 2200:
                                                            with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng11.txt", "a") as file:
                                                                file.write(h1)
                                                                file.close
                                                                h1 = ''
                                                        else:
                                                            if filled <= 2400:
                                                                with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng12.txt", "a") as file:
                                                                    file.write(h1)
                                                                    file.close
                                                                    h1 = ''
                                                            else:
                                                                if filled <= 2600:
                                                                    with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng13.txt", "a") as file:
                                                                        file.write(h1)
                                                                        file.close
                                                                        h1 = ''
                                                                else:
                                                                    if filled <= 2800:
                                                                        with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng14.txt", "a") as file:
                                                                            file.write(h1)
                                                                            file.close
                                                                            h1 = ''
                                                                    else:
                                                                        if filled <= 3000:
                                                                            with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng15.txt", "a") as file:
                                                                                file.write(h1)
                                                                                file.close
                                                                                h1 = ''
                                                                        else:
                                                                            if filled <= 3200:
                                                                                with open("E:\\ALL OF N\\nh-pdf-downloader-master\\Alleng16.txt", "a") as file:
                                                                                    file.write(h1)
                                                                                    file.close
                                                                                    h1 = ''
                filled = filled + 1
                curpage = curpage + 1 #Now that all six digit numbers on the page are saved, we can move on to searching the next page.
                print(curpage)
                if curpage == 3117: #Check how many English pages on NHentai, then change this var to that ammount.
                    print('done')
                curpagestr = str(curpage)
                comburl =                                                                                                                                                                     "https://nhentai.net/search/?q=english&page="+curpagestr
                url = comburl
                print(comburl)
                endpage = "</script></body></html>"
                page = requests.get(url)
                data = page.text
                soup = BeautifulSoup(data, 'html.parser')
                curchar = 0
                charcheck = ""
            
        if charcheck in (number): #This is the brain of my perverted little code. This just checks for all six digit numbers on a page.
            if data[curchar+1] in (number):
                if data[curchar+2] in (number):
                    if data[curchar+3] in (number):
                        if data[curchar+4] in (number):
                            if data[curchar+5] in (number): #Once a six digit number is found, it's saved as a variable.
                                h1 = h1+data[curchar]+data[curchar+1]+data[curchar+2]+data[curchar+3]+data[curchar+4]+data[curchar+5]+" "
                                curchar = curchar + 5 
