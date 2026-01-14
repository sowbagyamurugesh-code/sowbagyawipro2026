import xml.etree.ElementTree as ET
tree = ET.parse('student.xml')
root = tree.getroot()

for student in root.findall('student'):
    id=student.find('id').text
    name=student.find('name').text
    marks=student.find('marks').text
    print(id, name, marks)


root=ET.Element("employee")
emp1=ET.SubElement(root,"emp")
ET.SubElement(emp1,"id").text="1"
ET.SubElement(emp1,"name").text="John"

emp2=ET.SubElement(root,"emp")
ET.SubElement(emp2,"id").text="2"
ET.SubElement(emp2,"name").text="Michael"
tree = ET.ElementTree(root)
tree.write("employee.xml")
print("xml file written successfully")