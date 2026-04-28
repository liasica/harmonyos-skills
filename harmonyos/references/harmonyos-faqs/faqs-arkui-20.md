---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-20
title: 如何主动清除控件的焦点
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何主动清除控件的焦点
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:98e9a0657b35014f3fd42144d2d943ac0ec090c9ed75115c1c44f1954b1de7ef
---

当组件处于获焦状态时，将其focusable属性或enabled属性设置为false，会自动使该组件失焦。焦点将按照[走焦规则](../harmonyos-guides/arkts-common-events-focus-event.md#走焦规范)转移给其他组件。参考代码如下：

```
1. @Entry
2. @Component
3. struct ClearComponentFocus {
4. // Whether textInput is focus
5. @State textFocusable: boolean = true;
6. @State text: string = 'Gain focus';

8. build() {
9. Column() {
10. TextInput({ text: this.text })
11. .focusable(this.textFocusable)
12. .onFocus(() => {
13. this.text = 'Gain focus';
14. })
15. .onBlur(() => {
16. this.text = 'Lost Focus';
17. })
18. Button('Button1')
19. .width(160)
20. .height(70)
21. .margin({ top: 20 })
22. .onClick(() => {
23. this.textFocusable = !this.textFocusable;
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

[ProactivelyClearTheFocusOfTheControl.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ProactivelyClearTheFocusOfTheControl.ets#L21-L49)

**参考链接**

[设置组件是否获焦](../harmonyos-guides/arkts-common-events-focus-event.md#设置组件是否可获焦)
