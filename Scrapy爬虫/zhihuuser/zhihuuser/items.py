# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class ZhihuuserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    answer_count = Field()
    articles_count = Field()
    avatar_url = Field()
    columns_count = Field()
    description = Field()
    favorited_count = Field()
    follower_count = Field()
    following_columns_count = Field()
    following_count = Field()
    following_favlists_count = Field()
    following_question_count = Field()
    following_topic_count = Field()
    gender = Field()
    headline = Field()
    hosted_live_count = Field()
    id = Field()
    logs_count = Field()
    marked_answers_count = Field()
    participated_live_count = Field()
    question_count = Field()
    thanked_count = Field()
    url_token = Field()
    voteup_count = Field()




    business = Field()
    educations = Field()
    employments = Field()
    locations = Field()



