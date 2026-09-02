---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-45
title: 调用Comments API返回错误码20770002
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 调用Comments API返回错误码20770002
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c98e829349a0d603ae0dd36426ca3ec697f322386764bf11444a53a9b263d7f3
---

## 问题现象

在调用Comments API的[查询应用评论列表](../AppGallery-connect-References/agcapi-comapi-getreviews-harmonyos-0000002470893976.md)结果返回了以下错误信息，创建API客户端使用的是团队主账号。

```json
{
    "code": 20770002,
    "msg": "uid no white list permission"
}
```

## 解决方案

该错误信息显示用户没有白名单权限，Comments API下的所有API接口依赖于Marketing API，需要先参考[Marketing API](../promotion/bp-functions-marketing_api-0000001435633681.md)，开通权限后即可使用。
