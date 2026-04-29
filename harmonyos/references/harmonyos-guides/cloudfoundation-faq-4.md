---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-4
title: 运行应用时报“XXX Read timed out”异常
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 运行应用时报“XXX Read timed out”异常
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:55+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:64d72d625a2dfea8bd1012e576059a8fe6b47adeec756f24e4edbef132889e44
---

**问题现象**

运行应用时报“XXX Read timed out”异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/ptUQOjbvQMWgXPYu9XHZ1A/zh-cn_image_0000002558765382.png?HW-CC-KV=V1&HW-CC-Date=20260429T053755Z&HW-CC-Expire=86400&HW-CC-Sign=3E3E62422DC4E78D601DD05CA416CC9B0B15783F0126F13826997E5174956B22)

**解决措施**

出现此错误，是因为云侧没有启动云函数实例，卸载应用重新安装即可。
