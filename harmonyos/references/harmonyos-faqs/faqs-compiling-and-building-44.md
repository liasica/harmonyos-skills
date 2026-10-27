---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-44
title: 编译时DevEco Studio提示Signing material error
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译时DevEco Studio提示Signing material error
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:53+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:55e2a2671f279edc9a265a1f5a4167c8fa59b4d54118ede9b882bd29d6ffb8fb
---

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/Qeut_u45QMOzJZOHxSOjWg/zh-cn_image_0000002654797871.png "点击放大")

**解决措施**

删除C盘用户路径下 .hvigor 文件夹中的 meta 文件，然后重新签名并编译。
