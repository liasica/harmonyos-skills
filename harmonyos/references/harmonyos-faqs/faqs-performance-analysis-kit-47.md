---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-47
title: 如何通过hdc命令关闭整个应用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过hdc命令关闭整个应用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:19+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:5b997e28a719b4fda8653431e95218d69b0d75648cdcc2adfae129fac8685ce2
---

可以通过以下命令结束应用：

```
1. hdc shell aa force-stop <bundleName>
```

返回“force stop process successfully”，表示应用已成功结束。

示例如下：

```
1. hdc shell aa force-stop com.example.myapplication
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/rC8SbQ_rQeaFHJGkqlPRYQ/zh-cn_image_0000002194158796.png?HW-CC-KV=V1&HW-CC-Date=20260428T002318Z&HW-CC-Expire=86400&HW-CC-Sign=C722CB31B5C14DF645BFD76C458B74B2A75F704720A78565D5ADB14CCD4E297E "点击放大")

**参考链接**

[aa工具](../harmonyos-guides/aa-tool.md)
