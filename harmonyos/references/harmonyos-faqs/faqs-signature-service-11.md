---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-11
title: 签名时，提示"Failed to query agreement signing records"
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名时，提示"Failed to query agreement signing records"
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f0c4c3b3934aa2365ba7bb5ac2b8ecaf9b4b0900f44258d5e1be37b3032e50bb
---

**问题现象**

使用未实名认证的华为账号登录会导致签名错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/a9OJaS4yTceURD3j4_ppAA/zh-cn_image_0000002654838047.png)

**解决措施**

出现该问题的原因是签名过程中，DevEco Studio与查询协议的连接通道发生异常

请尝试以下两种方法解决此问题

方式一：该问题可能是由于DevEco Studio的HTTP代理问题引起的，请参考[配置代理](../harmonyos-guides/ide-environment-config.md)。

方式二：进行开发者实名认证，具体指导可以参考[实名认证介绍](../start/itrna-0000001076878172.md)。
