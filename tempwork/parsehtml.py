from os import link
from bs4 import BeautifulSoup
import pprint
import csv

soup = BeautifulSoup(open('text.html', encoding="utf8"), 'html.parser')
prettyhtml = soup.prettify()

# Empty list to store the output
final_list = []
  
# For loop that iterates over all the <li> tags
for h in soup.findAll('li', {'class':'pv-detail-featured-list__item'}):
    temp_dict = {}
    # looking for anchor tag inside the <li>tag
    a = h.find('a')
    content = h.find('div', {'class' : 'pab-featured-item-detail__text-container'}).find('div')
    # print(content.text)
    try:
          
        # looking for href inside anchor tag
        if 'href' in a.attrs:
              
            # storing the value of href in a separate 
            # variable
            url = a.get('href')
              
            # appending the url to the output list
            temp_dict['urls'] = url
        temp_dict['content'] = content.text.strip().replace('\n', '')
        temp_dict['300DaysOfData'] = True if '#300DaysOfData' in temp_dict['content'] else False
        final_list.append(temp_dict)
    # if the list does not has a anchor tag or an anchor 
    # tag does not has a href params we pass
    except:
        pass

if final_list:
    keys = final_list[0].keys()

    with open('final_list.csv', 'w', newline='',  encoding="utf8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(final_list)