import requests
import bs4

search_query = input("Enter what you want to search for: ")
no_of_results = int(input("Enter the number of results you want to see in multiples of 10 or 100: "))

headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
username = "abe9r9g267ndixi"
password = "mk72n2ajsuco98g"
proxy = "rp.proxyscrape.com:6060"
proxy_auth = "{}:{}@{}".format(username, password, proxy)
proxies = {
    "http":"http://{}".format(proxy_auth)
}
if no_of_results<100:
 for i in range(int(no_of_results/10)):
    url = 'https://google.com/search?q='+search_query+"&num=10"+"&start="+str(10*i)
    req_result = requests.get(url,headers=headers,proxies=proxies)
    soup = bs4.BeautifulSoup(req_result.text,'lxml')
    for res in  soup.select('.tF2Cxc'):
     
      print(res.select_one('.DKV0Md').text)
      print(res.select_one('.yuRUbf a')['href'])
      try:
          print(res.select_one('.hJNv6b').text)
      except:
          print("------ description not found ------")
      print("--------------------")
      
else:
   for i in range(int(no_of_results/100)):
    url = 'https://google.com/search?q='+search_query+"&num=100"+"&start="+str(100*i)
    req_result = requests.get(url,headers=headers,proxies=proxies)
    soup = bs4.BeautifulSoup(req_result.text,'lxml')
    for res in  soup.select('.tF2Cxc'):
     
      print(res.select_one('.DKV0Md').text)
      print(res.select_one('.yuRUbf a')['href'])
      try:
          print(res.select_one('.hJNv6b').text)
      except:
          print("------ description not found ------")
      print("--------------------")
     


print("\nPEOPLE ALSO SEARCH FOR:")
url = 'https://google.com/search?q='+search_query
req_result = requests.get(url,headers=headers,proxies=proxies)
soup = bs4.BeautifulSoup(req_result.text,'lxml')
for span in soup.find_all('div', jsname='yEVEwb'):
    print(span.select_one('.CSkcDe').text)
    print("---------------") 