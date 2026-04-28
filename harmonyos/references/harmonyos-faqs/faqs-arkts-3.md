---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-3
title: 如何使用正则表达式
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何使用正则表达式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7153988613b0a8abf10c60776401dc67cf6661d7bf4393a6f46e234f0936f0f3
---

首先使用new RegExp()定义一个正则表达式：

```
1. const reg = new RegExp('ba');
```

[RegExp.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/RegExp.ets#L5-L5)

然后，通过test() 方法检测字符串是否匹配，如果字符串中有匹配的值返回true，否则返回false：

```
1. const res = reg.test('bar');
2. console.info('result', res);
```

[RegExp.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/RegExp.ets#L9-L10)
