---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-34
title: 如何使HSP包版本号统一
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何使HSP包版本号统一
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7bdd344c91dede05c19ffbafd492967d3c7da657dccf1ffde013ad77a240d6bb
---

**问题场景**

当多个业务团队各自开发各自的模块时，确保每个团队的HSP版本号一致较为困难。即使初始版本号一致，如果某个团队后续升级了版本号，其他未修改代码的团队也需重新升级版本号并重新打包。

**解决措施**

HSP和宿主HAP一起安装时，校验严格。包名、版本号、sdk版本号、releaseType需一致。可以通过打包工具：[版本归一指令（versionNormalize）](../harmonyos-guides/packing-tool.md#版本归一指令versionnormalize)，将多个HAP、HSP的版本统一。

示例：

```
1. java -jar path\app_packing_tool.jar --mode versionNormalize --input-list 1.hap,2.hsp --version-code 1000001 --version-name 1.0.1 --out-path path\out\
```
