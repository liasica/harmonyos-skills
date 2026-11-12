---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-80
title: 生成签名时报错删除 .p12 文件目录下的 material 文件夹，重新应用自动签名
breadcrumb: FAQ > DevEco Studio > 编译构建 > 生成签名时报错删除 .p12 文件目录下的 material 文件夹，重新应用自动签名
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:3f2c615ff4544460ca6727f68fc58738ac6b4e8d874cc5a8ac4fc46261df667c
---

**问题描述**

点击生成签名时出现错误：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/nkUibxM7QfiwI7huvfs9YQ/zh-cn_image_0000002624638444.png?HW-CC-KV=V1&HW-CC-Date=20261112T233210Z&HW-CC-Expire=31536000000&HW-CC-Sign=3371AE65BB0750CF729CE587ED2225D2921A03CBEAE5DEFEEE17F21880AE40CB)**解决方案：**

可以通过签名界面提供的profile文件（\*.p7b）或Certpath文件（\*.cer）对应的签名文件路径，删除本地的material文件夹，然后重新启动DevEco Studio进行签名。
