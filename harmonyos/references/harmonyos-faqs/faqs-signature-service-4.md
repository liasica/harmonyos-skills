---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-4
title: 浏览器点击“允许”按钮后，出现登录客户端失败提示
breadcrumb: FAQ > DevEco Studio > 签名服务 > 浏览器点击“允许”按钮后，出现登录客户端失败提示
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:37d2c7ec378d999098c6600c70e6e7f187f367cd3b0a4034c3967769c9ac0f34
---

**问题现象**

使用实名认证的华为账号登录后，点击“允许”按钮进行授权。如果浏览器提示“登录HUAWEI DevEco Studio客户端失败”，请检查网络连接或重新尝试登录。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/fBJIClKLRb2-_SR8guuvpQ/zh-cn_image_0000002229604393.png?HW-CC-KV=V1&HW-CC-Date=20260428T002949Z&HW-CC-Expire=86400&HW-CC-Sign=B47ED0AEE40897391CB9B539D245900316AF42B7F4E6E4DB393AEABA4241721D "点击放大")

**解决措施**

该问题由DevEco Studio的HTTP代理问题引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/Yp79d53sTY6KPRWba0rYGw/zh-cn_image_0000002194318608.png?HW-CC-KV=V1&HW-CC-Date=20260428T002949Z&HW-CC-Expire=86400&HW-CC-Sign=DBFBEBCC787357416D082E7CEC5BBC694621DA377DA27D681D92C59225E35547 "点击放大")

1. 检查HTTP Proxy设置。
   * 如果网络无需代理即可访问Internet，设置代理会影响模拟器的登录授权。请检查并确保HTTP Proxy设置为“No proxy”。
   * 如果您的网络需要代理访问Internet，未设置代理会影响模拟器的登录授权，请检查并将HTTP Proxy设置为“Manual proxy configuration”，设置方法可参考[配置Proxy代理](../harmonyos-guides/ide-environment-config.md#section10369436568)。
2. 在DevEco Studio界面，点击**Cancel**按钮，重新登录授权。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/Hn4rkwA8RKKMBZhVnTmyGQ/zh-cn_image_0000002229758881.png?HW-CC-KV=V1&HW-CC-Date=20260428T002949Z&HW-CC-Expire=86400&HW-CC-Sign=16D24A11CA3153068E0C81782A7635B4C7FBA3F775587C3E7DEFBA54D7E905B4)
