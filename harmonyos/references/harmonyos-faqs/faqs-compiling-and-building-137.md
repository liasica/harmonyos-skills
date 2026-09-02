---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-137
title: 编译报错“The required attribute module-srcPath is missing”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The required attribute module-srcPath is missing”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:ba16de94a57fd2c982e81835aa4fdaeb66df4fd46c7ea95c0794150bd1e4e8a5
---

**错误描述**

缺少必需属性：module-srcPath。

**可能原因**

build-profile.json5文件中缺少模块的相对路径，具体表现为module-srcPath字段缺失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/rcrHtbo0QqCyr0UoQcaO5A/zh-cn_image_0000002624638528.png)

**解决措施**

进入项目根目录下的build-profile.json5文件，确保module下srcPath字段存在且非空。
