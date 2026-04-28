---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ffaqs-arkui-489
title: 如何解决应用键盘出现遮挡，输入框被拦截一半
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决应用键盘出现遮挡，输入框被拦截一半
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ca90803ab09d87f19e9df26b190d3e11942ecb10b2b7d49cb9cded74871bc3f3
---

为了避免组件覆盖，系统规格设计软键盘的[安全间距](../harmonyos-references/ts-universal-attributes-expand-safe-area.md)为16vp。用[offset](../harmonyos-references/js-apis-arkui-componentutils.md#offset)方法设置16vp的间距，示例代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ComponentContent } from '@kit.ArkUI';

4. class Params {
5. text: string = '';

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. @Builder
13. function buildText(params: Params) {
14. Column() {
15. TextInput({ placeholder: 'input your word...' })
16. .placeholderColor(Color.Grey)
17. .placeholderFont({
18. size: 14,
19. weight: 400
20. })
21. .caretColor(Color.Blue)
22. .fontColor(Color.Black)
23. }
24. .backgroundColor('#FFF0F0F0')
25. .borderRadius(12)
26. .height(350)
27. .width('100%')
28. .offset({
29. x: 0,
30. y: 16  // Popup window position, when y equals 16, it is just right.
31. })
32. }

34. @Entry
35. @Component
36. struct Index {
37. @State message: string = 'hello';

39. build() {
40. Row() {
41. Column() {
42. Button('click me')
43. .onClick(() => {
44. let uiContext = this.getUIContext();
45. let promptAction = uiContext.getPromptAction();
46. let contentNode = new ComponentContent(uiContext, wrapBuilder(buildText), new Params(this.message));
47. try {
48. promptAction.openCustomDialog(contentNode, {
49. alignment: DialogAlignment.Bottom,
50. offset: {
51. dx: 0,
52. dy: 0
53. }
54. });
55. } catch (error) {
56. let message = (error as BusinessError).message;
57. let code = (error as BusinessError).code;
58. console.error(`OpenCustomDialog args error code is ${code}, message is ${message}`);
59. }
60. })
61. }
62. .width('100%')
63. .height('100%')
64. }
65. .height('100%')
66. }
67. }
```

[InputBoxIsBlocked.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/InputBoxIsBlocked.ets#L21-L88)
