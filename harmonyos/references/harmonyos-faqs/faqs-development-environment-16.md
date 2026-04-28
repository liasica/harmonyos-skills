---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-16
title: 运行时出现Import DevEco Studio Settings弹窗
breadcrumb: FAQ > DevEco Studio > 环境准备 > 运行时出现Import DevEco Studio Settings弹窗
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:694ca7d84a32ab70fdea21162f1009c37656e00cbd7fcfee29769ff38d48f684
---

**问题现象**

问题出现包含两种场景：

场景一：首次运行DevEco Studio时，出现**Import DevEco Studio Settings**弹窗。

场景二：本地清理DevEco Studio缓存后再次下载安装运行时，可能出现**Import DevEco Studio Settings**弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/vSTAc7RLTdWQxBYq4vXuuQ/zh-cn_image_0000002474225988.png?HW-CC-KV=V1&HW-CC-Date=20260428T002854Z&HW-CC-Expire=86400&HW-CC-Sign=E966EC9BED4B3E13A3A0AA664479B7F938A54818CAEE22913BB4F25F63EE40A1)

**解决措施**

方案一：建议保持默认勾选项**Do not import settings**。

方案二：勾选**Config or installation directory**，上传配置项压缩包（settings.zip）。

说明

* 点击**File** > **Manage IDE Settings** > **Export Settings**...将包含Ark插件等配置项导出，再次运行时可以将配置项直接导入。
* DevEco Studio版本不同，支持导出的配置项不同。可导出的配置项需以具体版本为准。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/VF9pM_nIRBCHugI6DchE2Q/zh-cn_image_0000002509067411.png?HW-CC-KV=V1&HW-CC-Date=20260428T002854Z&HW-CC-Expire=86400&HW-CC-Sign=4EB23923E1D044BC9BA737A78A1D8C6FAD43457D8C72FCF6DFFD896E8ECFFD8F)
