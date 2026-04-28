---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-601
title: OS新增和增强特性
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > OS新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e7a687b75e73f60478839bd2d7a2823e23f023ac3c560f042c36de148ab26147
---

## 6.0.1(21) Release关键特性

### Ability Kit

C API新增支持设置子进程配置信息对象的uid是否隔离。（[API参考](../harmonyos-references/capi-native-child-process-h.md#oh_ability_childprocessconfigs_setisolationuid)）

### ArkUI

图像类型定义新增对内容切换时的过渡效果的定义。（[API参考](../harmonyos-references/ts-image-common.md#contenttransitioneffect21对象说明)）

### ArkWeb

* WebView的prefetchPage新增同名接口，可自定义预取行为的相关选项。（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#prefetchpage21)）
* Web组件事件新增支持网站安全风险检查结束时触发的回调。（[API参考](../harmonyos-references/arkts-basic-components-web-events.md#onsafebrowsingcheckfinish21)）

### Media Library Kit

新增PhotoPicker退出界面的上下文信息，可以用于下次使用PhotoPicker时恢复上次退出时的现场。（[API参考](../harmonyos-references/arkts-apis-photoaccesshelper-class.md#contextrecoveryinfo21)）

## 6.0.1(21) Beta1关键特性

### Ability Kit

* 新增支持通过C API获取应用版本号的能力。（[API参考](../harmonyos-references/capi-application-context-h.md#oh_abilityruntime_applicationcontextgetversioncode)）
* 拉起UIExtensionAbility的回调新增属性completionHandler，用于返回拉起指定类型的Ability组件的回调结果。（[API参考](../harmonyos-references/js-apis-inner-application-abilitystartcallback.md#abilitystartcallback-1)）
* 应用启动框架新增支持设置启动任务的调度阶段。（[指南](../harmonyos-guides/app-startup.md#设置启动任务调度阶段)）
* openLink的可选参数OpenLinkOptions新增支持传递拉起应用结果的操作类（completionHandler），用于处理拉起应用的结果。（[API参考](../harmonyos-references/js-apis-app-ability-openlinkoptions.md#openlinkoptions)）
* 包管理新增支持清理应用自身的缓存。（[API参考](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagercleanbundlecachefilesforself21)）
* C API新增支持获取可打开特定文件类型的组件资源信息列表。（[API参考](../harmonyos-references/capi-native-interface-bundle-h.md#oh_nativebundle_getabilityresourceinfo)）

### Agent Framework Kit

新增支持图标与标题呈现上下结构的胶囊按钮。（[API参考](../harmonyos-references/hmaf-function-component.md#buttontype)）

### ArkGraphics 2D

新增行高缩放基数枚举，支持设置以字号大小或字形高度作为缩放基数进行行高设置。（[API参考](../harmonyos-references/js-apis-graphics-text.md#lineheightstyle21)）

### ArkUI

* 新增支持通过图片对象说明获取属性字符串中的图片的尺寸。（[API参考](../harmonyos-references/ts-universal-styled-string.md#imageattachment)）
* RichEditor新增支持设置组件滚动条的颜色。（[API参考](../harmonyos-references/ts-basic-components-richeditor.md#scrollbarcolor21)）
* FrameNode新增支持在当前帧触发节点属性更新。（[ArkTS API参考](../harmonyos-references/js-apis-arkui-framenode.md#invalidateattributes21)、[C API参考](../harmonyos-references/capi-native-node-h.md#oh_arkui_nativemodule_invalidateattributes)、[C API指南](../harmonyos-guides/ndk-node-query-operate.md#在当前即时帧触发节点属性更新)）
* 新增支持通过C API注册目标节点的基础事件回调。（[API参考](../harmonyos-references/capi-native-node-h.md#oh_arkui_nativemodule_registercommonevent)）
* Image组件SVG新增多个解析处理能力，包括SVG易用性提升、仿射变换能力扩展、解析能力扩展、显示效果扩展。（[API参考](../harmonyos-references/ts-image-svg2-capabilities.md)）
* 新增动画控制器的相关能力。（[API参考](../harmonyos-references/js-apis-arkui-drawabledescriptor.md#animationcontroller21)）
* 新增支持发起图片资源的同步加载和异步加载，并返回加载结果。（[API参考](../harmonyos-references/js-apis-arkui-drawabledescriptor.md#loadsync21)）
* Text组件新增支持设置文本内容区在组件内的垂直对齐方式，以便在文本内容区高度大于组件高度时确保文本内容区的对齐方式正确显示。（[API参考](../harmonyos-references/ts-basic-components-text.md#textcontentalign21)）
* C API的属性样式集合ArkUI\_NodeAttributeType的枚举项增强：（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）
  + 背景图位置属性NODE\_BACKGROUND\_IMAGE\_POSITION新增属性值.value[2].?i32，表示对齐模式；新增属性值.value[3].?i32，表示布局方向。
  + 遮罩属性NODE\_OVERLAY新增属性值.value[3]?.i32，表示浮层的布局方向；新增属性值.object，表示overlay的节点树。
  + 新增属性NODE\_WIDTH\_LAYOUTPOLICY = 105，用于设置组件宽度布局策略。
  + 新增属性NODE\_HEIGHT\_LAYOUTPOLICY = 106，用于设置组件高度布局策略。
  + 新增属性NODE\_POSITION\_EDGES = 107，用于设置组件相对容器内容区边界的位置。
  + 新增属性NODE\_PIXEL\_ROUND = 109，用于设置组件的像素取整策略。
  + 新增属性NODE\_TEXT\_CONTENT\_ALIGN = 1036，用于设置文本内容区垂直对齐方式。
  + 新增属性NODE\_IMAGE\_SOURCE\_SIZE = 4013，用于设置图片解码尺寸。
  + 新增属性NODE\_IMAGE\_IMAGE\_MATRIX = 4014，用于设置图片的变换矩阵属性。
  + 新增属性NODE\_IMAGE\_MATCH\_TEXT\_DIRECTION = 4015，用于设置图片是否跟随系统语言方向。
  + 新增属性NODE\_IMAGE\_COPY\_OPTION = 4016，用于设置图片的拷贝方式。
  + 新增属性NODE\_IMAGE\_ENABLE\_ANALYZER = 4017，用于设置组件支持AI分析。
  + 新增属性NODE\_IMAGE\_DYNAMIC\_RANGE\_MODE = 4018，用于定义图片显示动态范围属性。
  + 新增属性NODE\_IMAGE\_HDR\_BRIGHTNESS = 4019，用于定义图片HDR模式下的亮度属性。
  + 新增属性NODE\_IMAGE\_ORIENTATION = 4020，用于设置图像内容的显示方向。
  + 新增属性NODE\_IMAGE\_SUPPORT\_SVG2 = 4021，用于通过启用SVG新解析能力开关设置SVG解析功能支持的范围。
  + 新增属性NODE\_IMAGE\_CONTENT\_TRANSITION = 4022，用于设置图像变化时的转场动效。
  + 新增属性NODE\_SLIDER\_BLOCK\_LINEAR\_GRADIENT\_COLOR，用于定义Slider滑块的颜色。
  + 新增属性NODE\_SLIDER\_TRACK\_LINEAR\_GRADIENT\_COLOR，用于定义Slider滑轨的背景颜色。
  + 新增属性NODE\_SLIDER\_SELECTED\_LINEAR\_GRADIENT\_COLOR，用于定义Slider滑轨的已滑动部分颜色。
* 新增ListItem划出菜单管理器，支持展开和收起指定ListItem的划出菜单。（[ArkTS API参考](../harmonyos-references/ts-container-listitem.md#listitemswipeactionmanager21)、[C API参考](../harmonyos-references/capi-native-type-h.md#oh_arkui_listitemswipeaction_expand)）
* 滚动组件通用接口增强生命周期回调事件，新增：
  + 滚动组件开始拖动时触发onWillStartDragging（[API参考](../harmonyos-references/ts-container-scrollable-common.md#onwillstartdragging21)）；
  + 滚动组件结束拖拽时触发onDidStopDragging（[API参考](../harmonyos-references/ts-container-scrollable-common.md#ondidstopdragging21)）；
  + 滚动组件将要开始Fling动效时触发onWillStartFling（[API参考](../harmonyos-references/ts-container-scrollable-common.md#onwillstartfling21)）；
  + 滚动组件结束Fling动效后触发onDidStopFling（[API参考](../harmonyos-references/ts-container-scrollable-common.md#ondidstopfling21)）；
  + 滚动组件在结束拖拽时触发OnDidStopDraggingCallback（[API参考](../harmonyos-references/ts-container-scrollable-common.md#ondidstopdraggingcallback21)）。
* NavDestination的页面显示事件onShown能力增强，新增支持通过[VisibilityChangeReason](../harmonyos-references/ts-basic-components-navdestination.md#visibilitychangereason21)说明onShown触发的原因。（[API参考](../harmonyos-references/ts-basic-components-navdestination.md#onshown10)）
* 新增支持定制CheckboxGroup内容区的方法。（[API参考](../harmonyos-references/ts-basic-components-checkboxgroup.md#contentmodifier21)）
* UIContext新增支持设置HSP资源管理对象缓存个数的上限。（[API参考](../harmonyos-references/arkts-apis-uicontext-uicontext.md#setresourcemanagercachemaxcountforhsp21)）
* 窗口管理新增支持设置窗口内容布局（不含边框和标题栏等装饰）的比例。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setcontentaspectratio21)）
* 窗口管理新增支持设置本应用进程下窗口的水印图片。（[API参考](../harmonyos-references/arkts-apis-window-f.md#windowsetwatermarkimageforappwindows21)）

### ArkWeb

* 新增支持设置Web组件是否启用强制缩放功能。（[API参考](../harmonyos-references/arkts-basic-components-web-attributes.md#forceenablezoom21)）
* WebView能力增强：
  + customizeSchemes新增同名接口，可设置接口内部是否跳过初始化WebEngine。（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#customizeschemes21)）
  + 新增支持设置（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setautopreconnect21)）和查询（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#isautopreconnectenabled21)）Web内核的自动预连接状态。
  + 新增支持设置（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setsiteisolationmode21)）和查询（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getsiteisolationmode21)）站点隔离模式。
  + 新增支持设置ArkWeb中已使用过的空闲socket的超时时间。（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setsocketidletimeout21)）
* Web组件的自定义菜单扩展项新增onMenuShow和onMenuHide事件回调。（[API参考](../harmonyos-references/arkts-basic-components-web-i.md#selectionmenuoptionsext13)）
* Web组件的枚举属性增强：
  + 网页元素信息WebElementType新增枚举TEXT，表示网页元素为文本或可编辑区域类型。（[API参考](../harmonyos-references/arkts-basic-components-web-e.md#webelementtype13)）
  + 菜单响应类型WebResponseType新增枚举RIGHT\_CLICK，表示通过鼠标右键触发菜单弹出。（[API参考](../harmonyos-references/arkts-basic-components-web-e.md#webresponsetype13)）

### Asset Store Kit

关键资产删除时机的规则优化。从API 21开始，应用卸载时清除存储在ASSET中的非群组数据，群组数据调整为仅在群组内所有应用卸载时清除。（[指南](../harmonyos-guides/asset-store-kit-overview.md#约束与限制)）

### Audio Kit

* 音频返听能力增强，新增支持设置音频返听器的混响模式（[API参考](../harmonyos-references/arkts-apis-audio-audioloopback.md#setreverbpreset21)）、获取当前音频返听器的混响模式（[API参考](../harmonyos-references/arkts-apis-audio-audioloopback.md#getreverbpreset21)）、设置音频返听器的均衡器类型（[API参考](../harmonyos-references/arkts-apis-audio-audioloopback.md#setequalizerpreset21)）、获取当前音频返听器的均衡器类型（[API参考](../harmonyos-references/arkts-apis-audio-audioloopback.md#getequalizerpreset21)）。
* 新增支持查询指定录音流类型的智能降噪开关是否已开启。（[ArkTS API参考](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isintelligentnoisereductionenabledforcurrentdevice21)、[C API参考](../harmonyos-references/capi-native-audio-stream-manager-h.md#oh_audiostreammanager_isintelligentnoisereductionenabledforcurrentdevice)）

### Background Tasks Kit

* 新增支持申请长时任务的同名接口，新接口支持同一时间申请多个长时任务。（[指南](../harmonyos-guides/continuous-task.md#约束与限制)、[API参考](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstartbackgroundrunning21)）
* 针对上述接口申请的长时任务，配套新增更新长时任务的接口。（[API参考](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerupdatebackgroundrunning21)）
* 新增支持取消指定ID的长时任务。（[API参考](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerstopbackgroundrunning21)）

### Basic Services Kit

* 系统时间：新增支持获取自动设置时间的开关的状态。（[API参考](../harmonyos-references/js-apis-date-time.md#systemdatetimegetautotimestatus21)）
* 设备信息：常量定义中新增设备CPU芯片型号（chipType）和设备重启次数（bootCount）。（[API参考](../harmonyos-references/js-apis-device-info.md#常量)）
* 上传下载：通知栏的自定义信息新增支持设置任务的显示方式（visibility）。（[API参考](../harmonyos-references/js-apis-request.md#requestagentnotification15)）
* 剪贴板：当使用延迟复制功能的应用退出时，支持应用主动通知剪贴板获取所有延迟数据。（[指南](../harmonyos-guides/pasteboard-time-lapse-copy-and-paste.md#使用基于record级别的延迟复制粘贴)、[API参考](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_syncdelayeddataasync)）

### Camera Kit

* 新增支持设置拍照画质优先策略。（[API参考](../harmonyos-references/arkts-apis-camera-photooutput.md#setphotoqualityprioritization21)）

### Cloud Foundation Kit

* 新增支持调试本地云函数。（[指南](../harmonyos-guides/cloudfoundation-debug-local-function.md)、[API参考](../harmonyos-references/cloudfoundation-cloudfunction.md#functionparams)）
* 云数据库模块新增支持以随机顺序展示查询结果集中的对象。（[指南](../harmonyos-guides/cloudfoundation-database-query.md#随机查询)、[API参考](../harmonyos-references/cloudfoundation-clouddatabase.md#orderbyrandom)）

### Connectivity Kit

新增支持通过C API获取设备真实Mac地址。（[API参考](../harmonyos-references/capi-oh-wifi-h.md#oh_wifi_getdevicemacaddress)）

### Crypto Architecture Kit

新增支持开启硬件熵源的能力。（[API参考](../harmonyos-references/js-apis-cryptoframework.md#enablehardwareentropy21)）

### Device Security Kit

新增支持拉起系统级防窥蒙层对窗口敏感内容进行覆盖。（[指南](../harmonyos-guides/devicesecurity-dlpantipeep.md)、[API参考](../harmonyos-references/devicesecurity-dlpantipeep-api.md#setantipeepmasklayer)）

### Enterprise Space Kit

空间管理服务场景下，新增支持设置系统服务进程不可访问后台用户数据、获取系统服务进程不可访问的后台用户数据状态、获取不可访问后台用户数据的系统服务进程列表、新增不可访问后台用户数据的系统服务进程列表、删除不可访问后台用户数据的系统服务进程列表功能。（[指南](../harmonyos-guides/enterprisespace-spacemanager-guide.md)、[API参考](../harmonyos-references/enterprisespace-spacemanager.md)）

### Game Controller Kit

【新增Kit】Game Controller Kit（游戏控制器服务）支持游戏类应用适配控制器外设（如游戏手柄），解决玩家操控性问题，保障用户体验。游戏开发者可通过接入该服务实现游戏外设的上下线和按键及轴事件监听等功能。（[指南](../harmonyos-guides/game-controller-introduction.md)、[API参考](../harmonyos-references/game-controller-api.md)）

### Game Service Kit

新增支持小游戏相关能力，包括小游戏登录和小游戏支付。（[指南](../harmonyos-guides/gameservice-gameplayer-minigame.md)、[API参考](../harmonyos-references/gameservice-gameplayer.md)）

### IME Kit

新增支持获取指定屏幕当前状态（例如：折叠或展开）下输入法软键盘相对系统面板的偏移区域。（[指南-详见步骤2](../harmonyos-guides/inputmethod-application-guide.md#文件介绍)、[API参考](../harmonyos-references/js-apis-inputmethodengine.md#getsystempanelcurrentinsets21)）

### Input Kit

* 全局快捷键模块的按键事件消费设置新增支持识别媒体播放的播放/暂停（KEYCODE\_MEDIA\_PLAY\_PAUSE）、下一首（KEYCODE\_MEDIA\_NEXT）、上一首（KEYCODE\_MEDIA\_PREVIOUS）的快捷键。（[API参考](../harmonyos-references/js-apis-inputconsumer.md#keypressedconfig16)）
* C API新增如下能力的相关接口：
  + 获取按键事件的Id。（[API参考](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_getkeyeventid)）
  + 添加（[API参考](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_addkeyeventhook)）和移除（[API参考](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_removekeyeventhook)）按键事件拦截钩子函数。
  + 重新分发按键事件。（[API参考](../harmonyos-references/capi-oh-input-manager-h.md#oh_input_dispatchtonexthandler)）

### Localization Kit

新增支持在开发者模式下通过param工具的“param get persist.global.language”命令获取系统语言。（[指南](../harmonyos-guides/i18n-system-language-region.md)）

### Location Kit

新增支持判断指定的BSSID是否存在于最新的WLAN扫描结果里。（[API参考](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageriswlanbssidmatched21)）

### Map Kit

* 新增支持更改我的位置图层相对于覆盖物的压盖顺序。（[指南](../harmonyos-guides/map-location.md#更改我的位置图层相对于覆盖物的压盖顺序)、[API参考](../harmonyos-references/map-map-mapcomponentcontroller.md#changemylocationlayerorder)）
* 新增支持拉起地图应用的打车页面。（[指南](../harmonyos-guides/map-petalmaps.md#打开地图应用打车页面)、[API参考](../harmonyos-references/map-petal-maps.md#openmaptaxi)）
* 地图应用的POI详情页面，新增设置地图缩放级别和地图坐标系类型。（[API参考](../harmonyos-references/map-petal-maps.md#poidetailparams)）
* 路线规划场景下，新增支持设置地图坐标系类型。（[API参考](../harmonyos-references/map-petal-maps.md#routeplanparams)）
* 导航场景下，新增支持设置起点信息和地图坐标系类型。（[API参考](../harmonyos-references/map-petal-maps.md#naviparams)）
* 打开地图应用规划路线或导航，新增支持公交类型。（[API参考](../harmonyos-references/map-petal-maps.md#vehicletype)）

### MDM Kit

* 企业应用的应用管理（[API参考](../harmonyos-references/js-apis-enterprise-applicationmanager.md)）和包管理（[API参考](../harmonyos-references/js-apis-enterprise-bundlemanager.md)）的相关接口在需要传入appIds参数时均新增支持使用appIdentifier参数作为入参，代替原先使用appId的方式。可在对应模块的API参考中搜索“appIds”了解详情。
* 可设置禁用/启用的特性新增如下（[API参考](../harmonyos-references/js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)）：
  + 应用分身能力（appClone）
  + 外置存储能力（externalStorageCard）
  + Wi-Fi链接时使用随机MAC（randomMac）
* 新增支持应用运行允许名单，添加至允许名单的应用允许在指定用户下运行，不在允许名单的应用不允许在指定用户下运行。（[API参考](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageraddallowedrunningbundles21)）

  同时调整了应用运行禁止名单的策略，如果应用运行允许名单addallowedRunningBundles非空，就不能再通过接口添加应用到应用运行禁止名单。（[API参考](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageradddisallowedrunningbundlessync)）

### Media Kit

* 媒体信息描述的枚举新增视频原始宽度（MD\_KEY\_ORIGINAL\_WIDTH）和视频原始高度（MD\_KEY\_ORIGINAL\_HEIGHT）两个信息。（[API参考](../harmonyos-references/arkts-apis-media-e.md#mediadescriptionkey8)）
* 新增支持通过C API设置播放器的媒体源。（[API参考](../harmonyos-references/capi-avplayer-h.md#oh_avplayer_setdatasource)）

### NearLink Kit

新增支持获取已配对设备列表。（[API参考](../harmonyos-references/nearlink-manager.md#getpaireddevices)）

### Online Authentication Kit

FIDO新增支持业务切换自定义认证方式。（[API参考](../harmonyos-references/onlineauthentication-fido-api.md#uafmessage)）

### PDF Kit

新增搜索关键词API，开发者可以对PDF文档进行搜索，并获取上下文、关键词位置等信息。（[API参考](../harmonyos-references/pdf-arkts-pdfservice.md#searchkey)）

### Remote Communication Kit

* 发送简单的HTTP表单数据场景下，新增支持按照键列表的先后顺序发送。（[指南](../harmonyos-guides/remote-communication-netsend-arkts.md#如何使用form发送http简单的表格数据)、[API参考](../harmonyos-references/remote-communication-rcp.md#form)）
* 发送HTTP多部分表格数据时，新增支持按照键列表的先后顺序发送。（[指南](../harmonyos-guides/remote-communication-netsend-arkts.md#如何使用multipartform发送http多部分表格数据)、[API参考](../harmonyos-references/remote-communication-rcp.md#multipartform)）
* 新增C API，支持监听响应状态码的功能。（[API参考](../harmonyos-references/remote-communication-overview.md#hms_rcp_setrequestonstatuscodereceivecallback)）

### Scenario Fusion Kit

新增支持关注组件API，开发者可在应用页面展示服务号关注组件，实现用户点击关注按钮可关注对应服务号。（[指南](../harmonyos-guides/scenario-fusion-api-followcomponent.md)、[API参考](../harmonyos-references/scenario-fusion-atomicservice.md#showfollowcomponent)）

### Share Kit

新增支持宿主应用配置目标应用名单。（[指南](../harmonyos-guides/share-app-sharing-mode.md)）

### Spatial Recon Kit

【新增Kit】Spatial Recon Kit（空间建模套件）集成了3DGS（3D Gaussian Splatting）模型的渲染、运算等能力，支持3DGS模型的加载和渲染功能、3DGS渲染的复古风格、漫画风格和比特风格特效。（[指南](../harmonyos-guides/spatial-recon-introduction.md)、[API参考](../harmonyos-references/spatial-recon-gsnode.md)）

### Speech Kit

* 朗读控件记录上次播放位置，用于下次继续播放。（[API参考](../harmonyos-references/speech-textreader-api.md#readprogress)、[API参考](../harmonyos-references/speech-textreader-api.md#startparams)）
* 朗读控件悬浮框新增支持是否显示倍速播放按钮以及是否显示下一篇按钮。（[API参考](../harmonyos-references/speech-textreader-api.md#minibarparams)）

### Telephony Kit

新增支持订阅通话状态变化拓展事件。（[API参考](../harmonyos-references/js-apis-observer.md#observeroncallstatechangeex21)）

### UI Design Kit

HdsNavigation提供标题栏顶部自定义区域。（[API参考](../harmonyos-references/ui-design-hdsnavigation.md#titlebarcontentoptions)）
