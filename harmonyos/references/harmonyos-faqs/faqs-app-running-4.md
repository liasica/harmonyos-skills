---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-4
title: 在本地模拟器中卸载应用显示成功，但实际未卸载成功
breadcrumb: FAQ > DevEco Studio > 应用运行 > 在本地模拟器中卸载应用显示成功，但实际未卸载成功
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:12+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:43d42a66eba271d7e63c478765f918c7c2d0cb372ef546298bbce87f1d8f1492
---

**问题现象**

通过桌面菜单卸载应用，显示卸载成功，但实际上未卸载。

**解决措施**

出现该问题的原因是模拟器的磁盘空间已满，无法正常卸载应用。在频繁使用 `hdc file send local remote` 命令向模拟器中推送文件后，可能会导致磁盘空间不足。

请尝试以下两种方法解决。

* 方式一：及时删除本地模拟器中不再使用的文件。可以通过hdc shell [COMMAND]命令删除相关文件，更多关于hdc命令使用指导请参考[hdc](../harmonyos-guides/hdc.md)。
* 方式二：删除本地模拟器，然后重新创建。如果使用本地模拟器推送大文件或应用，建议在创建时适当增加模拟器的内部存储空间。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/2rK33YNYTauAYtWCOz6nCQ/zh-cn_image_0000002194318364.png?HW-CC-KV=V1&HW-CC-Date=20260429T062111Z&HW-CC-Expire=86400&HW-CC-Sign=5ABA701D7F954074E75B002926DF892C8547C34819A16FC4EDFA3A31534A1817 "点击放大")
