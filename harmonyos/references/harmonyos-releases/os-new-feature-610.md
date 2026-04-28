---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-610
title: OS新增和增强特性
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > OS新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8cd70c78f9748f20257c21d42c0d1f83c78842d0973286bdeae1b8e375919d7f
---

## 6.1.0(23) Release新增关键特性

6.1.0(23) Release在Beta2版本基础上未引入新增特性。

## 6.1.0(23) Beta2新增关键特性

### Ability Kit

BundleInfo新增buildVersion。（[API参考](../harmonyos-references/js-apis-bundlemanager-bundleinfo.md#bundleinfo-1)）

### ArkUI

* 新增支持设置自定义键盘在输入框之间切换时是否接续（即不收回）。（[API参考](../harmonyos-references/arkts-apis-uicontext-uicontext.md#setcustomkeyboardcontinuefeature23)）
* 跑马灯ArkTS API的初始化参数新增两轮跑马灯之间的间距“spacing”和每次滚动的时间间隔“delay”。（[API参考](../harmonyos-references/ts-basic-components-marquee.md#marqueeoptions18对象说明)）
* 跑马灯C API新增[设置](../harmonyos-references/capi-native-type-h.md#oh_arkui_textmarqueeoptions_setspacing)和[获取](../harmonyos-references/capi-native-type-h.md#oh_arkui_textmarqueeoptions_getspacing)间距、[设置](../harmonyos-references/capi-native-type-h.md#oh_arkui_textmarqueeoptions_setloop)和[获取](../harmonyos-references/capi-native-type-h.md#oh_arkui_textmarqueeoptions_getloop)重复滚动次数、[设置](../harmonyos-references/capi-native-type-h.md#oh_arkui_textmarqueeoptions_setfromstart)和[获取](../harmonyos-references/capi-native-type-h.md#oh_arkui_textmarqueeoptions_getfromstart)运行方向、[设置](../harmonyos-references/capi-native-type-h.md#oh_arkui_textmarqueeoptions_setdelay)和[获取](../harmonyos-references/capi-native-type-h.md#oh_arkui_textmarqueeoptions_getdelay)滚动时间间隔的能力。
* 组件布局位置设置新增定义在相对容器中子组件在[水平方向](../harmonyos-references/ts-universal-attributes-location.md#horizontalalignparam23对象说明)和[垂直方向](../harmonyos-references/ts-universal-attributes-location.md#verticalalignparam23对象说明)上的对齐规则。
* 滚动组件新增模拟拖拽功能，支持开启/关闭模拟拖拽功能、设置模拟拖拽距离以及获取是否处于模拟拖拽状态的能力。（[ArkTS API参考](../harmonyos-references/ts-container-swiper.md#startfakedrag23)、[C API参考](../harmonyos-references/capi-native-node-h.md#oh_arkui_swiper_startfakedrag)）

### Basic Services Kit

* 新增用于消除API产生的告警的API注解能力。在源码用此注解后，编译时会根据配置的规则来抑制对应警告。（[API参考](../harmonyos-references/js-apis-annotation.md#suppresswarnings23)）
* 新增支持查询免打扰的相关功能的开启状态。（[API参考](../harmonyos-references/js-apis-intelligentscene.md)）

### Connectivity Kit

新增支持带有卡在位状态周期性检测的NFC Tag读卡事件订阅能力。（[API参考](../harmonyos-references/js-apis-nfctag.md#tagon23)）

### Graphics Accelerate Kit

游戏渲染加速服务新增支持TV设备（[指南](../harmonyos-guides/graphics-accelerate-introduction.md#支持的设备)）。

### Share Kit

新增支持阅读分享功能，即选中文本进行分享时，分享面板同时显示图片分享和文本分享，用户可选择图片或文本进行分享。（[API参考](../harmonyos-references/share-system-share.md#readingextendedsharerecorddata)）

### Spatial Recon Kit

3D空间重建场景下，新增支持空间重建会话管理、3DGS（3D Gaussian Splatting）场景建模、任务控制、进度查询以及三维模型文件导出功能。（[API参考](../harmonyos-references/capi-spatial-recon-interface-h.md)）

## 6.1.0(23) Beta1新增关键特性

开发套件Beta (基于API 23) 新增如下关键特性，开发者可通过新增的API调用相应特性的能力。完整的API新增请参见[API变更清单](apidiff-610.md)。

### Ability Kit

* 应用程序包管理新增支持对Native软件包（hnp）进行独立签名的能力。可通过module.json5配置文件的hnpPackages标签进行标识。（[指南](../harmonyos-guides/module-configuration-file.md#hnppackages标签)）
* 在启动参数中提供UIAbility开始启动的时间戳（launchUTCTime和launchUptime），应用获取后可用于计算启动时间。（[API参考](../harmonyos-references/js-apis-app-ability-abilityconstant.md#launchparam)）

### AppGallery Kit

应用归因服务新增支持PC/2in1、TV设备。（[指南](../harmonyos-guides/store-attribution-introduction.md#约束与限制)）

### App Linking Kit

* 新增支持配置应用链接跳转的优先级。（[指南](../harmonyos-guides/app-linking-startupapp.md#建立域名与应用关联关系)）
* 延迟链接新增支持PC/2in1设备。（[指南](../harmonyos-guides/applinking-deferredlink.md#约束与限制)）

### AR Engine

* 新增支持人脸识别与跟踪能力。（[指南-ArkTS](../harmonyos-guides/arengine-face.md)、[指南-C/C++](../harmonyos-guides/arengine-c-face.md)）
* 新增支持人体骨骼关键点识别与跟踪能力。（[指南-ArkTS](../harmonyos-guides/arengine-body.md)、[指南-C/C++](../harmonyos-guides/arengine-c-body.md)）

### ArkTS

util模块新增接口ArkTSVM.setMultithreadingDetectionEnabled，支持开启或关闭多线程检测能力。（[API参考](../harmonyos-references/js-apis-util.md#setmultithreadingdetectionenabled23)）

### ArkUI

* FrameNode提供查询节点是否在渲染树上的能力。（[API参考](../harmonyos-references/js-apis-arkui-framenode.md#isinrenderstate23)）
* 普通文本输入框（[API参考](../harmonyos-references/ts-universal-attributes-text-style.md#deletebackward23)）及RichEditor（[API参考](../harmonyos-references/ts-basic-components-richeditor.md#deletebackward23)）新增支持deleteBackward删除字符的能力。
* 普通文本新增支持行首标点符号压缩。（[API参考](../harmonyos-references/ts-basic-components-text.md#compressleadingpunctuation23)）
* TextController新增支持文本选择能力。（[API参考](../harmonyos-references/ts-basic-components-text.md#settextselection23)）
* Text跑马灯新增参数spacing，支持配置跑马灯间距。（[API参考](../harmonyos-references/ts-basic-components-text.md#textmarqueeoptions18对象说明)）
* PersistenceV2的globalConnect新增支持集合类型（Array、Map、Set、Date、collections.Array、collections.Map、collections.Set）的持久化。（[指南](../harmonyos-guides/arkts-new-persistencev2.md)）
* Navigation支持自定义双栏模式下分割线的颜色和间距。（[API参考](../harmonyos-references/ts-basic-components-navigation.md#divider23)）
* List组件或Grid组件下使用LazyForEach或带virtualScroll的Repeat时，新增支持不包含任何节点的空分支，空分支按大小为0的子节点处理。（[List组件ArkTS API参考](../harmonyos-references/ts-container-list.md#supportemptybranchinlazyloading23)、[Grid组件ArkTS API参考](../harmonyos-references/ts-container-grid.md#supportemptybranchinlazyloading23)、[C API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)-ArkUI\_NodeAttributeType新增属性NODE\_LIST\_SUPPORT\_EMPTY\_BRANCH\_IN\_LAZY\_LOADING、NODE\_GRID\_SUPPORT\_EMPTY\_BRANCH\_IN\_LAZY\_LOADING）
* RichEditor新增支持单行模式。（[API参考](../harmonyos-references/ts-basic-components-richeditor.md#singleline23)）

### ArkWeb

* 新增支持Web应用模拟点击检测。（[指南](../harmonyos-guides/web-detect-simulated-click-risk-enhanced.md)）
* 新增支持禁用AI识图能力。（[API参考](../harmonyos-references/arkts-basic-components-web-attributes.md#enableimageanalyzer23)）
* 新增支持获取ConsoleMessage的日志来源。（[API参考](../harmonyos-references/arkts-basic-components-web-consolemessage.md#getsource23)）
* 新增支持Web首屏渲染时间统计的能力，用于衡量首屏网页加载渲染性能。（[API参考](../harmonyos-references/arkts-basic-components-web-events.md#onfirstscreenpaint23)）
* 新增支持获取所有存储的Cookies和Cookies的属性。（[API参考](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#fetchallcookies23)）
* 新增白屏插帧接口，提供插帧信息回调和设置失效时间的能力。（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setblanklessloadingwithparams23)）

### Audio Kit

* 新增C API，支持变声效果节点变声类型设置和设置结果查询。（[API参考](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setspacerenderpositionparams)）
* 系统音量变化回调中新增“上一音量值”字段，用于获取音量变化前的音量值。（[API参考](../harmonyos-references/arkts-apis-audio-i.md#streamvolumeevent20)）
* 新增系统音效管理和播放的API，提供管理系统声音的基础能力，包括对系统音效类型的定义、获取系统音效播放器等。（[指南](../harmonyos-guides/using-soundplayer-for-playback.md)、[API参考](../harmonyos-references/js-apis-systemsoundmanager.md)）
* 新增支持获取当前音频路由的预估时延。（[API参考](../harmonyos-references/arkts-apis-audio-audiorenderer.md#getlatency23)）

### AVCodec Kit

AVCodec新增支持AV1/VP9/VP8/RV30/RV40/WVC1/DVVIDEO/RAWVIDEO/MPEG1格式的视频软解码能力。（[指南](../harmonyos-guides/avcodec-support-formats.md#媒体编解码)）

### Basic Service Kit

上传下载的预下载模块新增支持获取对端IP地址。（[API参考](../harmonyos-references/js-apis-request-cachedownload.md#networkinfo20)）

### Call Service Kit

* 新增支持查询应用是否有企业来电显示权限以及获取陌生号码与信息识别开关状态、应用号码识别开关状态。（[API参考](../harmonyos-references/callservicekit-numberldentify.md)）
* 新增支持跳转陌生号码和信息识别设置页面能力。（[指南](../harmonyos-guides/callservice-enterprise-contact-display.md#应用跳转陌生号码和信息识别页面)）

### Camera Kit

* 新增支持获取全质量图和未压缩图的对象。（[API参考](../harmonyos-references/arkts-apis-camera-photooutput.md#oncapturephotoavailable23)）
* 新增支持HDR动态照片拍摄能力，即组成动态照片的静态图片与动态短视频均为高动态范围（HDR）内容。（[指南](../harmonyos-guides/camera-moving-photo.md#hdr动态照片)）
* 新增addMetadataObjectTypes、removeMetadataObjectTypes，用于针对检测类型进行实时增删。（[API参考](../harmonyos-references/arkts-apis-camera-metadataoutput.md#addmetadataobjecttypes23)）
* 新增C API，支持使用元数据对象类型数组创建元数据输出实例。（[API参考](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createmetadataoutputwithobjecttypes)）

### Cloud Foundation Kit

* 新增支持PC/2in1设备。（[指南](../harmonyos-guides/cloudfoundation-introduction.md#支持的设备)）
* 预加载模块新增支持跳链安装预加载类型。（[指南](../harmonyos-guides/cloudfoundation-prefetch-overview.md)、[API参考](../harmonyos-references/cloudfoundation-cloudresprefetch.md#prefetchmode)）

### Connectivity Kit

BLE广播报文数据AdvertiseData新增advertiseName，支持应用自定义BLE广播名称。（[API参考](../harmonyos-references/js-apis-bluetooth-ble.md#advertisedata)）

Wi-Fi的P2P连接方式新增支持通过指定群组频率创建群组的能力。（[API参考](../harmonyos-references/js-apis-wifimanager.md#wifip2pconfig)）

### Crypto Architecture Kit

新增支持通过私钥对象获取公钥对象的能力。（[API参考](../harmonyos-references/js-apis-cryptoframework.md#getpubkey23)）

### Enterprise Space Kit

空间管理场景下，新增支持企业账号认证、获取企业应用访问令牌、设置工作空间状态栏图标、设置工作空间本地名称功能。（[指南](../harmonyos-guides/enterprisespace-spacemanager-guide.md)）

### Form Kit

ArkTS卡片开发支持V2装饰器语法。（[指南](../harmonyos-guides/arkts-ui-widget-adapt-faq.md)）

### Game Service Kit

游戏近场快传新增支持安装包传输。（[指南](../harmonyos-guides/gameservice-nearbytransfer-installation-package.md)、[API参考](../harmonyos-references/gameservice-nearbytransfer.md#gamenearbytransferonremoteinstallationinfonotify)）

### Graphics Accelerate Kit

* 游戏资源加速服务AppDownloadProgress接口新增支持设置资源类型。（[API参考](../harmonyos-references/graphics-accelerate-assetdownloadmanager.md#appdownloadprogress)）
* 游戏启动加速服务新增支持PC/2in1设备。（[指南](../harmonyos-guides/graphics-accelerate-introduction.md#支持的设备)）

### IAP Kit

* 新增开票接口，实现在用户在购买数字商品场景下，申请开发票。（[指南](../harmonyos-guides/iap-after-sales.md)、[API参考](../harmonyos-references/iap-iap.md#iapshowmanagedinvoices)）
* 新增ArkTS嵌入式收银台组件，支持TV设备上的嵌入式收银台。（[API参考](../harmonyos-references/iap-arkts-component.md)）

### Image Kit

* 新增支持读取和批量修改图像源的元数据的能力。（[API参考](../harmonyos-references/arkts-apis-image-imagesource.md#readimagemetadata23)）
* PixelMap新增自动处理旋转角的能力。（[ArkTS API参考](../harmonyos-references/arkts-apis-image-f.md#imagecreatepixelmapfromsurfacewithtransformation23)、[C API参考](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmapfromsurfacewithtransformation)）

### Live View Kit

新增支持基于地理位置的实况窗提醒。（[API参考](../harmonyos-references/liveview-liveviewmanager.md#liveviewmanagerstartliveviewbytrigger)）

### Map Kit

* 新增3D地图城市灯光效果。（[指南](../harmonyos-guides/map-presenting.md#开启3d地球)、[API参考](../harmonyos-references/map-map-mapcomponentcontroller.md#setsphereenabled-2)）
* 新增支持在地图左下角设置审图号。（[指南](../harmonyos-guides/map-controls-and-interaction.md#审图号)、[API参考](../harmonyos-references/map-map-mapcomponentcontroller.md#setapprovenumberenabled)）
* 新增支持设置Marker碰撞优先级以及Marker最大、最小层级。（[API参考](../harmonyos-references/map-common.md#markeroptions)）

### NearLink Kit

新增查询当前设备是否支持NearLink Kit的能力。（[指南](../harmonyos-guides/nearlink-issupported.md)、[API参考](../harmonyos-references/nearlink-manager.md#isnearlinksupported)）

### MDM Kit

* 新增支持根据给定的bundleInfoGetFlag获取设备指定用户下已安装应用列表。（[API参考](../harmonyos-references/js-apis-enterprise-bundlemanager.md#bundlemanagergetinstalledbundlelist23)）
* 应用管理模块新增支持设置UIAbility组件禁用策略。（[API参考](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanagersetabilitydisabled23)）
* MDM应用支持在后台访问context和启动应用的功能。（[API参考](../harmonyos-references/s-apis-application-enterpriseadminextensioncontext.md)）

### Media Kit

* 新增支持批量提取视频缩略图的能力，通过传入一个时间戳数组，可获取时间戳对应视频帧的缩略图。（[指南](../harmonyos-guides/avmetadataextractor.md)-详见步骤7、[API参考](../harmonyos-references/arkts-apis-media-avmetadataextractor.md#fetchframesbytimes23)）
* 支持将HDR VIVID/HLG/HDR10视频转换为SDR视频，以及SDR视频的转码。（[指南](../harmonyos-guides/media-kit-intro.md#支持的格式-4)）

### Media Library Kit

新增支持获取媒体库相册的虚拟路径。（[API参考](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#albumkeys)）

### Network Kit

* HTTP请求新增多个可选配置信息（[API参考](../harmonyos-references/js-apis-http.md#httprequestoptions)）：
  + 新增配置参数customMethod支持自定义请求方法；
  + 新增配置参数maxRedirects支持针对HttpRequest指定最大跳转次数；
  + 新增配置参数sniHostName支持客户端通过配置SNI（Server Name Indication，服务器名称指示）在TLS握手阶段向服务器声明目标域名；
  + 新增配置参数pathPreference支持HTTP请求指定特定激活的网络。
* 新增接口支持VPN类应用获取数据包对应的UID。（[API参考](../harmonyos-references/js-apis-net-connection.md#connectiongetconnectowneruid23)）
* DNS解析能力支持转码，可将Unicode编码形式的主机名转换为ASCII编码形式（[API参考](../harmonyos-references/js-apis-net-connection.md#connectiongetdnsascii23)），也可将ASCII编码形式的主机名转换为Unicode编码形式（[API参考](../harmonyos-references/js-apis-net-connection.md#connectiongetdnsunicode23)）。（[指南](../harmonyos-guides/net-dns.md)）

### Notification Kit

* NotificationRequest中新增多个属性（[API参考](../harmonyos-references/js-apis-inner-notification-notificationrequest.md#notificationrequest-1)）：
  + 新增属性priorityNotificationType，支持设置通知优先显示。
  + 新增属性overlayIcon，支持设置重叠图标。
* NotificationFlags新增属性，支持应用调整通知是否在横幅和锁屏界面显示。（[API参考](../harmonyos-references/js-apis-inner-notification-notificationflags.md#notificationflags-1)）

### Payment Kit

新增营销组件，开发者可在应用内实现领券、选券能力。（[指南](../harmonyos-guides/payment-promotion-service.md)、[API参考](../harmonyos-references/payment-promotionservice.md)）

### PDF Kit

* 新增支持自定义页面视图的缩放范围。（[API参考](../harmonyos-references/pdf-arkts-pdfviewmanage.md#setmaxzoom)）
* 新增支持在PDF页面获取页面文本信息。（[API参考](../harmonyos-references/pdf-arkts-pdfservice.md#gettextcontent)）

### Pen Kit

新增禁用画布缩放能力、设置滚动位置ScrollTo及监听长画布滚动位置能力、自定义长画布最大高度能力。（[指南](../harmonyos-guides/pen-suite.md)、[API参考](../harmonyos-references/pen-handwritecomponent.md#handwritecomponent)）

### Performance Analysis Kit

HiappEvent新增ArkWeb抛滑触控操作丢帧检测能力。（[指南](../harmonyos-guides/hiappevent-watcher-web-fling-jank-events.md)）

HiDebug新增提供添加维测信息的接口，开发者可根据业务需要将维测信息添加到崩溃日志中，若程序发生崩溃，可在崩溃日志中找到该维测信息。（[指南](../harmonyos-guides/hidebug-guidelines.md#添加维测信息到崩溃日志中)、[API参考](../harmonyos-references/capi-hidebug-h.md#oh_hidebug_setcrashobj)）

AppFreeze日志中调用栈的堆栈信息增加线程状态信息。（[指南](../harmonyos-guides/appfreeze-guidelines.md#堆栈信息)）

### Preview Kit

新增C API，支持通用文件缓存加速功能，即通过缓存解码后的图片、视频等数据至磁盘，实现后续文件打开或浏览时的直接读取，减少重复解码耗时，提升用户操作流畅度。（[指南](../harmonyos-guides/preview-filecacheboost.md)）

### Remote Communication Kit

* 新增Response.toJSON接口，支持BigInt模式。（[API参考](../harmonyos-references/remote-communication-rcp.md#tojson-1)）
* 在网络请求的场景下，新增支持通过OnAuthenticationChallenge接口，实现认证挑战。（[API参考](../harmonyos-references/remote-communication-rcp.md#onauthenticationchallenge)）
* 在网络请求的场景下，新增支持获取本次请求的重定向次数。（[API参考](../harmonyos-references/remote-communication-rcp.md#debugevent)）
* 在网络请求的场景下，新增支持通过ConnectionReusePolicy接口，设置HTTP管道复用策略。（[API参考](../harmonyos-references/remote-communication-rcp.md#connectionreusepolicy)）
* 新增支持应用通过network\_config.json文件，配置HTTP明文请求禁用策略。（[指南](../harmonyos-guides/remote-communication-preparations.md#http明文设置)）
* 新增默认的通信会话，支持在不需要定制Session的配置场景下，便捷地发起网络请求。（[API参考](../harmonyos-references/remote-communication-rcp.md#defaultsession)）
* 在网络请求的场景下，新增支持通过CookieRepository管理cookie。（[API参考](../harmonyos-references/remote-communication-rcp.md#cookierepository)）

### Scan Kit

默认界面扫码能力、图像识码能力和自定义界面扫码能力支持带后置相机的Wearable。（[指南](../harmonyos-guides/scan-introduction.md#支持的设备)）

### Telephony Kit

新增VCard模块，提供电子名片的文件格式标准，支持将VCard文件导入联系人数据库和将联系人数据导出为VCard文件等。（[API参考](../harmonyos-references/js-apis-vcard.md)）

### UI Design Kit

* 新增底部页签悬浮样式以及迷你栏，支持迷你栏动态折叠展开。（[指南](../harmonyos-guides/ui-design-hds-tabs-bar-floating.md)、[API参考](../harmonyos-references/ui-design-hdstabs.md#hdstabsfloatingstyle)）
* 导航组件新增支持设置双栏模式下的分割线和右侧页面显示默认占位页。（[API参考-双栏分割线](../harmonyos-references/ui-design-hdsnavigation.md#divider)、[API参考-双栏默认占位页](../harmonyos-references/ui-design-hdsnavigation.md#splitplaceholder)）
* 导航组件新增支持设置标题字号、局部页面自定义主题等能力。（[API参考-标题字号](../harmonyos-references/ui-design-hdsnavigation.md#titlesize)、[API参考-局部自定义](../harmonyos-references/ui-design-hdsnavdestination.md#withtheme)）
* 底部页签和导航组件新增支持沉浸式材质效果。（[API参考-底部页签材质参数](../harmonyos-references/ui-design-hdstabs.md#systemmaterialparams)、[API参考-导航组件材质参数](../harmonyos-references/ui-design-hdsnavigation.md#systemmaterialparams)）
* 列表卡片新增支持无障碍相关能力，包括无障碍分组、聚合播报等。（[API参考](../harmonyos-references/ui-design-hdslistitemcard.md#accessibilitygroupoptions)）
* 新增支持设置列表的预览菜单样式、横滑删除触发类型以及拦截无障碍事件等能力。（[API参考](../harmonyos-references/ui-design-hdslistitem.md#menustyle)）
* 侧边栏新增支持通过横滑手势打开/关闭侧边栏。（[API参考](../harmonyos-references/ui-design-hdssidebar.md#接口)）
* 操作栏新增支持设置操作栏上下边距。（[API参考](../harmonyos-references/ui-design-hdsactionbar.md#actionbarstyle)）
* 即时消息栏新增支持高度随组件文本内容自适应变化。（[API参考](../harmonyos-references/ui-design-hdssnackbar.md#snackbarstyleoptions)）
* 新增材质模块，支持设置材质类型和等级，实现组件的沉浸式材质效果。（[API参考](../harmonyos-references/ui-design-hdsmaterial.md)）

### Universal Keystore Kit

HUKS新增支持群组密钥功能，针对同一开发者开发的多个HAP应用提供跨应用密钥共享能力。（[指南](../harmonyos-guides/huks-group-key-overview.md)）

### Weather Service Kit

* 新增支持根据精确位置查询天气信息。（[API参考](../harmonyos-references/weather-service-weatherservice.md#weatherrequest)）
* 新增支持根据位置信息，查询对应位置地点名称。（[API参考](../harmonyos-references/weather-service-weatherservice.md#city)）
* 新增支持TV设备。（[指南](../harmonyos-guides/weather-service-introduction.md#约束与限制)）

### 调测调优

打包工具打包hap/hsp时，支持传入已存在的hap/hsp（--exist-src-path）和指定要保留的目录（--lib-path-retain），要保留的目录会从已存在的hap/hsp中直接拷贝到目标包，不会从源文件中重新压缩打包。当前保留目录只支持--lib-path。（[指南](../harmonyos-guides/packing-tool.md)）
