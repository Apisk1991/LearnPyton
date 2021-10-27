import urllib.request
import re
print('Beginning file download with urllib2...')
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
my_file = 'cat.txt'
urllib.request.urlretrieve(url, my_file)

with open(my_file) as file:
    file_text = [row.strip() for row in file]
spisok_res_param = []
for line in file_text:
    my_pattern = r"^\'?(.*?) - - .*?(GET|POST|HEAD)\s?(.*?)\s?(?:\(|\")"
    match = re.search(my_pattern, line, re.M)
    remote_adr, requests_type, requests_resourse = match.group(1), match.group(2), match.group(3)
    res_param = (remote_adr, requests_type, requests_resourse)
    spisok_res_param.append(res_param)
pass

