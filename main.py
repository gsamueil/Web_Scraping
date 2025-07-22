from  bs4 import BeautifulSoup

with open('D:/InnovionRay_team/Innovisionray_team/InnoVisionRay/Amit/AI_Diploma/Data_Science/Python for AI and Data Science/Python/H_APIs & Web Scraping/Web_Scraping/home.html','r') as html_file:
    content = html_file.read()
    soup =BeautifulSoup(content,'lxml')
    # print(soup.prettify())
    # tags =  soup.find_all('h5')
    # print(tags)
    
    # for course in tags:
    #     print(course.text)
        
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()
        
        print(course_name)
        print(course_price)