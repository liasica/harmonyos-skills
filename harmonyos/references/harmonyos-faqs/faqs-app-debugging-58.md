---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-58
title: 如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:d6569a66167042bb05417c5963603d4f1fc0f50e5d4121424982b34afa924dbb
---

如果需要在运行后保留存储在Preferences中的用户信息，可以在DevEco Studio中进行如下设置：点击“Run”->“Edit Configurations...”，进入“Debug Configurations”->“General”->“Installation Options”，勾选“Keep Application Data”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/8ZSgYmhXRg6MASZzTdzDGQ/zh-cn_image_0000002654798171.png?HW-CC-KV=V1&HW-CC-Date=20261112T233144Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBB80B4C18142948E1F8D79A4A7B91CCEFFE04C8C8A617FB2DD96CA97AD0C065)
