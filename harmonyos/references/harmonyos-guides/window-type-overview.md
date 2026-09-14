---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-type-overview
title: 窗口类型开发概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 窗口类型 > 窗口类型开发概述
category: harmonyos-guides
scraped_at: 2026-09-15T07:01:33+08:00
doc_updated_at: 2026-09-14
content_hash: sha256:d4532f9a63f20ea8c564d8b75dfd69cf0b53f378af47da2925d9b9c9322df468
---

窗口分为系统窗口、应用窗口两种类型。

## 系统窗口

系统窗口指完成系统特定功能的窗口。如音量条、壁纸、通知栏、状态栏、导航栏等。

## 应用窗口

应用窗口区别于系统窗口，指与应用显示相关的窗口，用来显示应用的内容。根据管理方式和用途的不同，应用窗口又可以分为主窗口、辅助窗口两种。

### 主窗口

主窗口由UIAbility创建时默认创建，会在“任务管理界面”中以一个独立的任务卡片显示，用于显示应用UIAbility主界面。

### 辅助窗口

辅助窗口由应用自行管理创建和销毁，不会在“任务管理界面”中以一个独立的任务卡片显示，可以用于显示应用的辅助内容，例如弹窗等。

辅助窗口包括：

* 子窗口

  Stage模型下通过[createSubWindow()](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindow9-1)或[createSubWindowWithOptions()](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindowwithoptions11)接口创建。具体可见[子窗口开发指导](subwindow-guide.md)。

  当使用[createSubWindowWithOptions()](../harmonyos-references/arkts-apis-window-windowstage.md#createsubwindowwithoptions11)接口配置zLevelAboveParentLoosened属性为true时，创建得到的子窗称为独立子窗。
* 全局悬浮窗（即WindowType.TYPE\_FLOAT），具体可见[全局悬浮窗开发指导](global-floating-window-guide.md)。
* 模态窗口（即WindowType.TYPE\_DIALOG），具体可见[模态窗口开发指导](dialog-window-guide.md)。
* [画中画](../harmonyos-references/js-apis-pipwindow.md)
* [闪控球](../harmonyos-references/js-apis-floatingball.md)
* [闪控窗](../harmonyos-references/js-apis-floatview.md)

## 闪控球和闪控窗的对比

* 共同点：闪控窗和[闪控球](../harmonyos-references/js-apis-floatingball.md)均为一种特殊的应用辅助窗口，具备在应用主窗口和对应UIAbility（应用组件）退至后台后仍然可以在前台显示的能力。可以用于应用退至后台后，使用闪控窗或闪控球继续显示UI。
* 区别：

  + 显示形式不同。闪控球以小圆球的形式展现，适用于展示关键信息。闪控窗以小型窗口展示，展示区域较大，可以持续展示应用内容或提供快捷操作。
  + 闪控球只能贴边展示，闪控窗则没有此限制。
  + 闪控球模板固定，应用不能定制UI。闪控窗同样存在模板，并由系统管理并统一绘制UI，但是提供了可绘制的区域，可供应用加载指定页面内容。
* 适用场景：

  + 闪控球适用于跨应用的题目搜索、账单记录、商品比价、抢单、翻译场景，以及金融类应用的实时盯盘场景。
  + 闪控窗适用于需要在独立小窗口中持续展示应用内容或提供快捷操作的场景。比如股市盯盘应用、直播应用。
* 联动：闪控窗和闪控球可以联合使用。通过[floatView.bind](../harmonyos-references/js-apis-floatview.md#floatviewbind)接口将闪控窗控制器与闪控球控制器绑定后，用户点击闪控球可展开为闪控窗，点击闪控窗左上角的缩小按钮可收起为闪控球，实现两种窗口形态的相互切换。

## 全局悬浮窗和闪控窗的对比

* 共同点：全局悬浮窗和闪控窗均为一种特殊的应用辅助窗口，具备在应用主窗口和对应UIAbility退至后台后仍然可以在前台显示的能力。可以用于应用退至后台后，使用全局悬浮窗或闪控窗继续显示UI。
* 区别：

  + 全局悬浮窗由开发者管理并实现UI绘制，无统一UI及动效。
  + 闪控窗由系统管理并统一绘制UI，动效更为高端精致。
  + 闪控窗支持与[闪控球](../harmonyos-references/js-apis-floatingball.md)互相绑定联合使用，实现更复杂场景。
  + 全局悬浮窗仅支持在PC/2in1设备上使用。
  + 闪控窗支持在Phone、Tablet、PC/2in1设备上使用。
* 适用场景：

  + 全局悬浮窗适用于多人视频通话、屏幕共享的场景。
  + 闪控窗适用于需要在独立小窗口中持续展示应用内容或提供快捷操作的场景。比如股市盯盘应用、手机直播应用。
  + 针对其他非指定场景，如视频播放、视频会议、视频通话等，建议使用[画中画](../harmonyos-references/js-apis-pipwindow.md)来以小窗模式呈现视频内容。
