---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-45
title: 如何通过hdc命令拉起指定的UIAbility
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 如何通过hdc命令拉起指定的UIAbility
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:8b6e355c732042bd6947cb081717f146c6a22a215e5b6c7e55afe75bf373f77e
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/SCmK0CwvTBmi6BGew8VSLQ/zh-cn_image_0000002624636362.png "点击放大")

**参考链接**

[aa工具](../harmonyos-guides/aa-tool.md)
