import os
import codecs
import subprocess
import logging
from bs4 import BeautifulSoup
import lxml.html

# If we want to avoid downloading the HTML files, we could use this method to read it
#import requests
#doc = lxml.html.fromstring(requests.get("http://appsheethelp.zendesk.com/hc/en-us/articles/205754997-Who-should-use-AppSheet-and-what-kind-of-apps-can-it-create-").content)


SITE = 'appsheethelp.zendesk.com'
NEWFILESFOLDER = 'newfiles/'

HEADER = '''<!DOCTYPE html>
<html dir="ltr" lang="en-US">
<head>'''

ASHELP_HOME = "http://%s" % SITE

mdbasedir = r'topics-md/'
xhtmlbasedir = r'topics-xhtml/'
ditabasedir = r'topics-dita/'

def markdownify_html2text(html):

    p = subprocess.Popen(['html2text', '-d', '-b', '0', ],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    stdout, stderr = p.communicate(input=html.encode('utf-8'))

    return stdout

def wget_file(resource):

    p = subprocess.Popen(['wget', '-N',  "%s/%s" % (ASHELP_HOME, resource)],
        stdout=subprocess.PIPE)
    stdout, stderr = p.communicate(input=resource.encode('utf-8'))

    return stdout

def process_homepage(Skip_Print):

    with codecs.open('index.html','r',encoding='Windows-1252') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    if not Skip_Print:
        ditamapfd = codecs.open(ditabasedir+'/top.ditamap', 'w', 'utf-8')
        mdtopfd = codecs.open(mdbasedir+'/top.md', 'w', 'utf-8')

        mdtopfd.write('# AppSheet Reference Manual\n')

        ditamapfd.write('''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE map PUBLIC "-//OASIS//DTD DITA Map//EN" "map.dtd">
<map>
  <topichead navtitle="AppSheet Reference Manual">
  ''')

    filelist = []

    #Skip the next 2 sections
    catsection = soup.find("section","category")
    while catsection:
        category = catsection.find("h2")

        if not Skip_Print:
            mdtopfd.write(markdownify_html2text(category))
            ditamapfd.write('  <topichead navtitle="%s">' % category.text)

        section = catsection.find('section','section')

        while (section and (section.parent == category.parent)):

            if not Skip_Print:
                mdtopfd.write(markdownify_html2text(section.h3))
                ditamapfd.write('  <topichead navtitle="%s">' % section.h3.text)

                mdtopfd.write(markdownify_html2text(section.ul))
                for ref in section.ul.find_all('a'):
                    ditamapfd.write('  <topicref navtitle="%s" href="%s"/>\n' % (ref.text, os.path.basename(ref['href']) + '.md'))
                ditamapfd.write('  </topichead>' )

            filelist = filelist + [section.ul]
            section.extract()
            section = catsection.find("section","section")

        if not Skip_Print:
            ditamapfd.write('  </topichead>' )

        if (category):
            catsection.extract()
            catsection = soup.find("section","category")
        else:
            catsection = None

    if not Skip_Print:
        mdtopfd.close()
        ditamapfd.write('  </topichead>\n</map>' )
        ditamapfd.close()

    return filelist

def process_file(file):

    f = open(file,'r')
    f = codecs.open(file,'r','utf-8')
    doc = lxml.html.parse(f)

    # f = codecs.open(file,'r','utf-8')
    # soup = BeautifulSoup(f.read(), 'html.parser')

    mdtopfd = codecs.open(mdbasedir+'/%s.html' % os.path.basename(file), 'w', 'utf-8')

    title = doc.find('//title').text
    mdtopfd.write("%s <title>%s</title>\n</head>\n<body>\n<h1>%s</h1>\n" % (HEADER, title, title))


    for ref in doc.findall('//a'):
        try:
            ref.set('href', ref.get('href').replace('/hc/en-us/articles/','') + '.html')
        except:
            continue

    for img in doc.findall('//img'):
        try:
            img.set('src', img.get('src').replace('/hc/en-us/art','../art'))
        except:
            continue

    # mdtopfd = open(mdbasedir+'/%s.md' % os.path.basename(file), 'w')
    # mdtopfd.write("# %s" % soup.title.text)
    # mdtopfd.write("# %s" % doc.find('//title').text)
    # article = soup.find("div")
    # article.extract()
    #
    # article = soup.find("div")
    # date = article.find("div","meta").text
    # article.extract()
    #
    # mdtopfd.write( date + '\n')
    #
    # article = soup.find("div")
    # # change path to file in href
    # for a in article.find_all("a"):
    #     if a['href'][0] == '/':
    #         a['href'] =  os.path.basename(a['href']) + '.md'
    #
    # # change path to image in href
    # for img in article.find_all("img"):
    #     img['src'] = '../' + SITE + img['src']

    #mdtopfd.write(html2text.html2text(article))

    article = doc.findall('//div')

    #mdtopfd.write(html2text.html2text(lxml.html.tostring(article[7], encoding='utf-8')))
    mdtopfd.write(lxml.html.tostring(article[7]))

    related = doc.findall('//aside')
    inner = related[0].getchildren()
    inner[1].tag = 'div'
    inner[1].getchildren()[0].tag = 'h2'

    mdtopfd.write(lxml.html.tostring(inner[1]))
    mdtopfd.write('</body>\n</html>')
    mdtopfd.close()


    #Skip the next 2 sections
    # for i in range(2):
    #     related = soup.find("section")
    #     related.extract()
    #
    # mdtopfd.write('## Related Topics\n')
    #
    # for a in related.find_all("a"):
    #     a['href'] =  os.path.basename(a['href']) + '.md'
    #     mdtopfd.write(markdownify_html2text(a))

def main():

    # create folders that don't exist
    for folder in {mdbasedir,xhtmlbasedir,ditabasedir, NEWFILESFOLDER}:
        if not os.path.exists(folder):
            os.mkdir(folder)

    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

    seclist = process_homepage(1)

    for section in seclist:
        for file in section.find_all('a'):
            wget_file(file['href'])
            fname = os.path.basename(file['href'])
            if os.path.exists(fname):
                os.rename(fname, NEWFILESFOLDER + fname)
                process_file(NEWFILESFOLDER + fname)


if __name__ == '__main__':
    main()
    #process_file('newfiles/205860137-Change-alerts-and-workflows')
    #process_file('newfiles/205754997-Who-should-use-AppSheet-and-what-kind-of-apps-can-it-create-')
    #process_homepage()



