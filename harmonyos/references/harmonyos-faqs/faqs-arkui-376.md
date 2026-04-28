---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-376
title: 如何实现ArkUI组件字符串变量拼接
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现ArkUI组件字符串变量拼接
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:37+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:2a65d938ff2d95fd809b373848a05ff1379158bdfee44c41dd5e32d337f89e01
---

**问题现象**

例如：在Text组件中如何实现字符串与变量的拼接功能？

```
1. Text($r('app.string.EntryAbility_desc', 'Hello'))
```

**解决措施**

可以通过资源文件结合%d、%s的方式进行实现。

示例如下所示：

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
2. 在页面组件中使用$r()方法拼接变量（示例代码如下）。

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

   [ImplementArkUIComponentStringVariableConcatenation.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementArkUIComponentStringVariableConcatenation.ets#L21-L37)
3. 切换中英文语言时，会自动跟随语言的切换代入对应的变量信息。

**参考链接**

[资源访问](../harmonyos-guides/resource-categories-and-access.md#资源访问)
