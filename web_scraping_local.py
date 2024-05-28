from bs4 import BeautifulSoup

with open("new.html","r") as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, "lxml")
    # print(soup.prettify())
    tag = soup.find("h2")
    tags = soup.find_all("section", id="home")
    # print(tag,tags)
    for stuff in tags:
        att_name = stuff.h2.text
        att_x = stuff.p.text.split()[-1]
        print(f'{att_name} is the section of {att_x}')