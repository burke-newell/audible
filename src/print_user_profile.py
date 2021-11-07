import audible

auth = audible.Authenticator.from_file('../auth/burke_auth.py')

print(audible.Client(auth).get_user_profile())
