# -*- coding: utf-8 -*-
  

import xml.etree.ElementTree as ET
import json
import argparse

def convert():

  parser = argparse.ArgumentParser(description='Taking input as XML file')
  parser.add_argument('-f', '--file', required=True,  help="Option for XML file path")
  args = parser.parse_args()

  xmlparser = ET.XMLParser(encoding="utf-8")
  tree = ET.parse(args.file, parser=xmlparser)
  root = tree.getroot()

  fields = ['batchid', 'batchname', 'nodeid', 'activityid', 'context', 'inputchannel', 'numberofdocumentsinactivity', 'positionofdocumentinactivity', 'timestampofreceipt', 'documentid', 'documenttype', 'identificationnumber', 'faxnumber', 'imailid', 'sender', 'receiver', 'subject', 'analyzecomplain', 'analyzeoffer', 'originaltext', 'inputruntimeenvironment']

  keys = []
  values = []
  final_dict = {}

  for elements in root:
      for subelements in elements:
          if 'value' in subelements.attrib.keys():
             keys.append(subelements.tag)
             values.append(subelements.attrib['value'])
          elif 'name' in subelements.attrib.keys():
             keys.append(subelements.tag)
             values.append(subelements.attrib['name'])

  intermidiate = dict(zip(keys, values))

  for k,v in intermidiate.items():
      for i in fields:
          if i==k:
              final_dict[k] = v

  final_json = json.dumps(final_dict)
  return final_json

def tojson(file):

  xmlparser = ET.XMLParser(encoding="utf-8")
  tree = ET.parse(file, parser=xmlparser)
  root = tree.getroot()

  fields = ['batchid', 'batchname', 'nodeid', 'activityid', 'context', 'inputchannel', 'numberofdocumentsinactivity', 'positionofdocumentinactivity', 'timestampofreceipt', 'documentid', 'documenttype', 'identificationnumber', 'faxnumber', 'imailid', 'sender', 'receiver', 'subject', 'analyzecomplain', 'analyzeoffer', 'originaltext', 'inputruntimeenvironment']

  keys = []
  values = []
  final_dict = {}

  for elements in root:
      for subelements in elements:
          if 'value' in subelements.attrib.keys():
             keys.append(subelements.tag)
             values.append(subelements.attrib['value'])
          elif 'name' in subelements.attrib.keys():
             keys.append(subelements.tag)
             values.append(subelements.attrib['name'])

  intermidiate = dict(zip(keys, values))

  for k,v in intermidiate.items():
      for i in fields:
          if i==k:
              final_dict[k] = v

  final_json = json.dumps(final_dict)
  return final_json



if __name__ == '__main__':
  
  output = convert()
  print(output)

  outpt = tojson('docs.xml')
  print(outpt)


