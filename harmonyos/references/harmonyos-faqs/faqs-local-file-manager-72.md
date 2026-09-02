---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-72
title: 关系型数据库文件如何清理
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 关系型数据库文件如何清理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:c9354ea1a370dd0d1fd707f3bba28ad445295f5ecf0f5f3c9df47ede9fcacaa9
---

## 问题现象

使用关系型数据库提供的API删除数据库，并没有完全删除建库时生成的文件夹和文件，如何彻底删除？

调用deleteRdbStore删除后的文件夹结构如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/4DnlC8BeRCCYf_EKRfGQ2Q/zh-cn_image_0000002628899110.png)

## 背景知识

* [relationalStore.getRdbStore](../harmonyos-references/arkts-apis-data-relationalstore-f.md#relationalstoregetrdbstore)：创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用Promise异步回调。系统会根据配置创建关系型数据库文件目录，如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/cD6i0lZRTcWhCg88nlnbvg/zh-cn_image_0000002659138379.png)
* [relationalStore.deleteRdbStore](../harmonyos-references/arkts-apis-data-relationalstore-f.md#relationalstoredeleterdbstore10-1)：使用指定的数据库文件配置删除数据库，使用Promise异步回调。
* 关系型数据库目录："/data/app/el2/100/database/(bundleName)/entry/rdb/"，参考：[获取应用文件路径](../harmonyos-guides/application-context-stage.md#获取应用文件路径)。

## 解决方案

使用[@ohos.file.fs (文件管理)](../harmonyos-references/js-apis-file-fs.md)的功能进行文件夹/文件删除。步骤如下：

1. 使用[fs.listFileSync](../harmonyos-references/js-apis-file-fs.md#fileiolistfilesync)获取关系型数据库文件目录(context.databaseDir)下的文件夹/文件。
2. 使用[isDirectory](../harmonyos-references/js-apis-file-fs.md#isdirectory)判断获取到的是目录还是文件，使用[fs.rmdirSync](../harmonyos-references/js-apis-file-fs.md#fileiormdirsync)删除目录、使用[fs.unlinkSync](../harmonyos-references/js-apis-file-fs.md#fileiounlinksync)删除文件。
