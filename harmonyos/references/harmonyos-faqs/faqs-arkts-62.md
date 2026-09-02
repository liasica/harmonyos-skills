---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-62
title: 如何实现类似Java中的反射方法调用能力
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何实现类似Java中的反射方法调用能力
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:549821b4217455a33e6e3f5252ff06a4a1db8d252e522f52924f98dcfd51938c
---

可以通过[动态import](../harmonyos-guides/arkts-dynamic-import.md#动态import实现方案介绍)的方式实现类似反射能力，具体实现可参考以下代码。

```ts
import('./module').then(
  module => {
    const t = module.DataTable.tagName();
  });
```

```ts
export class DataTable {
  constructor() {
  }
  static tagName(){
    return 'data-table'
  }
}
```
