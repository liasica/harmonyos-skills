---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-80
title: 生成签名时报错删除 .p12 文件目录下的 material 文件夹，重新应用自动签名
breadcrumb: FAQ > DevEco Studio > 编译构建 > 生成签名时报错删除 .p12 文件目录下的 material 文件夹，重新应用自动签名
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0c40668540d7e2528f8df84e854e145c9a274975809afca26dec53846aa3172d
---

**问题描述**

点击生成签名时出现错误：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/OzqB_vWuQkCRGaBYaW0E2A/zh-cn_image_0000002229604377.png)**解决方案：**

可以通过签名界面提供的profile文件（\*.p7b）或Certpath文件（\*.cer）对应的签名文件路径，删除本地的material文件夹，然后重新启动DevEco Studio进行签名。
