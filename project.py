from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://ceoranking.com/pages/page_232.php")

soup=BeautifulSoup(html, "lxml")
company_table = soup.find_all('table', {"class":"item_table smartOutput htmlEditor"})

company_table_tr=company_table[0].find_all("tr")

company_info=[]
for tr in company_table_tr:
   company_sales_info=[]
   td=tr.find_all("td")

   for content in td:
       print(content.get_text(), end=', ')
       company_sales_info.append(content.get_text())
   print("")
   company_info.append(company_sales_info)
