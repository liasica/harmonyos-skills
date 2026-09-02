---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-137
title: 编译报错“The required attribute module-srcPath is missing”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The required attribute module-srcPath is missing”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b66ee33f9f1b5ed2c35132165946cb8908a674186d5c5911f82d53abf5cd1abd
---

**错误描述**

缺少必需属性：module-srcPath。

**可能原因**

build-profile.json5文件中缺少模块的相对路径，具体表现为module-srcPath字段缺失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/rjqOBQ1yRSGIax9GX_PzPQ/zh-cn_image_0000002229758669.png)

**解决措施**

进入项目根目录下的build-profile.json5文件，确保module下srcPath字段存在且非空。
