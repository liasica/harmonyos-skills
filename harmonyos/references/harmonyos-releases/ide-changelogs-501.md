---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-501
title: 变更说明
breadcrumb: 版本说明 > 更多版本 > 历史版本 > 5.0.1(13) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:1a70361498dea4c9c7b9bf1fab416063c9c8336bd1649683d0ca2588686fd663
---

## 5.0.5.200至5.0.5.300

### 编译构建对卡片引用HSP增加校验

升级到DevEco Studio 5.0.1 Release（5.0.5.300）及以上版本，Form卡片直接或间接引用HSP的场景，编译构建会报错。

**变更影响**

如果历史工程使用了Form卡片并且在卡片页面文件（form\_config.json文件src字段对应的值）中直接或间接引用了HSP模块，则编译会报错，并提示相关文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ScP5E3oQQEW48Ek9gvvx9Q/zh-cn_image_0000002300332792.png?HW-CC-KV=V1&HW-CC-Date=20261112T233241Z&HW-CC-Expire=31536000000&HW-CC-Sign=4BF4E657F2EEA9C201D5969A3B79A932BA0A3E5DF6E6DC2CD2AA5D149E97497D "点击放大")

**适配指导**

根据报错提示的信息，找到直接或间接引用HSP的卡片文件，将对应的HSP模块移除，并修改为引用HAR模块的方式。
