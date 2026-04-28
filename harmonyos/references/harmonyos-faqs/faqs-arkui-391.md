---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-391
title: 如何实现弹窗动画和遮罩动画分开设置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现弹窗动画和遮罩动画分开设置
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:42+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:62fe7c5c2b04907e92627a7ab26ea835b1766fe531463b47a804f159b502b3af
---

**问题现象**

目前由于弹窗和遮罩是一起的，如果给弹窗增加由上往下的动画，遮罩也会同时执行相同的动画效果。

**解决措施**

可以单独给dialog里的自定义组件添加.transition属性设置该组件的出现方式，在消失前，通过让组件提前进入隐藏状态触发.transition动画，然后再关闭弹窗实现退场效果：

```
1. import { ComponentContent } from '@kit.ArkUI';

3. export interface SimpleDialogParams {
4. title: string
5. desc: string
6. visible?: Visibility
7. }

9. @Builder
10. function SimpleDialogBuilder(params: SimpleDialogParams) {
11. SimpleDialogUI({ params })
12. }

14. @Component
15. struct SimpleDialogUI {
16. @Prop params: SimpleDialogParams | null = null;
17. @State yOffset: number | string = '100%';
18. @Prop visible: Visibility = Visibility.Visible;

20. build() {
21. Column() {
22. Text(this.params?.title)
23. .fontSize(18)
24. .fontWeight(FontWeight.Bold)
25. .textAlign(TextAlign.Center)
26. .fontColor(Color.Black)
27. .margin({ bottom: 16 })
28. .width('100%')
29. Text(this.params?.desc)
30. .fontSize(14)
31. .lineHeight(22)
32. .fontColor(Color.Gray)
33. .margin({ bottom: 16 })
34. .width('100%')
35. }
36. .borderRadius({ topLeft: 16, topRight: 16 })
37. .backgroundColor(Color.White)
38. .width('100%')
39. .alignItems(HorizontalAlign.Start)
40. .visibility(this.params?.visible)
41. .padding(20)
42. .transition(TransitionEffect.translate({ y: '100%' }).animation({ duration: 200 }))
43. }
44. }

46. @Entry
47. @Component
48. struct SetDialogAnimationAndMaskAnimationSeparately {
49. @State message: string = 'Hello World';

51. build() {
52. RelativeContainer() {
53. Text(this.message)
54. .id('HelloWorld')
55. .fontSize($r('app.float.page_text_font_size'))
56. .fontWeight(FontWeight.Bold)
57. .alignRules({
58. center: { anchor: '__container__', align: VerticalAlign.Center },
59. middle: { anchor: '__container__', align: HorizontalAlign.Center }
60. })
61. .onClick(() => {
62. const param =
63. { title: '标题标题标题', desc: '描述描述描述描述描述描述描述描述描述描述描述描述' } as SimpleDialogParams;
64. const contentNode = new ComponentContent(this.getUIContext(), new WrappedBuilder(SimpleDialogBuilder), param);
65. this.getUIContext().getPromptAction().openCustomDialog(contentNode, {
66. autoCancel: true,
67. maskColor: 'cc000000',
68. maskRect: {
69. x: 0,
70. y: '-100%',
71. width: '100%',
72. height: '200%'
73. },
74. alignment: DialogAlignment.Bottom,
75. transition: TransitionEffect.opacity(0).animation({ duration: 200 }),
76. onWillDismiss: res => {
77. contentNode.update({
78. title: '标题标题标题',
79. desc: '描述描述描述描述描述描述描述描述描述描述描述描述',
80. visible: Visibility.Hidden
81. });
82. res.dismiss();
83. }
84. });
85. })
86. }
87. .width('100%')
88. .height('100%')
89. }
90. }
```

[SetDialogAnimationAndMaskAnimationSeparately.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/7f6ec93b3156f9d44df41be0b753fb848a6934fd/ArkUI/entry/src/main/ets/pages/SetDialogAnimationAndMaskAnimationSeparately.ets#L21-L111)
