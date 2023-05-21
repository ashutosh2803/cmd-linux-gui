# DateTime functionality 

import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time
formatted_date = current_datetime.strftime("%B %d, %Y")
formatted_time = current_datetime.strftime("%I:%M %p")

# Create a beautiful display string
display_string = f"Current Date: {formatted_date}\nCurrent Time: {formatted_time}"

# Print the display string
print(display_string)
