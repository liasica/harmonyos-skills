---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-15
title: 如何在模拟器访问Mac本地HTTP服务
breadcrumb: FAQ > DevEco Studio > 应用运行 > 如何在模拟器访问Mac本地HTTP服务
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:45053945b641a380f38e34677c92c3f7e5aabd229003a5cf4879f1ef1bd2d71d
---

可以通过hdc shell ip -r查看映射到PC的IP地址，该地址为 10.0.2.2。

在请求HTTP的URL中，将IP地址替换为10.0.2.2。例如，Mac上的HTTP URL为http://127.0.0.1:8088/api/userinfo，替换后的URL为http://10.0.2.2:8088/api/userinfo。
