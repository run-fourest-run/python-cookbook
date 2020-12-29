from datetime import datetime

now = datetime.now()

now_formatted = format(now,'%H:%M:%S')
print(now_formatted)
