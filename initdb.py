from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMDZfMjMy%2FMDAxNjQ0MTIxMTM1NjY1.a8PbgijWJ_9hPEgvI5P2m3ekYG4qFXpFN994JMdtJ6Ug.UiBe5NVzS7vexYQjr_Gkcsgkp_ID4D764H3ZaMwZR78g.JPEG.jungtaesung6%2FIMG_9973.JPG&type=a340',
       'name':'초밥',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20151209_131%2Fchoi9036903_1449611008735Bnwui_JPEG%2FDSC08888.JPG&type=a340',
       'name':'쭈꾸미볶음',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzA1MjJfMjAx%2FMDAxNDk1NDU1MjMwNjI0.E6fCrGEDN1dAng_XkRM6F30pdw4uWIt6qYlVqvlIKKIg.szCBtgyKseX7WpuqfcMMfUbDH3YgNDffYY1nFcHESGog.JPEG.gookbapbug%2FIMG_9757.JPG&type=a340',
       'name':'돼지국밥',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMjVfODIg%2FMDAxNjE0MTg2OTU4Mzkx.OJPuQSvRJdk4IyQgmXTJYhbKmSjc3gQZmYpxg4KAErgg.BFiIrRNdR0ik2-FW4VLLDcorpHWjtWFCoAMw2dctb98g.JPEG.rose7779%2FIMG_6861.JPG&type=a340',
       'name':'육회',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTJfMjUw%2FMDAxNjQ0NjcwMjgzMjU2._U1IHmy33TRpQAyrg2S0ychA5QPf9ZOiR1Tw1sTVbsYg.Gt1VE0Mw3Lp6DXwEIbwkT3iFiUuNCfI9tydkkCWsOLcg.JPEG.kutty1945%2F20220212%25A3%25DF213311.jpg&type=a340',
       'name':'족발',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140727_5%2Fjuhanarim_1406465713941JKbD5_JPEG%2F%25BB%25E7%25C1%25F8_872.jpg&type=a340',
       'name':'삼계탕',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20110626_67%2Frail4128_1309058512028hcv6m_JPEG%2FP6245686.JPG&type=a340',
       'name':'부침개',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMDAxMzFfNDIg%2FMDAxNTgwNDgxMjE0ODAw.q1IzUrGNjPMj9HWkLwpSOdjSmxYoZc4aG_A5ewx92HYg.3OY7ZmgQnnugH3vXuVWtdBxYzBwYBYLO9wPC5o9eriIg.JPEG.lallanamu%2F1580465870174.jpg&type=a340',
       'name':'라멘',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTA1MTlfMTc1%2FMDAxNTU4MjMxNTE0ODI2.VoDDBEeEYxJ_IuGAJTycnarFKjJgPIjrf8K4t5NGPs8g.pMROJQdvNTTZqegRSqK7kg6jb_6OvG_-ABNDcVOV6ogg.JPEG.gamseongtrip5%2FIMG_3415.JPG&type=a340',
       'name':'쌀국수',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTExMjdfOTQg%2FMDAxNTc0ODU2OTc3Njk1.13cMiNAHUVGM9Yf918fP8gLQukYmngS5R28I2c4ZLFQg.__uVRdX-zSf4cuQrhSYkjNnxQGDL1HHa3XWoq7zAvI0g.JPEG.mnws90%2FIMG_7057.jpg&type=a340',
       'name':'규카츠',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMjZfMjMz%2FMDAxNjQ1ODc3OTg4MDgx.raH_ehNms_kuA6fX6SwWmtoUShyisEpLLnxZbPhl8FEg.GL0eE3OPO23Fdtpi4IzeZMNsdQRO-p0TS1ozdwSUODAg.JPEG.jyoh97%2FIMG_6459.jpg&type=a340',
       'name':'마라탕',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMTdfMTQ4%2FMDAxNjEzNTcwMzEyMjc2.-9-V3FAgv37pJYVHkjF4htCaJgqnhoZ919lK6Qp6RZQg.hCrB2H_YLevmR_S4W2o5gWmhb6YFIlSJyq3uwp13NAEg.JPEG.cis7903%2FIMG_5936.JPG&type=a340',
       'name':'삼겹살',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAzMjJfMjA4%2FMDAxNjQ3OTU5NDQ4MTM3.qNT1ehfmE1lf1aTEt4Yg-6jeFsn8JCyEJZzr2dZPU34g.0k4w2xyJIUOYqmkysmWMZMbVTp65qLiLZjlmhF5mDpIg.JPEG.kongg1005%2FIMG_9393.jpg&type=a340',
       'name':'조개구이',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTA0MDNfMTk3%2FMDAxNTU0MjcyMTIwNDI2.jROdFWZF-Urd6JkeKoeG-nJ018D79ZF92A5Vh5OrXxQg.SLu07vboj9q4mM90_yks4DseiVHdHqZXD29HLpt748Eg.GIF.clubnina%2F20190330_171459.gif&type=a340',
       'name':'김치찌개',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzEyMzBfNzIg%2FMDAxNTE0NjI5MzEwNTU0._eFcXg4Z6aJvqHLKJEPGOwSrlzHqlwR5RanxM867hA8g.VaDWnmJYmLnzhDCPEON7ev3x30s9Kmyw9iAyDNYrMm8g.JPEG.yonugy%2F%25B5%25D0%25B3%25BB%25B8%25E9%25B8%25C0%25C1%25FD%25B8%25B8%25B5%25CE%25B1%25B9%25B8%25C0%25C1%25FD%25C4%25AE%25B1%25B9%25BC%25F6%25B8%25C0%25C1%25FD%25B0%25A8%25C0%25DA%25C0%25FC%25B8%25C0%25C1%25FD20171230-IMG_0836.JPG&type=a340',
       'name':'만둣국',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAyMTlfMjIx%2FMDAxNjQ1MjU2Nzg1NjY4.FCEIKzUnzyctu4MhQxNcp9isvNen8P98uIxFkWykpnQg.b_pxSywpF70dJKvVQkfrdBJfpEvyIt_eWwo4XWxBeUMg.JPEG.cowqk1004%2F1645256785387.jpg&type=a340',
       'name':'우동',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNjExMjVfMjg2%2FMDAxNDgwMDQ2MzM4MjQz.lcvl1nqUh5qDcKWCMOm72K2weS9GVBuGCg5QRsauHJMg.JKYy2nfSC_NgpYZ0SBozcNLZsXdo4oX4cy7T4rknOX8g.JPEG.pyoun0181%2F%25BF%25C0%25B4%25F3%25C5%25C1DSC04461-001.jpg&type=a340',
       'name':'오뎅탕',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTExMTBfMTg0%2FMDAxNjM2NTI2NDg3MTkx.ogUC48E_EgbOG_2GifOC6OiBvQEJ5eQEckpCG_0DDAEg.rRXsKrdN4i-3DkItYvw4WUjJACN0VjprCyKVDgaUTuog.JPEG.dtd_95%2FIMG_7114.jpg&type=a340',
       'name':'국수',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://recipe1.ezmember.co.kr/cache/recipe/2019/03/03/11baafbe81803965b17c3ab42a5992cb1.jpg',
       'name':'소불고기',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://t1.daumcdn.net/liveboard/dailylife/7e239e8f47dd47a9bd1ffb9079b3cfa0.jpg',
       'name':'양꼬치',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://t1.daumcdn.net/cfile/tistory/99E1D4495D7DA0F932',
       'name':'스파게티',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'http://kormedi.com/wp-content/uploads/2021/10/r658x041.jpg',
       'name':'짜장면',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://img.hankyung.com/photo/202012/02.24628239.1.jpg',
       'name':'비빔면',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://img.hankyung.com/photo/202106/01.26649267.1.jpg',
       'name':'냉면',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'http://doksanseongfood.com/files/attach/images/212/670/b907ec1fe136b8b5d2aea9e6f60bb944.jpg',
       'name':'생선구이',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://cafe24img.poxo.com/jhygroup/web/product/big/202011/4aaa0c1c1c6ca22b1bd4828c8c8f1ec1.png',
       'name':'치킨',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'http://img.nbntv.co.kr/resources/2019/01/28/m_AnpaF1wWKLYnX8ex.jpg',
       'name':'돼지두루치기',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://file.mk.co.kr/meet/neds/2021/11/image_readtop_2021_1080531_16371756654852938.jpg',
       'name':'카레',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/02/a0002274/img/basic/a0002274_main.jpg?20200626102550&q=80&rw=750&rh=536',
       'name':'돈까스',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://img.hankyung.com/photo/202108/99.26501439.1.jpg',
       'name':'피자',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'http://img4.tmon.kr/cdn3/deals/2021/03/05/5463612318/front_58bc8_qseiv.jpg',
       'name':'떡볶이',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://img.etoday.co.kr/pto_db/2019/10/600/20191011164701_1375452_600_362.jpg',
       'name':'닭갈비',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://newsimg.sedaily.com/2021/11/24/22U54KFD5N_3.jpg',
       'name':'햄버거',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://cdn.crowdpic.net/detail-thumb/thumb_d_196BE1F2F6A92446A09FA76DFC8C9F64.jpg',
       'name':'회',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://recipe1.ezmember.co.kr/cache/recipe/2017/06/14/a804caadb0d47c608fcf326c66e1abc31.jpg',
       'name':'조개탕',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://simg.ssgcdn.com/trans.ssg?src=/cmpt/edit/202005/28/102020052810014534459085730018_841.jpg&w=830&t=08500ac239997fb0e9e148a739bc0eb9f874bb77',
       'name':'부대찌개',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://recipe1.ezmember.co.kr/cache/recipe/2017/04/26/ddd495fd432955701068e1a21a0d33211.jpg',
       'name':'된장찌개',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'http://www.chungjungone.com/knowhow/images/blog/ezr/ker76/1.jpg',
       'name':'수제비',
       'like': 0}
db.food.insert_one(doc)

doc = {'img':'https://recipe1.ezmember.co.kr/cache/recipe/2021/08/05/98998b80a8bba88b91b8829417f416a61.jpg',
       'name':'아구찜',
       'like': 0}
db.food.insert_one(doc)


