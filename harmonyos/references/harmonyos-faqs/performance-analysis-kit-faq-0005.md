---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/performance-analysis-kit-faq-0005
title: 设备CPU信息获取方法常见问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 常见问题 > 设备CPU信息获取方法常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:44+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:8d4719a18ebd5870719b116ee90dc686c69b77327cb3dc2f624f07858a01f0b4
---

**Q：如何获取设备的CPU信息？**

**A**：可以通过以下命令来查看CPU信息：

```shell
// 查看CPU信息  
hdc shell param get const.product.cpu.abilist
```

返回结果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/7ykAdVpnQ9GCH_jRJF7hfg/zh-cn_image_0000002795027009.png)
