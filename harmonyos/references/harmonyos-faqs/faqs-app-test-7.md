---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-7
title: 命令行方式执行Instrument Test堆栈路径打印错误
breadcrumb: FAQ > DevEco Studio > 应用测试 > 命令行方式执行Instrument Test堆栈路径打印错误
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:9f13514a72f43c560a0aa226e41e323e48d64eddcc7dfb70c8b03b9d0e4b84d5
---

**问题现象**

在5.0.3.400版本下，通过命令行执行Instrument Test，堆栈信息中的文件路径和位置有误，出现“|”而不是“/”，升级到5.0.3.401及以上版本仍然有误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/lfMWo_lZT-WeGeockYlhWQ/zh-cn_image_0000002654838143.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=E83268F79E6A70A7386A57706480FABE3DF1E3BA97759F2EB67FBA8ED8347DC9 "点击放大")

**原因**

在5.0.3.400版本下生成的.test文件和build文件夹未被同时删除，需要手动删除。

**解决措施**

删除5.0.3.400版本下生成的.test文件和build文件夹，然后重新执行测试用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/GJqiZPQIQeS98L6hlcG_ww/zh-cn_image_0000002624478824.png?HW-CC-KV=V1&HW-CC-Date=20261112T233145Z&HW-CC-Expire=31536000000&HW-CC-Sign=95C1784BEE33F615D927A92B00BD4EEE05E25B15FA61BCC123F45A0DB08AD7CA "点击放大")
