---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0005
title: 设备CPU信息获取方法常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > 设备CPU信息获取方法常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:15+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:a0a43505d8afa08c7d7e85da870253c1cf0bede53821cf4cf3a59ddc7e7f6592
---

**Q：如何获取设备的CPU信息？**

**A**：可以通过以下命令来查看CPU信息：

```shell
// 查看CPU信息  
hdc shell param get const.product.cpu.abilist
```

返回结果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/CB9VqHkQTPy-GBqXgj-I1Q/zh-cn_image_0000002795027009.png)
