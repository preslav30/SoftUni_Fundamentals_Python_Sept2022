force_and_users = {'Light': ['Peter'], 'Dark': ['Kim']}
force_user = "Kim"
for side, user in force_and_users.items():
    if force_user in user:
        user.remove(force_user)
print(force_and_users)