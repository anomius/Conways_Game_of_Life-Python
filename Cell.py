class Cell:
    def __init__(self):
        self.state=0

    def set_ded(self):
        self.state=0
    
    def set_liv(self):
        self.state=1
    
    def is_alive(self):
        return self.state==1

    def __str__(self):
        if self.state==1:
            return "O"
        else:
            return " "

