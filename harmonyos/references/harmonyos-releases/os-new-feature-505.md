---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-505
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.5(17) > OS平台能力 > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a880ee489a6d1927548ade997e586dfcd92762b07d29c81e85448843f7eb8197
---

## Ability

* 新增支持通过startAbility的属性StartOptions来指定创建新窗口的大小（minWindowWidth、minWindowHeight、maxWindowWidth、maxWindowHeight）。（[API参考](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)）
* C API新增支持启动Ability时传递StartOptions。（[API参考](../harmonyos-references/capi-start-options-h.md)）
* C API新增支持获取子进程启动参数。（[指南](../harmonyos-guides/capi-nativechildprocess-development-guideline.md#子进程获取启动参数)、[API参考](../harmonyos-references/capi-native-child-process-h.md#oh_ability_getcurrentchildprocessargs)）
* C API新增支持设置启动Ability时窗口和dock栏图标的显示模式。（[API参考](../harmonyos-references/capi-start-options-h.md)）

## ArkData

UDMF新增支持将传入的data转换成多样式数据结构的能力。若原data使用多个record去承载同一份数据的不同样式，则可以使用此接口将原data转换为多样式数据结构。（[API参考](../harmonyos-references/js-apis-data-unifieddatachannel.md#unifieddatachannelconvertrecordstoentries17)）

## AR Engine

新增深度估计，提供三维感知能力，可实现测量、体积估算等。（[指南](../harmonyos-guides/arengine-c-get-depth.md)）

## ArkUI

* 新增鼠标轴事件相关接口。（[API参考-ArkTS](../harmonyos-references/ts-universal-events-axis.md)、[API参考-C API](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_axisevent_setpropagation)）
* NavDestination新增onActive和onInactive生命周期。（[API参考](../harmonyos-references/ts-basic-components-navdestination.md#onactive17)）
* C API的事件能力增强，新增支持获取事件命中的组件的宽度、高度、X坐标、Y坐标等能力。（[API参考](../harmonyos-references/capi-ui-input-event-h.md#oh_arkui_uiinputevent_geteventtargetwidth)）
* 基础类型定义新增支持清除当前的预上屏文本内容。（[API参考](../harmonyos-references/ts-universal-attributes-text-style.md#clearpreviewtext17)）
* UIContext新增支持创建不依赖窗口的UI实例。（[API参考](../harmonyos-references/arkts-apis-uicontext-uicontext.md#createuicontextwithoutwindow17)）
* 组件可见区域变化事件新增支持设置事件的回调参数，限制它的执行间隔。（[API参考-ArkTS](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareaapproximatechange17)、[API参考-C API](../harmonyos-references/capi-native-type-h.md#oh_arkui_visibleareaeventoptions_create)）
* ImageAnimator组件支持设置是否通过系统onVisibleAreaChange的可见性来判断组件的暂停和播放。（[API参考](../harmonyos-references/ts-basic-components-imageanimator.md#monitorinvisiblearea17)）
* 画中画窗口支持通过创建参数LocalStorage实现页面级别的UI状态存储单元，多实例下可用来跟踪主窗实例。（[API参考](../harmonyos-references/js-apis-pipwindow.md#pipconfiguration)）
* 针对PC/2in1设备的窗口管理新增支持主窗的尺寸记忆功能。（[API参考](../harmonyos-references/arkts-apis-window-windowstage.md#setwindowrectautosave17)）
* 针对PC/2in1设备和平板设备的窗口管理新增支持设置子窗或悬浮窗窗口边缘阴影的模糊半径。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setwindowshadowradius17)）
* 针对PC/2in1设备和平板设备的窗口管理新增支持设置子窗口在其父窗口处于拖拽移动或拖拽缩放过程时，该子窗口是否支持跨多个屏幕同时显示。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setfollowparentmultiscreenpolicy17)）

## Audio Kit

新增支持Float32音频流采样格式。（[API参考](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_sampleformat)）

## AVCodec Kit

视频解码新增支持MPEG2、MPEG4、H.263的软件解码。（[指南](../harmonyos-guides/avcodec-support-formats.md)）

## AVSession Kit

新增支持单句/单条歌词展示的属性singleLyricText。（[API参考](../harmonyos-references/arkts-apis-avsession-i.md#avmetadata10)）

## Background Tasks Kit

新增后台子进程管理模块，提供应用对子进程进行压制、解压制的能力，避免子进程过多占用系统资源，导致系统使用卡顿。（[API参考](../harmonyos-references/js-apis-backgroundprocessmanager.md)）

## Connectivity Kit

蓝牙socket模块新增支持通过clientSocket获取对端设备地址的能力。（[API参考](../harmonyos-references/js-apis-bluetooth-socket.md#socketgetdeviceid17)）

## File Manager Service Kit

【新增Kit】File Manager Service Kit（文件管理服务）为开发者提供文件管理相关能力，开发者通过File Manager Service Kit完成文件删除到回收站、获取文件图标等功能，满足用户对文件管理的多样性诉求。（[指南](../harmonyos-guides/filemanagerservice-introduction.md)、[API参考](../harmonyos-references/filemanagerservice-arkts-filemanagerservice.md)）

## IME Kit

输入法框架新增支持设置显示预览文本时的回调（[API参考](../harmonyos-references/js-apis-inputmethod.md#setpreviewtextcallback17)），支持订阅输入法应用操作文本预览内容的事件（[API参考](../harmonyos-references/js-apis-inputmethod.md#onsetpreviewtext17)）。

## Media Kit

调用媒体播放器AVPlayer设置播放策略时，新增支持Prepare之后显示视频起播首帧（showFirstFrameOnPrepare）。（[API参考](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)）

## Payment Kit

新增引导用户绑卡能力。（[指南](../harmonyos-guides/payment-partner-bindcard.md)、[API参考](../harmonyos-references/payment-paymentservice.md#paymentservicerequestbindcard)）

## PDF Kit

新增支持对PDF文档进行加密。（[API参考](../harmonyos-references/pdf-arkts-pdfservice.md#setpdfpassword)）

## Preview Kit

新增文件打开加速预加载状态感知能力。（[指南](../harmonyos-guides/preview-openfileboost-stateawareness.md)、[API参考](../harmonyos-references/preview-arkts-openfileboost-api.md#openfileboostaddfile)）

## Vision Kit

文档扫描结果回调接口增加状态码，用于判断输入图片uris是否全部无效。（[API参考](../harmonyos-references/vision-document-scanner.md#documentscannerresultcallback)）

## 配置文件

配置文件module.json5新增Hook配置：通过abilitySrcEntryDelegator可标识当前Module需要Hook的UIAbility的名称，通过abilityStageSrcEntryDelegator可标识当前Module需要Hook的AbilityStage（其值配置为对应Module的名称），两者组合使用，共同指定Hook的目标对象。（[指南](../harmonyos-guides/module-configuration-file.md#配置文件标签)）
