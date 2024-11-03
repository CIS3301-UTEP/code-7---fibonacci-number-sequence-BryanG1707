import re

# file_object = open("social_media_users.csv")

# text_from_file = file_object.read()

# emails = re.findall('[a-z]+@[a-z]{4,}\.com', text_from_file)
# print(emails)
# print(len(emails))
# # print(text_from_file)

# are_emails = re.search('[a-z]+@gmail\.com', text_from_file)
# print(are_emails)


def get_password_level(user_password):
    level_0 = re.findall(r"^\S{8,}$", user_password)
    level_1 = re.findall(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", user_password)
    level_2 = re.findall(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", user_password)
    level_3 = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",user_password)

    if len(level_3) > 0:
         return "This is a level 3 password"
    elif len(level_2) > 0:
         return "This is a level 2 password"
    elif len(level_1) > 0:
         return "This is a level 1 password"
    elif len(level_0) > 0:
         return "This is a level 0 password"
    else: 
         return "The password entered does not meet the requirements"

user_password = input("Please enter a password: ")
print(get_password_level(user_password))
