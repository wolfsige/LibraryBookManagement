class Book:
    def __init__(self, title="", author="", check_out_status=0):
        self.__Title = title
        self.__Author = author
        self.__Check_Out_Status = check_out_status

    def getTitle(self):
        return self.__Title

    def getAuthor(self):
        return self.__Author

    def getCheck_out_Status(self):
        return self.__Check_Out_Status

    def __str__(self):
        return (f"Title: {self.__Title}\n"
                f"Author: {self.__Author}\n"
                f"Checked Out: {'Yes' if self.__Check_Out_Status == 0 else 'No'}")

    def setCheck_out_Status(self, new_status):
        self.__Check_Out_Status = new_status