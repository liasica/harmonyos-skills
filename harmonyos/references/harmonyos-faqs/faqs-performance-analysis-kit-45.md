---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-45
title: 如何通过hdc命令拉起指定的UIAbility
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过hdc命令拉起指定的UIAbility
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:4099d07dfbfe2692342542368c1f23f6350d37332b2fca76ca3cf2be73a15bb6
---

使用命令拉起指定UIAbility：

```powershell
hdc shell aa start -a <UIAbility Name> -b <Bundle Name>
```

启动成功时，返回"start ability successfully."，启动失败时，返回"error: failed to start ability"，同时会包含相应的失败信息。

示例如下：

```powershell
hdc shell aa start -a EntryAbility -b com.example.myapplication
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/WayBDQbmT5ynNPAUFDJS6Q/zh-cn_image_0000002624636362.png?HW-CC-KV=V1&HW-CC-Date=20261112T233216Z&HW-CC-Expire=31536000000&HW-CC-Sign=502EBEA5DE668591D513683A993F7A61FF00A70460B4A33D7F400204204BC9D7 "点击放大")

**参考链接**

[aa工具](../harmonyos-guides/aa-tool.md)
