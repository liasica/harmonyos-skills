---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-140
title: 编译报错“Cannot resolved import statement”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Cannot resolved import statement”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4947e65eaaf47954ce862cfe2e8f3f352f76cb7a82c3175044936aec8dc1c4ef
---

**错误描述**

在编译过程中，提示“Cannot resolved import statement”错误信息。

**可能原因**

导入文件时，大小写不一致会导致问题（导入到单个文件夹时，默认寻址小写 “index.ets”文件，但该文件夹下仅存在大写“index.ets”文件）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/wVd69cGLRLW0WyXbsZriJQ/zh-cn_image_0000002654797983.png)

**解决措施**

检查import文件的大小写。
