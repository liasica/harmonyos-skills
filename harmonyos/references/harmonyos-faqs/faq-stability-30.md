---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-30
title: 应用在弹窗消失后页面暗屏，点击侧滑无响应
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用在弹窗消失后页面暗屏，点击侧滑无响应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b6bfe1348f8750920b9a7dbc3b6e26398187a2f8c9d630516c81624242205802
---

## 问题现象

应用在使用过程中，在弹窗出现并消失后，屏幕变暗，点击侧滑都无响应。

## 背景知识

[不依赖UI组件的全局自定义弹出框 (openCustomDialog)](../harmonyos-guides/arkts-uicontext-custom-dialog.md)：推荐使用UIContext中获取到的PromptAction对象提供的[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)接口在相对应用复杂的场景来实现自定义弹出框，相较于[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)优势点在于页面解耦，支持动态刷新。

## 问题定位

1. 查看hilog日志，检查到手势事件的触碰测试touch test hitted recognizer识别到的组件为Dialog。

   ```screen
   04-21 20:13:44.471 59131 59266 I C02805/com.hm.example/InputKeyFlow: [][OnPointerEvent:216] ac: down: 9015
   04-21 20:13:44.471 59131 59266 I C02805/com.hm.example/InputKeyFlow: [P:D:9015][OnPointerEvent:572] id:9015 recv
   04-21 20:13:44.471 59131 59266 I C04213/com.hm.example/InputKeyFlow: [] OnInputEvent(86): eid:68,InputId:9015,wid:47,ac:2
   04-21 20:13:44.472 59131 59266 I C04213/com.hm.example/InputKeyFlow: [] ConsumePointerEventInner(902): InputId:9015,wid:47,pointId:0,srcType:2,rect:[0,0,1224,2776],notify:1
   04-21 20:13:44.472 59131 59131 I C03951/com.hm.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:9015, fingerId:0, type=0, inject=0, isPrivacyMode=0
   04-21 20:13:44.472 59131 59131 I C03951/com.hm.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:9015, touch test hitted node info: fingerId: 0{ tag: Dialog, depth: 2 };
   04-21 20:13:44.472 59131 59131 I C03951/com.hm.example/InputKeyFlow: [(100000:100000:scope)] InputTracking id:9015, touch test hitted recognizer type info: recognizer type ClickRecognizer node info: { tag: Dialog };
   04-21 20:13:44.472 59131 59131 I C03919/com.hm.example/AceInputTracking: [(100000:100000:scope)] Consumed new event id=9015 in ace_container, lastEventInfo: id:9013
   ```
2. 往前排查，日志中可以看到曾有自定义弹窗打开open custom dialog，并且焦点也移到了Dialog上focus on focusView: Dialog。

   ```screen
   04-21 20:13:14.569 59131 59131 I C0390D/com.hm.example/AceOverlay: [(100000:100000:scope)] open custom dialog isShowInSubWindow 0
   04-21 20:13:14.569 59131 59131 I C0390F/com.hm.example/AceDialog: [(100000:100000:scope)] dialog GetContext fontScale : 1.000000
   ...
   04-21 20:13:14.726 59131 59131 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] FocusView: Dialog/907 show
   04-21 20:13:14.726 59131 59131 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] FocusView: AlertDialog/862 lost focus
   04-21 20:13:14.733 59131 59131 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Request focus on focusView: Dialog/907.
   04-21 20:13:14.734 59131 59131 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] Focus view has no default focus.
   04-21 20:13:14.734 59131 59131 I C0391C/com.hm.example/AceFocus: [(100000:100000:scope)] FocusSwitch end, Column/secure_field onBlur, BuilderProxyNode/secure_field onFocus, start: 2, end: 1, update: 2
   ```
3. 查看closeCustomDialog接口，检查所有弹窗是否正确关闭。

## 分析结论

页面弹窗未正确关闭，应用上层有弹窗的透明窗口，拦截了手势事件导致无响应。

## 修改建议

参考文档[自定义弹出框的打开与关闭](../harmonyos-guides/arkts-uicontext-custom-dialog.md#自定义弹出框的打开与关闭)中的代码示例，修改弹窗关闭逻辑。
