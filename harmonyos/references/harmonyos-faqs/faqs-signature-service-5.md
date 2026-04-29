---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-5
title: 点击“允许”后，浏览器提示“无法访问此网站”
breadcrumb: FAQ > DevEco Studio > 签名服务 > 点击“允许”后，浏览器提示“无法访问此网站”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a664a807660feb4a5249369b5019ebae2677fe77f2740ce79bb8a076b53d4d4b
---

**问题现象**

使用浏览器登录华为账号并点击“允许”按钮后，浏览器将跳转至http://localhost:10101/xxx，显示“无法访问此网站”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/-vk_QZpRR9-5huAurJpnqg/zh-cn_image_0000002194318008.png?HW-CC-KV=V1&HW-CC-Date=20260429T062107Z&HW-CC-Expire=86400&HW-CC-Sign=C497A2F25109EF954D60EA2AA3CB0F5F14EC25938E519B361BB88F3DD4C423FE)

**解决措施**

出现该问题的原因是登录授权过程中，DevEco Studio与华为账号之间的登录通道异常。具体原因包括点击了DevEco Studio登录界面的**Cancel**按钮，或者DevEco Studio在登录过程中异常关闭。

请尝试重新登录；建议在登录过程中不要做其它操作，避免误操作。如果重新登录还是出现该界面，请根据[浏览器点击“允许”按钮后，出现登录客户端失败提示](faqs-signature-service-4.md)解决措施，检查和设置DevEco Studio的HTTP Proxy后进行重试。
