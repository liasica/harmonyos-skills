---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-188
title: 触摸事件的TouchEvent调用stopPropagation时无法阻止事件分发
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 触摸事件的TouchEvent调用stopPropagation时无法阻止事件分发
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:33618d2f261b8d2a5a5d5eb1dadbffc542a43d450b7ae213b107dd2fb56790c3
---

**问题现象**

当Button嵌套在另一个Button中时，外部调用stopPropagation方法无法阻止内部Button的onTouch事件触发。

```
1. Button() {
2. Button()
3. .onTouch(xx)
4. }
5. .onTouch((event: TouchEvent) => {
6. // 没有阻止内部的button触发onTouch事件
7. event.stopPropagation();
8. })
```

[TouchEventCallsStopPropagation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TouchEventCallsStopPropagation.ets#L25-L32)

**解决措施**

由于事件冒泡是从内层向外层传递的，外层按钮的stopPropagation只能阻止事件继续向外冒泡，无法影响已经触发的内层事件。因此，给外层按钮设置stopPropagation无效。若想阻止内层按钮的触摸事件，可以在外层按钮上添加.hitTestBehavior(HitTestMode.Block)。

**参考链接**

[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)
