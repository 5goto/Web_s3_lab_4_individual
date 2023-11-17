from flask import render_template
import sqlite3
from model.reader_book_model import *


def get_simple_request(min_days=14, max_year=2020):
    conn = sqlite3.connect("/home/goto/workspace/web/lab4_individual/library.sqlite")  # harcode

    try:
        df_book_reader = get_book_reader(conn, min_days, max_year)
        conn.close()
        return render_template("index_tmp.html",
                               book_reader=[df_book_reader],
                               table_name=["Сводка о сданных книгах"],
                               len=len,
                               zip=zip)
    except:
        return render_template("error.html",
                               day=min_days,
                               year=max_year
                            )
