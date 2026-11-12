---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6
title: 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:80bfd4585799b8edbe5752f5c47e5a1ecdd505a2cab54f27c10b55fab8527fdd
---

**问题现象**

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/3Iu405UwT5y4jKtLNoOUOQ/zh-cn_image_0000002815399775.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=874633E852B4855DECBCB222F3B0F882164D9F846A0CA0D460C9E4B13CCEF980)
* upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/OgcVrtV5TM6zjVwhBP1ktg/zh-cn_image_0000002786360272.png?HW-CC-KV=V1&HW-CC-Date=20261112T233229Z&HW-CC-Expire=31536000000&HW-CC-Sign=9967168521D96E8E6FAED3D02BDC785BFC616FFBAFD44BE4BE5311DD4AC9A9E2)

**解决措施**

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
