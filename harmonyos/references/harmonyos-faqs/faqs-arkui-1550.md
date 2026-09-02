---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1550
title: getContext和getHostContext方法之间的差异
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > getContext和getHostContext方法之间的差异
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d3f1429bfee60a0e5c7118aad58e5c5b4998d5d56961c05c273c432186dfaa4b
---

## 问题现象

API参考文档中说明getContext方法从API version 18开始弃用，建议使用UIContext中的getHostContext替代。在使用过程中发现，将返回值类型注解为Context时编译报错，请问两者有什么差异？

## 解决方案

| 对比维度 | getContext | getHostContext |
| --- | --- | --- |
| 废弃状态 | 从API 18起废弃，不再推荐使用。 | API 12引入，API 18起作为推荐替代方案。 |
| 返回值类型 | Context | Context|undefined |
| 获取Context方式 | let context: Context = getContext(this); | let context: Context|undefined = this.getUIContext().getHostContext(); |
