import requests as r
import os
from tkinter.commondialog import Dialog
import sys
import json
import inspect

class Message(Dialog):
    "A message box"
    command  = "tk_messageBox"

def _show():
    if _icon and "icon" not in options:    options["icon"] = _icon
    if _type and "type" not in options:    options["type"] = _type
    if title:   options["title"] = title
    if message: options["message"] = message
    res = Message(**options).show()
    if isinstance(res, bool):
        if res:
            return YES
        return No
    return str(res)

def china_total(make_dirs):
	inspect.InSpect(make_dirs)	
	try:
		world = r.get("https://view.inews.qq.com/g2/getOnsInfo?_t=0.7205175088889795&name=disease_h5&callback=__jpcb1")
	except:
		_show(title="疫情数据爬取", message="网络似乎开小差了,请稍后重试！")
		exit()
	else:
		world_text = world.text

	world_text = world_text.replace("__jpcb1","")
	world_text = world_text.replace("(","")
	world_text = world_text.replace(")","")

	world_text = json.loads(world_text)
	list_1 = list(world_text.keys())
	list_2 = list(world_text.values())

	with open(r"C://ZSwork//ZSncov//cache//china.txt","w+")as f:
		f.write(str(world_text))
		f.close()

	world_text_dict = world_text['data']
	world_text_dict = json.loads(world_text_dict)
	world_text_dict = world_text_dict['chinaTotal']
	confirm = str(world_text_dict['confirm'])
	heal = str(world_text_dict['heal'])
	dead = str(world_text_dict['dead'])
	nowConfirm = str(world_text_dict['nowConfirm'])
	nowSevere = str(world_text_dict['nowSevere'])
	importedcase = str(world_text_dict['importedCase'])
	return confirm,heal,dead,nowConfirm,nowSevere,importedcase

def china_add():
	with open(r"C://ZSwork//ZSncov//cache//china.txt","r")as f:
		world = f.readline()
		world = eval(world)
	lastupdatetime = world['data']
	lastupdatetime = json.loads(lastupdatetime)
	china_add = lastupdatetime
	#print(type(lastupdatetime))
	#print(lastupdatetime)

	with open(r"C://ZSwork//ZSncov//cache//china.txt","w+")as f:
		world2 = f.write(str(china_add))
		world2 = f.close()

	lastupdatetime = str(lastupdatetime['lastUpdateTime'])
	#print(lastupdatetime)
	china_add = china_add['chinaAdd']
	#print(china_add)
	add_confirm = str(china_add['confirm'])
	add_heal = str(china_add['heal'])
	add_dead = str(china_add['dead'])
	add_nowConfirm = str(china_add['nowConfirm'])
	add_nowSevere = str(china_add['nowSevere'])
	add_importedcase = str(china_add['importedCase'])
	return add_confirm,add_heal,add_dead,add_nowConfirm,add_nowSevere,add_importedcase


confirm,heal,dead,nowConfirm,nowSevere,importedcase = china_total("C://ZSwork//ZSncov//cache//")
add_confirm,add_heal,add_dead,add_nowConfirm,add_nowSevere,add_importedcase = china_add()
china_total = open("C://ZSwork//ZSncov//cache//china_total.txt","w+")
china_total.write(confirm+"\n"+heal+"\n"+dead+"\n"+nowConfirm+"\n"+nowSevere+"\n"+importedcase)
china_total.close()
china_add = open("C://ZSwork//ZSncov//cache//china_add.txt","w+")
china_add.write(add_confirm+"\n"+add_heal+"\n"+add_dead+"\n"+add_nowConfirm+"\n"+add_nowSevere+"\n"+add_importedcase)
china_add.close()
