# coding=utf-8

from client import *
import time
import os

def tear_down(result, comments):
	logger.write(comments, result)
	case_info.result = result
	case_info.comments = comments

def set_up():
	pass

def test_ttt(parameter):
	try:
		#kill_process()
		tmp = wait_check_click("icon-apps.png", 2)
		tmp = wait_check("icon-apps.png", 2)
		case_info.result = tmp
	except Exception as e:
		tear_down(1, str(e))

def test_launch_client(parameter):
	try:
		kill_process()
		os.startfile(os.path.normcase(parameter[0]))
		sleep(2)
		image_str = "logo.png/video_1.png/video_2.png/video_3.png"
		tmp = check_imagelist(image_str)
		case_info.result = tmp
	except Exception as e:
		tear_down(1, str(e))

def test_check_homepage(parameter):
	try:
		wait_image(case_info.case_id + "\\" + "manage.png", 10)
		image_str = "manage.png/title.png/tool.png"
		tmp = check_imagelist(image_str)
		case_info.result = tmp
	except Exception as e:
		tear_down(1, str(e))