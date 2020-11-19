import requests
from pyquery import PyQuery as pq

def parse_search_page(url):
    doc = pq(requests.get(url).text)
    trs = doc('tbody tr').items()
    index_contents = []
    gang_wei_detail = []
    for tr in trs:
        line_info = tr.find('td').text().split(" ")
        index_contents.append(line_info)
        td = tr.find("td")
        for i in td.items():
            if i.text() == "查看":
                detail_url = (i.find('a').attr('href'))
                tables = parse_detail("http://ah.huatu.com/zw/jdwz/%s" % (detail_url.split("../")[1]))
                gang_wei_detail.append(tables)
    return gang_wei_detail, index_contents

def parse_detail(url):
    content = requests.get(url).text.encode('ISO-8859-1').decode('gbk')
    tables = []
    doc = pq(content)
    trs = doc('tbody tr').items()
    for tr in trs:
        line_info = tr.find('td').text().split(" ")[1]
        tables.append(line_info)
    tables.pop(-1)
    return tables






if __name__ == '__main__':
    f1 = open("./岗位详情2020-2", 'w')
    f2 = open("./搜索首页列表2020-2", 'w')
    f2.write("岗位代码	地区	招聘单位	招聘职位	专业	专业科目	招聘人数	合格人数	职位详情	对比\n")
    f1.write("岗位代码   地区   部委   用人单位序号   用人单位名称   岗位类别   岗位名称   从事工作   招考数量   报名人数   来源类别   学历   学位   所学专业   考试专业科目   高校毕业生专业技术资格   社会人才专业技术资格   高校毕业生职业资格   社会人才职业资格   其他条件   工作地点\n")
    counter = 0
# 2018年
#     for page in range(1, 356):
#         gang_wei_detail, index_contents = parse_search_page('http://ah.huatu.com/zw/jdwz/search/?yr=2018&dq=&ly=&zw=&xb=&xl=&zy=&page=%s' % page)
#         print("-----------2018年第%s页数据--------" % page)
#         for i in gang_wei_detail:
#             f1.write("---".join(i))
#             f1.write("\n")
#         for j in index_contents:
#             f2.write("--".join(j))
#             f2.write("\n")
#         counter = counter + 1

    # # 2019年
    # for page in range(1, 761):
    #     gang_wei_detail, index_contents = parse_search_page('http://ah.huatu.com/zw/jdwz/search/?yr=2019&dq=&ly=&zw=&xb=&xl=&zy=&page=%s' % page)
    #     print("-----------2019年第%s页数据--------" % page)
    #     for i in gang_wei_detail:
    #         f1.write("---".join(i))
    #         f1.write("\n")
    #     for j in index_contents:
    #         f2.write("--".join(j))
    #         f2.write("\n")
    #     counter = counter + 1
    #
    # 2020年
    for page in range(584, 1011):
        gang_wei_detail, index_contents = parse_search_page('http://ah.huatu.com/zw/jdwz/search/?yr=2020&dq=&ly=&zw=&xb=&xl=&zy=&page=%s' % page)
        print("-----------2020年第%s页数据--------" % page)
        for i in gang_wei_detail:
            f1.write("---".join(i))
            f1.write("\n")
        for j in index_contents:
            f2.write("--".join(j))
            f2.write("\n")
        counter = counter + 1
