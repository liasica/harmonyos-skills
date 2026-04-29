---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-codegenie-2
title: 点击CodeGenie顶部栏的新建会话、历史记录等快捷按钮后无反应
breadcrumb: FAQ > DevEco Studio > AI辅助编程 > 点击CodeGenie顶部栏的新建会话、历史记录等快捷按钮后无反应
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:38+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:4e9c978af51961cc478531033d7b8811f8a4425b793ea3d20dec6bc9eae557d5
---

**问题现象**

CodeGenie使用过程中，点击顶部栏新建会话、历史记录、Agent配置等快捷按钮后无反应。

**问题原因**

代码异常，导致前端渲染问题。

**解决措施**

1. 保存工程并关闭DevEco Studio。
2. 打开当前DevEco Studio的安装目录，按如下安装路径找到**codegenie-plugin**文件夹，手动删除此文件夹或将此文件夹移动到其他位置缓存备份。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/Njhc1_VUSYWt6OPvivORyw/zh-cn_image_0000002566394897.png?HW-CC-KV=V1&HW-CC-Date=20260429T062137Z&HW-CC-Expire=86400&HW-CC-Sign=47273BE2F5B43F9AA61DED11EA5540B09BC1D43B25FE17A43B2C23E4328DF881)
3. 在[官网链接](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)下载最新发布的**DevEco CodeGenie 6.0.2 Release**版本，按照[插件安装指导](../harmonyos-guides/ide-codegenie.md#section18337533718)安装和使用新版本插件。
