import xml.etree.ElementTree as ET
import pandas as pd

xml_data =  '../data/GSIP117-684812-2306112359_EU.xml'

root = ET.parse(xml_data).getroot()

print(root)
for child in root.iter('records'):
    print(child.find('RecordType').text)
    break
