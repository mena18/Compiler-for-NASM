class obj:

    def pr(self):
        print("hello")


class hello:
    def __init__(self):
        self.a = obj()
        self.a.val=12;
    def get_a(self):
        return self.a
