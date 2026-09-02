---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-8
title: 安装npm包失败的处理办法
breadcrumb: FAQ > DevEco Studio > 环境准备 > 安装npm包失败的处理办法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:f32a2a707e8103073f3ac319b6f225a5781ecf23da84ac6d149fa4eb12ab41b7
---

**问题现象**

执行npm install命令安装npm包时，可能会提示安装失败。

**解决措施**

由于未设置npm仓库地址，可执行如下命令后重新安装。

```powershell
npm config set @ohos:registry=https://repo.harmonyos.com/npm/
```
