import pandas as pd


def get_reader(conn):
    return pd.read_sql("SELECT * FROM reader", conn)


def get_book_reader(conn, min_days, max_year):
    return pd.read_sql(f'''
        select title as Название,
        reader_name as Читатель,
        year_publication as Год_публикации,
        julianday(return_date) - julianday(borrow_date) + 1 as Количество_дней
    from book_reader
        join reader using (reader_id)
        join book using (book_id)
    where return_date IS NOT NULL and Количество_дней > {min_days} and Год_публикации <= {max_year}
    order by Название, Количество_дней desc, Читатель;
    ''', conn)