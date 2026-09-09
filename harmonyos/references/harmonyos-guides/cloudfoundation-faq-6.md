---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6
title: 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3e627618bee314dd84d2a605a572d24352c51539bb417cb41a587f1cb4296d8a
---

**问题现象**

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/D9iMfjbcRi25XDBgnwO99A/zh-cn_image_0000002747211619.png)
* upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/fTf4rwCkQM2muxbmDeVaRg/zh-cn_image_0000002717611752.png)

**解决措施**

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
