# coding=utf-8

from client import *
import time
import os

def test_ttt(parameter):
	try:
		os.startfile(os.path.normcase(parameter))
		tmp = rs.action_wait("page-help.png", 5)
		logger.write("action_wait page-help.png", tmp)
		tmp = rs.action_check("page-help.png")
		logger.write("action_check page-help.png", tmp)
		case_info.result = tmp
	except Exception as e:
		logger.write(str(e), 1)
		case_info.result = 1
		case_info.comments = str(e)

#主界面
def launch_mobo_client(num, case_id, parameter, take_effect = True):
	try:
		os.startfile(os.path.normcase(parameter))
		tmp = rs.action_wait("page-help.png", 20)
		logger.write("action_wait page-help.png", tmp)
		tmp = rs.action_check("page-help.png")
		logger.write("action_check page-help.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def check_homepage(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("popup-bind.png", 5)
		logger.write("action_wait popup-bind.png", tmp)
		tmp = rs.action_check("popup-bind.png")
		logger.write("action_check popup-bind.png", tmp)
		if tmp == 0:
			tmp = rs.action_click("button-bind-cancel.png")
			logger.write("action_click button-bind-cancel.png", tmp)	
		tmp = rs.action_wait("page-home.png", 60)
		logger.write("action_wait page-home.png", tmp)
		tmp = rs.action_check("page-home.png")
		logger.write("action_check page-home.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def hover_title_icon(img1, img2, num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait(img1, 5)
		logger.write("action_wait " + img1, tmp)
		tmp = rs.action_check(img1)
		logger.write("action_check " + img1, tmp)
		tmp = rs.action_hover(img1)
		logger.write("action_hover " + img1, tmp)
		tmp = rs.action_wait(img2, 5)
		logger.write("action_wait " + img2, tmp)
		tmp = rs.action_check(img2)
		logger.write("action_check " + img2, tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def click_title_icon(img1, img2, num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_click(img1)
		logger.write("action_click " + img1, tmp)
		tmp = rs.action_wait(img2, 5)
		logger.write("action_wait " + img2, tmp)
		tmp = rs.action_check(img2)
		logger.write("action_check " + img2, tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def hover_showcase(num, case_id, parameter):
	hover_title_icon("icon-showcase.png", "icon-showcase-highlight.png", num, case_id, parameter)

def click_showcase(num, case_id, parameter):
	click_title_icon("icon-showcase-highlight.png", "page-showcase.png", num, case_id, parameter)

def hover_myphone(num, case_id, parameter, take_effect = True):
	hover_title_icon("icon-myphone.png", "icon-myphone-highlight.png", num, case_id, parameter, take_effect)

def click_myphone(num, case_id, parameter, take_effect = True):
	click_title_icon("icon-myphone-highlight.png", "page-home.png", num, case_id, parameter, take_effect)

def hover_apps(num, case_id, parameter):
	hover_title_icon("icon-apps.png", "icon-apps-highlight.png", num, case_id, parameter)

def click_apps(num, case_id, parameter):
	click_title_icon("icon-apps-highlight.png", "page-apps.png", num, case_id, parameter)

def hover_games(num, case_id, parameter):
	hover_title_icon("icon-games.png", "icon-games-highlight.png", num, case_id, parameter)

def click_games(num, case_id, parameter):
	click_title_icon("icon-games-highlight.png", "page-games.png", num, case_id, parameter)

def hover_ringtones(num, case_id, parameter):
	hover_title_icon("icon-ringtones.png", "icon-ringtones-highlight.png", num, case_id, parameter)

def click_ringtones(num, case_id, parameter):
	click_title_icon("icon-ringtones-highlight.png", "page-ringtones.png", num, case_id, parameter)

def hover_wallpapers(num, case_id, parameter):
	hover_title_icon("icon-wallpapers.png", "icon-wallpapers-highlight.png", num, case_id, parameter)

def click_wallpapers(num, case_id, parameter):
	click_title_icon("icon-wallpapers-highlight.png", "page-wallpapers.png", num, case_id, parameter)

def hover_youtube(num, case_id, parameter):
	hover_title_icon("icon-youtube.png", "icon-youtube-highlight.png", num, case_id, parameter)

def click_youtube(num, case_id, parameter):
	click_title_icon("icon-youtube-highlight.png", "page-youtube.png", num, case_id, parameter)

#手机管理界面
def click_sdcard(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("icon-sdcard.png", 5)
		logger.write("action_wait icon-sdcard.png", tmp)
		tmp = rs.action_check("icon-sdcard.png")
		logger.write("action_check icon-sdcard.png", tmp)
		tmp = rs.action_click("icon-sdcard.png")
		logger.write("action_click icon-sdcard.png", tmp)
		img = ''
		if os_platform.find('XP') == -1:
			img = "window-win7-sdcard.png"
		else:
			img = 'window-xp-sdcard.png'
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		check_point(num, case_id, tmp, '', take_effect)
		rs.action_close_by_key()
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def click_management_icon(img, img_expect, num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait " + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check " + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click " + img, tmp)

		tmp = rs.action_wait(img_expect, 5)
		logger.write("action_wait " + img_expect, tmp)
		tmp = rs.action_check(img_expect)
		logger.write("action_check " + img_expect, tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def click_contacts_icon(num, case_id, parameter, take_effect = True):
	click_management_icon("icon-contacts.png", "page-contacts.png", num, case_id, parameter, take_effect)

def click_sms_icon(num, case_id, parameter, take_effect = True):
	click_management_icon("icon-sms.png", "page-sms.png", num, case_id, parameter, take_effect)
	click_myphone(num, case_id, parameter, False)

def click_appsgames_icon(num, case_id, parameter, take_effect = True):
	click_management_icon("icon-myapps.png", "page-appsgames.png", num, case_id, parameter, take_effect)
	click_myphone(num, case_id, parameter, False)

def click_music_icon(num, case_id, parameter, take_effect = True):
	click_management_icon("icon-music.png", "page-music.png", num, case_id, parameter, take_effect)
	click_myphone(num, case_id, parameter, False)

def click_pictures_icon(num, case_id, parameter, take_effect = True):
	click_management_icon("icon-pictures.png", "page-pictures.png", num, case_id, parameter, take_effect)
	click_myphone(num, case_id, parameter, False)

def click_videos_icon(num, case_id, parameter, take_effect = True):
	click_management_icon("icon-videos.png", "page-videos.png", num, case_id, parameter, take_effect)
	click_myphone(num, case_id, parameter, False)

def install_apk(num, case_id, parameter, take_effect = True):
	try:
		#先删除原有的Apps
		click_management_icon("icon-myapps.png", "page-appsgames.png", num, case_id, parameter, False)
		uninstall_all_apps(num, case_id, parameter, False)
		click_myphone(num, case_id, parameter, False)
		#点击新建按钮
		tmp = rs.action_wait("icon-insallapk.png", 5)
		logger.write("action_wait icon-insallapk.png", tmp)
		tmp = rs.action_check("icon-insallapk.png")
		logger.write("action_check icon-insallapk.png", tmp)
		tmp = rs.action_click("icon-insallapk.png")
		logger.write("action_click icon-insallapk.png", tmp)
		#点击 add files 按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-addfile.png", 5)
		logger.write("action_wait button-addfile.png", tmp)
		tmp = rs.action_check("button-addfile.png")
		logger.write("action_check button-addfile.png", tmp)
		tmp = rs.action_click("button-addfile.png")
		logger.write("action_click button-addfile.png", tmp)
		#键入Apps地址
		rs.action_wait2(2)
		apps_path = os.path.normcase(current_path + r'/resource/apps')
		tmp = rs.action_typekey(apps_path,'a')
		img = ''
		offset = -49
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
			offset = -90
		else:
			img = 'button-windows-xpopen.png'
			offset = -49
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click_offset(img, 0, offset)
		logger.write("action_click_offset" + img, tmp)
		rs.action_wait2(2)
		#选择全部Apps
		tmp = rs.action_select_all_key()
		rs.action_wait2(2)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)
		#点击确认按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-confirm-blue.png", 5)
		logger.write("action_wait button-confirm-blue.png", tmp)
		tmp = rs.action_check("button-confirm-blue.png")
		logger.write("action_check button-confirm-blue.png", tmp)
		tmp = rs.action_click("button-confirm-blue.png")
		logger.write("action_click button-confirm-blue.png", tmp)
		#等待安装成功，点击OK按钮
		rs.action_wait2(5)
		tmp = rs.action_wait("button-popup-ok.png", 600)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)
		#检查是否符合预期
		click_management_icon("icon-myapps.png", "page-appsgames.png", num, case_id, parameter, False)
		rs.action_wait2(5)
		tmp = rs.action_wait("page-installapps.png", 5)
		logger.write("action_wait page-installapps.png", tmp)
		tmp = rs.action_check("page-installapps.png")
		logger.write("action_check page-installapps.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
		hover_myphone(num, case_id, parameter, False)
		click_myphone(num, case_id, parameter, False)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

# 联系人模块
def quick_new_contact(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_type("tom","textbox-quick-name.png")
		logger.write("action_type textbox-quick-name.png", tmp)
		tmp = rs.action_type("13678901234","textbox-quick-mobile.png")
		logger.write("action_type textbox-quick-mobile.png", tmp)
		tmp = rs.action_type("123@163.com","textbox-quick-email.png")
		logger.write("action_type textbox-quick-email.png", tmp)

		tmp = rs.action_wait("button-save-contact.png", 5)
		logger.write("action_wait button-save-contact.png", tmp)
		tmp = rs.action_check("button-save-contact.png")
		logger.write("action_check button-save-contact.png", tmp)
		tmp = rs.action_click("button-save-contact.png")
		logger.write("action_click button-save-contact.png", tmp)

		rs.action_wait2(3)

		tmp = rs.action_wait("button-popup-close.png", 5)
		logger.write("action_wait button-popup-close.png", tmp)
		tmp = rs.action_check("button-popup-close.png")
		logger.write("action_check button-popup-close.png", tmp)
		tmp = rs.action_click("button-popup-close.png")
		logger.write("action_click button-popup-close.png", tmp)
		tmp = rs.action_wait("Item-new-contact.png", 5)
		logger.write("action_wait Item-new-contact.png", tmp)
		tmp = rs.action_check("Item-new-contact.png")
		logger.write("action_check Item-new-contact.png", tmp)
		tmp = rs.action_hover("Item-new-contact.png")
		logger.write("action_hover Item-new-contact.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def refresh(img, num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("button-contacts-refresh.png", 5)
		logger.write("action_wait button-contacts-refresh.png", tmp)
		tmp = rs.action_check("button-contacts-refresh.png")
		logger.write("check button-contacts-refresh.png", tmp)
		tmp = rs.action_click("button-contacts-refresh.png")
		logger.write("click button-contacts-refresh.png", tmp)
		if img != '':
			tmp = rs.action_wait(img, 30)
			logger.write("action_wait " + img, tmp)
			tmp = rs.action_check(img)
			logger.write("action_check " + img, tmp)
			check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def refresh_contacts(num, case_id, parameter, take_effect = True):
	refresh("Item-new-contact.png", num, case_id, parameter, take_effect)

def delete_one_contact(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("Item-new-contact.png", 5)
		logger.write("action_wait Item-new-contact.png", tmp)
		tmp = rs.action_check("Item-new-contact.png")
		logger.write("check Item-new-contact.png", tmp)
		if tmp == 1:
			tmp = rs.action_wait("Item-new-contact-sdcard.png", 5)
			logger.write("action_wait Item-new-contact-sdcard.png", tmp)
			tmp = rs.action_check("Item-new-contact-sdcard.png")
			logger.write("action_check Item-new-contact-sdcard.png", tmp)
			tmp = rs.action_click_offset("Item-new-contact-sdcard.png", -70, 6)
			logger.write("action_click_offset Item-new-contact-sdcard.png", tmp)
		else:
			tmp = rs.action_click_offset("Item-new-contact.png", -70, 6)
			logger.write("action_click_offset Item-new-contact.png", tmp)

		tmp = rs.action_wait("button-delete.png", 5)
		logger.write("action_wait button-delete.png", tmp)
		tmp = rs.action_check("button-delete.png")
		logger.write("action_check button-delete.png", tmp)
		tmp = rs.action_click("button-delete.png")
		logger.write("action_click button-delete.png", tmp)

		rs.action_wait2(2)

		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)

		tmp = rs.action_wait("page-contacts-deleteall.png", 5)
		logger.write("action_wait page-contacts-deleteall.png", tmp)
		tmp = rs.action_check("page-contacts-deleteall.png")
		logger.write("action_check page-contacts-deleteall.png", tmp)
		tmp = rs.action_hover("page-contacts-deleteall.png")
		logger.write("action_hover page-contacts-deleteall.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def new_contact(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("button-contacts-selectall.png", 5)
		logger.write("action_wait button-contacts-selectall.png", tmp)
		tmp = rs.action_check("button-contacts-selectall.png")
		logger.write("check button-contacts-selectall.png", tmp)
		tmp = rs.action_click("button-contacts-selectall.png")
		logger.write("click button-contacts-selectall.png", tmp)

		tmp = rs.action_wait("page-new-contacts.png", 5)
		logger.write("action_wait page-new-contacts.png", tmp)
		tmp = rs.action_check("page-new-contacts.png")
		logger.write("action_check page-new-contacts.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def cancel_new_contact(num, case_id, parameter, take_effect = True):
	try:
		new_contact(num, case_id, parameter, False)
		tmp = rs.action_wait("button-bind-cancel.png", 5)
		logger.write("action_wait button-bind-cancel.png", tmp)
		tmp = rs.action_check("button-bind-cancel.png")
		logger.write("check button-bind-cancel.png", tmp)
		tmp = rs.action_click("button-bind-cancel.png")
		logger.write("click button-bind-cancel.png", tmp)

		tmp = rs.action_wait("page-contacts.png", 5)
		logger.write("action_wait page-contacts.png", tmp)
		tmp = rs.action_check("page-contacts.png")
		logger.write("action_check page-contacts.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def change_portrait(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("button-contact-portrait.png", 5)
		logger.write("action_wait button-contact-portrait.png", tmp)
		tmp = rs.action_check("button-contact-portrait.png")
		logger.write("check button-contact-portrait.png", tmp)
		tmp = rs.action_click("button-contact-portrait.png")
		logger.write("click button-contact-portrait.png", tmp)

		rs.action_wait2(2)
		picture_path = os.path.normcase(current_path + r'/images')
		tmp = rs.action_typekey(picture_path,'a')
		rs.action_wait2(2)
		tmp = rs.action_typekey('icon-sdcard.png','abc')
		rs.action_wait2(2)

		img = ''
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
		else:
			img = 'button-windows-xpopen.png'

		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)

		tmp = rs.action_wait("button-contact-portrait-sdcard.png", 5)
		logger.write("action_wait button-contact-portrait-sdcard.png", tmp)
		tmp = rs.action_check("button-contact-portrait-sdcard.png")
		logger.write("action_check button-contact-portrait-sdcard.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def delete_contact_info(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("textbox-mobile.png", 5)
		logger.write("action_wait textbox-mobile.png", tmp)
		tmp = rs.action_check("textbox-mobile.png")
		logger.write("check textbox-mobile.png", tmp)
		#tmp = rs.action_type('13678901234',"textbox-mobile.png")
		#logger.write("action_type textbox-mobile.png", tmp)

		tmp = rs.action_click_offset("textbox-mobile.png", 143, 0)
		logger.write("action_click_offset textbox-mobile.png, 143, 0", tmp)
		tmp = rs.action_click_offset("textbox-mobile.png", 155, 0)

		tmp = rs.action_wait("page-new-contacts-info-delete-mobile.png", 5)
		logger.write("action_wait page-new-contacts-info-delete-mobile.png", tmp)
		tmp = rs.action_check("page-new-contacts-info-delete-mobile.png")
		logger.write("action_check page-new-contacts-info-delete-mobile.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def add_contact_info(num, case_id, parameter, take_effect = True):
	try:
		img = ''
		if os_platform.find('XP') == -1:
			img = "combobox-addother.png"
		else:
			img = 'combobox-XP-addother.png'

		tmp = rs.action_wait(img, 5)
		logger.write("action_wait " + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check " + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click " + img, tmp)

		tmp = rs.action_typekey('', 'down')
		rs.action_wait2(2)
		tmp = rs.action_typekey('')

		tmp = rs.action_wait("page-new-contacts-info-add-mobile.png", 5)
		logger.write("action_wait page-new-contacts-info-add-mobile.png", tmp)
		tmp = rs.action_check("page-new-contacts-info-add-mobile.png")
		logger.write("action_check page-new-contacts-info-add-mobile.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def fill_contact_info(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("textbox-name.png", 5)
		logger.write("action_wait textbox-name.png", tmp)
		tmp = rs.action_check("textbox-name.png")
		logger.write("action_check textbox-name.png", tmp)
		tmp = rs.action_type('Sikuli Script', "textbox-name.png")
		logger.write("action_type textbox-name.png", tmp)
		tmp = rs.action_type('Sikuli', "textbox-nickname.png")
		logger.write("action_type textbox-nickname.png", tmp)
		tmp = rs.action_type('13678901234',"textbox-mobile.png")
		logger.write("action_type textbox-mobile.png", tmp)
		tmp = rs.action_type('13578901234',"textbox-workmobile.png")
		logger.write("action_type textbox-workmobile.png", tmp)
		tmp = rs.action_type('010-67890123',"textbox-worknum.png")
		logger.write("action_type textbox-worknum.png", tmp)
		tmp = rs.action_type('010-67891234',"textbox-homenum.png")
		logger.write("action_type textbox-homenum.png", tmp)
		tmp = rs.action_type('sikuli-dev@lists.csail.mit.edu',"textbox-homemail.png")
		logger.write("action_type textbox-homemail.png", tmp)
		tmp = rs.action_type('hello world~',"textbox-note.png")
		logger.write("action_type textbox-note.png", tmp)

		tmp = rs.action_click("button-save-contact.png")
		logger.write("action_click button-save-contact.png", tmp)
		rs.action_wait2(2)
		tmp = rs.action_wait("button-popup-close.png", 5)
		logger.write("action_wait button-popup-close.png", tmp)
		tmp = rs.action_check("button-popup-close.png")
		logger.write("action_check button-popup-close.png", tmp)
		tmp = rs.action_click("button-popup-close.png")
		logger.write("action_click button-popup-close.png", tmp)
		rs.action_wait2(2)
		tmp = rs.action_wait("Item-new-contact-sdcard.png", 5)
		logger.write("action_wait Item-new-contact-sdcard.png", tmp)
		tmp = rs.action_check("Item-new-contact-sdcard.png")
		logger.write("action_check Item-new-contact-sdcard.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
		refresh("Item-new-contact-sdcard.png",num, case_id, parameter, False)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def edit_contact(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("Item-new-contact-sdcard.png", 5)
		logger.write("action_wait Item-new-contact-sdcard.png", tmp)
		tmp = rs.action_check("Item-new-contact-sdcard.png")
		logger.write("action_check Item-new-contact-sdcard.png", tmp)
		tmp = rs.action_click_offset("Item-new-contact-sdcard.png", -65, 5)
		logger.write("action_click_offset Item-new-contact-sdcard.png", tmp)

		tmp = rs.action_wait("button-contact-edit.png", 5)
		logger.write("action_wait button-contact-edit.png", tmp)
		tmp = rs.action_check("button-contact-edit.png")
		logger.write("action_check button-contact-edit.png", tmp)
		tmp = rs.action_click("button-contact-edit.png")
		logger.write("action_click button-contact-edit.png", tmp)

		tmp = rs.action_wait("textbox-name-sikuli.png", 5)
		logger.write("action_wait textbox-name-sikuli.png", tmp)
		tmp = rs.action_check("textbox-name-sikuli.png")
		logger.write("action_check textbox-name-sikuli.png", tmp)

		tmp = rs.action_type('Automation',"textbox-name-sikuli.png")
		logger.write("action_type textbox-name-sikuli.png", tmp)

		tmp = rs.action_click("button-save-contact.png")
		logger.write("action_click button-save-contact.png", tmp)
		rs.action_wait2(2)
		tmp = rs.action_wait("button-popup-close.png", 5)
		logger.write("action_wait button-popup-close.png", tmp)
		tmp = rs.action_check("button-popup-close.png")
		logger.write("action_check button-popup-close.png", tmp)
		tmp = rs.action_click("button-popup-close.png")
		logger.write("action_click button-popup-close.png", tmp)

		tmp = rs.action_wait("page-after-edit.png", 5)
		logger.write("action_wait page-after-edit.png", tmp)
		tmp = rs.action_check("page-after-edit.png")
		logger.write("action_check page-after-edit.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
		refresh("Item-new-contact-sdcard.png",num, case_id, parameter, False)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def delete_all_contact(num, case_id, parameter, take_effect = True):
	try:
		#点击手机管理界面的联系人图标
		tmp = rs.action_wait("icon-contacts.png", 5)
		logger.write("action_wait icon-contacts.png", tmp)
		tmp = rs.action_check("icon-contacts.png")
		logger.write("action_check icon-contacts.png", tmp)
		tmp = rs.action_click("icon-contacts.png")
		logger.write("action_click icon-contacts.png", tmp)
		#点击全选
		tmp = rs.action_wait("button-contacts-selectall.png", 5)
		logger.write("action_wait button-contacts-selectall.png", tmp)
		tmp = rs.action_check("button-contacts-selectall.png")
		logger.write("action_check button-contacts-selectall.png", tmp)
		tmp = rs.action_click_offset("button-contacts-selectall.png", -55, 0)
		logger.write("action_click_offset button-contacts-selectall.png", tmp)
		#点击删除
		tmp = rs.action_wait("button-delete.png", 5)
		logger.write("action_wait button-delete.png", tmp)
		tmp = rs.action_check("button-delete.png")
		logger.write("action_check button-delete.png", tmp)
		tmp = rs.action_click("button-delete.png")
		logger.write("action_click button-delete.png", tmp)

		rs.action_wait2(2)
		#确认删除
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#检查删除后是否出现期望的页面
		tmp = rs.action_wait("page-contacts-deleteall.png", 600)
		logger.write("action_wait page-contacts-deleteall.png", tmp)
		tmp = rs.action_check("page-contacts-deleteall.png")
		logger.write("action_check page-contacts-deleteall.png", tmp)
		tmp = rs.action_hover("page-contacts-deleteall.png")
		logger.write("action_hover page-contacts-deleteall.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
		refresh("page-contacts-deleteall.png",num, case_id, parameter, False)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def import_contacts(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("button-import.png", 5)
		logger.write("action_wait button-import.png", tmp)
		tmp = rs.action_check("button-import.png")
		logger.write("action_check button-import.png", tmp)
		tmp = rs.action_click("button-import.png")
		logger.write("click button-import.png", tmp)

		rs.action_wait2(2)

		tmp = rs.action_wait("button-popup-view.png", 5)
		logger.write("action_wait button-popup-view.png", tmp)
		tmp = rs.action_check("button-popup-view.png")
		logger.write("action_check button-popup-view.png", tmp)
		tmp = rs.action_click("button-popup-view.png")
		logger.write("action_click button-popup-view.png", tmp)

		rs.action_wait2(2)
		vcf_path = os.path.normcase(current_path + r'/resource/contacts')
		tmp = rs.action_typekey(vcf_path,'a')
		rs.action_wait2(2)
		tmp = rs.action_typekey('contact.vcf','abc')
		rs.action_wait2(2)

		img = ''
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
		else:
			img = 'button-windows-xpopen.png'

		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)

		tmp = rs.action_wait("button-popup-next.png", 5)
		logger.write("action_wait button-popup-next.png", tmp)
		tmp = rs.action_check("button-popup-next.png")
		logger.write("action_check button-popup-next.png", tmp)
		tmp = rs.action_click("button-popup-next.png")
		logger.write("action_click button-popup-next.png", tmp)

		rs.action_wait2(5)

		tmp = rs.action_wait("button-contacts-popup-ok.png", 150)
		logger.write("action_wait button-contacts-popup-ok.png", tmp)
		tmp = rs.action_check("button-contacts-popup-ok.png")
		logger.write("action_check button-contacts-popup-ok.png", tmp)
		tmp = rs.action_click_offset("button-contacts-popup-ok.png", -30, 0)
		logger.write("action_click_offset button-contacts-popup-ok.png", tmp)

		tmp = rs.action_wait("page-contacts-import.png", 5)
		logger.write("action_wait page-contacts-import.png", tmp)
		tmp = rs.action_check("page-contacts-import.png")
		logger.write("action_check page-contacts-import.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def export_contacts(num, case_id, parameter, take_effect = True):
	try:
		#选中所有联系人
		tmp = rs.action_wait("button-contacts-selectall.png", 5)
		logger.write("action_wait button-contacts-selectall.png", tmp)
		tmp = rs.action_check("button-contacts-selectall.png")
		logger.write("action_check button-contacts-selectall.png", tmp)
		tmp = rs.action_click_offset("button-contacts-selectall.png", -55, 0)
		logger.write("action_click_offset button-contacts-selectall.png", tmp)
		#点击 export 按钮
		tmp = rs.action_wait("button-export.png", 5)
		logger.write("action_wait button-export.png", tmp)
		tmp = rs.action_check("button-export.png")
		logger.write("action_check button-export.png", tmp)
		tmp = rs.action_click("button-export.png")
		logger.write("action_click button-export.png", tmp)
		#默认路径，点击确定
		img = ''
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
		else:
			img = 'button-windows-xp.png'

		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)

		rs.action_wait2(5)
		#点击OK按钮
		logger.write("wait for exporting, timeout 150", tmp)
		tmp = rs.action_wait("button-popup-ok.png", 150)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)
		#检查目录下是否有导出文件
		export_file_list = all_files(os.path.expanduser('~'), 'contact*.vcf', True, False)
		logger.write("export_file_list", len(export_file_list))
		if len(export_file_list) > 0:
			tmp = 0
			for export_file in export_file_list:
				os.remove(export_file)
				logger.write("export_file", export_file)
		else:
			tmp = 1
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

# Apps&Games 模块
def click_left_menu(img, img_expect, num, case_id, parameter, take_effect = True):
	try:
		#点击左侧菜单栏里的按钮
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait " + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check " + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click " + img, tmp)
		#检查是否出现期望的界面
		tmp = rs.action_wait(img_expect, 5)
		logger.write("action_wait " + img_expect, tmp)
		tmp = rs.action_check(img_expect)
		logger.write("action_check " + img_expect, tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def click_menu_apps(num, case_id, parameter, take_effect = True):
	click_left_menu("button-menu-apps.png", "page-appsgames.png", num, case_id, parameter, take_effect)

def uninstall_all_apps(num, case_id, parameter, take_effect = True):
	try:
		#选中所有Apps
		tmp = rs.action_wait("button-apps-newapps.png", 5)
		logger.write("action_wait button-apps-newapps.png", tmp)
		tmp = rs.action_check("button-apps-newapps.png")
		logger.write("action_check button-apps-newapps.png", tmp)
		tmp = rs.action_click_offset("button-apps-newapps.png", -49, 0)
		logger.write("action_click_offset button-apps-newapps.png", tmp)
		#点击卸载按钮
		tmp = rs.action_wait("button-delete.png", 5)
		logger.write("action_wait button-delete.png", tmp)
		tmp = rs.action_check("button-delete.png")
		logger.write("action_check button-delete.png", tmp)
		tmp = rs.action_click("button-delete.png")
		logger.write("action_click button-delete.png", tmp)
		#确认删除
		rs.action_wait2(2)
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#检查删除后在apps栏是否出现期望的页面
		tmp = rs.action_wait("page-apps-uninstallall.png", 500)
		logger.write("action_wait page-apps-uninstallall.png", tmp)
		tmp = rs.action_check("page-apps-uninstallall.png")
		logger.write("action_check page-apps-uninstallall.png", tmp)
		#进入updates栏
		img = ''
		if os_platform.find('XP') == -1:
			img = "button-apps-appstab-win7.png"
		else:
			img = 'button-apps-appstab.png'
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait " + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check " + img, tmp)
		tmp = rs.action_click_offset(img, 110, 0)
		logger.write("action_click_offset " + img, tmp)
		#检查删除后在updates栏是否出现期望的页面
		tmp_2 = rs.action_wait("page-apps-updatestab-uninstallall.png", 60)
		logger.write("action_wait page-apps-updatestab-uninstallall.png", tmp_2)
		tmp_2 = rs.action_check("page-apps-updatestab-uninstallall.png")
		logger.write("action_check page-apps-updatestab-uninstallall.png", tmp_2)
		if tmp + tmp_2 > 0:
			tmp = 1
		else:
			tmp = tmp + tmp_2
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def refresh_apps(num, case_id, parameter, take_effect = True):
	refresh('', num, case_id, parameter, False)
	rs.action_wait2(5)
	img = ''
	if os_platform.find('XP') == -1:
		img = "button-apps-appstab-win7.png"
	else:
		img = 'button-apps-appstab.png'
	tmp = rs.action_wait(img, 5)
	logger.write("action_wait " + img, tmp)
	tmp = rs.action_check(img)
	logger.write("action_check " + img, tmp)
	tmp = rs.action_click_offset(img, 110, 0)
	logger.write("action_click_offset " + img, tmp)
	#检查删除后在updates栏是否出现期望的页面
	tmp_2 = rs.action_wait("page-apps-updatestab-uninstallall.png", 60)
	logger.write("action_wait page-apps-updatestab-uninstallall.png", tmp_2)
	tmp_2 = rs.action_check("page-apps-updatestab-uninstallall.png")
	logger.write("action_check page-apps-updatestab-uninstallall.png", tmp_2)
	if tmp + tmp_2 > 0:
		tmp = 1
	else:
		tmp = tmp + tmp_2
	check_point(num, case_id, tmp, '', take_effect)

def new_apps(num, case_id, parameter, take_effect = True):
	try:
		#点击新建按钮
		tmp = rs.action_wait("button-apps-newapps.png", 5)
		logger.write("action_wait button-apps-newapps.png", tmp)
		tmp = rs.action_check("button-apps-newapps.png")
		logger.write("action_check button-apps-newapps.png", tmp)
		tmp = rs.action_click("button-apps-newapps.png")
		logger.write("action_click button-apps-newapps.png", tmp)
		#点击 add files 按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-addfile.png", 5)
		logger.write("action_wait button-addfile.png", tmp)
		tmp = rs.action_check("button-addfile.png")
		logger.write("action_check button-addfile.png", tmp)
		tmp = rs.action_click("button-addfile.png")
		logger.write("action_click button-addfile.png", tmp)
		#键入Apps地址
		rs.action_wait2(2)
		apps_path = os.path.normcase(current_path + r'/resource/apps')
		tmp = rs.action_typekey(apps_path,'a')
		img = ''
		offset = -49
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
			offset = -100
		else:
			img = 'button-windows-xpopen.png'
			offset = -49
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click_offset(img, 0, offset)
		logger.write("action_click_offset" + img, tmp)
		rs.action_wait2(2)
		#选择全部Apps
		tmp = rs.action_select_all_key()
		rs.action_wait2(2)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)
		#点击确认按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-confirm-blue.png", 5)
		logger.write("action_wait button-confirm-blue.png", tmp)
		tmp = rs.action_check("button-confirm-blue.png")
		logger.write("action_check button-confirm-blue.png", tmp)
		tmp = rs.action_click("button-confirm-blue.png")
		logger.write("action_click button-confirm-blue.png", tmp)
		#等待安装成功，点击OK按钮
		rs.action_wait2(5)
		tmp = rs.action_wait("button-popup-ok.png", 600)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)
		#检查是否符合预期
		tmp = rs.action_wait("page-installapps.png", 5)
		logger.write("action_wait page-installapps.png", tmp)
		tmp = rs.action_check("page-installapps.png")
		logger.write("action_check page-installapps.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def delete_one_apps(num, case_id, parameter, take_effect = True):
	try:
		#选中 360手机助手
		tmp = rs.action_wait("item-apps-360.png", 5)
		logger.write("action_wait item-apps-360.png", tmp)
		tmp = rs.action_check("item-apps-360.png")
		logger.write("action_check item-apps-360.png", tmp)
		tmp = rs.action_click_offset("item-apps-360.png", -65, 0)
		logger.write("action_click_offset item-apps-360.png", tmp)
		#点击卸载按钮
		img = ''
		if os_platform.find('XP') == -1:
			img = "button-apps-uninstall -win7.png"
		else:
			img = 'button-apps-uninstall.png'
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait " + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check " + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click " + img, tmp)
		#点击确认按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#检查apps列表中360的图标是否消失
		tmp = rs.action_wait("page-after-uninstall360.png", 60)
		logger.write("action_wait page-after-uninstall360.png", tmp)
		tmp = rs.action_check("page-after-uninstall360.png")
		logger.write("action_check page-after-uninstall360.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(logger, path, case_id, num, 1, comments)

def move_to_sd(num, case_id, parameter, take_effect = True):
	try:
		#选中app
		tmp = rs.action_wait("item-apps-office.png", 5)
		logger.write("action_wait item-apps-office.png", tmp)
		tmp = rs.action_check("item-apps-office.png")
		logger.write("action_check item-apps-office.png", tmp)
		tmp = rs.action_click_offset("item-apps-office.png", -23, 0)
		logger.write("action_click_offset item-apps-office.png", tmp)
		#点击移动到SD Card按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-apps-movesd.png", 5)
		logger.write("action_wait button-apps-movesd.png", tmp)
		tmp = rs.action_check("button-apps-movesd.png")
		logger.write("action_check button-apps-movesd.png", tmp)
		tmp = rs.action_click("button-apps-movesd.png")
		logger.write("action_click button-apps-movesd.png", tmp)
		#点击确认按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#等待完成，并点击Close按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-popup-close.png", 60)
		logger.write("action_wait button-popup-close.png", tmp)
		tmp = rs.action_check("button-popup-close.png")
		logger.write("action_check button-popup-close.png", tmp)
		tmp = rs.action_click("button-popup-close.png")
		logger.write("action_click button-popup-close.png", tmp)
		#检查是否显示为SD Card
		tmp = rs.action_wait("item-apps-carssd.png", 5)
		logger.write("action_wait item-apps-carssd.png", tmp)
		tmp = rs.action_check("item-apps-carssd.png")
		logger.write("action_check item-apps-carssd.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(logger, path, case_id, num, 1, comments)

def move_to_phone(num, case_id, parameter, take_effect = True):
	try:
		#点击移动到Phone memory按钮
		tmp = rs.action_wait("button-apps-movephone.png", 5)
		logger.write("action_wait button-apps-movephone.png", tmp)
		tmp = rs.action_check("button-apps-movephone.png")
		logger.write("action_check button-apps-movephone.png", tmp)
		tmp = rs.action_click("button-apps-movephone.png")
		logger.write("action_click button-apps-movephone.png", tmp)
		#点击确认按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#等待完成，并点击Close按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-popup-close.png", 60)
		logger.write("action_wait button-popup-close.png", tmp)
		tmp = rs.action_check("button-popup-close.png")
		logger.write("action_check button-popup-close.png", tmp)
		tmp = rs.action_click("button-popup-close.png")
		logger.write("action_click button-popup-close.png", tmp)
		#检查是否显示为Phone memory
		tmp = rs.action_wait("item-apps-carsphone.png", 5)
		logger.write("action_wait item-apps-carsphone.png", tmp)
		tmp = rs.action_check("item-apps-carsphone.png")
		logger.write("action_check item-apps-carsphone.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
		refresh('page-after-uninstall360.png', num, case_id, parameter, False)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(logger, path, case_id, num, 1, comments)

def export_apps(num, case_id, parameter, take_effect = True):
	try:
		#选中所有联系人
		tmp = rs.action_wait("button-apps-newapps.png", 5)
		logger.write("action_wait button-apps-newapps.png", tmp)
		tmp = rs.action_check("button-apps-newapps.png")
		logger.write("action_check button-apps-newapps.png", tmp)
		tmp = rs.action_click_offset("button-apps-newapps.png", -49, 0)
		logger.write("action_click_offset button-apps-newapps.png", tmp)
		#点击 export 按钮
		tmp = rs.action_wait("button-export.png", 5)
		logger.write("action_wait button-export.png", tmp)
		tmp = rs.action_check("button-export.png")
		logger.write("action_check button-export.png", tmp)
		tmp = rs.action_click("button-export.png")
		logger.write("action_click button-export.png", tmp)
		#默认路径，点击确定
		img = ''
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
		else:
			img = 'button-windows-xp.png'

		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)

		rs.action_wait2(5)
		#点击OK按钮
		logger.write("wait for exporting, timeout 300s", tmp)
		tmp = rs.action_wait("button-popup-ok.png", 300)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)
		#检查目录下是否有导出文件
		export_file_list = all_files(os.path.expanduser('~'), '*.apk', True, False)
		logger.write("export_file_list", len(export_file_list))
		if len(export_file_list) == 6:
			tmp = 0
		else:
			tmp = 1
		if len(export_file_list) > 0:
			for export_file in export_file_list:
				os.remove(export_file)
				logger.write("export_file", export_file)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

#短信模块
def click_menu_sms(num, case_id, parameter, take_effect = True):
	click_left_menu("button-menu-messages.png", "page-sms.png", num, case_id, parameter, take_effect)

def delete_all_sms(num, case_id, parameter, take_effect = True):
	try:
		#选中所有短信
		tmp = rs.action_wait("button-sms-selectall.png", 5)
		logger.write("action_wait button-sms-selectall.png", tmp)
		tmp = rs.action_check("button-sms-selectall.png")
		logger.write("action_check button-sms-selectall.png", tmp)
		tmp = rs.action_click_offset("button-sms-selectall.png", -40, 0)
		logger.write("action_click_offset button-sms-selectall.png", tmp)
		#点击删除按钮
		tmp = rs.action_wait("button-delete.png", 5)
		logger.write("action_wait button-delete.png", tmp)
		tmp = rs.action_check("button-delete.png")
		logger.write("action_check button-delete.png", tmp)
		tmp = rs.action_click("button-delete.png")
		logger.write("action_click button-delete.png", tmp)
		#确认删除
		rs.action_wait2(2)
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#检查删除后是否出现期望的页面
		rs.action_wait2(10)
		tmp = rs.action_wait("page-sms-deleteall.png", 150)
		logger.write("action_wait page-sms-deleteall.png", tmp)
		tmp = rs.action_check("page-sms-deleteall.png")
		logger.write("action_check page-sms-deleteall.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(logger, path, case_id, num, 1, comments)

def refresh_sms(num, case_id, parameter, take_effect = True):
	refresh('page-sms-deleteall.png', num, case_id, parameter, True)

def import_sms(num, case_id, parameter, take_effect = True):
	try:
		#点击import按钮
		tmp = rs.action_wait("button-import.png", 5)
		logger.write("action_wait button-import.png", tmp)
		tmp = rs.action_check("button-import.png")
		logger.write("action_check button-import.png", tmp)
		tmp = rs.action_click("button-import.png")
		logger.write("click button-import.png", tmp)
		#点击view按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-popup-view.png", 5)
		logger.write("action_wait button-popup-view.png", tmp)
		tmp = rs.action_check("button-popup-view.png")
		logger.write("action_check button-popup-view.png", tmp)
		tmp = rs.action_click("button-popup-view.png")
		logger.write("action_click button-popup-view.png", tmp)
		#键入短信文件的地址
		rs.action_wait2(2)
		vcf_path = os.path.normcase(current_path + r'/resource/sms')
		tmp = rs.action_typekey(vcf_path,'a')
		rs.action_wait2(2)
		tmp = rs.action_typekey('sms.csv','abc')
		rs.action_wait2(2)
		#点击打开按钮
		img = ''
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
		else:
			img = 'button-windows-xpopen.png'
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)
		#点击Next按钮
		tmp = rs.action_wait("button-popup-next.png", 5)
		logger.write("action_wait button-popup-next.png", tmp)
		tmp = rs.action_check("button-popup-next.png")
		logger.write("action_check button-popup-next.png", tmp)
		tmp = rs.action_click("button-popup-next.png")
		logger.write("action_click button-popup-next.png", tmp)
		#点击OK按钮
		rs.action_wait2(5)
		tmp = rs.action_wait("button-popup-ok.png", 150)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)

		tmp = rs.action_wait("page-sms-importcompleted.png", 5)
		logger.write("action_wait page-sms-importcompleted.png", tmp)
		tmp = rs.action_check("page-sms-importcompleted.png")
		logger.write("action_check page-sms-importcompleted.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def export_sms(num, case_id, parameter, take_effect = True):
	try:
		#选中所有短信
		tmp = rs.action_wait("button-sms-selectall.png", 5)
		logger.write("action_wait button-sms-selectall.png", tmp)
		tmp = rs.action_check("button-sms-selectall.png")
		logger.write("action_check button-sms-selectall.png", tmp)
		tmp = rs.action_click_offset("button-sms-selectall.png", -40, 0)
		logger.write("action_click_offset button-sms-selectall.png", tmp)
		#点击 export 按钮
		tmp = rs.action_wait("button-export.png", 5)
		logger.write("action_wait button-export.png", tmp)
		tmp = rs.action_check("button-export.png")
		logger.write("action_check button-export.png", tmp)
		tmp = rs.action_click("button-export.png")
		logger.write("action_click button-export.png", tmp)
		#默认路径，点击确定
		img = ''
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
		else:
			img = 'button-windows-xp.png'

		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)

		rs.action_wait2(5)
		#点击OK按钮
		tmp = rs.action_wait("button-popup-ok.png", 150)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)
		#检查目录下是否有导出文件
		export_file_list = all_files(os.path.expanduser('~'), '*.csv', True, False)
		logger.write("export_file_list", len(export_file_list))
		if len(export_file_list) > 0:
			tmp = 0
			for export_file in export_file_list:
				os.remove(export_file)
				logger.write("export_file", export_file)
		else:
			tmp = 1
		check_point(num, case_id, tmp, '', take_effect)
		refresh('page-sms-importcompleted.png', num, case_id, parameter, False)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

#音乐模块
def click_menu_music(num, case_id, parameter, take_effect = True):
	click_left_menu("button-menu-music.png", "page-music.png", num, case_id, parameter, take_effect)

def delete_all_music(num, case_id, parameter, take_effect = True):
	try:
		#选中所有音乐
		tmp = rs.action_wait("button-music-import.png", 5)
		logger.write("action_wait button-music-import.png", tmp)
		tmp = rs.action_check("button-music-import.png")
		logger.write("action_check button-music-import.png", tmp)
		tmp = rs.action_click_offset("button-music-import.png", -14, 0)
		logger.write("action_click_offset button-music-import.png", tmp)
		#点击删除按钮
		tmp = rs.action_wait("button-delete.png", 5)
		logger.write("action_wait button-delete.png", tmp)
		tmp = rs.action_check("button-delete.png")
		logger.write("action_check button-delete.png", tmp)
		tmp = rs.action_click("button-delete.png")
		logger.write("action_click button-delete.png", tmp)
		#确认删除
		rs.action_wait2(2)
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#检查删除后是否出现期望的页面
		tmp = rs.action_wait("page-music-deleteall.png", 150)
		logger.write("action_wait page-music-deleteall.png", tmp)
		tmp = rs.action_check("page-music-deleteall.png")
		logger.write("action_check page-music-deleteall.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def refresh_music(num, case_id, parameter, take_effect = True):
	refresh('page-music-deleteall.png', num, case_id, parameter, True)

def import_music(num, case_id, parameter, take_effect = True):
	try:
		#点击import按钮
		tmp = rs.action_wait("button-music-import.png", 5)
		logger.write("action_wait button-music-import.png", tmp)
		tmp = rs.action_check("button-music-import.png")
		logger.write("action_check button-music-import.png", tmp)
		tmp = rs.action_click_offset("button-music-import.png", 14, 0)
		logger.write("action_click_offset button-music-import.png", tmp)
		#点击 add files 按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-addfile.png", 5)
		logger.write("action_wait button-addfile.png", tmp)
		tmp = rs.action_check("button-addfile.png")
		logger.write("action_check button-addfile.png", tmp)
		tmp = rs.action_click("button-addfile.png")
		logger.write("action_click button-addfile.png", tmp)
		#键入Music地址
		rs.action_wait2(2)
		music_path = os.path.normcase(current_path + r'/resource/music')
		tmp = rs.action_typekey(music_path,'a')
		img = ''
		offset = -49
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
			offset = -100
		else:
			img = 'button-windows-xpopen.png'
			offset = -49
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click_offset(img, 0, offset)
		logger.write("action_click_offset" + img, tmp)
		rs.action_wait2(2)
		#选择全部Music
		tmp = rs.action_select_all_key()
		rs.action_wait2(2)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)
		#点击确认按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-confirm-blue.png", 5)
		logger.write("action_wait button-confirm-blue.png", tmp)
		tmp = rs.action_check("button-confirm-blue.png")
		logger.write("action_check button-confirm-blue.png", tmp)
		tmp = rs.action_click("button-confirm-blue.png")
		logger.write("action_click button-confirm-blue.png", tmp)
		#等待，点击OK按钮
		rs.action_wait2(5)
		tmp = rs.action_wait("button-popup-ok.png", 600)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)
		#检查是否符合预期
		tmp = rs.action_wait("page-music-import.png", 5)
		logger.write("action_wait page-music-import.png", tmp)
		tmp = rs.action_check("page-music-import.png")
		logger.write("action_check page-music-import.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

# 图片模块
def click_menu_pictures(num, case_id, parameter, take_effect = True):
	click_left_menu("button-menu-picture.png", "page-pictures.png", num, case_id, parameter, take_effect)

def delete_all_picture(num, case_id, parameter, take_effect = True):
	try:
		#选中所有图片
		tmp = rs.action_wait("button-pic-import.png", 5)
		logger.write("action_wait button-pic-import.png", tmp)
		tmp = rs.action_check("button-pic-import.png")
		logger.write("action_check button-pic-import.png", tmp)
		tmp = rs.action_click_offset("button-pic-import.png", -60, 0)
		logger.write("action_click_offset button-pic-import.png", tmp)
		#点击删除按钮
		tmp = rs.action_wait("button-delete.png", 5)
		logger.write("action_wait button-delete.png", tmp)
		tmp = rs.action_check("button-delete.png")
		logger.write("action_check button-delete.png", tmp)
		tmp = rs.action_click("button-delete.png")
		logger.write("action_click button-delete.png", tmp)
		#确认删除
		rs.action_wait2(2)
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#检查删除后是否出现期望的页面
		tmp = rs.action_wait("page-pic-deleteall.png", 150)
		logger.write("action_wait page-pic-deleteall.png", tmp)
		tmp = rs.action_check("page-pic-deleteall.png")
		logger.write("action_check page-pic-deleteall.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def refresh_picture(num, case_id, parameter, take_effect = True):
	refresh('page-pic-deleteall.png', num, case_id, parameter, True)

def import_picture(num, case_id, parameter, take_effect = True):
	try:
		#点击import按钮
		tmp = rs.action_wait("button-pic-import.png", 5)
		logger.write("action_wait button-pic-import.png", tmp)
		tmp = rs.action_check("button-pic-import.png")
		logger.write("action_check button-pic-import.png", tmp)
		tmp = rs.action_click("button-pic-import.png")
		logger.write("click button-pic-import.png", tmp)
		#点击 add files 按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-addfile.png", 5)
		logger.write("action_wait button-addfile.png", tmp)
		tmp = rs.action_check("button-addfile.png")
		logger.write("action_check button-addfile.png", tmp)
		tmp = rs.action_click("button-addfile.png")
		logger.write("action_click button-addfile.png", tmp)
		#键入Pictures地址
		rs.action_wait2(2)
		music_path = os.path.normcase(current_path + r'/resource/pictures')
		tmp = rs.action_typekey(music_path,'a')
		img = ''
		offset = -49
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
			offset = -100
		else:
			img = 'button-windows-xpopen.png'
			offset = -49
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click_offset(img, 0, offset)
		logger.write("action_click_offset" + img, tmp)
		rs.action_wait2(2)
		#选择全部pictures
		tmp = rs.action_select_all_key()
		rs.action_wait2(2)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)
		#点击确认按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-confirm-blue.png", 5)
		logger.write("action_wait button-confirm-blue.png", tmp)
		tmp = rs.action_check("button-confirm-blue.png")
		logger.write("action_check button-confirm-blue.png", tmp)
		tmp = rs.action_click("button-confirm-blue.png")
		logger.write("action_click button-confirm-blue.png", tmp)
		#等待，点击OK按钮
		rs.action_wait2(5)
		tmp = rs.action_wait("button-popup-ok.png", 150)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)
		refresh('', num, case_id, parameter, False)
		#检查是否符合预期
		tmp = rs.action_wait("page-pic-import.png", 5)
		logger.write("action_wait page-pic-import.png", tmp)
		tmp = rs.action_check("page-pic-import.png")
		logger.write("action_check page-pic-import.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
		refresh('', num, case_id, parameter, False)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def click_one_picture(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("page-pic-import.png", 5)
		logger.write("action_wait page-pic-import.png", tmp)
		tmp = rs.action_check("page-pic-import.png")
		logger.write("action_check page-pic-import.png", tmp)
		if tmp == 1:
			refresh('', num, case_id, parameter, False)
		tmp = rs.action_click("page-pic-import.png")
		logger.write("action_click page-pic-import.png", tmp)

		tmp = rs.action_wait("page-popup-pic.png", 30)
		logger.write("action_wait page-popup-pic.png", tmp)
		tmp = rs.action_check("page-popup-pic.png")
		logger.write("action_check page-popup-pic.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def close_big_picture(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("page-popup-pic.png", 5)
		logger.write("action_wait page-popup-pic.png", tmp)
		tmp = rs.action_check("page-popup-pic.png")
		logger.write("action_check page-popup-pic.png", tmp)
		tmp = rs.action_click_offset("page-popup-pic.png", 230, 136)
		logger.write("action_click_offset page-popup-pic.png", tmp)

		tmp = rs.action_wait("page-pic-import.png", 30)
		logger.write("action_wait page-pic-import.png", tmp)
		tmp = rs.action_check("page-pic-import.png")
		logger.write("action_check page-pic-import.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def delete_one_picture(num, case_id, parameter, take_effect = True):
	try:
		#选中其中一张图片
		tmp = rs.action_wait("page-pic-import.png", 5)
		logger.write("action_wait page-pic-import.png", tmp)
		tmp = rs.action_check("page-pic-import.png")
		logger.write("action_check page-pic-import.png", tmp)
		tmp = rs.action_click_offset("page-pic-import.png", 62, -66)
		logger.write("action_click_offset page-pic-import.png", tmp)
		#点击删除按钮
		tmp = rs.action_wait("button-delete.png", 5)
		logger.write("action_wait button-delete.png", tmp)
		tmp = rs.action_check("button-delete.png")
		logger.write("action_check button-delete.png", tmp)
		tmp = rs.action_click("button-delete.png")
		logger.write("action_click button-delete.png", tmp)
		#确认删除
		rs.action_wait2(2)
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#检查删除后是否出现期望的页面
		rs.action_wait2(2)
		tmp = rs.action_check("page-pic-import.png")
		logger.write("action_check page-pic-import.png", tmp)
		if tmp == 1:
			tmp = 0
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def export_picture(num, case_id, parameter, take_effect = True):
	try:
		#选中所有图片
		tmp = rs.action_wait("button-pic-import.png", 5)
		logger.write("action_wait button-pic-import.png", tmp)
		tmp = rs.action_check("button-pic-import.png")
		logger.write("action_check button-pic-import.png", tmp)
		tmp = rs.action_click_offset("button-pic-import.png", -60, 0)
		logger.write("action_click_offset button-pic-import.png", tmp)
		#点击 export 按钮
		tmp = rs.action_wait("button-export.png", 5)
		logger.write("action_wait button-export.png", tmp)
		tmp = rs.action_check("button-export.png")
		logger.write("action_check button-export.png", tmp)
		tmp = rs.action_click("button-export.png")
		logger.write("action_click button-export.png", tmp)
		#默认路径，点击确定
		img = ''
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
		else:
			img = 'button-windows-xp.png'

		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)

		rs.action_wait2(5)
		#点击OK按钮
		tmp = rs.action_wait("button-popup-ok.png", 150)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)
		#检查目录下是否有导出文件
		export_file_list = all_files(os.path.expanduser('~'), '*.jpg', True, False)
		logger.write("export_file_list", len(export_file_list))
		if len(export_file_list) == 11:
			tmp = 0
			for export_file in export_file_list:
				os.remove(export_file)
				logger.write("export_file", export_file)
		else:
			tmp = 1
		check_point(num, case_id, tmp, '', take_effect)
		refresh('', num, case_id, parameter, False)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

#视频模块
def click_menu_videos(num, case_id, parameter, take_effect = True):
	click_left_menu("button-menu-videos.png", "page-videos.png", num, case_id, parameter, take_effect)

def delete_all_videos(num, case_id, parameter, take_effect = True):
	try:
		#选中所有视频
		tmp = rs.action_wait("button-videos-import.png", 5)
		logger.write("action_wait button-videos-import.png", tmp)
		tmp = rs.action_check("button-videos-import.png")
		logger.write("action_check button-videos-import.png", tmp)
		tmp = rs.action_click_offset("button-videos-import.png", -53, 0)
		logger.write("action_click_offset button-videos-import.png", tmp)
		#点击删除按钮
		tmp = rs.action_wait("button-delete.png", 5)
		logger.write("action_wait button-delete.png", tmp)
		tmp = rs.action_check("button-delete.png")
		logger.write("action_check button-delete.png", tmp)
		tmp = rs.action_click("button-delete.png")
		logger.write("action_click button-delete.png", tmp)
		#确认删除
		rs.action_wait2(2)
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#检查删除后是否出现期望的页面
		tmp = rs.action_wait("page-videos-deleteall.png", 300)
		logger.write("action_wait page-videos-deleteall.png", tmp)
		tmp = rs.action_check("page-videos-deleteall.png")
		logger.write("action_check page-videos-deleteall.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def refresh_videos(num, case_id, parameter, take_effect = True):
	refresh('page-videos-deleteall.png', num, case_id, parameter, True)

def import_videos(num, case_id, parameter, take_effect = True):
	try:
		#点击import按钮
		tmp = rs.action_wait("button-videos-import.png", 5)
		logger.write("action_wait button-videos-import.png", tmp)
		tmp = rs.action_check("button-videos-import.png")
		logger.write("action_check button-videos-import.png", tmp)
		tmp = rs.action_click("button-videos-import.png")
		logger.write("click button-videos-import.png", tmp)
		#点击 add files 按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-addfile.png", 5)
		logger.write("action_wait button-addfile.png", tmp)
		tmp = rs.action_check("button-addfile.png")
		logger.write("action_check button-addfile.png", tmp)
		tmp = rs.action_click("button-addfile.png")
		logger.write("action_click button-addfile.png", tmp)
		#键入vedios 地址
		rs.action_wait2(2)
		music_path = os.path.normcase(current_path + r'/resource/vedios')
		tmp = rs.action_typekey(music_path,'a')
		img = ''
		offset = -49
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
			offset = -100
		else:
			img = 'button-windows-xpopen.png'
			offset = -49
		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click_offset(img, 0, offset)
		logger.write("action_click_offset" + img, tmp)
		rs.action_wait2(2)
		#选择全部vedios
		tmp = rs.action_select_all_key()
		rs.action_wait2(2)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)
		#点击确认按钮
		rs.action_wait2(2)
		tmp = rs.action_wait("button-confirm-blue.png", 5)
		logger.write("action_wait button-confirm-blue.png", tmp)
		tmp = rs.action_check("button-confirm-blue.png")
		logger.write("action_check button-confirm-blue.png", tmp)
		tmp = rs.action_click("button-confirm-blue.png")
		logger.write("action_click button-confirm-blue.png", tmp)
		#等待，点击OK按钮
		rs.action_wait2(5)
		tmp = rs.action_wait("button-popup-ok.png", 300)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)
		refresh('', num, case_id, parameter, False)
		rs.action_wait2(10)
		#检查是否符合预期
		tmp = rs.action_wait("page-video-importcompleted.png", 5)
		logger.write("action_wait page-video-importcompleted.png", tmp)
		tmp = rs.action_check("page-video-importcompleted.png")
		logger.write("action_check page-video-importcompleted.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
		refresh('', num, case_id, parameter, False)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def delete_one_video(num, case_id, parameter, take_effect = True):
	try:
		#选中其中一个视频
		tmp = rs.action_wait("page-video-importcompleted.png", 5)
		logger.write("action_wait page-video-importcompleted.png", tmp)
		tmp = rs.action_check("page-video-importcompleted.png")
		logger.write("action_check page-video-importcompleted.png", tmp)
		tmp = rs.action_click_offset("page-video-importcompleted.png", -64, -64)
		logger.write("action_click_offset page-video-importcompleted.png", tmp)
		#点击删除按钮
		tmp = rs.action_wait("button-delete.png", 5)
		logger.write("action_wait button-delete.png", tmp)
		tmp = rs.action_check("button-delete.png")
		logger.write("action_check button-delete.png", tmp)
		tmp = rs.action_click("button-delete.png")
		logger.write("action_click button-delete.png", tmp)
		#确认删除
		rs.action_wait2(2)
		tmp = rs.action_wait("button-contacts-confirm.png", 5)
		logger.write("action_wait button-contacts-confirm.png", tmp)
		tmp = rs.action_check("button-contacts-confirm.png")
		logger.write("action_check button-contacts-confirm.png", tmp)
		tmp = rs.action_click("button-contacts-confirm.png")
		logger.write("action_click button-contacts-confirm.png", tmp)
		#检查删除后是否出现期望的页面
		rs.action_wait2(2)
		tmp = rs.action_check("page-video-importcompleted.png")
		logger.write("action_check page-video-importcompleted.png", tmp)
		if tmp == 1:
			tmp = 0
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def export_videos(num, case_id, parameter, take_effect = True):
	try:
		#选中所有视频
		tmp = rs.action_wait("button-videos-import.png", 5)
		logger.write("action_wait button-videos-import.png", tmp)
		tmp = rs.action_check("button-videos-import.png")
		logger.write("action_check button-videos-import.png", tmp)
		tmp = rs.action_click_offset("button-videos-import.png", -53, 0)
		logger.write("action_click_offset button-videos-import.png", tmp)
		#点击 export 按钮
		tmp = rs.action_wait("button-export.png", 5)
		logger.write("action_wait button-export.png", tmp)
		tmp = rs.action_check("button-export.png")
		logger.write("action_check button-export.png", tmp)
		tmp = rs.action_click("button-export.png")
		logger.write("action_click button-export.png", tmp)
		#默认路径，点击确定
		img = ''
		if os_platform.find('XP') == -1:
			img = "button-windows.png"
		else:
			img = 'button-windows-xp.png'

		tmp = rs.action_wait(img, 5)
		logger.write("action_wait" + img, tmp)
		tmp = rs.action_check(img)
		logger.write("action_check" + img, tmp)
		tmp = rs.action_click(img)
		logger.write("action_click" + img, tmp)

		rs.action_wait2(5)
		#点击OK按钮
		tmp = rs.action_wait("button-popup-ok.png", 150)
		logger.write("action_wait button-popup-ok.png", tmp)
		tmp = rs.action_check("button-popup-ok.png")
		logger.write("action_check button-popup-ok.png", tmp)
		tmp = rs.action_click("button-popup-ok.png")
		logger.write("action_click button-popup-ok.png", tmp)
		#检查目录下是否有导出文件
		export_file_list = all_files(os.path.expanduser('~'), '*.3gp;*.mp4;*.avi;*.m4v', True, False)
		logger.write("export_file_list", len(export_file_list))
		if len(export_file_list) == 7:
			tmp = 0
		else:
			tmp = 1
		if len(export_file_list) > 0:
			for export_file in export_file_list:
				os.remove(export_file)
				logger.write("export_file", export_file)
		check_point(num, case_id, tmp, '', take_effect)
		refresh('', num, case_id, parameter, False)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)










def click_backup(num, case_id, parameter, take_effect = True):
	try:
		tmp = rs.action_wait("icon-backup.png", 5)
		logger.write("action_wait icon-backup.png", tmp)
		tmp = rs.action_check("icon-backup.png")
		logger.write("check icon-backup", tmp)
		tmp = rs.action_click("icon-backup.png")
		logger.write("click icon-backup", tmp)
		tmp = rs.action_wait("popup-backup.png", 5)
		logger.write("action_wait icon-backup.png", tmp)
		tmp = rs.action_check("popup-backup.png")
		logger.write("action_check icon-backup.png", tmp)
		check_point(num, case_id, tmp, '', take_effect)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(num, case_id, 1, '', take_effect)

def backup_all_data(logger, path, num, parameter, case_id):
	try:
		comments = ''
		#选择全部数据
		tmp = rs.action_wait("button-backup-selectall.png", 5)
		tmp = rs.action_check("button-backup-selectall.png")
		logger.write("check button-backup-selectall", tmp)
		tmp = rs.action_click_offset("button-backup-selectall.png",-29,-3)
		logger.write("click button-backup-selectall", tmp)
		#点击change按钮
		tmp = rs.action_wait("button-backupchange.png", 5)
		tmp = rs.action_check("button-backupchange.png")
		tmp = rs.action_click("button-backupchange.png")
		logger.write("click button-backupchange", tmp)
		#更改保存路径
		tmp = rs.action_wait("button-windows-save.png", 5)
		tmp = rs.action_check("button-windows-save.png")
		tmp = rs.action_typekey(parameter,'a')
		tmp = rs.action_wait2(2)
		tmp = rs.action_typekey('automation_backup','abc')
		tmp = rs.action_wait2(2)
		tmp = rs.action_click("button-windows-save.png")
		#开始备份
		tmp = rs.action_wait("button-backup.png", 5)
		tmp = rs.action_check("button-backup.png")
		tmp = rs.action_click("button-backup.png")
		logger.write("click button-backup.png", tmp)
		#等待备份完成
		tmp = rs.action_wait("popup-backup-completed.png", 300)
		tmp = rs.action_check("popup-backup-completed.png")
		logger.write("check popup-backup-completed", tmp)
		check_point(logger, path, case_id, num, tmp, comments)
		#点击结束按钮
		tmp = rs.action_wait("button-backupfinish.png", 5)
		tmp = rs.action_check("button-backupfinish.png")
		tmp = rs.action_click("button-backupfinish.png")
		logger.write("click button-backupfinish.png", tmp)
	except Exception as e:
		logger.write(str(e), 1)
		check_point(logger, path, case_id, num, 1, comments)

def test():
	tmp = rs.action_wait("icon-backup.png", 2)
	tmp = rs.action_check("icon-backup.png")
	logger.write("check backup icon", tmp)

	tmp = rs.action_click("icon-backup.png")
	logger.write("click backup icon", tmp)

	tmp = rs.action_wait("button-backup.png", 2)
	tmp = rs.action_check("button-backup.png")
	logger.write("check backup button", tmp)

	tmp = rs.action_click("button-backup.png")
	logger.write("click backup button", tmp)

	tmp = rs.action_wait("button-backupfinish.png", 2)
	tmp = rs.action_check("button-backupfinish.png")
	logger.write("check finish button", tmp)

	tmp = rs.action_click("button-backupfinish.png")
	logger.write("click finish button", tmp)


