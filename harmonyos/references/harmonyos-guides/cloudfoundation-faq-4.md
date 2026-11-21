---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-4
title: 运行应用时报“XXX Read timed out”异常
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 运行应用时报“XXX Read timed out”异常
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:541de84e4db70c7775aa02f6f03950efd1ba40d0f512957aef57f8f8993205a4
---

**问题现象**

运行应用时报“XXX Read timed out”异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/aFf7FgAHS_SAQbL_KLmd1w/zh-cn_image_0000002821757897.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E71B9D1FA379BDDF0275C23A1691ED35BFF1E2E3366F0112240AC10A7B6345E)

**解决措施**

出现此错误，是因为云侧没有启动云函数实例，卸载应用重新安装即可。
