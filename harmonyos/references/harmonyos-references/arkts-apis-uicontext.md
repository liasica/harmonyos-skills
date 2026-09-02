---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext
title: 模块描述
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > 模块描述
category: harmonyos-references
scraped_at: 2026-09-02T15:00:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a7a50ed937eafac01acf9f695a1eac2284d1ed09b8a0b3e00d513e2857622bdd
---

在Stage模型中，WindowStage/Window可以通过[loadContent](arkts-apis-window-window.md#loadcontent9)接口加载页面并创建UI实例，并将页面内容渲染到关联窗口中，因此UI实例和窗口一一关联。与具体UI实例执行上下文相关的全局UI接口，在调用时会通过追溯调用链跟踪UI上下文，确定具体的UI实例。若在非UI页面中或者未绑定当前UI上下文的异步回调中调用这类接口，可能无法跟踪到当前UI上下文，导致接口执行失败。本模块提供UIContext及其关联对象的能力，用于获取和操作指定UI实例的上下文，例如显示弹窗、页面路由、组件信息查询、媒体查询、焦点控制和拖拽控制等；也可通过[runScopedTask](arkts-apis-uicontext-uicontext.md#runscopedtask)在指定UIContext作用域内执行任务，避免因UI上下文不明确导致相关接口执行失败。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

## 导入模块

```ts
import {
  AtomicServiceBar, ComponentUtils, ContextMenuController, CursorController, DragController, Font, KeyboardAvoidMode, MediaQuery, OverlayManager,
  PromptAction, Router, UIContext, ResolvedUIContext, UIInspector, UIObserver, PageInfo, SwiperDynamicSyncScene, SwiperDynamicSyncSceneType, MeasureUtils, FrameCallback,
  OverlayManagerOptions, TargetInfo, MarqueeDynamicSyncScene, MarqueeDynamicSyncSceneType, Magnifier
} from '@kit.ArkUI';
```

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
