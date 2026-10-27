---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-4
title: 浏览器点击“允许”按钮后，出现登录客户端失败提示
breadcrumb: FAQ > DevEco Studio > 签名服务 > 浏览器点击“允许”按钮后，出现登录客户端失败提示
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:2fc7abcefa185073ffcabcb53de938343deaed78538c54c9b98f2735a0508484
---

**问题现象**

使用实名认证的华为账号登录后，点击“允许”按钮进行授权。如果浏览器提示“登录HUAWEI DevEco Studio客户端失败”，请检查网络连接或重新尝试登录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/ebV6HF7NQzOLeOS7zEreUw/zh-cn_image_0000002624478732.png "点击放大")

**解决措施**

该问题由DevEco Studio的HTTP代理问题引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/kU_CkVEbSLOHWeyuU02AaQ/zh-cn_image_0000002654798093.png "点击放大")

1. 检查HTTP Proxy设置。
   * 如果网络无需代理即可访问Internet，设置代理会影响模拟器的登录授权。请检查并确保HTTP Proxy设置为“No proxy”。
   * 如果您的网络需要代理访问Internet，未设置代理会影响模拟器的登录授权，请检查并将HTTP Proxy设置为“Manual proxy configuration”，设置方法可参考[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)。
2. 在DevEco Studio界面，点击**Cancel**按钮，重新登录授权。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/EhJojmJLRg-sbK9XlCujLQ/zh-cn_image_0000002624638642.png)
