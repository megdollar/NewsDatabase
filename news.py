import psycopg2

DBNAME = "news"


def top_news():

    # connect to database news
    db = psycopg2.connect(database=DBNAME)

    c = db.cursor()

    # get the top 3 articles based on the amount of views
    # select article title, and count each time article was viewed, save count\
    # column info that matches the info in the articles.slug info. \
    # the like contact(%) shortens the data in log.path to match the data
    # in articles.slug.
    # group the results by the title and order them by the views (count) from \
    # largest to smallest, top 3
    query1 = (
        "SELECT articles.title, count(*) AS views "
        "FROM articles LEFT JOIN log ON log.path "
        "LIKE CONCAT('%', articles.slug) "
        "GROUP BY articles.title "
        "ORDER BY views DESC LIMIT 3"
    )

    c.execute(query1)

    # fetch the results
    posts = c.fetchall()

    # print out the label for this sorting
    question1 = print("\nTop 3 Articles Sorted by Views")

    # loop though the posts list(of tuples) and print out the data. Reference
    # site https://pyformat.info
    # post[0] = article.title, post[1] = count
    for post in posts:
        print("\nArticle: {:^10} \nViews: {:^10}" .format(post[0], post[1]))

    # close database
    db.close()


def top_author():

    db = psycopg2.connect(database=DBNAME)

    c = db.cursor()

    # select the authors name, and count for the number of times each article\
    # was accessed, join articles table using the id from authors and join the\
    # log table using the same as the previous query where log.path contents\
    # concat to match the articles.slug. (so counting the number of times the
    # log.path was accessed then join the tables and then able to see #times\
    # each authors' article was viewed)
    # most popular authors of all time
    query2 = (
        "SELECT authors.name, count(log.path) AS views "
        "FROM authors LEFT JOIN articles ON authors.id = articles.author "
        "LEFT JOIN log ON log.path LIKE CONCAT('%', articles.slug) "
        "GROUP BY authors.name "
        "ORDER BY views DESC"
    )

    c.execute(query2)

    authors = c.fetchall()

    question2 = print("\nMost Popular Article Authors")

    for author in authors:
        print("\nAuthor: {:^10} \nViews: {:^10}" .format(author[0], author[1]))


def request_errors():

    db = psycopg2.connect(database=DBNAME)

    c = db.cursor()

    # which days did more than 1% of requests lead to errors time::date as
    # date https://stackoverflow.com/questions/2934192/beginner-sql-question-
    # arithmetic-with-multiple-count-results Initially created two separate
    # queries, this article allowed me to combine the two queries and conduct
    # mathematical equations Add cast as foat to each count select statement
    # to get the floating int, divide errors into total and multiply by 100 to
    # get the % of errors for each day

    query3 = (
        "WITH totalErrors AS "
        "(SELECT time:: date AS date, "
        "count(log.status) AS errors "
        "FROM log where status LIKE '%404 %' "
        "GROUP BY date), "
        "totalViews AS "
        "(SELECT time::date as date, count(status) AS total "
        "FROM log "
        "GROUP by date) "
        "SELECT totalErrors.date, totalErrors.errors, totalViews.total, "
        "CAST(totalErrors.errors AS FLOAT)/totalViews.total*100 "
        "FROM totalErrors, totalViews "
        "WHERE totalErrors.date = totalViews.date"
    )

    c.execute(query3)

    results = c.fetchall()

    question3 = print("\nDay with requests leading to errors greater than 1%:")

    for result in results:
        if result[3] > 1.0:
            print("\nDay: {} \nErrors: {:.2f}" .format(result[0], result[3]))


# runs the function to start the queries
if __name__ == "__main__":
    top_news()
    top_author()
    request_errors()
