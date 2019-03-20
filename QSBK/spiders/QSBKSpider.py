# -*- coding: utf-8 -*-
import scrapy
# 导入DuanZi
from QSBK.items import DuanZi


class QsbkspiderSpider(scrapy.Spider):
    name = 'QSBKSpider'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/hot/page/1']  # 替换一下起始页
    i = 1

    def parse(self, response):
        page = self.i
        # 选取每页中存储单个用户信息的tag，以列表形式返回
        users = response.xpath('//div[@class="col1"]/div')  # 注意col1第一个'l'是字母'l',第二个'1'是数字'1'
        # 依次迭代每个tag，进行信息提取
        for user in users:
            item = DuanZi()
            # 因为存在匿名用户,所以需要分类判断
            if user.xpath('./div/a/h2/text()').get():
                # 获取用户名
                user_name = user.xpath('./div/a/h2/text()').get().strip()
                # 获取用户年龄
                user_age = user.xpath('./div/div/text()').get().strip()
                # 获取用户性别
                user_gender = user.xpath('./div/div/@class').get().strip().split()[1][:-4]
                # 获取用户段子
                user_content = ''.join(user.xpath('./a/div[@class="content"]/span/text()').getall())
                # 获取好笑数
                laught_number = user.xpath('./div[@class="stats"]/span/i/text()').get().strip()
                # 获取评论数
                comment_number = user.xpath('./div[@class="stats"]/span/a/i/text()').get().strip()
            else:
                # 获取匿名用户名
                user_name = user.xpath('./div/span/h2/text()').get().strip()
                # 匿名用户age设为None
                user_age = None
                # 匿名用户gender设为None
                user_gender = None
                # 获取用户段子
                user_content = ''.join(user.xpath('./a/div/span/text()').getall())
                # 获取好笑数
                laught_number = user.xpath('./div[@class="stats"]/span/i/text()').get().strip()
                # 获取评论数
                comment_number = user.xpath('./div[@class="stats"]/span/a/i/text()').get().strip()

            item['page'] = page
            item['user_name'] = user_name
            item['user_age'] = user_age
            item['user_gender'] = user_gender
            item['user_content'] = user_content
            item['laught_number'] = laught_number
            item['comment_number'] = comment_number
            yield item

        self.i += 1
        url = 'https://www.qiushibaike.com/hot/page/' + str(self.i)
        yield scrapy.Request(url=url, callback=self.parse)