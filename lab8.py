class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.uid} - {self.title} ({self.year})"



    def __eq__(self, other):
        return self.uid == other.uid


    def is_recent(self, n):
        return self.year >= 2025 - n


class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book -> {super().__str__()}, Author: {self.author}, Pages: {self.pages}"

class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi
    def __str__(self):
        return f"Article -> {super().__str__()}, Journal: {self.journal}, DOI: {self.doi}"

class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = duration

    def __str__(self):
        return f"Podcast -> {super().__str__()}, Host: {self.host}, Duration: {self.duration} mins"

def save_to_file(items, filename):
    f = open(filename, "w")
    for item in items:
        if(isinstance(item, Book)):
            f.write("Book: "+str(item) + "\n")
        elif(isinstance(item, Article)):
            f.write("Article: "+str(item) + "\n")
        elif(isinstance(item, Podcast)):
            f.write("Podcast: "+str(item) + "\n")
    f.close()
    print("Items saved to file: ", filename)

def load_from_file(filename):
    items = []
    f = open(filename, "r")
    line = f.readlines()
    for line in f:
        parts = line.strip().split(",") # Strip javadaki trim()
        t = parts[0]
        if t == "Book":
            items.append(Book(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
        elif t == "Article":
            items.append(Article(parts[1], parts[2], int(parts[3]), parts[4], parts[5]))
        elif t == "Podcast":
            items.append(Podcast(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
    f.close()
    print("Items loaded from file: ", filename)
    return items


items = [
    Book("B1", "Python Basics", 2021, "Ali Yılmaz", 300),
    Book("B2", "Data Science", 2019, "Ayşe Kaya", 250),
    Article("A1", "AI Future", 2022, "TechToday", "10.1234/abc"),
    Article("A2", "ML Trends", 2020, "CompSci", "10.5678/def"),
    Podcast("P1", "CodeTalk", 2023, "Mehmet Can", 40),
    Podcast("P2", "DeepCast", 2018, "Elif Demir", 60)
]

save_to_file(items, "archive.txt")
loaded=load_from_file("archive.txt")
print("Tüm içerikler:")
for item in loaded:
    print(item)

print("\nSon 5 yıl:")
for item in loaded:
    if item.is_recent(5):
        print(item)

print("\nDOI 10.1234 ile başlayan makaleler:")
for item in loaded:
    if isinstance(item, Article) and item.doi.startswith("10.1234"):
        print(item)
