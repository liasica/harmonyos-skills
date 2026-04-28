---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-111
title: 如何遍历JSON对象
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何遍历JSON对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8c56dfe5c797dbc0e6745feb9fa4d7f378a812c8fa827879afd95a977bd4b8ba
---

具体请参考如下示例代码：

```
1. import { ArrayList } from '@kit.ArkTS';

4. interface Winner { num: number };
5. let tmpStr: Record<string, Winner> = JSON.parse('{ "0": {"num": 1}, "1": {"num": 2} }');
6. const arrayList: ArrayList<Winner> = new ArrayList();
7. Object.entries(tmpStr).forEach((item) => {
8. const value = item[1];
9. arrayList.add(value);
10. })
```

[Entries.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Entries.ets#L21-L30)
