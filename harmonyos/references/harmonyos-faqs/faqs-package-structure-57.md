---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-57
title: 安装HAP包报“failed to install bundle. install debug type not same”错误
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 安装HAP包报“failed to install bundle. install debug type not same”错误
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:52+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:8a7027d0e1d98ae360431eba7badf0e764f85cb3fcedacb1bd182a1c27bc08d0
---

**原因**

HAP包与设备上已安装的HAP的debug信息不一致导致的问题。

**解决措施**

1. 查看设备上应用的debug配置，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/cb4zrYUHS5aFa8h5ok9vvA/zh-cn_image_0000002229758797.png "点击放大")
2. 检查当前应用代码工程中module下的build-profile.json5文件中的debuggable字段配置（该字段可缺省，缺省值为false），确保与设备上本应用的debug配置一致。如果不一致，需要进行修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/5ij3ljRaTBq4DBO7M9gbBw/zh-cn_image_0000002229604297.png "点击放大")
