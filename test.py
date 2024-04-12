import datetime

unix_time = 1712937687  # Replace with your Unix time value

# Convert Unix time to datetime
datetime_obj = datetime.datetime.fromtimestamp(unix_time)

# Print the datetime in a specific format
formatted_datetime = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)

print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))