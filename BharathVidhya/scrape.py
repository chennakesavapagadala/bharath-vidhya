
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

## extract data from career360 web page
## url link from career360 web page
URL = 'https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india'
total_pages = 179

college_data = []
private_colleges = []
Government_colleges = []
def fetch_college_data():
    print('Getting colleges data....')
    for page in range(1, total_pages + 1):
        url = f"{URL}?page={page}"
        response = requests.get(url)

        if response.status_code != 200 :
            print(f'Fetching Failed:{response.status_code}')

        soup = BeautifulSoup(response.content, "html.parser")
        college_cards = soup.find_all('div', class_= 'card_block')

        # get college details
        for card in college_cards:
            college_name = card.find('h3', class_ ='college_name').get_text(strip=True)
            temp_name = college_name.lower()
            pattern1 = r'.*?[-]\s'
            pattern2 = r'\s|,\s'
            if temp_name:
                name_link = re.sub(pattern1,'',temp_name)
                name_link = re.sub(pattern2,'-',name_link)
            name_link = name_link
            college_link = f'https://careers360.com/colleges/{name_link}'
            gallery = f'https://www.careers360.com/colleges/{name_link}?gallery=true'
            unv_college_link = f'https://careers360.com/university/{name_link}'
            unv_gallery = f'https://www.careers360.com/university/{name_link}?gallery=true'
            location = card.find(lambda tag: tag.name == "span" and not tag.attrs).get_text(strip=True)
            rating = card.find('span', class_ = 'star_text')
            ranking = card.find(['div','span'], class_ = 'ranking_strip')
            branch = card.find('a', class_='general_text').get_text(strip=True)

            exams = card.find('a', class_ = 'exam_black_link').get_text()if card.find('a', class_ = 'exam_black_link')else ''
            moreExams = card.find(['div','a'],class_ = 'plus_more').get_text()if card.find(['div','a'],class_ = 'plus_more') else ''
            entrance_exams = exams +','+ moreExams if (exams + moreExams)else 'Not Mentioned'

            ## Extract text from li Tags for Fees Details
            li_elements = card.find_all('li')
            fees =[li.get_text().replace('Fees :  ','') for li in li_elements if 'Fees :' in li.get_text()]

            ## Extract Text for college type from span Tags with no attributes
            span_elements = card.find_all(lambda tag: tag.name == "span" and not tag.attrs)
            typeof_college = []# to store college type
            for types in span_elements:
                typeof_college.append(types.get_text())

            # adding each college in college data
            college_data.append(
            {
            'name' : college_name,
            'location' : location,
            'state' : location.split(',')[-1],
            'city' : location.split(',')[0],
            'ranking':ranking.get_text().replace('C',' | C') if ranking else 'No Ranking',
            'branch' : branch,
            'exams' : entrance_exams,
            'rating' : rating.get_text(strip=True)if rating else 'No Ratings',
            'fees' : fees  if fees else 'Not Mentioned',
            'type' : typeof_college[1],
            'links':college_link,
            'gallery':gallery,
            'unv_links' : unv_college_link,
            'unv_gallery':unv_gallery

            })

    print("Data Saving in 'colleges_data.csv' file")
    df = pd.DataFrame(college_data)
    df.to_csv("csvfiles/colleges_data.csv", index=False)
    print('Data Fteched and Saved Succesfully....!!')


#fetch_college_data()
