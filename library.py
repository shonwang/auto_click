import clr
import time
import os
import platform
import fnmatch
import shutil
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import fromstring
from xml.etree.ElementTree import Element

clr.AddReference("System")
from System.Text import *
from System.IO import *

class log():
	def __init__(self, path):
		self.path = path
		if path != '':
			log_file = open(self.path, 'w')

	def write(self, text, result):
		if result == 0:
			result = 'done'
		elif result == 1:
			result = 'none'
		log_current_time = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
		stream_writer = StreamWriter(self.path, True);
		text = log_current_time + " >> " + text + ': ' + result.ToString();
		print(text);
		stream_writer.WriteLine(text);
		stream_writer.Close();
		# log_current_time = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
		# log_file = open(self.path, 'a')
		# text = log_current_time + ' >> ' + text + ': ' + str(result) + '\n'
		# print text
		# log_file.write(text)
		# log_file.close()

class case_info():
	def __init__(self, result_file_path = '', iterate_num = 0, case_id = '', 
		result = 0, comments = '', run_time = 0):
		self.iterate_num = iterate_num
		self.case_id = case_id
		self.result = result
		self.comments = comments
		self.run_time = run_time
		self.result_file_path = result_file_path