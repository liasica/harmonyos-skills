---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-11
title: 签名时，提示"Failed to query agreement signing records"
breadcrumb: FAQ > DevEco Studio > 签名服务 > 签名时，提示"Failed to query agreement signing records"
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:ae549ade6a982ca78aa0078742dd88859303d86bc75e2294bd9ee1b5773efce9
---

**问题现象**

使用未实名认证的华为账号登录会导致签名错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/h3k9QKAmSXKVxpf2uJXJPQ/zh-cn_image_0000002654838047.png)

**解决措施**

出现该问题的原因是签名过程中，DevEco Studio与查询协议的连接通道发生异常

请尝试以下两种方法解决此问题

方式一：该问题可能是由于DevEco Studio的HTTP代理问题引起的，请参考[配置代理](../harmonyos-guides/ide-environment-config.md)。

方式二：进行开发者实名认证，具体指导可以参考[实名认证介绍](../app/hdc-verification-introduction-0000002752607793.md)。
