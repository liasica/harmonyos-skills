---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-490
title: 自定义键盘如何设置可与输入框贴边
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 自定义键盘如何设置可与输入框贴边
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:37112d22bfd4cef6b97b88ad8c6ef44ac9218cef7b1743097880e23be460cc5e
---

自定义键盘可以通过自定义弹窗来实现，自定义弹窗默认位置会和底部保持距离，可以通过设置offset来实现贴边，设置keyboardAvoidDistance来实现和键盘贴边。参考代码：

```
1. @Entry
2. @Component
3. struct CustomDialogPage {
4. @State message: string = 'CustomDialogPage';
5. customDialogController: CustomDialogController = new CustomDialogController({
6. builder: CustomEditDialogWidget({
7. inputType: InputType.Normal,
8. textInputConString: () => {
9. }
10. }),
11. alignment: DialogAlignment.Bottom,
12. maskColor: Color.White,
13. customStyle: true
14. });

16. build() {
17. Row() {
18. Column() {
19. Button(this.message).onClick(() => {
20. this.customDialogController.open();
21. });
22. }
23. .width('100%');
24. }
25. .height('100%');
26. }
27. }

29. @CustomDialog
30. @Component
31. export struct CustomEditDialogWidget {
32. controller?: CustomDialogController;
33. @State textInputString: string = '';
34. textInputConString = () => {
35. };
36. inputType: InputType = InputType.Normal;

38. build() {
39. Column() {
40. TextArea({ placeholder: 'please input' })
41. .width('80%')
42. .backgroundColor(Color.Transparent)
43. .defaultFocus(true)
44. .onChange((value: string) => {
45. this.textInputString = value;
46. });
47. }
48. .justifyContent(FlexAlign.Center)
49. .alignItems(HorizontalAlign.Start)
50. .width('80%')
51. .height(450)
52. .borderRadius(10)
53. .backgroundColor('#fffaf7f7')
54. .offset({ x: 0, y: 16 });
55. }
56. }
```

[DialogCloseToInput.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/DialogCloseToInput.ets#L21-L76)
