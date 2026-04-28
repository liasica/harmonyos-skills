---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-457
title: 当一个组件同时绑定了点击事件（onClick）和并行手势（.parallelGesture），为什么当操作为长按时，两个手势都会响应
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 当一个组件同时绑定了点击事件（onClick）和并行手势（.parallelGesture），为什么当操作为长按时，两个手势都会响应
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:86d9dcdd8013c48d366cb4973045f3bf246e43c228556a04f8dfbac2c59a0d28
---

**问题描述**

由于onClick和.parallelGesture绑定的手势被组合成并行手势组，在长按操作时，系统会同时检测到长按手势和潜在的单击手势（在未达到长按时间阈值前），因此两者都会被触发。

```
1. @Entry
2. @Component
3. struct onClickAndParallelGestureProblematic {
4. @State message: string = '多种手势，长按这里';

6. build() {
7. RelativeContainer() {
8. Text(this.message)
9. .id('TwoGestureHelloWorld')
10. .fontSize($r('app.float.page_text_font_size'))
11. .fontWeight(FontWeight.Bold)
12. .alignRules({
13. center: { anchor: '__container__', align: VerticalAlign.Center },
14. middle: { anchor: '__container__', align: HorizontalAlign.Center }
15. })
16. .onClick(() => {
17. console.info('TapGesture--单击');
18. })
19. .parallelGesture(
20. GestureGroup(GestureMode.Exclusive,
21. LongPressGesture({ repeat: false })
22. .onAction(() => {
23. console.info('LongPressGesture--长按');
24. })
25. )
26. )
27. }
28. .height('100%')
29. .width('100%')
30. }
31. }
```

[onClickAndParallelGestureProblematic.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/0f9903169604dbc2f51873025d681d6224817e56/ArkUI/entry/src/main/ets/pages/onClickAndParallelGestureProblematic.ets#L21-L52)

**解决措施**

如需实现当前组件上绑定两个互斥的点击和长按手势，同时该组件上的手势又需要和子节点的手势同时识别时，可以参考下列代码，将两个互斥的点击和长按手势先绑定到一个互斥手势组内，然后通过.parallelGesture方式将手势组和子节点手势绑定成并行。示例代码如下：

```
1. @Entry
2. @Component
3. struct onClickAndParallelGestureSolution {
4. @State message: string = '多种手势，长按这里';

6. build() {
7. RelativeContainer() {
8. Text(this.message)
9. .id('HelloWorld')
10. .fontSize($r('app.float.page_text_font_size'))
11. .fontWeight(FontWeight.Bold)
12. .alignRules({
13. center: { anchor: '__container__', align: VerticalAlign.Center },
14. middle: { anchor: '__container__', align: HorizontalAlign.Center }
15. })
16. .parallelGesture(
17. GestureGroup(GestureMode.Exclusive,
18. TapGesture({ count: 1, fingers: 1 })
19. .onAction(() => {
20. console.info('TapGesture--单击');
21. }),
22. LongPressGesture({ repeat: false })
23. .onAction(() => {
24. console.info('LongPressGesture--长按');
25. })
26. )
27. )
28. }
29. .height('100%')
30. .width('100%')
31. }
32. }
```

[onClickAndParallelGestureSolution.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/0f9903169604dbc2f51873025d681d6224817e56/ArkUI/entry/src/main/ets/pages/onClickAndParallelGestureSolution.ets#L21-L53)
