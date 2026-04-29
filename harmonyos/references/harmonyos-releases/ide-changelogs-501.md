---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-501
title: 变更说明
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.1(13) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-04-29T13:24:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e14c98ecf4b656dbb73ddbc8c305104352baa7ec2b01590b689f98d0070cef71
---

## 5.0.5.200至5.0.5.300

### 编译构建对卡片引用HSP增加校验

升级到DevEco Studio 5.0.1 Release（5.0.5.300）及以上版本，Form卡片直接或间接引用HSP的场景，编译构建会报错。

**变更影响**

如果历史工程使用了Form卡片并且在卡片页面文件（form\_config.json文件src字段对应的值）中直接或间接引用了HSP模块，则编译会报错，并提示相关文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/hFXCHZe5RSqeu-97jsloDQ/zh-cn_image_0000002300332792.png?HW-CC-KV=V1&HW-CC-Date=20260429T052402Z&HW-CC-Expire=86400&HW-CC-Sign=84A79E2149DCA3D1D51F7C77337BBA5465F47AFB66CA5AE6EE1B235D4F6ED68D "点击放大")

**适配指导**

根据报错提示的信息，找到直接或间接引用HSP的卡片文件，将对应的HSP模块移除，并修改为引用HAR模块的方式。
