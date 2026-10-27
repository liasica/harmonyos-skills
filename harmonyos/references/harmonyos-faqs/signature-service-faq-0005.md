---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/signature-service-faq-0005
title: DevEco Studio华为账号登录异常问题排查
breadcrumb: FAQ > DevEco Studio > 签名服务 > 常见问题 > DevEco Studio华为账号登录异常问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:47334cccf83afb4d2ccc37127715c196862d9c349f04d2213a56c7a6bcb57b5c
---

**Q：使用浏览器登录华为账号并点击“允许”按钮后，浏览器将跳转至http://localhost:10101/xxx，显示“无法访问此网站”。**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/F4j8jgFXTESJDEuXW31hNA/zh-cn_image_0000002802224681.png "点击放大")

**A**：出现该问题的原因是登录授权过程中，DevEco Studio与华为账号之间的登录通道异常。具体原因包括点击了DevEco Studio登录界面的Cancel按钮，或者DevEco Studio在登录过程中异常关闭。

请尝试重新登录；建议在登录过程中不要做其它操作，避免误操作。如果重新登录还是出现该界面，请根据[浏览器点击“允许”按钮后，出现登录客户端失败提示](faqs-signature-service-5.md)解决措施，检查和设置DevEco Studio的HTTP Proxy后进行重试。
