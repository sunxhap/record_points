> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 https://blog.csdn.net/weixin_38927522/article/details/123691665 <link rel="stylesheet" href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/editerView/ck_htmledit_views-163de54645.css"> 

**Akamai 阿卡迈**：常用于国[外网](https://so.csdn.net/so/search?q=%E5%A4%96%E7%BD%91&spm=1001.2101.3001.7020)站，2019 年初期版本验证 cookies 中的_abck, 后期增加 ak_bmsc 等其他指纹设备。

**常见网站：**
韩国大韩航空：[https://www.koreanair.com/cn/zh-cn](https://www.koreanair.com/cn/zh-cn)
韩国韩亚航空：[https://www.flyasiana.com/C/CN/KO/index](https://www.flyasiana.com/C/CN/KO/index)
电子元器件： [https://www.ti.com/](https://www.ti.com/)
nike 官网： [https://www.nike.com/cn](https://www.nike.com/cn)

```
本文以韩亚航空为例：
采集航空机票数据的时候，我们发现cookie中的这些参数，无疑是akamai:

```

用 cookies 插件查看下 cookie 值：
![](https://img-blog.csdnimg.cn/3fd25e3318f84199a792e251163c9a87.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ29kZW9vbw==,size_20,color_FFFFFF,t_70,g_se,x_16)
清掉 cookies 观察发送请求包：

![](https://img-blog.csdnimg.cn/748cab37ac8c40d7bc85c49eaa0c8f21.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ29kZW9vbw==,size_20,color_FFFFFF,t_70,g_se,x_16)
这个请求就很奇怪，像是心跳包，只要是会话超时以及清掉 ck, 必然会发一个，我们看下参数是什么：
![](https://img-blog.csdnimg.cn/e987ad3f6b9a4e24b42bb85b40b349b1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ29kZW9vbw==,size_20,color_FFFFFF,t_70,g_se,x_16)
看到 sensor_data 更加无疑是阿卡迈了。。。
走完这个接口生成——abck?
![](https://img-blog.csdnimg.cn/961e864cb08b465bb6a75d0b2bc1375e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ29kZW9vbw==,size_20,color_FFFFFF,t_70,g_se,x_16)
堆栈追踪：逻辑还很是清楚的。
![](https://img-blog.csdnimg.cn/39103cb1ce18478bba9c304ffd35aec1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ29kZW9vbw==,size_20,color_FFFFFF,t_70,g_se,x_16)

![](https://img-blog.csdnimg.cn/499750d477a54b21a9012c94b3491053.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ29kZW9vbw==,size_20,color_FFFFFF,t_70,g_se,x_16)
这个数组很重要，一会需要我们还原下：
![](https://img-blog.csdnimg.cn/216b8217a17141489e69c9264ef984d8.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAQ29kZW9vbw==,size_20,color_FFFFFF,t_70,g_se,x_16)

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<script>
    var _0xf488 = ["\x4d\x69\x63\x72\x6f\x73\x6f\x66\x74\x20\x54\x61\x69\x20\x4c\x65", "\x69\x6e\x64\x65\x78\x65\x64\x44\x62\x4b\x65\x79", "\x6f\x70\x65\x72\x61", "\x68\x79\x70\x6f\x74", "\x63\x6c\x69\x63\x6b", "\x74\x6f\x75\x63\x68\x73\x74\x61\x72\x74", "\x24\x63\x68\x72\x6f\x6d\x65\x5f\x61\x73\x79\x6e\x63\x53\x63\x72\x69\x70\x74\x49\x6e\x66\x6f", "\x63\x6c\x65\x61\x72\x43\x61\x63\x68\x65", "\x73\x6c\x69\x63\x65", "\x61\x63\x63\x65\x6c\x65\x72\x61\x74\x69\x6f\x6e\x49\x6e\x63\x6c\x75\x64\x69\x6e\x67\x47\x72\x61\x76\x69\x74\x79", "\x6e\x61\x76\x69\x67\x61\x74\x6f\x72", "\x61\x6c\x6c", "\x2c\x22\x61\x75\x74\x68\x22\x20\x3a\x20\x22", "\x67\x65\x74\x5f\x73\x74\x6f\x70\x5f\x73\x69\x67\x6e\x61\x6c\x73", "\x74\x6f", "\x4d\x65\x6e\x6c\x6f", "\x70\x61\x63\x74", "\x6b\x65\x79\x64\x6f\x77\x6e", "\x69\x73\x49\x67\x6e", "\x73\x65\x61\x72\x63\x68", "\x67\x65\x74\x53\x74\x6f\x72\x61\x67\x65\x55\x70\x64\x61\x74\x65\x73", "\x41\x72\x69\x61\x6c\x48\x65\x62\x72\x65\x77\x2d\x4c\x69\x67\x68\x74", "\x66\x6f\x6e\x74\x46\x61\x6d\x69\x6c\x79", "\x77\x65\x62\x64\x72\x69\x76\x65\x72", "\x74\x6d\x65\x5f\x63\x6e\x74", "\x72\x65\x71\x75\x65\x73\x74\x4d\x65\x64\x69\x61\x4b\x65\x79\x53\x79\x73\x74\x65\x6d\x41\x63\x63\x65\x73\x73", "\x42\x75\x66\x66\x65\x72", "\x68\x6f\x73\x74\x6e\x61\x6d\x65", "\x63\x73\x73\x54\x65\x78\x74", "\x6e\x5f\x63\x6b", "\x69\x64", "\x6b\x65\x5f\x76\x65\x6c", "\x46\x75\x74\x75\x72\x61", "\x50\x4f\x53\x54", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x32\x30\x2c", "\x64\x61\x74\x61", "\x6c\x69\x73\x74\x46\x75\x6e\x63\x74\x69\x6f\x6e\x73", "\x64\x6d\x61\x5f\x74\x68\x72\x6f\x74\x74\x6c\x65", "\x4d\x61\x63\x20\x4f\x53\x20\x58\x20\x31\x30\x5f\x35", "\x6c\x61\x6e\x67\x75\x61\x67\x65", "\x43\x6f\x75\x72\x69\x65\x72\x20\x4e\x65\x77", "\x72\x67\x62\x28\x31\x32\x30\x2c\x20\x31\x38\x36\x2c\x20\x31\x37\x36\x29", "\x62\x6f\x64\x79", "\x57\x69\x6e\x64\x6f\x77\x73\x20\x4d\x65\x64\x69\x61\x20\x50\x6c\x61\x79\x65\x72\x20\x50\x6c\x75\x67\x2d\x69\x6e\x20\x44\x79\x6e\x61\x6d\x69\x63\x20\x4c\x69\x6e\x6b\x20\x4c\x69\x62\x72\x61\x72\x79", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x38\x30\x2c", "\x61\x70\x70\x6c\x79", "\x57\x65\x62\x45\x78\x36\x34\x20\x47\x65\x6e\x65\x72\x61\x6c\x20\x50\x6c\x75\x67\x69\x6e\x20\x43\x6f\x6e\x74\x61\x69\x6e\x65\x72", "\x76\x63\x5f\x63\x6e\x74", "\x2c\x69\x74\x30", "\x67\x66", "\x69\x31\x3a", "\x70\x61\x67\x65\x58", "\x4c\x61\x74\x6f", "\x5f\x73\x65\x74\x41\x75", "\x73\x65\x73\x73\x69\x6f\x6e\x53\x74\x6f\x72\x61\x67\x65\x4b\x65\x79", "\x4c\x6f\x62\x73\x74\x65\x72", "\x64\x69\x73\x46\x70\x43\x61\x6c\x4f\x6e\x54\x69\x6d\x65\x6f\x75\x74", "\x73\x65\x74\x5f\x63\x6f\x6f\x6b\x69\x65", "\x57\x45\x42\x47\x4c\x5f\x64\x65\x62\x75\x67\x5f\x72\x65\x6e\x64\x65\x72\x65\x72\x5f\x69\x6e\x66\x6f", "\x73\x74\x72\x6f\x6b\x65\x53\x74\x79\x6c\x65", "\x43\x6f\x72\x73\x69\x76\x61\x20\x48\x65\x62\x72\x65\x77", "\x72\x43\x46\x50", "\x64\x6f\x63\x75\x6d\x65\x6e\x74\x45\x6c\x65\x6d\x65\x6e\x74", "\x5f\x5f\x77\x65\x62\x64\x72\x69\x76\x65\x72\x5f\x75\x6e\x77\x72\x61\x70\x70\x65\x64", "\x2c\x73\x32\x3a", "\x6d\x6e\x5f\x73\x74\x6f\x75\x74", "\x72\x65\x71\x75\x69\x72\x65\x64", "\x70\x61\x72\x73\x65\x49\x6e\x74", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x30\x36\x2c", "\x5f\x73\x65\x74\x50\x6f\x77\x53\x74\x61\x74\x65", "\x72\x61\x6e\x64\x6f\x6d", "\x70\x61\x79\x6d\x65\x6e\x74\x2d\x68\x61\x6e\x64\x6c\x65\x72", "\x50\x72\x65\x73\x73\x20\x53\x74\x61\x72\x74\x20\x32\x50", "\x62\x64", "\x69\x6e\x64\x65\x78\x4f\x66", "\x66\x69\x6c\x6c\x54\x65\x78\x74", "\x41\x63\x74\x69\x76\x65\x58\x4f\x62\x6a\x65\x63\x74", "\x63\x6f\x6f\x6b\x69\x65", "\x62\x75\x74\x74\x6f\x6e", "\x6d\x6e\x5f\x72", "\x6d\x6e\x5f\x6d\x63\x5f\x6c\x6d\x74", "\x6d\x61\x63\x74", "\x6e\x6f\x77", "\x70\x6c\x75\x67\x69\x6e\x49\x6e\x66\x6f", "\x24\x63\x64\x63\x5f\x61\x73\x64\x6a\x66\x6c\x61\x73\x75\x74\x6f\x70\x66\x68\x76\x63\x5a\x4c\x6d\x63\x66\x6c\x5f", "\x75\x6e\x64\x65\x66", "\x63\x61\x74\x63\x68", "\x79\x31", "\x6d\x6f\x7a\x49\x6e\x6e\x65\x72\x53\x63\x72\x65\x65\x6e\x59", "\x61\x63\x63\x65\x73\x73\x69\x62\x69\x6c\x69\x74\x79\x2d\x65\x76\x65\x6e\x74\x73", "\x67\x65\x74\x41\x74\x74\x72\x69\x62\x75\x74\x65", "\x72\x6f\x74\x61\x74\x69\x6f\x6e\x52\x61\x74\x65", "\x74\x69\x6d\x65\x7a\x6f\x6e\x65\x4f\x66\x66\x73\x65\x74\x4b\x65\x79", "\x5f\x5f\x6c\x61\x73\x74\x57\x61\x74\x69\x72\x43\x6f\x6e\x66\x69\x72\x6d", "\x67\x64", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x32\x39\x2c", "\x74\x61", "\x58\x4d\x4c\x48\x74\x74\x70\x52\x65\x71\x75\x65\x73\x74", "\x63\x6f\x6c\x6f\x72\x44\x65\x70\x74\x68", "\x66\x6f\x6e\x74\x53\x69\x7a\x65", "\x65\x6d\x69\x74", "\x67\x65\x74\x5f\x63\x6f\x6f\x6b\x69\x65", "\x70\x75\x73\x68", "\x6d\x64\x75\x63\x65\x5f\x63\x6e\x74", "\x77\x69\x64\x74\x68", "\x6d\x73\x48\x69\x64\x64\x65\x6e", "\x76\x69\x73\x69\x62\x69\x6c\x69\x74\x79\x63\x68\x61\x6e\x67\x65", "\x77\x65\x62\x6b\x69\x74\x76\x69\x73\x69\x62\x69\x6c\x69\x74\x79\x63\x68\x61\x6e\x67\x65", "\x70\x6f\x73\x69\x74\x69\x6f\x6e\x3a\x20\x72\x65\x6c\x61\x74\x69\x76\x65\x3b\x20\x6c\x65\x66\x74\x3a\x20\x2d\x39\x39\x39\x39\x70\x78\x3b\x20\x76\x69\x73\x69\x62\x69\x6c\x69\x74\x79\x3a\x20\x68\x69\x64\x64\x65\x6e\x3b\x20\x64\x69\x73\x70\x6c\x61\x79\x3a\x20\x62\x6c\x6f\x63\x6b\x20\x21\x69\x6d\x70\x6f\x72\x74\x61\x6e\x74", "\x2d\x31", "\x62\x70\x64", "\x73\x65\x6e\x64", "\x72\x6f\x74\x61\x74\x65\x5f\x72\x69\x67\x68\x74", "\x6f\x6e\x72\x65\x61\x64\x79\x73\x74\x61\x74\x65\x63\x68\x61\x6e\x67\x65", "\x5f\x5f\x6c\x61\x73\x74\x57\x61\x74\x69\x72\x41\x6c\x65\x72\x74", "\x78\x32", "\x6d\x69\x63\x72\x6f\x70\x68\x6f\x6e\x65", "\x66\x66", "\x73\x65\x74\x52\x65\x71\x75\x65\x73\x74\x48\x65\x61\x64\x65\x72", "\x77\x65\x62\x6b\x69\x74\x47\x65\x74\x47\x61\x6d\x65\x70\x61\x64\x73", "\x6d\x6e\x5f\x63\x64", "\x74\x5f\x64\x69\x73", "\x62\x6d\x69\x73\x63", "\x76\x63\x5f\x63\x6e\x74\x5f\x6c\x6d\x74", "\x70\x72\x6f\x74\x6f\x63\x6f\x6c", "\x74\x6f\x75\x63\x68\x63\x61\x6e\x63\x65\x6c", "\x71\x75\x65\x72\x79", "\x4a\x61\x76\x61\x20\x50\x6c\x75\x67\x2d\x69\x6e\x20\x32\x20\x66\x6f\x72\x20\x4e\x50\x41\x50\x49\x20\x42\x72\x6f\x77\x73\x65\x72\x73", "\x68\x76\x63", "\x43\x68\x72\x6f\x6d\x65\x20\x52\x65\x6d\x6f\x74\x65\x20\x44\x65\x73\x6b\x74\x6f\x70\x20\x56\x69\x65\x77\x65\x72", "\x61\x70\x69\x5f\x70\x75\x62\x6c\x69\x63\x5f\x6b\x65\x79", "\x61\x75\x74\x68", "\x5f\x5f\x64\x72\x69\x76\x65\x72\x5f\x65\x76\x61\x6c\x75\x61\x74\x65", "\x2c\x73\x31\x3a", "\x32", "\x77\x72", "\x76\x69\x62\x72\x61\x74\x65", "\x66\x6d\x68", "\x67\x65\x74\x5f\x63\x66\x5f\x64\x61\x74\x65", "\x66\x6f\x6e\x74", "\x66\x6f\x6e\x74\x73\x5f\x6f\x70\x74\x6d", "\x6d\x6e\x5f\x70\x6f\x6c\x6c", "\x2c\x6c\x6f\x63\x3a", "\x6d\x64\x75\x63\x65\x5f\x63\x6e\x74\x5f\x6c\x6d\x74", "\x70\x65\x6e", "\x73\x65\x73\x73\x69\x6f\x6e\x53\x74\x6f\x72\x61\x67\x65", "\x64\x6f\x65\x5f\x63\x6e\x74", "\x63\x6b\x69\x65", "\x67\x65\x74\x5f\x62\x72\x6f\x77\x73\x65\x72", "\x63\x72\x65\x61\x74\x65\x45\x6c\x65\x6d\x65\x6e\x74", "\x66\x6f\x6e\x74\x73", "\x6d\x6e\x5f\x63\x63", "\x64\x6f\x5f\x64\x69\x73", "\x5f\x5f\x66\x78\x64\x72\x69\x76\x65\x72\x5f\x65\x76\x61\x6c\x75\x61\x74\x65", "\x61\x6a\x5f\x69\x6e\x64\x78", "\x66\x70\x56\x61\x6c\x73\x74\x72", "\x67\x62", "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x2b\x2f", "\x6c\x6f\x63\x61\x6c\x53\x74\x6f\x72\x61\x67\x65\x4b\x65\x79", "\x68\x61\x73\x4f\x77\x6e\x50\x72\x6f\x70\x65\x72\x74\x79", "\x61\x70\x69\x63\x61\x6c\x6c\x5f\x62\x6d", "\x68\x62\x73", "\x3d\x3d", "\x6c\x76\x63", "\x70\x6f\x77", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x31\x39\x2c", "\x70\x65\x5f\x76\x65\x6c", "\x6f\x6e\x66\x6f\x63\x75\x73", "\x64\x6f\x61\x5f\x74\x68\x72\x6f\x74\x74\x6c\x65", "\x61\x66\x53\x62\x65\x70\x38\x79\x6a\x6e\x5a\x55\x6a\x71\x33\x61\x4c\x30\x31\x30\x6a\x4f\x31\x35\x53\x61\x77\x6a\x32\x56\x5a\x66\x64\x59\x4b\x38\x75\x59\x39\x30\x75\x78\x71", "\x47\x65\x6e\x65\x76\x61", "\x63\x6c\x69\x65\x6e\x74\x57\x69\x64\x74\x68", "\x63\x64\x6f\x61", "\x7b\x22\x73\x65\x73\x73\x69\x6f\x6e\x5f\x69\x64\x22\x20\x3a\x20\x22", "\x77\x65\x62\x72\x74\x63\x4b\x65\x79", "\x64\x65\x66\x61\x75\x6c\x74\x5f\x73\x65\x73\x73\x69\x6f\x6e", "\x68\x6d\x6d", "\x63\x65\x69\x6c", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x30\x35\x2c", "\x6a\x6f\x69\x6e", "\x5f\x70\x68\x61\x6e\x74\x6f\x6d", "\x61\x6a\x5f\x6c\x6d\x74\x5f\x74\x61\x63\x74", "\x23\x66\x36\x30", "\x6d\x6e\x5f\x67\x65\x74\x5f\x6e\x65\x77\x5f\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x5f\x70\x61\x72\x61\x6d\x73", "\x73\x74\x61\x72\x74\x54\x72\x61\x63\x6b\x69\x6e\x67", "\x6b\x65\x79\x43\x6f\x64\x65", "\x61\x76\x61\x69\x6c\x57\x69\x64\x74\x68", "\x3b\x20\x70\x61\x74\x68\x3d\x2f\x3b\x20\x65\x78\x70\x69\x72\x65\x73\x3d\x46\x72\x69\x2c\x20\x30\x31\x20\x46\x65\x62\x20\x32\x30\x32\x35\x20\x30\x38\x3a\x30\x30\x3a\x30\x30\x20\x47\x4d\x54\x3b", "\x68\x6d\x64", "\x63\x64\x6d\x61", "\x61\x62\x73", "\x73\x65\x64", "\x31\x36\x70\x74\x20\x41\x72\x69\x61\x6c", "\x68\x69\x64\x64\x65\x6e", "\x74\x6f\x4c\x6f\x77\x65\x72\x43\x61\x73\x65", "\x66\x70\x63\x66", "\x70\x6c\x75\x67\x69\x6e\x73", "\x58\x50\x61\x74\x68\x52\x65\x73\x75\x6c\x74", "\x2f\x67\x65\x74\x5f\x70\x61\x72\x61\x6d\x73", "\x69\x6e\x69\x74\x5f\x74\x69\x6d\x65", "\x6d\x6e\x5f\x77", "\x73\x70\x6c\x69\x74", "\x65", "\x5f\x5f\x24\x77\x65\x62\x64\x72\x69\x76\x65\x72\x41\x73\x79\x6e\x63\x45\x78\x65\x63\x75\x74\x6f\x72", "\x6f\x66\x66", "\x66\x70\x56\x61\x6c", "\x6f\x66\x66\x73\x65\x74\x57\x69\x64\x74\x68", "\x70\x65\x72\x73\x69\x73\x74\x65\x6e\x74\x2d\x73\x74\x6f\x72\x61\x67\x65", "\x74\x6f\x44\x61\x74\x61\x55\x52\x4c", "\x78\x61\x67\x67", "\x64\x6f\x63\x75\x6d\x65\x6e\x74", "\x69\x6e\x66\x6f\x72\x6d\x69\x6e\x66\x6f", "\x42\x61\x73\x69\x63\x20", "\x64\x6d\x65\x5f\x63\x6e\x74\x5f\x6c\x6d\x74", "\x69\x6e\x6e\x65\x72\x48\x65\x69\x67\x68\x74", "\x68\x74\x63", "\x70\x64\x75\x63\x65\x5f\x63\x6e\x74", "\x74\x6f\x46\x69\x78\x65\x64", "\x69\x72", "\x73\x74\x72\x69\x6e\x67\x69\x66\x79", "\x77\x65\x62\x67\x6c", "\x63\x6c\x69\x70\x62\x6f\x61\x72\x64", "\x44\x65\x76\x69\x63\x65\x4f\x72\x69\x65\x6e\x74\x61\x74\x69\x6f\x6e\x45\x76\x65\x6e\x74", "\x6d\x61\x67\x6e\x65\x74\x6f\x6d\x65\x74\x65\x72", "\x30\x61\x34\x36\x47\x35\x6d\x31\x37\x56\x72\x70\x34\x6f\x34\x63", "\x64\x65\x66\x61\x75\x6c\x74\x56\x61\x6c\x75\x65", "\x2c", "\x61\x62\x63\x64\x65\x66\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x78\x79\x7a\x31\x32\x33\x34\x35\x36\x37\x38\x39\x30\x3b\x2b\x2d\x2e", "\x6d\x6f\x7a\x49\x73\x4c\x6f\x63\x61\x6c\x6c\x79\x41\x76\x61\x69\x6c\x61\x62\x6c\x65", "\x41\x75\x74\x68\x6f\x72\x69\x7a\x61\x74\x69\x6f\x6e", "\x41\x70\x70\x6c\x65\x20\x47\x6f\x74\x68\x69\x63", "\x2d", "\x65\x78\x63\x65\x70\x74\x69\x6f\x6e", "\x69\x6d\x75\x6c", "\x42\x61\x74\x61\x6e\x67", "\x73\x74\x6f\x72\x65\x57\x65\x62\x57\x69\x64\x65\x54\x72\x61\x63\x6b\x69\x6e\x67\x45\x78\x63\x65\x70\x74\x69\x6f\x6e", "\x70\x61\x74\x70", "\x63\x61\x6c\x6c\x53\x65\x6c\x65\x6e\x69\x75\x6d", "\x73\x74\x72\x6f\x6b\x65", "\x33", "\x74\x5f\x74\x73\x74", "\x68\x70\x64", "\x4d\x6f\x6e\x61\x63\x6f", "\x63\x73\x68", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x32\x36\x2c", "\x2c\x73\x33\x3a", "\x57\x69\x6e\x67\x64\x69\x6e\x67\x73\x20\x32", "\x63\x6b\x61", "\x61\x6c\x70\x68\x61", "\x6d\x72", "\x30", "\x68\x74\x6d", "\x61\x64\x64\x45\x76\x65\x6e\x74\x4c\x69\x73\x74\x65\x6e\x65\x72", "\x73\x70\x65\x61\x6b\x65\x72", "\x69\x6e\x70\x75\x74", "\x6e\x6f\x6e\x3a", "\x63\x6c\x69\x70\x62\x6f\x61\x72\x64\x2d\x77\x72\x69\x74\x65", "\x64\x6d\x5f\x64\x69\x73", "\x64\x6f\x4e\x6f\x74\x54\x72\x61\x63\x6b", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x30\x38\x2c", "\x4d\x69\x63\x72\x6f\x73\x6f\x66\x74\x20\x53\x61\x6e\x73\x20\x53\x65\x72\x69\x66", "\x73\x66\x34", "\x63\x64\x63\x5f\x61\x64\x6f\x51\x70\x6f\x61\x73\x6e\x66\x61\x37\x36\x70\x66\x63\x5a\x4c\x6d\x63\x66\x6c\x5f\x53\x79\x6d\x62\x6f\x6c", "\x73\x74\x61\x72\x74\x5f\x74\x73", "\x67\x65\x74\x50\x61\x72\x61\x6d\x65\x74\x65\x72", "\x52\x6f\x62\x6f\x74\x6f", "\x6d\x65\x73\x73\x61\x67\x65", "\x6d\x65\x64\x69\x61\x44\x65\x76\x69\x63\x65\x73", "\x66\x69\x72\x73\x74\x4c\x6f\x61\x64", "\x3a", "\x64\x69\x73", "\x68\x6b\x75", "\x53\x68\x61\x72\x65\x50\x6f\x69\x6e\x74\x20\x42\x72\x6f\x77\x73\x65\x72\x20\x50\x6c\x75\x67\x2d\x69\x6e", "\x67\x72\x61\x6e\x74\x65\x64", "\x64\x6f\x6d\x41\x75\x74\x6f\x6d\x61\x74\x69\x6f\x6e\x43\x6f\x6e\x74\x72\x6f\x6c\x6c\x65\x72", "\x67\x77\x64", "\x6c\x61\x6e\x67", "\x5c\x5c\x22", "\x63\x72\x65\x64\x65\x6e\x74\x69\x61\x6c\x73", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x31\x38\x2c", "\x5f\x5f\x77\x65\x62\x64\x72\x69\x76\x65\x72\x5f\x73\x63\x72\x69\x70\x74\x5f\x66\x75\x6e\x63\x74\x69\x6f\x6e", "\x6f\x6e\x4c\x69\x6e\x65", "\x64\x6f\x6d\x41\x75\x74\x6f\x6d\x61\x74\x69\x6f\x6e", "\x6c\x6f\x61\x70", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x30\x39\x2c", "\x72\x69\x72", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x32\x32\x2c", "\x63\x61\x6c\x5f\x64\x69\x73", "\x63\x73", "\x68\x70\x75", "\x41\x6c\x4e\x69\x6c\x65", "\x74\x61\x72\x67\x65\x74", "\x6d\x6d\x65\x5f\x63\x6e\x74", "\x44\x65\x66\x61\x75\x6c\x74\x20\x42\x72\x6f\x77\x73\x65\x72\x20\x48\x65\x6c\x70\x65\x72", "\x63\x6d\x61", "\x47\x45\x54", "\x70\x6f\x69\x6e\x74\x65\x72\x54\x79\x70\x65", "\x4c\x75\x63\x69\x64\x61\x20\x53\x61\x6e\x73", "\x69\x50\x61\x64\x3b", "\x5f\x73\x65\x74\x42\x6d", "\x61\x6c\x74\x4b\x65\x79", "\x6d\x6e\x5f\x72\x74\x73", "\x67\x79\x72\x6f\x73\x63\x6f\x70\x65", "\x64\x65\x76\x69\x63\x65\x50\x69\x78\x65\x6c\x52\x61\x74\x69\x6f", "\x6d\x6e\x5f\x73\x74\x61\x74\x65", "\x67\x65\x74\x5f\x74\x79\x70\x65", "\x5c\x27", "\x6f\x6e", "\x73\x74\x6f\x72\x61\x67\x65", "\x72\x67\x62\x28\x31\x30\x32\x2c\x20\x32\x30\x34\x2c\x20\x30\x29", "\x72\x76\x65", "\x4e\x69\x6d\x62\x75\x73\x20\x52\x6f\x6d\x61\x6e\x20\x4e\x6f\x20\x39\x20\x4c", "\x70\x6f\x69\x6e\x74\x65\x72\x64\x6f\x77\x6e", "\x64\x69\x76", "\x63\x68\x61\x72\x41\x74", "\x63\x6c\x69\x70\x62\x6f\x61\x72\x64\x2d\x72\x65\x61\x64", "\x73\x71\x72\x74", "\x77\x61\x74\x69\x6e\x45\x78\x70\x72\x65\x73\x73\x69\x6f\x6e\x52\x65\x73\x75\x6c\x74", "\x72\x65\x6d\x6f\x76\x65\x43\x68\x69\x6c\x64", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x30\x31\x2c", "\x6d\x6f\x7a\x48\x69\x64\x64\x65\x6e", "\x44\x65\x76\x69\x63\x65\x4d\x6f\x74\x69\x6f\x6e\x45\x76\x65\x6e\x74", "\x6d\x6e\x5f\x74\x63\x6c", "\x76\x63\x61\x63\x74", "\x63\x68\x65\x63\x6b\x5f\x73\x74\x6f\x70\x5f\x70\x72\x6f\x74\x6f\x63\x6f\x6c", "\x31\x39\x32\x70\x78", "\x56\x65\x72\x73\x69\x6f\x6e\x2f\x34\x2e\x30", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x31\x31\x2c", "\x6d\x73\x76\x69\x73\x69\x62\x69\x6c\x69\x74\x79\x63\x68\x61\x6e\x67\x65", "\x5f\x5f\x77\x65\x62\x64\x72\x69\x76\x65\x72\x5f\x73\x63\x72\x69\x70\x74\x5f\x66\x75\x6e\x63", "\x64\x6f\x61\x63\x74", "\x67\x65\x74\x47\x61\x6d\x65\x70\x61\x64\x73", "\x54\x6f\x75\x63\x68\x45\x76\x65\x6e\x74", "\x74\x64", "\x6f\x6e\x6b\x65\x79\x75\x70", "\x61\x70\x70\x6c\x79\x46\x75\x6e\x63", "\x55\x52\x4c", "\x68\x6d\x75", "\x73\x61\x6e\x73\x2d\x73\x65\x72\x69\x66", "\x67\x65\x74\x45\x6c\x65\x6d\x65\x6e\x74\x73\x42\x79\x54\x61\x67\x4e\x61\x6d\x65", "\x73\x65\x6e\x64\x42\x65\x61\x63\x6f\x6e", "\x6d\x6f\x7a\x41\x6c\x61\x72\x6d\x73", "\x61\x63\x63\x65\x6c\x65\x72\x6f\x6d\x65\x74\x65\x72", "\x2c\x63\x70\x65\x6e\x3a", "\x64\x65\x6e\x69\x65\x64", "\x65\x6e\x47\x65\x74\x4c\x6f\x63", "\x41\x70\x70\x6c\x65\x20\x4c\x69\x47\x6f\x74\x68\x69\x63", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x31\x30\x2c", "\x74\x68\x65\x6e", "\x57\x61\x73\x65\x65\x6d", "\x74\x6f\x75\x63\x68\x65\x6e\x64", "\x73\x70\x61\x6e", "\x66\x69\x6c\x6c\x52\x65\x63\x74", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x32\x31\x2c", "\x22\x7d", "\x73\x70\x6c\x69\x63\x65", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x31\x36\x2c", "\x68\x61\x73\x49\x6e\x64\x65\x78\x65\x64\x44\x42", "\x77\x69\x74\x68\x43\x72\x65\x64\x65\x6e\x74\x69\x61\x6c\x73", "\x68\x63", "\x62\x61\x63\x6b\x67\x72\x6f\x75\x6e\x64\x2d\x73\x79\x6e\x63", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x37\x30\x2c", "\x6a\x72\x73", "\x73\x74\x79\x6c\x65", "\x41\x76\x65\x6e\x69\x72", "\x50\x49", "\x67\x65\x74\x66\x6f\x72\x6d\x69\x6e\x66\x6f", "\x74\x64\x75\x63\x65\x5f\x63\x6e\x74\x5f\x6c\x6d\x74", "\x65\x6e\x63\x6f\x64\x65", "\x77\x67\x6c", "\x6d\x6e\x5f\x61\x62\x63\x6b", "\x63\x64\x63\x5f\x61\x64\x6f\x51\x70\x6f\x61\x73\x6e\x66\x61\x37\x36\x70\x66\x63\x5a\x4c\x6d\x63\x66\x6c\x5f\x41\x72\x72\x61\x79", "\x6d\x6e\x5f\x67\x65\x74\x5f\x63\x75\x72\x72\x65\x6e\x74\x5f\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x73", "\x4e\x61\x74\x69\x76\x65\x20\x43\x6c\x69\x65\x6e\x74", "\x6c\x61\x73\x74\x49\x6e\x64\x65\x78\x4f\x66", "\x61\x77\x65\x73\x6f\x6d\x69\x75\x6d", "\x73\x68\x69\x66\x74\x4b\x65\x79", "\x43\x68\x72\x6f\x6d\x65\x20\x50\x44\x46\x20\x56\x69\x65\x77\x65\x72", "\x31", "\x6f\x64", "\x6f\x6e\x6b\x65\x79\x70\x72\x65\x73\x73", "\x4f\x70\x65\x6e\x20\x53\x61\x6e\x73", "\x63\x61\x6e\x76\x61\x73", "\x73\x75\x62\x73\x74\x72\x69\x6e\x67", "\x73\x74\x61\x72\x74\x64\x6f\x61\x64\x6d\x61", "\x2f\x2f", "\x6d\x6e\x5f\x63\x74", "\x68\x6e", "", "\x7a\x31", "\x70\x69", "\x68\x74\x73", "\x6f\x6e\x70\x6f\x69\x6e\x74\x65\x72\x64\x6f\x77\x6e", "\x6d\x6e\x5f\x6c\x63", "\x64\x65\x6e", "\x6d\x6e\x5f\x73\x65\x6e", "\x4e\x6f\x74\x6f", "\x5f\x53\x65\x6c\x65\x6e\x69\x75\x6d\x5f\x49\x44\x45\x5f\x52\x65\x63\x6f\x72\x64\x65\x72", "\x2c\x6d\x6e\x5f\x77\x3a", "\x5f\x73\x65\x74\x46\x73\x70", "\x73\x65\x73\x73\x69\x6f\x6e\x5f\x69\x64", "\x70\x61\x73\x73\x77\x6f\x72\x64", "\x75\x6e\x64\x65\x66\x69\x6e\x65\x64", "\x6b\x65\x5f\x63\x6e\x74\x5f\x6c\x6d\x74", "\x68\x6b\x64", "\x46\x61\x6e\x74\x61\x73\x71\x75\x65\x20\x53\x61\x6e\x73\x20\x4d\x6f\x6e\x6f", "\x6d\x6e\x5f\x70\x72", "\x70\x72\x6f\x74\x6f\x74\x79\x70\x65", "\x75\x61\x72", "\x62\x61\x74\x3a", "\x73\x63\x72\x69\x70\x74", "\x78\x31", "\x67\x65\x6f\x6c\x6f\x63\x61\x74\x69\x6f\x6e", "\x63\x64\x63\x5f\x61\x64\x6f\x51\x70\x6f\x61\x73\x6e\x66\x61\x37\x36\x70\x66\x63\x5a\x4c\x6d\x63\x66\x6c\x5f\x50\x72\x6f\x6d\x69\x73\x65", "\x73\x70\x65\x65\x63\x68\x53\x79\x6e\x74\x68\x65\x73\x69\x73", "\x67\x65\x74\x42\x61\x74\x74\x65\x72\x79", "\x63\x65\x5f\x6a\x73\x5f\x70\x6f\x73\x74", "\x6d\x6e\x5f\x74\x6f\x75\x74", "\x6d\x6d\x65\x5f\x63\x6e\x74\x5f\x6c\x6d\x74", "\x6d\x6e\x5f\x6d\x63\x5f\x69\x6e\x64\x78", "\x63\x6c\x69\x65\x6e\x74\x58", "\x7a", "\x75\x72\x6c", "\x5f\x61\x62\x63\x6b", "\x75\x70\x64\x61\x74\x65\x74", "\x43\x6f\x6e\x74\x65\x6e\x74\x2d\x74\x79\x70\x65", "\x64\x6d\x61\x63\x74", "\x73\x72\x63", "\x63\x77\x65\x6e\x3a", "\x70\x72\x6f\x64\x75\x63\x74\x53\x75\x62", "\x68\x6b\x70", "\x5f", "\x6b\x61\x63\x74", "\x7b\x22\x73\x65\x6e\x73\x6f\x72\x5f\x64\x61\x74\x61\x22\x3a\x22", "\x73\x64\x5f\x64\x65\x62\x75\x67", "\x4d\x69\x63\x72\x6f\x73\x6f\x66\x74\x20\x4f\x66\x66\x69\x63\x65\x20\x4c\x69\x76\x65\x20\x50\x6c\x75\x67\x2d\x69\x6e", "\x61\x6a\x5f\x69\x6e\x64\x78\x5f\x64\x6f\x61\x63\x74", "\x72\x65\x61\x64\x79\x53\x74\x61\x74\x65", "\x61\x76\x61\x69\x6c\x48\x65\x69\x67\x68\x74", "\x61\x63\x63\x65\x6c\x65\x72\x61\x74\x69\x6f\x6e", "\x68\x74\x74\x70\x3a\x2f\x2f", "\x70\x65\x5f\x63\x6e\x74", "\x46\x69\x6c\x65\x52\x65\x61\x64\x65\x72", "\x6c\x6f\x63", "\x61\x73\x69\x6e", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x31\x32\x2c", "\x61\x6a\x5f\x74\x79\x70\x65", "\x53\x6f\x75\x72\x63\x65\x20\x53\x61\x6e\x73\x20\x50\x72\x6f", "\x68\x62", "\x73\x6f\x72\x74", "\x76\x63", "\x2c\x73\x37\x3a", "\x73\x63\x3a", "\x74\x6f\x45\x6c\x65\x6d\x65\x6e\x74", "\x63\x6f\x6f\x6b\x69\x65\x45\x6e\x61\x62\x6c\x65\x64", "\x70\x61\x72\x73\x65", "\x39\x30\x70\x78", "\x73\x65\x72\x69\x66", "\x67\x65\x74\x43\x6f\x6e\x74\x65\x78\x74", "\x63\x61\x6c\x63\x5f\x66\x70", "\x57\x69\x64\x65\x76\x69\x6e\x65\x20\x43\x6f\x6e\x74\x65\x6e\x74\x20\x44\x65\x63\x72\x79\x70\x74\x69\x6f\x6e\x20\x4d\x6f\x64\x75\x6c\x65", "\x7e", "\x6d\x6e\x5f\x6c\x64", "\x69\x50\x68\x6f\x6e\x65", "\x41\x64\x6f\x62\x65\x20\x42\x72\x61\x69\x6c\x6c\x65", "\x64\x6f\x65\x5f\x76\x65\x6c", "\x67\x65\x62", "\x4e\x65\x77\x20\x59\x6f\x72\x6b", "\x70\x64\x75\x63\x65\x5f\x63\x6e\x74\x5f\x6c\x6d\x74", "\x73\x63\x72\x65\x65\x6e", "\x2c\x73\x65\x74\x53\x44\x46\x4e\x3a", "\x4f\x73\x77\x61\x6c\x64", "\x32\x64", "\x77\x6c", "\x69\x73\x63\x3a", "\x67\x61\x6d\x6d\x61", "\x72\x65\x67\x69\x73\x74\x65\x72\x50\x72\x6f\x74\x6f\x63\x6f\x6c\x48\x61\x6e\x64\x6c\x65\x72", "\x77\x72\x63\x3a", "\x61\x70\x70\x6c\x69\x63\x61\x74\x69\x6f\x6e\x2f\x6a\x73\x6f\x6e", "\x6d\x6e\x5f\x77\x74", "\x50\x4c\x55\x47\x49\x4e\x53", "\x6d\x73\x4d\x61\x6e\x69\x70\x75\x6c\x61\x74\x69\x6f\x6e\x56\x69\x65\x77\x73\x45\x6e\x61\x62\x6c\x65\x64", "\x73\x64\x66\x6e", "\x43\x65\x6e\x74\x75\x72\x79\x20\x47\x6f\x74\x68\x69\x63", "\x70\x61\x72\x61\x6d\x73\x5f\x75\x72\x6c", "\x67\x65\x74\x5f\x6d\x6e\x5f\x70\x61\x72\x61\x6d\x73\x5f\x66\x72\x6f\x6d\x5f\x61\x62\x63\x6b", "\x5f\x5f\x70\x68\x61\x6e\x74\x6f\x6d\x61\x73", "\x6d\x2c\x45\x76\x21\x78\x56\x36\x37\x42\x61\x55\x3e\x20\x65\x68\x32\x6d\x3c\x66\x33\x41\x47\x33\x40", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x32\x37\x2c", "\x69\x73\x54\x72\x75\x73\x74\x65\x64", "\x61\x6a\x5f\x73\x73", "\x53\x68\x72\x65\x65\x20\x44\x65\x76\x61\x6e\x61\x67\x61\x72\x69\x20\x37\x31\x34", "\x43\x6f\x6e\x73\x74\x72\x75\x63\x74\x6f\x72", "\x61\x6a\x5f\x69\x6e\x64\x78\x5f\x74\x61\x63\x74", "\x62\x64\x6d", "\x41\x64\x6f\x62\x65\x20\x41\x63\x72\x6f\x62\x61\x74", "\x6f\x6e\x62\x6c\x75\x72", "\x4f\x53\x4d\x4a\x49\x46", "\x69\x73\x20\x6e\x6f\x74\x20\x61\x20\x76\x61\x6c\x69\x64\x20\x65\x6e\x75\x6d\x20\x76\x61\x6c\x75\x65\x20\x6f\x66\x20\x74\x79\x70\x65\x20\x50\x65\x72\x6d\x69\x73\x73\x69\x6f\x6e\x4e\x61\x6d\x65", "\x76\x69\x62\x3a", "\x53\x69\x6c\x76\x65\x72\x6c\x69\x67\x68\x74\x20\x50\x6c\x75\x67\x2d\x49\x6e", "\x5f\x5f\x77\x65\x62\x64\x72\x69\x76\x65\x72\x46\x75\x6e\x63\x67\x65\x62", "\x3c\x2f\x73\x65\x74\x53\x44\x46\x4e\x3e", "\x73\x70\x61\x77\x6e", "\x70\x64", "\x63\x6c\x69\x65\x6e\x74\x48\x65\x69\x67\x68\x74", "\x77\x65\x68", "\x45\x64\x67\x65\x20\x50\x44\x46\x20\x56\x69\x65\x77\x65\x72", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x32\x34\x2c", "\x43\x6f\x75\x72\x69\x65\x72", "\x6d\x6e\x5f\x69\x6c", "\x64\x6d\x65\x5f\x76\x65\x6c", "\x4a\x61\x76\x61\x20\x41\x70\x70\x6c\x65\x74\x20\x50\x6c\x75\x67\x2d\x69\x6e", "\x63\x68\x6b\x6e\x75\x6c\x6c", "\x22", "\x6f\x39", "\x66\x6f\x72\x45\x61\x63\x68", "\x5f\x5f\x66\x78\x64\x72\x69\x76\x65\x72\x5f\x75\x6e\x77\x72\x61\x70\x70\x65\x64", "\x72\x65\x70\x6c\x61\x63\x65", "\x74\x5f\x65\x6e", "\x4d\x53\x49\x45", "\x72\x6f\x75\x6e\x64", "\x6b\x65\x79\x75\x70", "\x6e\x6f\x74\x69\x66\x69\x63\x61\x74\x69\x6f\x6e\x73", "\x6e\x61\x76\x5f\x70\x65\x72\x6d", "\x73\x65\x72\x76\x69\x63\x65\x57\x6f\x72\x6b\x65\x72", "\x2f\x5f\x62\x6d\x2f\x5f\x64\x61\x74\x61", "\x6c\x6f\x63\x61\x74\x69\x6f\x6e", "\x2c\x30", "\x73\x73\x68", "\x67\x65\x74\x56\x6f\x69\x63\x65\x73", "\x63\x6c\x69\x65\x6e\x74\x59", "\x6d\x6e\x5f\x73", "\x63\x61\x6d\x65\x72\x61", "\x43\x65\x6e\x74\x75\x72\x79", "\x65\x6e\x52\x65\x61\x64\x44\x6f\x63\x55\x72\x6c", "\x6f\x6e\x63\x6c\x69\x63\x6b", "\x50\x61\x70\x79\x72\x75\x73", "\x61\x6d\x62\x69\x65\x6e\x74\x2d\x6c\x69\x67\x68\x74\x2d\x73\x65\x6e\x73\x6f\x72", "\x72\x73\x74", "\x3b\x20", "\x6e\x75\x6d\x62\x65\x72", "\x63\x6e\x73", "\x3c\x62\x70\x64\x3e", "\x63\x74\x61", "\x61\x74\x74\x61\x63\x68\x45\x76\x65\x6e\x74", "\x5f\x5f\x77\x65\x62\x64\x72\x69\x76\x65\x72\x5f\x65\x76\x61\x6c\x75\x61\x74\x65", "\x75\x6e\x6b", "\x68\x74\x74\x70\x73\x3a", "\x57\x65\x62\x4b\x69\x74\x2d\x69\x6e\x74\x65\x67\x72\x69\x65\x72\x74\x65\x20\x50\x44\x46", "\x6f\x6e\x6b\x65\x79\x64\x6f\x77\x6e", "\x6d\x69\x64\x69", "\x6d\x6f\x7a\x50\x68\x6f\x6e\x65\x4e\x75\x6d\x62\x65\x72\x53\x65\x72\x76\x69\x63\x65", "\x6d\x6e\x5f\x75\x70\x64\x61\x74\x65\x5f\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x5f\x64\x65\x74\x61\x69\x6c\x73", "\x66\x75\x6e\x63\x74\x69\x6f\x6e", "\x66\x6d", "\x67\x65\x74\x45\x78\x74\x65\x6e\x73\x69\x6f\x6e", "\x6d\x6f\x7a\x43\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e", "\x61\x72\x63", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x30\x33\x2c", "\x41\x64\x6f\x62\x65\x41\x41\x4d\x44\x65\x74\x65\x63\x74", "\x42\x69\x72\x63\x68\x20\x53\x74\x64", "\x42\x6f\x64\x6f\x6e\x69\x20\x37\x32", "\x73\x68\x69\x66\x74", "\x6d\x65\x74\x61\x4b\x65\x79", "\x76\x65\x72", "\x43\x61\x6e\x74\x61\x72\x65\x6c\x6c", "\x6d\x6f\x75\x73\x65\x6d\x6f\x76\x65", "\x74\x65\x5f\x63\x6e\x74", "\x74\x65\x5f\x76\x65\x6c", "\x64\x65\x76\x69\x63\x65\x6d\x6f\x74\x69\x6f\x6e", "\x55\x4e\x4d\x41\x53\x4b\x45\x44\x5f\x52\x45\x4e\x44\x45\x52\x45\x52\x5f\x57\x45\x42\x47\x4c", "\x63\x70\x61", "\x70\x72\x6f\x64\x75\x63\x74", "\x5f\x5f\x64\x72\x69\x76\x65\x72\x5f\x75\x6e\x77\x72\x61\x70\x70\x65\x64", "\x6d\x6e\x5f\x6c\x67", "\x6d\x6f\x7a\x52\x54\x43\x50\x65\x65\x72\x43\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e", "\x4d\x6f\x6e\x6f\x73\x70\x61\x63\x65", "\x6a\x61\x76\x61\x45\x6e\x61\x62\x6c\x65\x64", "\x43\x61\x6e\x64\x61\x72\x61", "\x66\x69\x6c\x6c\x53\x74\x79\x6c\x65", "\x6c\x6f\x63\x61\x6c\x53\x74\x6f\x72\x61\x67\x65", "\x64\x32", "\x6d\x6e\x5f\x74\x73", "\x66\x6d\x7a", "\x6d\x6e\x5f\x61\x6c", "\x64\x65\x76\x69\x63\x65\x6f\x72\x69\x65\x6e\x74\x61\x74\x69\x6f\x6e", "\x50\x61\x6c\x61\x74\x69\x6e\x6f\x2d\x42\x6f\x6c\x64", "\x52\x65\x61\x6c\x50\x6c\x61\x79\x65\x72\x20\x56\x65\x72\x73\x69\x6f\x6e\x20\x50\x6c\x75\x67\x69\x6e", "\x70\x61\x72\x73\x65\x5f\x67\x70", "\x77\x65\x62\x6b\x69\x74\x52\x54\x43\x50\x65\x65\x72\x43\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e", "\x73\x65\x6c\x65\x6e\x69\x75\x6d", "\x68\x61\x72\x64\x77\x61\x72\x65\x43\x6f\x6e\x63\x75\x72\x72\x65\x6e\x63\x79", "\x4d\x6f\x7a\x69\x6c\x6c\x61\x20\x44\x65\x66\x61\x75\x6c\x74\x20\x50\x6c\x75\x67\x2d\x69\x6e", "\x48\x54\x4d\x4c\x45\x6c\x65\x6d\x65\x6e\x74", "\x6e", "\x50\x61\x6c\x61\x74\x69\x6e\x6f", "\x6a\x73\x5f\x70\x6f\x73\x74", "\x66\x69\x64\x63\x6e\x74", "\x6d\x65\x5f\x63\x6e\x74", "\x77\x68\x69\x63\x68", "\x61\x63\x6f\x73", "\x6d\x6f\x75\x73\x65\x64\x6f\x77\x6e", "\x67\x65\x74\x53\x74\x61\x74\x65\x46\x69\x65\x6c\x64", "\x49\x54\x43\x20\x42\x6f\x64\x6f\x6e\x69\x20\x37\x32\x20\x42\x6f\x6c\x64", "\x6f\x6e\x6d\x6f\x75\x73\x65\x6d\x6f\x76\x65", "\x77\x65\x62\x73\x74\x6f\x72\x65", "\x6f\x6e\x6d\x6f\x75\x73\x65\x75\x70", "\x55\x4e\x4d\x41\x53\x4b\x45\x44\x5f\x56\x45\x4e\x44\x4f\x52\x5f\x57\x45\x42\x47\x4c", "\x68\x66", "\x5f\x5f\x6c\x61\x73\x74\x57\x61\x74\x69\x72\x50\x72\x6f\x6d\x70\x74", "\x70\x72\x6f\x6d\x70\x74", "\x6d\x61\x70", "\x65\x6d\x61\x69\x6c", "\x72\x75\x6e\x46\x6f\x6e\x74\x73", "\x69\x6e\x6e\x65\x72\x57\x69\x64\x74\x68", "\x72\x65\x71\x75\x65\x73\x74\x57\x61\x6b\x65\x4c\x6f\x63\x6b", "\x36\x70\x74\x20\x41\x72\x69\x61\x6c", "\x43\x61\x6c\x69\x62\x72\x69", "\x61\x6a\x5f\x6c\x6d\x74\x5f\x64\x6d\x61\x63\x74", "\x63\x61\x6c\x6c\x65\x64\x53\x65\x6c\x65\x6e\x69\x75\x6d", "\x6e\x6f\x6e\x65", "\x6d\x6e\x5f\x72\x74", "\x6d\x6f\x75\x73\x65", "\x66\x61\x73", "\x3c\x40\x6e\x76\x34\x35\x2e\x20\x46\x31\x6e\x36\x33\x72\x2c\x50\x72\x31\x6e\x37\x31\x6e\x36\x21", "\x68\x74\x74\x70\x73\x3a\x2f\x2f", "\x77\x76", "\x72\x56\x61\x6c", "\x6f\x66\x66\x73\x65\x74\x48\x65\x69\x67\x68\x74", "\x69\x6e\x6e\x65\x72\x48\x54\x4d\x4c", "\x64\x33", "\x41\x76\x65\x6e\x69\x72\x20\x4e\x65\x78\x74", "\x44\x61\x6d\x61\x73\x63\x75\x73", "\x61\x6a\x5f\x69\x6e\x64\x78\x5f\x64\x6d\x61\x63\x74", "\x70\x73\x75\x62", "\x70\x6d\x65\x5f\x63\x6e\x74\x5f\x6c\x6d\x74", "\x62\x63", "\x54\x49\x2d\x4e\x73\x70\x69\x72\x65", "\x61\x6a\x5f\x6c\x6d\x74\x5f\x64\x6f\x61\x63\x74", "\x3b", "\x53\x68\x6f\x63\x6b\x77\x61\x76\x65\x20\x66\x6f\x72\x20\x44\x69\x72\x65\x63\x74\x6f\x72", "\x61\x74\x61\x6e\x68", "\x70\x72\x65\x76\x66\x69\x64", "\x55\x62\x75\x6e\x74\x75\x20\x4d\x65\x64\x69\x75\x6d", "\x63\x63", "\x68\x74\x65", "\x65\x6e\x41\x64\x64\x48\x69\x64\x64\x65\x6e", "\x77\x65\x62\x6b\x69\x74\x54\x65\x6d\x70\x6f\x72\x61\x72\x79\x53\x74\x6f\x72\x61\x67\x65", "\x67\x62\x72\x76", "\x76\x61\x6c\x75\x65", "\x70\x6f\x69\x6e\x74\x65\x72\x75\x70", "\x63\x61\x6c\x6c\x65\x64\x50\x68\x61\x6e\x74\x6f\x6d", "\x63\x68\x72\x6f\x6d\x65", "\x68\x65\x69\x67\x68\x74", "\x63\x61\x6c\x6c", "\x6f\x70\x63\x3a", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x32\x33\x2c", "\x51\x75\x69\x63\x6b\x73\x61\x6e\x64", "\x68\x61\x73\x4c\x6f\x63\x61\x6c\x53\x74\x6f\x72\x61\x67\x65", "\x74\x6d\x65\x5f\x63\x6e\x74\x5f\x6c\x6d\x74", "\x43\x6f\x6d\x69\x63\x20\x4e\x65\x75\x65", "\x5f\x5f\x73\x65\x6c\x65\x6e\x69\x75\x6d\x5f\x75\x6e\x77\x72\x61\x70\x70\x65\x64", "\x73\x74\x61\x63\x6b", "\x63\x66\x5f\x75\x72\x6c", "\x3c\x73\x65\x74\x53\x44\x46\x4e\x3e", "\x61\x62", "\x62\x6d", "\x5f\x5f\x77\x65\x62\x64\x72\x69\x76\x65\x72\x5f\x5f\x63\x68\x72", "\x64\x6d\x65\x5f\x63\x6e\x74", "\x74\x61\x63\x74", "\x63\x74\x72\x6c\x4b\x65\x79", "\x61\x74\x73", "\x47\x6f\x6f\x67\x6c\x65\x20\x54\x61\x6c\x6b\x20\x50\x6c\x75\x67\x69\x6e\x20\x56\x69\x64\x65\x6f\x20\x52\x65\x6e\x64\x65\x72\x65\x72", "\x78\x31\x32\x3a", "\x63\x61\x6c\x6c\x50\x68\x61\x6e\x74\x6f\x6d", "\x53\x65\x72\x69\x66", "\x69\x50\x68\x6f\x74\x6f\x50\x68\x6f\x74\x6f\x63\x61\x73\x74", "\x74\x65\x6c", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x30\x30\x2c", "\x44\x72\x6f\x69\x64\x20\x53\x65\x72\x69\x66", "\x66\x6d\x67\x65\x74\x5f\x74\x61\x72\x67\x65\x74\x73", "\x61\x75\x74\x6f\x63\x6f\x6d\x70\x6c\x65\x74\x65", "\x77\x61\x74\x69\x6e\x45\x78\x70\x72\x65\x73\x73\x69\x6f\x6e\x45\x72\x72\x6f\x72", "\x64\x69\x73\x70\x6c\x61\x79", "\x69\x6e\x73", "\x48\x65\x6c\x76\x65\x74\x69\x63\x61\x20\x4e\x65\x75\x65", "\x74\x6f\x53\x74\x72\x69\x6e\x67", "\x70\x61\x67\x65\x59", "\x70\x72\x6f\x64", "\x64\x6d\x3a", "\x6f\x6e\x6c\x6f\x61\x64", "\x64\x6f\x63\x75\x6d\x65\x6e\x74\x4d\x6f\x64\x65", "\x78\x31\x31\x3a", "\x70\x6d\x65\x5f\x63\x6e\x74", "\x52\x54\x43\x50\x65\x65\x72\x43\x6f\x6e\x6e\x65\x63\x74\x69\x6f\x6e", "\x67\x65\x74\x45\x6c\x65\x6d\x65\x6e\x74\x42\x79\x49\x64", "\x62\x72\x76", "\x73\x70\x79\x6e\x6e\x65\x72\x5f\x61\x64\x64\x69\x74\x69\x6f\x6e\x61\x6c\x5f\x6a\x73\x5f\x6c\x6f\x61\x64\x65\x64", "\x7d", "\x6e\x61\x6d\x65", "\x68\x61\x73\x53\x65\x73\x73\x69\x6f\x6e\x53\x74\x6f\x72\x61\x67\x65", "\x62\x65\x74\x61", "\x70\x73\x74\x61\x74\x65", "\x65\x78\x70", "\x58\x44\x6f\x6d\x61\x69\x6e\x52\x65\x71\x75\x65\x73\x74", "\x69\x6e\x64\x65\x78\x65\x64\x44\x42", "\x61\x63\x74\x69\x76\x65\x45\x6c\x65\x6d\x65\x6e\x74", "\x55\x6e\x69\x74\x79\x20\x50\x6c\x61\x79\x65\x72", "\x53\x68\x6f\x63\x6b\x77\x61\x76\x65\x20\x46\x6c\x61\x73\x68", "\x63\x75\x72\x72\x65\x6e\x74\x53\x63\x72\x69\x70\x74", "\x43\x61\x6d\x62\x72\x69\x61", "\x6d\x65\x5f\x76\x65\x6c", "\x66\x70\x56\x61\x6c\x43\x61\x6c\x63\x75\x6c\x61\x74\x65\x64", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x31\x37\x2c", "\x62\x72\x61\x76\x65", "\x65\x6e\x63\x6f\x64\x65\x5f\x75\x74\x66\x38", "\x73\x65\x6e\x73\x6f\x72\x5f\x64\x61\x74\x61", "\x73\x74\x61\x74\x65", "\x51\x75\x69\x63\x6b\x54\x69\x6d\x65\x20\x50\x6c\x75\x67\x2d\x69\x6e", "\x64\x63\x73", "\x6e\x70", "\x70\x69\x78\x65\x6c\x44\x65\x70\x74\x68", "\x62", "\x64\x6f\x5f\x65\x6e", "\x70\x6c\x65\x6e", "\x75\x73\x65\x72\x41\x67\x65\x6e\x74", "\x6f\x70\x65\x6e", "\x6f\x75\x74\x65\x72\x57\x69\x64\x74\x68", "\x61\x6c\x74\x46\x6f\x6e\x74\x73", "\x63\x68\x69\x6c\x64\x4e\x6f\x64\x65\x73", "\x64\x6d\x5f\x65\x6e", "\x50\x6f\x69\x6e\x74\x65\x72\x45\x76\x65\x6e\x74", "\x67\x65\x74\x46\x6c\x6f\x61\x74\x56\x61\x6c", "\x55\x62\x75\x6e\x74\x75\x20\x52\x65\x67\x75\x6c\x61\x72", "\x42\x65\x6c\x6c\x20\x4d\x54", "\x63\x6f\x6f\x6b\x69\x65\x5f\x63\x68\x6b\x5f\x72\x65\x61\x64", "\x68\x62\x43\x61\x6c\x63", "\x73\x74\x72\x69\x6e\x67", "\x47\x69\x6c\x6c\x20\x53\x61\x6e\x73\x20\x4d\x54", "\x74\x73\x74", "\x64\x65\x76\x69\x63\x65\x2d\x69\x6e\x66\x6f", "\x6d\x6e\x5f\x6c\x63\x6c", "\x61\x70\x70\x65\x6e\x64\x43\x68\x69\x6c\x64", "\x66\x6c\x6f\x6f\x72", "\x74\x79\x70\x65", "\x63\x62\x72\x74", "\x54\x69\x6d\x65\x73", "\x52\x65\x61\x6c\x50\x6c\x61\x79\x65\x72\x28\x74\x6d\x29\x20\x47\x32\x20\x4c\x69\x76\x65\x43\x6f\x6e\x6e\x65\x63\x74\x2d\x45\x6e\x61\x62\x6c\x65\x64\x20\x50\x6c\x75\x67\x2d\x49\x6e\x20\x28\x33\x32\x2d\x62\x69\x74\x29", "\x6d\x6d\x6d\x6d\x6d\x6d\x6d\x6d\x6c\x6c\x69", "\x79", "\x5f\x5f\x77\x65\x62\x64\x72\x69\x76\x65\x72\x5f\x73\x63\x72\x69\x70\x74\x5f\x66\x6e", "\x63\x61\x63\x68\x65", "\x62\x6d\x2d\x74\x65\x6c\x65\x6d\x65\x74\x72\x79", "\x6d\x6f\x75\x73\x65\x75\x70", "\x67\x65\x74\x45\x6c\x65\x6d\x65\x6e\x74\x73\x42\x79\x4e\x61\x6d\x65", "\x59\x6f\x75\x54\x75\x62\x65\x20\x50\x6c\x75\x67\x2d\x69\x6e", "\x67\x65\x74\x54\x69\x6d\x65\x7a\x6f\x6e\x65\x4f\x66\x66\x73\x65\x74", "\x64\x72\x69\x76\x65\x72", "\x6d\x6f\x7a\x76\x69\x73\x69\x62\x69\x6c\x69\x74\x79\x63\x68\x61\x6e\x67\x65", "\x6f\x6e\x70\x6f\x69\x6e\x74\x65\x72\x75\x70", "\x5f\x5f\x73\x65\x6c\x65\x6e\x69\x75\x6d\x5f\x65\x76\x61\x6c\x75\x61\x74\x65", "\x2c\x75\x61\x65\x6e\x64\x2c", "\x69\x73\x42\x72\x61\x76\x65", "\x3c\x69\x6e\x69\x74\x2f\x3e", "\x76\x6f\x69\x63\x65\x55\x52\x49", "\x3d", "\x2f", "\x66\x73\x70", "\x6b\x65\x79\x70\x72\x65\x73\x73", "\x70\x65\x72\x6d\x69\x73\x73\x69\x6f\x6e\x73", "\x67\x65\x74\x6d\x72", "\x67\x65\x74\x64\x75\x72\x6c", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x30\x32\x2c", "\x61\x70\x70\x4d\x69\x6e\x6f\x72\x56\x65\x72\x73\x69\x6f\x6e", "\x77\x65\x62\x6b\x69\x74\x48\x69\x64\x64\x65\x6e", "\x63\x68\x61\x72\x43\x6f\x64\x65\x41\x74", "\x6d\x6e\x5f\x70\x73\x6e", "\x74\x64\x75\x63\x65\x5f\x63\x6e\x74", "\x63\x68\x61\x72\x43\x6f\x64\x65", "\x64\x6f\x61\x64\x6d\x61\x5f\x65\x6e", "\x6d\x6f\x6e\x6f\x73\x70\x61\x63\x65", "\x6d\x6e\x5f\x69\x6e\x69\x74", "\x64\x65\x66\x61\x75\x6c\x74", "\x61\x65\x69\x6f\x75\x79\x31\x33\x35\x37\x39", "\x62\x69\x6e\x64", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x31\x34\x2c", "\x77\x65\x6e", "\x74\x65\x78\x74", "\x22\x2c\x22\x73\x65\x6e\x73\x6f\x72\x5f\x64\x61\x74\x61\x22\x20\x3a\x20\x22", "\x65\x76\x65\x6e\x74", "\x61\x70\x70\x56\x65\x72\x73\x69\x6f\x6e", "\x78", "\x41\x64\x6f\x62\x65\x20\x48\x65\x62\x72\x65\x77", "\x2d\x31\x2c\x32\x2c\x2d\x39\x34\x2c\x2d\x31\x31\x35\x2c", "\x6f\x6e\x6d\x6f\x75\x73\x65\x64\x6f\x77\x6e", "\x64\x6f\x65\x5f\x63\x6e\x74\x5f\x6c\x6d\x74", "\x5f\x5f\x6e\x69\x67\x68\x74\x6d\x61\x72\x65", "\x6c\x65\x6e\x67\x74\x68", "\x74\x6f\x75\x63\x68\x6d\x6f\x76\x65", "\x4d\x69\x63\x72\x6f\x73\x6f\x66\x74\x2e\x58\x4d\x4c\x48\x54\x54\x50", "\x7c\x7c", "\x47\x6f\x6f\x67\x6c\x65\x20\x45\x61\x72\x74\x68\x20\x50\x6c\x75\x67\x2d\x69\x6e", "\x4d\x69\x6e\x69\x6f\x6e\x20\x50\x72\x6f", "\x66\x72\x6f\x6d\x43\x68\x61\x72\x43\x6f\x64\x65", "\x66\x63\x3a", "\x67\x65\x74\x53\x75\x70\x70\x6f\x72\x74\x65\x64\x45\x78\x74\x65\x6e\x73\x69\x6f\x6e\x73", "\x62\x6c\x75\x65\x74\x6f\x6f\x74\x68", "\x6b\x65\x5f\x63\x6e\x74", "\x3c\x2f\x62\x70\x64\x3e"];

    function decode() {
        var element = document.getElementById('code');
        console.log(_0xf488.length);
        for (var key in _0xf488) {
            element.value += _0xf488[key] + "\n";
        }
    }
</script>
<textarea id="code" cols="80" rows="20"></textarea>
<input type="button" onclick="decode()" value="解码">
</body>
</html>

```

源码解析后：

```

// var document = {'location': {'href': 'about:blank', 'origin': 'null', 'protocol': 'about:', 'host': '', 'hostname': '', 'port': '', 'pathname': 'blank', 'search': '', 'hash': ''}};

var _ac =['clientX', '==', 'keyCode', 'onclick', '-1,2,-94,-115,', 'input', 'pme_cnt_lmt', 'appMinorVersion', 'imul', 'kact', 'mme_cnt', 'pd', 'indexedDbKey', 'mediaDevices', 'plugins', 'aj_indx', 'dme_cnt_lmt', 'Open Sans', 'number', 'get_browser', 'Windows Media Player Plug-in Dynamic Link Library', 't_tst', 'Monaco', 'PointerEvent', 'click', 'sd_debug', '-1,2,-94,-106,', 'clientY', 'informinfo', 'cbrt', 'getContext', 'sendBeacon', 'ceil', ',c-', 'encode_utf8', 'vc', '/', 'fonts_optm', 'chknull', 'screen', '-1,2,-94,-117,', ',s3:', '$cdc_asdjflasutopfhvcZLmcfl_', 'type', 'removeChild', 'Courier New', '-1,2,-94,-103,', 'd2', 'domAutomation', 'getFloatVal', 'AdobeAAMDetect', 'iPhotoPhotocast', 'aj_indx_tact', 'strokeStyle', '-1,2,-94,-112,', '"', 'sf4', 'storeWebWideTrackingException', 'Constructor', 'mr', 'Papyrus', 'ins', '16pt Arial', 'Bell MT', 'sqrt', 'shift', 'get_cookie', 'Lobster', 'appVersion', 'userAgent', 'webrtcKey', 'indexedDB', ',s6:', 'Apple Gothic', 'XMLHttpRequest', 'rCFP', 'gb', 'string', 'offsetWidth', 'rgb(102, 204, 0)', 'z1', 'onfocus', 'pe_cnt', 'pointerdown', 'fillText', 'keypress', 'Minion Pro', 'toElement', 'api_public_key', 'gf', 'target', 'webstore', 'Authorization', 'mousedown', 'Oswald', 'Google Earth Plug-in', 'hardwareConcurrency', 'hku', 'cookie_chk_read', 'xagg', 'doact', 'home.html', 'replace', 'x12:', 'email', 'ff', 'Fantasque Sans Mono', 'cookieEnabled', '-1,2,-94,-70,', 'mouse', 'a', 'id', 'localStorage', 'mn_r', 'availHeight', ',loc:', 'doe_cnt', 'onkeypress', 'apicall_bm', 'outerWidth', '3', 'onmouseup', 'setRequestHeader', 'rVal', 'metaKey', 'onblur', 'webkitHidden', 'hvc', 'pi', 'onLine', 'getmr', 'onkeyup', 'cssText', 'charCode', 'mn_tcl', 'fpVal', 'div', 'bat:', 'Noto', '\\"', 'z', 'pow', 'aj_lmt_dmact', 'doadma_en', 'default', 'parse', '-', 'set_cookie', 'updatet', 'Microsoft.XMLHTTP', '; ', 'stroke', 'wen', 'cpa', 'loc', 'getBattery', 'getElementsByTagName', 'Droid Serif', 'init_time', 'hts', 'ce_js_post', 'bdm', 'doe_cnt_lmt', 'Century Gothic', 'bd', 'substring', 'tst', '-1,2,-94,-123,', 'mn_stout', 'ArialHebrew-Light', 'height', 'ke_cnt', 'get_stop_signals', 'SharePoint Browser Plug-in', 'withCredentials', 'Comic Neue', 'apply', 'startdoadma', 'serviceWorker', 'mn_abck', 'uar', 'lastIndexOf', 'hc', ',', 'unk', 'webkitGetGamepads', 'onpointerup', 'doe_vel', 'encode', 'tel', 'PI', 'sans-serif', 'aj_type', '-1,2,-94,-101,', 'opera', 'default_session', 'credentials', 'check_stop_protocol', 'plen', 'sessionStorage', 'XPathResult', 'XDomainRequest', '0', ':', 'slice', 'isTrusted', 'Buffer', 'mme_cnt_lmt', 'asin', 'Chrome Remote Desktop Viewer', 'te_vel', 'pixelDepth', 'mn_poll', ',a-', 'Google Talk Plugin Video Renderer', 'aj_lmt_tact', 'cma', 'webkitTemporaryStorage', '=', 'getdurl', 'mn_il', 'button', '<cfsubmit/>', ',setSDFN:', 'call', 'deviceorientation', 'fsp', 'sdfn', 'Futura', 'Palatino', 'hpu', '","sensor_data" : "', '-1,2,-94,-100,', '-1,2,-94,-110,', '-1,2,-94,-121,', '-1,2,-94,-118,', 'non:', 'mozRTCPeerConnection', 'cs', 'mn_w', 'storage', 'https:', '-1,2,-94,-116,', 'getGamepads', 'beta', 'pme_cnt', '-1,2,-94,-109,', 'now', 'Apple LiGothic', 'innerHTML', 'enAddHidden', '~', 'Helvetica Neue', 'onmousemove', 'me_vel', 'opc:', 'pd_en', 'span', '0a46G5m17Vrp4o4c', ',uaend,', 'webdriver', 'parseInt', 'y1', 'value', '<@nv45\. F1n63r,Pr1n71n6!', 'forEach', 'fpcf', 'mn_mc_lmt', '#f60', 'altKey', 'Chrome PDF Viewer', 'auth', 'https://', 'monospace', 'vc_cnt_lmt', 'cka', ',mn_w:', '{"session_id" : "', 'timezoneOffsetKey', 'Avenir Next', 'ke_vel', 'width', 'RealPlayer(tm) G2 LiveConnect-Enabled Plug-In (32-bit)', 'get_mn_params_from_abck', '1', '', 'PLUGINS', 'afSbep8yjnZUjq3aL010jO15Sawj2VZfdYK8uY90uxq', 'hb', 'availWidth', 'sensor_data', 'd3', 'x11:', 'send', 'pageX', 'Ubuntu Regular', 'mozvisibilitychange', 'cns', 'keydown', 'hte', 'Lato', 'documentMode', 'attachEvent', 'apid.cformanalytics.com/api/v1/attempt', 'autocomplete', 'ir', 'Java Plug-in 2 for NPAPI Browsers', 'text', 'msHidden', 'htm', 'Batang', 'documentElement', 'fontSize', 'New York', 'Mac OS X 10_5', 'Microsoft Sans Serif', '{"sensor_data":"', 'default_abck', 'lvc', 'clearCache', 'mouseup', 'DeviceMotionEvent', 'Microsoft Office Live Plug-in', 'mn_tout', 'ctrlKey', 'Java Applet Plug-in', 'canvas', 'do_dis', 'hidden', 'mozAlarms', 't_en', 'wrc:', 'push', 'Century', ',s4', 'dm_dis', 'Courier', 'getTimezoneOffset', 'TI-Nspire', 'none', '90px', '-1,2,-94,-105,', 'mn_al', 'mn_h', 'position: relative; left: -9999px; visibility: hidden; display: block !important', 'random', 'hn', 'touchmove', 'fonts', 'toFixed', 'js_post', 'enReadDocUrl', 'style', 'mn_lg', 'hpd', 'do_en', 'Adobe Braille', 'fas', 'mn_sen', 'cdoa', '-1,2,-94,-111,', 'return ', 'bind', 'Edge PDF Viewer', 'gck', 'body', 'vcact', 'dme_vel', 'sed', 'getStorageUpdates', 'rir', 'touchstart', 'rgb(120, 186, 176)', 'abcdefhijklmnopqrstuvxyz1234567890;+-.', "'", 'return a', 'rst', 'session_id', 'mozInnerScreenY', ',0', 'doNotTrack', 'bluetooth', '-1,2,-94,-108,', 'get_type', 'toLowerCase', 'aj_lmt_doact', 'gamma', 'exp', 'sort', 'toString', '-1,2,-94,-102,', 'fc:', 'runFonts', 'charAt', 'activeElement', 't_dis', 'document', 'off', 'undef', '-1,2,-94,-120,', 'Silverlight Plug-In', 'mn_init', 'dme_cnt', 'vc_cnt', 'round', 'rve', 'application/json', 'tme_cnt', 'defaultValue', 'msvisibilitychange', 'mn_pr', 'hf', 'hasSessionStorage', 'x1', 'cta', 'dma_throttle', 'iPad;', 'Shockwave Flash', 'vibrate', 'ta', 'mn_get_challenge', 'cf_url', 'fillStyle', 'dm_en', 'http://', 'data', 'getElementById', '-1', 'url', 'mduce_cnt', 'clientWidth', 'pointerup', 'MSIE', 'onreadystatechange', 'offsetHeight', 'fillRect', 'onmousedown', '-1,2,-94,-80,', 'Native Client', 'on', 'URL', 'Widevine Content Decryption Module', 'search', '-1,2,-94,-119,', ',s2:', 'open', 'tact', 'hasIndexedDB', 'split', 'aj_indx_doact', 'function', 'Basic ', 'undefined', '_', 'javaEnabled', 'forminfo', 'POST', 'pduce_cnt_lmt', 'getAttribute', 'readyState', 'webkitRTCPeerConnection', 'ver', '; path=/; expires=Fri, 01 Feb 2025 08:00:00 GMT;', 'dis', 'cc', 'childNodes', 'hkp', 'YouTube Plug-in', 'arc', 'indexOf', 'Cantarell', 'innerWidth', 'keyup', 'rotationRate', 'tme_cnt_lmt', 'pen', 'start_ts', 'callPhantom', 'bmisc', 'length', 'me_cnt', 'Times', 'fromCharCode', 'psub', 'Cambria', 'onload', 'gd', 'display', ',s7:', 'apicall', 'acos', 'isIgn', 'pe_vel', 'pduce_cnt', 'innerHeight', 'doa_throttle', 'listFunctions', 'colorDepth', 'abs', ',s1:', ',d', 'bm', 'bc', '_phantom', 'Mozilla Default Plug-in', 'dm:', 'o9', 'cache', 'Shockwave for Director', '6pt Arial', 'floor', 'mn_mc_indx', 'toDataURL', 'Adobe Acrobat', 'location', '2d', 'charCodeAt', 'hostname', 'password', 'visibilitychange', 'mact', 'bpd', '}', 'Geneva', 'fidcnt', 'selenium', 'sessionStorageKey', 'required', 'Avenir', 'fpValCalculated', 'chrome', 'hasLocalStorage', 'webkitvisibilitychange', 'lang', '"}', '<init/>', 'cwen:', 'DeviceOrientationEvent', 'mozHidden', 'mozIsLocallyAvailable', 'disFpCalOnTimeout', 'Default Browser Helper', 'htc', 'exception', 'requestWakeLock', 'Damascus', '</setSDFN>', 'applyFunc', ',"auth" : "', '<setSDFN>', 'x', ',c-null', 'driver', '_abck', 'FileReader', 'shiftKey', 'tduce_cnt_lmt', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/', 'WebEx64 General Plugin Container', 'pointerType', 'atanh', 'RealPlayer Version Plugin', 'clientHeight', 'localStorageKey', 'serif', 'mn_psn', 'emit', 'acceleration', 'Palatino-Bold', '<bpd>', 'startTracking', 'Adobe Hebrew', 'productSub', 'td', '</bpd>', 'Birch Std', ';', 'TouchEvent', 'Ubuntu Medium', 'fpValstr', 'isc:', 'Quicksand', 'vib:', ',s5', 'mozConnection', 'Content-type', 'pact', 'addEventListener', 'Corsiva Hebrew', 'requestMediaKeySystemAccess', 'msManipulationViewsEnabled', ',cpen:', 'aj_indx_dmact', 'mn_ts', 'protocol', '//', 'hypot', 'prototype', 'appendChild', 'ab', 'x2', 'touchend', 'tduce_cnt', 'mn_check_if_new_challenge', 'Version/4.0', 'name', 'QuickTime Plug-in', 'hmd', 'patp', 'onpointerdown', 'onkeydown', 'mozPhoneNumberService', 'Unity Player', 'prevfid', 'prod', 'dmact', 'accelerationIncludingGravity', 'iPhone', 'font', 'den', 'touchcancel', 'product', 'thr', 'mousemove', 'ckie', 'HTMLElement', 'RTCPeerConnection', 'sc:', 'y', '/_bm/_data', 'ke_cnt_lmt', 'AlNile', 'registerProtocolHandler', 'pageY', 'mn_ld', 'alpha', 'hmu', '-1,2,-94,-122,', 'aj_ss', 'mn_cd', 'fontFamily', 'od', 'rotate_left', 'mn_cc', 'te_cnt', 'mn_state', 'permissions', 'Source Sans Pro', 'spawn', 'hmm', 'n_ck', 'Calibri', 'cookie', 'join', 'to', 'language', 'get_cf_date', 'WebKit-integrierte PDF', 'devicemotion', 'Roboto', 'event', 'mduce_cnt_lmt', 'hkd', '-1,2,-94,-114,', '2', 'i1:', ',b', 'createElement', 'cdma', 'altFonts', 'return/*@cc_on!@*/!1', 'which', 'pluginInfo', 'enGetLoc', 'navigator', 'mn_lc'];
var _cf = _cf || [],
    bmak = {
        ver: 1.41,
        ke_cnt_lmt: 150,
        mme_cnt_lmt: 100,
        mduce_cnt_lmt: 75,
        pme_cnt_lmt: 25,
        pduce_cnt_lmt: 25,
        tme_cnt_lmt: 25,
        tduce_cnt_lmt: 25,
        doe_cnt_lmt: 10,
        dme_cnt_lmt: 10,
        vc_cnt_lmt: 100,
        doa_throttle: 0,
        dma_throttle: 0,
        session_id: 'default_session',
        js_post: !1,
        loc: '',
        cf_url: ('https:' === "https:" ? 'https://' : 'http://') + 'apid.cformanalytics.com/api/v1/attempt',
        auth: '',
        api_public_key: null,
        aj_lmt_doact: 1,
        aj_lmt_dmact: 1,
        aj_lmt_tact: 1,
        ce_js_post: 0,
        init_time: 0,
        informinfo: '',
        prevfid: -1,
        fidcnt: 0,
        sensor_data: 0,
        ins: null,
        cns: null,
        enGetLoc: 0,
        enReadDocUrl: 0,
        disFpCalOnTimeout: 0,
        xagg: -1,
        pen: -1,
        brow: '',
        browver: '',
        psub: '-',
        lang: '-',
        prod: '-',
        plen: -1,
        doadma_en: 0,
        sdfn: [],
        d2: 0,
        d3: 0,
        thr: 0,
        cs: '0a46G5m17Vrp4o4c',
        hn: 'unk',
        z1: 0,
        o9: 0,
        vc: '',
        y1: 2016,
        ta: 0,
        tst: -1,
        t_tst: 0,
        ckie: "_abck",
        n_ck: '0',
        ckurl: 0,
        bm: !1,
        mr: -1,
        altFonts: !1,
        rst: !1,
        runFonts: !0,
        fsp: !1,
        mn_mc_lmt: 10,
        mn_state: 0,
        mn_mc_indx: 0,
        mn_sen: 0,
        mn_tout: 100,
        mn_stout: 1e3,
        mn_cc: '',
        mn_cd: 1e4,
        mn_lc: '',
        mn_ld: 1e4,
        mn_al: [],
        mn_il: [],
        mn_tcl: [],
        mn_r: '',
        mn_abck: '',
        mn_psn: '',
        mn_ts: '',
        mn_lg: [],
        ir: function () {
            // 00000
            bmak['start_ts'] = Date.now ? Date.now() : +new Date,
            bmak['kact'] = '',
            bmak['ke_cnt'] = 0,
            bmak['ke_vel'] = 0,
            bmak['mact'] = '',
            bmak['mme_cnt'] = 0,
            bmak['mduce_cnt'] = 0,
            bmak['me_vel'] = 0,
            bmak['pact'] = '',
            bmak['pme_cnt'] = 0,
            bmak['pduce_cnt'] = 0,
            bmak['pe_vel'] = 0,
            bmak['tact'] = '',
            bmak['tme_cnt'] = 0,
            bmak['tduce_cnt'] = 0,
            bmak['te_vel'] = 0,
            bmak['doact'] = '',
            bmak['doe_cnt'] = 0,
            bmak['doe_vel'] = 0,
            bmak['dmact'] = '',
            bmak['dme_cnt'] = 0,
            bmak['dme_vel'] = 0,
            bmak['vcact'] = '',
            bmak['vc_cnt'] = 0,
            bmak["aj_indx"] = 0,
            bmak['aj_ss'] = 0,
            bmak["aj_type"] = -1,
            bmak['aj_indx_doact'] = 0,
            bmak['aj_indx_dmact'] = 0,
            bmak['aj_indx_tact'] = 0,
            bmak['me_cnt'] = 0,
            bmak['pe_cnt'] = 0,
            bmak['te_cnt'] = 0
        },
        // 000000
        get_cf_date: function () {
            return Date.now ? Date.now() : +new Date
        },
        // 00000
        sd_debug: function (a) {    // <init/>
            if (!bmak["js_post"]) {  //永远为true
            // if (!bmak["js_post"]) {      ! !1
                var t = a;
                'string' == typeof _sd_trace ? _sd_trace += t : _sd_trace = t
                // string == typeof _sd_trace ? _sd_trace += t : _sd_trace = t  -==> <init/><init/>
            }
        },
        pi: function (a) {
            return parseInt(a)
        },
        // 获取 U-A 头。 000000
        uar: function () {
            return window['navigator']['userAgent'].replace(/\\|"/g, '')
        },
        gd: function () {
            var a = bmak["uar"](),
                t = '' + bmak['ab'](a),
                e = bmak['start_ts'] / 2,
                n = window['screen'] ? window['screen']['availWidth'] : -1,
                o = window['screen'] ? window['screen']['availHeight'] : -1,
                m = window['screen'] ? window['screen']['width'] : -1,
                r = window['screen'] ? window['screen']['height'] : -1,
                i = window['innerWidth'] || 1431,
                c = window['innerHeight'] || 1315,
                b = window['outerWidth'] || undefined;
            bmak['z1'] = bmak['pi'](bmak['start_ts'] / (bmak['y1'] * bmak['y1']));
            var d = Math['random'](),
                k = bmak['pi'](1e3 * d / 2),
                s = d + '';
            return s = s['slice'](0, 11) + k,
            bmak['get_browser'](),
            bmak['bc'](),
            bmak['bmisc'](),
            a + ',uaend,' + bmak['xagg'] + "," + bmak['psub'] + "," + bmak['lang'] + "," + bmak['prod'] + "," + bmak['plen'] + "," + bmak['pen'] + "," + bmak['wen'] + "," + bmak['den'] + "," + bmak['z1'] + "," + bmak['d3'] + "," + n + "," + o + "," + m + "," + r + "," + i + "," + c + "," + b + "," + bmak['bd']() + "," + t + "," + s + "," + e + ',loc:' + bmak['loc']
        },
        get_browser: function () {
            navigator['productSub'] && (bmak['psub'] = navigator['productSub']),
            navigator['language'] && (bmak['lang'] = navigator['language']),
            navigator['product'] && (bmak['prod'] = navigator['product']),
            bmak['plen'] = void 0 !== navigator['plugins'] ? navigator['plugins'].length : -1
        },

        //  赋值   bmak['xagg'] = 12147
        bc: function () {
            var a = window['addEventListener'] ? 1 : 0,
                t = window['XMLHttpRequest'] ? 1 : 0,
                e = window['XDomainRequest'] ? 1 : 0,
                n = window['emit'] ? 1 : 0,
                o = window.DeviceOrientationEvent ? 1 : 0,
                m = window.DeviceMotionEvent ? 1 : 0,
                r = window.TouchEvent ? 1 : 0,
                i = window['spawn'] ? 1 : 0,
                c = window['innerWidth'] ? 1 : 0,
                b = window['outerWidth'] ? 1 : 0,
                d = window['chrome'] ? 1 : 0,
                k = Function['prototype']['bind'] ? 1 : 0,
                s = window['Buffer'] ? 1 : 0,
                l = window['PointerEvent'] ? 1 : 0;
            bmak['xagg'] = a + (t << 1) + (e << 2) + (n << 3) + (o << 4) + (m << 5) + (r << 6) + (i << 7) + (c << 8) + (b << 9) + (d << 10) + (k << 11) + (s << 12) + (l << 13)
        },

        bmisc: function () {
            bmak['pen'] = window['_phantom'] ? 1 : 0,
            bmak['wen'] = window['webdriver'] ? 1 : 0,
            bmak['den'] = window['domAutomation'] ? 1 : 0
        },
        bd: function () {
            var a = [],
                t = window['callPhantom'] ? 1 : 0;
            a['push'](',cpen:' + t);
            try {
                    var e = new Function('return/*@cc_on!@*/!1')() ? 1 : 0
                } catch (a) {
                    var e = 0
                }
            a['push']('i1:' + e);
            var n = number == typeof undefined ? 1 : 0;
            a['push']('dm:' + n);
            var o = window['chrome'] && window['chrome']['webstore'] ? 1 : 0;
            a['push']('cwen:' + o);
            var m = navigator['onLine'] ? 1 : 0;
            a['push']('non:' + m);
            var r = window['opera'] ? 1 : 0;
            a['push']('opc:' + r);
            var i = undefined != typeof InstallTrigger ? 1 : 0;
            a['push']('fc:' + i);
            var c = window['HTMLElement'] && Object['prototype']['toString']['call'](window['HTMLElement']).indexOf('Constructor') > 0 ? 1 : 0;
            a['push']('sc:' + c);
            var b = function == typeof window["RTCPeerConnection"] || function == typeof window["mozRTCPeerConnection"] || function == typeof window["webkitRTCPeerConnection"] ? 1 : 0;
            a['push']('wrc:' + b);
            var d = 'mozInnerScreenY' in window ? window['mozInnerScreenY'] : 0;
            a['push']('isc:' + d),
            bmak['d2'] = bmak['pi'](bmak['z1'] / 23);
            var k = 'function' == typeof navigator['vibrate'] ? 1 : 0;
            a['push']('vib:' + k);
            var s = 'function' == typeof navigator['getBattery'] ? 1 : 0;
            a['push']('bat:' + s);
            var l = Array['prototype']['forEach'] ? 0 : 1;
            a['push']('x11:' + l);
            var u = 'FileReader' in window ? 1 : 0;
            return a['push']('x12:' + u),
            a.join(",")
        },

        // 30261693
        fas: function () {
            try {
                return Boolean(navigator['credentials']) + (Boolean(navigator['appMinorVersion']) << 1) + (Boolean(navigator['bluetooth']) << 2) + (Boolean(navigator['storage']) << 3) + (Boolean(Math['imul']) << 4) + (Boolean(navigator['getGamepads']) << 5) + (Boolean(navigator['getStorageUpdates']) << 6) + (Boolean(navigator['hardwareConcurrency']) << 7) + (Boolean(navigator['mediaDevices']) << 8) + (Boolean(navigator['mozAlarms']) << 9) + (Boolean(navigator['mozConnection']) << 10) + (Boolean(navigator['mozIsLocallyAvailable']) << 11) + (Boolean(navigator['mozPhoneNumberService']) << 12) + (Boolean(navigator['msManipulationViewsEnabled']) << 13) + (Boolean(navigator['permissions']) << 14) + (Boolean(navigator['registerProtocolHandler']) << 15) + (Boolean(navigator['requestMediaKeySystemAccess']) << 16) + (Boolean(navigator['requestWakeLock']) << 17) + (Boolean(navigator['sendBeacon']) << 18) + (Boolean(navigator['serviceWorker']) << 19) + (Boolean(navigator['storeWebWideTrackingException']) << 20) + (Boolean(navigator['webkitGetGamepads']) << 21) + (Boolean(navigator['webkitTemporaryStorage']) << 22) + (Boolean(Number['parseInt']) << 23) + (Boolean(Math['hypot']) << 24)
            } catch (a) {
                return 0
            }
        },
        // 获取 bmak['mr'] = a
        getmr: function () {
            try {
                // false
                if (undefined == typeof performance || void 0 === performance.now || undefined == typeof JSON) return void(bmak["mr"] = "undef");
                // 一个随机 14 个的字符串
                // " 58,62,62,61,83,198,67,8,11,6,6,7,605,503,"
                for (var a = '', t = 1e3, e = [Math['abs'], Math['acos'], Math['asin'], Math['atanh'], Math['cbrt'], Math['exp'], Math['random'], Math['round'], Math['sqrt'], isFinite, isNaN, parseFloat, parseInt, JSON['parse']], n = 0; n < e.length; n++) {
                    var o = [],
                        m = 0,
                        r = performance.now(),
                        i = 0,
                        c = 0;
                    if (void 0 !== e[n]) {
                            for (i = 0; i < t && m < .6; i++) {
                                for (var b = performance.now(), d = 0; d < 4e3; d++) e[n](3.14);
                                var k = performance.now();
                                o['push'](Math['round'](1e3 * (k - b))),
                                m = k - r
                            }
                            var s = o['sort']();
                            c = s[Math['floor'](s.length / 2)] / 5
                        }
                    a = a + c + ","
                }
                bmak['mr'] = a
            } catch (a) {
                bmak['mr'] = 'exception'
            }
        },
        // 返回 0,0,0,0,1,0,0
        sed: function () {
            var a;
            a = '0';
            var t;
            t = '0';
            var e;
            e = '0';
            var n;
            n = '0';
            var o;
            o = '1';
            var m;
            m = '0';
            var r;
            return r = '0',
            [a, t, e, n, o, m, r].join(",")

        },

        cma: function (a, t) {
            try {
                if (1 == t && bmak['mme_cnt'] < bmak['mme_cnt_lmt'] || 1 != t && bmak['mduce_cnt'] < bmak['mduce_cnt_lmt']) {
                    var e = a || window['event'],
                        n = -1,
                        o = -1;
                    e && e['pageX'] && e['pageY'] ? (n = Math['floor'](e['pageX']), o = Math['floor'](e['pageY'])) : e && e['clientX'] && e['clientY'] && (n = Math['floor'](e['clientX']), o = Math['floor'](e['clientY']));
                    var m = e['toElement'];
                    null == m && (m = e['target']);
                    var r = bmak['gf'](m),
                        i = bmak["get_cf_date"]() - bmak['start_ts'],
                        c = bmak['me_cnt'] + "," + t + "," + i + "," + n + "," + o;
                    if (1 != t) {
                            c = c + "," + r;
                            var b = void 0 !== e['which'] ? e['which'] : e['button'];
                            null != b && 1 != b && (c = c + "," + b)
                        }
                    c += ';',
                    bmak['me_vel'] = bmak['me_vel'] + bmak['me_cnt'] + t + i + n + o,
                    bmak['mact'] = bmak['mact'] + c,
                    bmak['ta'] += i
                }
                1 == t ? bmak['mme_cnt']++ : bmak['mduce_cnt']++,
                bmak['me_cnt']++,
                bmak["js_post"] && 3 == t && (bmak["aj_type"] = 1, bmak['bpd'](), bmak['pd'](!0), bmak['ce_js_post'] = 1)
            } catch (a) {}
        },

        // 其实就是返回 时间戳
        x2: function () {
            // 指定uricoder  返回一个字符串
            var a = bmak['ff'],
                t = a(98) + a(109) + a(97) + a(107) + a(46) + a(103) + a(101) + a(116);
                // t = return bmak.get_cf_date();
            return t = t + a(95) + a(99) + a(102) + a(95),
            t = 'return ' + t + a(100) + a(97) + a(116) + a(101) + a(40) + a(41),
            t += ';',
            new Function(t)()
        },
        cpa: function (a, t) {
            try {
                var e = !1;
                if (1 == t && bmak['pme_cnt'] < bmak['pme_cnt_lmt'] || 1 != t && bmak['pduce_cnt'] < bmak['pduce_cnt_lmt']) {
                    var n = a || window['event'];
                    if (n && 'mouse' != n['pointerType']) {
                        e = !0;
                        var o = -1,
                            m = -1;
                        n && n['pageX'] && n['pageY'] ? (o = Math['floor'](n['pageX']), m = Math['floor'](n['pageY'])) : n && n['clientX'] && n['clientY'] && (o = Math['floor'](n['clientX']), m = Math['floor'](n['clientY']));
                        var r = bmak["get_cf_date"]() - bmak['start_ts'],
                            i = bmak['pe_cnt'] + "," + t + "," + r + "," + o + "," + m + ';';
                        bmak['pe_vel'] = bmak['pe_vel'] + bmak['pe_cnt'] + t + r + o + m,
                        bmak['pact'] = bmak['pact'] + i,
                        bmak['ta'] += r,
                        1 == t ? bmak['pme_cnt']++ : bmak['pduce_cnt']++
                    }
                }
                1 == t ? bmak['pme_cnt']++ : bmak['pduce_cnt']++,
                bmak['pe_cnt']++,
                bmak["js_post"] && 3 == t && e && (bmak["aj_type"] = 2, bmak['bpd'](), bmak['pd'](!0), bmak['ce_js_post'] = 1)
            } catch (a) {}
        },

        // 返回一个数字
        ab: function (a) {
            if (null == a) return -1;
            try {

                for (var t = 0, e = 0; e < a.length; e++) {
                    var n = a.charCodeAt(e);
                    n < 128 && (t += n)
                }
                return t    // 1676
            } catch (a) {
                return -2
            }
        },
        ff: function (a) {
            return String.fromCharCode(a)
        },

        to: function () {
            var a = bmak['x2']() % 1e7;
            bmak['d3'] = a;
            for (var t = a, e = 0; e < 5; e++) {
                var n = bmak['pi'](a / Math['pow'](10, e)) % 10,
                    o = n + 1,
                    m = 'return a' + bmak['cc'](n) + o + ';';
                t = new Function('a', m)(t)
            }
            bmak['o9'] = t
        },
        // 将其 name 或者id 进行数字化，在返回。
        // 也就是 a 肯定是一个 DOM 文档
        gf: function (a) {
            // t 等于 a
            var t;
            if (t = null == a ? document.activeElement : a, null == document.activeElement) return -1;

            var e = t.getAttribute('name');
            if (null == e) {
                var n = t.getAttribute('id');
                return null == n ? -1 : asd(n)
            }
            return asd(e)
        },
        // 模四余二 返回 逗号，  否则返回 -
        cc: function (a) {
            var t = a % 4;
            2 == t && (t = 3);
            var e = 42 + t;
            return String.fromCharCode(e)
        },
        isIgn: function (a) {
            var t = document['activeElement'];
            if (null == document['activeElement']) return 0;
            var e = t['getAttribute']('type');
            return 1 == (null == e ? -1 : bmak['get_type'](e)) && bmak['fidcnt'] > 12 && -2 == a ? 1 : 0
        },
        cka: function (a, t) {
            try {
                var e = a || window['event'],
                    n = -1,
                    o = 1;
                if (bmak['ke_cnt'] < bmak['ke_cnt_lmt'] && e) {
                        n = e['keyCode'];
                        var m = e['charCode'],
                            r = e['shiftKey'] ? 1 : 0,
                            i = e['ctrlKey'] ? 1 : 0,
                            c = e['metaKey'] ? 1 : 0,
                            b = e['altKey'] ? 1 : 0,
                            d = 8 * r + 4 * i + 2 * c + b,
                            k = bmak["get_cf_date"]() - bmak['start_ts'],
                            s = bmak['gf'](null),
                            l = 0;
                        m && n && (n = 0 != m && 0 != n && m != n ? -1 : 0 != n ? n : m),
                        0 == i && 0 == c && 0 == b && n >= 32 && (n = 3 == t && n >= 32 && n <= 126 ? -2 : n >= 33 && n <= 47 ? -3 : n >= 112 && n <= 123 ? -4 : -2),
                        s != bmak['prevfid'] ? (bmak['fidcnt'] = 0, bmak['prevfid'] = s) : bmak['fidcnt'] = bmak['fidcnt'] + 1;
                        if (0 == bmak['isIgn'](n)) {
                                var u = bmak['ke_cnt'] + "," + t + "," + k + "," + n + "," + l + "," + d + "," + s;
                                null != e['isTrusted'] && !1 === e['isTrusted'] && (u += ',0'),
                                u += ';',
                                bmak['kact'] = bmak['kact'] + u,
                                bmak['ke_vel'] = bmak['ke_vel'] + bmak['ke_cnt'] + t + k + n + d + s,
                                bmak['ta'] += k
                            } else o = 0
                    }
                o && e && bmak['ke_cnt']++,
                !bmak["js_post"] || 1 != t || 13 != n && 9 != n || (bmak["aj_type"] = 3, bmak['bpd'](), bmak['pd'](!0), bmak['ce_js_post'] = 1)
            } catch (a) {}
        },
        cta: function (a, t) {
            try {
                if (1 == t && bmak['tme_cnt'] < bmak['tme_cnt_lmt'] || 1 != t && bmak['tduce_cnt'] < bmak['tduce_cnt_lmt']) {
                    var e = a || window['event'],
                        n = -1,
                        o = -1;
                    e && e['pageX'] && e['pageY'] ? (n = Math['floor'](e['pageX']), o = Math['floor'](e['pageY'])) : e && e['clientX'] && e['clientY'] && (n = Math['floor'](e['clientX']), o = Math['floor'](e['clientY']));
                    var m = bmak["get_cf_date"]() - bmak['start_ts'],
                        r = bmak['te_cnt'] + "," + t + "," + m + "," + n + "," + o + ';';
                    bmak['tact'] = bmak['tact'] + r,
                    bmak['ta'] += m,
                    bmak['te_vel'] = bmak['te_vel'] + bmak['te_cnt'] + t + m + n + o,
                    bmak['doa_throttle'] = 0,
                    bmak['dma_throttle'] = 0
                }
                1 == t ? bmak['tme_cnt']++ : bmak['tduce_cnt']++,
                bmak['te_cnt']++,
                bmak["js_post"] && 2 == t && bmak['aj_indx_tact'] < bmak['aj_lmt_tact'] && (bmak["aj_type"] = 5, bmak['bpd'](), bmak['pd'](!0), bmak['ce_js_post'] = 1, bmak['aj_indx_tact']++)
            } catch (a) {}
        },
        getFloatVal: function (a) {
            try {
                if (-1 != bmak['chknull'](a) && !isNaN(a)) {
                    var t = parseFloat(a);
                    if (!isNaN(t)) return t['toFixed'](2)
                }
            } catch (a) {}
            return -1
        },
        cdoa: function (a) {
            try {
                if (bmak['doe_cnt'] < bmak['doe_cnt_lmt'] && bmak['doa_throttle'] < 2 && a) {
                    var t = bmak["get_cf_date"]() - bmak['start_ts'],
                        e = bmak['getFloatVal'](a['alpha']),
                        n = bmak['getFloatVal'](a['beta']),
                        o = bmak['getFloatVal'](a['gamma']),
                        m = bmak['doe_cnt'] + "," + t + "," + e + "," + n + "," + o + ';';
                    bmak['doact'] = bmak['doact'] + m,
                    bmak['ta'] += t,
                    bmak['doe_vel'] = bmak['doe_vel'] + bmak['doe_cnt'] + t,
                    bmak['doe_cnt']++
                }
                bmak["js_post"] && bmak['doe_cnt'] > 1 && bmak['aj_indx_doact'] < bmak['aj_lmt_doact'] && (bmak["aj_type"] = 6, bmak['bpd'](), bmak['pd'](!0), bmak['ce_js_post'] = 1, bmak['aj_indx_doact']++),
                bmak['doa_throttle']++
            } catch (a) {}
        },
        cdma: function (a) {
            try {
                if (bmak['dme_cnt'] < bmak['dme_cnt_lmt'] && bmak['dma_throttle'] < 2 && a) {
                    var t = bmak["get_cf_date"]() - bmak['start_ts'],
                        e = -1,
                        n = -1,
                        o = -1;
                    a['acceleration'] && (e = bmak['getFloatVal'](a['acceleration']['x']), n = bmak['getFloatVal'](a['acceleration']['y']), o = bmak['getFloatVal'](a['acceleration']['z']));
                    var m = -1,
                        r = -1,
                        i = -1;
                    a['accelerationIncludingGravity'] && (m = bmak['getFloatVal'](a['accelerationIncludingGravity']['x']), r = bmak['getFloatVal'](a['accelerationIncludingGravity']['y']), i = bmak['getFloatVal'](a['accelerationIncludingGravity']['z']));
                    var c = -1,
                        b = -1,
                        d = 1;
                    a['rotationRate'] && (c = bmak['getFloatVal'](a['rotationRate']['alpha']), b = bmak['getFloatVal'](a['rotationRate']['beta']), d = bmak['getFloatVal'](a['rotationRate']['gamma']));
                    var k = bmak['dme_cnt'] + "," + t + "," + e + "," + n + "," + o + "," + m + "," + r + "," + i + "," + c + "," + b + "," + d + ';';
                    bmak['dmact'] = bmak['dmact'] + k,
                    bmak['ta'] += t,
                    bmak['dme_vel'] = bmak['dme_vel'] + bmak['dme_cnt'] + t,
                    bmak['dme_cnt']++
                }
                bmak["js_post"] && bmak['dme_cnt'] > 1 && bmak['aj_indx_dmact'] < bmak['aj_lmt_dmact'] && (bmak["aj_type"] = 7, bmak['bpd'](), bmak['pd'](!0), bmak['ce_js_post'] = 1, bmak['aj_indx_dmact']++),
                bmak['dma_throttle']++
            } catch (a) {}
        },
        get_type: function (a) {
            return a = a['toLowerCase'](),
            'text' == a || 'search' == a || 'url' == a || 'email' == a || 'tel' == a || 'number' == a ? 0 : 'password' == a ? 1 : 2
        },
        chknull: function (a) {
            return null == a ? -1 : a
        },
        forminfo: function () {
            for (var a = '', t = '', e = document['getElementsByTagName']('input'), n = -1, o = 0; o < e.length; o++) {
                var m = e[o],
                    r = bmak['ab'](m['getAttribute']('name')),
                    i = bmak['ab'](m['getAttribute']('id')),
                    c = m['getAttribute']('required'),
                    b = null == c ? 0 : 1,
                    d = m['getAttribute']('type'),
                    k = null == d ? -1 : bmak['get_type'](d),
                    s = m['getAttribute']('autocomplete');
                null == s ? n = -1 : (s = s['toLowerCase'](), n = 'off' == s ? 0 : 'on' == s ? 1 : 2);
                var l = m['defaultValue'],
                    u = m['value'],
                    _ = 0,
                    f = 0;
                l && 0 != l.length && (f = 1),
                !u || 0 == u.length || f && u == l || (_ = 1),
                2 != k && (a = a + k + "," + n + "," + _ + "," + b + "," + i + "," + r + "," + f + ';'),
                t = t + _ + ';'
            }
            return null == bmak['ins'] && (bmak['ins'] = t),
            bmak['cns'] = t,
            a
        },
        startdoadma: function () {
            0 == bmak['doadma_en'] && window['addEventListener'] && (window['addEventListener']('deviceorientation', bmak['cdoa'], !0), window['addEventListener']('devicemotion', bmak['cdma'], !0), bmak['doadma_en'] = 1),
            bmak['doa_throttle'] = 0,
            bmak['dma_throttle'] = 0
        },
        // 00000
        updatet: function () {
            return bmak["get_cf_date"]() - bmak['start_ts']
        },
        htm: function (a) {
            bmak['cta'](a, 1)
        },
        hts: function (a) {
            bmak['cta'](a, 2)
        },
        hte: function (a) {
            bmak['cta'](a, 3)
        },
        htc: function (a) {
            bmak['cta'](a, 4)
        },
        hmm: function (a) {
            bmak['cma'](a, 1)
        },
        hc: function (a) {
            bmak['cma'](a, 2)
        },
        hmd: function (a) {
            bmak['cma'](a, 3)
        },
        hmu: function (a) {
            bmak['cma'](a, 4)
        },
        hpd: function (a) {
            bmak['cpa'](a, 3)
        },
        hpu: function (a) {
            bmak['cpa'](a, 4)
        },
        hkd: function (a) {
            bmak['cka'](a, 1)
        },
        hku: function (a) {
            bmak['cka'](a, 2)
        },
        hkp: function (a) {
            bmak['cka'](a, 3)
        },
        cfsubmit: function () {
            bmak["sd_debug"]('<cfsubmit/>'),
            bmak["js_post"] ? (bmak["aj_type"] = 4, bmak['bpd'](), 0 == bmak['ce_js_post'] && bmak['cns'] != bmak['ins'] && bmak['pd'](!0)) : bmak['bpd']()
        },
        getdurl: function () {
            return bmak['enReadDocUrl'] ? document['URL'].replace(/\\|"/g, '') : ''
        },
        x1: function () {

            return Math['floor'](16777216 * (1 + Math['random']()))['toString'](36)
            // Math.floor(16777216 * (1 + Math.random())).toString(36)
        },
        gck: function () {
            var a = bmak['x1']() + bmak['x1']() + bmak['x1']() + bmak['x1']();
            return bmak['set_cookie'](bmak["ckie"], a + '_' + bmak['ab'](a)),a
            // a = bmak[x1]() * 4   d5w0c  d5w0cd5w0cd5w0cd5w0c
            // bmak.set_cookie("_abck",a*4 + "_" + bmak[ab](a*4)), a
            // bmak.set_cookie("_abck",a*4 + "_" + 1676), a
            // d5w0cd5w0cd5w0cd5w0c
        },
        set_cookie: function (a, t) {
            void 0 !== document.cookie && (document.cookie = a + "=" + t + '; path=/; expires=Fri, 01 Feb 2025 08:00:00 GMT;')
            // void 0 !== document.cookie && (document.cookie = a + "=" + "d5w0cd5w0cd5w0cd5w0c_1676" + "; path=/; expires=Fri, 01 Feb 2025 08:00:00 GMT;")
        },
        get_cookie: function () {
            try {
                var a = bmak["cookie_chk_read"](bmak["ckie"]);
                return a || (bmak["n_ck"] = 1, a = bmak["gck"]()),
                a
            } catch (a) {}
            return 2  //dmr7fbzmlajit5fbuh3t_1982
        },
        // 返回 等于号后面的
        cookie_chk_read: function (a) {
            // a == "_abck"
            if (document.cookie)
                for (var t = a + "=", e = document.cookie.split(";"), n = 0; n < e.length; n++) {
                var o = e[n];
                if (0 === o.indexOf(t)) {

                    var m = o.substring(t.length, o.length);
                    if (!!1) return m;
                    if (-1 != m.indexOf("~")) return m
                }
            }
            return !1
        },
        // 00000
        bpd: function () {
            bmak["sd_debug"]("<bpd>");
            var a = 0;
            try {
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
            } catch (a) {
                try {
                    bmak["sd_debug"](',s2:' + a),
                    sensor_data = bmak['ver'] + '-1,2,-94,-100,' + bmak["uar"]() + '-1,2,-94,-120,' + a.replace(/\"/g, "'")
                } catch (a) {
                    bmak["sd_debug"](',s3:' + a)
                }
            }
            try {
                var g = bmak['od'](bmak['cs'], bmak['api_public_key'])['slice'](0, 16),
                    w = Math['floor'](bmak["get_cf_date"]() / 36e5),
                    y = bmak["get_cf_date"](),
                    C = g + bmak['od'](w, g) + sensor_data;
                sensor_data = C + ';' + (bmak["get_cf_date"]() - a) + ';' + bmak['tst'] + ';' + (bmak["get_cf_date"]() - y)

            } catch (a) {}
            try {
                if (0 == bmak["sdfn"].length) bmak["sd_debug"](',s4'),
                document['getElementById']('sensor_data') && (bmak["sd_debug"](',s5'), document['getElementById']('sensor_data')['value'] = sensor_data);
                else {
                    bmak["sd_debug"](',s6:');
                    for (var j = 0; j < bmak["sdfn"].length; j++) if (bmak["sd_debug"](',a-' + bmak["sdfn"][j]), document['getElementById'](bmak["sdfn"][j])) {
                        bmak["sd_debug"](',b'),
                        document['getElementById'](bmak["sdfn"][j])['value'] = sensor_data;
                        var S = document['getElementById'](bmak["sdfn"][j])['value'];
                        'string' == typeof S ? bmak["sd_debug"](',c-' + S['slice'](0, 5)) : bmak["sd_debug"](',c-null')
                    } else bmak["sd_debug"](',d')
                }
            } catch (a) {
                bmak["sd_debug"](',s7:' + a + "," + sensor_data)
            }
            bmak["sd_debug"]('</bpd>')
        },
        od: function (a, t) {
            try {
                a = String(a),
                t = String(t);
                var e = [],
                    n = t.length;
                if (n > 0) {
                        for (var o = 0; o < a.length; o++) {
                            var m = a['charCodeAt'](o),
                                r = a['charAt'](o),
                                i = t['charCodeAt'](o % n);
                            m = bmak['rir'](m, 47, 57, i),
                            m != a['charCodeAt'](o) && (r = String['fromCharCode'](m)),
                            e['push'](r)
                        }
                        if (e.length > 0) return e.join('')
                    }
            } catch (a) {}
            return a
        },
        rir: function (a, t, e, n) {
            return a > t && a <= e && (a += n % (e - t)) > e && (a = a - e + t),
            a
        },
        lvc: function (a) {
            try {
                if (bmak['vc_cnt'] < bmak['vc_cnt_lmt']) {
                    var t = bmak["get_cf_date"]() - bmak['start_ts'],
                        e = a + "," + t + ';';
                    bmak['vcact'] = bmak['vcact'] + e
                }
                bmak['vc_cnt']++
            } catch (a) {}
        },
        hvc: function () {
            try {
                var a = 1;
                document[bmak['hn']] && (a = 0),
                bmak['lvc'](a)
            } catch (a) {}
        },
        hb: function (a) {
            bmak['lvc'](2)
        },
        hf: function (a) {
            bmak['lvc'](3)
        },
        rve: function () {
            void 0 !== document['hidden'] ? (bmak['hn'] = 'hidden', bmak['vc'] = 'visibilitychange') : void 0 !== document['mozHidden'] ? (bmak['hn'] = 'mozHidden', bmak['vc'] = 'mozvisibilitychange') : void 0 !== document['msHidden'] ? (bmak['hn'] = 'msHidden', bmak['vc'] = 'msvisibilitychange') : void 0 !== document['webkitHidden'] && (bmak['hn'] = 'webkitHidden', bmak['vc'] = 'webkitvisibilitychange'),
            document['addEventListener'] ? 'unk' != bmak['hn'] && document['addEventListener'](bmak['vc'], bmak['hvc'], !0) : document['attachEvent'] && 'unk' != bmak['hn'] && document['attachEvent'](bmak['vc'], bmak['hvc']),
            window['onblur'] = bmak['hb'],
            window['onfocus'] = bmak['hf']
        },
        // 开启跟踪
        startTracking: function () {
            // 开启doadma
            bmak['startdoadma']();
            try {
                bmak['to']()
            } catch (a) {
                bmak['o9'] = -654321
            }
            setInterval(function () {
                bmak['startdoadma']()
            }, 3e3),
            document['addEventListener'] ? (document['addEventListener']('touchmove', bmak['htm'], !0), document['addEventListener']('touchstart', bmak['hts'], !0), document['addEventListener']('touchend', bmak['hte'], !0), document['addEventListener']('touchcancel', bmak['htc'], !0), document['addEventListener']('mousemove', bmak['hmm'], !0), document['addEventListener']('click', bmak['hc'], !0), document['addEventListener']('mousedown', bmak['hmd'], !0), document['addEventListener']('mouseup', bmak['hmu'], !0), document['addEventListener']('pointerdown', bmak['hpd'], !0), document['addEventListener']('pointerup', bmak['hpu'], !0), document['addEventListener']('keydown', bmak['hkd'], !0), document['addEventListener']('keyup', bmak['hku'], !0), document['addEventListener']('keypress', bmak['hkp'], !0)) : document['attachEvent'] && (document['attachEvent']('touchmove', bmak['htm']), document['attachEvent']('touchstart', bmak['hts']), document['attachEvent']('touchend', bmak['hte']), document['attachEvent']('touchcancel', bmak['htc']), document['attachEvent']('onmousemove', bmak['hmm']), document['attachEvent']('onclick', bmak['hc']), document['attachEvent']('onmousedown', bmak['hmd']), document['attachEvent']('onmouseup', bmak['hmu']), document['attachEvent']('onpointerdown', bmak['hpd']), document['attachEvent']('onpointerup', bmak['hpu']), document['attachEvent']('onkeydown', bmak['hkd']), document['attachEvent']('onkeyup', bmak['hku']), document['attachEvent']('onkeypress', bmak['hkp'])),
            bmak['rve'](),
            bmak['informinfo'] = bmak["forminfo"](),
            bmak["js_post"] && (bmak["aj_type"] = 0, bmak['bpd'](), bmak['pd'](!0))
        },
        gb: function (a, t) {
            var e = a['charCodeAt'](t);
            return e = e > 255 ? 0 : e
        },
        encode: function (a) {
            if ('undefined' != typeof btoa) return btoa(a);
            for (var t, e, n, o, m, r, i, c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/', b = '', d = 3 * Math['floor'](a.length / 3), k = 0; k < d; k += 3) t = bmak['gb'](a, k),
            e = bmak['gb'](a, k + 1),
            n = bmak['gb'](a, k + 2),
            o = t >> 2,
            m = ((3 & t) << 4) + (e >> 4),
            r = ((15 & e) << 2) + (n >> 6),
            i = 63 & n,
            b = b + c['charAt'](o) + c['charAt'](m) + c['charAt'](r) + c['charAt'](i);
            return a.length % 3 == 1 && (t = bmak['gb'](a, k), o = t >> 2, m = (3 & t) << 4, b = b + c['charAt'](o) + c['charAt'](m) + '=='),
            a.length % 3 == 2 && (t = bmak['gb'](a, k), e = bmak['gb'](a, k + 1), o = t >> 2, m = ((3 & t) << 4) + (e >> 4), r = (15 & e) << 2, b = b + c['charAt'](o) + c['charAt'](m) + c['charAt'](r) + "="),
            b
        },
        ie9OrLower: function () {
            try {
                if ('string' == typeof navigator['appVersion'] && -1 != navigator['appVersion'].indexOf('MSIE')) {
                    if (parseFloat(navigator['appVersion'].split('MSIE')[1]) <= 9) return !0
                }
            } catch (a) {}
            return !1
        },
        apicall: function (a, t) {
            var e;
            e = window['XDomainRequest'] ? new XDomainRequest : window['XMLHttpRequest'] ? new XMLHttpRequest : new ActiveXObject('Microsoft.XMLHTTP'),
            e['open']('POST', a, t);
            var n = bmak['encode'](bmak['api_public_key'] + ':');
            bmak['auth'] = ',"auth" : "' + n + '"',
            e['setRequestHeader'] && (e['setRequestHeader']('Content-type', 'application/json'), e['setRequestHeader']('Authorization', 'Basic ' + n), bmak['auth'] = '');
            var o = '{"session_id" : "' + bmak['session_id'] + '","sensor_data" : "' + sensor_data + '"' + bmak['auth'] + '}';
            e['send'](o)
        },
        apicall_bm: function (a, t, e) {
            var n;
            void 0 !== window['XMLHttpRequest'] ? n = new XMLHttpRequest : void 0 !== window['XDomainRequest'] ? (n = new XDomainRequest, n['onload'] = function () {
                this['readyState'] = 4,
                this['onreadystatechange'] instanceof Function && this['onreadystatechange']()
            }) : n = new ActiveXObject('Microsoft.XMLHTTP'),
            n['open']('POST', a, t),
            void 0 !== n['withCredentials'] && (n['withCredentials'] = !0);
            var o = '{"sensor_data":"' + sensor_data + '"}';
            n['onreadystatechange'] = function () {
                n['readyState'] > 3 && e && e(n)
            },
            n['send'](o)
        },
        pd_en: function () {
            var a, t = bmak["getdurl"]();
            return 0 == bmak['thr'] ? 1 : (a = t.indexOf('home.html') > -1 ? 1 : 0, bmak['start_ts'] % 10 != 0 ? 0 : bmak["aj_indx"] > 3 ? 0 : a && bmak["aj_indx"] > 0 ? 0 : 1)
        },
        pd: function (a) {
            var t;
            (t = bmak['pd_en']()) && (bmak["bm"] ? bmak['check_stop_protocol']() && bmak['apicall_bm'](bmak['cf_url'], a, bmak['patp']) : bmak['apicall'](bmak['cf_url'], a), bmak["aj_indx"] = bmak["aj_indx"] + 1)
        },
        check_stop_protocol: function () {
            var a = bmak['get_stop_signals'](),
                t = a[0];
            !bmak['rst'] && t > -1 && (bmak['ir'](), bmak['rst'] = !0);
            var e = a[1];
            return -1 == e || bmak['aj_ss'] < e
        },
        get_stop_signals: function () {
            var a = [-1, -1],
                t = bmak["cookie_chk_read"](bmak["ckie"]);
            //  t = bmak[cookie_chk_read]("_abck");
            if (!1 !== t) try {
                    var e = decodeURIComponent(t).split("~");
                    if (e.length >= 4) {
                        var n = bmak['pi'](e[1]),
                            o = bmak['pi'](e[3]);
                        n = isNaN(n) ? -1 : n,
                        o = isNaN(o) ? -1 : o,
                        a = [o, n]
                    }
                } catch (a) {}
            return a
        },
        patp: function (a) {
            bmak['aj_ss']++,
            bmak['rst'] = !1
        },
        get_mn_params_from_abck: function () {
            var a = [0, 'default_abck', '', 1e5, 100, 1e3];
            try {
                var t = bmak["cookie_chk_read"](bmak["ckie"]);
                if (!1 !== t) {
                    var e = decodeURIComponent(t).split("~");
                    if (e.length >= 5) {
                        var n = e[0],
                            o = e[4],
                            m = o.split('-');
                        if (m.length >= 5) {
                                a = [bmak['pi'](m[0]), n, m[1], bmak['pi'](m[2]), bmak['pi'](m[3]), bmak['pi'](m[4])]
                            }
                    }
                }
            } catch (a) {}
            return a
        },
        mn_get_challenge: function () {
            var a = bmak['get_mn_params_from_abck'](),
                t = a[0],
                e = a[1],
                n = a[2],
                o = a[3],
                m = a[4],
                r = a[5];
            bmak['mn_abck'] = e,
            bmak['mn_psn'] = n['toString'](),
            bmak['mn_sen'] = t,
            bmak['mn_cd'] = o,
            bmak['mn_tout'] = m,
            bmak['mn_stout'] = r,
            bmak['mn_ts'] = bmak['start_ts'],
            bmak['mn_cc'] = bmak['mn_abck'] + bmak['start_ts'] + bmak['mn_psn']
        },
        mn_check_if_new_challenge: function () {
            return bmak['mn_cc'] != bmak['mn_lc'] || bmak['mn_cd'] != bmak['mn_ld'] ? 1 : 0
        },
        mn_poll: function () {
            if (0 == bmak['mn_state']) {
                bmak['mn_get_challenge']();
                var a = bmak['mn_check_if_new_challenge']();
                bmak['mn_sen'] && a && (bmak['mn_state'] = 1, bmak['mn_mc_indx'] = 0, bmak['mn_al'] = [], bmak['mn_il'] = [], bmak['mn_tcl'] = [], bmak['mn_lg'] = [], setTimeout(bmak['mn_w'], bmak['mn_tout']))
            }
        },
        mn_init: function () {
            setInterval(bmak['mn_poll'], 1e3)
        },
        rotate_left: function (a, t) {
            return a << t | a >>> 32 - t
        },
        encode_utf8: function (a) {
            return unescape(encodeURIComponent(a))
        },
        mn_h: function (a) {
            var t = 1732584193,
                e = 4023233417,
                n = 2562383102,
                o = 271733878,
                m = 3285377520,
                r = bmak['encode_utf8'](a),
                i = 8 * r.length;
            r += String['fromCharCode'](128);
            for (var c = r.length / 4 + 2, b = Math['ceil'](c / 16), d = new Array(b), k = 0; k < b; k++) {
                    d[k] = new Array(16);
                    for (var s = 0; s < 16; s++) d[k][s] = r['charCodeAt'](64 * k + 4 * s) << 24 | r['charCodeAt'](64 * k + 4 * s + 1) << 16 | r['charCodeAt'](64 * k + 4 * s + 2) << 8 | r['charCodeAt'](64 * k + 4 * s + 3) << 0
                }
            var l = i / Math['pow'](2, 32);
            d[b - 1][14] = Math['floor'](l),
            d[b - 1][15] = 4294967295 & i;
            for (var u = 0; u < b; u++) {
                    for (var _, f, p, v = new Array(80), h = t, g = e, w = n, y = o, C = m, k = 0; k < 80; k++) v[k] = k < 16 ? d[u][k] : bmak['rotate_left'](v[k - 3] ^ v[k - 8] ^ v[k - 14] ^ v[k - 16], 1),
                    k < 20 ? (_ = g & w | ~g & y, f = 1518500249) : k < 40 ? (_ = g ^ w ^ y, f = 1859775393) : k < 60 ? (_ = g & w | g & y | w & y, f = 2400959708) : (_ = g ^ w ^ y, f = 3395469782),
                    p = bmak['rotate_left'](h, 5) + _ + C + f + v[k],
                    C = y,
                    y = w,
                    w = bmak['rotate_left'](g, 30),
                    g = h,
                    h = p;
                    t += h,
                    e += g,
                    n += w,
                    o += y,
                    m += C
                }
            return [t >> 24 & 255, t >> 16 & 255, t >> 8 & 255, 255 & t, e >> 24 & 255, e >> 16 & 255, e >> 8 & 255, 255 & e, n >> 24 & 255, n >> 16 & 255, n >> 8 & 255, 255 & n, o >> 24 & 255, o >> 16 & 255, o >> 8 & 255, 255 & o, m >> 24 & 255, m >> 16 & 255, m >> 8 & 255, 255 & m]
        },
        bdm: function (a, t) {
            for (var e = 0, n = 0; n < a.length; ++n) e = (e << 8 | a[n]) >>> 0,
            e %= t;
            return e
        },
        mn_w: function () {
            try {
                for (var a = 0, t = 0, e = 0, n = '', o = bmak["get_cf_date"](), m = bmak['mn_cd'] + bmak['mn_mc_indx']; 0 == a;) {
                    n = Math['random']()['toString'](16);
                    var r = bmak['mn_cc'] + m['toString']() + n,
                        i = bmak['mn_h'](r);
                    if (0 == bmak['bdm'](i, m)) a = 1,
                    e = bmak["get_cf_date"]() - o,
                    bmak['mn_al']['push'](n),
                    bmak['mn_tcl']['push'](e),
                    bmak['mn_il']['push'](t),
                    0 == bmak['mn_mc_indx'] && (bmak['mn_lg']['push'](bmak['mn_abck']), bmak['mn_lg']['push'](bmak['mn_ts']), bmak['mn_lg']['push'](bmak['mn_psn']), bmak['mn_lg']['push'](bmak['mn_cc']), bmak['mn_lg']['push'](bmak['mn_cd']['toString']()), bmak['mn_lg']['push'](m['toString']()), bmak['mn_lg']['push'](n), bmak['mn_lg']['push'](r), bmak['mn_lg']['push'](i));
                    else if ((t += 1) % 1e3 == 0 && (e = bmak["get_cf_date"]() - o) > bmak['mn_stout']) return void setTimeout(bmak['mn_w'], 1e3 + bmak['mn_stout'])
                }
                bmak['mn_mc_indx'] += 1,
                bmak['mn_mc_indx'] < bmak['mn_mc_lmt'] ? setTimeout(bmak['mn_w'], bmak['mn_tout'] + e) : (bmak['mn_mc_indx'] = 0, bmak['mn_state'] = 0, bmak['mn_lc'] = bmak['mn_cc'], bmak['mn_ld'] = bmak['mn_cd'], bmak['mn_r'] = bmak['mn_pr']())
            } catch (a) {
                bmak["sd_debug"](',mn_w:' + a)
            }
        },
        mn_pr: function () {
            return bmak['mn_al'].join(",") + ';' + bmak['mn_tcl'].join(",") + ';' + bmak['mn_il'].join(",") + ';' + bmak['mn_lg'].join(",") + ';'
        },
        listFunctions: {
            _setJsPost: function (a) {
                bmak["js_post"] = a,
                bmak["js_post"] && (bmak['enReadDocUrl'] = 1)
            },
            _setSessionId: function (a) {
                bmak['session_id'] = a
            },
            _setJavaScriptKey: function (a) {
                bmak['api_public_key'] = a
            },
            _setEnAddHidden: function (a) {
                bmak['enAddHidden'] = a
            },
            _setInitTime: function (a) {
                bmak['init_time'] = a
            },
            _setApiUrl: function (a) {
                bmak['cf_url'] = a
            },
            _setEnGetLoc: function (a) {
                bmak['enGetLoc'] = a
            },
            _setEnReadDocUrl: function (a) {
                bmak['enReadDocUrl'] = a
            },
            _setDisFpCalOnTimeout: function (a) {
                bmak['disFpCalOnTimeout'] = a
            },
            _setCookie: function (a) {
                bmak["ckie"] = a
            },
            _setCS: function (a) {
                bmak['cs'] = (String(a) + bmak['cs'])['slice'](0, 16)
            },
            _setFsp: function (a) {
                bmak['fsp'] = a,
                bmak['fsp'] && (bmak['cf_url'] = bmak['cf_url'].replace(/^http:\/\//i, 'https://'))
            },
            _setBm: function (a) {
                bmak["bm"] = a,
                bmak["bm"] && (bmak['cf_url'] = (bmak['fsp'] ? 'https:' : document['location']['protocol']) + '//' + document['location']['hostname'] + '/_bm/_data', bmak['api_public_key'] = 'afSbep8yjnZUjq3aL010jO15Sawj2VZfdYK8uY90uxq', bmak["js_post"] = !0, bmak['enReadDocUrl'] = 1, bmak["runFonts"] = !1)
            },
            _setAu: function (a) {
                'string' == typeof a && 0 === a['lastIndexOf']('/', 0) && (bmak['cf_url'] = (bmak['fsp'] ? 'https:' : document['location']['protocol']) + '//' + document['location']['hostname'] + a)
            },
            _setSDFieldNames: function () {
                try {
                    var a;
                    for (a = 0; a < arguments.length; a += 1) bmak["sdfn"]['push'](arguments[a])
                } catch (a) {
                    bmak["sd_debug"](',setSDFN:' + a)
                }
            },
            _setUseAltFonts: function (a) {
                bmak['altFonts'] = a
            }
        },
        applyFunc: function () {
            var a, t, e;
            for (a = 0; a < arguments.length; a += 1) e = arguments[a];
            t = e.shift(),
            bmak["listFunctions"][t] && bmak["listFunctions"][t]["apply"](bmak["listFunctions"], e)
        }
    };
bmak["sd_debug"]("<init/>");

for (var i = 0; i < _cf.length; i++) bmak["applyFunc"](_cf[i]);

bmak["sd_debug"]("<setSDFN>" + bmak["sdfn"].join() + "</setSDFN>"),
_cf = {
        push: bmak["applyFunc"]
    },

function (a) {
        var t = {};
        // 这里相当于一个赋值。 创建键值对
        a["fpcf"] = t,
        t["sf4"] = function () {
            // 获取 U-A 头   返回的是 false... 出了苹果手机
            var a = bmak["uar"]();
            return !(!~a.indexOf("Version/4.0") || !(~a.indexOf("iPad;") || ~a.indexOf("iPhone") || ~a.indexOf("Mac OS X 10_5")))
        },
        t["fpValstr"] = -1,
        t["fpValCalculated"] = !1,

        t["rVal"] = -1,
        t["rCFP"] = -1,
        t["cache"] = {},
        t["td"] = -999999,
        t["clearCache"] = function () {
            t["cache"] = {}
        },
        t["fpVal"] = function () {
            t["fpValCalculated"] = !0;
            try {
                var a = 0;
                // 一个时间戳。
                a = Date.now ? Date.now() : +new Date;
                var e = t["data"]();
                t["fpValstr"] = e.replace(/\"/g, '\\"');   // 就是一个杠换成两个杠
                var n = 0;
                n = Date.now ? Date.now() : +new Date,
                t["td"] = n - a
            } catch (a) {}
        },
        t["timezoneOffsetKey"] = function () {
            return (new Date).getTimezoneOffset()
            // -480  固定值
        },
        t["data"] = function () {
            var a = 24,
                e = 24,
                n = true,
                o = false,
                m = -1,
                r = 'default';
            return r = !0 ? !1 ? t['fonts_optm']() : t['fonts']() : 'dis',
            [t['canvas'](), r, t['pluginInfo'](), t['sessionStorageKey'](), t['localStorageKey'](), t['indexedDbKey'](), t["timezoneOffsetKey"](), t['webrtcKey'](), a, e, n, o, m].join(';')
        },
        t['PLUGINS'] = ['WebEx64 General Plugin Container', 'YouTube Plug-in', 'Java Applet Plug-in', 'Shockwave Flash', 'iPhotoPhotocast', 'SharePoint Browser Plug-in', 'Chrome Remote Desktop Viewer', 'Chrome PDF Viewer', 'Native Client', 'Unity Player', 'WebKit-integrierte PDF', 'QuickTime Plug-in', 'RealPlayer Version Plugin', 'RealPlayer(tm) G2 LiveConnect-Enabled Plug-In (32-bit)', 'Mozilla Default Plug-in', 'Adobe Acrobat', 'AdobeAAMDetect', 'Google Earth Plug-in', 'Java Plug-in 2 for NPAPI Browsers', 'Widevine Content Decryption Module', 'Microsoft Office Live Plug-in', 'Windows Media Player Plug-in Dynamic Link Library', 'Google Talk Plugin Video Renderer', 'Edge PDF Viewer', 'Shockwave for Director', 'Default Browser Helper', 'Silverlight Plug-In'],
        t['pluginInfo'] = function () {
            if (void 0 === navigator.plugins) return null;
            for (var a = t['PLUGINS'].length, e = '', n = 0; n < a; n++) {
                var o = t['PLUGINS'][n];
                void 0 !== navigator.plugins.o && (e = e + "," + n)
            }
            return e
            // 像 ",".json(li)
        },
        // 假设 是 -1
        t['canvas'] = function () {
            try {
                // 不为空的情况下 直接返回
                if (void 0 !== t["cache"]['canvas']) return t["cache"]['canvas'];
                var a = -1;
                // ！false
                if (!t["sf4"]()) {
                    var e = "<canvas>";
                    if (e['width'] = 280, e['height'] = 60, e['style']['display'] = 'none', 'function' == typeof e['getContext']) {
                        var n = e['getContext']('2d');
                        n['fillStyle'] = 'rgb(102, 204, 0)',
                        n['fillRect'](100, 5, 80, 50),
                        n['fillStyle'] = '#f60',
                        n['font'] = '16pt Arial',
                        n['fillText']('<@nv45\. F1n63r,Pr1n71n6!', 10, 40),
                        n['strokeStyle'] = 'rgb(120, 186, 176)',
                        n['arc'](80, 10, 20, 0, Math['PI'], !1),
                        n['stroke']();
                        var o = e.toDataURL();

                        a = 0;
                        for (var m = 0; m < o.length; m++) {
                            a = (a << 5) - a + o['charCodeAt'](m),
                            a &= a
                        }
                        a = a.toString();
                        var r = document['createElement']('canvas');
                        r['width'] = 16,
                        r['height'] = 16;
                        var i = r['getContext']('2d');
                        i['font'] = '6pt Arial',
                        t["rVal"] = Math['floor'](1e3 * Math['random']())['toString'](),
                        i['fillText'](t["rVal"], 1, 12);
                        for (var c = r['toDataURL'](), b = 0, d = 0; d < c.length; d++) {
                            b = (b << 5) - b + c['charCodeAt'](d),
                            b &= b
                        }
                        t["rCFP"] = b['toString']()
                    }
                }
                return a
            } catch (a) {
                return 'exception'
            }
        },
        t['fonts_optm'] = function () {
            var a = 200,
                // 一个时间戳
                e = bmak["get_cf_date"](),
                n = [];
            if (!t["sf4"]()) {
                    var o = ['sans-serif', 'monospace'],
                        m = [0, 0],
                        r = [0, 0],
                        i = document['createElement']('div');
                    i['style']['cssText'] = 'position: relative; left: -9999px; visibility: hidden; display: block !important';
                    var c;
                    for (c = 0; c < o.length; c++) {
                            var b = document['createElement']('span');
                            b['innerHTML'] = 'abcdefhijklmnopqrstuvxyz1234567890;+-.',
                            b['style']['fontSize'] = '90px',
                            b['style']['fontFamily'] = o[c],
                            i['appendChild'](b)
                        }
                    for (document['body']['appendChild'](i), c = 0; c < i['childNodes'].length; c++) b = i['childNodes'][c],
                    m[c] = b['offsetWidth'],
                    r[c] = b['offsetHeight'];
                    if (document['body']['removeChild'](i), bmak["get_cf_date"]() - e > a) return '';
                    var d = ['Geneva', 'Lobster', 'New York', 'Century', 'Apple Gothic', 'Minion Pro', 'Apple LiGothic', 'Century Gothic', 'Monaco', 'Lato', 'Fantasque Sans Mono', 'Adobe Braille', 'Cambria', 'Futura', 'Bell MT', 'Courier', 'Courier New', 'Calibri', 'Avenir Next', 'Birch Std', 'Palatino', 'Ubuntu Regular', 'Oswald', 'Batang', 'Ubuntu Medium', 'Cantarell', 'Droid Serif', 'Roboto', 'Helvetica Neue', 'Corsiva Hebrew', 'Adobe Hebrew', 'TI-Nspire', 'Comic Neue', 'Noto', 'AlNile', 'Palatino-Bold', 'ArialHebrew-Light', 'Avenir', 'Papyrus', 'Open Sans', 'Times', 'Quicksand', 'Source Sans Pro', 'Damascus', 'Microsoft Sans Serif'],
                        k = document['createElement']('div');
                    k['style']['cssText'] = 'position: relative; left: -9999px; visibility: hidden; display: block !important';
                    for (var s = [], l = 0; l < d.length; l++) {
                            var u = document['createElement']('div');
                            for (c = 0; c < o.length; c++) {
                                var b = document['createElement']('span');
                                b['innerHTML'] = 'abcdefhijklmnopqrstuvxyz1234567890;+-.',
                                b['style']['fontSize'] = '90px',
                                b['style']['fontFamily'] = d[l] + "," + o[c],
                                u['appendChild'](b)
                            }
                            k['appendChild'](u)
                        }
                    if (bmak["get_cf_date"]() - e > a) return '';
                    document['body']['appendChild'](k);
                    for (var l = 0; l < k['childNodes'].length; l++) {
                            var _ = !1,
                                u = k['childNodes'][l];
                            for (c = 0; c < u['childNodes'].length; c++) {
                                    var b = u['childNodes'][c];
                                    if (b['offsetWidth'] !== m[c] || b['offsetHeight'] !== r[c]) {
                                        _ = !0;
                                        break
                                    }
                                }
                            if (_ && s['push'](l), bmak["get_cf_date"]() - e > a) break
                        }
                    document['body']['removeChild'](k),
                    n = s['sort']()
                }
            return n.join(",")
        },
        t['fonts'] = function () {
            var a = [];
            if (!t["sf4"]()) {
                var e = ['serif', 'sans-serif', 'monospace'],
                    n = [0, 0, 0],
                    o = [0, 0, 0],
                    m = "<span></span>";
                m['innerHTML'] = 'abcdefhijklmnopqrstuvxyz1234567890;+-.',
                // m['style']['fontSize'] = '90px';
                var r;
                for (r = 0; r < e.length; r++) m['style']['fontFamily'] = e[r],
                document['body']['appendChild'](m),
                n[r] = m['offsetWidth'],
                o[r] = m['offsetHeight'],
                document['body']['removeChild'](m);
                for (var i = ['Geneva', 'Lobster', 'New York', 'Century', 'Apple Gothic', 'Minion Pro', 'Apple LiGothic', 'Century Gothic', 'Monaco', 'Lato', 'Fantasque Sans Mono', 'Adobe Braille', 'Cambria', 'Futura', 'Bell MT', 'Courier', 'Courier New', 'Calibri', 'Avenir Next', 'Birch Std', 'Palatino', 'Ubuntu Regular', 'Oswald', 'Batang', 'Ubuntu Medium', 'Cantarell', 'Droid Serif', 'Roboto', 'Helvetica Neue', 'Corsiva Hebrew', 'Adobe Hebrew', 'TI-Nspire', 'Comic Neue', 'Noto', 'AlNile', 'Palatino-Bold', 'ArialHebrew-Light', 'Avenir', 'Papyrus', 'Open Sans', 'Times', 'Quicksand', 'Source Sans Pro', 'Damascus', 'Microsoft Sans Serif'], c = [], b = 0; b < i.length; b++) {
                        var d = !1;
                        for (r = 0; r < e.length; r++) if (m['style']['fontFamily'] = i[b] + "," + e[r], document['body']['appendChild'](m), m['offsetWidth'] === n[r] && m['offsetHeight'] === o[r] || (d = !0), document['body']['removeChild'](m), d) {
                            c['push'](b);
                            break
                        }
                    }
                a = c['sort']()
            }
            return a.join(",")
        },
            // true
        t['webrtcKey'] = function () {
            return 'function' == typeof window['RTCPeerConnection'] || 'function' == typeof window['mozRTCPeerConnection'] || 'function' == typeof window['webkitRTCPeerConnection']
        },
        // true
        t['indexedDbKey'] = function () {
            return !!t['hasIndexedDB']()
        },
            // true  //false
        t['sessionStorageKey'] = function () {
            return !!t['hasSessionStorage']()
        },
            // true  //false
        t['localStorageKey'] = function () {
            return !!t['hasLocalStorage']()
        },
            // true 或 false
        t['hasSessionStorage'] = function () {
            try {
                return !!window['sessionStorage']
            } catch (a) {
                return !1
            }
        },
            // true 或 false
        t['hasLocalStorage'] = function () {
            try {
                return !!window['localStorage']
            } catch (a) {
                return !1
            }
        },
            // true
        t['hasIndexedDB'] = function () {
            return !!window['indexedDB']
        }
    }(bmak);
try {
        // _abck &&
        bmak["ckie"] && bmak["get_cookie"]()
    } catch (a) {}
try {
        // bmak 添加上一堆键值对
        bmak['ir'](),
            // 等于一个时间戳
        bmak['t_tst'] = bmak["get_cf_date"](),
        // 开启定位
        bmak['startTracking'](),
            // 时间间隔
        bmak['tst'] = bmak["get_cf_date"]() - bmak['t_tst'],
            // 0 ||
        bmak['disFpCalOnTimeout'] || setTimeout(bmak["fpcf"]["fpVal"], 100);
        for (var i = 0; i < 3; i++) setTimeout(bmak['getmr'], 400 + 5e3 * i);
        setTimeout(bmak['mn_init'], 1e3)
    } catch (a) {}

```

由于该文章字数太多了，csdn 好卡，分两个章节讲述吧。好卡卡卡卡卡卡… 请看下一篇详细解密把

<link href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/editerView/markdown_views-89f5acb30b.css" rel="stylesheet"> <link href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/style-49037e4d27.css" rel="stylesheet">