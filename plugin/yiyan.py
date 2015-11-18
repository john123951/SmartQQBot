# -*- coding:utf-8 -*-
import json
import logging
from HttpClient import HttpClient

__author__ = 'sweet'


class yiyan(object):
    """
    一言
    简单来说，一言（ヒトコト）指的是就是一句话，可以是动漫中的台词，可以是小说中的语句，也可以是网络上的各种小段子。
    或是感动，或是开心，又或是单纯的回忆，来到这里，留下你所喜欢的那一句句话，与大家分享，这就是一言存在的目的。
    """

    def __init__(self):
        self.httputil = HttpClient()
        pass

    def get_rand(self):
        """
        {
        hitokoto: "只要微笑就可以了。",
        cat: "a",
        author: "卍谷",
        source: "EVA",
        like: 27,
        date: "2011.10.16 23:57:36",
        catname: "Anime - 动画",
        id: 1318780656000
        }
        :return:
        """
        try:
            url = 'http://api.hitokoto.us/rand'
            response = self.httputil.Get(url)
            result = json.loads(response)
            return result
        except Exception as ex:
            logging.exception(ex)
            return {}
