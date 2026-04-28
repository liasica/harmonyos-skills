---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-30
title: 如何获取UI组件的显示或隐藏状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取UI组件的显示或隐藏状态
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:05+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:fbdb8270f1d07b0c001b438b80bc45271eac9e0716e325befc31f7fcb59223ce
---

* 方法1：使用if条件渲染，通过变量控制组件的显隐。使用@Watch监听变量，可以判断组件的显示状态。
* 方法2：组件显示或隐藏时，生命周期方法 aboutToAppear() 和 aboutToDisappear() 会触发，可以感知组件的显示状态。

具体可参考示例代码：

```
1. @Component
2. struct ComponentA {
3. aboutToAppear(): void {
4. // Perception components are visible and hidden
5. console.log('Component A display');
6. }

8. aboutToDisappear(): void {
9. // Perception components are visible and hidden
10. console.log('Component A hidden');
11. }

13. build() {
14. Column() {
15. Text('Component A').fontSize(16).fontColor(Color.Black);
16. }
17. .width(100)
18. .height(50)
19. }
20. }

22. @Entry
23. @Component
24. struct ComponentB {
25. @State @Watch('onCompAShowStatusChange') isShowA: boolean = false;
26. onCompAShowStatusChange() {
27. // Perception components are visible and hidden
28. console.log('Monitor component A：' + `${this.isShowA ? 'display' : 'hide'}`);
29. }

31. build() {
32. Column() {
33. Button('Switch between visible and hidden').type(ButtonType.Normal).width(100).height(50).onClick(() => {
34. this.isShowA = !this.isShowA;
35. })
36. if (this.isShowA) {
37. ComponentA();
38. }
39. }
40. }
41. }
```

[GetUIComponentStatus.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetUIComponentStatus.ets#L21-L61)

**参考链接**

[@Watch装饰器：状态变量更改通知](../harmonyos-guides/arkts-watch.md)、[if/else：条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)
