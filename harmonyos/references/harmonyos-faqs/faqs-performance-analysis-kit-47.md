---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-47
title: 如何通过hdc命令关闭整个应用
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过hdc命令关闭整个应用
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:34+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:dea7338fe77c16379dc25a50c5d070b5a667031bffd82dd7d41348c80019e6af
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/rC8SbQ_rQeaFHJGkqlPRYQ/zh-cn_image_0000002194158796.png?HW-CC-KV=V1&HW-CC-Date=20260429T061433Z&HW-CC-Expire=86400&HW-CC-Sign=0F69A484AD3EC24B7EAAA4C95FDB87C2A0E5E17B41776DE2CCD683168B89DB09 "点击放大")

**参考链接**

[aa工具](../harmonyos-guides/aa-tool.md)
