---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-8
title: 如何给UI组件设置不同情况下的属性
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何给UI组件设置不同情况下的属性
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5071cb3013a33213f58a490d400163569bd5ab9e65e97f97a9af327926bfc132
---

使用if/else条件渲染设置组件属性值。具体可参考示例代码：

```
1. @Entry
2. @Component
3. struct TestHeightPage {
4. @State message: string = 'Hello World';
5. @State myHeight1: number = 30;
6. @State myHeight2: number = 60;
7. @State flag: boolean = false

9. build() {
10. Column() {
11. Text(this.message)
12. .fontSize(20)
13. .fontWeight(FontWeight.Bold)
14. .width('100%')
15. .height(this.flag ? this.myHeight1 : this.myHeight2)
16. .backgroundColor(Color.Orange)

18. Button('Modify Text attribute height').onClick(() => {
19. this.flag = !this.flag;
20. }).margin({ top: 12 })
21. }
22. .height('100%')
23. }
24. }
```

[SetDifferentAttributes.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SetDifferentAttributes.ets#L21-L45)

**参考链接**

[if/else：条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)
