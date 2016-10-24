# Pedestrian CA simulator in Python
#
# *** Bobby Dodd Stadium Map ****
#
# Copyright 2016 Yuying Liu, Xiao Wang & Sen Yang
# {yliu814, xiaowang, syang356}@gatech.edu

def ped_update(pedes, Map, num_out,time, statistic):
	invert_id_index = {}
	move_id = []
	del move_id[:]
	for pedestrian in pedes:
		#index_ped = pedes.index(pedestrian)
		pedestrian.next_mov(Map)
		pedestrian.update_step()
		info = pedestrian.get_ped_info()
		#invert_id_index[info['id']] = index_ped
		Map[info['xm']][info['ym']].update_sum()
		if(info['xm']!= info['x'] or info['ym'] != info['y']):
			Map[info['xm']][info['ym']].move_in(info['id'],info['mov_pro'])
	

	for row in Map:
		for grid in row:
			grid.decay_dynamic()
			grid.update_group(-1)
			if grid.conflict_id != []:
				ind = grid.handler_conflict()
				move_id.append(ind)
				grid.resetconflict()

	del_list = []
	move_list = []
	for pedestrian in pedes:
	    information = pedestrian.get_ped_info()
	    if information['id'] in move_id:
	        move_list.append(pedestrian)

	for item in move_list:
		#index = invert_id_index[item]
		info = item.get_ped_info()
		f_x = info['x']
		f_y = info['y']
		a_x = info['xm']
		a_y = info['ym']
		p_g = info['group']
		Map[f_x][f_y].empty_state()
		Map[f_x][f_y].update_dynamic()
		Map[f_x][f_y].update_group(p_g)
		Map[a_x][a_y].fill_state()
		item.move()
		if (a_y == 199 or a_x == 0 or a_x == 139 or a_y == 0):
			del_list.append(item)
			Map[a_x][a_y].empty_state()
			Map[a_x][a_y].update_dynamic()

	for item in del_list:
		item.set_stop(time)
		pedes.remove(item)
		num_out += 1
		node = {}
		node['start'] = item.get_start()
		node['stop']  = item.get_stop()
		node['step'] = item.get_step() 
		node['destination'] = item.get_ped_info()['destination']
		node['id'] = item.get_ped_info()['id']
		node['born'] = item.get_ped_info()['born']
		statistic.append(node)
	#print "delete: ",del_list
	return num_out