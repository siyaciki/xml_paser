# -*- coding: UTF-8 -*-
import xml.etree.ElementTree as ET
from myClass import my_job
tree = ET.parse('xmlRes\JOBTest.xml')
root = tree.getroot()
name_root=root.tag

#print("-----------字符串读取-----子节点输出--------------")
#str='''<?xml version="1.0"?><data><country name="Liechtenstein"><rank>1</rank><year>2008</year><gdppc>141100</gdppc><neighbor name="Austria" direction="E"/><neighbor name="Switzerland" direction="W"/></country><country name="Singapore"><rank>4</rank><year>2011</year><gdppc>59900</gdppc><neighbor name="Malaysia" direction="N"/></country></data>'''
'''
root2=ET.fromstring(str)
print(root2.tag)
for child in root2:
    print(child.tag)
    print(child.attrib)
print("-----------------------------")
for neb in root2.iter('neighbor'):
    print(neb.attrib)

print("-----------------------------")
for country in root2.findall('country'):
    name=country.get('name')
    rank=country.find('rank').text
    print(name,rank)
    '''
print("------------开始--------------")
#print(root[0].get('Name'))
try:
    i=0
    j=0
    for tag_type in root.findall('TAGTYPE'):
        name_type=tag_type.get('Name')
        
        mydata = my_job()
        j+=1
        print(name_type)
        for tag_file in tag_type.findall('TAGFILE'):
            i+=1
            try:
                name_file=tag_file.get('Name')
                print(name_file)
                for partno in tag_file.findall('PARTNO'):
                    for my_property in partno.findall('PROPERTY'):
                        print("---property:")
                        mydata.version=my_property.find('Version').text
                        mydata.Icon = my_property.find('Icon').text
                        mydata.ConsiderBoardNumber = my_property.find('ConsiderBoardNumber').text
                        mydata.Shape = my_property.find('Shape').text
                        mydata.Package = my_property.find('Package').text
                        mydata.TopViewShape = my_property.find('TopViewShape').text
                        mydata.LimitTargetMachines = my_property.find('LimitTargetMachines').text
                        mydata.TargetMachineList = my_property.find('TargetMachineList').text
                        mydata.FirstPinPosition = my_property.find('FirstPinPosition').text
                        mydata.UserField1 = my_property.find('UserField1').text
                        mydata.UserField2 = my_property.find('UserField2').text
                        mydata.UserField3 = my_property.find('UserField3').text
                        mydata.UserField4 = my_property.find('UserField4').text
                        mydata.UserField5 = my_property.find('UserField5').text

                    for my_information in partno.findall('INFORMATION'):
                        print("---information:")
                        pass

                    for my_editor in partno.findall('EDITOR'):
                        print("---editor:")
                        for addedshape in my_editor.findall('ADDEDSHAPE'):
                            print("----addedshape:")
                            mydata.key={'Key':addedshape.find('Key').text}
                        pass
            except AttributeError:
                pass
            mydata.shuchu()
    print(i)
    print("j",j)
except AttributeError:
    print("数据不符")

