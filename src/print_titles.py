import audible

auth = audible.Authenticator.from_file('../auth/burke_auth.py')
client = audible.Client(auth)

library = client.get("library", num_results=500)
titles = [book["title"] for book in library["items"]]

print(titles)
