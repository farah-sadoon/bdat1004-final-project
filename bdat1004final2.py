import pyodbc
import pandas as pd

cnxn = cnxn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};Server=tcp:db-server-xyz-books.database.windows.net,1433;Database=db-xyz-final;Uid=user1;Pwd=x7P%zbf&Gg;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
cursor = cnxn.cursor()

query = "SELECT * FROM BookReviews;"
df = pd.read_sql(query, cnxn)
print(df.head())
# numpy manipulation

# 1 Find the books with the highest average star rating.

max_rating_book = df[df["AverageStar"] == df["AverageStar"].max()]
print(max_rating_book)

# 2 Calculate the average number of ratings given to all books.

average_num_ratings = df[["five_star", "four_star", "three_star", "two_star", "one_star"]].mean().mean
print("Average Number of Ratings:", average_num_ratings)

# 3 Calculate the average star rating for all books.
average_star = df[["AverageStar"]].mean()
print("Average Star Ratings:", average_star)

# 4 Calculate the percentage of 5-star ratings for each book:

df["Percentage_5_Star"] = (df["five_star"] / df["Ratings"]) * 100
print(df[["BookName", "Percentage_5_Star"]])

# 5 Filter books with an average rating greater than 4.0:
high_rated_books = df[df["AverageStar"] > 4.0]
print(high_rated_books)

# 6 Sort the DataFrame by the number of reviews in descending order:
sorted_by_reviews = df.sort_values(by="Reviews", ascending=False)
print(sorted_by_reviews)