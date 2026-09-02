---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-45
title: 如何通过hdc命令拉起指定的UIAbility
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过hdc命令拉起指定的UIAbility
category: harmonyos-faqs
scraped_at: 2026-04-29T14:14:34+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:f44e394a61ac09e94f160601cbd5b5cc3c6ff4434f18c8753c1bf9c079e7a80b
---

使用命令拉起指定UIAbility：

```
1. hdc shell aa start -a <UIAbility Name> -b <Bundle Name>
```

启动成功时，返回"start ability successfully."，启动失败时，返回"error: failed to start ability"，同时会包含相应的失败信息。

示例如下：

```
1. hdc shell aa start -a EntryAbility -b com.example.myapplication
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/DLXUXeenRyOpCvaUeM887g/zh-cn_image_0000002229758597.png "点击放大")

**参考链接**

[aa工具](../harmonyos-guides/aa-tool.md)
