---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-57
title: 安装HAP包报“failed to install bundle. install debug type not same”错误
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 安装HAP包报“failed to install bundle. install debug type not same”错误
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:46+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:e29ec3b161fee17855f9220307b9c5215a99df8d424f66c8765bae6e85191909
---

**原因**

HAP包与设备上已安装的HAP的debug信息不一致导致的问题。

**解决措施**

1. 查看设备上应用的debug配置，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/hzBq-NBnRz-nfTYYQY7M1w/zh-cn_image_0000002624635768.png "点击放大")
2. 检查当前应用代码工程中module下的build-profile.json5文件中的debuggable字段配置（该字段可缺省，缺省值为false），确保与设备上本应用的debug配置一致。如果不一致，需要进行修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/84lXzBvXT42UVRx49vSPHA/zh-cn_image_0000002624475866.png "点击放大")
