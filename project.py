import matplotlib.pyplot as plt
import matplotlib
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
       company_sales_info.append(content.get_text())
   company_info.append(company_sales_info)
del company_info[0]

company_name=[]
first_company_sales=[]
second_company_sales=[]
third_company_sales=[]

for company_sales_info in company_info:
    company_name.append(company_sales_info[2])
    company_sales_info[4] = company_sales_info[4].replace(',','')
    first_company_sales.append(int(company_sales_info[4]))
    company_sales_info[5] = company_sales_info[5].replace(',', '')
    second_company_sales.append(int(company_sales_info[5]))
    company_sales_info[6] = company_sales_info[6].replace(',', '')
    third_company_sales.append(int(company_sales_info[6]))

del company_name[10:]
del first_company_sales[10:]
del second_company_sales[10:]
del third_company_sales[10:]

print(company_name)
print(first_company_sales)
print(second_company_sales)
print(third_company_sales)

print("빨강 : 2017")
print("파랑 : 2018")
print("검정 : 2019")

matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font', family='Malgun Gothic')


x=range(len(company_name))

fig, ax1 = plt.subplots()
ax1.set_title('2017~2019년도 대기업 매출')
ax1.plot(x, first_company_sales, '-o',color="red")
ax1.plot(x, second_company_sales, '-o',color="blue")
ax1.plot(x, third_company_sales, '-o',color="black")
ax1.set_ylim(0, 400000)
ax1.set_ylabel('매출액')

ax1.patch.set_visible(False)

ax1.set_xticks(x)
ax1.set_xticklabels(company_name,rotation="vertical")

plt.show()
