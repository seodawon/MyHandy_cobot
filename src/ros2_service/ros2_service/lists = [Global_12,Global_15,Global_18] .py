lists = [Global_12,Global_15,Global_18] # small
listm = [Global_11,Global_14,Global_17] # medium
listb = [Global_10,Global_13,Global_16] # big

list_first = [Global_1,Global_2,Global_3,Global_4,Global_5,Global_6,Global_7,Global_8,Global_9]

set_digital_output(1,ON)
set_digital_output(2,ON)
sock= server_socket_open(21)
Global_countb=0
Global_counts=0
Global_countm=0
task_compliance_ctrl()
set_stiffnessx([750.0, 750.0, 750.0, 0.0, 0.0, 0.0],time=0.0)
rx_data= server_socket_read(sock)
rx_data=rx_data[1]
rx_data = rx_data.decode('utf-8').strip()
a =rx_data.split(',')
#tp_popup("{} ".format(a[1]),DR_PM_MESSAGE)
for idx,i in enumerate(a):
	movel(trans(list_first[idx], [0,0,100,0,0,0],ref = DR_BASE))
	movel(list_first[idx])
	# 그리퍼 on  # wait(1)
	set_digital_output(2,OFF)
	wait(1.0)
	movel(trans(list_first[idx], [0,0,100,0,0,0],ref = DR_BASE))
	if  i =='0':
		movel(trans(lists[Global_counts], [0,0,100,0,0,0],ref = DR_BASE))
		movel(lists[Global_counts])
		set_digital_output(2,ON)
		wait(1.0)
		movel(trans(lists[Global_counts], [0,0,100,0,0,0],ref = DR_BASE))
		Global_counts+=1
	elif i=='1':
		movel(trans(listm[Global_countm], [0,0,100,0,0,0],ref = DR_BASE))
		movel(listm[Global_countm])
		set_digital_output(2,ON)
		wait(1.0)
		movel(trans(listm[Global_countm], [0,0,100,0,0,0],ref = DR_BASE))
		Global_countm+=1
	elif i=='2':
		movel(trans(listb[Global_countb], [0,0,,0,0,0],ref = DR_BASE))
		movel(listb[Global_countb])
		set_digital_output(2,ON)
		wait(1.0)
		movel(trans(listb[Global_countb], [0,0,100,0,0,0],ref = DR_BASE))
		Global_countb+=1
release_compliance_ctrl()
move_home(DR_HOME_TARGET_USER)