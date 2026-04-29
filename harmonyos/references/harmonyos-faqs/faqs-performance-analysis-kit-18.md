---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-18
title: 如何查看应用是否为系统应用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查看应用是否为系统应用
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1360451f6c684e6148390d0dd768386e1aef17029d64700c3db5d78ceb915179
---

1. 连接设备。
2. 执行以下命令打印日志（Bundle Name获取参考：[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)）：

   ```
   1. hdc shell bm dump -n <Bundle Name>
   ```
3. 当isSystemApp字段返回值为true时，表示当前应用是系统应用。

   返回的部分结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/gTTKI2dXSYueRIwIlctQ-Q/zh-cn_image_0000002244305208.png?HW-CC-KV=V1&HW-CC-Date=20260429T061428Z&HW-CC-Expire=86400&HW-CC-Sign=7B768366E6B83ED47CFDFF2F04117249E202F4AE41D594A6C57B1118B9C40E71 "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/2FqBXOe0R5qSDTrccI0f_Q/zh-cn_image_0000002279264169.png?HW-CC-KV=V1&HW-CC-Date=20260429T061428Z&HW-CC-Expire=86400&HW-CC-Sign=3018872398AA7D6769585155BA781FE1E4E14575413C93EFDB61590775E5A86D "点击放大")
