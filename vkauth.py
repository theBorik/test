# -*- coding: utf-8 -*-
import vk
import datetime

session = vk.Session()
vk_api = vk.API(session)

a = [i for i in range(2000,2005)]

profiles = vk_api.users.get(user_ids=(a), fields='online, sex, last_seen, screen_name, status, first_name, last_name')

for i in range(len(profiles)):
	print u'Адрес страницы:', profiles[i]['screen_name']
	print u'Имя:', profiles[i]['first_name']
	print u'Фамилия:', profiles[i]['last_name']
	
	if profiles[i]['online']:
		print u'Онлайн: в сети'
	else:
		print u'Онлайн: не в сети'

	if (profiles[i]['sex'] == 1):
		print u'Пол: женский'
	elif (profiles[i]['sex'] == 2):
		print u'Пол: мужской'
	else:
		print u'Пол: не указан'
	
	print u'Статус:', profiles[i]['status']
	print u'Последний раз заходил/а:', datetime.datetime.fromtimestamp(profiles[i]['last_seen']['time']).strftime('%d-%m-%Y %H:%M')
	print u'-----------------------'
