# -*- coding: utf-8 -*-
# @Project : myfisher
# @Time    : 2020/10/15 14:45
# @Author  : Biao
# @FileName: book.py
from flask import jsonify,request

from app.forms.book import SearchForm
from . import  book_bp
from helper import is_isbn_or_key
from yushu_book import YuShuBook

@book_bp.route("/book/search")
def search():
	# q = request.args['q']
	# page = request.args['page']

	form = SearchForm(request.args)
	if form.validate():
		#strip去掉空格
		q = form.q.data.strip()
		page = form.page.data
		isbn_or_key = is_isbn_or_key(q)

		if isbn_or_key == "isbn":
			result = YuShuBook.search_by_isbn(q)
		else:
			result = YuShuBook.search_by_keyword(q,page)
		return jsonify(result)
	else:
		return jsonify(form.errors)

