---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-10
title: 上架发布应用失败，提示“请使用发布版本的API开发应用申请上架”
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 上架发布应用失败，提示“请使用发布版本的API开发应用申请上架”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:45+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:814bc22d6fa7a212b7f6794572574c85ac3ccbed9f298415d78fc1f2cd99ae1a
---

## 问题现象

提交应用并上架发布应用被拒，报错信息提示如下：

“请使用发布版本的API开发应用申请上架”。

## 背景知识

完成HarmonyOS应用开发、调试与测试后，您便可以在HarmonyOS 开发者中心正式提交应用上架申请。HarmonyOS应用审核通过上架后，用户可在华为应用市场搜索到您的HarmonyOS应用。

## 问题定位

检查应用上架是否使用发布版本的API。

## 分析结论

应用上架未使用发布版本的API。

## 修改建议

检查app包内pack.info文件中的releaseType是否为Release，若不是的话升级IDE版本，使用Release版本的IDE重新打包app。

HarmonyOS应用不限定API版本，应用发布版本的API兼容性可参考：[应用开发中的兼容性场景开发指导](../harmonyos-releases/app-compatibility-scenarios.md)。

是否Release看的是IDE内置SDK的releaseType，并非API版本是否Release。例如：6.0Beta5版IDE内置SDK的releaseType是Beta版本，即使应用设置compatibleSdkVersion为"5.0.0(12)"，releaseType仍然为Beta。
