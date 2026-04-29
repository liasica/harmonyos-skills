---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-4
title: 浏览器点击“允许”按钮后，出现登录客户端失败提示
breadcrumb: FAQ > DevEco Studio > 签名服务 > 浏览器点击“允许”按钮后，出现登录客户端失败提示
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7cd0eb05430281bd3b193f1187e3f2726281ba1d2f3598c2be676e7d50ada3c8
---

**问题现象**

使用实名认证的华为账号登录后，点击“允许”按钮进行授权。如果浏览器提示“登录HUAWEI DevEco Studio客户端失败”，请检查网络连接或重新尝试登录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/fBJIClKLRb2-_SR8guuvpQ/zh-cn_image_0000002229604393.png?HW-CC-KV=V1&HW-CC-Date=20260429T062107Z&HW-CC-Expire=86400&HW-CC-Sign=52E12F7605931D382A5F27DC29D91A33E2BFBB2ECCEF13C21B85D9387181391B "点击放大")

**解决措施**

该问题由DevEco Studio的HTTP代理问题引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/Yp79d53sTY6KPRWba0rYGw/zh-cn_image_0000002194318608.png?HW-CC-KV=V1&HW-CC-Date=20260429T062107Z&HW-CC-Expire=86400&HW-CC-Sign=10DE4F10008F31F21372351C78030DEEA53BE7578D820B7A74F9057BB1E05986 "点击放大")

1. 检查HTTP Proxy设置。
   * 如果网络无需代理即可访问Internet，设置代理会影响模拟器的登录授权。请检查并确保HTTP Proxy设置为“No proxy”。
   * 如果您的网络需要代理访问Internet，未设置代理会影响模拟器的登录授权，请检查并将HTTP Proxy设置为“Manual proxy configuration”，设置方法可参考[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)。
2. 在DevEco Studio界面，点击**Cancel**按钮，重新登录授权。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Hn4rkwA8RKKMBZhVnTmyGQ/zh-cn_image_0000002229758881.png?HW-CC-KV=V1&HW-CC-Date=20260429T062107Z&HW-CC-Expire=86400&HW-CC-Sign=951B493FAA1E38030CEE52554DBBB08FD1932D7EACD4A1FBFB16754CEA4C0213)
