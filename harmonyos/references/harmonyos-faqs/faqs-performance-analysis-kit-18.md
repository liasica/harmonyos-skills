---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-18
title: 如何查看应用是否为系统应用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查看应用是否为系统应用
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:44+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:55bf99800fd3fcf2013867be1c409125cf2d1c8e1c98ff50fe3d5af3f29db825
---

1. 连接设备。
2. 执行以下命令打印日志（Bundle Name获取参考：[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)）：

   ```powershell
   hdc shell bm dump -n <Bundle Name>
   ```
3. 当isSystemApp字段返回值为true时，表示当前应用是系统应用。

   返回的部分结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/A_3EzelQSHaojl7d7CWZFw/zh-cn_image_0000002624476468.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/QQ7C_hwmR8SXyQ8T1U3iag/zh-cn_image_0000002654795827.png "点击放大")
