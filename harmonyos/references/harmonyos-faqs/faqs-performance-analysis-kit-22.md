---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-22
title: 如何获取设备的CPU信息
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何获取设备的CPU信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f0e1bde9c4bbd3804d8a940ae31905c7b96008607348cfd54590b20e5afdc186
---

可以通过以下命令来查看CPU信息：

```powershell
// 查看CPU信息  
hdc shell param get const.product.cpu.abilist
```

返回结果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/t5br7lu7REaDvQwpc7D0LA/zh-cn_image_0000002624636360.png "点击放大")
