---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-273
title: 如何在Navigation页面中实现侧滑事件拦截
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在Navigation页面中实现侧滑事件拦截
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c9a7e2cdf376d1e16e12b67761eb2b124cdc81e0ce9f30c417391394481f4bc0
---

1. 因为功能以har形式集成在主工程中，没有@Entry修饰的组件，无法作为入口组件，也不能使用onBackPress生命周期函数。
2. 在使用onBackPressed时，它是NavDestination的事件，需要与NavDestination组件配合使用。组件本身用于显示导航内容区，作为子页面的根容器。因此，若需拦截子页面的返回事件，可以使用onBackPressed回调。
3. 在使用onBackPress时， 生命周期函数onBackPress只能在 @Entry 组件中使用，因此可以使用该函数拦截入口组件的返回事件。
4. 开发者可通过NavDestination组件onBackPressed回调拦截返回事件。

参考代码如下：

```
1. import { ShowDialogSuccessResponse } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct SideslipIntercept {
6. controller: TextAreaController = new TextAreaController();
7. @State text: string = '';
8. @Provide pageStack: NavPathStack = new NavPathStack();

10. build() {
11. // Main page uses NavDestination as carrier to display Navigation content area
12. Navigation(this.pageStack) {
13. }
14. .onAppear(() => {
15. this.pageStack.pushPathByName('MainPage', null, false);
16. })
17. // Create NavDestination component, use its onBackPressed callback to intercept back event
18. .navDestination(this.textArea)
19. }

21. @Builder
22. textArea(name: string) {
23. NavDestination() {
24. Column() {
25. TextArea({
26. text: this.text,
27. placeholder: 'input your word...',
28. controller: this.controller
29. })
30. .onChange((value: string) => {
31. this.text = value;
32. })
33. }
34. .justifyContent(FlexAlign.Start)
35. .width('100%')
36. .height('100%')
37. }
38. .onBackPressed(() => {
39. // Interception logic can be added here, then return true to proceed
40. this.getUIContext().getPromptAction().showDialog({
41. message: 'Save?',
42. alignment: DialogAlignment.Center,
43. buttons: [
44. {
45. text: "Don't Save",
46. color: '#0000FF'
47. },
48. {
49. text: 'Save',
50. color: '#0000FF'
51. }
52. ]
53. }).then((data: ShowDialogSuccessResponse) => {
54. // When selecting button index in buttons array, starting from 0, second index is 1
55. // Click Don't Save button
56. if (data.index === 0) {
57. console.info('Not saving')
58. }
59. // Click Save button
60. if (data.index === 1) {
61. console.info('Saving')
62. }
63. })
64. return true;
65. })
66. }
67. }
```

[SideSlipEventInterception.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SideSlipEventInterception.ets#L21-L88)

**参考链接**

[侧滑返回事件拦截案例](https://gitcode.com/HarmonyOS-Cases/cases/tree/master/CommonAppDevelopment/feature/sideslipintercept)
