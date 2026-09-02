---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-6
title: http网络连接中的通用知识
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http网络连接中的通用知识
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:e122039a41a472a364ab0b8ff75eaad366feb36f071054ce5cadc0a532cef18a
---

http请求需要申请ohos.permission.INTERNET权限，其错误码参考文档：[错误码合集](https://curl.se/libcurl/c/libcurl-errors.html)。

常用的请求方式为GET、POST，请求成功时，返回的业务数据在data.result中，cookie信息则在data.cookies中，更改字符集方法为：在请求头head中添加参数为

```json
'Content-Type': "application/json; charset=UTF-8"
```

其请求网页时，如果返回的数据为超长文本内容，console.log无法正确输出。

**参考链接**

[@ohos.net.http (数据请求)](../harmonyos-references/js-apis-http.md)
