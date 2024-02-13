import os
hostname = input("please input ip: ")
response = os.system("ping -t " + hostname)