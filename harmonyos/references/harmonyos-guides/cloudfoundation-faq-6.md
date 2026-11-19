---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6
title: 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:43eda138818844fb92e4ae3cade60add28096d340aeace5154c9997d6f078bcb
---

**问题现象**

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/NmuTnN9uRDqKaIguV4SAQg/zh-cn_image_0000002820526285.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=0182BC329D9B6B19B11971E7E25EC2258BBFF558D44B174158C32BD9776CAED2)
* upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/6ijZhddcRMSovCPUFeHSzw/zh-cn_image_0000002791726306.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=8AEA1A0B1152D13DBF35CEABEDEA4E54CFF01EA818E014CFECA9E88E991ACDF0)

**解决措施**

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
