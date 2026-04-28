---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-4
title: 运行应用时报“XXX Read timed out”异常
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 运行应用时报“XXX Read timed out”异常
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fcf2c9642f4059b4e16747e9d1ad98612569bf52627c699c8c5e51b0dbb5c9e8
---

**问题现象**

运行应用时报“XXX Read timed out”异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/kJbTPJ_rSy-hhqzd17ys_g/zh-cn_image_0000002552958882.png?HW-CC-KV=V1&HW-CC-Date=20260427T234851Z&HW-CC-Expire=86400&HW-CC-Sign=17D1706AA99A8CFC042D81AD80CA0DAAE3AE07275C26B1C235F399F2602D9BA0)

**解决措施**

出现此错误，是因为云侧没有启动云函数实例，卸载应用重新安装即可。
