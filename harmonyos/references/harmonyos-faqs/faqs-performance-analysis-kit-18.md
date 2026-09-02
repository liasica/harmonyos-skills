---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-18
title: 如何查看应用是否为系统应用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何查看应用是否为系统应用
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:712c394baf6a576b27ee991df198a3209e7323cd8ff38d8e63f44ef0c9bbb872
---

1. 连接设备。
2. 执行以下命令打印日志（Bundle Name获取参考：[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)）：

   ```
   1. hdc shell bm dump -n <Bundle Name>
   ```
3. 当isSystemApp字段返回值为true时，表示当前应用是系统应用。

   返回的部分结果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/gTTKI2dXSYueRIwIlctQ-Q/zh-cn_image_0000002244305208.png "点击放大")

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/2FqBXOe0R5qSDTrccI0f_Q/zh-cn_image_0000002279264169.png "点击放大")
