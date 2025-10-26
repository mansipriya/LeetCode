# problem here - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)  # current page

    def visit(self, url: str) -> None:
        # Create new node
        new_page = Node(url)

        # Remove all forward history
        self.curr.next = None

        # Link current → new page
        new_page.prev = self.curr

        # Move current pointer to new page
        self.curr.next = new_page
        self.curr = new_page

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.url
