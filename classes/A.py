class BlogPost:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.likes = 0

    def likes(self):
        self.likes +=1

    def display(self):
        print(f" '{self.title}' by {self.author}") 
        print(f"Content: {self.content}")
        print(f"Likes: {self.likes}")      

myBlog = BlogPost("Blog", "me", "coding")
print(myBlog.display())








