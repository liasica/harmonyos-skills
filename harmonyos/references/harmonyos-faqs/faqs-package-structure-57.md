---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-57
title: 安装HAP包报“failed to install bundle. install debug type not same”错误
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 安装HAP包报“failed to install bundle. install debug type not same”错误
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:0437245000fd5acd5a9efa9387f69f0243f1bef49a85c3a4f801d59277ccf970
---

**原因**

HAP包与设备上已安装的HAP的debug信息不一致导致的问题。

**解决措施**

1. 查看设备上应用的debug配置，如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/DBfJVU_BQeCYrwAKq8roQw/zh-cn_image_0000002624635768.png "点击放大")
2. 检查当前应用代码工程中module下的build-profile.json5文件中的debuggable字段配置（该字段可缺省，缺省值为false），确保与设备上本应用的debug配置一致。如果不一致，需要进行修改。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/_7-Z7k2LT4ieshtfYA60ug/zh-cn_image_0000002624475866.png "点击放大")
