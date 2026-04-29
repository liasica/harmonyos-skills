---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-7
title: 命令行方式执行Instrument Test堆栈路径打印错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > 命令行方式执行Instrument Test堆栈路径打印错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5050b852d55e8bac3ffe077a6cc07cfc51c4af537126f78d4121157276221d67
---

**问题现象**

在5.0.3.400版本下，通过命令行执行Instrument Test，堆栈信息中的文件路径和位置有误，出现“|”而不是“/”，升级到5.0.3.401及以上版本仍然有误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/EyBpI74aTAynCMpGkpPoQg/zh-cn_image_0000002194158620.png?HW-CC-KV=V1&HW-CC-Date=20260429T062135Z&HW-CC-Expire=86400&HW-CC-Sign=6C2AA992DAE4E6FEC946EA4F4BF83CAD31EE86787E006A2D2E1455F7BA9F7CEE "点击放大")

**原因**

在5.0.3.400版本下生成的.test文件和build文件夹未被同时删除，需要手动删除。

**解决措施**

删除5.0.3.400版本下生成的.test文件和build文件夹，然后重新执行测试用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/wX_KCHSTTtaJwck3EylV9g/zh-cn_image_0000002194318232.png?HW-CC-KV=V1&HW-CC-Date=20260429T062135Z&HW-CC-Expire=86400&HW-CC-Sign=7B06F8B2E0DBDB0857150B649E18EC9E5FB2A02DA9B74A1C1F620B00AF57E66B "点击放大")
