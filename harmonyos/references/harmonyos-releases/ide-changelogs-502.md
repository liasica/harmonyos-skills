---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-502
title: 变更说明
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-04-29T13:23:51+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4a5fb8c1fb7edb7f95a578dd598ab41616ae92cb4ec1fb542cddf4542e673c1f
---

## 5.0.5.315至5.0.7.100

### 编译构建对签名配置的name字段增加非空字符串校验

升级到DevEco Studio 5.0.2 Beta1（5.0.7.100）及以上版本，工程级build-profile.json5文件中signingConfigs下的name字段不允许为空字符串。

**变更影响**

如果历史工程的工程级build-profile.json5文件中signingConfigs下的name字段为空字符串，编译时会报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/q9xMcN28Tiyh7so6Yxvf2g/zh-cn_image_0000002336615601.png)

**适配指导**

将signingConfigs下的name字段配置为非空字符串。
