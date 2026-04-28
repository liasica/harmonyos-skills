---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-124
title: TextInput按压态背景色如何修改
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > TextInput按压态背景色如何修改
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:33+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:323039a9442f93d35f65f1e40a4f703112f2bbb795c20088a29a9b6b82595222
---

可以使用动态属性进行设置。自定义class实现AttributeModifier接口，并给组件设置.attributeModifier()进行绑定即可。参考代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. @State modifier: MyTextInputModifier = new MyTextInputModifier();

6. build() {
7. Row() {
8. Column() {
9. TextInput({ placeholder: 'test' })
10. .width('80%')
11. .height(100)
12. .attributeModifier(this.modifier)
13. }
14. .width('100%')
15. }
16. .height('100%')
17. }
18. }

20. class MyTextInputModifier implements AttributeModifier<TextInputAttribute> {
21. applyNormalAttribute(instance: TextInputAttribute): void {
22. instance.backgroundColor(Color.Grey);
23. }

25. applyPressedAttribute(instance: TextInputAttribute): void {
26. instance.backgroundColor(Color.Blue);
27. }
28. }
```

[ModifyBackgroundColorOfPressedState.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ModifyBackgroundColorOfPressedState.ets#L21-L49)

**参考链接**

[动态属性设置](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)
