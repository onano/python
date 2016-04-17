from urllib import request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=3&e=9&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'

def download_stock_data(usr_url):
    #Opening url using urlopen()
    response = request.urlopen(usr_url)
    #reading file from url using read()
    csv = response.read()
    csv_str = str(csv)
    #split() allows us to divide data in proper lines
    lines = csv_str.split("\\n")
    #Destination name
    dest_url = r'GOOG.csv'
    fw = open(dest_url, 'w')
    for each_line in lines:
        fw.write(each_line + "\n")
    fw.close()

download_stock_data(goog_url)
