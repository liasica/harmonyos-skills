---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6
title: 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fab76daaffc74cd176b848be50fdca7b3ed2482010e0af826ef3349ee12ea41d
---

**问题现象**

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/yIMix5OeS4WRFAVNghRfmA/zh-cn_image_0000002793037956.png?HW-CC-KV=V1&HW-CC-Date=20261121T011222Z&HW-CC-Expire=31536000000&HW-CC-Sign=AEF1A4E067848AA28B3BF1299F01B88B7752CF35E4B56C0539C6CBBF26EEADAC)
* upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/-JqKMRDqRUmtwaQX3kC0rw/zh-cn_image_0000002821837893.png?HW-CC-KV=V1&HW-CC-Date=20261121T011222Z&HW-CC-Expire=31536000000&HW-CC-Sign=89D37E57B99056B8D9CC27C580A14C7C2D6477C3DAA181ACA6851979075CBDB8)

**解决措施**

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
