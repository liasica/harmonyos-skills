---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-501
title: 变更说明
breadcrumb: 版本说明 > 更多版本 > 历史版本 > 5.0.1(13) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-09-02T14:58:53+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:273db3d9b85ca77abc84fd1684415596e0771b71f6a76f0f7bc198949a30b30b
---

## 5.0.5.200至5.0.5.300

### 编译构建对卡片引用HSP增加校验

升级到DevEco Studio 5.0.1 Release（5.0.5.300）及以上版本，Form卡片直接或间接引用HSP的场景，编译构建会报错。

**变更影响**

如果历史工程使用了Form卡片并且在卡片页面文件（form\_config.json文件src字段对应的值）中直接或间接引用了HSP模块，则编译会报错，并提示相关文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/ebowgBENRPqRcYEh9rFeAA/zh-cn_image_0000002300332792.png "点击放大")

**适配指导**

根据报错提示的信息，找到直接或间接引用HSP的卡片文件，将对应的HSP模块移除，并修改为引用HAR模块的方式。
