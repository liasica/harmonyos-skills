---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-45
title: 如何通过hdc命令拉起指定的UIAbility
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过hdc命令拉起指定的UIAbility
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:44+08:00
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/WayBDQbmT5ynNPAUFDJS6Q/zh-cn_image_0000002624636362.png "点击放大")

**参考链接**

[aa工具](../harmonyos-guides/aa-tool.md)
