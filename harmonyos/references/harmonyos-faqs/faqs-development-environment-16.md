---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-16
title: 运行时出现Import DevEco Studio Settings弹窗
breadcrumb: FAQ > DevEco Studio > 环境准备 > 运行时出现Import DevEco Studio Settings弹窗
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:31+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:1eff8789ddd125439df65b2453c814a5614034595c95109048564c076c0c4da6
---

**问题现象**

问题出现包含两种场景：

场景一：首次运行DevEco Studio时，出现**Import DevEco Studio Settings**弹窗。

场景二：本地清理DevEco Studio缓存后再次下载安装运行时，可能出现**Import DevEco Studio Settings**弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/i5MUvdhVQPKiuQpoP-9ieA/zh-cn_image_0000002654837727.png)

**解决措施**

方案一：建议保持默认勾选项**Do not import settings**。

方案二：勾选**Config or installation directory**，上传配置项压缩包（settings.zip）。

**说明** 

* 点击**File** > **Manage IDE Settings** > **Export Settings**...将包含Ark插件等配置项导出，再次运行时可以将配置项直接导入。
* DevEco Studio版本不同，支持导出的配置项不同。可导出的配置项需以具体版本为准。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/K3iLdF2nT2WcIdiD2Bd6Vw/zh-cn_image_0000002624478414.png)
