---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-1
title: http网络请求中extraData支持的数据格式有哪些
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http网络请求中extraData支持的数据格式有哪些
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:04+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:69cfaf04533d98a1745afea3a57902ae5abb728601856bad031f45efa406af8a
---

extraData代表发送请求的额外数据，支持如下数据：

* 当http请求为POST、PUT方法时，此字段为http请求的content。
* 当http请求为GET、OPTIONS、DELETE、TRACE、CONNECT方法时，此字段为http请求的参数补充，参数内容会拼接到URL中进行发送。
* 若传入string对象，需自行编码，将编码后的字符串传入。
