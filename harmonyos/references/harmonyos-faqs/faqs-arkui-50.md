---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-50
title: 如何在自定义组件的构建流程里跟踪组件数据或者状态，如在build里增加日志跟踪状态变量等
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在自定义组件的构建流程里跟踪组件数据或者状态，如在build里增加日志跟踪状态变量等
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:0146956b244bcb89e846a70224dd9743a61ecaad3529de8db7ebd2f4665255c2
---

使用@Watch回调来监测状态变量的变化。如果回调函数执行，说明在下一次VSync信号发送时，使用该状态变量的UI会刷新绘制。

参考代码如下：

```
1. @Component
2. struct TotalView {
3. @Prop @Watch('onCountUpdated') count: number = 0;
4. @State total: number = 0;
5. // @Watch callback
6. onCountUpdated(propName: string): void {
7. this.total += this.count;
8. }

10. build() {
11. Text(`Total: ${this.total}`)
12. }
13. }

15. @Entry
16. @Component
17. struct CountModifier {
18. @State count: number = 0;

20. build() {
21. Column() {
22. Button('add to basket')
23. .onClick(() => {
24. this.count++;
25. })
26. TotalView({ count: this.count })
27. }
28. }
29. }
```

[TrackComponentData.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TrackComponentData.ets#L21-L49)

**参考链接**

[watch和自定义组件更新](../harmonyos-guides/arkts-watch.md#watch和自定义组件更新)
