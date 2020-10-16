# -*- coding: utf-8 -*-
# @Project : myfisher
# @Time    : 2020/10/15 15:39
# @Author  : Biao
# @FileName: __init__.py


from flask import Blueprint

book_bp = Blueprint("blueprint",__name__)

from app.blueprint import book
