> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 https://blog.csdn.net/weixin_38927522/article/details/123693086 <link rel="stylesheet" href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/editerView/ck_htmledit_views-163de54645.css"> 

继续跟着上一篇搞起来：
上一篇传输门：[https://blog.csdn.net/weixin_38927522/article/details/123691665](https://blog.csdn.net/weixin_38927522/article/details/123691665)

在我的记忆里，国外大部分航司全部是用的这一套，像韩国的，捷星航空，还有美国的一些航空。

这一篇我直接先将思路公布一下：

```
思路：
    1\. 首先访问 https://www.flyasiana.com/5qSZcnDz_/hGWtnW/AkEc/auTFfPPk/9rYphrpkup/dDswFj8m/FVRIJ3V/tGkQ?n$eum=157910959357612400 ,取出 set_cookie (ak_bmsc, bm_sz, _abck)
    2\. 再通过 _abck 动态生成 sensor_data
    3\. 再次访问  https://www.flyasiana.com/5qSZcnDz_/hGWtnW/AkEc/auTFfPPk/9rYphrpkup/dDswFj8m/FVRIJ3V/tGkQ?n$eum=157910959357612400 , 携带 三个cookie 以及 sensor_data ,注意：sensor_data 是一个 request playload, 因此需要 json.dumps() 。取出 set_cookie (_abck)
    4\. 携带 _abck 进行访问 https://www.flyasiana.com/I/CN/CH/SearchRevenueDomesticFareDrivenAvailFlights.do?n$eum=157910959357612400 。取到返回值
    5\. 如果第四步 返回状态码为 403, 则将参与以上步骤进行置换_abck值

```

**sensor_data 生成重写前 js：**

```
function pd() {
    var a = 0;

    a = bmak["get_cf_date"]();
    var t = bmak["updatet"](),
        e = 3;
    bmak["ckie"] && (e = bmak["get_cookie"]());
    var n = bmak["gd"](),
        o = "do_en",
        m = "dm_en",
        r = "t_en",
        i = o + "," + m + "," + r,
        c = bmak["forminfo"](),
        b = bmak["getdurl"](),
        d = bmak["aj_type"] + "," + bmak["aj_indx"];
    !bmak["fpcf"]["fpValCalculated"] && (0 == bmak["js_post"] || bmak["aj_indx"] > 0) && bmak["fpcf"]["fpVal"]();
    var k = bmak['ke_vel'] + bmak['me_vel'] + bmak['doe_vel'] + bmak['dme_vel'] + bmak['te_vel'] + bmak['pe_vel'],
        s = bmak["get_cf_date"]() - bmak['start_ts'],
        l = bmak['pi'](bmak['d2'] / 6),
        u = bmak['fas'](),
        _ = [bmak['ke_vel'] + 1, bmak['me_vel'] + 1, bmak['te_vel'], bmak['doe_vel'], bmak['dme_vel'], bmak['pe_vel'], k, t, bmak['init_time'], bmak['start_ts'], bmak["fpcf"]["td"], bmak['d2'], bmak['ke_cnt'], bmak['me_cnt'], l, bmak['pe_cnt'], bmak['te_cnt'], s, bmak['ta'], bmak["n_ck"], e, bmak['ab'](e), bmak["fpcf"]["rVal"], bmak["fpcf"]["rCFP"], u],
        f = _.join(","),
        p = '' + bmak['ab'](bmak["fpcf"]["fpValstr"]),
        v = bmak['sed']();

    sensor_data = bmak['ver'] + '-1,2,-94,-100,' + n + '-1,2,-94,-101,' + i + '-1,2,-94,-105,' + bmak['informinfo'] + '-1,2,-94,-102,' + c + '-1,2,-94,-108,' + bmak['kact'] + '-1,2,-94,-110,' + bmak['mact'] + '-1,2,-94,-117,' + bmak['tact'] + '-1,2,-94,-111,' + bmak['doact'] + '-1,2,-94,-109,' + bmak['dmact'] + '-1,2,-94,-114,' + bmak['pact'] + '-1,2,-94,-103,' + bmak['vcact'] + '-1,2,-94,-112,' + b + '-1,2,-94,-115,' + f + '-1,2,-94,-106,' + d,
        sensor_data = sensor_data + '-1,2,-94,-119,' + bmak['mr'] + '-1,2,-94,-122,' + v + '-1,2,-94,-123,' + bmak['mn_r'];
    var h = bmak['ab'](sensor_data);
    sensor_data = sensor_data + '-1,2,-94,-70,' + bmak["fpcf"]["fpValstr"] + '-1,2,-94,-80,' + p + '-1,2,-94,-116,' + bmak['o9'] + '-1,2,-94,-118,' + h + '-1,2,-94,-121,',
        bmak["sd_debug"](',s1:' + sensor_data['slice'](0, 10))

    var g = bmak['od'](bmak['cs'], bmak['api_public_key'])['slice'](0, 16),
        w = Math['floor'](bmak["get_cf_date"]() / 36e5),
        y = bmak["get_cf_date"](),
        C = g + bmak['od'](w, g) + sensor_data;
    sensor_data = C + ';' + (bmak["get_cf_date"]() - a) + ';' + bmak['tst'] + ';' + (bmak["get_cf_date"]() - y)
}

```

我已经将部分值打断点调试为定制，设备指纹目前写死的情况。
**sensor_data 重写后**：

```
function get_cf_date() {
    return Date.now ? Date.now() : +new Date
}

function updatet() {
    return get_cf_date() - (Date.now ? Date.now() : +new Date)
}

function pi(a) {
    return parseInt(a)
}

function ab(a) {
    if (null == a) return -1;
    try {

        for (var t = 0, e = 0; e < a.length; e++) {
            var n = a.charCodeAt(e);
            n < 128 && (t += n)
        }
        return t
    } catch (a) {
        return -2
    }
}

function od(a, t) {
    try {
        a = String(a);
        t = String(t);
        var e = [];
        var n = t.length;
        if (n > 0) {
            for (var o = 0; o < a.length; o++) {
                var m = a['charCodeAt'](o);
                var r = a['charAt'](o);
                var i = t['charCodeAt'](o % n);
                var m = bmak['rir'](m, 47, 57, i);
                m != a['charCodeAt'](o) && (r = String['fromCharCode'](m)),
                    e['push'](r)
            }
            if (e.length > 0) return e.join('')
        }
    } catch (a) {
    }
    return a
}

function pd() {

    var ver = 1.41;
    var a = get_cf_date();
    var t = updatet();
    var e = bmak["get_cookie"]();
    var n = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36,uaend,12147,20030107,zh-CN,Gecko,3,0,0,0,385409,1471924,1536,864,1536,864,858,760,1536,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:0,sc:0,wrc:1,isc:0,vib:1,bat:1,x11:0,x12:1,8323,0.983836920491,783200735962,loc:";
    var i = "do_en" + "," + "dm_en" + "," + "t_en";
    var c = "0,-1,0,0,1340,113,0;0,-1,0,0,916,-1,0;0,-1,0,0,918,-1,0;0,-1,0,0,921,-1,0;0,-1,0,0,964,-1,1;0,-1,0,0,966,-1,1;0,-1,0,0,967,-1,1;";
    var b = "https://www.flyasiana.com/C/CN/CH/index";
    var d = 1 + "," + 1;
    var s = get_cf_date() - (Date.now ? Date.now() : +new Date);
    var l = pi(16756 / 6);
    var u = 30261693;

    var k = 7584 + 1599 + 1556;
    var _ = [1, 7777 + 1, 0, 1599, 1556, 0, k, t, 0, (Date.now ? Date.now() : +new Date), 4, 16756, 0, 1, l, 2, 0, s, 0, 1, e, ab(e), "126", "-1066190195", u];

    var f = _.join(",");
    var p = '' + ab("-1752250632;dis;,7,8;true;true;true;-480;true;24;24;true;false;-1");
    var v = "0,0,0,0,1,0,0";

    var mact = "0,1,7513,853,371;1,1,7516,853,371;2,1,7522,843,370;3,1,7530,833,369;4,1,7538,826,367;5,1,7545,817,366;6,1,7553,808,364;7,1,7561,801,362;8,1,7569,796,360;9,1,7576,790,359;10,1,7585,787,358;11,1,7592,784,357;12,1,7600,780,356;13,1,7632,778,356;14,1,7640,778,355;15,1,7648,777,355;16,1,7665,776,355;17,1,7681,776,354;18,1,7697,775,354;19,1,7720,774,354;20,1,7793,772,354;21,3,8249,772,354,2176;22,4,8377,772,354,2176;23,2,8377,772,354,2176;24,1,8561,773,354;25,1,8569,779,358;26,1,8576,784,362;27,1,8585,791,367;28,1,8592,798,373;29,1,8601,808,381;30,1,8608,818,387;31,1,8616,828,396;32,1,8625,840,406;33,1,8633,850,416;";

    var sensor_data = ver + '-1,2,-94,-100,' + n + '-1,2,-94,-101,' + i + '-1,2,-94,-105,' + "0,-1,0,0,1340,113,0;" + '-1,2,-94,-102,' + c + '-1,2,-94,-108,' + "" + '-1,2,-94,-110,' + mact + '-1,2,-94,-117,' + "" + '-1,2,-94,-111,' + "0,1613,-1,-1,-1;" + '-1,2,-94,-109,' + "0,1613,-1,-1,-1,-1,-1,-1,-1,-1,-1;" + '-1,2,-94,-114,' + "" + '-1,2,-94,-103,' + "2,3443;3,9857;2,10883;3,51884;2,52813;3,55619;2,56282;3,59249;2,60333;" + '-1,2,-94,-112,' + b + '-1,2,-94,-115,' + f + '-1,2,-94,-106,' + d;

    sensor_data = sensor_data + '-1,2,-94,-119,' + "7,8,9,8,17,19,13,8,6,6,5,5,283,307," + '-1,2,-94,-122,' + v + '-1,2,-94,-123,' + "";
    var h = ab(sensor_data);

    sensor_data = sensor_data + '-1,2,-94,-70,' + "-1752250632;dis;,7,8;true;true;true;-480;true;24;24;true;false;-1" + '-1,2,-94,-80,' + p + '-1,2,-94,-116,' + 4419261 + '-1,2,-94,-118,' + h + '-1,2,-94,-121,';

    var g = "7a74G7m23Vrp0o5c";
    var w = Math.floor(get_cf_date() / 36e5);
    var y = get_cf_date();
    var C = g + od(w, g) + sensor_data;
    sensor_data = C + ';' + (get_cf_date() - a) + ';' + (get_cf_date() - a + 100) + ';' + (get_cf_date() - y);

    return sensor_data
}

```

缺啥补啥，继续搞 -》get_sensor_data.js：

```
function get_cf_date() {
    return Date.now ? Date.now() : +new Date
}

function updatet() {
    return get_cf_date() - (Date.now ? Date.now() : +new Date)
}

function pi(a) {
    return parseInt(a)
}

function ab(a) {
    if (null == a) return -1;
    try {

        for (var t = 0, e = 0; e < a.length; e++) {
            var n = a.charCodeAt(e);
            n < 128 && (t += n)
        }
        return t
    } catch (a) {
        return -2
    }
}

function od(a, t) {
    try {
        a = String(a);
        t = String(t);
        var e = [];
        var n = t.length;
        if (n > 0) {
            for (var o = 0; o < a.length; o++) {
                var m = a['charCodeAt'](o);
                var r = a['charAt'](o);
                var i = t['charCodeAt'](o % n);
                var m = bmak['rir'](m, 47, 57, i);
                m != a['charCodeAt'](o) && (r = String['fromCharCode'](m)),
                    e['push'](r)
            }
            if (e.length > 0) return e.join('')
        }
    } catch (a) {
    }
    return a
}

function get_sensor_data() {
    var ver = 1.41;
    var a = get_cf_date();
    var t = updatet();
    var e = "this_is_abck_cookie";
    var n = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36,uaend,12147,20030107,zh-CN,Gecko,3,0,0,0,385409,1471924,1536,864,1536,864,858,760,1536,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:0,sc:0,wrc:1,isc:0,vib:1,bat:1,x11:0,x12:1,8323,0.983836920491,783200735962,loc:";
    var i = "do_en" + "," + "dm_en" + "," + "t_en";
    var c = "0,-1,0,0,1340,113,0;0,-1,0,0,916,-1,0;0,-1,0,0,918,-1,0;0,-1,0,0,921,-1,0;0,-1,0,0,964,-1,1;0,-1,0,0,966,-1,1;0,-1,0,0,967,-1,1;";
    var b = "https://www.flyasiana.com/C/CN/CH/index";
    var d = 1 + "," + 1;
    var s = get_cf_date() - (Date.now ? Date.now() : +new Date);
    var l = pi(16756 / 6);
    var u = 30261693;

    var k = 7584 + 1599 + 1556;
    var _ = [1, 7777 + 1, 0, 1599, 1556, 0, k, t, 0, (Date.now ? Date.now() : +new Date), 4, 16756, 0, 1, l, 2, 0, s, 0, 1, e, ab(e), "126", "-1066190195", u];

    var f = _.join(",");
    var p = '' + ab("-1752250632;dis;,7,8;true;true;true;-480;true;24;24;true;false;-1");
    var v = "0,0,0,0,1,0,0";

    var mact = "0,1,7513,853,371;1,1,7516,853,371;2,1,7522,843,370;3,1,7530,833,369;4,1,7538,826,367;5,1,7545,817,366;6,1,7553,808,364;7,1,7561,801,362;8,1,7569,796,360;9,1,7576,790,359;10,1,7585,787,358;11,1,7592,784,357;12,1,7600,780,356;13,1,7632,778,356;14,1,7640,778,355;15,1,7648,777,355;16,1,7665,776,355;17,1,7681,776,354;18,1,7697,775,354;19,1,7720,774,354;20,1,7793,772,354;21,3,8249,772,354,2176;22,4,8377,772,354,2176;23,2,8377,772,354,2176;24,1,8561,773,354;25,1,8569,779,358;26,1,8576,784,362;27,1,8585,791,367;28,1,8592,798,373;29,1,8601,808,381;30,1,8608,818,387;31,1,8616,828,396;32,1,8625,840,406;33,1,8633,850,416;";

    var sensor_data = ver + '-1,2,-94,-100,' + n + '-1,2,-94,-101,' + i + '-1,2,-94,-105,' + "0,-1,0,0,1340,113,0;" + '-1,2,-94,-102,' + c + '-1,2,-94,-108,' + "" + '-1,2,-94,-110,' + mact + '-1,2,-94,-117,' + "" + '-1,2,-94,-111,' + "0,1613,-1,-1,-1;" + '-1,2,-94,-109,' + "0,1613,-1,-1,-1,-1,-1,-1,-1,-1,-1;" + '-1,2,-94,-114,' + "" + '-1,2,-94,-103,' + "2,3443;3,9857;2,10883;3,51884;2,52813;3,55619;2,56282;3,59249;2,60333;" + '-1,2,-94,-112,' + b + '-1,2,-94,-115,' + f + '-1,2,-94,-106,' + d;

    sensor_data = sensor_data + '-1,2,-94,-119,' + "7,8,9,8,17,19,13,8,6,6,5,5,283,307," + '-1,2,-94,-122,' + v + '-1,2,-94,-123,' + "";
    var h = ab(sensor_data);

    sensor_data = sensor_data + '-1,2,-94,-70,' + "-1752250632;dis;,7,8;true;true;true;-480;true;24;24;true;false;-1" + '-1,2,-94,-80,' + p + '-1,2,-94,-116,' + 4419261 + '-1,2,-94,-118,' + h + '-1,2,-94,-121,';

    var g = "7a74G7m23Vrp0o5c";
    var w = Math.floor(get_cf_date() / 36e5);
    var y = get_cf_date();
    var C = g + od(w, g) + sensor_data;
    sensor_data = C + ';' + (get_cf_date() - a) + ';' + (get_cf_date() - a + 100) + ';' + (get_cf_date() - y);

    return sensor_data
}

```

以上改写成了可调用的方式：

```
    def __get_sensor_data(self, old_abck_cookie: str):
        """
        根据 old_abck_cookie ,获取 sensor_data
        """
        with open(JS_FILENAME, "r", encoding="utf-8") as f:
            js_content = f.read().replace("this_is_abck_cookie", old_abck_cookie).replace("this_is_url", self.url)
        jscontext = execjs.compile(js_content)
        sensor_data = jscontext.call('get_sensor_data')
        return sensor_data

```

整个流程用 python 模拟下：

```
# -*- coding: utf-8 -*-
# @Author  : Codeooo
# @Time    : 2022/03/25

import json
import execjs
import requests
from fake_useragent import UserAgent

JS_FILENAME = "get_sensor_data.js"

class Abck_Cookie:

    def __init__(self, headers, url, data=None):
        self.headers = headers
        self.url = url
        self.data = data
        self.proxies = None

    def __get_sensor_data(self, old_abck_cookie: str):
        """
        根据 old_abck_cookie ,获取 sensor_data
        """
        with open(JS_FILENAME, "r", encoding="utf-8") as f:
            js_content = f.read().replace("this_is_abck_cookie", old_abck_cookie).replace("this_is_url", self.url)
        jscontext = execjs.compile(js_content)
        sensor_data = jscontext.call('get_sensor_data')
        print("生成sensor_data：",sensor_data)
        return sensor_data

    def __get_old_abck(self):
        """
        获取 set_cookie 中的 _abck_cookie_value,以及所有的 cookie
        """
        headers = {
            "User-Agent": UserAgent().random,
            'content-type': 'text/plain;charset=UTF-8',
        }
        # 更新添加自己所写 headers
        headers.update(self.headers)
        try:
            old_abck_response = requests.post(url=self.url, headers=headers, proxies=self.proxies, data=self.data,
                                              timeout=5)
            print("old_abck_response:",old_abck_response.text)
        except Exception as e:
            return False
        for cookie in old_abck_response.cookies:
            if cookie.name == "_abck":
                return (cookie.value, old_abck_response.cookies)
        return False

    def __get_new_abck(self, sensor_data=None, cookies=None):
        """
        获取 set_cookie 中的 _abck_cookie
        """
        cookies_dict = {cookie.name: cookie.value for cookie in cookies}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv',
            'Content-Type': 'text/plain;charset=UTF-8',
            'Connection': 'keep-alive',
            'Cookie': 'ak_bmsc={}; bm_sz={}; _abck={}'.format(cookies_dict.get("ak_bmsc"), cookies_dict.get("bm_sz"),
                                                              cookies_dict.get("_abck")),
            'TE': 'Trailers'
        }
        headers.update(self.headers)
        data = {
            "sensor_data": sensor_data
        }
        try:
            res = requests.post(url=self.url, headers=headers, data=json.dumps(data), proxies=self.proxies, timeout=5)
            print("get_new_abck：", res.text)
        except:
            return False

        self.cookies = res.cookies.get_dict()
        print("=======当前可用cookies====",self.cookies)

    def execute_get_abck_cookie(self):
        """
        统一规划，执行获得新的 abck_cookie
        :return:abck_cookie
        """
        # 获取 未可以使用的 abck_cookie
        old_abck_cookie, cookies = self.__get_old_abck()
        # 获取 sensor_data
        sensor_data = self.__get_sensor_data(old_abck_cookie)
        # 获取 可以使用的 abck_cookie
        self.__get_new_abck(sensor_data, cookies)

if __name__ == '__main__':
    url = "https://www.flyasiana.com/5qSZcnDz_/hGWtnW/AkEc/auTFfPPk/9rYphrpkup/dDswFj8m/FVRIJ3V/tGkQ?n$eum=157910959357612400"

    headers = {
        'authority': 'www.flyasiana.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'referer': 'https://www.flyasiana.com/I/CN/CH/RevenueRegistTravel.do',
    }

    abck = Abck_Cookie(url=url, headers=headers)

    abck.execute_get_abck_cookie()

```

运行结果 ======：
![](https://img-blog.csdnimg.cn/ac5e76ea5c5b4ebea0a2c162a9650ae2.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ29kZW9vbw==,size_20,color_FFFFFF,t_70,g_se,x_16)

```
get_sensor_data.js 文件中
        部分值为固定的直接做了替换；
        值不固定的，则按照首次请求后得到的结果 做替换。
    以下是可能会对 cookie 产生约束的字段
        bmak['mact']   也和时间戳有关系。
        bmak['vcact']  感觉有在控制次数。每次重新请求一下都会新添加 两个数
        bmak['me_cnt']  请求之间的累计间隔时间。 初始化为 1
        bmak['pe_cnt']  请求次数 * 2  ，初始化为 0
        bmak['ta']  当前请求时间与初始化时间的累和  ，初始化为 0
        bmak['me_vel']   也同样是一个累计运算。 再加上当前请求时间与初始化时间的差
        bmak['dme_vel']  感觉像似响应时长。
        bmak['pe_vel']   看js 的加密，应该是 在原来的基础上 加上 请求次数 * 2 ，以及时间。但是直接打印 一直为 

```

<link href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/editerView/markdown_views-89f5acb30b.css" rel="stylesheet"> <link href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/style-49037e4d27.css" rel="stylesheet">