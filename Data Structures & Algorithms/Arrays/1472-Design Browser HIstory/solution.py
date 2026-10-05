class BrowserHistory:

    def __init__(self, homepage):
        # Store all visited pages in a list
        self.history = [homepage]

        # 'current' stores the index of the page we are currently on
        self.current = 0

    def visit(self, url):
        # Remove all forward history
        # Example: [a, b, c, d] and current = 1
        # Visiting new page means c and d can no longer be visited using forward()
        self.history = self.history[:self.current + 1]

        # Add the new URL to the history
        self.history.append(url)

        # Move current position to the newly visited page
        self.current += 1

    def back(self, steps):
        # Move backwards by 'steps'
        # max(0, ...) prevents going before the homepage
        self.current = max(0, self.current - steps)

        # Return the page we are currently on
        return self.history[self.current]

    def forward(self, steps):
        # Move forward by 'steps'
        # min(...) prevents going beyond the last visited page
        self.current = min(len(self.history) - 1, self.current + steps)

        # Return the page we are currently on
        return self.history[self.current]
