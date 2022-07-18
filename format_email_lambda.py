# Python
# using lambda() function combined
# with map() function
email_list = ["  ERICALVESTEIN@GMAIL.COM  "," RoGerio_germAno@terra.com.br  ","adilsOnbasso@gmail.com"]

# here we intend to change all emails
# to upper case and return the same
email_stripped_list = list(map(str.strip, email_list))

final_email_list = list(map(lambda email: str.lower(email), email_stripped_list))

print(final_email_list)