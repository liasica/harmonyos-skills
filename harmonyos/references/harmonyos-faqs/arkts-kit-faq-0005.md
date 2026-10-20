---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-kit-faq-0005
title: ArkTS正则表达式使用常见问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 常见问题 > ArkTS正则表达式使用常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:19+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:2a0c306279b93c3a86b80c5d974ad4a9b464bb014cc57680f71fc229ff86ba70
---

**Q：如何使用正则表达式？**

**A**：首先使用new RegExp()定义一个正则表达式：

```ts
const reg = new RegExp('ba');
```

然后，通过test() 方法检测字符串是否匹配，如果字符串中有匹配的值返回true，否则返回false：

```ts
const res = reg.test('bar');
console.info('result', res);
```
