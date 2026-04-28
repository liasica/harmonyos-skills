---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext
title: 模块描述
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > 模块描述
category: harmonyos-references
scraped_at: 2026-04-28T08:00:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d48aae655e67f1cba462cd2eef7522335b4812661565ea8dbe7ca142a041387f
---

在Stage模型中，WindowStage/Window可以通过[loadContent](arkts-apis-window-window.md#loadcontent9)接口加载页面并创建UI的实例，并将页面内容渲染到关联的窗口中，所以UI实例和窗口是一一关联的。一些全局的UI接口是和具体UI实例的执行上下文相关的，在当前接口调用时，通过追溯调用链跟踪到UI的上下文，来确定具体的UI实例。若在非UI页面中或者一些异步回调中调用这类接口，可能无法跟踪到当前UI的上下文，导致接口执行失败。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import {
2. AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager,
3. PromptAction, Router, UIContext, ResolvedUIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MeasureUtils, FrameCallback,
4. OverlayManagerOptions, TargetInfo, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, Magnifier
5. } from "@kit.ArkUI";
```

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
