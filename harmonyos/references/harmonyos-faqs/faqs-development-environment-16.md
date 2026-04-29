---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-16
title: 运行时出现Import DevEco Studio Settings弹窗
breadcrumb: FAQ > DevEco Studio > 环境准备 > 运行时出现Import DevEco Studio Settings弹窗
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:90b5c7a571e41c295aa6f8ef560363f3e4018310a0e87d6670fad4a9edd8247b
---

**问题现象**

问题出现包含两种场景：

场景一：首次运行DevEco Studio时，出现**Import DevEco Studio Settings**弹窗。

场景二：本地清理DevEco Studio缓存后再次下载安装运行时，可能出现**Import DevEco Studio Settings**弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/vSTAc7RLTdWQxBYq4vXuuQ/zh-cn_image_0000002474225988.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=F34043C761DA92E319BDF72B6FCE1643A644839B642A0A0DE7A7B82165AA4FCF)

**解决措施**

方案一：建议保持默认勾选项**Do not import settings**。

方案二：勾选**Config or installation directory**，上传配置项压缩包（settings.zip）。

说明

* 点击**File** > **Manage IDE Settings** > **Export Settings**...将包含Ark插件等配置项导出，再次运行时可以将配置项直接导入。
* DevEco Studio版本不同，支持导出的配置项不同。可导出的配置项需以具体版本为准。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/VF9pM_nIRBCHugI6DchE2Q/zh-cn_image_0000002509067411.png?HW-CC-KV=V1&HW-CC-Date=20260429T062007Z&HW-CC-Expire=86400&HW-CC-Sign=A126F3B8FFCA71D8576B2CDEA9DEEB53CD26831BB1A364A3FD85D8FAEDE4407F)
