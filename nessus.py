import xml.etree.ElementTree as ET
import sys
from os.path import exists


class Nessus_Parser():
	file=""
	def __init__(self, file):
		self.file = file
		
	def parse(self):
		if(exists(self.file)):
			try:
				tree = ET.parse(self.file)
				root = tree.getroot()
				self.web_servers(root)
				self.ssh_servers(root)
			except Exception as e:
				print("Invalid Nessus file: Unable to parse this file")
				print(e)
		else:
			exit("File not exists")

	def web_servers(self,root):
		print("             Web Servers:")
		print("==========================================")
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
		print("==========================================")


	def ssh_servers(self,root):
		print("             SSH Servers:")
		print("==========================================")
		for child in root:
			for hosts in child.findall('ReportHost'):
				if hosts.get('name') != "None":
						host=hosts.get('name')
				ports=[]
				for items in hosts.findall('ReportItem'):
					if items.get("pluginName")=="SSH Server Type and Version Information":
						if items.get("port") not in ports:
							ports.append(items.get("port"))
							print(host+":"+items.get("port"))
		print("==========================================")


if __name__ == '__main__':
	if(len(sys.argv) == 2 ):
		obj=Nessus_Parser(sys.argv[1])
		obj.parse()
	else:
		print("Usage: python3 nessus.py <file.nessus>")