---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-157
title: 编译报错“Unrecognized archive format in parameterFile”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Unrecognized archive format in parameterFile”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:1a5ca1aac14b7796f7393b864da40b33cad15669a3c97b71ba312e8f4e442c86
---

**错误描述**

parameterFile中包含无法识别的格式。

**可能原因**

使用parameterFile参数化配置的本地依赖既不是目录，也不是.har或.tgz文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/otmjiA11QUi1tJ8Z44VEFQ/zh-cn_image_0000002624478638.png)

**解决措施**

将本地依赖修改为模块目录或模块编译后的har/tgz文件。
