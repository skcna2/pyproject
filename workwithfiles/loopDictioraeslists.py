#starts with users that need to be verified, and an empty list to hold confirmed users
unconfirmed_users=['alice','brian','candace']
confirmed_users = []

#verify each user until are no more unconfirmed users.
#Move each verified user int the list of confirmed users

while unconfirmed_users:
    current_user= unconfirmed_users.pop()

    print(f"verifiying user: {current_user.title()}")
    confirmed_users.append(current_user)


#display all confirmed users

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())