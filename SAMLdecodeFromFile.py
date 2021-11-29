import base64, zlib, xml.dom.minidom, sys

filename = sys.argv[1]
print('processing file: {}'.format(filename))
print()

file = open(filename, 'r')

for each in file:
  decoded_value = zlib.decompress(base64.b64decode(each), -15)
  print(xml.dom.minidom.parseString(decoded_value).toprettyxml())
  print()