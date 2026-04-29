---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-58
title: 如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:28+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c593a3daad87dd83d752541a3872aafefe82f795fe59727ab3721bf8f5af9369
---

如果需要在运行后保留存储在Preferences中的用户信息，可以在DevEco Studio中进行如下设置：点击“Run”->“Edit Configurations...”，进入“Debug Configurations”->“General”->“Installation Options”，勾选“Keep Application Data”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/uA4SzWgHTPSB6vlL9kVR5w/zh-cn_image_0000002229758741.png?HW-CC-KV=V1&HW-CC-Date=20260429T062127Z&HW-CC-Expire=86400&HW-CC-Sign=F7B2E066700211E0E06991499FF34771251F4DF4D2CD798C10362DD3940DA3B5)
