---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-502
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.2(14) > OS平台能力 > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:44+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:be44e8afec783f189748a063a8caa4922c0cc3fde1f1e67358e169944e66baaa
---

## Ability Kit

* HSP支持在配置文件中声明除入口Ability以外的UIAbility组件。（[指南](../harmonyos-guides/in-app-hsp.md#约束限制)）
* 针对PC/2in1与平板设备，新增支持自定义应用启动时的启动页。（[API参考](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)）
* 通过Want传递对象间信息时支持在parameters参数中携带应用分身的索引（ohos.param.callerAppCloneIndex）。（[API参考](../harmonyos-references/js-apis-app-ability-want.md#want)）
* 新增支持获取应用上下文的能力。（[API参考](../harmonyos-references/js-apis-app-ability-application.md#applicationgetapplicationcontext14)）
* 开放包管理能力供三方应用调用。（[API参考](../harmonyos-references/js-apis-bundlemanager.md)）
* 新增支持UIAbility备份恢复的能力。（[API参考](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#setrestoreenabled14)，[指南](../harmonyos-guides/ability-recover-guideline.md)）
* 新增支持获取当前应用多实例的唯一实例标识。（[API参考](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextgetcurrentinstancekey14)）
* 环境变量信息的定义中新增当前应用字体的唯一ID的定义fontId。（[API参考](../harmonyos-references/js-apis-app-ability-configuration.md#configuration)）
* 新增C API，支持获取当前应用适用的设备类型。适用于在将手机应用分发到平板/PC/2in1设备时，合理适配布局和字体大小。（[API参考](../harmonyos-references/capi-native-interface-bundle-h.md#oh_nativebundle_getcompatibledevicetype)）

## ArkData

* 新增flushSync()接口支持将缓存的Preferences实例中的数据存储到共享用户首选项的持久化文件中。（[API参考](../harmonyos-references/js-apis-data-sendablepreferences.md#flushsync14)）
* 关系型数据库（RDB）的配置属性StoreConfig新增参数cryptoParam，用于自定义加密参数。（[API参考](../harmonyos-references/arkts-apis-data-relationalstore-i.md#cryptoparam14)）
* 关系型数据库（RDB）新增支持创建可并发的事务对象。（[API参考](../harmonyos-references/arkts-apis-data-relationalstore-rdbstore.md#createtransaction14)）
* 标准化数据结构（UDMF）新增内容卡片类型的数据结构（ContentForm）。（[API参考](../harmonyos-references/js-apis-data-uniformdatastruct.md#contentform14)）
* 标准化数据结构（UDMF）新增支持设置应用内拖拽通道数据可使用的范围。（[API参考](../harmonyos-references/js-apis-data-unifieddatachannel.md#unifieddatachannelsetappshareoptions14)）

## ArkGraphics 2D

* 新增C API，支持获取系统全局字体集。（[API参考](../harmonyos-references/capi-drawing-font-collection-h.md#oh_drawing_getfontcollectionglobalinstance)）
* 新增Decoupled VSync（DVSync）的C API能力以提高自绘制动画场景的流畅性。（[API参考](../harmonyos-references/capi-native-vsync-h.md#oh_nativevsync_dvsyncswitch)）
* 新增一个模糊效果的处理能力，增加着色器效果平铺模式，影响图像边缘的模糊效果。（[API参考](../harmonyos-references/js-apis-effectkit.md#blur14)）
* 新增C API，使浏览器支持动态帧率。（[API参考](../harmonyos-references/capi-native-vsync-h.md#oh_nativevsync_create_forassociatedwindow)）

## ArkUI

* 文本输入时的键盘避让模式支持光标避让。（[指南](../harmonyos-guides/arkts-common-components-text-input.md#光标避让)）
* 新增支持将属性字符串转换成HTML格式字符串的能力。（[API参考](../harmonyos-references/ts-universal-styled-string.md#tohtml14)）
* 新增支持设置子窗的模态类型。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setsubwindowmodal14)）
* 新增支持对容器设置组件级的安全区域。（[API参考](../harmonyos-references/ts-universal-attributes-size.md#safeareapadding14)）
* 新增支持获取文本组件中指定字符的绘制区域信息。（[API参考](../harmonyos-references/ts-text-common.md#getrectsforrange14)）
* Navigation（NavDestination）的title和menus属性新增支持Resource资源类型。（[API参考-title属性](../harmonyos-references/ts-basic-components-navdestination.md#title)、[API参考-menus属性](../harmonyos-references/ts-basic-components-navigation.md#navigationmenuitem)）
* Navigation自定义转场动画能力增强，支持分别设置系统标题栏动画和内容动画。（[API参考](../harmonyos-references/ts-basic-components-navdestination.md#systemtransition14)）
* TextArea、Search组件新增新的onSubmit事件用于在事件提交时保持组件的编辑状态。（[API参考-TextArea组件](../harmonyos-references/ts-basic-components-textarea.md#onsubmit14)、[API参考-Search组件](../harmonyos-references/ts-basic-components-search.md#onsubmit14)）
* 按键事件新增unicode对象，支持返回当前keyEvent对应按键的unicode码值。（[API参考](../harmonyos-references/ts-universal-events-key.md#keyevent对象说明)）
* 半模态转场的SheetOptions新增enableHoverMode和hoverModeArea属性用于支持悬停。（[API参考](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetoptions)）
* 文本选择器组件（TextPicker）新增支持滑动停止时的事件回调。（[API参考](../harmonyos-references/ts-basic-components-textpicker.md#onscrollstop14)）
* 新增C API，支持为OH\_NativeXComponent实例注册带有返回值的按键事件回调。（[API参考](../harmonyos-references/capi-native-interface-xcomponent-h.md#oh_nativexcomponent_registerkeyeventcallbackwithresult)）
* ArkUI的NodeAttributeType新增获取滚动类组件及所有子组件全展开尺寸的C API属性定义。（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）
* List组件新增支持设置列表中ListItem/ListItemGroup的预加载数量，并支持配置是否显示预加载节点。（[API参考](../harmonyos-references/ts-container-list.md#cachedcount14)）
* 滚动组件新增支持设置滚动容器的内容层裁剪区域。（[API参考](../harmonyos-references/ts-container-scrollable-common.md#clipcontent14)）
* 滚动组件新增支持设置边缘渐隐效果及设置边缘渐隐长度。（[API参考](../harmonyos-references/ts-container-scrollable-common.md#fadingedge14)）
* Grid、WaterFlow组件新增支持设置预加载的GridItem、FlowItem数量，并配置是否显示预加载节点。（[API参考-Grid](../harmonyos-references/ts-container-grid.md#cachedcount14)、[API参考-WaterFlow](../harmonyos-references/ts-container-waterflow.md#cachedcount14)）
* ImageSpan组件新增支持为图像设置颜色滤镜效果。（[API参考](../harmonyos-references/ts-basic-components-imagespan.md#colorfilter14)）
* SegmentButton组件新增支持适老化大字体。（[API参考](../harmonyos-references/ohos-arkui-advanced-segmentbutton.md#segmentbutton-1)）
* 属性字符串新增支持设置文字背景色。（[API参考](../harmonyos-references/ts-universal-styled-string.md#backgroundcolorstyle14)）
* 属性字符串新增支持设置为超链接。（[API参考](../harmonyos-references/ts-universal-styled-string.md#urlstyle14)）
* Chip和ChipGroup组件新增支持多种类型的无障碍朗读能力。（[API参考-Chip](../harmonyos-references/ohos-arkui-advanced-chip.md)、[API参考-ChipGroup](../harmonyos-references/ohos-arkui-advanced-chipgroup.md)）
* 日期滑动选择器弹窗（DatePickerDialog）新增支持设置切换农历开关的样式。（[API参考](../harmonyos-references/ts-methods-datepicker-dialog.md#lunarswitchstyle14对象说明)）
* Tabs组件新增支持对底部页签适配组件级布局安全区。（[API参考](../harmonyos-references/ts-container-tabs.md#barheight)）
* Text组件新增支持设置选中文本的手柄颜色和底板颜色。（[API参考](../harmonyos-references/ts-basic-components-text.md#caretcolor14)）
* 新增支持设置跑马灯（Marquee）的动态帧率。（[API参考](../harmonyos-references/arkts-apis-uicontext-marqueedynamicsyncscene.md)）
* 手势处理的能力涉及到的六类手势事件新增支持设置允许的事件输入源。（[API参考](../harmonyos-references/ts-gesture-common.md#allowedtypes14)）
* 组件的位置设置，新增支持对形成链的组件进行重新布局（仅当父容器为RelativeContainer时生效）。（[API参考](../harmonyos-references/ts-universal-attributes-location.md#chainweight14)）
* 组件的背景设置，新增支持设置窗口失焦后，窗口内控件模糊效果会被移除。（[API参考](../harmonyos-references/ts-universal-attributes-background.md#backgroundeffectoptions11)）
* 路由跳转新增支持设置页面是否可恢复。（[API参考](../harmonyos-references/js-apis-router.md#routeroptions)）
* 新增C API，支持获取节点的节点类型（[API参考](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getnodetype)）和窗口信息（[API参考](../harmonyos-references/capi-native-node-h.md#oh_arkui_nodeutils_getwindowinfo)）。
* FrameNode新增支持手势事件。（[API参考](../harmonyos-references/js-apis-arkui-framenode.md#gestureevent14)）
* Image组件新增支持设置图片的显示方向。（[API参考](../harmonyos-references/ts-basic-components-image.md#orientation14)）
* RichEditor新增支持鼠标悬停事件回调（OnHoverCallback）。（[API参考](../harmonyos-references/ts-basic-components-richeditor.md#onhovercallback14)）
* Navigation页面栈新增支持配置可在异常退出时恢复。（[API参考](../harmonyos-references/ts-basic-components-navigation.md#recoverable14)）
* 新增支持绑定NavDestination组件和可滚动容器组件，当滑动可滚动容器组件时，会触发所有与其绑定的NavDestination组件的标题栏和工具栏的显示和隐藏动效。（[API参考](../harmonyos-references/ts-basic-components-navdestination.md#bindtoscrollable14)）
* 新增支持设置窗口使用效果模板，比如使用有透视的背景模糊效果。（[API参考](../harmonyos-references/ts-universal-attributes-use-effect.md#useeffect14)）
* 针对PC/2in1设备的应用的窗口管理，新增通过应用窗口关闭按钮关闭应用的监听，使用该API可忽略已设置的预关闭开关的回调。（[API参考](../harmonyos-references/arkts-apis-window-windowstage.md#onwindowstageclose14)）
* 针对PC/2in1设备的应用的窗口管理，新增自定义应用主窗口大小和位置的能力，通过配置文件module.json5进行配置。（[指南](../harmonyos-guides/module-configuration-file.md#metadata标签)）
* 针对PC/2in1设备的应用的窗口管理，新增支持将应用从最小化恢复到前台显示的能力。（[API参考](../harmonyos-references/arkts-apis-window-window.md#restore14)）
* 针对PC/2in1设备的应用的窗口管理，新增支持查询本应用内指定坐标下的可见窗口的能力。（[API参考](../harmonyos-references/arkts-apis-window-f.md#windowgetwindowsbycoordinate14)）
* 针对PC/2in1设备的应用的窗口管理，新增支持使能/禁用通过拖拽方式缩放主窗口或子窗口。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setresizebydragenabled14)）
* 针对PC/2in1设备的应用的窗口管理，新增支持设置主窗口为模态窗口。（[API参考](../harmonyos-references/arkts-apis-window-windowstage.md#setwindowmodal14)）
* 针对PC/2in1设备的应用的窗口管理，新增支持应用控制启动页消失时机。（[API参考](../harmonyos-references/arkts-apis-window-windowstage.md#removestartingwindow14)）
* 针对PC/2in1设备的应用的窗口管理，新增支持设置主窗的尺寸记忆是否启用。（[API参考](../harmonyos-references/arkts-apis-window-windowstage.md#setwindowrectautosave14)）
* 针对PC/2in1设备的应用的窗口管理，新增支持设置主窗口进入全屏沉浸式时鼠标Hover到热区上隐藏窗口标题栏和dock栏。（[API参考](../harmonyos-references/arkts-apis-window-window.md#settitleanddockhovershown14)）
* 针对PC/2in1设备的应用的窗口管理，新增支持设置主窗标题栏上的最大化、最小化、关闭按钮是否可见。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setwindowtitlebuttonvisible14)）
* 针对PC/2in1设备的应用的窗口管理，新增支持设置主窗口置于其他应用窗口之上而不被遮挡。（[API参考](../harmonyos-references/arkts-apis-window-window.md#setwindowtopmost14)）
* 针对PC/2in1设备的应用的窗口管理，新增支持对窗口所在屏幕进行事件监听，例如当前窗口移动到其他屏幕时，可以从此接口监听到这个行为。（[API参考](../harmonyos-references/arkts-apis-window-window.md#ondisplayidchange14)）
* 针对PC/2in1设备的应用的窗口管理，新增支持应用窗口无系统标题栏场景下拖拽移动窗口的能力。（[API参考](../harmonyos-references/arkts-apis-window-window.md#startmoving14)）

## ArkWeb

* 用户主动收起软键盘时，新增支持设置焦点从输入框转移到Web的body上，使文本框失焦。（[API参考](../harmonyos-references/arkts-basic-components-web-attributes.md#bluronkeyboardhidemode14)）
* 新增C API，用于获取调用JavaScriptProxy最后一帧的url。（[API参考](../harmonyos-references/capi-web-arkweb-controllerapi.md#getlastjavascriptproxycallingframeurl)）
* 新增支持获取默认的用户代理。（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#getdefaultuseragent14)）
* 新增支持为指定url设置cookie的值。（[API参考](../harmonyos-references/arkts-apis-webview-webcookiemanager.md#configcookiesync14)）
* 新增支持上下左右四种嵌套滚动模式。（[API参考](../harmonyos-references/arkts-basic-components-web-attributes.md#nestedscroll11)）
* 新增支持根据指定的内存压力等级主动清理Web组件占用的缓存。（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#trimmemorybypressurelevel14)）
* 新增支持网页另存为PDF的能力。（[API参考](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#createpdf14)）
* 新增支持设置滚动动画的持续时间。（[API参考-scrollTo](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#scrollto)、[API参考-scrollBy](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#scrollby)）
* 新增支持设置滚动条常驻。（[API参考](../harmonyos-references/arkts-basic-components-web-attributes.md#forcedisplayscrollbar14)）

## AVCodec Kit

音视频编解码的C API新增支持HE-AAC编解码能力，该能力仅在HarmonyOS支持。（[API参考](../harmonyos-references/capi-codecbase.md#媒体编解码格式)）

## AVSession Kit

新增支持投播半模态对象的能力。（[API参考](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md)）

## Basic Service Kit

* 设备信息（Device Info）模块新增productModelAlias属性用于支持查询设备认证型号的别名。（[API参考](../harmonyos-references/js-apis-device-info.md)）
* 剪贴板新增支持通过MIME定义和使用多种格式的内容对象。（[API参考](../harmonyos-references/js-apis-pasteboard.md#pasteboardcreatedata14)）
* 剪贴板新增C API和ArkTS API支持获取剪贴板内容的MIME类型。（[C API参考](../harmonyos-references/capi-oh-pasteboard-h.md#oh_pasteboard_getmimetypes)、[ArkTS API参考](../harmonyos-references/js-apis-pasteboard.md#getmimetypes14)）
* USB管理新增支持检查应用程序是否有权访问USB配件。（[API参考](../harmonyos-references/js-apis-usbmanager.md#usbmanagerhasaccessoryright14)）

## Call Service Kit

* kit名称修改，导致kit文件名称变更。（[指南](../harmonyos-guides/call-introduction.md)）
* 支持企业联系人来去电显示功能。（[指南](../harmonyos-guides/callservice-enterprise-contact-display.md)）

## Camera Kit

新增C API和ArkTS API用于设置录像质量的优先级，提供高质量和功耗平衡两档选择。（[C API参考](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_setqualityprioritization)、[ArkTS API参考](../harmonyos-references/arkts-apis-camera-videosession.md#setqualityprioritization14)）

## Core File Kit

新增支持获取保存成功后的文件后缀类型的下标。（[API参考](../harmonyos-references/js-apis-file-picker.md#getselectedindex14)）

## Crypto Architecture Kit

[非对称密钥生成和转换](../harmonyos-guides/crypto-asym-key-generation-conversion-spec.md#使用字符串参数生成-1)、[密钥协商](../harmonyos-guides/crypto-key-agreement-overview.md#ecdh)、[签名验签](../harmonyos-guides/crypto-sign-sig-verify-overview.md#ecdsa)所使用的ECC算法支持secp256k1曲线。

## Data Protection Kit

新增数据防泄漏（DLP）解决方案，通过C API提供对应能力的调用。（[API参考](../harmonyos-references/capi-dlppermissionapi.md)）

## Game Service Kit

* 游戏场景感知模块提供C API。（[API参考](../harmonyos-references/gameservice-c.md)）
* 支持订阅或查询GPU信息时，返回GPU当前频点。（[API参考](../harmonyos-references/gameservice-gameperformance.md#gpuinfo)）

## IAP Kit

支持非续期订阅类型商品的购买。（[指南](../harmonyos-guides/iap-nonrenewable.md)）

## IME Kit

输入法框架提供的编辑框属性新增编辑框所属应用的包名。（[API参考](../harmonyos-references/js-apis-inputmethodengine.md#editorattribute)）

## Live View Kit

支持设置左右文本模板扩展区文本子样式类型、右侧标题和内容的右上角展示内容、中间间隔文本、扩展区底部内容等。（[API参考](../harmonyos-references/liveview-liveviewmanager.md#flightlayout)）

## Location Kit

新增地理围栏类型的ExtensionAbility，提供基于位置的地理围栏的能力。（[指南](../harmonyos-guides/fenceextensionability.md)、[API参考](../harmonyos-references/js-apis-app-ability-fenceextensionability.md)）

## MDM Kit

* 企业应用禁用设备功能的能力新增支持禁用设备相机能力。（[API参考](../harmonyos-references/js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicy)）
* 企业应用安装事件新增一类回调，该回调返回的信息包括安装包名和账号ID。（[API参考](../harmonyos-references/js-apis-enterpriseadminextensionability.md#enterpriseadminextensionabilityonbundleadded14)）
* 企业应用新增支持委托其他应用来设置设备的管控策略。（[API参考](../harmonyos-references/js-apis-enterprise-adminmanager.md#adminmanagersetdelegatedpolicies14)）
* 企业应用新增支持设置禁用/启用设备指纹功能，该能力目前仅限PC/2in1设备使用。（[API参考](../harmonyos-references/js-apis-enterprise-restrictions.md#restrictionssetdisallowedpolicyforaccount14)）
* 企业应用新增支持设置禁用屏幕快照（即截屏）功能，该能力目前仅限PC/2in1设备使用。（[API参考](../harmonyos-references/js-apis-enterprise-restrictions.md#restrictionsadddisallowedlistforaccount14)）
* 企业应用新增支持对应用设置水印的能力，该能力目前仅限PC/2in1设备使用。（[API参考](../harmonyos-references/js-apis-enterprise-securitymanager.md#securitymanagersetwatermarkimage14)）
* 企业应用新增支持“设备管理”应用添加保活的应用，该能力目前仅限PC/2in1设备使用。（[API参考](../harmonyos-references/js-apis-enterprise-applicationmanager.md#applicationmanageraddkeepaliveapps14)）
* 企业应用新增支持“设备管理”应用添加禁止使用的USB设备类型，该能力目前仅限PC/2in1设备使用。（[API参考](../harmonyos-references/js-apis-enterprise-usbmanager.md#usbmanageradddisallowedusbdevices14)）

## Media Kit

* 新增C API支持设置录屏时的最大帧率。（[API参考](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_setmaxvideoframerate)）
* 流媒体新增一批错误码以细化流媒体播放可能出现的异常场景。（[API参考](../harmonyos-references/arkts-apis-media-e.md#averrorcode9)）

## Media Library Kit

* 新增支持定义配置相册图片后的完成按钮，可显示“完成”、“发送”或“添加”。（[API参考](../harmonyos-references/arkts-apis-photoaccesshelper-e.md#completebuttontext14)）
* Photo Picker组件新增支持大图页视频播放状态的回调videoPlayStateChangedCallback。（[API参考](../harmonyos-references/ohos-file-photopickercomponent.md#videoplaystatechangedcallback14)）

## Payment Kit

新增通用收银台，支持多种支付方式。（[指南](../harmonyos-guides/payment-common-pay-connect.md)）

## Push Kit

支持场景化消息类型为通知消息场景（DEFAULT类型）。（[API参考](../harmonyos-references/push-pushservice.md#pushservicepushtype)）

## Scenario Fusion Kit

* 支持文件路径转换，即可实现将源文件路径转换为目标文件路径。（[指南](../harmonyos-guides/scenario-fusion-api-path-conversion.md)）
* 支持权限设置button，实现二次拉起权限设置弹框。（[指南](../harmonyos-guides/scenario-fusion-button-permissiononsetting.md)）

## Speech Kit

* 朗读控件支持在线预录制播报场景。（[API参考](../harmonyos-references/speech-textreader-api.md#readinfo)）
* 朗读控件支持[朗读起播](../harmonyos-references/speech-textreader-api.md#start-1)以及[起播参数](../harmonyos-references/speech-textreader-api.md#startparams)、[朗读参数](../harmonyos-references/speech-textreader-api.md#readerparam)的定制。

## Status Bar Extension Kit

支持监听状态栏图标点击事件、右键菜单点击事件。（[API参考-监听状态栏图标点击事件](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageronstatusbariconclick)，[API参考-监听右键菜单点击事件](../harmonyos-references/statusbar-extension-manager.md#statusbarmanageronrightmenuclick)）

## Store Kit

* 支持应用市场推荐场景下，应用内快捷方式加桌。（[指南](../harmonyos-guides/store-productview.md#通过app-linking拉起写评论页-1)）
* 应用详情页展示和元服务卡片加桌场景下，支持成功打开和关闭回调函数。（[API参考](../harmonyos-references/store-productviewmanager.md#productviewcallback)）
* 应用详情页展示场景下，支持设置登记归因来源的广告曝光数据属性参数。（[API参考](../harmonyos-references/store-productviewmanager.md#skexposure)）
* 产品特性按需分发新增C接口，支持用户按需动态下载所需的增强特性。（[API参考](../harmonyos-references/store-c.md)）
* 支持拉起标准化隐私弹框。（[API参考](../harmonyos-references/store-privacymanager.md#privacymanagerrequestappprivacyconsent)）

## Vision Kit

* 支持对身份证图片质量检测，包括检测身份证图片是否完整、是否反光。（[API参考](../harmonyos-references/vision-card-recognition.md#idcardconfig)）
* 支持获取当前图片分析UI状态。（[API参考](../harmonyos-references/vision-image-analyzer.md#getimageanalyzeruistatus)）

## Weather Service Kit

支持根据调用方提供的上下文信息获取天气数据。（[API参考](../harmonyos-references/weather-service-weatherservice.md#weatherservicegetweatherwithcontext)）

## XEngine Kit

新增支持平板和PC/2in1设备。（[指南](../harmonyos-guides/xengine-kit-preparations.md#硬件要求)）

## 公共

* 配置文件[module.json5中abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)的orientation属性新增支持通过资源索引方式（$string）进行配置。
* 配置文件[module.json5中extensionAbilities标签](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)的extensionProcessMode属性新增支持配置runWithMainProcess类型，表示该ExtensionAbility和应用主进程共进程。
* 配置文件[module.json5中extensionAbilities标签](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)新增process属性，type为embeddedUI的ExtensionAbility可通过该属性的配置使ExtensionAbility和Ability运行在同一进程。

## 工具

* 使用[打包工具](../harmonyos-guides/packing-tool.md#app打包指令)打包APP时，支持打包加密配置文件。本特性不涉及命令、接口的新增，仍可参照原有工具指导进行打包操作。
* [mediatool工具](../harmonyos-guides/mediatool.md#查询命令mediatool-query)查询媒体库资源的命令新增返回资源源文件真实路径或媒体资源uri的参数。
