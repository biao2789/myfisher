# -*- coding: utf-8 -*-
# @Project : myfisher
# @Time    : 2020/10/15 14:00
# @Author  : Biao
# @FileName: yushu_book.py

from httper import  HTTP
from flask import current_app
# 不能  from fisher import app
class YuShuBook:
	isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
	keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

	def search_by_isbn(isbn):
		url = YuShuBook.isbn_url.format(isbn)
		result = HTTP.get(url)
		return result
	def search_by_keyword(keyword,page=1):
		url = YuShuBook.keyword_url.format(keyword,current_app.config['PER_PAGE'],YuShuBook.calculate_start(page))
		result = HTTP.get(url)
		return result
	@staticmethod
	def calculate_start(page):
		return (page-1) * current_app.config['PER_PAGE']