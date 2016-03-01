import lxml.etree as et
import lxml.html as lh

root = et.Element("items")
link = "http://veliki.com.ua/dir_cross_city.htm"
parser = lh.HTMLParser(encoding="windows-1251")
tree = lh.parse(link, parser)
counter=0
#@data_src = src
for node in tree.xpath("//li/div[@class='holder']"):
    item = et.Element("item")
    img_ = node.xpath("./div/a/img/@src")[0]
    title_ = node.xpath("./div[@class='name']/a/text()")[0].strip()
    price_ = node.xpath("./div[@class='price']/span/*[1]/text()")[0]
    description_link = node.xpath("./div[@class='name']/a/@href")[0]
    item_page_tree = lh.parse(description_link, parser)
    description_ = item_page_tree.xpath("//div[@class='text-holder']")[0]
    et.strip_tags(description_,'strong','br','ul','li','p','iframe')
    title = et.Element("title")
    title.text = title_
    item.append(title)
    description = et.Element("description")
    description.text = description_.text.strip()
    item.append(description)
    price = et.Element("price")
    price.text = price_[:-5]
    item.append(price)
    img = et.Element("img")
    img.text = img_
    item.append(img)
    root.append(item)
    print description_link
fileToWrite = "task3.xml"
et.ElementTree(root).write(fileToWrite,encoding="utf-8",pretty_print=True)










