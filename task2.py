import xml.etree.ElementTree as et

tree = et.parse("Task1/task1.xml")
root = tree.getroot()
counter=1
for fragment in root.findall(".//page"):
    print "Page "+str(counter)+" : "+str(len(fragment.findall(".//image")))+" images"
    counter+=1






