---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-codegenie-2
title: 点击CodeGenie顶部栏的新建会话、历史记录等快捷按钮后无反应
breadcrumb: FAQ > DevEco Studio > AI辅助编程 > 点击CodeGenie顶部栏的新建会话、历史记录等快捷按钮后无反应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:9a3b592acec06c9c79b8f3a2f4627f6f28c10284c8216076f4d982ffd197203d
---

**问题现象**

CodeGenie使用过程中，点击顶部栏新建会话、历史记录、Agent配置等快捷按钮后无反应。

**问题原因**

代码异常，导致前端渲染问题。

**解决措施**

1. 保存工程并关闭DevEco Studio。
2. 打开当前DevEco Studio的安装目录，按如下安装路径找到**codegenie-plugin**文件夹，手动删除此文件夹或将此文件夹移动到其他位置缓存备份。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/GWM6RyACQwKzCXwsCd3-_g/zh-cn_image_0000002654838149.png)
3. 在[官网链接](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)下载最新发布的**DevEco CodeGenie 6.0.2 Release**版本，按照[插件安装指导](../harmonyos-guides/ide-codegenie.md#section18337533718)安装和使用新版本插件。
