---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-7
title: 命令行方式执行Instrument Test堆栈路径打印错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > 命令行方式执行Instrument Test堆栈路径打印错误
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e535830fb9ed80fc4958ab5202a265fd0a8300efe085f3e712a7965f6e2b983c
---

**问题现象**

在5.0.3.400版本下，通过命令行执行Instrument Test，堆栈信息中的文件路径和位置有误，出现“|”而不是“/”，升级到5.0.3.401及以上版本仍然有误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/EyBpI74aTAynCMpGkpPoQg/zh-cn_image_0000002194158620.png?HW-CC-KV=V1&HW-CC-Date=20260428T003017Z&HW-CC-Expire=86400&HW-CC-Sign=DAB31D4ED7326D67611E5C18BC8A7882E5A527C927122FDF186551F954CC8047 "点击放大")

**原因**

在5.0.3.400版本下生成的.test文件和build文件夹未被同时删除，需要手动删除。

**解决措施**

删除5.0.3.400版本下生成的.test文件和build文件夹，然后重新执行测试用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/wX_KCHSTTtaJwck3EylV9g/zh-cn_image_0000002194318232.png?HW-CC-KV=V1&HW-CC-Date=20260428T003017Z&HW-CC-Expire=86400&HW-CC-Sign=F1B123AADB1C68D1506E7AED1AF0026B0507D2DCE3D7891158B28A8D9154E2F1 "点击放大")
