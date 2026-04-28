---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-62
title: 如何实现类似Java中的反射方法调用能力
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何实现类似Java中的反射方法调用能力
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d1ccc6ec5dffe891ba79b24ed89d435b762655169379628596fce1b6c70cef44
---

可以通过[动态import](../harmonyos-guides/arkts-dynamic-import.md#动态import实现方案介绍)的方式实现类似反射能力，具体实现可参考以下代码。

```
1. import('./module').then(
2. module => {
3. const t = module.DataTable.tagName();
4. });
```

[DynamicImport.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/DynamicImport.ets#L21-L24)

```
1. export class DataTable {
2. constructor() {
3. }
4. static tagName(){
5. return 'data-table'
6. }
7. }
```

[module.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/module.ets#L21-L27)
