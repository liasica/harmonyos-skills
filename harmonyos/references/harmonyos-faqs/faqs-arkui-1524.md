---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1524
title: 提示框无法弹出
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 提示框无法弹出
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:93e04edd0e1ce1185639e1cbf9fddfdcf7ee02ed53117b6675b4a01ce3ab6a24
---

## 问题现象

功能运行成功后，本应弹出运行成功的提示框，然而没有弹出提示框。

## 背景知识

* [promptAction.showToast](../harmonyos-references/js-apis-promptaction.md#promptactionshowtoastdeprecated)：创建并显示文本提示框。从API version 18开始废弃，且直接使用showToast可能导致UI上下文不明确的问题。
* UI上下文不明确是指调用ArkUI全局接口时，调用点无法明确指定UI实例的问题。

## 问题定位

1. 功能运行成功后，输出如下日志，从第6、7行日志可知因为生命周期异常，提示框创建失败。

   ```shell
   C03926/com.example/AceTheme               W     [(1000000:1000000:scope)] style -1 not contains toast_pattern!
   C03903/com.example/AceSubWindow           I     [(1000000:1000000:scope)] show toast, window parent id is 1000000
   C03903/com.example/AceSubWindow           I     [(-1:100000:singleton)] Toast posX: 0, posY: 0, width: 3120, height: 2080, density: 1.900000
   C04200/com.example/WindowSceneSessionImpl I     (139)WindowSceneSessionImpl: [WMSCom] Constructor ARK_APP_SUBWINDOW_TOAST_DIALOG_0
   C0420A/com.example/WMSLife                I     [] Create(560): Window Create name:ARK_APP_SUBWINDOW_TOAST_DIALOG_0, state:0, mode:1
   C0420A/com.example/WMSLife                I     [] CreateAndConnectSpecificSession(324): create specific failed, session is nullptr, name: ARK_APP_SUBWINDOW_TOAST_DIALOG_0
   C0420A/com.example/WMSLife                I     [] RecordLifeCycleExceptionEvent(509): window life cycle exception: life cycle is abnormal: window_name: ARK_APP_SUBWINDOW_TOAST_DIALOG_0, id:0, event: CREATE, errCode: 1001;
   C04200/com.example/WindowSceneSessionImpl I     (144)~WindowSceneSessionImpl: [WMSCom] Destructor 0, ARK_APP_SUBWINDOW_TOAST_DIALOG_0
   C01406/com.example/OHOS::RS               I     RSSurfaceNode::~RSSurfaceNode, Node: 108353434943740, Name: ARK_APP_SUBWINDOW_TOAST_DIALOG_0
   C03903/com.example/AceSubWindow           W     [(-1:100000:singleton)] init toast dialog window failed
   C03903/com.example/AceSubWindow           W     [(1000000:1000000:scope)] can not find systemTopMost window when clear system toast
   ```
2. 排查提示框创建逻辑，发现是在异步方法中用promptAction.showToast创建的提示框。

## 分析结论

在异步方法中用promptAction.showToast创建提示框会出现UI上下文不明确的情况。

## 修改建议

使用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)获取PromptAction实例，再通过此实例调用替代方法[showToast](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showtoast)。
