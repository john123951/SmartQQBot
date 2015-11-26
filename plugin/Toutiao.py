# -*- coding:utf-8 -*-
import time

__author__ = 'sweet'


class Toutiao(object):
    """
    新闻头条
    """

    def __init__(self):
        self.category = {
            '__all__': u'推荐',
            'news_hot': u'热点',
            'news_society': u'社会',
            'news_entertainment': u'娱乐',
            'news_tech': u'科技',
            'news_car': u'汽车',
            'news_sports': u'体育',
            'news_finance': u'财经',
            'news_military': u'军事',
            'news_world': u'国际',
            'news_game': u'游戏',
            'news_travel': u'旅游',
            'news_food': u'美食',
            'news_fashion': u'时尚',
            'news_history': u'历史',
            'news_discovery': u'探索',
            'news_baby': u'育儿',
            'news_regimen': u'养生',
            'news_story': u'故事',
            'news_essay': u'美文'
        }

    def get_category(self):
        return self.category

    def recent(self, category='__all__'):
        url = 'http://toutiao.com/api/article/recent/?source=2&count=20&category={0}&max_behot_time={1}&utm_source=toutiao&offset=0'.format(category, time.time())

    def search(self, keyword):
        url = 'http://toutiao.com/search_content/?offset=0&format=json&keyword={0}&autoload=true&count=20'.format(keyword)
