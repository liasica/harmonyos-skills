---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-142
title: 半模态转场如何控制固定高度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 半模态转场如何控制固定高度
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b5f6594e606c36ebc349dc75aaed63b6758c3fcd4f7c30665c1da90a41b1e812
---

通过设置bindSheet()的参数options对高度进行控制。参考代码如下：

```
1. @Entry
2. @Component
3. struct SheetTransitionExample {
4. @State isShow: boolean = false;
5. @State sheetHeight: number = 300;

7. @Builder
8. myBuilder() {
9. Column() {
10. Button('change height')
11. .margin(10)
12. .fontSize(20)
13. .onClick(() => {
14. this.sheetHeight = 500;
15. })

17. Button('Set Illegal height')
18. .margin(10)
19. .fontSize(20)
20. .onClick(() => {
21. this.sheetHeight = 0;
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }

28. build() {
29. Column() {
30. Button('transition modal 1')
31. .onClick(() => {
32. this.isShow = true;
33. })
34. .fontSize(20)
35. .margin(10)
36. .bindSheet(this.isShow, this.myBuilder(), { height: this.sheetHeight, backgroundColor: Color.Green })
37. }
38. .justifyContent(FlexAlign.Center)
39. .width('100%')
40. .height('100%')
41. }
42. }
```

[SemiModalControlWithFixedHeight.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SemiModalControlWithFixedHeight.ets#L21-L62)

**参考链接**

[半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md)
