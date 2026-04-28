---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-144
title: ArkUI组件的字符串中如何实现字符串变量拼接
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > ArkUI组件的字符串中如何实现字符串变量拼接
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4ea9874275df26b11e76d7b92d42b41c1f1484e6c2cdc29c2d042ed62189cf48
---

**问题现象**

ArkUI组件的字符串中如何实现字符串变量拼接，结合限定词目录的资源文件，例如语言切换时候，字符串内容自动跟随切换。例如Text()组件如何实现字符串变量的拼接功能？

```
1. Text($r('app.string.EntryAbility_desc', 'Hello'))
```

[ImplementingStringVariableConcatenation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementingStringVariableConcatenation.ets#L24-L24)

**解决措施**

可以通过资源文件结合`%d`和`%s`的方式实现。使用样例如下所示。

1. 修改"src/main/resources/zh\_CN/element/string.json"文件，对其中的一个需要变量拼接内容增加%d拼接。

   ```
   1. {
   2. "string": [
   3. {
   4. "name": "module_desc",
   5. "value": "模块描述%d"
   6. },
   7. {
   8. "name": "EntryAbility_desc",
   9. "value": "description"
   10. },
   11. {
   12. "name": "EntryAbility_label",
   13. "value": "label"
   14. }
   15. ]
   16. }
   ```

   修改"src/main/resources/en\_US/element/string.json"文件，对其中的一个需要变量拼接内容增加%d拼接。

   ```
   1. {
   2. "string": [
   3. {
   4. "name": "module_desc",
   5. "value": "module description%d"
   6. },
   7. {
   8. "name": "EntryAbility_desc",
   9. "value": "description%d"
   10. },
   11. {
   12. "name": "EntryAbility_label",
   13. "value": "label"
   14. }
   15. ]
   16. }
   ```
2. 在页面组件中，使用$r(xx)拼接变量。

   ```
   1. @Entry
   2. @Component
   3. struct Page1 {
   4. @State num1: number = 100;

   6. build() {
   7. Row() {
   8. Column() {
   9. Text($r('app.string.module_desc', this.num1))
   10. .fontSize(50)
   11. .fontWeight(FontWeight.Bold)
   12. }
   13. .width('100%')
   14. }
   15. .height('100%')
   16. }
   17. }
   ```

   [ImplementingStringVariableConcatenation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementingStringVariableConcatenation.ets#L30-L46)
3. 切换中英文语言时，自动带入对应变量信息。

**参考链接**

[资源分类与访问](../harmonyos-guides/resource-categories-and-access.md)
