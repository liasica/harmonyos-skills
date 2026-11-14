---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-4
title: 运行应用时报“XXX Read timed out”异常
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 预加载 > 运行应用时报“XXX Read timed out”异常
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:16+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:368d7bfe9c1f374ebc58e16564c784122a01c003f6429b12cdc313df0ab7304d
---

**问题现象**

运行应用时报“XXX Read timed out”异常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/as8uvPyfQayk8When09NhA/zh-cn_image_0000002788467950.png?HW-CC-KV=V1&HW-CC-Date=20261114T004633Z&HW-CC-Expire=31536000000&HW-CC-Sign=1ADD1FE85B752E716D5A2EA68C842074D0208D41D0A70DA8B42DDA5B9E0DF26A)

**解决措施**

出现此错误，是因为云侧没有启动云函数实例，卸载应用重新安装即可。
