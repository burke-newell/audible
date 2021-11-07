import audible
import json

auth = audible.Authenticator.from_file('../auth/burke_auth.py')

with audible.Client(auth=auth) as client:
    library = client.get(
        "1.0/library",
        num_results=1,
        response_groups="product_desc, product_attrs",
        sort_by="-PurchaseDate"
    )
    for book in library["items"]:
        with open('library.json', 'a') as convert_file:
            convert_file.write(json.dumps(book))
