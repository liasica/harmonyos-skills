---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6
title: 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c8ebe9eb3d375404084d69d765011687892944841b2cdd8a97a503da1797b3cb
---

**问题现象**

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/AX3CjscRTEOAM6-nsjpgCA/zh-cn_image_0000002552799230.png?HW-CC-KV=V1&HW-CC-Date=20260427T234848Z&HW-CC-Expire=86400&HW-CC-Sign=C5E29644B705023D69338FEEB1BABCBC4E960A5FBED30A97B026E63FD554DA33)
* upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Xu2eUkRFR-C_PhIWImlf7g/zh-cn_image_0000002583438925.png?HW-CC-KV=V1&HW-CC-Date=20260427T234848Z&HW-CC-Expire=86400&HW-CC-Sign=7B139036182E4AE7D080CF0F30F62A59C4C3FE976082488A9FE6F7EECBBCBCA7)

**解决措施**

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
