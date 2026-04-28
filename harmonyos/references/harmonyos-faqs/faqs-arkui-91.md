---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-91
title: 如何实现文本竖向排列
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现文本竖向排列
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4ef80d179c3ff8708b6c8bceef6ee9d7d16ab1f53a9d8d0e4f3b6f2104f4d54d
---

可以通过设置Text组件宽度width与字号一致的方式实现。参考代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. private message: string = 'This document is suitable for beginners in application development. By building a simple application with page jump/return function, quickly understand the main files of the project directory and familiarize yourself with the application development process.';
5. build() {
6. Column() {
7. Text(this.message)
8. .fontSize(13)
9. .width(13)
10. }
11. }
12. }
```

[VerticalArrangementOfText.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/VerticalArrangementOfText.ets#L21-L32)
