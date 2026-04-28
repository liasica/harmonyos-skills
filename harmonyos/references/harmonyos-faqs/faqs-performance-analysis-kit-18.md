---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-18
title: 如何查看应用是否为系统应用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查看应用是否为系统应用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c64fe62cf7604ba2b37016f2618355dd6ef6fc2944d0c8d8d4198864033469b5
---

1. 连接设备。
2. 执行以下命令打印日志（Bundle Name获取参考：[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)）：

   ```
   1. hdc shell bm dump -n <Bundle Name>
   ```
3. 当isSystemApp字段返回值为true时，表示当前应用是系统应用。

   返回的部分结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/gTTKI2dXSYueRIwIlctQ-Q/zh-cn_image_0000002244305208.png?HW-CC-KV=V1&HW-CC-Date=20260428T002315Z&HW-CC-Expire=86400&HW-CC-Sign=DC91113B4AFF8EAD171E131CDBFDC9D0A8E9E31B2DB510ACECAA46841AC75509 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/2FqBXOe0R5qSDTrccI0f_Q/zh-cn_image_0000002279264169.png?HW-CC-KV=V1&HW-CC-Date=20260428T002315Z&HW-CC-Expire=86400&HW-CC-Sign=48C8D89369FD9F43B0B92EAE6C373AD27DB34596EAB1036E19C860D85267D38A "点击放大")
