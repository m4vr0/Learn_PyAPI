class TestPhrase:
    def setup_class(self):
        self.phrase = input('Enter a phrase (less then 15 symbols): ')

    def test_phrase(self):
        assert len(self.phrase) < 15, f"Length of the Phrase is bigger than 15 symbols (length = {len(self.phrase)})"
