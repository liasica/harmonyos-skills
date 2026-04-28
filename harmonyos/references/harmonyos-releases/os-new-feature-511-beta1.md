---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-511-beta1
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.1(19) > OS平台能力 > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:46+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:ae079b42515b4017cf25d6ffa7af5a9c752b6b7021127fc54b89de1b05921c99
---

## ArkUI

* 弹窗能力增强。包括：
  + 进一步丰富弹窗在Native侧的能力，包括：设置自定义弹窗显示的顺序、边框宽度和边框颜色等。（[API参考](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3.md)）
  + 支持通过侧滑手势关闭OverlayManager下的[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)。（[API参考](../harmonyos-references/arkts-apis-uicontext-i.md#overlaymanageroptions15)）
  + 支持设置弹窗内容和蒙层显示的过渡效果。（[API参考](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)）
  + 支持设置弹窗是否获取焦点。（[API参考](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)）

* XComponent支持在Native侧获取XComponent节点实例、注册XComponent持有的Surface的生命周期回调和触摸、鼠标、按键等组件事件回调。（[API参考](../harmonyos-references/ts-basic-components-xcomponent.md#xcomponent19)）
* 新增LazyVGridLayout组件，用于实现懒加载的网格布局。（[API参考](../harmonyos-references/ts-container-lazyvgridlayout.md)）
* Tabs支持设置子组件的最大缓存个数和缓存模式。（[API参考](../harmonyos-references/ts-container-tabs.md#cachedmaxcount19)）
* List组件支持从末尾开始布局。（[API参考](../harmonyos-references/ts-container-list.md#stackfromend19)）
* 丰富Swiper组件在Native侧的能力，包括：创建并设置数字导航指示器的样式、创建并设置导航箭头的样式等。（[API参考](../harmonyos-references/capi-native-type-h.md#oh_arkui_swiperdigitindicator_create)）
* Swiper组件支持设置圆点导航点间距和导航点底部相对于Swiper的位置。（[API参考](../harmonyos-references/ts-container-swiper.md#space19)）
* Navigation支持获取当前路由栈中的路由页面信息数组，并将数组更新为指定内容，实现路由转场。（[API参考](../harmonyos-references/ts-basic-components-navigation.md#getpathstack19)）
* 新增onNewParam回调，当栈中存在的NavDestination页面通过单实例方式移动到栈顶时，触发对应的生命周期。（[API参考](../harmonyos-references/ts-basic-components-navdestination.md#onnewparam19)）
* 属性字符串和RichEditor支持设置段落间距。（[API参考-属性字符串](../harmonyos-references/ts-universal-styled-string.md#属性-8)、[API参考-RichEditor](../harmonyos-references/ts-basic-components-richeditor.md#richeditorparagraphstyle11)）
* 支持设置关键帧动画（keyframeAnimateTo）的期望帧率。（[API参考-ArkTS](../harmonyos-references/ts-keyframeanimateto.md#keyframeanimateparam对象说明)、[API参考-C](../harmonyos-references/capi-native-animate-h.md#oh_arkui_keyframeanimateoption_setexpectedframerate)）
* 支持在按键事件发生时获取NumLock/CapsLock/ScrollLock的状态。（[API参考-ArkTS](../harmonyos-references/ts-universal-events-key.md#keyevent对象说明)、[API参考-C](../harmonyos-references/capi-native-key-event-h.md#oh_arkui_keyevent_isnumlockon)）
* 拖拽释放时，支持应用延迟返回处理结果。（[API参考](../harmonyos-references/capi-drag-and-drop-h.md#oh_arkui_dragevent_requestdragendpending)）
* 支持监听Pan手势的[onActionStart](../harmonyos-references/ts-basic-gestures-pangesture.md#事件)事件，可获取触发Pan手势事件的相关信息。（[API参考](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onbeforepanstart19)）
* 背景图支持通过NODE\_BACKGROUND\_IMAGE\_RESIZABLE\_WITH\_SLICE属性，在拉伸时可调整大小。（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）
* 针对PC/2in1设备的窗口能力新增支持更改子窗口所属的父窗口。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setparentwindow19)）
* 屏幕属性新增屏幕显示内容的显示模式枚举。该枚举在屏幕实例中传递。（[API参考](../harmonyos-references/js-apis-display.md#displaysourcemode19)）

## Performance Analysis Kit

* HiTraceMeter新增一批API，增强了HiTraceMeter的打点能力和日志能力。（[指南](../harmonyos-guides/hitracemeter.md)）
* hitrace命令新增支持“--trace\_level”参数，用于设置trace输出级别的阈值。（[指南](../harmonyos-guides/hitrace.md)）

## Camera Kit

新增支持查询和使用相机微距的能力。（[API参考](../harmonyos-references/arkts-apis-camera-macro.md)）

## CANN Kit

支持AscendC算子开发，可实现对NPU的编程。（[指南](../harmonyos-guides/cannkit-ascendc-operator-development.md)）

## Core Speech Kit

文本转语音能力新增支持音色下载。（[API参考](../harmonyos-references/hms-ai-texttospeech.md#texttospeechdownloadvoice)）

## Device Security Kit

新增支持获取诈骗应用信息。（[指南](../harmonyos-guides/devicesecurity-selectfraudapp.md)、[API参考](../harmonyos-references/devicesecurity-antifraudpicker-api.md#selectfraudapp)）

## Enterprise Data Guard Kit

* 新增支持只写模式打开[用户数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下的文件。（[API参考](../harmonyos-references/dataguard-fileguard.md#openfilewrite)）
* 新增支持设置文件自定义属性标签，方便应用对管控文件进行标识、分类。（[API参考](../harmonyos-references/dataguard-fileguard.md#setfilecustomtag)）

## Graphics Accelerate Kit

新增支持应用通过自身下载器下载资源包。（[指南](../harmonyos-guides/graphics-accelerate-assetdownload-back-self.md)、[API参考](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#appdownloadstatus)）

## Health Service Kit

新增支持在Wearable设备中调用该Kit的能力。（[指南](../harmonyos-guides/health-wearable-app-dev.md)）

## Map Kit

* 新增控制mark文字显隐能力。（[指南](../harmonyos-guides/map-marker.md#控制marker文字显隐)、[API参考](../harmonyos-references/map-map-marker.md#setannotationvisible)）
* 新增支持地图logo顶部居中和底部居中两个布局位置。（[API参考](../harmonyos-references/map-common.md#logoalignment)）
* 新增公交交通规划能力。（[指南](../harmonyos-guides/map-navi-routes.md#公共交通规划)、[API参考](../harmonyos-references/map-navi-api.md#gettransitroutes)）
* 新增地图比例尺支持公英制切换能力。（[指南](../harmonyos-guides/map-presenting.md#设置地图属性)、[API参考](../harmonyos-references/map-common.md#scaleunit)）
* 新增室内图功能，提供室内地图和楼层选择的能力。（[指南](../harmonyos-guides/map-presenting.md#室内图)、[API参考](../harmonyos-references/map-map-mapcomponentcontroller.md#setindoormapenabled)）

## MDM Kit

新增支持设置Wi-Fi黑名单、白名单能力。（[API参考](../harmonyos-references/js-apis-enterprise-wifimanager.md#wifimanageraddallowedwifilist19)）

## Payment Kit

* 新增支持实名信息验证、实名信息授权。（[指南](../harmonyos-guides/payment-real-name-verification.md)）
* 新增支持人脸核身实人验证。（[指南](../harmonyos-guides/payment-real-name-face-verification.md)）

## Pen kit

新增支持应用监听手写笔双击/轻捏事件。（[API参考](../harmonyos-references/pen-stylusinteraction.md)）

## Scan Kit

码图生成能力新增支持2in1设备。（[指南](../harmonyos-guides/scan-introduction.md#支持的设备)）

## Vision Kit

新增支持在未完成卡证识别退出的场景下，返回结果码信息。（[API参考](../harmonyos-references/vision-card-recognition.md#cardrecognition)）

## UI Design Kit

新增支持应用注册加载自定义Symbol能力。（[指南](../harmonyos-guides/ui-design-custom-symbol-res-register.md)、[API参考](../harmonyos-references/ui-design-symbolregister.md)）

## 其他

从5.1.1(19) Release开始，支持TV设备的应用开发。除通用的底座基础能力外，涉及对TV设备提供支持的Kit包括但不限于：

AppGallery Kit、CANN Kit、Cloud Foundation Kit、Game Service Kit、IAP Kit、NearLink Kit、Push Kit、Remote Communication Kit、Scan Kit、Scenario Fusion Kit、Service Collaboration Kit、Share Kit、UI Design Kit、XEngine Kit
