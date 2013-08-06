# coding=utf-8

import clr
import xmlrpclib
import time
import os
import platform
import fnmatch
import shutil
from library import *
# from xml.etree import ElementTree as ET
# from xml.etree.ElementTree import fromstring
# from xml.etree.ElementTree import Element

clr.AddReference("System.XML")
from System.Xml import *

rs = xmlrpclib.ServerProxy("http://127.0.0.1:1338", allow_none=True)
os_platform = platform.platform()
current_time = time.strftime('%Y-%m-%d-%H-%M',time.localtime(time.time()))
current_path = os.getcwd()
logpath = os.path.normcase(current_path + r'/log/' + str(current_time) + '.txt')
logger = log(logpath)
case_info = case_info()

def wait_check_click(img, time_out):
	tmp = rs.action_wait(img, time_out)
	logger.write("action_wait " + img, tmp)
	tmp = rs.action_check(img)
	logger.write("action_check " + img, tmp)
	if tmp == 0:
		tmp = rs.action_click(img)
		logger.write("action_click " + img, tmp)
	return tmp

def wait_check_offsetclick(img, time_out, x, y):
	tmp = rs.action_wait(img, time_out)
	logger.write("action_wait " + img, tmp)
	tmp = rs.action_check(img)
	logger.write("action_check " + img, tmp)
	if tmp == 0:
		tmp = rs.action_click_offset(img, x, y)
		logger.write("action_click_offset " + img, tmp)
	return tmp

def wait_check(img, time_out):
	tmp = rs.action_wait(img, time_out)
	logger.write("action_wait " + img, tmp)
	tmp = rs.action_check(img)
	logger.write("action_check " + img, tmp)
	return tmp

def click(img):
	tmp = rs.action_click(img)
	logger.write("action_click " + img, tmp)
	return tmp

def check(img):
	tmp = rs.action_check(img)
	logger.write("action_check " + img, tmp)
	return tmp

def click_offset(img, x, y):
	tmp = rs.action_click_offset(img, x, y)
	logger.write("action_click_offset " + img + " " + str(x) + "/" +str(y), tmp)
	return tmp

def wait_image(img, time_out):
	tmp = rs.action_wait(img, time_out)
	logger.write("action_wait_image " + img + " " + str(time_out), tmp)
	return tmp

def sleep(time_out):
	tmp = rs.action_wait2(time_out)
	logger.write("action_sleep " + str(time_out), tmp)
	return tmp

def wait_vanish(img, time_out):
	tmp = rs.action_waitVanish(img, time_out)
	logger.write("action_waitVanish " + img, tmp)
	return tmp

def type(key, option, img = ""):
	if option == "string":
		tmp = rs.action_typekey(key, "abc")
		logger.write("action_typekey string " + str(key), tmp)
	elif option == "down":
		tmp = rs.action_typekey(key, "down")
		logger.write("action_typekey down ", tmp)
	elif option == "enter":
		tmp = rs.action_typekey(key, "enter")
		logger.write("action_typekey enter ", tmp)
	elif option == "img":
		tmp = rs.action_type(key, img)
		logger.write("action_type to image " + str(key) + " " + img, tmp)
	elif option == "select_all":
		tmp = rs.action_select_all_key()
		logger.write("action_select_all_key", tmp)
	elif option == "alt_f4":
		tmp = rs.action_close_by_key()
		logger.write("action_close_by_key", tmp)
	return tmp

def check_imagelist(img_string):
	img_list = img_string.split('/')
	count = 0
	for img in img_list:
		tmp = rs.action_check(case_info.case_id + "\\" + img)
		logger.write(case_info.case_id + "\\" + img, tmp)
		if tmp == 0:
			count = count + 1
	if count == len(img_list):
		tmp = 0
	else:
		tmp = 1
	return tmp

def check_point(is_take_effect = True):
	if is_take_effect == True:
		if case_info.result == 0:
			result = 'pass'
			comments = case_info.comments
		elif case_info.result == 1:
			result = 'fail'
			comments = case_info.comments
		elif len(case_info.result) > 1:
			comments = case_info.result
			result = 'fail'
		screeshot_path = current_path + '\\screenshot\\iteration_' + str(case_info.iterate_num) + '\\' + case_info.case_id + '.png'
		rs.action_capture(screeshot_path)
		# run_time_string = '<Time_Taken>' + str(case_info.run_time) + '</Time_Taken>'
		# result_string = '<Result>' + result + '</Result>'
		# comments_string = '<Comments>' + comments + '</Comments>'
		write_to_xml(case_info.result_file_path, case_info.case_id, "Time_Taken", str(case_info.run_time))
		write_to_xml(case_info.result_file_path, case_info.case_id, "Result", result)
		write_to_xml(case_info.result_file_path, case_info.case_id, "comments", comments)
		logger.write('[check point] time_taken', str(case_info.run_time))
		logger.write('[check point] result', result)
		logger.write('[check point] comments', comments)
		logger.write('[check point] screeshot_path', screeshot_path)

def get_iteration_number(path):
	xml_doc = XmlDocument()
	xml_doc.Load(path)
	root = xml_doc.DocumentElement
	first_node = root.FirstChild
	return first_node.InnerText
	# tree = ET.parse(os.path.normcase(path))
	# root = tree.getroot()
	# return root.find('Iteration').text

def get_all_testcase(path):
	case_list = []
	xml_doc = XmlDocument()
	xml_doc.Load(path)
	root = xml_doc.DocumentElement
	for child_node in root.ChildNodes:
		if child_node.LocalName == "TestCase":
			case_list.append(child_node)
	return case_list
	# tree = ET.parse(os.path.normcase(path))
	# root = tree.getroot()
	# return root.findall('TestCase')

def write_to_xml(path, case_id, node_name, node_text):
	xml_doc = XmlDocument()
	xml_doc.Load(path)
	root = xml_doc.DocumentElement
	for child_node in root.ChildNodes:
		if child_node.LocalName == "TestCase":
			id_node = child_node.SelectSingleNode("ID")
			if id_node.InnerText == case_id:
				newnode = xml_doc.CreateElement(node_name)
				newnode.InnerText = node_text
				child_node.AppendChild(newnode)
	xml_doc.Save(path)
	# tree = ET.parse(os.path.normcase(path))
	# root = tree.getroot()
	# for child in root.findall('TestCase'):
	# 	if child.find('ID').text == case_id:
	# 		child.append(fromstring(string))
	# tree.write(os.path.normcase(path))

def all_files(root, patterns='*', single_level=True, yield_folders=False):
	files_list = []
	patterns_list = []
	if patterns.find(';') != -1:
		patterns_list = patterns.split(';')
	else:
		patterns_list.append(patterns)
	for path, dirs, files in os.walk(os.path.normcase(root)):
		if yield_folders:
			files.extend(dirs)
		files.sort()
		for name in files:
			for pattern in patterns_list:
				if fnmatch.fnmatch(name, pattern):
					files_list.append(os.path.join(path, name))
					break
		if single_level:
			break
	return files_list

def kill_process():
	if os.popen("tasklist").read().find('Mobogenie.exe') != -1:
		os.system("taskkill /im Mobogenie.exe /f")
	if os.popen("tasklist").read().find('mgadb.exe') != -1:
		os.system("taskkill /im mgadb.exe /f")
	if os.popen("tasklist").read().find('DaemonProcess.exe') != -1:
		os.system("taskkill /im DaemonProcess.exe /f")

def delete_dir(path):
	if os.path.exists(path):
		shutil.rmtree(path)
		os.makedirs(path)




	



