import inspect                                     #导入新建文件夹模块

def get_message(dirs,make_dirs):
	inspect.InSpect(make_dirs)						#新建文件夹
	message = open(dirs,"r")
	world_message = message.readline()				#读取已储存信息
	world_message = eval(world_message)				#转换信息为字典
	#print(type(world_message))
	areatree = world_message['areaTree']
	#print(areatree)
	for i in areatree:								#循环遍历列表
		#print(type(i))
		#print(i)
		#print(i.keys())
		name = i.get("name")						#以下get()方法获取列表的数据
		today = i.get("today")
		total = i.get("total")
		children = i.get("children")
		#print(name)
		#print(today)
		#print(total)
		#print(type(children))
		for i in children:							#循环遍历列表children
			name = i.get("name")
			today = i.get("today")
			total = i.get("total")
			confirm_1 = today.get("confirm")
			children = i.get("children")
			tip = today.get("tip")
			nowConfirm = total.get("nowConfirm")
			confirm = total.get("confirm")
			dead = total.get("dead")
			deadRate = total.get("deadRate")
			heal = total.get("heal")
			healrate = total.get("healRate")

			if tip == "":							#处理数据
				tip = "无"
			else:
				pass

			city = open("C://ZSwork//ZSncov//message//cache//china//"+name+".txt","w+")					#打开文件，写入数据
			city.write("城市名称为："+name+"\n"+"今日新增数量为："+str(confirm_1)+";现有确诊人数："+str(confirm)+";城市总确诊数量为："+str(confirm)+";累计死亡数："+str(dead)+
				";城市致死率为："+str(deadRate)+";城市治愈总人数为："+str(heal)+";城市治愈率为："+str(healrate)+"\n"+
				"城市备注："+tip)
			city.close()							#关闭文件

get_message("C://ZSwork//ZSncov//cache//china.txt","C://ZSwork//ZSncov//message//cache//china//")			#文件执行总命令