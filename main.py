<<<<<<< HEAD
from  bs4 import BeautifulSoup

with open('D:/InnovionRay_team/Innovisionray_team/InnoVisionRay/Amit/AI_Diploma/Data_Science/Python for AI and Data Science/Python/H_APIs & Web Scraping/Web_Scraping/home.html','r') as html_file:
    content = html_file.read()
    soup =BeautifulSoup(content,'lxml')
    # print(soup.prettify())
    tags =  soup.find_all('h5')
    # print(tags)
    
    for course in tags:
=======
from  bs4 import BeautifulSoup

with open('D:/InnovionRay_team/Innovisionray_team/InnoVisionRay/Amit/AI_Diploma/Data_Science/Python for AI and Data Science/Python/H_APIs & Web Scraping/Web_Scraping/home.html','r') as html_file:
    content = html_file.read()
    soup =BeautifulSoup(content,'lxml')
    # print(soup.prettify())
    tags =  soup.find_all('h5')
    # print(tags)
    
    for course in tags:
>>>>>>> 37837ffd0ade5a83fa55051283cfadd6362e6c52
        print(course.text)