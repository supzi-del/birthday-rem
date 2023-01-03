
import time

#plyer module
from plyer import notification

birthdayFile = 'C:\\Users\\reminder\\birthdays.data’

def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    flag = 0
    for line in fileName:
        if today in line:
            line = line.split(' ')
            flag =1
         
            notification.notify(
               title ="Birthday Reminder",
               message= line[1] + ' ' + line[2],
               timeout = 10
            )

    if flag == 0:
            notification.notify(
               title ="Birthday Reminder",
               message="No Birthdays Today!",
               timeout = 10
            )

  
if __name__ == '__main__':
    checkTodaysBirthdays()
