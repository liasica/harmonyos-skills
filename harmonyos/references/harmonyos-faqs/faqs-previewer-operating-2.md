---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-2
title: 预览功能使用过程中，可能无法使用帮助菜单压缩日志按钮收集日志
breadcrumb: FAQ > DevEco Studio > 界面预览 > 预览功能使用过程中，可能无法使用帮助菜单压缩日志按钮收集日志
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:06+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6a123ae24aa4541ecdb7eeec9d14c5bf892bb8b04fe641130c4583a35d64b0b1
---

**问题现象**

当同时预览多个工程时，点击帮助菜单中的“压缩日志”按钮，可能会因日志文件被占用而无法压缩。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/A_hKpDKYRRS7Fpj1W8OJiw/zh-cn_image_0000002229603945.png?HW-CC-KV=V1&HW-CC-Date=20260428T002904Z&HW-CC-Expire=86400&HW-CC-Sign=32D3B47A66A29440BB850FD18F65824C4E988BC07D2124BB4497859651C5443E)

此时右下角会出现压缩失败的提示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/QjPV5E4bShS3gEiRl4wSSw/zh-cn_image_0000002229758417.png?HW-CC-KV=V1&HW-CC-Date=20260428T002904Z&HW-CC-Expire=86400&HW-CC-Sign=A94D960E42FA893EF4C1088E0AC2652FA30AB72F0206A565F1D78BDF79AA1282)

**解决措施**

请关闭预览过的工程，或者重启DevEco Studio后不要打开预览器，即可再次压缩收集日志。
