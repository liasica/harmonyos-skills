---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-111
title: 如何遍历JSON对象
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何遍历JSON对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7fe124cad0f40e56824aa03b60d4cf95f27ac70b827b970717462e8a115cc1ff
---

具体请参考如下示例代码：

```ts
import { ArrayList } from '@kit.ArkTS';

interface Winner { num: number };
let tmpStr: Record<string, Winner> = JSON.parse('{ "0": {"num": 1}, "1": {"num": 2} }');
const arrayList: ArrayList<Winner> = new ArrayList();
Object.entries(tmpStr).forEach((item) => {
  const value = item[1];
  arrayList.add(value);
})
```
