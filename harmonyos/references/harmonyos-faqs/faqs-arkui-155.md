---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-155
title: 如何实现事件透传
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现事件透传
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:071bda518b288d286d9022dbea8688fd7f947e4844ed9ffe92f46762fbd6a802
---

**问题现象**

在Stack中，如果有两个兄弟组件，组件A被组件B覆盖，用户点击组件B时，是否可以将点击事件透传给组件A，触发组件A的onClick回调，而不触发组件B的onClick回调。

**解决措施**

将组件B的hitTestBehavior属性设置为HitTestMode.None即可。参考代码如下：

```
1. @Entry
2. @Component
3. struct StackExample {
4. build() {
5. Stack({ alignContent: Alignment.Bottom }) {
6. Text('A')
7. .width('90%')
8. .height('100%')
9. .backgroundColor(0xd2cab3)
10. .align(Alignment.Top)
11. .onClick(() => {
12. console.log('TextA click')
13. })
14. Text('B')
15. .width('70%')
16. .height('60%')
17. .backgroundColor(0xc1cbac)
18. .align(Alignment.Top)
19. .hitTestBehavior(HitTestMode.None)
20. .onClick(() => {
21. console.log('TextB click')
22. })
23. }
24. .width('100%')
25. .height(150)
26. .margin({ top: 5 })
27. }
28. }
```

[RealizeTransparentTransmissionOfEvents.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/RealizeTransparentTransmissionOfEvents.ets#L21-L48)

**参考链接**

[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)
