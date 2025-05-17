class Book:
    def __init__(self, title="Title", page_count=0):
        self.title = title
        self.page_count = page_count  # Utilise le setter ici

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, count):
        if isinstance(count, int):
            self._page_count = count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
