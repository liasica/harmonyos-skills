---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-148
title: 编译报错“Invalid tag 'xxx' at 'xxx/xxx.json5'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Invalid tag 'xxx' at 'xxx/xxx.json5'.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:26617596cec24ad60a970cf461cb544e2529ed1b8f475c4d41604160ca08a54e
---

**错误描述**

在xxx/xxx.json5文件中存在无效的tag标签“xxx”。

**可能原因**

在项目根目录的oh-package.json5文件中定义parameterFile参数配置文件的配置版本号时，使用的tag标签包含不符合要求的字符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/xcSiXKFtRBKaj7rDpDQkxQ/zh-cn_image_0000002229758505.png?HW-CC-KV=V1&HW-CC-Date=20260428T002939Z&HW-CC-Expire=86400&HW-CC-Sign=A5363A0675B4C0347B31D37A6C3AA5F476E194E71F6AA51EBFCC85343A966B3C)

**解决措施**

确保parameterFile中定义的tag标签仅由字母、数字、“.”、“-”或“\_”组成，必须以字母或数字开头，长度不超过 60 个字符，且不能配置为latest。
