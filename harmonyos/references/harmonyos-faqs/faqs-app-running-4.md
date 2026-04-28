---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-4
title: 在本地模拟器中卸载应用显示成功，但实际未卸载成功
breadcrumb: FAQ > DevEco Studio > 应用运行 > 在本地模拟器中卸载应用显示成功，但实际未卸载成功
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:56+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:525eb0a7a409a5aae1ef159de3a0bcf94fd183a992fa8564d496bc4f25419380
---

**问题现象**

通过桌面菜单卸载应用，显示卸载成功，但实际上未卸载。

**解决措施**

出现该问题的原因是模拟器的磁盘空间已满，无法正常卸载应用。在频繁使用 `hdc file send local remote` 命令向模拟器中推送文件后，可能会导致磁盘空间不足。

请尝试以下两种方法解决。

* 方式一：及时删除本地模拟器中不再使用的文件。可以通过hdc shell [COMMAND]命令删除相关文件，更多关于hdc命令使用指导请参考[hdc](../harmonyos-guides/hdc.md)。
* 方式二：删除本地模拟器，然后重新创建。如果使用本地模拟器推送大文件或应用，建议在创建时适当增加模拟器的内部存储空间。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/2rK33YNYTauAYtWCOz6nCQ/zh-cn_image_0000002194318364.png?HW-CC-KV=V1&HW-CC-Date=20260428T002955Z&HW-CC-Expire=86400&HW-CC-Sign=D0015EC3D2CF6C195967EC92A9EACFC28224CA396489E6294FB04A3F4635514F "点击放大")
