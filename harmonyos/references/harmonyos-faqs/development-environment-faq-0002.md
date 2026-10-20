---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/development-environment-faq-0002
title: npm包安装失败问题排查
breadcrumb: FAQ > DevEco Studio > 环境准备 > 常见问题 > npm包安装失败问题排查
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:36+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:c13e1b1c041324cc31b5ba368fc63fc9e660bbc3adde8cf4a18eff5b1ea4f5ed
---

**Q：执行npm install命令安装npm包时，可能会提示安装失败。**

**A**：由于未设置npm仓库地址，可执行如下命令后重新安装。

```bash
npm config set @ohos:registry=https://repo.harmonyos.com/npm/
```
