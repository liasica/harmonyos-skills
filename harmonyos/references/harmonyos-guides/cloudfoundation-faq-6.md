---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6
title: 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7f550cde58e4e2673fb266eb6dff6e2b4ff703c0fbfaefe7eb48acb642acfc98
---

**问题现象**

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/aB_ssmDrSQCIHS3HLFRKHQ/zh-cn_image_0000002589325249.png?HW-CC-KV=V1&HW-CC-Date=20260429T053754Z&HW-CC-Expire=86400&HW-CC-Sign=871E9DD5C486BD4BB776D90377C356FE66DB5647D0EDB6B4FB2F468A713E57F3)
* upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/3opltu9AQsSGzaMWRt8LrA/zh-cn_image_0000002589245185.png?HW-CC-KV=V1&HW-CC-Date=20260429T053754Z&HW-CC-Expire=86400&HW-CC-Sign=3F9208EAC0D1DFC82A4243F877DEB9120F9281E8F2B4BE37A52BF1B6C26615E6)

**解决措施**

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
