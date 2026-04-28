---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-22
title: 如何获取设备的CPU信息
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何获取设备的CPU信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2fd81d94fed94994599f8877e54a683f6d3f5a627414c542b78048c7ead30963
---

可以通过以下命令来查看CPU信息：

```
1. // 查看CPU信息
2. hdc shell param get const.product.cpu.abilist
```

返回结果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/1uTysY7SROq_f18VG1wKqg/zh-cn_image_0000002229758737.png?HW-CC-KV=V1&HW-CC-Date=20260428T002315Z&HW-CC-Expire=86400&HW-CC-Sign=0B94867A9D4FE913A33F2BFD54B469F98BBB9580399A346C902A8FC5D2741E4D "点击放大")
