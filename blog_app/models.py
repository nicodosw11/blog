class Paginate:
    def __init__(self, PER_PAGE_NUMBER, pages):
        count = 0
        self.list_pages = []
        for page in pages:
            if count % PER_PAGE_NUMBER == 0:
                self.list_pages.append([])
            self.list_pages[int(count / PER_PAGE_NUMBER)].append(page)
            count += 1

    @property
    def paginated(self):
        return self.list_pages

    def get_total_number(self):
        return len(self.list_pages)

    def get_number_pages(self, num):
        return self.list_pages[num - 1]
