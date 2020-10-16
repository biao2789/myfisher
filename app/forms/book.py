# -*- coding: utf-8 -*-
# @Project : myfisher
# @Time    : 2020/10/15 16:36
# @Author  : Biao
# @FileName: book.py

from wtforms import Form,StringField,IntegerField
from wtforms.validators import  Length,NumberRange,DataRequired
class SearchForm(Form):
	q = StringField(DataRequired(),validators=[Length(min=1,max=30)])
	page = IntegerField(validators=[NumberRange(min=1,max=99)],default=1)
