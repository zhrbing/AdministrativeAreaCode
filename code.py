import requests,json
from openpyxl import Workbook,load_workbook

filename='E:\JupyterNotebook\全国行政区划.xlsx'
resp=requests.post('http://xzqh.mca.gov.cn/getInfo?code=100000&type=1').json()

title=['区划编码','名称','驻地','人口（万人）','面积（平方千米）','区号','邮编','类型','省级归属','地级归属']
wb=Workbook()
sheet=wb.active
sheet.append(title)

for k,v in resp.items():
    sheet.append([k]+v)
  
wb.save(filename)    
