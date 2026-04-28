---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-89
title: 如何提高代码混淆率
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何提高代码混淆率
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:26b2ca6b21ca4fcc1dd78c3e4817a51a4cc54ec9cbe5d34d21e594da2ec656e3
---

**问题描述**

闭源库如何确保其闭源性和安全性？

当前闭源库仅能实现基础的字段混淆，混淆比例低于20%，实际逻辑无法混淆。相比之下，使用Webpack打包工具进行打包后的代码混淆效果显著，格式化后仍无法看清内部逻辑。我们在这方面存在较大差距。

如果后续有规划，具体的规划是怎样的？针对当前现状，如何保证银行金融类SDK的闭源安全性？

**解决方案**

混淆比例较低的原因有以下两点

1：属性混淆、导出内容混淆和顶层作用域混淆等选项未开启。

2：若上述主要混淆选项均已开启，但混淆比例仍较低，可能是因为定义的变量、属性名、函数名或方法名与系统白名单中的名称重叠，导致未被混淆。建议在名称中添加前缀或后缀，以避开系统白名单。系统白名单的缓存路径为：build/cache/{...}/release/obfuscation/systemApiCache.json。
