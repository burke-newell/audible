import audible

auth = audible.Authenticator.from_file('../auth/burke_auth.py')
client = audible.Client(auth)

library = client.get("library", num_results=250)
titles = [book["title"] for book in library["items"]]


class TestTitles:
    def test_titles_count(self):
        # My library contains 288 books
        assert len(titles) == 250

    def test_titles_contains_favorite(self):
        assert titles.__contains__('Rhythm of War')

    def test_titles_do_not_contain_star_strike(self):
        # Star Strike's purchase date is the oldest in my library and returns last
        assert not titles.__contains__('Star Strike')
