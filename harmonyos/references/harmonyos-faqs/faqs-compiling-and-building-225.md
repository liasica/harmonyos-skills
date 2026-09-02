---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-225
title: build-profile.json5中配置useNormalizedOHMUrl为true常见报错问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > build-profile.json5中配置useNormalizedOHMUrl为true常见报错问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:614d0841aeae96b16950960855069f9b58acae64b352f03f9737e2ac715fbb71
---

## 问题现象

* 场景一：编译报错：

  Failed to resolve OhmUrl. Failed to get a resolved OhmUrl for hvigor\_ignore\_xxxxx imported by XXX.
* 场景二：编译报错：

  The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match.
* 场景三：编译报错：

  ohpm ERROR: local dependency xxx found in "oh-package.json5" does not match the actual name xxx of its oh-package.json5.

  ohpm ERROR: Install failed, detail: There are some dependency names that are inconsistent with the actual package names.
* 场景四：编译报错：

  ERROR: 00309001 ArkTS Compiler Error.

  Error Message: Cannot import files outside of the current module using relative paths.
* 场景五：编译报错：

  Bytecode HARs:xxx库名 not supported when useNormalizedOHMUrl is not true.

## 背景知识

在工程级build-profile.json5文件中，[strictMode](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)用于定义严格模式，含有useNormalizedOHMUrl、caseSensitiveCheck等配置字段。

* useNormalizedOHMUrl：布尔值类型，选择是否使用标准化的OHMUrl格式，标准化的OHMUrl统一了原有OHMUrl的格式，使用集成态HSP和字节码HAR需使用标准化的OHMUrl格式。
* caseSensitiveCheck：布尔值类型，选择导入文件是否严格校验大小写，支持相对路径和软链接。

## 解决方案

* 场景一：

  参考官方文档：[编译报错“Failed to get a resolved OhmUrl by filepath xx”](../harmonyos-guides/ide-hvigor-faqs.md#section16345217154214)中的场景五。
* 场景二：

  参考官方文档：[编译报错“The useNormalizedOHMUrl settings of packages xxx and the project useNormalizedOHMUrl: xxx do not match”](../harmonyos-guides/ide-hvigor-faqs.md#section1585241711814)。
* 场景三：

  从DevEco Studio NEXT Beta1（5.0.3.800）版本开始，当useNormalizedOHMUrl设置为true时，不允许通过相对路径跨模块或绝对路径导入文件，oh-package.json5中依赖的包使用的别名需要和依赖包的oh-package.json5的name保持一致，具体的适配指导请参考[变更说明](../harmonyos-releases/ide-changelog-500-release.md#section1130320228353)。
* 场景四：

  同场景三。
* 场景五：

  使用集成态HSP和字节码HAR需使用标准化的OHMUrl格式，需要将useNormalizedOHMUrl配置为true。
