from lxml import etree
tree = etree.parse('plant_catalog.xml')
root = tree.getroot()
x = "Aquilegia canadensis"
def find_common_name(root,x):
    for element in root:
        for alltags in element.findall('.//'):
            if alltags.tag=="BOTANICAL" and alltags.text==x:
                name = element.find("COMMON").text
                return name

name = find_common_name(root,x)
print 'The common name is : ',name
