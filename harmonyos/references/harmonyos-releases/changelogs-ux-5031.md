---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-ux-5031
title: UX样式或效果的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > OS平台行为变更说明 > HarmonyOS 5.0.3(15) Beta1引入的行为变更 > UX样式或效果的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:31+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:0bba287338c672a8b41cf5b3a48b42fbf47c3e62a39619cb5c11950b17d9900d
---

说明

从HarmonyOS 5.0.3版本开始，DevEco Studio将会对涉及变更的接口进行提示，并给出链接直接跳转至变更说明对应条目。

为方便DevEco Studio索引，每条变更说明改为使用ID作为目录索引。

## 半模态SheetMode.EMBEDDED模式支持响应ESC键退出

**变更原因**

半模态SheetMode.EMBEDDED模式不支持ESC键退出，变更后，支持SheetMode.EMBEDDED模式ESC键退出。

**变更影响**

该变更涉及应用适配。

变更前：SheetMode.OVERLAY模式的半模态响应ESC键退出，SheetMode.EMBEDDED模式的半模态不响应ESC键退出。

变更后：两种模式的半模态都响应ESC键，ESC键退出与手机侧滑体验保持一致。

**起始API Level**

12

**变更的接口/组件**

bindSheet的SheetMode.EMBEDDED属性。

**适配指导**

变更后，若开发者仍不期望ESC键退出半模态，可以通过半模态的[onWillDismiss](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)回调控制是否响应ESC和侧滑关闭半模态。

```
1. onWillDismiss: ((DismissSheetAction: DismissSheetAction) => {
2. if (DismissSheetAction.reason == DismissReason.PRESS_BACK) {
3. } else {
4. DismissSheetAction.dismiss() //注册dismiss行为会关闭半模态
5. }
6. }),
```
