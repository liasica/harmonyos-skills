---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6
title: 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
category: harmonyos-guides
scraped_at: 2026-10-22T07:05:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d88ea66e465345e22294adc1284d061e570d730d479591c99ecdc6fd6d5f0e84
---

**问题现象**

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/at5a5YkGTRW_zc705fhWCQ/zh-cn_image_0000002768021376.png)
* upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/rxge_Bf1RoaadFui3udRTg/zh-cn_image_0000002767861394.png)

**解决措施**

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
