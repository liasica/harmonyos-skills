---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-12
title: 如何在Navigation跳转页面时返回传参
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在Navigation跳转页面时返回传参
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:01+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:56f3a76329071c8fb50a472fa63f16fa4c2bef891236ea112ed30260db8fbb37
---

在页面跳转时使用[pushPath()](../harmonyos-references/ts-basic-components-navigation.md#pushpath12)，添加onPop回调接收入栈页面出栈时的返回结果。当页面返回时，通过[pop()](../harmonyos-references/ts-basic-components-navigation.md#pop11)设置result参数并传递给目标页面，由onPop回调接收返回参数。示例代码如下：

```
1. interface paramType {
2. param: string
3. }

5. let paramA: paramType = {
6. param: 'test1'
7. }

9. @Entry
10. @Component
11. struct Index {
12. @Provide('pathInfos') pathInfos: NavPathStack = new NavPathStack();

14. @Builder
15. myRouter(name: string) {
16. if (name === 'MyFirstNavDestination') {
17. MyFirstNavDestination()
18. } else if (name === 'MySecondNavDestination') {
19. MySecondNavDestination()
20. }
21. }

23. build() {
24. Navigation(this.pathInfos) {
25. Row() {
26. Column() {
27. Text('hello world')
28. }
29. .height('100%')
30. }
31. .onClick(() => {
32. this.pathInfos.pushPathByName('MyFirstNavDestination', paramA);
33. })
34. }
35. .navDestination(this.myRouter)
36. }
37. }

39. @Component
40. export struct MyFirstNavDestination {
41. @Consume('pathInfos') pathInfos: NavPathStack;

43. getParamsPrint() {
44. console.info('param is ' + JSON.stringify(this.pathInfos.getParamByName('MyFirstNavDestination')));
45. }

47. build() {
48. NavDestination() {
49. Row() {
50. Column() {
51. Text('MyFirstNavDestination')
52. }
53. .width('100%')
54. }
55. .height('100%')
56. .onClick(() => {
57. this.pathInfos.pushPath({
58. name: 'MySecondNavDestination', param: null, onPop: (popInfo: PopInfo) => {
59. console.info(`[pushPath]last page is: ${popInfo.info.name},result: ${JSON.stringify(popInfo.result)}`);
60. }
61. });
62. })
63. }.onShown(() => {
64. this.getParamsPrint();
65. })
66. }
67. }

69. @Component
70. export struct MySecondNavDestination {
71. @Consume('pathInfos') pathInfos: NavPathStack;
72. private routerParams: paramType = { param: 'test 2' };

74. build() {
75. NavDestination() {
76. Row() {
77. Text('MySecondNavDestination')
78. }
79. .height('100%')
80. }.onBackPressed(() => {
81. this.pathInfos.pop(this.routerParams);
82. return true;
83. })
84. }
85. }
```

[JumpPageTransferParameters.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/JumpPageTransferParameters.ets#L21-L106)
