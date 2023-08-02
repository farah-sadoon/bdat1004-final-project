import numpy as np
import pandas as pd
import pyodbc #to connect to Azure SQL Database

# Scraping web to find data in csv format

# Reading csv as pandas dataframe
df = pd.read_csv("/Users/farahsadoon/Desktop/books.csv")
df.rename(columns={"5_Star": "five_star", "4_Star": "four_star", "3_Star": "three_star", "2_Star": "two_star", "1_Star": "one_star"}, inplace = True)

# Connecting to Azure SQL database 
cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:db-server-xyz-books.database.windows.net,1433;Database=db-xyz-final;Uid=user1;Pwd={your_password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()

# Creating Table in database
cursor.execute("DROP TABLE dbo.BookReviews")
cursor.execute("CREATE TABLE [BookReviews]([BookID] [int] NOT NULL, [BookName] nvarchar(50), [Author] nvarchar(50), [AverageStar] float, [Ratings] [int], [Reviews] [int], [5 Stars] [int], [4 Stars] [int], [3 Stars] [int], [2 Stars] [int], [1 Star] [int])")

# Insert Dataframe into SQL Server:
for index, row in df.iterrows():
    book_name = row.Book_Name[:50]
    author = row.Author[:50]
    ave_star = row.Average_star
    ratings = int(row.Ratings.replace(',', ''))
    reviews = int(row.Reviews.replace(',', ''))
    five_star = int(row.five_star.replace(',', ''))
    four_star = int(row.four_star.replace(',', ''))
    three_star = int(row.three_star.replace(',', ''))
    two_star = int(row.two_star.replace(',', ''))
    one_star = int(row.one_star.replace(',', ''))
    cursor.execute("INSERT INTO BookReviews (BookID,BookName,Author,AverageStar,Ratings,Reviews,[5 Stars],[4 Stars],[3 Stars],[2 Stars],[1 Star]) VALUES(?,?,?,?,?,?,?,?,?,?,?)", 
                    index, book_name, author, ave_star, ratings, reviews, five_star, four_star, three_star, two_star, one_star)
    
cnxn.commit()
cursor.close()