---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/ide-changelogs-502
title: 变更说明
breadcrumb: 版本说明 > 更多版本 > 历史版本 > 5.0.2(14) > DevEco Studio > 变更说明
category: harmonyos-releases
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:f5e48264270169cf226754b3e1a48bf56ec932fc632b800fe2e2b69398151a5f
---

## 5.0.5.315至5.0.7.100

### 编译构建对签名配置的name字段增加非空字符串校验

升级到DevEco Studio 5.0.2 Beta1（5.0.7.100）及以上版本，工程级build-profile.json5文件中signingConfigs下的name字段不允许为空字符串。

**变更影响**

如果历史工程的工程级build-profile.json5文件中signingConfigs下的name字段为空字符串，编译时会报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/bfXhH-B7TmedI_JSxLlj6A/zh-cn_image_0000002336615601.png?HW-CC-KV=V1&HW-CC-Date=20261112T233241Z&HW-CC-Expire=31536000000&HW-CC-Sign=4CDB692078EB1491AA5EEB2BD3DC641D772D9CA3C81E1910B1607E832EC2983B)

**适配指导**

将signingConfigs下的name字段配置为非空字符串。
