from arsein import Messenger
from arsein.Zedcontent import Antiadvertisement
au = ("")
tabligh = Antiadvertisement(au)

bot = Messenger(au)

guid_gap = "g0CJz3Z085657540e6589d50ac85e0f9"

list_id = []

de = 0

while 1:
	try:
		message = bot.getChatGroup(guid_gap)
		for msg in message:
			if not msg.get("message_id") in list_id:
				list_id.append(msg.get("message_id"))
				tabligh.Anti("link",guid_gap,msg)
				tabligh.Anti("forward",guid_gap,msg)
				de += 1
				print(de)
	except:continue