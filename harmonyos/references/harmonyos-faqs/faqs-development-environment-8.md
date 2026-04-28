---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-development-environment-8
title: 安装npm包失败的处理办法
breadcrumb: FAQ > DevEco Studio > 环境准备 > 安装npm包失败的处理办法
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:736f11f92333826b619dbc5232a014cb674bbc5a8dc2281f81202e889c7cca27
---

**问题现象**

执行npm install命令安装npm包时，可能会提示安装失败。

**解决措施**

由于未设置npm仓库地址，可执行如下命令后重新安装。

```
1. npm config set @ohos:registry=https://repo.harmonyos.com/npm/
```
