---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-3
title: 如何使用正则表达式
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何使用正则表达式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:812b537dab5a1868d57f1b322fc6c79cd6aaa40b51500e2b31a99eb8fd9bf619
---

首先使用new RegExp()定义一个正则表达式：

```ts
const reg = new RegExp('ba');
```

然后，通过test() 方法检测字符串是否匹配，如果字符串中有匹配的值返回true，否则返回false：

```ts
const res = reg.test('bar');
console.info('result', res);
```
