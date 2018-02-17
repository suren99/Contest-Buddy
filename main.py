import urllib2
import requests 
import os
import sys
from bs4 import BeautifulSoup
location = "/Users/suren/cp/codechef"
language = ".cpp"

class parser:
    def __init__(self):
        self.hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}
        self.url = "http://www.codechef.com"
    
    def parse(self,code):
        r = requests.get(self.url+"/"+code)
        soup = BeautifulSoup(r.text, "html.parser")
        div_tags = soup.find_all("div", class_ = "problemname")
        problem_links = [each.find('a')['href'] for each in div_tags]
        template_fp = open("template.txt","r");
        template = ''.join(template_fp.readlines());
        for problem_link in problem_links:
            problem = problem_link[problem_link.index("problems") + len("problems/"):]
            if not os.path.exists(location + "/" + code):
                os.makedirs(location + "/" + code)
            fp = open(location + "/" + code + "/" + problem + language, "w")
            fp.write(template)
            fp.close()
        template_fp.close()
        print "You are ready to go"

p = parser()
p.parse(sys.argv[1])

