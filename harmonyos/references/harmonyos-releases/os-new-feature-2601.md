---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-2601
title: OS新增和增强特性
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > OS新增和增强特性
category: harmonyos-releases
scraped_at: 2026-11-14T08:45:41+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:106a5d4c1309e7dcccd7f1d9177492aa55025b684bbb0a23322f10a72061359c
---

## 26.0.1 Beta1

### Ability Kit

* 新增应用自身子进程信息查询能力，提供[childProcessManager.getChildProcessInfos](../doccenter-references/api/js-apis-app-ability-childprocessmanager.md#childprocessmanagergetchildprocessinfos)、[ApplicationContext.getUIAbilityChildProcessInfos](../doccenter-references/api/js-apis-inner-application-applicationcontext.md#applicationcontextgetuiabilitychildprocessinfos)接口及对应的C API，返回子进程的PID、父进程PID和进程名。
  + 不带页面的子进程：通过Native子进程接口及childProcessManager.startChildProcess（非SELF\_FORK模式）、startArkChildProcess、startNativeChildProcess创建。（[API参考](../doccenter-references/api/js-apis-app-ability-childprocessmanager.md#childprocessmanagerstartchildprocess)）
  + UIAbility子进程：通过startSelfUIAbilityInChildProcess接口启动，或通过startAbility接口启动且processMode设置为NEW\_PROCESS\_ATTACH\_TO\_PARENT的子进程。（[API参考](../doccenter-references/api/js-apis-inner-application-uiabilitycontext.md#startselfuiabilityinchildprocess)）
* 新增子进程信息读取与释放的C API，支持按索引获取子进程信息、获取子进程PID、父进程PID、进程名，以及释放子进程信息集合。（[API参考](../doccenter-references/api/capi-child-process-info-h.md)）
* 应用快启管理新增支持获取指定场景下当前应用的最后一次快启错误信息。（[API参考](../doccenter-references/api/js-apis-app-ability-hypersnapmanager.md#hypersnapmanagergetlasterror)）

### AppGallery Kit

应用市场推荐、产品特性按需分发、生态查询服务、应用市场更新功能、应用归因服务、隐私管理服务、图标管理服务能力新增支持Car设备。（[指南](../doccenter-capabilities/store-introduction.md#支持的设备)）

### ArkGraphics 2D

文字绘制能力的C API新增支持多个创建文本对象的接口，这些接口支持字体回退。（[API参考-1](../doccenter-references/api/capi-drawing-text-blob-h.md#oh_drawing_textblobcreatefromtextwithfallback)、[API参考-2](../doccenter-references/api/capi-drawing-text-blob-h.md#oh_drawing_textblobcreatefrompostextwithfallback)、[API参考-3](../doccenter-references/api/capi-drawing-text-blob-h.md#oh_drawing_textblobcreatefromstringwithfallback)）

### ArkTS

* 新增支持在解析JSON字符串时生成可跨线程共享的Sendable对象（[API参考](../doccenter-references/api/js-apis-json.md#jsonparsesendable)）。可用于解析包含大量数字键的JSON字符串等场景（[指南](../doccenter-capabilities/commonlibrary-faq.md#解析包含大量数字键的json字符串)）。
* ArkTS容器集Map类新增多个接口，支持判断指定键值对映射关系（[API参考](../doccenter-references/api/arkts-apis-arkts-collections-map.md#containsvalue)），以及更新（[API参考-put](../doccenter-references/api/arkts-apis-arkts-collections-map.md#put)、[API参考-putAll](../doccenter-references/api/arkts-apis-arkts-collections-map.md#putall)）、删除指定键值对映射（[API参考](../doccenter-references/api/arkts-apis-arkts-collections-map.md#remove)）。

### ArkUI

* LazyForEach新增onDataReloaded的同名接口，支持配置是否允许在更新过程中复用旧的子组件。（[API参考](../doccenter-references/api/ts-rendering-control-lazyforeach.md#ondatareloaded-1)）
* 窗口管理新增窗口焦点状态的变化信息WindowFocusState（[API参考](../doccenter-references/api/arkts-apis-window-i.md#windowfocusstate)）和调整主窗口Z序时使用的位置参数WindowPositionParams（[API参考](../doccenter-references/api/arkts-apis-window-i.md#windowpositionparams)）。
* Navigation组件新增接口，支持预加载指定的NavDestination页面。（[API参考](../doccenter-references/api/ts-basic-components-navigation.md#preloadpath)）
* NavigationConfiguration新增clearContentStackOnPrimaryNavigation属性，支持左起右清栈效果。（[API参考](../doccenter-references/api/ts-basic-components-navigation.md#示例21开启左起右清栈效果)）
* 子标题组件（SubHeader）新增支持设置尾部图标。（[API参考-SubHeader](../doccenter-references/api/ohos-arkui-advanced-subheader.md#示例10设置子标题尾部图标)、[API参考-SubHeaderV2](../doccenter-references/api/ohos-arkui-advanced-subheaderv2.md#示例10设置子标题尾部图标)）
* 动画组件的C API新增[属性动画](../doccenter-references/api/capi-arkui-nativemodule-arkui-propertyanimation8h.md)、[关键帧动画](../doccenter-references/api/capi-arkui-nativemodule-arkui-keyframeanimation8h.md)、[路径动画](../doccenter-references/api/capi-arkui-nativemodule-arkui-pathanimation8h.md)、[动画组](../doccenter-references/api/capi-arkui-nativemodule-arkui-animationgroup8h.md)的句柄定义。
* TabContent组件新增tabBarVisibility属性，支持设置页签在不同样式的页签栏中的可见性。（[API参考](../doccenter-references/api/ts-container-tabcontent.md#示例12设置页签在不同页签栏中的可见性)）
* Text组件的C API新增支持创建文本行间距选项对象（[API参考](../doccenter-references/api/capi-text-h.md#oh_arkui_nativemodule_linespacingoptions_create)），同时支持通过文本行间距选项的onlyBetweenLines参数设置首行上方和尾行下方是否有额外的行间距（[API参考](../doccenter-references/api/capi-text-h.md#oh_arkui_nativemodule_linespacingoptions_setonlybetweenlines)）。

### Background Tasks Kit

新增支持更新包含数据传输类型的长时任务通知。（[API参考](../doccenter-references/api/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundtaskmanagerupdatedatatransferprogress)）

### Basic Services Kit

* 设备管理的C API新增USB管理能力，支持管理USB设备驱动。（[指南](../doccenter-capabilities/devicemanager-capi.md)、[API参考](../doccenter-references/api/capi-ohusb-manager-h.md)）
* 设备管理新增支持板级硬件信息查询能力，支持获取CPU、主板、BIOS等硬件信息，适用于设备识别、资产管理、兼容性判断等场景。（[API参考](../doccenter-references/api/js-apis-board-info.md)）
* 账号管理新增系统账号授权管理能力，提供操作系统本地账号的授权管理能力。（[API参考](../doccenter-references/api/js-apis-osaccount-authorization.md)）

### Call Service Kit

* 新增外设VoIP通话控制，实现远端设备（如第三方穿戴设备）上控制本设备的VoIP通话的接听、挂断等。（[指南](../doccenter-capabilities/remote-voip-call-control.md)、[API参考](../doccenter-references/api/call-voipcallcontrol.md)）
* 新增支持隐私查询企业服务信息。（[指南](../doccenter-capabilities/callservice-enterprise-service-display.md)、[API参考](../doccenter-references/api/callservicekit-callerinfoquery-extension-ability.md#onquerybusinessservicedatawithprotocol)）
* 企业服务信息新增外卖服务类型及数据。（[API参考](../doccenter-references/api/callservicekit-numberldentify.md#carryoutdata)）

### CANN Kit

新增支持Car设备。（[指南](../doccenter-capabilities/cannkit-introduction.md#约束与限制)）

### Core File Kit

* 新增卷（Volume）管理模块，提供外置存储磁盘设备和卷设备信息查询的相关功能。（[API参考](../doccenter-references/api/js-apis-file-volumemanager.md)）
* 云盘管理新增支持云盘类应用注册带占位符信息的同步根（[API参考](../doccenter-references/api/capi-oh-cloud-disk-manager-h.md#oh_clouddisk_registersyncfolderex)），适用于需要将本地目录设置为云盘同步目录并标记是否支持占位符的场景。同时支持获取所有带占位符的同步根（[API参考](../doccenter-references/api/capi-oh-cloud-disk-manager-h.md#oh_clouddisk_getsyncfoldersex)）。

### Core Speech Kit

新增文本转语音暂停/继续播报接口，支持控制文本播报的暂停和恢复。（[API参考](../doccenter-references/api/hms-ai-texttospeech.md#pause)）

### Data Protection Kit

新增隐私计算能力，提供隐私保护的数据比对与检索能力，包括隐私目标生成、隐私搜索、搜索结果检索。（[指南](../doccenter-capabilities/privacy-computation-guidelines.md)）

### Device Certificate Kit

新增UkeyAuthExtensionAbility（[API参考](../doccenter-references/api/js-apis-ukeyauthextensionability.md)）及其上下文UkeyAuthExtensionContext（[API参考](../doccenter-references/api/js-apis-ukeyauthextensioncontext.md)），用于自定义UKey认证时的UI显示。

### Device Security Kit

* 新增自定义DLP文件访问和光盘刻录拦截通知类审计事件。（[API参考](../doccenter-references/api/devicesecurity-securityaudit-api.md#notifyevent)）
* 新增侧载安全管控能力。支持查询设备是否允许加载外部二进制文件，以及打开外部二进制源控制开关的设置弹窗以请求用户修改开关状态。（[API参考](../doccenter-capabilities/devicesecurity-sideloading.md)）

### Enterprise Data Guard Kit

* 新增删除策略，支持开发者从已配置的管控策略集合中删除对应的策略信息。（[API参考](../doccenter-references/api/dataguard-fileguard.md#deletepolicy)）
* 新增进程UID可信任列表管理，支持开发者查询、添加与删除进程UID可信任列表。（[API参考](../doccenter-references/api/dataguard-fileguard.md#querytrustedprocessuid)）
* 新增加密U盘管理，支持开发者挂载或卸载加密U盘的加密区与交换区。（[API参考](../doccenter-references/api/dataguard-encryptedusbmanager.md)）
* 新增获取数据盘企业恢复密钥，支持开发者获取数据盘企业恢复密钥，用于解密数据盘。（[API参考](../doccenter-references/api/dataguard-recoverykey.md#recoverykeygetdatavolumeenterpriserecoverykey)）
* 新增企业账号验证用户身份，支持开发者通过企业账号核验用户身份，获取重置锁屏密码的企业恢复密钥。（[API参考](../doccenter-references/api/dataguard-recoverykey.md#recoverykeyverifyuserbyenterpriseauthentication)）

### Enterprise Foundation Kit

【新增Kit】Enterprise Foundation Kit（企业办公服务）面向企业应用，提供组织生产力开发能力，包括数据备份与还原功能，助力开发者高效构建安全合规的企业应用。（[指南](../doccenter-capabilities/enterprises-foundation-introduction.md)、[API参考](../doccenter-references/api/enterprise-foundation.md)）

### FAST Kit

新增支持Car设备。（[指南](../doccenter-capabilities/fast-introduction.md#支持的设备)）

### File Manager Service Kit

* 新增自定义文件角标和右键菜单项的能力。（[指南](../doccenter-capabilities/filemanagerservice-filemanagerextension.md)）
* 新增C接口，提供将云盘同步根文件夹添加到文件管理应用侧边栏以及设置同步文件夹图标的能力。（[指南](../doccenter-capabilities/filemanagerservice-capi-sidebar.md)、[API参考](../doccenter-references/api/capi-filemanager-service-h.md)）

### Game Service Kit

* 游戏场景感知实况窗后台保活能力支持本地调试。（[指南](../doccenter-capabilities/gameservice-gameperformance-keep-alive.md)）
* 游戏场景感知新增支持设置游戏触控区域。（[指南-ArkTS](../doccenter-capabilities/gameservice-gameperformance-set-touch-area.md)、[API参考-ArkTS](../doccenter-references/api/gameservice-gameperformance.md#gametoucharea)、[指南-C/C++](../doccenter-capabilities/gameservice-gameperformance-set-touch-area-c.md)、[API参考-C/C++](../doccenter-references/api/gameservice-game-performance.md#gameperformance_toucharea)）
* 基础游戏服务新增支持Car设备。（[指南](../doccenter-capabilities/gameservice-introduction.md#支持的设备)）

### Graphics Accelerate Kit

* 游戏资源加速服务新增查询是否支持设置和查询资源包后台下载开关状态的能力。（[API参考](../doccenter-references/api/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerissupportdownloadswitchsetting)）
* 游戏资源加速服务新增[queryDownloadSwitchEnabled](../doccenter-references/api/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagerquerydownloadswitchenabled)、[setDownloadSwitchEnabled](../doccenter-references/api/graphics-accelerate-assetdownloadmanager.md#assetdownloadmanagersetdownloadswitchenabled)接口，分别支持查询和设置当前游戏资源包后台下载开关状态。

### Health Service Kit

* Lite Wearable设备新增支持笼式网球、滑雪、户外跑步、户外骑行、自由训练和普拉提运动类型，并且同步开放对应的锻炼记录数据。（[API参考](../doccenter-references/api/health-api-exercisesequencehelper-lite.md#outdoorsnowboard)）
* 新增C API，提供应用与Lite Wearable设备进行运动数据交互的能力，如实时传输心率、卡路里等运动数据。（[API参考](../doccenter-references/api/capi-workout-dict-data-h.md)）
* Wearable设备新增支持笼式网球、滑雪、自由训练和普拉提运动类型，并且同步开放对应的锻炼记录数据。（[API参考](../doccenter-references/api/health-api-healthfields.md#padelsummary)）
* Wearable设备户外跑步、户外骑行锻炼记录新增训练负荷等数据开放。（[API参考](../doccenter-references/api/health-api-healthfields.md#cyclingsummary)）

### IAP Kit

新增支持支付优惠查询功能，通过让用户在购买前预览实际享受的优惠，提升应用下单转化率。（[指南](../doccenter-capabilities/iap-payment-promotions.md)、[API参考](../doccenter-references/api/iap-iap.md#iapquerypaymentpromotions)）

### Intents Kit

新增支持应用注册热词并处理执行回调，使智慧语音助手能够响应用户更多操控应用界面可见的UI元素语音指令，帮助应用拓展可视可说能力的可用范围。（[指南](../doccenter-capabilities/intents-voice-control-guide.md)、[API参考](../doccenter-references/api/intents-visible-voice-control-arkts-api.md)）

### Image Kit

ImageReceiver类新增支持为接收的图像缓冲区设置内存标识符，便于在内存调试或问题定位时识别相关缓冲区。（[API参考](../doccenter-references/api/arkts-apis-image-imagereceiver.md#setmemoryname)）

### Input Kit

新增支持对鼠标光标和光标类型外设的管理功能。（[API参考](../doccenter-references/api/js-apis-pointer.md)）

KeyCode定义中新增云台设备的相关按键定义。（[ArkTS API参考](../doccenter-references/api/js-apis-keycode.md#keycode)、[C API参考](../doccenter-references/api/capi-oh-key-code-h.md#input_keycode)）

### Localization Kit

新增字体管理模块，支持为应用提供第三方字体的安装、卸载、查询以及字体服务状态监听能力。（[API参考](../doccenter-references/api/js-apis-font-manager.md)）

### Map Kit

新增支持3D地球设置球体中线距离屏幕的比例值。（[API参考](../doccenter-references/api/map-common.md#sphereparams)）

### MDM Kit

* 系统管理新增多个接口能力：
  + 新增支持管理基于IP的网络打印机白名单策略，支持以设备视角或用户视角进行添加、删除、查询等多种操作。（[API参考](../doccenter-references/api/js-apis-enterprise-systemmanager.md#systemmanageraddallowedprinteripaddressesfordevice)）
  + 新增支持管理精确定时器，支持创建、启动、停止、销毁精确定时器的操作。适用于企业设备需要精确定时执行任务的场景。（[API参考](../doccenter-references/api/js-apis-enterprise-systemmanager.md#systemmanagercreateexacttimer)）
* 安全管理新增用于锁屏弱密码校验的弱密码库设置，设置弱密码库后，用户无法在设置锁屏密码时使用库中包含的弱密码。（[API参考](../doccenter-references/api/js-apis-enterprise-securitymanager.md#securitymanagersetweakpinenable)）
* 应用管理新增多个接口能力：
  + 支持为指定应用申请待机资源豁免。申请成功后，指定应用可以在设备进入待机模式时继续使用被豁免的资源（如网络访问）。（[API参考](../doccenter-references/api/js-apis-enterprise-applicationmanager.md#applicationmanagerrequestexemptionresource)）
  + 支持添加指定卡片到当前用户的桌面。（[API参考](../doccenter-references/api/js-apis-enterprise-applicationmanager.md#applicationmanagerpublishformtodesktop)）

### Media Kit

屏幕录制的C API能力新增支持创建虚拟扩展屏幕并对其内容进行录制。（[指南](https://gitcode.com/openharmony/docs/blob/weekly_20261012/zh-cn/application-dev/media/media/avscreencapture-c-basic-process.md#录制虚拟扩展屏幕)）

### PDF Kit

* 新增在PDF界面中自由绘制曲线以及使用橡皮擦擦除曲线的能力。（[API参考](../doccenter-references/api/pdf-arkts-pdfviewmanage.md#enablepen)）
* 新增在PDF界面中同时添加多个不同颜色的临时高亮矩形的能力。（[API参考](../doccenter-references/api/pdf-arkts-pdfviewmanage.md#sethighlightrectswithcolors)）

### Performance Analysis Kit

hidebug的C API新增一批接口，包括：hiprofiler资源采集API新增混合类型，支持Global Handle对象调用栈、堆快照、映射文件打包；2D资源采集API开放场景，hiprofiler StartProfiler接口新增异步嵌套层数、每层异步栈深配置参数；资源采集API新增DMABUF资源类型，支撑应用自行采集DMA内存分配栈；支持分配释放栈消减去重能力，减少数据采集量，降低性能开销。（请在[API参考](../doccenter-references/api/capi-hidebug-h.md)页面内搜索关键词“26.0.1”）

新增支持external\_log日志管理者注册接口，确保故障日志沙箱目录容量达到阈值时可通知应用清理删除external\_log文件。（[指南](../doccenter-capabilities/external-log.md)）

### Spatial Recon Kit

* 新增端云重建鉴权签名接口，支持为待重建的mp4视频文件派生云侧验签凭证。（[API参考](../doccenter-references/api/capi-spatial-recon-interface-h.md#hms_spatialrecon_derivefileverifykey)）
* 新增分档渲染接口，支持为3DGS大场景提供渲染质量等级配置能力。（[API参考](../doccenter-references/api/spatial-recon-spatialrender.md#tiledgsrenderpreference)）
* 新增碰撞检测接口，支持为3DGS大场景漫游提供碰撞检测能力。（[API参考](../doccenter-references/api/spatial-recon-spatialrender.md#cameracollisiondetector)）

### UI Design Kit

HdsColorPicker颜色选择器组件新增显示状态控制及状态变化回调能力。（[API参考](../doccenter-references/api/ui-design-hdscolorpicker.md#hdscolorpicker)）

### User Authentication Kit

新增用户识别能力，应用可查询最新识别结果或订阅识别结果变化，用于判断当前使用者是否与已登录的系统用户匹配。（[指南](../doccenter-capabilities/obtain-user-recognition-result.md)）

### Wear Engine Kit

新增支持穿戴表盘能力，包括将构造好的表盘配置添加到穿戴设备以及生成对应预览展示效果等。（[API参考](../doccenter-references/api/watchface_api.md)）

### Weather Service Kit

新增朝霞晚霞天气数据。（[API参考](../doccenter-references/api/weather-service-weatherservice.md#weather)）

### XEngine Kit

新增支持Car设备。([指南](../doccenter-capabilities/xengine-kit-gpu-spatial-upscaling.md#约束与限制))
