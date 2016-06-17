def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''


def get_all_links(page):
    listed = []
    while True:
        url,endpos = get_target(page)
        if url:
            listed.append(url)
            page = page[endpos:]
        else:
            break
               

def get_target(page):
    start_page = page.find('<a href=')
    start_quote = page.find('"',start_page)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url,end_quote

print_all_links(get_page('http://xkcd.com/353/'))    
#url,endpos = get_target('abkdkjahFJAFHJSDFJDKBVNXZBVN<a href="http://google.com"/>jHSFkjgfkhgfhbzdfnmzb')
#print url,endpos
#next_target()