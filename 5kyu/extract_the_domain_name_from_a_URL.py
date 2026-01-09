"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

"""
def domain_name(url):
    if '://' in url:
        url = url.split("://")[1]
    url = url.split('/')[0]
    if url.startswith('www.'):
        url = url[4:]
    return url.split(".")[0]


#Other solution 
def domain_name(url):
    url = url.replace('www.','')
    url = url.replace('https://','')
    url = url.replace('http://','')
    
    return url[0:url.find('.')]