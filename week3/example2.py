from datetime import datetime
now_method = datetime.now()
currenttime = now_method.strftime("%H,%M,%S")
print("current time = ",currenttime)