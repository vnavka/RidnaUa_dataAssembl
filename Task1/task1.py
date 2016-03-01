import lxml.html as lh
import lxml.etree as et

url = "http://ridna.ua/"
maintree = lh.parse(url)
rezLinks = maintree.xpath("//a[starts-with(@href,'http://ridna.ua/')]/@href")
root = et.Element("data")
counter = 0

for link in rezLinks:

    counter+=1
    if(counter>20):
        break

    page = et.Element('page')
    page.set('url',link)
    pageTree = lh.parse(link)

    fragmentText = et.Element("fragment")
    fragmentText.set('type','text')
    rezText = pageTree.xpath("//*[text()]/self::*[not(self::script) and not(self::style)]/text()")

    for i in rezText:
        text = et.Element("text")
        i = i.strip()
        if i:
            text.text = i
            fragmentText.append(text)
    page.append(fragmentText)

    fragmentImg = et.Element("fragment")
    fragmentImg.set('type','image')
    rezImgs = pageTree.xpath("//img[@src]/@src")

    for i in rezImgs:
        image = et.Element("image")
        image.text = i
        fragmentImg.append(image)

    page.append(fragmentImg)

    root.append(page)



fileToWrite = "task1.xml"

et.ElementTree(root).write(fileToWrite,encoding="utf-8",pretty_print=True)



