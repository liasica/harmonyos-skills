---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-510
title: OS新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > OS新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2635f907868846dfba89f987eadc8615f6e3dc29ae126df1e420c0195071040c
---

## 关键特性

HarmonyOS 5.1.0 Release版本重点提供如下的开放能力。全量新增接口可查看[API变更清单](apidiff-510.md)。

### Ability Kit

* 新增支持根据指定的数据加密级别创建应用上下文，以获取相应的路径。（[API参考](../harmonyos-references/js-apis-inner-application-context.md#createareamodecontext18)）
* 新增支持同步获取当前进程的进程名（processName）。（[API参考](../harmonyos-references/js-apis-inner-application-context.md#属性)）
* 新增支持获取应用被拉起原因（LAUNCH\_REASON\_MESSAGE）。（[API参考](../harmonyos-references/js-apis-app-ability-wantconstant.md#params)）
* 启动框架新增支持HAR/HSP和so文件。（[指南](../harmonyos-guides/app-startup.md#支持的范围)、[API参考](../harmonyos-references/js-apis-app-appstartup-startupmanager.md)）
* 新增支持获取应用上次异常退出的详细原因。（[指南](../harmonyos-guides/ability-exit-info-record.md)、[API参考](../harmonyos-references/js-apis-app-ability-abilityconstant.md#lastexitdetailinfo18)）
* 新增支持设置UIAbility的颜色模式。（[API参考](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#setcolormode18)）

### Account Kit

* 华为账号授权支持Wearable设备获取用户头像昵称、手机号和风险等级等信息。（[指南](../harmonyos-guides/account-introduction.md#约束与限制)）
* 登录场景支持获取用户风险等级。（[指南](../harmonyos-guides/account-get-risklevel.md)）

### AppGallery Kit

应用市场更新功能、图标管理服务支持Wearable设备。（[指南](../harmonyos-guides/store-introduction.md#支持的设备)）

### AR Engine

* 新增ArkTS API，支持运动跟踪能力、环境跟踪能力和命中检测能力，包括管理AR会话、获取设备位姿、检测环境中的平面、识别平面语义、获取深度估计信息、获取网格扫描信息、图像跟踪、AR物体摆放。（[指南](../harmonyos-guides/arengine-guide.md)）
* 新增C API，支持如下特性：
  + 图像跟踪，实现传入图像数据对现实环境中的物体进行识别跟踪。（[指南](../harmonyos-guides/arengine-c-image-track.md)）
  + 获取网格扫描信息，实现检测当前环境中的物体，并对物体表面进行网格化。（[指南](../harmonyos-guides/arengine-c-get-mesh.md)）

### ArkData

* RelationalStore新增rootDir配置，支持打开非database目录下的数据库（[API参考](../harmonyos-references/arkts-apis-data-relationalstore-i.md#storeconfig)）
* ArkData RDB向量数据管理新增支持对向量数据的快速检索和相似性搜索。（[指南-ArkTS](../harmonyos-guides/data-persistence-by-vector-store.md)、[指南-C/C++](../harmonyos-guides/native-vector-store-guidelines.md)）
* 关系型数据库新增支持根据指定的列索引或列名称获取列数据类型。（[API参考](../harmonyos-references/arkts-apis-data-relationalstore-resultset.md#getcolumntype18)）

### ArkTS

* TaskPool支持指定任务执行并发度和指定任务的排队策略。（[API参考](../harmonyos-references/js-apis-taskpool.md#asyncrunner18)）
* TaskPool支持通过任务ID取消任务池中的任务。（[API参考](../harmonyos-references/js-apis-taskpool.md#taskpoolcancel18)）
* collections（ArkTS容器集）在API 18新增支持以下方法（[API参考](../harmonyos-references/js-apis-arkts-collections.md)）：

  Array：from、isArray、of、copyWithin、lastIndexOf、some、reduceRight、reverse、toString、every、toLocaleString

  TypedArray：toString、toLocaleString、lastIndexOf、reduceRight
* Sendable支持在缓存空间不够的时候，将近期最少使用的数据替换为新数据。（[API参考](../harmonyos-references/arkts-apis-arkts-utils-sendablelrucache.md)）
* Worker支持创建任务时指定任务的优先级。（[API参考](../harmonyos-references/js-apis-worker.md#threadworkerpriority18)）

### ArkUI

* 文本与输入组件能力增强。包括：
  + 文本组件支持通过NODE\_IMMUTABLE\_FONT\_WEIGHT属性，设置文字粗细不会跟随系统字体粗细而变化。（[API参考-C API](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）
  + 文本组件支持对选中的文本提供分享服务 （[API参考](../harmonyos-references/ts-text-common.md#属性)）、支持按音节连字符换行（[API参考](../harmonyos-references/ts-appendix-enums.md#wordbreak11)）。
  + 富文本（RichEditor）组件支持设置最大行数。（[API参考](../harmonyos-references/ts-basic-components-richeditor.md#maxlength18)）
  + TextInput组件支持设置文本省略位置。（[API参考](../harmonyos-references/ts-basic-components-textinput.md#ellipsismode18)）
  + TextInput/TextArea/Search/RichEditor组件支持将文本行间距平分至行的顶部与底部。（[API参考-TextInput](../harmonyos-references/ts-basic-components-textinput.md#halfleading18)、[API参考-TextArea](../harmonyos-references/ts-basic-components-textarea.md#halfleading18)、[API参考-Search](../harmonyos-references/ts-basic-components-search.md#halfleading18)、[API参考-RichEditor](../harmonyos-references/ts-basic-components-richeditor.md#richeditortextstyleresult)）
  + TextInput/TextArea组件扩展自动填充类型，包含：车牌号、护照号等。（[API参考-ArkTS](../harmonyos-references/ts-basic-components-textinput.md#contenttype12枚举说明)、[API参考-C API](../harmonyos-references/capi-native-type-h.md#arkui_textinputcontenttype)）
  + 富文本（RichEditor）组件在长按预览菜单时支持振动效果。（[API参考](../harmonyos-references/ts-basic-components-richeditor.md#previewmenuoptions18)）
* 新增适配圆形屏幕的能力。包括：
  + 新增旋转表冠事件，组件获焦后扭动表冠可获取时间戳、旋转角速度、旋转角度和表冠动作信息。（[API参考](../harmonyos-references/ts-universal-events-crown.md)、[指南](../harmonyos-guides/arkts-common-events-crown-event.md)）
  + 新增弧形列表组件ArcList和ArcListItem，可呈现连续、多行的同类数据。（[API参考-ArcList](../harmonyos-references/ts-container-arclist.md)、[API参考-ArcListItem](../harmonyos-references/ts-container-arclistitem.md)、[指南](../harmonyos-guides/arkts-layout-development-create-arclist.md)）
  + 新增弧形索引条组件ArcAlphabetIndexer，可按字母顺排序进行快速定位。（[API参考](../harmonyos-references/ts-container-arc-alphabet-indexer.md)、[指南](../harmonyos-guides/arkts-layout-development-create-arclist.md#与弧形索引条arcalphabetindexer联动)）
  + 新增弧形滚动条组件ArcScrollBar，可为弧形列表添加外置滚动条。（[API参考](../harmonyos-references/ts-basic-components-arcscrollbar.md)、[指南](../harmonyos-guides/arkts-layout-development-create-arclist.md#添加外置滚动条arcscrollbar)）
  + 新增弧形按钮组件ArcButton，可提供强调、普通、警告等样式按钮。（[API参考](../harmonyos-references/ohos-arkui-advanced-arcbutton.md)、[指南](../harmonyos-guides/arkts-advanced-components-arcbutton.md)）
* 通用拖拽能力增强。包括：
  + 支持设置自定义落位动效。（[API参考](../harmonyos-references/ts-universal-events-drag-drop.md#executedropanimation18)）
  + 支持自定义控制在拖拽至可滚动组件边缘时，是否触发自动滚屏（[API参考](../harmonyos-references/ts-universal-attributes-drag-drop.md#draginteractionoptions12)）
* 弹窗能力增强。包括：
  + 支持通过设置levelOrder来管理弹出框的显示顺序，确保层级较高的弹出框覆盖在层级较低的弹出框之上。（[API参考](../harmonyos-references/js-apis-promptaction.md#showdialogoptions)、[指南](../harmonyos-guides/arkts-dialog-levelorder.md)）
  + 支持在自定义内容中，创建和关闭对应的自定义弹窗。（[API参考](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18)）
  + Popup组件支持通过maxWidth设置最大宽度。（[API参考](../harmonyos-references/ohos-arkui-advanced-popup.md#popupoptions)）
  + 半模态Popup样式弹窗，支持通过placement设置相对于目标的显示位置，通过placementOnTarget设置弹窗能否覆盖在目标节点上。（[API参考](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)）
  + Menu和Dialog支持通过backgroundBlurStyleOptions和backgroundEffect设置自定义背景模糊。（[API参考-Menu](../harmonyos-references/ts-universal-attributes-menu.md#contextmenuoptions10)、[API参考-Dialog](../harmonyos-references/js-apis-promptaction.md#showdialogoptions)）
  + 模态转场和MenuItem支持!!双向绑定变量。（[API参考-半模态转场](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)、[API参考-全屏模态转场](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover)、[API参考-MenuItem](../harmonyos-references/ts-basic-components-menuitem.md#selected)）
  + 自定义弹窗支持避让键盘后，通过keyboardAvoidDistance设置弹窗和键盘之间的最小距离。（[API参考](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)、[API参考-C API](../harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2.md)）
  + 支持通过effectEdge设置半模态面板边缘滚动的效果。（[API参考](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)）
* 表单选择类组件能力增强。包括：
  + 新增SegmentButtonV2组件，可创建页签型、单选或多选的胶囊型分段按钮。（[API参考](../harmonyos-references/ohos-arkui-advanced-segmentbuttonv2.md)）
  + TextPicker/TimePicker支持选项进入选中区域时触发事件回调。（[API参考-TextPicker](../harmonyos-references/ts-basic-components-textpicker.md#onenterselectedarea18)、[API参考-TimePicker](../harmonyos-references/ts-basic-components-timepicker.md#onenterselectedarea18)）
  + TimePicker/CalendarPicker支持通过start和end配置开始时间和结束时间（[API参考-TimePicker](../harmonyos-references/ts-basic-components-timepicker.md#timepickeroptions对象说明)、[API参考-CalendarPicker](../harmonyos-references/ts-basic-components-calendarpicker.md#calendaroptions对象说明)）。
  + TimePicker支持通过enableCascade设置12小时制时上午下午跟随时间联动。（[API参考](../harmonyos-references/ts-basic-components-timepicker.md#enablecascade18)）
* 滚动与滑动组件能力增强。包括：
  + Swiper/Tabs组件增加页面选中元素改变时触发的回调，返回当前选中或将要隐藏的元素的索引值。（[API参考-Swiper](../harmonyos-references/ts-container-swiper.md#onselected18)、[API参考-Tabs](../harmonyos-references/ts-container-tabs.md#onselected18)）
  + Swiper组件增加控制手指或者鼠标等按下屏幕时，子组件是否停止自动播放的能力。（[API参考-Swiper](../harmonyos-references/ts-container-swiper.md#autoplay18)）
  + Swiper组件CAPI能力增强，可设置缓存节点是否显示、数字导航点和导航箭头的样式。（[API参考-C API](../harmonyos-references/capi-arkui-nativemodule-arkui-swiperdigitindicator.md)）
  + List组件支持设置布局样式和滚动效果（NODE\_LIST\_SCROLL\_TO\_INDEX\_IN\_GROUP、 NODE\_LIST\_LANES、NODE\_LIST\_SCROLL\_SNAP\_ALIGN、NODE\_LIST\_MAINTAIN\_VISIBLE\_CONTENT\_POSITION）（[API参考-C API](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）。
* 新增C API，支持可配置用户自定义数据的手势中断事件回调函数。（[API参考](../harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-2.md)）
* 支持设置组件的自定义焦点走焦逻辑。（[API参考](../harmonyos-references/ts-universal-attributes-focus.md#nextfocus18)、[API参考-C API](../harmonyos-references/capi-native-type-h.md#arkui_focusmove)）
* 支持动态获取手势配置参数，可返回连续点击次数阈值。（[API参考](../harmonyos-references/ts-gesture-common.md#taprecognizer18)）
* 支持手势取消时，触发的onActionCancel回调中返回手势事件信息。（[API参考-LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md#事件)、[API参考-PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md#事件)、[API参考-PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md#事件)、[API参考-RotationGesture](../harmonyos-references/ts-basic-gestures-rotationgesture.md#事件)）
* 无障碍支持自定义焦点顺序（[API参考](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitynextfocusid18)）、支持控制组件的屏幕朗读方式（[API参考](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityrole18)）、支持设置屏幕朗读滚动操作（[API参考](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilityscrolltriggerable18)）。
* 支持设置EmbeddedComponent或UIExtensionComponent组件的占用事件，指定手势事件的响应方式。（[API参考](../harmonyos-references/js-apis-arkui-uiextension.md#occupyevents18)）
* 支持将当前FrameNode移动到目标FrameNode的指定位置，实现跨实例节点迁移。（[API参考](../harmonyos-references/js-apis-arkui-framenode.md#moveto18)、[API参考-C API](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_moveto)）
* NodeController新增节点上下树和绑定解绑前后的生命周期回调接口（onAttach、onDetach、onWillBind、onWillUnbind、onBind、onUnbind）。（[API参考](../harmonyos-references/js-apis-arkui-nodecontroller.md#onattach18)）
* 支持对ComponentContent构建的UI组件进行截图。（[API参考](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#createfromcomponent18)）
* 菜单（Menu）在弹出时支持振动效果。（[API参考](../harmonyos-references/ts-universal-attributes-menu.md#hapticfeedbackmode18)）
* 窗口管理新增软键盘弹出动画完成的监听回调。（[API参考](../harmonyos-references/arkts-apis-window-window.md#onkeyboarddidshow18)）
* 窗口管理新增支持设置当前子窗口（未设置模态属性）的层级级别。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setsubwindowzlevel18)）

### ArkWeb

* 支持获取上一次被点击区域的元素信息。（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getlasthittest18)）
* 支持设置Web组件是否开启字重跟随系统设置变化。（[API参考](../harmonyos-references/arkts-basic-components-web-attributes.md#enablefollowsystemfontweight18)）
* 支持Web内音视频可对接到播控中心。（[API参考](../harmonyos-references/arkts-basic-components-web-attributes.md#enablewebavsession18)）
* 对接W3C规范，支持通过accept指定上传的文件类型。（[API参考](../harmonyos-references/arkts-basic-components-web-events.md#onshowfileselector9)）
* 提供静态方法，清除应用中的资源缓存文件。（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#removeallcache18)）

### Asset Store Kit

新增基于群组的关键资产访问控制。通过设置群组属性，同一开发者开发的多个应用可以共享数据。（[指南](../harmonyos-guides/asset-js-group-access-control.md)）

### Audio Kit

* 音频新增支持Float32格式音频输出。（[API参考](../harmonyos-references/capi-native-audiostream-base-h.md#oh_audiostream_sampleformat)）
* 新增支持空间音频管理的能力。（[指南](../harmonyos-guides/public-audio-spatialization-management.md)、[API参考](../harmonyos-references/arkts-apis-audio-audiomanager.md#getspatializationmanager18)）

### AVCodec Kit

视频解码新增支持MPEG2、MPEG4。（[指南](../harmonyos-guides/avcodec-support-formats.md)）

### AVSession Kit

新增支持通过AV会话命令传递设置目标循环模式（setTargetLoopMode）的能力（[API参考](../harmonyos-references/arkts-apis-avsession-t.md#avcontrolcommandtype10)），并提供对设置动作的事件监听回调（[API参考](../harmonyos-references/arkts-apis-avsession-avsession.md#onsettargetloopmode18)）。

### Basic Service Kit

* 上传下载支持应用缓存下载能力，支持应用提前缓存文件到沙箱目录或内存中。（[API参考](../harmonyos-references/js-apis-request-cachedownload.md)）
* 上传下载agent接口支持设置任务最高限速（[API参考](../harmonyos-references/js-apis-request.md#setmaxspeed18)），支持设置待上传文件在表单中的content-type字段（[API参考](../harmonyos-references/js-apis-request.md#requestagentfilespec10)）。
* 剪贴板支持获取剪贴板的内容变化的次数。（[API参考-ArkTS API](../harmonyos-references/js-apis-pasteboard.md#getchangecount18)、[API参考-C API](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_getchangecount)）

### CANN Kit（原HiAI Foundation Kit）

* Kit名称从HiAI Foundation Kit修改为CANN Kit，相关Kit API引用方式同步变更。（[指南](../harmonyos-guides/cannkit-introduction.md)、[API参考](../harmonyos-references/cannkit.md)）
* 新增支持设置模型加载时的维测选项，用于采集Profiling性能数据。（[API参考](../harmonyos-references/cannkit.md#hms_hiaioptions_setomoptions)）

### Car Kit

导航信息服务支持向地图类应用发起兴趣点（POI）搜索。（[API参考](../harmonyos-references/car-navigationinfomgr.md#commandtype)）

### Cloud Foundation Kit

云函数、云数据库、云存储服务支持Wearable设备。（[指南](../harmonyos-guides/cloudfoundation-introduction.md#支持的设备)）

### Device Security Kit

新增ArkTS API，支持安全图像压缩、裁剪特性能力。（[指南](../harmonyos-guides/devicesecurity-taas-secimage-process.md)）

### Distributed Service Kit

新增应用跨设备协同进行数据传输的能力。（[指南](../harmonyos-guides/abilityconnectmanager-guidelines.md)、[API参考](../harmonyos-references/js-apis-distributed-abilityconnectionmanager.md)）

### Form Kit

新增渲染模式的配置项renderingMode。（[指南](../harmonyos-guides/arkts-ui-widget-configuration.md)）

### Game Service Kit

* 新增游戏近场快传能力，支持设备在彼此靠近的情况下进行游戏数据交换。（[指南](../harmonyos-guides/gameservice-nearbytransfer-dev.md)、[API参考](../harmonyos-references/gameservice-nearbytransfer.md)）
* 新增addGameCustomData接口，支持上报自定义数据。（[API参考](../harmonyos-references/gameservice-gameperformance.md#gameperformanceaddgamecustomdata)）

### Graphics Accelerate Kit

* 新增ArkTS API，支持资源包预下载能力。（[指南](../harmonyos-guides/graphics-accelerate-assetdownload-introduction.md)、[API参考](../harmonyos-references/graphics-accelerate-arkts.md)）
* 新增支持系统送显模式，当游戏应用触发插帧任务后，系统会完成送显。（[指南](../harmonyos-guides/graphics-accelerate-fg-systempresent.md)、[API参考](../harmonyos-references/_graphics_accelerate.md#fg_presentmode-1)）

### Health Service Kit

* 新增情绪、心率变异性采样数据类型。（[指南](../harmonyos-guides/health-emotion.md)、[API参考](../harmonyos-references/health-api-samplepointhelper.md#fields-4)）
* 新增手动数据同步能力。（[指南](../harmonyos-guides/health-cloudsync.md)、[API参考](../harmonyos-references/health-api-healthstore.md#healthstoresyncall)）

### IAP Kit

消耗型、非消耗型商品购买支持Wearable设备。（[指南](../harmonyos-guides/iap-introduction.md#支持的设备)）

### Image Kit

新增C API支持获取图片的可编辑标志。（[API参考](../harmonyos-references/capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_geteditable)）

### Localization Kit

* 新增支持获取用户偏好温度单位和周起始日的能力，新增支持获取语言的最简表示的能力。（[API参考](../harmonyos-references/js-apis-i18n.md#gettemperaturetype18)）
* 新增支持时间日期/数字精细化格式化的能力，便于更灵活的使用格式化能力。（[API参考](../harmonyos-references/js-apis-i18n.md#i18ngetsimpledatetimeformatbypatterndeprecated)）
* 新增支持返回富文本的数字格式化能力。（[API参考](../harmonyos-references/js-apis-i18n.md#stylednumberformat18)）
* 新增支持路径本地化显示的能力，可以根据输入语言判断路径是否需要镜像显示。（[API参考](../harmonyos-references/js-apis-i18n.md#getunicodewrappedfilepathdeprecated)）

### MDM Kit

* 可禁用/启用的特性限制新增MTP（mtpClient/mtpServer）和恢复出厂设置（resetFactory）。（[API参考](../harmonyos-references/js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)）
* 新增支持按系统账户安装用户证书。（[API参考](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagerinstallusercertificate18)）
* 新增支持订阅账号的新增、删除、切换系统事件。（[API参考](../harmonyos-references/js-apis-enterprise-adminmanager.md#managedevent)）

### Media Kit

* 播放器支持向应用透传SEI字段数据，适用于HTTP-FLV直播。（[API参考](../harmonyos-references/arkts-apis-media-avplayer.md#onseimessagereceived18)）
* 调用媒体播放器AVPlayer设置播放策略时，新增支持起播缓冲水线（preferredBufferDurationForPlaying）的播放策略。（[API参考](../harmonyos-references/arkts-apis-media-avplayer.md#setplaybackstrategy12)）
* 能力增强：支持应用创建多个SoundPool实例。（[API参考](../harmonyos-references/arkts-apis-media-f.md#mediacreatesoundpool10)）
* 新增屏幕录制时视频填充模式的枚举。（[API参考](../harmonyos-references/arkts-apis-media-e.md#avscreencapturefillmode18)）
* 音视频录制配置文件新增支持配置稳定录制模式enableStableQualityMode。（[API参考](../harmonyos-references/arkts-apis-media-i.md#avrecorderconfig9)）
* 播放器新增支持向媒体源申请媒体数据。（[API参考](../harmonyos-references/arkts-apis-media-mediasource.md#setmediaresourceloaderdelegate18)）
* 播放器新增支持动态开启视频超分算法。（[API参考](../harmonyos-references/arkts-apis-media-avplayer.md#setsuperresolution18)）
* 调用媒体播放器AVPlayer设置播放策略时，新增支持智能追帧水线（thresholdForAutoQuickPlay）。（[API参考](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)）

### Media Library Kit

* 相册管理单选模式增强，新增支持多种相册内图片在单选时的呈现模式类型。（[API参考](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#singleselectionmode18)）

### NearLink Kit

* 支持使用星闪传输数据。（[指南](../harmonyos-guides/nearlink-start-data-transfer.md)、[API参考](../harmonyos-references/nearlink-data-transfer-api.md)）
* 新增逻辑链路连接状态获取能力。（[API参考](../harmonyos-references/nearlink-remote-device.md#getacbstate)）
* 新增数传链路连接状态获取能力。（[API参考](../harmonyos-references/nearlink-data-transfer-api.md#getconnectionstate)）

### Network Boost Kit

新增C API，提供网络加速能力以及网络感知、网络质量预测等能力。（[指南](../harmonyos-guides/network-boost-kit-guide.md)、[API参考](../harmonyos-references/networkboost-c.md)）

### PDF Kit

* 新增支持获取透明背景的PDF页面pixelMap类型的图片。（[API参考](../harmonyos-references/pdf-arkts-pdfservice.md#getareapixelmapwithoptions)）
* 新增PdfAction及相关类，支持获取页面内链接和网址链接跳转信息。（[API参考](../harmonyos-references/pdf-arkts-pdfservice.md#pdfannotationinfo)）

### Pen Kit

* 支持设置工具栏默认笔刷、笔刷类型及笔宽、各笔刷默认宽度。（API参考：[默认笔刷](../harmonyos-references/pen-handwritecomponent.md#handwritecomponent)、[笔刷类型及笔宽](../harmonyos-references/pen-handwritecomponent.md#penhspinfo)、[各笔刷默认宽度](../harmonyos-references/pen-handwritecomponent.md#handwritecomponent)）
* 新增支持全局取色实时显示RGB色值。（[API参考](../harmonyos-references/pen-imagefeaturepicker.md#pickforresult-1)）

### Performance Analysis Kit

新增支持为当前线程转储虚拟机的原始堆快照。（[API参考](../harmonyos-references/js-apis-hidebug.md#hidebugdumpjsrawheapdata18)）

### Remote Communication Kit

MultipartForm新增boundary分隔符字段，支持开发者在上传多表单时通过自定义方式实现对表单数据的准确分隔与传输。([API参考](../harmonyos-references/remote-communication-rcp.md#multipartform))

### Scan Kit

新增setAutoZoomEnabled接口，支持设置自动变焦。（[API参考](../harmonyos-references/scan-customscan-api.md#customscansetautozoomenabled)）

### Scenario Fusion Kit

* 新增场景化Input组件，开发者可调用对应FunctionalInput组件快速拉起选择地区界面，供用户选择地区信息。([指南](../harmonyos-guides/scenario-fusion-input-zone-selectors.md)、[API参考](../harmonyos-references/scenario-fusion-functionalinput.md))
* 支持智能填充的推荐车牌号场景。（[指南](../harmonyos-guides/scenario-fusion-licenseplateno.md)）
* 场景化API新增支持Wearable设备。（[指南](../harmonyos-guides/scenario-fusion-api-information-attribute.md)）
* 支持智能填充的发票抬头推荐场景。（[指南](../harmonyos-guides/scenario-fusion-introduction-to-smart-fill.md#发票抬头推荐场景)）

### Share Kit

新增支持获取用户分享结果，可实现对用户内容分享渠道的统计。（[指南](../harmonyos-guides/share-share-completed.md)）

### Test Kit

* 新增支持按照模糊匹配/正则匹配方式查找符合条件的控件id、type的能力。（API参考：[id](../harmonyos-references/js-apis-uitest.md#id18)、[type](../harmonyos-references/js-apis-uitest.md#type18)）
* 新增支持获取控件提示文本（[API参考](../harmonyos-references/js-apis-uitest.md#gethint18)），并根据控件提示文本查找控件（[API参考](../harmonyos-references/js-apis-uitest.md#hint18)）。
* 新增支持横向滑动查找控件，仅适用于支持滑动的控件。（[API参考](../harmonyos-references/js-apis-uitest.md#scrollsearch18)）
* 新增支持模拟触摸板多指滑动手势操作，仅支持2in1设备。（[API参考](../harmonyos-references/js-apis-uitest.md#touchpadmultifingerswipe18)）
* 新增支持模拟手写笔的点击、长按、双击、滑动操作。（[API参考](../harmonyos-references/js-apis-uitest.md#penclick18)）

### UI Design Kit

新增Hds导航组件HdsNavigation以及HdsNavDestination，继承ArkUI [Navigation](../harmonyos-guides/arkts-navigation-navigation.md)的页面跳转能力及基础样式，同时扩展支持：

* 标题栏随内容区滚动的动态模糊样式。（[指南](../harmonyos-guides/ui-design-navigation-dynamic-blur.md)）
* 菜单栏新增信息提醒能力。（[指南](../harmonyos-guides/ui-design-navigation-message-reminder.md)）

### Vision Kit

新增支持在PC设备上对光标移入移出文本事件的监听。（[API参考](../harmonyos-references/vision-image-analyzer.md#ontype-cursormoveintext)）

### Wear Engine Kit

新增支持Wearable设备。（[指南](../harmonyos-guides/we-business_introduction.md#支持的设备)）
