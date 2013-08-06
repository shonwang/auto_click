import sys
import shutil
from SimpleXMLRPCServer import SimpleXMLRPCServer as Server

try:
    addImagePath(sys.argv[1])
except IndexError:
    print "=====This script must run with snapshot path.====="
    exit(1)

def action_click(img):
    try:
        screen = Screen()
        region = Region.create(screen.getBounds())
        img_region = region.getRegionFromPSRM(img)
        img_region.highlight(1)
        region.click(img_region)
        return 0
    except FindFailed:
        return "[%s] not Found" % img

def action_click_offset(img, x, y):
    try:
        screen = Screen()
        region = Region.create(screen.getBounds())
        img_pattern = Pattern(img).targetOffset(x, y)
        img_region = region.getRegionFromPSRM(img_pattern)
        img_region.highlight(1)
        region.click(img_region)
        return 0
    except FindFailed:
        return "[%s] not Found" % img    

def action_check(img, seconds=3):
    if exists(img, seconds):
        screen = Screen()
        region = Region.create(screen.getBounds())
        img_region = region.getRegionFromPSRM(img)
        img_region.highlight(1)
        return 0
    else:
        return 1

def action_wait(img, seconds=30):
    try:
        wait(img,seconds)
        return 0
    except FindFailed:
        return "Wait fail with [%s]" % img

def action_wait2(seconds=2):
    try:
        wait(seconds)
        return 0
    except FindFailed:
        return "Wait fail"

def action_waitVanish(img,seconds=60):
    try:
        waitVanish(img, seconds)
        return 0
    except FindFailed:
        return "waitVanish fail with [%s]" % img

def action_type(msg, img="x"):
    if img == "x":
        type(msg)
    else:
        type(img,msg)
    return 0

def action_typekey(key1,key2='a'):
    if key2=='abc':
        type(key1)
    elif key2 == 'down':
        type(Key.DOWN)
    elif key2 == 'enter':
        type(key1+Key.ENTER)
    return 0

def action_close_by_key():
    type(Key.F4, KeyModifier.ALT)
    return 0

def action_select_all_key():
    type('a', KeyModifier.CTRL)
    return 0

def action_findall(img):
    try:
        for i in findAll(Pattern(img).similar(0.90)):
            click(i)
            if i=='continue.png':
                waitVanish(img,30)
        return 0
    except FindFailed:
        return "[%s] not Found" % img

def action_clickright(img="cancel.png"):
    wait(1)
    s = find(img).right(100)
    click(s)
    return 0

def action_findbelow(img='search3.png'):
    wait(1)
    p = find(img).below(65)
    wait(1)
    click(p)
    return 0

def action_capture(img_name):
    s = Screen()
    r = getBounds()
    default_filename = s.capture(r)
    shutil.copyfile(default_filename, img_name)
    return 0

def action_hover(img):
    try:
        screen = Screen()
        region = Region.create(screen.getBounds())
        img_region = region.getRegionFromPSRM(img)
        img_region.highlight(1)
        region.hover(img_region)
        return 0
    except FindFailed:
        return "[%s] not Found" % img

def action_click_by_path(img_string):
    try:
        screen = Screen()
        region = Region.create(screen.getBounds())
        img_list = img_string.split('/')
        img_region = action_walk_in_region(region, img_list, 0)
        region.click(img_region)
    except FindFailed:
        return "[%s] not Found" % img_string

def action_walk_in_region(region, img_list, id):
    try:
        sub_region = region.getRegionFromPSRM(img_list[id])
        sub_region.highlight(1)
        if id + 1 <= len(img_list) -1:
            sub_region = action_walk_in_region(sub_region, img_list, id + 1)
        return sub_region
    except FindFailed:
        return "[%s] not Found" % img_list[id]

def action_findall_number(img):
    try:
        pic_list = findAll(img)
        temp = []
        for pic in pic_list:
            temp.append(pic)
            region.getRegionFromPSRM(pic).highlight(1)
            hover(pic)
        return len(temp)
    except FindFailed:
        return "[%s] not Found" % img

Settings.MoveMouseDelay=0
srv = Server(("127.0.0.1", 1338))
if not srv:exit(1)
srv.register_introspection_functions()
srv.register_function(action_click)
srv.register_function(action_check)
srv.register_function(action_wait)
srv.register_function(action_type)
srv.register_function(action_waitVanish)
srv.register_function(action_findall)
srv.register_function(action_wait2)
srv.register_function(action_clickright)
srv.register_function(action_findbelow)
srv.register_function(action_typekey)
srv.register_function(action_capture)
srv.register_function(action_hover)
srv.register_function(action_click_offset)
srv.register_function(action_close_by_key)
srv.register_function(action_select_all_key)
srv.register_function(action_click_by_path)
srv.register_function(action_walk_in_region)
srv.register_function(action_findall_number)

srv.serve_forever()