import datetime

now = datetime.datetime.now()

formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("-"*30)
print("\tDate : time\n")
print("   ",formatted_date_time)
print("-"*30)
