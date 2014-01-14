# this program is free, and it was distributed 
# in the hope that it will be useful .and without any warranty.
# Copyright (c) 2014 Slim_ZoMoe < xianszm007@gmail.com >

#----------------------------------------------------
# mainly value is the 'pgpgin' and 'pgpgout' from vmstat_file 
# since the last boot ! it can get the amount of data 
# read from/write into the hard disk physical memory per second .
class vmstat_read(object):
	def __init__(self):
		self.source_file=open('/proc/vmstat')
		self.vmstat=self.read_function()
	def read_function(self):
		for line in self.source_file:
			if line.startswith('pgpgin '):
				pgpgin=(int(line.split()[1])*1024)
				break
		for line in self.source_file:
			if line.startswith('pgpgout '):
				pgpgout=(int(line.split()[1])*1024)
				break
		self.source_file.seek(0)
		return pgpgin,pgpgout
	def pgpg_delta(self):
		new_value=self.read_function()
		pgpg_delta=new_value[0]-self.vmstat[0],new_value[1]-self.vmstat[1]
		self.vmstat=new_value
		return pgpg_delta


