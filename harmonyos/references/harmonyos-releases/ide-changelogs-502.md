---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-502
title: 变更说明
breadcrumb: 版本说明 > 更多版本 > 历史版本 > 5.0.2(14) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-10-09T08:12:34+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:2fcd1608cbd247c74fd2876d52eeff04d2b6f2412426c1a5c32f04e4c74ff21d
---

## 5.0.5.315至5.0.7.100

### 编译构建对签名配置的name字段增加非空字符串校验

升级到DevEco Studio 5.0.2 Beta1（5.0.7.100）及以上版本，工程级build-profile.json5文件中signingConfigs下的name字段不允许为空字符串。

**变更影响**

如果历史工程的工程级build-profile.json5文件中signingConfigs下的name字段为空字符串，编译时会报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/jFWJOPpGQ1ue-c-y2j1uXw/zh-cn_image_0000002336615601.png)

**适配指导**

将signingConfigs下的name字段配置为非空字符串。
