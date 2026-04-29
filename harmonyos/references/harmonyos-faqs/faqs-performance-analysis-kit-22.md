---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-22
title: 如何获取设备的CPU信息
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何获取设备的CPU信息
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c94b25570d8aa62f273e9b779fcf2d8ce5d197b5df5404820be76a002818975d
---

可以通过以下命令来查看CPU信息：

```
1. // 查看CPU信息
2. hdc shell param get const.product.cpu.abilist
```

返回结果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/1uTysY7SROq_f18VG1wKqg/zh-cn_image_0000002229758737.png?HW-CC-KV=V1&HW-CC-Date=20260429T061431Z&HW-CC-Expire=86400&HW-CC-Sign=C004AC851251972DBC32A366351869C14335DD1FCDA8DE3C88AEF5FEEA8A01D2 "点击放大")
