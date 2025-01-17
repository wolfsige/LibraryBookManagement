class Book:
    def __init__(self):
        self.Title = ""
        self.Author = ""
        self.Check_Out_Status = 0
        self.__str__ = f"This book has a string"