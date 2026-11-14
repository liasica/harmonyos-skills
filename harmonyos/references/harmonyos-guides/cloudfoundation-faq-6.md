---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6
title: 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0185a146d356b72d75f5ab99d422c030b98d488adffe38f771984a9e922db0c0
---

**问题现象**

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/QJDcgmT3TSGeEHbb0ve-bw/zh-cn_image_0000002817507435.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=9B8DF2475214C3D217905B5B35D96FFA12CC6D371B8D4165D5860C46A91398E8)
* upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/FtmTrgMaT8S0H8QNYN7vsQ/zh-cn_image_0000002817427367.png?HW-CC-KV=V1&HW-CC-Date=20261114T004815Z&HW-CC-Expire=31536000000&HW-CC-Sign=68B4223F94D9C7E344F00774705FC4C67578D0B2918CB2E64BFD43B4C7576D33)

**解决措施**

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
