---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-108
title: 如何通过key获取对象值
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何通过key获取对象值
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:13+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:383ef89cb12bf033f8a5ca06654497b4fc2baeffa2fb88bf135cd975ffb430a6
---

ArkTS中不支持通过索引访问字段，要使用索引的话可以考虑Record<key, value>，参考代码如下：

```
1. class Student {
2. data: Record<string, string> = { 'name': 'aaa', 'age': 'bbb' };
3. }

6. @Entry
7. @Component
8. struct KeyObject {
9. build() {
10. Column() {
11. Button('click')
12. .onClick(() => {
13. let student = new Student();
14. console.info(`${student.data['name']}`);
15. })
16. }
17. .justifyContent(FlexAlign.Center)
18. .alignItems(HorizontalAlign.Center)
19. .width('100%')
20. .height('100%')
21. }
22. }
```

[KeyObject.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/KeyObject.ets#L21-L42)
