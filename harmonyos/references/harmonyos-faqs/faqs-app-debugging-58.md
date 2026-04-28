---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-58
title: 如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何保证代码修改后每次Run之后Preferences存储的用户信息不会被清除
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ba6b839bb90c7c04c84e7ac99c844401cad733be41705ea25bb456c0efcfee98
---

如果需要在运行后保留存储在Preferences中的用户信息，可以在DevEco Studio中进行如下设置：点击“Run”->“Edit Configurations...”，进入“Debug Configurations”->“General”->“Installation Options”，勾选“Keep Application Data”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/uA4SzWgHTPSB6vlL9kVR5w/zh-cn_image_0000002229758741.png?HW-CC-KV=V1&HW-CC-Date=20260428T003010Z&HW-CC-Expire=86400&HW-CC-Sign=7A018E078D1777FF06142F8DEF4A6BE6BE3113CB1951C68A7496D30A44060360)
