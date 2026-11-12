---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-149
title: 编译报错“The 'tag' keyword is not allowed for 'version' at 'xxx/oh-package.json5'”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The 'tag' keyword is not allowed for 'version' at 'xxx/oh-package.json5'”
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:fb8f0dc1cac4ca89f086ce17203b5903861c4f40e982e6dd277a5472d5ec7cc3
---

**错误描述**

oh-package.json5文件中的version字段不能包含tag标签。

**可能原因**

使用parameterFile参数化配置版本号时，oh-package.json5文件中的version字段不能包含tag标签。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/NhWineJXRqeQct7bOBR50g/zh-cn_image_0000002654797991.png?HW-CC-KV=V1&HW-CC-Date=20261112T233208Z&HW-CC-Expire=31536000000&HW-CC-Sign=5831621206EADAF749C48B473508CED53DB374B59BA4F1C2DDD3A1A34B9BA630)

**解决措施**

当oh-package.json5文件中的version字段引用parameterFile时，开发者不应使用tag标签。
