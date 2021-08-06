import xml.etree.ElementTree as ET

file=you_file_name_here
tree = ET.parse(file)
root = tree.getroot()

for child in root:
	for hosts in child.findall('ReportHost'):
		if hosts.get('name') != "None":
				host=hosts.get('name')
		ports=[]
		for items in hosts.findall('ReportItem'):
			if items.get("pluginFamily")=="Web Servers":
				if items.get("port") not in ports:
					ports.append(items.get("port"))
					print(host+":"+items.get("port"))
