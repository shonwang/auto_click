# coding=utf-8

from client import *
from script import *
import time
import os
import sys
import shutil

def start_test():
	#杀死当前运行的mobogenie进程
	kill_process()
	screenshot_dir = os.path.normcase(current_path + r'/screenshot/')
	delete_dir(screenshot_dir)
	#获取配置文件
	config_files = all_files(current_path + os.path.normcase(r'/config/'), '*.xml', True, False)
	config_name = config_files[0].split('\\')[len(config_files[0].split('\\')) - 1][:-4]
	iteration = get_iteration_number(config_files[0])
	logger.write("config file name", config_files[0])
	logger.write("total iteration", iteration)
	nodes = get_all_testcase(os.path.normcase(config_files[0]))
	#开始迭代
	for num in range(int(iteration)):
		case_info.iterate_num = num
		logger.write("current iteration", str(num))
		#创建当前迭代轮数的截图文件夹和结果文件
		screenshot_path = screenshot_dir +'iteration_' + str(num)
		if not os.path.exists(screenshot_path):
			os.mkdir(screenshot_path)
		case_info.result_file_path = current_path + r'\\result\\' + config_name +'_iteration_' + str(num) + '.xml'
		shutil.copyfile(config_files[0], case_info.result_file_path)
		#读取用例信息开始测试
		try: 
			for child in nodes:
				case_info.case_id = child.SelectSingleNode("ID").InnerText
				module = child.SelectSingleNode("Module").InnerText
				des = child.SelectSingleNode("Test_Case_Description").InnerText
				expect = child.SelectSingleNode("Expected_Result").InnerText
				parameter = child.SelectSingleNode("Parameter").InnerText
				script_name = child.SelectSingleNode("Test_Script_Name").InnerText
				option = child.SelectSingleNode("Option").InnerText
				# module = child.find('Module').text
				# des = child.find('Test_Case_Description').text
				# expect = child.find('Expected_Result').text
				# parameter = child.find('Parameter').text
				# script_name = child.find('Test_Script_Name').text
				# option = child.find('Option').text
				logger.write("ID", case_info.case_id)
				logger.write("Module", module)
				logger.write("Test case description", des)
				logger.write("Expected result", expect)
				logger.write("Parameter", parameter)
				logger.write("Test script name", script_name)
				logger.write("Option", option)
				if script_name != '' and option != 'ignore':
					logger.write("execute", script_name)
					start_time = time.time()
					#eval(script_name)(num, case_id, parameter)
					eval('test_ttt')(parameter)
					stop_time = time.time()
					case_info.run_time = float(stop_time - start_time)
					check_point()
			rs.action_wait2(2)		
			kill_process()
			rs.action_wait2(10)
		except Exception as e:
			logger.write(str(e), 1)
			kill_process()

if __name__ == "__main__":
	reload(sys) 
	sys.setdefaultencoding('utf-8')
	start_test()