---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/version-number-26
title: 版本号格式调整说明
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > 版本号格式调整说明
category: harmonyos-releases
scraped_at: 2026-09-02T14:58:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2eea0582e570ee481dc14d7c6ec13e58789da50c3ac47f0c700425ea06e72dec
---

HarmonyOS开发套件版本号统一采用API版本进行描述。API版本号可在搭载HarmonyOS的设备的设置中查询。

从API版本26.0.0开始，API版本号统一采用[语义化版本（Semantic Versioning，简称SemVer）](https://semver.org/lang/zh-CN/)格式（X.Y.Z），取代原有的格式。这一变更旨在：

* 统一HarmonyOS开发套件版本（API版本）及其底座OpenHarmony的版本号体系。
* 提供更清晰的版本定位，体现主、次版本的概念及升级建议。
* 符合行业标准的语义化版本（SemVer）规范。

**注意** 

API版本号格式变化后，应用中涉及API兼容性判断的代码也需要随之进行优化，详见[应用兼容性说明](app-compatibility.md)。

## 从26.0.0起的语义化版本格式说明

API版本号遵循[语义化版本（Semantic Versioning，简称SemVer）](https://semver.org/lang/zh-CN/)规范，格式为 X.Y.Z。

**格式定义**：

```screen
X.Y.Z
```

**字段说明**：

| 字段 | 说明 |
| --- | --- |
| X：主版本号 | 包含大量的新功能以及重要的变更，变更可能包含对API的修改，需要开发者对已开发的应用进行适配修改。 |
| Y：次版本号 | 包含新功能，原则上向后兼容，但重大安全隐患或关键体验问题可能引入不兼容变更，会在版本说明中提供详细的变更说明指导。 |
| Z：修订版本号 | 问题修复和小改进，保持向后兼容。 |

格式示例：

**说明** 

以下版本号仅为示例，不代表后续的版本规划。

* 26.0.0：首次采用完全语义化的版本。
* 26.0.1：26.0.0的修订版本升级，包含问题修复。
* 26.1.0：26.0.0的次版本升级，包含新功能。
* 27.0.0：主版本升级，包含重大变更。

## 26.0.0之前的版本格式说明

在26.0.0之前，API版本号采用X.Y.Z(N)格式，其中：

* **X**：主版本号，取值1-99，表示API大版本更新。
* **Y**：次版本号，取值0-99，表示API小版本更新。
* **Z**：修订版本号，取值0-99，表示API微小更新。
* **N**：OpenHarmony底座API level，取值1-99。
