---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-503
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-29T13:23:19+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:80f3787d4bce13a8ed0fb186a7a344022f756bbd3708e3d7dc623339f91c24c1
---

## Ability Kit

* 新增支持根据指定的物理屏幕ID创建应用上下文的能力，以便于获取和使用其他带有屏幕信息。（[API参考](../harmonyos-references/js-apis-inner-application-context.md#createdisplaycontext15)）
* 新增支持通过C API拉起UIAbility的能力。仅支持PC/2in1设备。（[API参考](../harmonyos-references/capi-application-context-h.md#oh_abilityruntime_startselfuiability)）
* 新增支持应用预关闭的回调方法，可用于询问用户选择立即执行操作还是取消操作。仅支持PC/2in1设备。（[API参考-UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md#onpreparetoterminateasync15)、[API参考-AbilityStage](../harmonyos-references/js-apis-app-ability-abilitystage.md#onprepareterminationasync15)）
* 包管理应用信息（ApplicationInfo）中，应用程序安装来源（installSource）定义增强，新增ota、recovery、安装包名三类安装来源。（[API参考](../harmonyos-references/js-apis-bundlemanager-applicationinfo.md#applicationinfo-1)）

* 在C API新增组件启动参数Want的定义与接口。（[API参考](../harmonyos-references/capi-abilitybase.md)）

## Account Kit

儿童账号支持华为账号一键登录功能。（[指南](../harmonyos-guides/account-phone-unionid-login.md)）

## App Linking Kit

【新增Kit】App Linking Kit（应用链接服务）提供延迟链接能力，支持对用户点击的应用链接保存十分钟，以便当用户下载安装并打开应用时，仍能获取之前点击的该应用相关链接。（[指南](../harmonyos-guides/applinking-introduction.md)、[API参考](../harmonyos-references/applinking-deferredlink-api.md)）

## AppGallery Kit（原Store Kit）

Kit名称从Store Kit修改为AppGallery Kit，相关Kit API引用方式同步变更。（[指南](../harmonyos-guides/store-introduction.md)、[API参考](../harmonyos-references/store-moduleinstallmanager.md)）

## ArkData

* 新增应用数据向量化能力。提供端侧的数据智慧化构建，使应用数据向量化，通过嵌入模型将非结构化的文本、图像等多模态数据，转换成具有语义的向量。仅支持PC/2in1设备。（[指南](../harmonyos-guides/aip-data-intelligence-embedding.md)、[API参考](../harmonyos-references/js-apis-data-intelligence.md)）
* UDMF新增支持获取进度信息和数据的能力。（[API参考](../harmonyos-references/js-apis-data-unifieddatachannel.md#dataprogresslistener15)）
* UDMF新增支持添加指定数据类型和内容的数据，同时新增对应的查询接口。（[API参考](../harmonyos-references/js-apis-data-unifieddatachannel.md#addentry15)）

## ArkGraphics 2D

NativeBuffer支持的格式新增BLOB格式（NATIVEBUFFER\_PIXEL\_FMT\_BLOB）和RGBA16 float格式（NATIVEBUFFER\_PIXEL\_FMT\_RGBA16\_FLOAT）。（[API参考](../harmonyos-references/capi-buffer-common-h.md#oh_nativebuffer_format)）

* 新增工具类Tool，用于处理ResourceColor类型的值向common2D.Color对象的转换。（[API参考](../harmonyos-references/arkts-apis-graphics-drawing-tool.md)）
* 新增支持设置绘制字型的字体是否跟随主题字体的变化。（[API参考-C API](../harmonyos-references/capi-drawing-font-h.md#oh_drawing_fontsetthemefontfollowed)、[API参考-ArkTS API](../harmonyos-references/arkts-apis-graphics-drawing-font.md#setthemefontfollowed15)）
* 新增C API支持获取一类变换矩阵的能力，该变换矩阵根据生产端设置的旋转角度和buffer实际有效内容区域计算得出。（[API参考](../harmonyos-references/capi-native-image-h.md)）

## ArkTS

【规格更新】一个进程最多创建的运行时环境数量从16个增加到64个，并且需要满足同时运行的Worker子线程数量和进程创建的运行时的总数不超过80个。

## ArkUI

* 基础组件新增支持在已编辑文本的指定位置插入文本和删除指定区域内容的能力。（[API参考](../harmonyos-references/ts-universal-attributes-text-style.md#addtext15)）
* 通用事件新增焦点轴事件，支持对游戏手柄轴事件的响应（[API参考-C API](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_axisevent_getaxisaction)、[API参考-ArkTS API](../harmonyos-references/ts-universal-events-focus_axis.md)）；C API额外支持获取当前轴事件的操作类型的值（[API参考-C API](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_focusaxisevent_getaxisvalue)）。
* 图案密码锁组件新增支持设置未选中的宫格圆点在密码路径经过时是否自动选中。（[API参考](../harmonyos-references/ts-basic-components-patternlock.md#skipunselectedpoint15)）
* 窗口管理新增定义窗口管理的C API，主要用于设置和获取指定窗口的属性，以及设置指定窗口的状态栏样式、导航栏样式。（[API参考](../harmonyos-references/capi-oh-window-h.md)）
* Image组件新增支持可覆盖原有颜色的颜色填充能力，仅针对SVG格式的图源生效。（[API参考](../harmonyos-references/ts-basic-components-image.md#fillcolor15)）
* Image组件新增支持按图片矩阵做自动变换，在类似图库的场景呈现宫格型缩略图时提供自动的变换优化。（[API参考](../harmonyos-references/ts-basic-components-image.md#imagematrix15)）
* Tabs组件和Swiper组件新增支持设置鼠标滚轮翻页模式。（[API参考-Tabs组件](../harmonyos-references/ts-container-tabs.md#pageflipmode15)、[API参考-Swiper组件](../harmonyos-references/ts-container-swiper.md#pageflipmode15)）
* NavDestination新增支持事件返回时的回调，用于在事件返回时传参。（[API参考](../harmonyos-references/ts-basic-components-navdestination.md#onresult15)）
* TextPicker组件新增支持配置各个选择项文本样式。（[API参考](../harmonyos-references/ts-basic-components-textpicker.md#disabletextstyleanimation15)）
* Progress组件新增C API，支持线性进度条样式的设置。（[API参考](../harmonyos-references/capi-native-type-h.md#oh_arkui_progresslinearstyleoption_create)）
* 屏幕属性模块折叠屏状态枚举新增多个针对折轴二的状态定义。（[API参考](../harmonyos-references/js-apis-display.md#foldstatus10)）
* C API的Node属性样式新增背景模糊效果属性NODE\_BACKDROP\_BLUR。（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）
* FrameNode新增支持跨语言能力。（[API参考](../harmonyos-references/js-apis-arkui-framenode.md#setcrosslanguageoptions15)）
* FrameNode新增支持选择遍历节点时子节点的展开模式。（[API参考](../harmonyos-references/js-apis-arkui-framenode.md#expandmode15)）
* 尺寸设置新增支持设置宽度、高度适应父组件布局。（[API参考](../harmonyos-references/ts-universal-attributes-size.md#width15)）
* 文本组件在TextMenuItem中新增支持快捷键提示（labelInfo）。（[API参考](../harmonyos-references/ts-text-common.md#textmenuitem12对象说明)）
* 三类弹窗组件新增支持设置弹窗显示层级及相关的属性和效果（levelMode、levelUniqueId、immersiveMode）。（[API参考-列表选择弹窗](../harmonyos-references/ts-methods-action-sheet.md#actionsheetoptions对象说明)、[API参考-警告弹窗](../harmonyos-references/ts-methods-alert-dialog-box.md#alertdialogparam对象说明)、[API参考-自定义弹窗](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)）
* bindSheet新增支持圆角（radius）属性，用于设置半模态页面圆角半径；新增支持非手势切换挡位（detentSelection）属性。（[API参考](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)）
* 新增导航点组件，提供圆点导航点以及数字导航点两种导航点样式。（[API参考](../harmonyos-references/ts-swiper-components-indicator.md)）
* Swiper和Tabs组件新增支持带动画跳转的模式。（[API参考-Swiper组件C API](../harmonyos-references/capi-native-type-h.md#arkui_swiperanimationmode)、[API参考-Swiper组件ArkTS API](../harmonyos-references/ts-container-swiper.md#swiperanimationmode15枚举说明)、[API参考-Tabs组件ArkTS API](../harmonyos-references/ts-container-tabs.md#animationmode12枚举说明)）
* Swiper组件新增支持滑动行为拦截事件，可判断是否允许滑动行为。其中，C API通过属性控制，属性名NODE\_SWIPER\_EVENT\_ON\_CONTENT\_WILL\_SCROLL。（[API参考-C API](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)、[API参考-ArkTS API](../harmonyos-references/ts-container-swiper.md#oncontentwillscroll15)）
* 三方平台接入ArkUI无障碍框架新增支持查找上一个或下一个焦点（ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_NEXT\_HTML\_ITEM、ARKUI\_ACCESSIBILITY\_NATIVE\_ACTION\_TYPE\_PREVIOUS\_HTML\_ITEM）。（[API参考](../harmonyos-references/capi-native-interface-accessibility-h.md#arkui_accessibility_actiontype)）
* 三方平台接入ArkUI无障碍框架新增支持多实例场景。（[API参考](../harmonyos-references/capi-native-interface-accessibility-h.md#oh_arkui_accessibilityproviderregistercallback)）
* ohos.arkui.observer模块NavDestination组件信息新增NavDestination类型和uniqueId。（[API参考](../harmonyos-references/js-apis-arkui-observer.md#navdestinationinfo)）
* 新增支持C API的截图能力。（[API参考](../harmonyos-references/capi-native-node-h.md#oh_arkui_getnodesnapshot)）
* UIContext新增支持通过uniqueId获取已加载的组件的截图。（[API参考](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#getwithuniqueid15)）
* UIContext新增支持获取元服务menuBar相对窗口的布局信息的能力。（[API参考](../harmonyos-references/arkts-apis-uicontext-atomicservicebar.md#getbarrect15)）
* 通用事件新增C API支持获取当前触摸事件触发的ID。（[API参考](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_pointerevent_getchangedpointerid)）
* 窗口新增一个针对PC/2in1设备用于设置应用窗口尺寸限制的同名接口。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setwindowlimits15)）
* 窗口新增一个用于指定鼠标在窗口内的位置并移动窗口的同名接口。（[API参考](../harmonyos-references/arkts-apis-window-window.md#startmoving15)）
* 窗口新增针对PC/2in1设备的窗口关闭事件监听的异步回调。（[API参考](../harmonyos-references/arkts-apis-window-window.md#onwindowwillclose15)）
* 窗口新增支持开启画中画窗口尺寸变化事件的监听。（[API参考](../harmonyos-references/js-apis-pipwindow.md#onpipwindowsizechange15)）
* 窗口新增支持动态设置窗口标题栏的标题。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setwindowtitle15)）
* 窗口新增设置主窗的窗口支持模式（全屏、悬浮窗、分屏等模式）。（[API参考](../harmonyos-references/arkts-apis-window-windowstage.md#setsupportedwindowmodes15)）
* NavDestination新增支持设置是否隐藏标题栏中的返回键。（[API参考](../harmonyos-references/ts-basic-components-navdestination.md#hidebackbutton15)）
* 新增C API支持控制焦点以及处理焦点事件的能力。（[API参考](../harmonyos-references/capi-native-interface-focus-h.md)）
* 新增C API支持克隆事件的转发。（[API参考](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_pointerevent_postclonedevent)）
* Popup组件新增keyboardAvoidMode属性用于设置Popup气泡是否避让软键盘。（[API参考](../harmonyos-references/ts-universal-attributes-popup.md#popupoptions类型说明)）
* 弹窗新增支持设置避让键盘的距离。其中ArkTS API均以属性方式提供，可在链接指向的表格中搜索关键词keyboardAvoidDistance。（[API参考-C API](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2.md#setkeyboardavoiddistance)、[API参考-自定义弹窗ArkTS API](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)、[API参考-弹窗模块ArkTS API](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)）
* 属性字符串新增支持ResourceStr类型图片的设置。（[API参考](../harmonyos-references/ts-universal-styled-string.md#resourceimageattachmentoptions15)）
* 属性字符串的图片对象新增支持获取属性字符串的图片颜色滤镜效果（colorFilter）。（[API参考](../harmonyos-references/ts-universal-styled-string.md#imageattachment)）
* 拖拽能力新增支持获取拖拽进度条拖拽数据的能力。（[API参考-C API](../harmonyos-references/capi-drag-and-drop-h.md#oh_arkui_dragevent_startdataloading)、[API参考-ArkTS API](../harmonyos-references/ts-universal-events-drag-drop.md#startdataloading15)）
* 组件截图能力新增支持定义组件截图区域。（[API参考](../harmonyos-references/js-apis-arkui-componentsnapshot.md#snapshotregion15)）
* Tabs组件新增组件参数，支持设置Tabs的页签位置。（[API参考](../harmonyos-references/ts-container-tabs.md#tabsoptions15)）
* 文本类组件新增支持在文本内容将要发生变化时触发回调。（[API参考-Search组件](../harmonyos-references/ts-basic-components-search.md#onwillchange15)、[API参考-TextArea组件](../harmonyos-references/ts-basic-components-textarea.md#onwillchange15)、[API参考-TextInput组件](../harmonyos-references/ts-basic-components-textinput.md#onwillchange15)）
* 新增支持获取触摸相关的事件来自左手还是右手，涉及多个模块：
  + 事件模块新增相关C API。（[API参考](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_pointerevent_getinteractionhand)）
  + 绑定手势方法FingerInfo对象新增hand属性。（[API参考](../harmonyos-references/ts-gesture-common.md#fingerinfo8对象说明)）
  + 触摸事件TouchObject对象新增hand属性。（[API参考](../harmonyos-references/ts-universal-events-touch.md#touchobject)）
  + 点击事件clickevent对象新增hand属性。（[API参考](../harmonyos-references/ts-universal-events-click.md#clickevent)）
* 新增支持检查触摸屏幕的手指数量，涉及多个模块：
  + NDK新增相关C API。（[API参考](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_setgesturerecognizerlimitfingercount)）
  + 组件新增设置是否检查触摸屏幕的手指数量的属性isFingerCountLimited。可在各组件参考页面中查看该属性。（[API参考-长按手势事件](../harmonyos-references/ts-basic-gestures-longpressgesture.md)、[API参考-滑动手势事件](../harmonyos-references/ts-basic-gestures-pangesture.md)、[API参考-捏合手势事件](../harmonyos-references/ts-basic-gestures-pinchgesture.md)、[API参考-旋转手势事件](../harmonyos-references/ts-basic-gestures-rotationgesture.md)、[API参考-滑动事件](../harmonyos-references/ts-basic-gestures-swipegesture.md)、[API参考-单击双击和多次点击事件](../harmonyos-references/ts-basic-gestures-tapgesture.md)）
* 新增支持设置按键事件处理的优先级和重新派发的能力。涉及：
  + NDK新增设置按键事件处理优先级的C API。（[API参考](../harmonyos-references/capi-native-interface-focus-h.md#oh_arkui_focussetkeyprocessingmode)）
  + NDK中ArkUI\_NodeEventType枚举新增NODE\_DISPATCH\_KEY\_EVENT，表示组件按键事件重新派发事件（C API）。（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeeventtype)）
  + UIContext新增设置按键事件处理优先级的ArkTS API。（[API参考](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#setkeyprocessingmode15)）
  + UIContext新增分发按键事件给指定组件的ArkTS API。（[API参考](../harmonyos-references/arkts-apis-uicontext-uicontext.md#dispatchkeyevent15)）
* C API新增支持NODE\_CHECKBOX\_GROUP相关能力。可在API参考中搜索该关键字。（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）
* Navigation新增支持自定义开启或关闭单双栏显示切换时的动效。（[API参考](../harmonyos-references/ts-basic-components-navigation.md#enablemodechangeanimation15)）
* Video组件新增支持设置对快捷键的响应。（[API参考](../harmonyos-references/ts-media-components-video.md#enableshortcutkey15)）
* TextInput/TextArea/Search组件新增支持配置不拦截返回键操作（onBackPressed）的回调。（[API参考-TextInput](../harmonyos-references/ts-basic-components-textinput.md#stopbackpress15)、[API参考-TextArea](../harmonyos-references/ts-basic-components-textarea.md#stopbackpress15)、[API参考-Search](../harmonyos-references/ts-basic-components-search.md#stopbackpress15)）
* UIContext新增支持设置OverlayManager的参数，可设置是否需要渲染overlay根节点等属性。（[API参考](../harmonyos-references/arkts-apis-uicontext-uicontext.md#setoverlaymanageroptions15)）
* RichEditor新增支持设置键盘外观。（[API参考](../harmonyos-references/ts-basic-components-richeditor.md#keyboardappearance15)）
* 安全组件支持设置图标文本的对齐方式。（[API参考](../harmonyos-references/ts-securitycomponent-attributes.md#align15)）
* 安全组件支持分别设置边框四个圆角的半径。（[API参考](../harmonyos-references/ts-securitycomponent-attributes.md#borderradius15)）
* 新增C API支持组件布局完成和组件绘制完成的回调方法。（[API参考-组件布局完成回调](../harmonyos-references/capi-native-node-h.md#oh_arkui_registerlayoutcallbackonnodehandle)、[API参考-组件绘制完成回调](../harmonyos-references/capi-native-node-h.md#oh_arkui_registerdrawcallbackonnodehandle)）
* 新增C API属性样式NODE\_IMMUTABLE\_FONT\_WEIGHT，支持设置文字粗细属性不跟随系统字体粗细而变化。（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）
* 窗口新增支持获取画中画窗口的信息，如ID和尺寸。（[API参考](../harmonyos-references/js-apis-pipwindow.md#getpipwindowinfo15)）
* 窗口新增支持获取指定屏幕上可见的窗口布局的信息。（[API参考](../harmonyos-references/arkts-apis-window-f.md#windowgetallwindowlayoutinfo15)）
* 窗口新增支持获取当前窗口所在屏幕的显示大小缩放系数的信息（[API参考](../harmonyos-references/arkts-apis-window-window.md#getwindowdensityinfo15)），支持设置本窗口所处屏幕的系统显示大小缩放系数变化事件的监听（[API参考](../harmonyos-references/arkts-apis-window-window.md#onsystemdensitychange15)），支持应用主窗口自定义其显示大小缩放系数（[API参考](../harmonyos-references/arkts-apis-window-windowstage.md#setcustomdensity15)）。
* 窗口新增窗口移动选项的定义，当前可定义屏幕ID，支持在移动窗口时移动到其他屏幕。（[API参考](../harmonyos-references/arkts-apis-window-window.md#movewindowtoasync15)）
* 窗口新增定义窗口管理的C API，主要用于设置和获取指定窗口的属性，以及设置指定窗口的状态栏样式、导航栏样式。（[API参考](../harmonyos-references/capi-oh-window-h.md)）
* 文本组件公共接口的菜单属性新增TRANSLATE值，表示可对选中的文本提供翻译服务。Text/TextArea/TextInput/Search/RichEditor组件支持此菜单属性。（[API参考](../harmonyos-references/ts-text-common.md#textmenuitemid12)）
* 拖拽控制新增支持对拖拽时的自定义预览图设置是否浮起。（[API参考](../harmonyos-references/ts-universal-attributes-drag-drop.md#dragpreview15)）
* 滚动组件新增支持点击状态栏回到顶部的能力。（[API参考](../harmonyos-references/ts-container-scrollable-common.md#backtotop15)）
* 悬浮事件新增支持手写笔悬浮状态下的移动事件。（[API参考](../harmonyos-references/ts-universal-events-hover.md#onhovermove15)）

## AVCodec Kit

新增C API支持视频可变帧率的能力。（[指南](../harmonyos-guides/video-variable-refreshrate.md)）

## Background Tasks Kit

新增支持长时任务取消的监听回调。（[API参考](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanageroncontinuoustaskcancel15)）

## AppGallery Kit

新增图标管理服务，支持管理动态图标。（[指南](../harmonyos-guides/appgallery-appinfo.md)、[API参考](../harmonyos-references/appgallery-appinfomanager.md)）

## ArkWeb

新增支持对Cookie进行持久化的能力。（[API参考](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#savecookiesync15)）

## Basic Service Kit

* 上传下载新增支持使用单个上传请求上传多文件，该能力通过Config的multipart参数配置。（[API参考](../harmonyos-references/js-apis-request.md#requestagentconfig10)）
* 剪贴板新增支持设置进度指示条。（[API参考-C API](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_getdataparams_setprogressindicator)、[API参考-ArkTS API](../harmonyos-references/js-apis-pasteboard.md#progressindicator15)）
* 上传下载新增支持下载任务分组，并按分组显示通知。（[API参考](../harmonyos-references/js-apis-request.md#requestagentcreategroup15)）
* 上传下载支持的URL地址长度从2048个字符扩展到8192个字符。（[API参考](../harmonyos-references/js-apis-request.md#uploadconfig)）
* 上传下载新增支持自定义通知栏的信息。（[API参考](../harmonyos-references/js-apis-request.md#requestagentnotification15)）
* 系统账号新增支持获取账号关联的域账号信息。（[API参考](../harmonyos-references/js-apis-osaccount.md#getosaccountdomaininfo15)）

## Camera Kit

* 新增支持获取分布式相机设备的类型。（[API参考](../harmonyos-references/arkts-apis-camera-e.md#hostdevicetype15)）
* 新增支持镜像录像的能力。（[API参考](../harmonyos-references/arkts-apis-camera-videooutput.md#enablemirror15)）

## Connectivity Kit

* Wi-Fi新增支持Wi-Fi 7和Wi-Fi 7+类型的网络。（[API参考](../harmonyos-references/js-apis-wifimanager.md#wificategory12)）
* 面向企业应用开放wifiManager模块的Wi-Fi管理能力。（[API参考](../harmonyos-references/js-apis-wifimanager.md#wifimanagerenablewifi15)）
* Wi-Fi新增支持查询热点是否处于活跃状态。（[API参考](../harmonyos-references/js-apis-wifimanager.md#wifimanagerishotspotactive15)）

## Cloud Foundation Kit

新增安装预加载和周期性预加载功能，支持提前下载所需数据缓存到本地，页面打开时从本地直接获取数据渲染。（[指南](../harmonyos-guides/cloudfoundation-prefetch-overview.md)、[API参考](../harmonyos-references/cloudfoundation-cloudresprefetch.md)）

## Core File Kit

文件选择器新增支持批量授权文件的能力。（[指南](../harmonyos-guides/select-user-file.md#选择文档类文件)、[API参考](../harmonyos-references/js-apis-file-picker.md#documentselectoptions)）

* 新增原子文件的定义和操作能力。（[API参考](../harmonyos-references/js-apis-file-fs.md#atomicfile15)）
* 新增支持获取设备内置存储总大小和可用大小。（[API参考](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgettotalsize15)）
* 文件信息属性Stat新增上次访问时间（atimeNs）、上次修改时间（mtimeNs）、最近文件状态变更的时间（ctimeNs）三个属性。（[API参考](../harmonyos-references/js-apis-file-fs.md#stat)）

## Device Security Kit

* 新增支持反诈类应用获取诈骗消息。（[指南](../harmonyos-guides/devicesecurity-selectfraudmessage.md)）
* 新增支持反诈类应用获取诈骗通话记录。（[指南](../harmonyos-guides/devicesecurity-selectfraudcalllog.md)）

## Enterprise Data Guard Kit

* 新增支持在KIA文件打开时进行水印保护。（[指南](../harmonyos-guides/fileguard-set-kia-watermark.md)）
* 新增支持企业恢复密钥的管理能力。（[指南](../harmonyos-guides/dataguard-enterprise-recoverykey.md)）

## IAP Kit

* PurchaseParameter新增购买参数quantity，支持单次购买多个商品。（[API参考](../harmonyos-references/iap-iap.md#purchaseparameter)）
* 新增支持非游戏应用订单退款。（[API参考](../harmonyos-references/iap-iap.md#iapcreaterefundrequest)）

## IME Kit

新增支持移动输入法窗口的能力。（[API参考](../harmonyos-references/js-apis-inputmethodengine.md#startmoving15)）

* 新增支持查询输入法的启用状态。（[API参考](../harmonyos-references/js-apis-inputmethod.md#getinputmethodstate15)）
* 新增一系列API，用于支持输入法应用与输入框/编辑框的自定义通信。（[API参考-输入法框架](../harmonyos-references/js-apis-inputmethod.md#onmessage15)、[API参考-输入法服务](../harmonyos-references/js-apis-inputmethodengine.md#onmessage15)）

## Image Kit

* 新增从Surface id创建PixelMap对象的方法，相比原有方法，无需指定区域。（[API参考](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmapfromsurface15)）
* 新增C API支持获取Pixelmap像素数据的内存地址。（[API参考](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_accesspixels)）

## Input Kit

* 新增支持游戏手柄设备的按键事件的识别和分发。（[API参考](../harmonyos-references/js-apis-keycode.md#keycode)）
* 新增支持红外信号发射能力，应用可使用该能力与外部接收红外信号的设备进行交互。（[API参考](../harmonyos-references/js-apis-infraredemitter.md#infraredemittertransmitinfrared)）
* 新增支持Capslock灯的查询/修改，密码框可以提示用户大写已打开，输入法应用可以更新Capslock灯的状态。（[API参考](../harmonyos-references/js-apis-inputdevice.md)）

## Localization Kit

新增支持获取语言的简化表示的能力，例如将"en-Latn-US"的简化表示为"en"。（[API参考](../harmonyos-references/js-apis-i18n.md#getsimplifiedlanguage15)）

国际化支持的标准ICU C库（ICU4C）支持的语言新增Unicode字符串处理(ustring.h)、ICU文本抽象表示(utext.h)。（[API参考](../harmonyos-references/icu4c.md)）

## Map Kit

* 新增支持设置和查看Logo缩放比例。（[指南](../harmonyos-guides/map-presenting.md#logo缩放比例)）
* 新增支持在地图上显示3D地球。（[指南](../harmonyos-guides/map-presenting.md#开启3d地球)）
* 新增支持设置自定义瓦片图层。（[指南](../harmonyos-guides/map-tile.md)）
* 新增支持通过贴图的方式实现折线纹理。（[API参考](../harmonyos-references/map-map-mappolyline.md#setcustomtexture-1)）
* 新增支持Marker能力碰撞检测。（[指南](../harmonyos-guides/map-marker.md#碰撞检测)）
* 新增支持折线分段设置纹理和动态设置纹理。（[API参考](../harmonyos-references/map-map-mappolyline.md#setcustomtextureindexes)）
* 新增petalMaps模块，支持拉起花瓣地图。（[指南](../harmonyos-guides/map-petalmaps.md)、[API参考](../harmonyos-references/map-petal-maps.md)）
* 新增地图Picker支持设置主题色。（[API参考](../harmonyos-references/map-scenemap.md#locationqueryoptions)）
* 区划查询控件新增支持拉起子窗。（[API参考](../harmonyos-references/map-scenemap.md#districtselectoptions)）
* 新增支持地图Picker关闭回调。（[API参考](../harmonyos-references/map-scenemap.md#locationqueryoptions)）
* 新增支持聚合展开图标点击回调。（[API参考](../harmonyos-references/map-map-clusteroverlay.md#onmarkerclusterclick)）

## MDM Kit

* 新增支持为指定的浏览器设置浏览器托管策略。（[API参考](../harmonyos-references/js-apis-enterprise-browser.md#browsersetmanagedbrowserpolicy15)）

## Media Kit

屏幕录制新增支持获取录屏的屏幕ID的回调。（[API参考](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_setdisplaycallback)）

屏幕录制的C API新增支持设置录屏内容是否显示光标。（[API参考](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_showcursor)）

## Media Library Kit

新增支持通过photoPicker预览并替换相册中图片的能力。（[API参考](../harmonyos-references/ohos-file-photopickercomponent.md#replacephotopickerpreview15)）

## Multimodal Awareness Kit

新增支持动作感知能力，可对用户行为、动作进行感知。（[指南](../harmonyos-guides/motion-guidelines.md)、[API参考](../harmonyos-references/js-apis-awareness-motion.md)）

## Preview Kit

新增C API，支持文件打开加速功能。（[指南](../harmonyos-guides/preview-openfileboost.md)、[API参考](../harmonyos-references/openfileboost_preview.md)）

## Remote Communication Kit

新增OntimeInfo接口，在HTTP请求成功/失败时的回调，用于监听HTTP请求的成功/失败。（[API参考](../harmonyos-references/remote-communication-rcp.md#ontimeinfo)）

## Speech Kit

TextReader新增支持注销拉到播放列表底端且带用户自定义参数的回调函数。（[API参考](../harmonyos-references/speech-textreader-api.md#offtype-requestmore-1)）

## Live View Kit

* 支持配置导航模板扩展区是否显示导航方向的箭头集合图片。（[API参考](../harmonyos-references/liveview-liveviewmanager.md#navigationlayout)）
* 支持配置实况胶囊的内容是否展示。（[API参考](../harmonyos-references/liveview-liveviewmanager.md#capsuledata)）

## Network Kit

新增支持设置系统级代理自动配置（PAC）脚本地址。（[API参考-C API](../harmonyos-references/capi-net-connection-h.md#oh_netconn_setpacurl)、[API参考-ArkTS API](../harmonyos-references/js-apis-net-connection.md#connectionsetpacurl15)）

## Performance Analysis Kit

HiLog支持设置应用打印的最低日志级别。（[API参考-C API](../harmonyos-references/capi-log-h.md#oh_log_setminloglevel)、[API参考-ArkTS API](../harmonyos-references/js-apis-hilog.md#hilogsetminloglevel15)）

## Share Kit

碰一碰分享回调新增拒绝方法，支撑开发者处理异常逻辑。（[API参考](../harmonyos-references/share-harmony-share.md#reject)）

## Vision Kit

卡证识别支持设置经裁剪的卡证图片预留边距。（[API参考](../harmonyos-references/vision-card-recognition.md#cardrecognitionconfig)）

## NDK开发

新增支持基于OpenMP库的开发能力。（[指南](../harmonyos-guides/openmp-overview.md)）

## 调试调优

* 新增支持通过hdc访问debug应用的沙箱，以读取调测状态下应用沙箱中的日志及资源。（[指南](../harmonyos-guides/hdc.md#执行交互命令)）
* HiAppEvent对主线程超时事件的维测能力增强。（[指南](../harmonyos-guides/hiappevent-watcher-mainthreadjank-events.md)、[API参考](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventseteventconfig15)）
