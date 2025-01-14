import time
from plyer import notification # pip install plyer

notification_title = input("Enter notification titel:")
notification_details = input("Enter notification details:")
seconds_wait = int(input("Enter the seconds: "))

time.sleep(seconds_wait)

notification.notify(
    notification_title=notification_title,
    message=notification_details,
)



# for MacOS & linux:
# import os
# import time
# from plyer import notification # pip install plyer
#
# notification_title = input("Enter notification titel:")
# notification_details = input("Enter notification details:")
# seconds_wait = int(input("Enter the seconds: "))
#
# time.sleep(seconds_wait)
#
# os.system(f'''
#     osascript -e 'display notification "{notification_details}" with title "{notification_title}"'
#     ''')