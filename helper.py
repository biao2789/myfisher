# -*- coding: utf-8 -*-
# @Project : myfisher
# @Time    : 2020/10/15 11:35
# @Author  : Biao
# @FileName: helper.py

def is_isbn_or_key(word):

	isbn_or_key = "key"
	if len(word)==13 and word.isdigit():
		isbn_or_key = "isbn"
	short_q = word.replace("-","")
	if "-" in word and len(short_q) ==10 and short_q.isdigit():
		isbn_or_key = "isbn"
	return isbn_or_key
