---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-137
title: 编译报错“The required attribute module-srcPath is missing”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The required attribute module-srcPath is missing”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:80671170d1fa2ca2c00084e160bd9dc59e46643052c91055198c4f6b2ecf8ecc
---

**错误描述**

缺少必需属性：module-srcPath。

**可能原因**

build-profile.json5文件中缺少模块的相对路径，具体表现为module-srcPath字段缺失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/rjqOBQ1yRSGIax9GX_PzPQ/zh-cn_image_0000002229758669.png?HW-CC-KV=V1&HW-CC-Date=20260429T062051Z&HW-CC-Expire=86400&HW-CC-Sign=D5274F758100D0A3E072CB64D5D45FC0750D12BD76D63D6D42CE88A59D3A2F7A)

**解决措施**

进入项目根目录下的build-profile.json5文件，确保module下srcPath字段存在且非空。
