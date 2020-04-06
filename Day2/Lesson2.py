
import datetime
try:
    try:
        f = open("\\log_file.txt", "a")
    except OSError as e:
        print("something went wrong: " + e.strerror)
    x = datetime.datetime.now()
    f.write(x.strftime("%d/%m/%Y, %H:%M:%S") + " Current Date & Time \n")
except Exception as e:
    print(e)










# try:
#   os.makedirs('/Users/macpro/Desktop/Exercises-2')
#
# except FileExistsError as e:
#     print(e)
#
# try:
#     f = open('/Users/macpro/Desktop/Exercise1.txt',"w+")
#     x = datetime.datetime.now()
#     print(x.strftime("%d %b %y %H:%M:%s"))
# except OSError as e:
#     print("something went wrong" + e.strerror)






