---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/os-new-feature-500
title: 新增和增强特性
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 新增和增强特性
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:b72ad7481f53aee145041568a9ce871f4c3c5f76767fda0a8c777f54ed6ca161
---

## 应用框架

### Ability Kit（程序框架服务）

Ability Kit（程序框架服务）提供了应用程序开发和运行的应用模型，是系统为开发者提供的应用程序所需能力的抽象提炼，它提供了应用程序必备的组件和运行机制。有了应用模型，开发者可以基于一套统一的模型进行应用开发，使应用开发更简单、高效。

Ability Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

**应用框架**

* AppStartUp框架提供一种在应用启动时初始化组件的简单而高效的方法，有效提升启动性能。
* 新增元服务启动API，提供跳出式和嵌入式两种启动方式。
* 填充服务支持以非模态的Popup形式拉起，提供数据的填充和保存服务。
* 支持根据hint识别情景化自动填充类型，比如hint是“请输入手机号码”，把其识别为手机号码类型的自动填充类型。
* aa工具支持隐式启动应用。
* 统一DeepLink和AppLinking跳转技术方案，降低开发者使用成本，提高跳转安全性。
* 提供安全的应用重启应用能力。
* 系统环境新增字体大小和粗细变化通知。
* UIExtension调用直接结果返回。
* UIAbilityContext提供获取WindowStage能力，提供应用主动把UIAbility移到后台能力。
* 支持跨端迁移时：同应用可跨Ability迁移；应用可使用异步接口保存数据；应用可配置立即启动字段，在pull场景下提前启动可迁移应用。

**包管理**

* 业务模块（HSP/HAR）支持配置router\_map.json路由表，实现模块间动态路由解耦。
* 支持集成态HSP，集团内部的多个应用之间，可以使用集成态HSP实现代码和资源共享。
* 支持卸载更新的能力，通过应用市场更新的预置应用，可以通过卸载更新恢复到出厂的版本。
* 提供In-House应用的安装及查询能力，支持In-House应用管理。
* 统一资源缓存，支持overlay和主题切换场景。
* 支持gzip格式文件解压缩能力。
* 静态快捷方式能力增强，支持跳转到指定的页面。
* 支持resfile目录，resfile目录开发者可以自由放置各类资源文件，应用安装时，资源会被解压到应用沙箱路径。
* zlib模块新增GZip的相关能力。（[API参考](../harmonyos-references-V5/js-apis-zlib-V5.md#gzip12)）
* 新增Native子进程的开发能力。（[指南](../harmonyos-guides-V5/capi_nativechildprocess_development_guideline-V5.md)）
* 支持应用监听UIAbility的生命周期。（[API参考](../harmonyos-references/js-apis-app-ability-abilitylifecyclecallback.md#onabilitywillcreate12)）
* 默认应用的管理、查询、打开支持UTD格式，即[module.json5配置文件](../harmonyos-guides-V5/module-configuration-file-V5.md#skills标签)uris标签的type属性新增支持[UniformDataType](../harmonyos-references-V5/js-apis-data-uniformtypedescriptor-V5.md#uniformdatatype)类型规范。
* Node-API支持在模块加载失败时生成异常对象，并设置异常信息到对象属性中。（[指南](../harmonyos-guides-V5/use-napi-faqs-V5.md#arktsjs侧import-xxx-from-libxxxso后使用xxx报错显示undefinednot-callable或明确的error-message)）
* 支持查询应用的分身信息。（[API参考](../harmonyos-references-V5/js-apis-inner-application-applicationcontext-V5.md#applicationcontextgetcurrentappcloneindex12)）
* ErrorManager支持监听应用运行时未被捕获的rejection事件。（[API参考](../harmonyos-references-V5/js-apis-app-ability-errormanager-V5.md#unhandledrejectionobserver12)）

详细信息请参见[Ability Kit开发指南](../harmonyos-guides-V5/ability-kit-V5.md)。

* 程序访问控制支持拉起设备设置页面的应用权限管理界面。（[API参考](../harmonyos-references-V5/js-apis-abilityaccessctrl-V5.md#requestpermissiononsetting12)）
* 在release模式下打包APP时可以选择对APP内的HAP、HSP包进行压缩。（[指南](../harmonyos-guides-V5/packing-tool-V5.md#app打包指令)）
* 新增支持传参和异步ArkTS API调用的子进程启动方法。（[API参考](../harmonyos-references-V5/js-apis-app-ability-childprocessmanager-V5.md#childprocessmanagerstartarkchildprocess12)）
* 新增支持want属性中parameter参数支持更多描述信息，包括callerAbilityName（拉起方的AbilityName）、callerNativeName（Native调用时拉起方的进程名）、callerAppId（拉起应用的AppId信息）、callerAppIdentifier（拉起应用的AppIdentifier信息）。（[API参考](../harmonyos-references-V5/js-apis-app-ability-want-V5.md)）
* 新增API用以支持拉起目标方Ability并在目标方返回结果的同时返回拉起动作的发起方。（[API参考](../harmonyos-references-V5/js-apis-inner-application-uiabilitycontext-V5.md#uiabilitycontextbacktocallerabilitywithresult12)）

### Accessibility Kit（无障碍开发服务）

Accessibility Kit（无障碍开发服务）为应用开放无障碍适配接口，让应用可以查询无障碍开启状态、发送无障碍事件等，以便应用可以更好的适配无障碍，更好的服务于障碍人群。

Accessibility Kit在HarmonyOS NEXT阶段新增了主动聚焦、主动播报的能力，满足应用适配屏幕朗读时需要主动聚焦、主动播报的场景诉求。

详细信息请参见[Accessibility Kit开发指南](../harmonyos-guides-V5/accessibility-kit-V5.md)。

### ArkData（方舟数据管理）

ArkData（方舟数据管理）是多模态（关系型、键值型、文档型）、端端&端云一体（分布式数据库、分布式变量）的数据存储框架。

ArkData包括Preference、RDB、ORM、UDMF、分布式KVStore、分布式对象等。

在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* Preference：新增支持BigInt、Object类型数据存储；支持指定key值进行数据变更订阅 。
* RDB：新增支持BigInt类型，支持attach、detach、notContains，数据库变更通知携带数据ID，支持TS同步API。
* UDMF：系统预定义的UTD数据类型从80种扩展到120种，支持应用自定义UTD数据类型。

详细信息请参见[ArkData开发指南](../harmonyos-guides-V5/arkdata-V5.md)。

* RDB支持统计SQL执行时间。（[API参考](../harmonyos-references-V5/js-apis-data-relationalstore-V5.md#onstatistics12)）
* RDB的配置属性StoreConfig新增配置项isReadOnly，支持指定数据库为只读。（[API参考](../harmonyos-references-V5/js-apis-data-relationalstore-V5.md#storeconfig)）
* 新增一批标准化数据定义。（[API参考](../harmonyos-references-V5/js-apis-data-uniformtypedescriptor-V5.md#uniformdatatype)）
* 支持通过C API调用UDMF提供的统一数据管理和拖拽通道的能力。（[API参考](../harmonyos-references-V5/_u_d_m_f-V5.md)）
* 提供新增模块@ohos.data.sendableRelationalStore，使能关系型数据库（RDB）支持sendable能力。（[API参考](../harmonyos-references-V5/js-apis-data-sendablerelationalstore-V5.md)）
* 支持在关系型数据库（RDB）中引入支持fts（Full-Text Search，即全文搜索引擎）等功能的动态库的能力。（[API参考](../harmonyos-references-V5/js-apis-data-relationalstore-V5.md#storeconfig)）

### ArkTS（方舟编程语言）

ArkTS（方舟编程语言）提供HarmonyOS应用开发语言ArkTS相关的公共核心基础能力接口，包括并发、容器、流、文本编解码、XML、URI、Buffer等能力。

ArkTS在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* Taskpool新增支持任务组、串行队列、长时任务、取消任务、宿主通信、设置任务监听、设置任务依赖关系，新增受限worker能力。
* 新增流基础能力，包括流读、写、双工和转换。
* 增强Uri、TextDecoder、StringDecoder等模块能力。
* Taskpool、TextDecoder、buffer、uri等模块接口性能优化。

详细信息请参见[ArkTS开发指南](../harmonyos-guides-V5/arkts-V5.md)。

* 新增方舟字节码函数命名规则。（[指南](../harmonyos-guides-V5/arkts-bytecode-function-name-V5.md)）
* Taskpool提供任务监控能力，可对任务入队、任务开始执行、任务执行成功、任务执行失败等状态进行监控。（[API参考](../harmonyos-references-V5/js-apis-taskpool-V5.md#onenqueued12)）
* Taskpool的SequenceRunner支持构造全局的串行队列。（[API参考](../harmonyos-references-V5/js-apis-taskpool-V5.md#constructor12)）
* Taskpool的任务执行优先级增加IDLE，表示任务为后台任务。（[API参考](../harmonyos-references-V5/js-apis-taskpool-V5.md#priority)）
* Uint8ClampedArray支持Sendable能力。（[API参考](../harmonyos-references-V5/js-apis-arkts-collections-V5.md)）
* 支持Sendable类型的Function。（[指南](../harmonyos-guides-V5/arkts-sendable-V5.md#sendable-function)）
* JSON支持对BigInt的解析。（[API参考](../harmonyos-references-V5/js-apis-json-V5.md#bigintmode)）

### UI Design Kit

【新增Kit】UI Design Kit（UI设计套件）是华为提供的符合华为HarmonyOS Design System定义的UI界面开发套件集合，包含HarmonyOS Design System设计定义的扩展UI组件及其多样化的组件样式、丰富多样的UI界面场景下的光影效果，支撑应用实现跟随HarmonyOS Design System高端精致设计效果UI界面，达成应用界面与华为HarmonyOS多设备UI设计风格完美融合。（[指南](../harmonyos-guides-V5/ui-design-introduction-V5.md)、[API参考](../harmonyos-references-V5/ui-design-hdsdrawable-V5.md)）

## 公共

配置文件app.json5新增cloudFileSyncEnabled标签，用于标识当前应用是否启用端云文件同步能力。（[指南](../harmonyos-guides-V5/app-configuration-file-V5.md#配置文件标签)）

## NDK

* 支持使用JSVM-API的WebAssembly接口编译wasm module。（[指南](../harmonyos-guides-V5/jsvm-data-types-interfaces-V5.md#使用-jsvm-api-webassembly-接口编译-wasm-module)）
* JSVM的内存管理支持BackingStore机制，可以基于BackingStore申请的内存创建array buffer。（[指南](../harmonyos-guides-V5/jsvm-data-types-interfaces-V5.md#内存管理)）

### ArkUI（方舟UI框架）

ArkUI（方舟UI框架）是一个简洁的、高性能、支持跨设备的UI框架，提供了丰富的应用界面开发所需能力。

ArkUI包括UI组件、动画、绘制、交互事件、JS API扩展机制等。

ArkUI在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 针对三方框架场景提供组件NDK接口，涵盖组件创建、属性设置、事件注册、自定义能力、组件树构建。
* 自定义节点能力增强，提供FrameNode的自定义能力以及节点代理能力，并提供基础组件、手势、事件的Modifier能力。
* Navigation新增页面生命周期：支持onWillShow和onWillHide页面生命周期、转场动画支持打断和接续、页面内容扩展到状态栏、单例跳转能力和自定义动效能力增强。
* Video/XComponent/Canvas组件支持AI能力，支持文本和实体识别。
* Text等文本类组件支持属性字符串。
* 支持使用NativeWindowEventFilter能力拦截按键事件。
* 支持使用画中画功能。
* 新增提供智慧多窗的适配指导。

详细信息请参见[ArkUI开发指南](../harmonyos-guides-V5/arkui-V5.md)。

* 半模态页面支持自定义宽度、边框、阴影，同时生效了高度设置。（[API参考](../harmonyos-references-V5/ts-universal-attributes-sheet-transition-V5.md)）
* 半模态弹窗支持在页面内顶层显示（[API参考](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetmode12枚举说明)）。
* AlphabetIndexer支持宽度自适应。（[API参考](../harmonyos-references-V5/ts-container-alphabet-indexer-V5.md#属性)）
* RichEditor组件支持lineHeight、decoration、letter-spacing属性（[API参考](../harmonyos-references-V5/ts-basic-components-richeditor-V5.md#richeditortextstyleresult)）；RichEditor支持获取对象的布局信息，包括查询LineMetrics（指定行的信息如文本、文本样式、字体属性）和获取文本行数（[API参考](../harmonyos-references-V5/ts-basic-components-richeditor-V5.md#getlayoutmanager12)）。
* TextInput输入框下划线模式支持配置下划线颜色。（[API参考](../harmonyos-references-V5/ts-basic-components-textinput-V5.md#underlinecolor12)）
* Slider新增无滑块样式（[API参考](../harmonyos-references-V5/ts-basic-components-slider-V5.md#sliderstyle枚举说明)）；支持禁用点击拖动进度条（[API参考](../harmonyos-references-V5/ts-basic-components-slider-V5.md#sliderinteraction12枚举说明)），并且支持设置响应滑动的有效区间（[API参考](../harmonyos-references-V5/ts-basic-components-slider-V5.md#sliderange12对象说明)）。
* Toggle组件支持部分样式自定义。（[API参考](../harmonyos-references-V5/ts-basic-components-toggle-V5.md)）
* Radio支持显示自定义图标。（[API参考](../harmonyos-references-V5/ts-basic-components-radio-V5.md#radioindicatortype12枚举说明)）
* 文本类组件[Text](../harmonyos-references-V5/ts-basic-components-text-V5.md#fontfeature12)/[TextInput](../harmonyos-references-V5/ts-basic-components-textinput-V5.md#fontfeature12)/[TextArea](../harmonyos-references-V5/ts-basic-components-textarea-V5.md#fontfeature12)/[Search](../harmonyos-references-V5/ts-basic-components-search-V5.md#fontfeature12)、[RichEditor](../harmonyos-references-V5/ts-basic-components-richeditor-V5.md#richeditortextstyle)支持font feature属性（[API参考](../harmonyos-references-V5/ts-basic-components-richeditor-V5.md#richeditortextstyleresult)）。
* 安全区域新增支持将屏幕挖孔区域定义为非安全区域并进行自动避让。（[API参考](../harmonyos-references-V5/ts-universal-attributes-expand-safe-area-V5.md)）
* Video组件提供onStop回调。（[API参考](../harmonyos-references-V5/ts-media-components-video-V5.md#onstop12)）
* 支持设置应用自定义主题配色风格及动态切换。（[API参考](../harmonyos-references-V5/js-apis-arkui-theme-V5.md)）
* 支持设置页面局部自定义主题配色风格。（[API参考](../harmonyos-references-V5/ts-container-with-theme-V5.md)）
* 圆点导航点优化超长显示效果。（[API参考](../harmonyos-references-V5/ts-container-swiper-V5.md#dotindicator10)）
* 新增手势增强拦截。（[API参考](../harmonyos-references-V5/ts-gesture-blocking-enhancement-V5.md)）
* 支持在动画的下一帧进行渲染时执行回调。（[API参考](../harmonyos-references-V5/js-apis-arkui-uicontext-V5.md#postframecallback12)）
* PatternLock设置圆点外层阴影圆弧半径大小颜色以及提供波浪效果的开关属性。（[API参考](../harmonyos-references-V5/ts-basic-components-patternlock-V5.md#circlestyleoptions12对象说明)）
* Text组件支持获取指定行的信息如文本、文本样式、字体属性。（[API参考](../harmonyos-references-V5/ts-basic-components-text-V5.md#getlayoutmanager12)）
* Swiper组件nextMargin和prevMargin新增参数，支持非Loop场景下首页不显示PrevMargin（[API参考](../harmonyos-references-V5/ts-container-swiper-V5.md#prevmargin10)），尾页不显示NextMargin（[API参考](../harmonyos-references-V5/ts-container-swiper-V5.md#nextmargin10)）。
* Swiper组件提供设置动态帧率的接口。（[API参考](../harmonyos-references-V5/js-apis-arkui-uicontext-V5.md#swiperdynamicsyncscene12)）
* Navigation支持交互转场。（[API参考](../harmonyos-references-V5/ts-basic-components-navigation-V5.md#navigationanimatedtransition11)）
* Navigation支持页面级状态栏的样式更新。（[Navigation API参考](../harmonyos-references-V5/ts-basic-components-navigation-V5.md#systembarstyle12)、[NavDestination API参考](../harmonyos-references-V5/ts-basic-components-navdestination-V5.md#systembarstyle12)）
* Navigation支持单例跳转。（[API参考](../harmonyos-references-V5/ts-basic-components-navigation-V5.md#pushpath12)）
* Image组件提供C API支持统计Gif图播放次数（[API参考](../harmonyos-references-V5/drawable__descriptor_8h-V5.md#函数)）、支持滤镜属性（NODE\_IMAGE\_COLOR\_FILTER）（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）。
* 通用属性border支持配置dashGap和dashWidth。（[API参考](../harmonyos-references-V5/ts-universal-attributes-border-V5.md#borderoptions对象说明)）
* WaterFlow组件支持快速切换列数。（[API参考](../harmonyos-references/ts-container-waterflow.md#waterflowlayoutmode12枚举说明)）
* [TextInput](../harmonyos-references-V5/ts-basic-components-textinput-V5.md#onwillinsert12)/[TextArea](../harmonyos-references-V5/ts-basic-components-textarea-V5.md#onwillinsert12)/[Search](../harmonyos-references-V5/ts-basic-components-search-V5.md#oneditchange12)支持监听输入法框架的生命周期的回调。
* TextArea支持场景化自动填充能力。（[API参考](../harmonyos-references-V5/ts-basic-components-textarea-V5.md#enableautofill12)）
* Refresh组件支持设置下拉跟手系数。（[API参考](../harmonyos-references-V5/ts-container-refresh-V5.md#pulldownratio12)）
* Animator支持delay配置项为负数。（[API参考](../harmonyos-references-V5/js-apis-animator-V5.md#animatoroptions)）
* Tabs组件支持设置cachedCount进行页面预加载。（[API参考](../harmonyos-references-V5/ts-container-tabs-V5.md#preloaditems12)）
* C API的NODE\_BORDER\_RADIUS\_PERCENT属性支持百分比设置。（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）
* RenderNode支持设置nodeGroup。（[API参考](../harmonyos-references-V5/js-apis-arkui-rendernode-V5.md#marknodegroup12)）
* RelativeContainer组件支持镜像能力，同时提供了使用镜像能力的指南。（[指南](../harmonyos-guides-V5/arkts-mirroring-display-V5.md)）
* FrameNode支持查询Navigation/Router页面信息。（[API参考](../harmonyos-references-V5/js-apis-arkui-uicontext-V5.md#pageinfo12)）
* 支持子窗口关闭事件通知。（[API参考](../harmonyos-references-V5/js-apis-window-V5.md#onsubwindowclose12)）
* 支持三方应用使用截屏功能。
* 画中画的控制面板提供可选控件，开发者可自定义选择是否显示可选控件。（[API参考](../harmonyos-references-V5/js-apis-pipwindow-V5.md#pipcontrolgroup12)）
* 普通文本控件支持文本菜单自定义。（[API参考](../harmonyos-references-V5/ts-basic-components-text-V5.md#editmenuoptions12)）
* 富文本控件支持文本菜单自定义。（[API参考](../harmonyos-references-V5/ts-basic-components-richeditor-V5.md#editmenuoptions12)）
* 组件内转场（transition）提供动画结束回调的监听。（[API参考](../harmonyos-references-V5/ts-transition-animation-component-V5.md#transitionfinishcallback12)）
* [TextInput](../harmonyos-references-V5/ts-basic-components-textinput-V5.md#inputtype枚举说明)/[TextArea](../harmonyos-references-V5/ts-basic-components-textarea-V5.md#textareatype11枚举说明)/[Search](../harmonyos-references-V5/ts-basic-components-search-V5.md#searchtype11枚举说明)支持URL格式的输入模式。
* 滚动控制器ScrollToIndex支持设置额外偏移量。（[API参考](../harmonyos-references-V5/ts-container-scroll-V5.md#scrolltoindex)）
* 属性字符串支持存储自定义扩展信息。（[API参考](../harmonyos-references-V5/ts-universal-styled-string-V5.md#userdataspan)）
* 支持创建并弹出以bindSheetContent作为内容的半模态页面。（[API参考](../harmonyos-references-V5/js-apis-arkui-uicontext-V5.md#openbindsheet12)）
* Image组件支持更多图片内容的对齐方式。（[API参考](../harmonyos-references-V5/ts-appendix-enums-V5.md#imagefit)）
* RenderNode支持设置裁剪形状。（[API参考](../harmonyos-references-V5/js-apis-arkui-rendernode-V5.md#shapeclip12)）
* 分组瀑布流支持移动窗口布局模式。（[API参考](../harmonyos-references/ts-container-waterflow.md#waterflowlayoutmode12枚举说明)）
* 组件截图接口ComponentSnapshot支持自定义参数SnapshotOptions。（[API参考](../harmonyos-references-V5/js-apis-arkui-uicontext-V5.md#componentsnapshot12)）
* Tabs支持设置边缘回弹效果。（[API参考](../harmonyos-references-V5/ts-container-tabs-V5.md#edgeeffect12)）
* Navigation支持一种新的创建NavDestination示例的模式——NEW\_INSTANCE。与STANDARD模式相比，该方法不会复用栈中同名实例。（[API参考](../harmonyos-references-V5/ts-basic-components-navigation-V5.md#launchmode12枚举说明)）
* C API通用属性支持设置、重置和获取Refresh/Swiper/List相关接口，包括List分割线样式（NODE\_LIST\_DIVIDER）、Swiper组件前边距（NODE\_SWIPER\_PREV\_MARGIN）/后边距（NODE\_SWIPER\_NEXT\_MARGIN）、Refresh组件下拉偏移量等（NODE\_REFRESH\_OFFSET）。（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）
* TextInput/TextArea组件C API支持设置和重置输入文本（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）。包括：
  + NODE\_TEXT\_INPUT\_ON\_WILL\_INSERT
  + NODE\_TEXT\_INPUT\_ON\_DID\_INSERT
  + NODE\_TEXT\_INPUT\_ON\_WILL\_DELETE
  + NODE\_TEXT\_INPUT\_ON\_DID\_DELETE
  + NODE\_TEXT\_AREA\_ON\_WILL\_INSERT
  + NODE\_TEXT\_AREA\_ON\_DID\_INSERT
  + NODE\_TEXT\_AREA\_ON\_WILL\_DELETE
  + NODE\_TEXT\_AREA\_ON\_DID\_DELETE
* 组件C API通用能力增强。包括：

  支持通过[NODE\_CLIP\_SHAPE](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)设置组件四边圆角、[NODE\_EXPAND\_SAFE\_AREA](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)扩展组件安全区域。

  通用onTouch事件支持[阻止事件冒泡](../harmonyos-references-V5/ui__input__event_8h-V5.md)。通用手势事件提供[手势识别器句柄](../harmonyos-references-V5/native__gesture_8h-V5.md#汇总)类型对象，返回触发该事件的组件对象。

  通过[OH\_ArkUI\_GetContextByNode](../harmonyos-references/capi-native-node-h.md#oh_arkui_getcontextbynode)获取当前节前所在页面的UI上下文实例对象指针。
* 通过C API提供定义帧动画对象的能力，可获取、销毁、设置关键帧动画相关参数。（[API参考](../harmonyos-references-V5/native__animate_8h-V5.md)）
* XComponent支持通过C API获取触摸点相对于屏幕或应用窗口的坐标。（[API参考](../harmonyos-references-V5/_o_h___native_x_component-V5.md#oh_nativexcomponent_gettouchpointwindowx)）
* FrameNode支持数据懒加载能力。（[API参考](../harmonyos-references-V5/js-apis-arkui-framenode-V5.md#nodeadapter12)）
* FrameNode支持创建具体类型的FrameNode，类型覆盖中高频组件。（[API参考](../harmonyos-references-V5/js-apis-arkui-framenode-V5.md#typenode12)）
* 提供通用拖拽能力的C API。（[API参考](../harmonyos-references-V5/drag__and__drop_8h-V5.md)）
* Grid组件支持选取一行中最高的GridItem的高度定义为行高。（[API参考](../harmonyos-references-V5/ts-container-grid-V5.md#alignitems12)）
* Tabs组件支持通过无感监听上报TabContent页面的切换事件。（[API参考](../harmonyos-references-V5/js-apis-arkui-observer-V5.md#observerontabcontentupdate12)）
* 屏幕属性新增接口用于获取折叠设备的显示模式以及对应的物理屏幕分辨率信息对象（[API参考](../harmonyos-references-V5/js-apis-display-V5.md#displaygetalldisplayphysicalresolution12)）；新增接口用于获取PC/2in1设备屏幕的可用区域（[API参考](../harmonyos-references-V5/js-apis-display-V5.md#getavailablearea12)）。
* Image组件新增ImageContent传参类型，允许当设置的图片源为空时，Image组件显示为空。（[API参考](../harmonyos-references-V5/ts-basic-components-image-V5.md#image12)）
* 支持获取状态管理框架代理前的原始对象。（[指南](../harmonyos-guides-V5/arkts-new-gettarget-V5.md)）
* 支持通过C API获取组件标识ID（NODE\_UNIQUE\_ID）。（[API参考](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)）
* Refresh组件的RefreshOption对象支持ComponentContent类型的对象refreshingContent，用于自定义刷新区域显示的内容。（[API参考](../harmonyos-references-V5/ts-container-refresh-V5.md#refreshoptions对象说明)）
* 支持通过C API自定义段落组件的测量信息（[ArkUI\_CustomSpanMeasureInfo](../harmonyos-references-V5/_ark_u_i___native_module-V5.md#arkui_customspanmeasureinfo)）、度量指标（[ArkUI\_CustomSpanMetrics](../harmonyos-references-V5/_ark_u_i___native_module-V5.md#arkui_customspanmetrics)）、绘制信息（[ArkUI\_CustomSpanDrawInfo](../harmonyos-references-V5/_ark_u_i___native_module-V5.md#arkui_customspandrawinfo)）。
* Navigation组件支持将页面栈内指定navDestinationId的NavDestination页面删除。（[API参考](../harmonyos-references-V5/ts-basic-components-navigation-V5.md#removebynavdestinationid12)）
* RichEditor支持配置获焦时是否拉起软键盘。（[API参考](../harmonyos-references-V5/ts-basic-components-richeditor-V5.md#enablekeyboardonfocus12)）
* 新增API支持测量字符宽度。（[API参考](../harmonyos-references-V5/js-apis-graphics-drawing-V5.md#measuresinglecharacter12)）
* 点击事件和手势支持设置触控阈值distanceThreshold。（[API参考-点击事件](../harmonyos-references-V5/ts-universal-events-click-V5.md#onclick12)、[API参考-TapGesture](../harmonyos-references-V5/ts-basic-gestures-tapgesture-V5.md#tapgestureparameters12对象说明)）
* Text组件可设置文本是否将行间距平分至行的顶部与底部。（[API参考](../harmonyos-references-V5/ts-basic-components-text-V5.md#halfleading12)）
* 获取已加载的组件的截图新增同步接口。（[API参考](../harmonyos-references-V5/js-apis-arkui-componentsnapshot-V5.md#componentsnapshotgetsync12)）
* 新增空闲时间的生命周期回调用以支持应用闲时处理耗时任务。（[API参考](../harmonyos-references-V5/js-apis-arkui-uicontext-V5.md#onidle12)）
* 支持通过typeNode创建画中画。（[API参考](../harmonyos-references-V5/js-apis-pipwindow-V5.md#pipwindowcreate12)）
* 支持按照options中的配置参数创建XComponent类型的FrameNode节点。（[API参考](../harmonyos-references-V5/js-apis-arkui-framenode-V5.md#createnodexcomponent12-1)）
* List组件支持设置在显示区域以外删除数据后保持显示区域内容不变的能力。（[API参考](../harmonyos-references-V5/ts-container-list-V5.md#maintainvisiblecontentposition12)）
* 提供查询窗口状态和查询窗口是否获焦的API。（[API参考-getwindowstatus](../harmonyos-references-V5/js-apis-window-V5.md#getwindowstatus12)、[API参考-isFocused](../harmonyos-references-V5/js-apis-window-V5.md#isfocused12)）
* 新增C API用于将普通不可观察数据变为可观察数据。（[API参考](../harmonyos-references-V5/js-apis-statemanagement-V5.md#makeobserved)、[指南](../harmonyos-guides-V5/arkts-new-makeobserved-V5.md)）
* Column组件支持设置其子组件在主轴（即竖直方向）上反转排列。（[API参考](../harmonyos-references-V5/ts-container-column-V5.md#reverse12)）
* 新增支持通过C API管理屏幕的能力。（[API参考](../harmonyos-references-V5/_o_h___display_manager-V5.md)）
* CustomDialog组件和弹窗模块（ohos.promptAction）支持通过keyboardAvoidMode属性设置弹窗是否在拉起软键盘时进行自动避让。（[API参考-CustomDialog](../harmonyos-references-V5/ts-methods-custom-dialog-box-V5.md#customdialogcontrolleroptions对象说明)、[API参考-promptAction](../harmonyos-references-V5/js-apis-promptaction-V5.md#basedialogoptions11)）
* TextArea组件可设置点击回车键后软键盘不收起。（[API参考](../harmonyos-references-V5/ts-basic-components-richeditor-V5.md#enterkeytype12)）

### ArkWeb（方舟Web）

ArkWeb（方舟Web）提供了在应用中使用Web页面的能力，支持应用集成Web页面、小程序、浏览器网页浏览等场景的混合开发。

ArkWeb在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 网页加载与页面导航：新增支持打开UniversalLink链接、应用托管网络、应用级自定义DNS。
* 网页渲染与显示：新增支持object/embed标签的同层渲染与事件传递、长网页渲染模式、网页长截图、扩展安全区域与H5避让区查询能力、预览PDF（内置PDFView扩展）。
* UX一致性增强：增强支持文本选择智能选词、图片长按识文、列表滑动曲线的能力。
* 网页媒体：新增支持显示HEIF图片、网页视频托管、网页音视频与摄像头控制。
* 网页安全隐私：新增广告过滤能力支持定义自定义拦截规则，智能防跟踪及限制三方Cookie的访问，网页高级安全模式。
* W3C兼容性增强：支持设置meta标签的viewport属性，支持鼠标悬停提示tooltip、datalist元素，支持自定义光标样式等。
* 性能增强：新增ArkWeb组件动态创建与上下树、JavaScript接口性能提升、V8引擎性能优化。
* DFX增强：新增支持独立Web GPU进程提升应用稳定性，应用可使能独立Web渲染进程，提升应用安全与稳定性，无障碍常用功能，增强网页性能度量接口（LCP/FMP），生成crashpad崩溃信息。

详细信息请参见[ArkWeb开发指南](../harmonyos-guides-V5/arkweb-V5.md)。

* 支持广告过滤的能力，并支持设置过滤规则。（[API参考](../harmonyos-references-V5/js-apis-webview-V5.md#enableadsblock12)）
* 支持配置Web页面全量绘制模式，支持获取绘制结果。（[API参考](../harmonyos-references-V5/js-apis-webview-V5.md#enablewholewebpagedrawing12)）
* 支持设置ArkWeb渲染子进程的模式。（[API参考](../harmonyos-references-V5/js-apis-webview-V5.md#setrenderprocessmode12)）
* 将本地离线资源注入到内存缓存。（[API参考](../harmonyos-references-V5/js-apis-webview-V5.md#injectofflineresources12)）
* Web组件的可编辑元素（如input标签）支持拉起输入法软键盘的回调，允许使用回调接口拦截输入法软键盘，并配置为应用自定义的软键盘。（[API参考](../harmonyos-references-V5/ts-basic-components-web-V5.md#oninterceptkeyboardattach12)）
* Web组件的网络拦截功能支持获取被拦截请求的ResourceType。（[指南](../harmonyos-guides-V5/web-scheme-handler-V5.md)）
* 支持设置允许File协议跨域访问的白名单目录。（[API参考](../harmonyos-references-V5/js-apis-webview-V5.md#setpathallowinguniversalaccess12)）
* Web组件支持自定义软件键盘避让模式。（[API参考](../harmonyos-references-V5/ts-basic-components-web-V5.md#keyboardavoidmode12)）
* 支持通过W3C标准协议接口对接运动和方向相关的传感器。（[指南](../harmonyos-guides-V5/web-sensor-V5.md)）
* 新增ScrollType类型定义，用于增强嵌套滚动能力。（[API参考](../harmonyos-references-V5/js-apis-webview-V5.md#scrolltype12)）
* 新增C API的Post Message能力。（[API参考](../harmonyos-references/capi-web-arkweb-webmessageportapi.md)）
* 新增API用于支持自定义系统菜单。（[API参考](../harmonyos-references-V5/ts-basic-components-web-V5.md#editmenuoptions12)）
* 新增API用于支持同层渲染可见性发生变化时的回调。（[API参考](../harmonyos-references-V5/ts-basic-components-web-V5.md#onnativeembedvisibilitychange12)）
* 新增API用于在滚动事件以外设置将页面滚动指定的偏移量并返回执行结果。（[API参考](../harmonyos-references-V5/js-apis-webview-V5.md#scrollbywithresult12)）

### Background Tasks Kit（后台任务开发服务）

Background Tasks Kit（后台任务开发服务）提供后台任务开发的能力，包括短时任务、长时任务、延迟任务、代理提醒，开发者可以选择合适的后台任务，以满足应用退至后台后继续运行的需求。

Background Tasks Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

长时任务：

* 申请长时任务返回通知ID
* 提供下载类长时任务

代理提醒：

* 新增接口 getAllValidReminders 支持查询 reminderId；
* 日历类型提醒支持设置结束时间；
* 重复的日历类型提醒支持添加 excludeDate，在此范围内的不提醒；
* wantAgent 增加 uri 和 parameters 参数。

详细信息请参见[Background Tasks Kit开发指南](../harmonyos-guides-V5/background-task-kit-V5.md)。

### Core File Kit（文件基础服务）

Core File Kit（文件基础服务）提供访问和管理应用文件和用户文件的能力。

Core File Kit涵盖了应用文件管理、应用存储空间管理、用户文件访问与管理、文件分享、应用数据备份恢复、跨设备文件访问与拷贝等能力。

Core File Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 基础文件API高阶能力。
* 用户文件访问框架。
* 文件分享。
* 备份恢复。
* 跨设备文件访问与拷贝。

详细信息请参见[Core File Kit开发指南](../harmonyos-guides-V5/core-file-kit-V5.md)。

### Form Kit（卡片开发服务）

Form Kit（卡片开发服务）提供一种界面展示形式，可以将应用的重要信息或操作前置到服务卡片，以达到服务直达、减少跳转层级的体验效果。卡片常用于嵌入到其他应用（当前被嵌入方即卡片使用方只支持系统应用，例如桌面）中作为其界面显示的一部分，并支持拉起页面、发送消息等基础的交互能力。Form Kit涵盖了原有服务卡片部分的能力。

Form Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 支持6\*4 大卡片尺寸。
* 支持卡片提供方感知应用权限变更通知。

详细信息请参见[Form Kit开发指南](../harmonyos-guides-V5/form-kit-V5.md)。

### IME Kit（输入法开发服务）

IME Kit（输入法开发服务）负责建立和管理编辑框所在应用与输入法应用之间的通信通道，确保两者可以共同协作提供文本输入功能，也为系统应用提供管理输入法应用的能力。

IME Kit涵盖了原有输入法框架的相关能力，并在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 面向输入法应用提供创建软键盘窗口、插入/删除字符、选中文本、文本预上屏、监听物理键盘按键事件和文本框状态变化等功能。
* 面向主应用自绘编辑框控件提供相关API，包括绑定输入法，配合输入法应用完成输入、删除、选中、光标移动等文本框操作的接口实现。
* 提供系统应用管理输入法应用的能力，实现对输入法应用的控制，包括显示/隐藏输入法软键盘、切换输入法、获取所有输入法列表。
* 提供了输入法完整体验模式确保输入法进程沙箱隔离，输入法应用需要同时支持基础模式和完整体验模式的切换。

详细信息请参见[IME Kit开发指南](../harmonyos-guides-V5/ime-kit-V5.md)。

新增支持通过C API调用输入法的相关能力。（[API参考](../harmonyos-references-V5/_input_method-V5.md)）

### IPC Kit（进程间通信服务）

IPC Kit（进程间通信服务）提供进程间通信能力，包括设备内的进程间通信（IPC）和设备间的进程间通信（RPC），用来实现数据交互。

IPC Kit涵盖了原有IPC与RPC通信部分的能力，包括传递基本类型的数据、传递IPC对象和自定义序列化对象、大数据量的数据以共享内存的形式传递、序列化读写数据等。

IPC Kit在HarmonyOS NEXT阶段对上述能力的接口进行了重新设计，使功能得以增强。

详细信息请参见[IPC Kit开发指南](../harmonyos-guides-V5/ipc-kit-V5.md)。

新增一系列IPC能力的C API。（[API参考](../harmonyos-references-V5/ipc-c-V5.md)）

提供基于C API的IPC通信开发指导。（[指南](../harmonyos-guides-V5/ipc-capi-development-guideline-V5.md)）

### Localization Kit（本地化开发服务）

Localization Kit（本地化开发服务）提供国际化和本地化能力，可使应用符合当地用户的使用习惯。

国际化是系统提供的一套能力集，支持多语言输入输出、多语言文字处理、区域文化习惯特性、时区和夏令时等，满足应用多语言多文化的设计需求。本地化是为应用开发者提供的一套能力集，支持包括配置多语言翻译资源、资源加载、敏感禁忌检查和本地化测试能力。

Localization Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 增强了国际化和本地化的能力，提供更多国际化和本地化应用的功能和场景。
* 新增本地化测试能力。

详细信息请参见[Localization Kit开发指南](../harmonyos-guides-V5/localization-kit-V5.md)。

## 系统-安全

### Asset Store Kit（关键资产存储服务）

Asset Store Kit（关键资产存储服务）提供用户短敏感数据的安全存储及管理能力。其中，短敏感数据可以是密码类（账号/密码）、Token类（应用凭据）、其他关键明文（如银行卡号）等长度较短的用户敏感数据。

Asset Store Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Asset Store Kit开发指南](../harmonyos-guides-V5/asset-store-kit-V5.md)。

### Crypto Architecture Kit（加解密算法框架服务）

Crypto Architecture Kit（加解密算法框架服务）提供了加解密、签名验签等算法能力。

Crypto Architecture Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 提供国密SM2、SM3、SM4算法。
* 提供基于EC曲线名的密钥生成能力。
* 提供DSA、ED25519签名验签算法，ECDSA算法支持brainpool曲线。
* 提供X25519、DH密钥协商算法。
* 提供PBKDF2、HKDF密钥派生算法。
* 算法均提供异步和同步接口。

详细信息请参见[Crypto Architecture Kit开发指南](../harmonyos-guides-V5/crypto-architecture-kit-V5.md)。

算法库适配层提供[签名验签](../harmonyos-references-V5/js-apis-cryptoframework-V5.md#signsync12)、[密钥协商](../harmonyos-references-V5/js-apis-cryptoframework-V5.md#generatesecretsync12)的同步接口，指南同步提供相关示例。（[指南-签名验签](../harmonyos-guides-V5/crypto-sign-sig-verify-overview-V5.md)、[指南-密钥协商](../harmonyos-guides-V5/crypto-key-agreement-overview-V5.md)）

密钥生成和转换、加解密、签名验签、消息摘要等能力新增支持通过C API调用，同步提供开发指南。（[指南](../harmonyos-guides-V5/crypto-architecture-kit-intro-V5.md)）

### Data Loss Prevention Kit（数据防泄漏服务）

Data Loss Prevention Kit（数据防泄漏服务）提供系统级的数据防泄漏解决方案，提供文档权限管理、加密存储、授权访问等能力，数据所有者可以基于账号认证对机密文档进行权限配置，允许拥有只读、编辑、拥有者权限，随后机密文件会通过密文存储，在支持DLP机制的设备上可以通过端云协调进行认证授权，获取对数据的访问和修改的能力。

Data Loss Prevention Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Data Loss Prevention Kit开发指南](../harmonyos-guides-V5/data-protection-kit-V5.md)。

### Device Certification Kit（设备证书服务）

Device Certificate Kit（设备证书服务）提供了系统级的证书管理、证书解析和校验、设备证明的能力。

Device Certificate Kit涵盖了证书安装、查询、使用和删除能力，X509证书解析、CRL解析和证书链校验能力。

Device Certificate Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 设备真实性证明。
* 证书集合及证书吊销列表集合。
* 证书链对象的创建和校验。

详细信息请参见[Device Certificate Kit开发指南](../harmonyos-guides-V5/device-certificate-kit-V5.md)。

支持获取X.509证书主体名称，名称支持中文。（[API参考](../harmonyos-references-V5/js-apis-cert-V5.md#getsubjectname)）

### Device Security Kit（设备安全服务）

Device Security Kit（设备安全服务）提供应用设备状态检测（DeviceVerify）、安全检测（SafetyDetect）和可信应用服务（TrustedAppService），可以保护应用程序免受安全威胁和保证应用的数据安全。

Device Security Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Device Security Kit开发指南](../harmonyos-guides-V5/device-security-kit-guide-V5.md)。

支持涉诈剧本检测功能。金融支付类应用在用户转账、支付前，通过调用Device Security Kit，检测用户是否受到欺诈威胁，应用可根据检测结果，对用户的支付、转账进行有效提示或拦截。（[指南](../harmonyos-guides-V5/devicesecurity-fraudriskdetection-V5.md)）

新增安全审计API，支持应用获取安全审计数据，审计数据包括窗口截屏事件、USB插拔事件、剪切板复制粘贴事件等。（[指南](../harmonyos-guides-V5/devicesecurity-securityaudit-V5.md)）

### Enterprise Data Guard Kit（企业数据保护服务）

Enterprise Data Guard Kit（企业数据保护服务）为企业安全管控类MDM应用提供统一企业关键信息资产（KIA）文件的识别和外发管控能力，支撑企业构建完整的数据防泄漏解决方案，实现企业数据资产可知、可控、可追溯。

Enterprise Data Guard Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Enterprise Data Guard Kit开发指南](../harmonyos-guides-V5/data-guard-kit-guide-V5.md)。

### Online Authentication Kit（在线认证服务）

Online Authentication Kit（在线认证服务）遵循FIDO（Fast Identity Online）和IIFAA（ 互联网可信认证联盟）标准规范，提供免密身份认证的移动端能力。用户应用接入FIDO或IIFAA服务器后，可以使用相应的移动端能力，用生物特征（指纹/3D人脸）代替密码，实现免密登录、免密支付等业务场景。

Online Authentication Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Online Authentication Kit开发指南](../harmonyos-guides-V5/online-authentication-kit-guide-V5.md)。

支持SOTER免密身份认证。（[指南](../harmonyos-guides-V5/onlineauthentication-soter-V5.md)）

### Universal Keystore Kit（密钥管理服务）

Universal Keystore Kit（密钥管理服务）提供密钥的全生命周期管理能力，包括密钥生成、销毁、导入、派生、使用（如加密/解密、签名/验签）、访问控制及密钥合法性证明等功能。

Universal Keystore Kit为HarmonyOS NEXT全新提供的能力。详细信息请参见[Universal Keystore Kit开发指南](../harmonyos-guides-V5/huks-kit-V5.md)。

### User Authentication Kit（用户认证服务）

User Authentication Kit（用户认证服务）提供了基于锁屏口令、人脸和指纹在设备本地认证用户身份的能力。

User Authentication Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 提供用户凭据注册状态的查询功能。
* 提供可供集成的嵌入式身份认证控件。
* 支持在锁屏解锁5分钟内复用锁屏认证结果。

详细信息请参见[User Authentication Kit开发指南](../harmonyos-guides-V5/user-authentication-kit-V5.md)。

## 系统-网络

## Network Boost Kit

【新增Kit】NetworkBoost Kit（网络加速服务）提供无线通信传输能力封装以及网络QoE能力开放，可以为开发者提供定制化的通信解决方案，包括通信资源调度、QoE信息实时反馈，应用体验质量反馈等功能，为应用带来大带宽、低时延、高可靠的网络体验。（[指南](../harmonyos-guides-V5/networkboost-introduction-V5.md)、[API参考](../harmonyos-references-V5/networkboost-netquality-V5.md)）

新增网络场景识别订阅功能。（[指南](../harmonyos-guides-V5/networkboost-scenecallback-V5.md)）

* 新增支持连接迁移状态订阅和去订阅功能。（[指南](../harmonyos-guides-V5/networkboost-nethandovercallback-V5.md)）
* 支持连接迁移模式设置。（[指南](../harmonyos-guides-V5/networkboost-reporthandovermode-V5.md)）

### Connectivity Kit（短距通信服务）

Connectivity Kit（短距通信服务）提供通信服务开放能力，涵盖了WLAN、蓝牙、NFC等能力。

Connectivity Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 提供WLAN管理&状态查询等相关能力。
* 提供蓝牙设备管理、状态查询、BR&BLE数据传输等能力。
* 提供NFC管理、TAG读写、卡模拟等相关能力。

详细信息请参见[Connectivity Kit开发指南](../harmonyos-guides-V5/connectivity-kit-V5.md)。

### Distributed Service Kit（分布式管理服务）

Distributed Service Kit（分布式管理服务）提供了分布式设备管理、分布式硬件管理、分布式键鼠穿越等能力。

分布式管理服务开放能力包括：

* 分布式设备管理：进行周围设备的发现、认证、信息查询、状态监听等，该能力是分布式业务的入口功能，只有完成认证后的设备之间才可以进行分布式业务。
* 分布式硬件管理：提供控制分布式硬件的能力，包括暂停、恢复和停止被控端分布式硬件业务。
* 键鼠穿越模块：提供两台或多台设备组网协同后键鼠共享能力，实现键鼠输入设备的跨设备协同操作。

Distributed Service Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Distributed Service Kit开发指南](../harmonyos-guides-V5/distributed-service-kit-V5.md)。

### Network Kit（网络服务）

Network Kit（网络服务）提供了网络管理和网络通信能力。

Network Kit涵盖了网络状态、代理、流量统计、VPN等网络管理能力，也涵盖了HTTP、WebScoket、Socket、DNS等与网络服务设备通信的能力。

Network Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* HTTP协议栈支持自动读取与使用系统、用户安装的证书，支持SSL pinning。
* WebSocket支持设置Header、代理等参数，同时降低了WebSocket的传输功耗。
* 包括HTTP协议栈、DNS解析在内的全链路性能优化。

详细信息请参见[Network Kit开发指南](../harmonyos-guides-V5/network-kit-V5.md)。

支持接收经过brotli算法压缩的HTTP响应，不涉及新增接口，相关说明可参见[@ohos.net.http (数据请求)](../harmonyos-references-V5/js-apis-http-V5.md)。

新增支持通过C API调用网络管理的能力。（[API参考-NetStack](../harmonyos-references-V5/netstack-V5.md)、[API参考-NetConnection](../harmonyos-references-V5/_net_connection-V5.md)）

### Remote Communication Kit（远场通信服务）

Remote Communication Kit（远场通信服务）是华为提供的HTTP发起数据请求的NAPI封装。应用通过Remote Communication Kit可便捷快速地向服务器发起数据请求。

Remote Communication Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Remote Communication Kit开发指南](../harmonyos-guides-V5/remote-communication-kit-guide-V5.md)。

* 支持证书锁定。（[指南](../harmonyos-guides-V5/remote-communication-validationlock-V5.md)）
* 支持响应校验。（[指南](../harmonyos-guides-V5/remote-communication-responsecheck-V5.md)）
* 支持设置读写超时。（[指南](../harmonyos-guides-V5/remote-communication-readtimeout-V5.md)）
* 支持请求暂停和恢复。（[指南](../harmonyos-guides-V5/remote-communication-pause-resume-V5.md)）
* 支持同步读写流。（[指南](../harmonyos-guides-V5/remote-communication-asyncreadwrite-V5.md)）

### Service Collaboration Kit（协同服务）

Service Collaboration Kit（协同服务）提供了同账号下多端设备协同的能力。用户通过此能力实现跨设备交互，可以使用其他设备的相机、扫描和图库功能。

Service Collaboration Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Service Collaboration Kit开发指南](../harmonyos-guides-V5/service-collaboration-kit-guide-V5.md)。

跨设备互通能力新增C API。（[指南](../harmonyos-guides-V5/servicecollaboration-servicendk-description-V5.md)、[API参考](../harmonyos-references-V5/servicecollaboration-capi-model-V5.md)）

支持在跨设备互通场景下，自定义接收图片的最大张数。（[API参考](../harmonyos-references-V5/servicecollaboration-collaborationservice-V5.md#section149271552154711)）

### Telephony Kit（蜂窝通信服务）

Telephony Kit（蜂窝通信服务）提供了SIM卡、搜网、移动数据、短彩信和通话能力。

Telephony Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 支持广电SIM卡、支持电信和虚拟卡的APN适配、副卡通话可上网能力。
* 支持基于运营商蜂窝网络的视频通话、支持通话拦截。
* 支持小区广播、彩信收发。

详细信息请参见[Telephony Kit开发指南](../harmonyos-guides-V5/telephony-kit-V5.md)。

## 系统-基本功能

### Basic Services Kit（基础服务）

Basic Services Kit（基础服务）作为基础服务套件，为应用开发者提供常用的基础能力。比如常用的剪贴板读写、文件上传下载、文件压缩、文件打印、进程间/线程间通信、设备管理、应用账号管理等能力都由本Kit提供。

Basic Services Kit在涵盖上述能力的基础上，在HarmonyOS NEXT阶段对上述能力进行了增强。

详细信息请参见[Basic Services Kit开发指南](../harmonyos-guides-V5/basic-services-kit-V5.md)。

Emitter支持传递sendable类型的对象，详见[API参考](../harmonyos-references-V5/js-apis-emitter-V5.md)的示例用法。

新增支持通过C API获取和使用时间时区的能力。（[API参考](../harmonyos-references-V5/_time_service-V5.md)）

新增支持通过C API订阅/退订公共事件的能力。（[API参考](../harmonyos-references-V5/capi-common-event-V5.md)）

### Function Flow Runtime Kit（任务并发调度服务）

Function Flow Runtime Kit提供一种基于任务和数据驱动的并发编程模型，开发者可专注于应用功能开发，由FFRT在运行时根据任务依赖状态和可用执行资源自动并发调度和执行任务。

Function Flow Runtime Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Function Flow Runtime Kit开发指南](../harmonyos-guides-V5/ffrt-kit-V5.md)。

### Input Kit（多模输入服务）

Input Kit（多模输入Kit）为多种输入设备提供服务，如触控板、触摸屏、鼠标、键盘等。通过对这些输入设备上报驱动事件的归一化处理，确保不同输入设备与用户交互体验统一和流畅。除基础的输入事件服务，多模子系统还支持获取设备列表，以及改变鼠标光标样式等。

Input Kit在原有支持输入事件的基础上，在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 将常用的一些输入动作定义为一组标准化事件，并将不同输入设备的输入事件映射到标准化事件上。
* 支持输入设备管理，监听输入设备连接和断开状态，查询输入设备相关信息。
* 支持鼠标光标样式自定义。

详细信息请参见[Input Kit开发指南](../harmonyos-guides-V5/input-kit-V5.md)。

### MDM Kit（企业设备管理服务）

移动设备管理（Mobile Device Management）是一种企业级的IT应用解决方案，用于管理并保护公司设备上的数据和应用程序。

MDM Kit（企业设备管理服务）可以通过集中管理、远程配置和监控来保障设备和数据的安全性和稳定性。它广泛应用于企业和政府机构，以确保员工和客户使用的设备和数受到保护，实现企业高效管理、安全使用设备。

MDM Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[MDM Kit开发指南](../harmonyos-guides-V5/mdm-kit-V5.md)。

### Status Bar Extension Kit（状态栏开放服务）

Status Bar Extension Kit（状态栏开放服务）提供了在状态栏中添加应用图标、管理图标等一系列方法，为应用提供可以在状态栏与用户进行交互的功能。

Status Bar Extension Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Status Bar Extension Kit开发指南](../harmonyos-guides-V5/status-bar-extension-kit-guide-V5.md)。

## 系统-硬件

### Car Kit（车服务）

Car Kit（车服务）提供强大而便捷的汽车出行服务能力，助力全球开发者轻松完成智慧出行场景业务。HarmonyOS整合出行导航业务，开发者只需集成一个Kit，就可构建智慧出行业务场景。为应用瘦身的同时，也大大降低开发和维护成本。

Car Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Car Kit开发指南](../harmonyos-guides-V5/car-kit-guide-V5.md)。

支持开始和停止更新导航状态的指令。（[API参考](../harmonyos-references-V5/car-navigationinfomgr-V5.md#section1255014591510)）

* 新增管理应用与系统的连接状态，包括对连接状态的监听（[指南](../harmonyos-guides-V5/car-register-events-listener-V5.md)）、取消监听（[指南](../harmonyos-guides-V5/car-unregister-events-listener-V5.md)）和查询（[指南](../harmonyos-guides-V5/car-check-sys-events-detail-V5.md)）。
* 新增管理应用与系统的事件通知，包括对事件通知的监听（[指南](../harmonyos-guides-V5/car-register-connection-listener-V5.md)）、取消监听（[指南](../harmonyos-guides-V5/car-unregister-connection-listener-V5.md)）和查询（[指南](../harmonyos-guides-V5/car-get-connection-status-V5.md)）。
* 在设置导航数据场景下，支持自定义模式传递导航元数据。（[API参考](../harmonyos-references-V5/car-navigationinfomgr-V5.md#section12118327148)）

### Driver Development Kit（驱动开发服务）

Driver Development Kit（驱动开发服务）为开发者提供高效、安全、便捷的外设扩展驱动开发解决方案，为消费者带来即插即用的极致体验。

* 支持开发者开发外设配件的高阶功能，满足消费者高阶使用场景诉求。
* 扩展驱动框架支持外设扩展驱动生命周期管理，面向扩展设备应用提供扩展外设查询绑定能力接口。

Driver Development Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Driver Development Kit开发指南](../harmonyos-guides-V5/driver-development-kit-V5.md)。

### Multimodal Awareness Kit（多模态融合感知服务）

Multimodal Awareness Kit（多模态融合感知服务）多模态融合感知是基于设备的泛传感器数据，比如加速度计，陀螺仪等器件，进行活动，状态，姿态等的识别，例如，提供设备是否静止的感知事件。

Multimodal Awareness Kit继承原有设备状态感知框架的接口能力，在HarmonyOS NEXT进行了能力的增强，无新增接口能力。

详细信息请参见[MultimodalAwareness Kit开发指南](../harmonyos-guides-V5/multimodal-awareness-kit-V5.md)。

### Pen Kit（手写笔服务）

Pen Kit（手写笔服务）是华为提供的一套手写套件，提供笔刷效果、笔迹编辑、报点预测和一笔成形的功能。手写笔服务可以为产品带来优质手写体验，为您创造更多的手写应用场景。

Pen Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Pen Kit开发指南](../harmonyos-guides-V5/pen-kit-guide-V5.md)。

新增全局取色功能。（[指南](../harmonyos-guides-V5/pen-image-feature-picker-V5.md)、[API参考](../harmonyos-references-V5/pen-instantsshapegenerator-V5.md)）

### Sensor Service Kit（传感器服务）

Sensor Service Kit（传感器服务）使应用程序能够从传感器获取原始数据，并提供振感控制能力。

Sensor（传感器）模块是应用访问底层硬件传感器的一种设备抽象概念。开发者可根据传感器提供的相关接口订阅传感器数据，并根据传感器数据定制相应的算法开发各类应用，比如指南针、运动健康、游戏等。

Vibrator（振动）模块最大化开放马达器件能力，通过拓展马达服务实现振动与交互融合设计，打造细腻精致的一体化振动体验和差异化体验，提升用户交互效率和易用性、提升用户体验、增强品牌竞争力。

Sensor Service Kit在HarmonyOS NEXT阶段对Sensor和Vibrator的能力进行了增强，对支持的场景、功能进行了进一步完善。

详细信息请参见[Sensor Service Kit开发指南](../harmonyos-guides-V5/sensor-service-kit-V5.md)。

## 系统-调试调优

### Performance Analysis Kit（性能分析服务）

Performance Analysis Kit（性能分析服务）为开发者提供应用事件、日志、跟踪分析工具，可观测应用运行时状态，用于行为分析、故障分析、安全分析、统计分析，帮助开发者持续改进应用体验。

Performance Analysis Kit在应用调试、问题定位、线上运维监控提供了如下能力：

* HiLog流水日志，提供开发者记录和获取流水日志能力。
* HiTraceMeter和HiTraceChain跟踪，提供开发者Trace度量和跨线程跨进程分布式跟踪的能力。
* HiAppEvent应用事件，提供开发者记录故障、行为、安全、统计事件的能力，并订阅系统事件。
* FaultLogger故障日志管理，提供开发者主动查询故障日志的通道。
* HiDebug资源采集，提供开发者获取应用、系统资源的使用情况。

Performance Analysis Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 新增应用崩溃、卡死事件支持扩展自定义参数的功能。
* 新增应用启动耗时、滑动卡顿、主线程超时事件。
* 新增应用CPU高负载、24h功耗器件分解统计事件。
* 新增应用踩内存、资源泄漏事件。
* 新增应用内Trace采集接口，应用内存、CPU使用率、系统GC统计信息获取接口。
* 增强故障分析案例库。

详细信息请参见[Performance Analysis Kit开发指南](../harmonyos-guides-V5/performance-analysis-kit-V5.md)。

HiAppEvent支持设置每次取出的应用事件包的数据条数。（[API参考](../harmonyos-references-V5/js-apis-hiviewdfx-hiappevent-V5.md#setrow12)）

HiDebug提供获取应用进程的JS堆内存限制的接口。（[API参考](../harmonyos-references-V5/js-apis-hidebug-V5.md#memorylimit12)）

新增API支持获取应用进程被调试的状态。（[API参考](../harmonyos-references-V5/js-apis-hidebug-V5.md#hidebugisdebugstate12)）

## 调试命令

bm工具支持指定目录安装hqf和卸载hqf。（[指南](../harmonyos-guides-V5/bm-tool-V5.md#快速修复命令quickfix)）

cem工具已支持在USER版本的镜像中使用。

### Test Kit（应用测试服务）

Test Kit（应用测试服务）为开发者提供单元测试和UI测试能力，同时为开发者提供了SmartPerf性能功耗测试工具。

单元测试能力包括单元测试用例执行能力，提供用例编写基础接口，生成对应报告，用于测试系统或应用接口。

UI测试能力提供简洁易用的查找和操作界面控件的API，支持用户开发基于界面操作的自动化测试脚本。

测试能力在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 支持shell命令模拟操作能力，可通过shell命令模拟UI操作 。
* 支持鼠标、键盘外设模拟操作能力。
* 支持监听Toast和Dialog控件，并可获取控件文本内容。
* 控件查找能力优化，支持查找指定控件节点下属子控件。
* 控件查找效率优化，内部逻辑优化，缩短控件查找耗时。

SmartPerf工具可用于检测性能、功耗相关指标，包括FPS、CPU、GPU、RAM、Temp等，通过量化的指标项了解应用性能状况。SmartPerf-Daemon支持shell命令行方式，同时适用于有屏和无屏设备。

详细信息请参见[测试开发指南](../harmonyos-guides-V5/app-testing-overview-V5.md)。

## 媒体

## Ringtone Kit

【新增Kit】Ringtone Kit（铃声服务）是一个用于设置铃声的工具库。通过使用Ringtone Kit，开发者可以在HarmonyOS应用中提供铃声设置的功能，为用户提供简单一致、安全高品质的铃声设置体验。（[指南](../harmonyos-guides-V5/ringtone-kit-guide-V5.md)、[API参考](../harmonyos-references-V5/ringtone-ringtone-V5.md)）

### Audio Kit（音频服务）

Audio Kit（音频服务）主要提供场景化的音频播放、录制接口，帮助开发者快速构建音频高清采集及沉浸式播放能力。

Audio Kit在HarmonyOS NEXT阶段新增支持低时延采集/播放，低功耗播放，空间音频，音振协同等关键功能。

详细信息请参见[Audio Kit开发指南](../harmonyos-guides-V5/audio-kit-V5.md)。

提供取消注册监听音量变化事件的接口。（[API参考](../harmonyos-references-V5/js-apis-audio-V5.md#offvolumechange12)）

### AVCodec Kit（音视频编解码服务）

AVCodec kit（音视频编解码服务）提供音视频文件或者流媒体的读取，媒体文件的解析和音视频解码，音视频文件的编码和文件封装等功能。视频编解码还提供了硬件加速能力。

AVCodec Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[AVCodec Kit开发指南](../harmonyos-guides-V5/avcodec-kit-V5.md)。

* 支持随帧设置编码QP。（[指南](../harmonyos-guides-V5/video-encoding-V5.md)）
* DRM媒体解密场景支持增强，支持由上层应用做媒体解封装。（[音频解码指南](../harmonyos-guides-V5/audio-decoding-V5.md)、[视频解码指南](../harmonyos-guides-V5/video-decoding-V5.md)）

### AVSession Kit（音视频播控服务）

AVSession Kit（音视频播控服务）是系统提供的音视频管控服务，用于统一管理系统中所有音视频行为，帮助开发者快速构建音视频统一展示和控制能力。

AVSession Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[AVSession Kit开发指南](../harmonyos-guides-V5/avsession-kit-V5.md)。

支持自定义投播组件样式（pickerStyle）。（[API参考](../harmonyos-references-V5/ohos-multimedia-avcastpicker-V5.md#属性)）

### Camera Kit（相机服务）

Camera Kit（相机服务）提供的接口可以开发相机应用，应用通过访问和操作相机硬件，实现基础操作，如预览、拍照和录像；还可以通过接口组合完成更多操作，如控制闪光灯和曝光时间、对焦或调焦等。

Camera Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Camera Kit开发指南](../harmonyos-guides-V5/camera-kit-V5.md)。

提供用于获取相机设备传感器方向的C API。（[API参考](../harmonyos-references-V5/camera__device_8h-V5.md)）

新增一批C API，完善相机C API能力，例如获取图片对象的能力（photo\_native.h）、拍照开始信息的定义（Camera\_CaptureStartInfo）、曝光结束信息的定义（Camera\_FrameShutterEndInfo）、平滑变焦参数信息的定义（Camera\_SmoothZoomInfo）、手电筒状态信息的定义（Camera\_TorchStatusInfo）等。（[API参考](../harmonyos-references-V5/_o_h___camera-V5.md)）

### DRM Kit（数字版权保护服务）

DRM Kit（数字版权保护服务）提供媒体内容播放过程中的数字版权保护功能，内置WisePlay DRM客户端功能，提供了证书管理、许可证管理、内容授权、内容解密等功能。

DRM Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[DRM Kit开发指南](../harmonyos-guides-V5/drm-kit-V5.md)。

### Image Kit（图片处理服务）

Image Kit提供了基础的图片编解码能力、图片编辑框架和图片加载框架能能力，包括以下关键能力集：

* 常用格式图片编解码，如Png，Jpeg，Webp，Gif（解码）。
* 图片常用变换操作，如旋转、平移、缩放、裁切。
* 图片常用EXIF信息读、写操作。
* 图片色彩空间支持和转换。
* HDR图片编解码，可选解码为SDR和HDR。
* 图像编辑框架和基础调节算法。

Image Kit在HarmonyOS NEXT阶段对上述能力进行了增强，比如支持更多编码格式、提供更强大的图片处理能力等。

详细信息请参见[Image Kit开发指南](../harmonyos-guides-V5/image-kit-V5.md)。

新增用于处理位图的C API。（[API参考](../harmonyos-references-V5/pixelmap__native_8h-V5.md)）

* 支持通过C API设置图像跨距，即图像每行占用的真实内存大小。（[API参考](../harmonyos-references-V5/_image___native_module-V5.md#oh_pixelmapinitializationoptions_setrowstride)）
* Pixelmap缩放时支持采用双线性缩放算法（C API）。（[API参考](../harmonyos-references-V5/_image___native_module-V5.md#oh_pixelmapnative_antialiasinglevel)）

### Media Kit（媒体服务）

Media Kit（媒体服务）提供了AVPlayer和AVRecorder用于播放、录制音视频。

Media Kit在HarmonyOS NEXT阶段新增支持在线视频播放（包含音频文件播放），视频录制，屏幕录制，视频转码，音频池，视频文件元数据获取，视频文件抽帧等能力。

详细信息请参见[Media Kit开发指南](../harmonyos-guides-V5/media-kit-V5.md)。

* AVPlayer支持字幕加载和选择。（[API参考](../harmonyos-references-V5/js-apis-media-V5.md#subtitleinfo12)）
* AvPlayer提供设置音频流类型的C API。（[API参考](../harmonyos-references-V5/_a_v_player-V5.md#oh_avplayer_setaudiorendererinfo)）
* AVScreenCapture支持PC端按屏幕录制时排除指定windowID的窗口画面。（[API参考](../harmonyos-references-V5/_a_v_screen_capture-V5.md#oh_avscreencapture_contentfilter_addwindowcontent)）
* 新增API支持AVPlayer播放多音轨的视频时选择指定音轨。（[API参考](../harmonyos-references-V5/js-apis-media-V5.md#selecttrack12)）
* 新增API支持设置音频静音或取消静音。（[API参考](../harmonyos-references-V5/js-apis-media-V5.md#setmediamuted12)）
* 新增C API支持设置录屏时的屏幕分辨率。（[API参考](../harmonyos-references-V5/_a_v_screen_capture-V5.md#oh_avscreencapture_resizecanvas)、[指南](../harmonyos-guides/avscreencapture-c-custom-scenarios.md#设置旋转适配)）
* 新增C API支持对应用自身的窗口做录屏隐私保护的豁免。（[API参考](../harmonyos-references-V5/_a_v_screen_capture-V5.md#oh_avscreencapture_skipprivacymode)、[指南](../harmonyos-guides/avscreencapture-c-custom-scenarios.md#隐私设置)）
* 新增API支持获取视频的预览缩略图。（[API参考](../harmonyos-references-V5/js-apis-media-V5.md#avimagequeryoptions12)）

### Media Library Kit（媒体文件管理服务）

Media Library Kit提供了用户图片和视频的增删改查和相册管理能力，包括以下关键能力集：

* 提供了图片和视频资产的管理能力，包含基础的增删改查功能；此外提供了分段式能力开放、HDR转码等能力。
* 提供了用户相册管理能力，支持相册重命名、相册图片和视频管理功能。
* 提供了应用监听用户图片和视频、相册变化的能力。
* 提供了特殊图片格式，如动态照片、连拍照片的能力。
* 提供了图片和视频的缩略图管理功能。
* 提供了photopicker组件，支持用户自有选择图片和视频。
* 提供了动态照片播放组件。

Media Library Kit在HarmonyOS NEXT阶段以全新架构为开发者提供媒体文件管理能力。详细信息请参见[Media Library Kit开发指南](../harmonyos-guides-V5/medialibrary-kit-V5.md)。

支持获取最近图片的能力。（[API参考](../harmonyos-references-V5/ohos-file-recentphotocomponent-V5.md)）

支持PhotoPicker缩略图和大图预览之间的联动。（[API参考](../harmonyos-references-V5/ohos-file-photopickercomponent-V5.md)）

### Scan Kit（统一扫码服务）

Scan Kit（统一扫码服务）作为软硬协同的系统级扫码服务，帮助开发者的应用快速构建面向各种场景的码图识别和生成能力，以及扫码直达能力。Scan Kit应用了多项计算机视觉技术和AI算法技术，不仅实现了远距离自动扫码，同时还针对多种复杂扫码场景（如暗光、污损、模糊、小角度、曲面码等）做了识别优化，提升扫码成功率与用户体验。

Scan Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Scan Kit开发指南](../harmonyos-guides-V5/scan-kit-guide-V5.md)。

* 新增通过字节数组生成码图能力。（[指南](../harmonyos-guides-V5/scan-generatearray-V5.md)）
* 识别本地图片能力支持模拟器适配。（[指南](../harmonyos-guides-V5/scan-detectbarcode-V5.md#section8793479155)）
* 自定义界面扫码提供重启算法识别的接口。（[API参考](../harmonyos-references-V5/scan-customscan-api-V5.md#section19244173211169)）

## Weather Service Kit

【新增Kit】Weather Service Kit（天气服务）是鸿蒙生态下的一个数据提供服务，Weather Service Kit融合了多家气象行业TOPs供应商，提供专业、精准、稳定的超本地化天气预报服务，帮助开发者为用户提供更贴心的本地生活服务，支撑行业客户防灾减灾、降本增效。（[指南](../harmonyos-guides-V5/weather-service-introduction-V5.md)、[API参考](../harmonyos-references-V5/weather-service-weatherservice-V5.md)）

## Wear Engine

【新增Kit】Wear Engine（穿戴引擎服务）面向手机和穿戴设备的应用与服务开发者，提供华为穿戴设备开放能力。可以实现手机上的生态应用与服务给华为穿戴设备发消息、发通知、传输数据，并获取穿戴设备状态、读取传感器数据等，也可以实现华为穿戴设备上的生态应用与服务给手机发消息、传输数据等。（[指南](../harmonyos-guides-V5/we-business_introduction-V5.md)、[API参考](../harmonyos-references-V5/wearengine_api-V5.md)）

## 图形

### AR Engine（AR引擎服务）

AR Engine（AR引擎服务）是一个用于在HarmonyOS上构建增强现实应用的引擎，提供了运动跟踪、环境跟踪和命中检测等空间计算能力。通过这些能力，可让您的应用实现虚拟世界与现实世界的融合，为您的应用提供全新的视觉体验和交互方式。

AR Engine是HarmonyOS NEXT全新提供的能力。详细信息请参见[AR Engine开发指南](../harmonyos-guides-V5/ar-engine-kit-guide-V5.md)。

* 新增平面语义识别能力，支持识别的平面类型包括墙面、地面、座椅面、桌面、天花板、门面、窗面、床面。（[指南](../harmonyos-guides-V5/arengine-get-plane-target-V5.md)）
* 新增识别目标形状能力，可识别的形状包括矩形和圆形。（[指南](../harmonyos-guides-V5/arengine-get-plane-shape-V5.md)）

### ArkGraphics 2D（方舟2D图形服务）

ArkGraphics 2D（方舟2D图形服务）提供多样化的2D绘制能力，自然流畅的动效和灵活的帧率配置能力，满足开发者多样化的UI自绘制需求，助力打造实时、沉浸、交互的应用体验。

ArkGraphics 2D在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 支持定制业务帧率。
* 支持更多色域定义。
* Drawing、文字绘制能力增强。

详细信息请参见[ArkGraphics 2D开发指南](../harmonyos-guides-V5/arkgraphics-2d-V5.md)。

* 2D绘制能力进一步增强，新增一批接口支持更多2D图形绘制的能力。（[API参考](../harmonyos-references-V5/js-apis-graphics-drawing-V5.md#clippath12)）
* 提供C API支持对独立进程窗口的帧率控制渲染。（[指南](../harmonyos-guides-V5/displaysoloist-native-guidelines-V5.md)、[API参考](../harmonyos-references-V5/_native_display_soloist-V5.md)）

  该能力依赖Native子进程及父子进程间的IPC通道的相关能力，更多信息请参考[Native子进程开发指导](../harmonyos-guides-V5/capi_nativechildprocess_development_guideline-V5.md)、[IPC通信开发指导](../harmonyos-guides-V5/ipc-capi-development-guideline-V5.md)。
* 新增多个自定义绘制的C API，包括[OH\_Drawing\_CanvasClipRoundRect()](../harmonyos-references-V5/_drawing-V5.md#oh_drawing_canvascliproundrect)、[OH\_Drawing\_PathAddOval()](../harmonyos-references-V5/_drawing-V5.md#oh_drawing_pathaddoval)、[OH\_Drawing\_RoundRectSetCorner()](../harmonyos-references-V5/_drawing-V5.md#oh_drawing_roundrectsetcorner)。
* 提供区域对象的相关API用于描述所绘制图形的区域信息。（[API参考](../harmonyos-references-V5/js-apis-graphics-drawing-V5.md#region12)）
* 提供C API增强图形绘制能力的易用性。（[API参考](../harmonyos-references-V5/_drawing-V5.md#oh_drawing_matrixgetall)）
* 新增文本及其效果绘制类接口。（[API参考](../harmonyos-references-V5/js-apis-graphics-drawing-V5.md#fontmetrics)）
* 支持设置页面级状态栏的文字颜色。（[API参考](../harmonyos-references-V5/js-apis-window-V5.md#systembarstyle12)）
* Surface提供支持HDR vivid播放屏幕提亮的C API：SET\_HDR\_WHITE\_POINT\_BRIGHTNESS、SET\_SDR\_WHITE\_POINT\_BRIGHTNESS。（[API参考](../harmonyos-references-V5/_native_window-V5.md#nativewindowoperation-1)）
* NativeWindow新增色彩空间的C API：SET\_COLOR\_GAMUT、GET\_COLOR\_GAMUT。（[API参考](../harmonyos-references-V5/_native_window-V5.md#nativewindowoperation-1)）
* NativeWindow与NativeBuffer新增HDR元数据类型的C API。（[OHHDRMetaData API参考](../harmonyos-references-V5/_o_h_h_d_r_meta_data-V5.md)、[OH\_NativeBuffer\_StaticMetadata API参考](../harmonyos-references-V5/_o_h___native_buffer___static_metadata-V5.md)）
* 绘制模块在原有C API能力的基础上，补齐ArkTS API能力。（[API参考](../harmonyos-references-V5/js-apis-graphics-drawing-V5.md)）
* 新增矩形网格对象Lattice，用于将图片按矩形网格进行划分。（[API参考](../harmonyos-references-V5/js-apis-graphics-drawing-V5.md#lattice12)）
* 新增支持描述文本行中连续文本块的度量信息（RunMetrics）和文本布局中单行文字的度量信息（LineMetrics）。（[API参考](../harmonyos-references-V5/js-apis-graphics-text-V5.md#runmetrics)）
* 对同一个帧同步信号支持多个callback回调实例。（[API参考](../harmonyos-references-V5/_native_vsync-V5.md#oh_nativevsync_requestframewithmulticallback)）
* 新增Window Buffer的C API定义NativeWindowBuffer。（[API参考](../harmonyos-references-V5/_o_h___native_image-V5.md#ohnativewindowbuffer)）

### ArkGraphics 3D（方舟3D图形服务）

ArkGraphics 3D（方舟3D图形服务）基于轻量级的3D引擎以及渲染管线为开发者提供基础3D场景绘制能力，供开发者便捷、高效地构建3D场景并完成渲染。

提供如下关键能力：

* 提供加载并解析glTF模型的能力，支持开发者将glTF模型文件置于应用文件沙盒中，通过ArkGraphics 3D提供的异步接口完成模型的加载以及渲染。
* 提供自定义灯光（Light）、相机（Camera）节点以及通用节点（Node）的能力，支撑开发者自定义场景灯光、渲染视角等信息，同时支撑用户动态地调整场景树结构以及节点属性进而调整3D场景。
* 提供创建图片（Image）、材质（Material）、环境（Environment）以及自定义着色器(Shader)的能力，支撑开发者调用ArkGraphics 3D提供的能力创建3D场景中使用的各种资源，支撑开发者自定义着色器，完成自定义3D材质渲染。
* 提供控制3D场景动画状态的能力，支撑开发者控制动画的开始、暂停、结束、播放到指定位置等操作，同时提供动画开始、结束时的回调函数支持开发者进行逻辑控制。
* 提供基础的3D渲染后处理能力，提供接口支撑开发者进行ToneMapping后处理相关控制。

ArkGraphics 3D是HarmonyOS NEXT全新提供的能力。详细信息请参见[ArkGraphics 3D开发指南](../harmonyos-guides-V5/arkgraphics-3d-V5.md)。

### Graphics Accelerate Kit（图形加速服务）

Graphics Accelerate Kit（图形加速服务）作为软硬件协同的系统级图形加速解决方案，帮助游戏应用快速构建超帧、ABR（自适应稳态渲染）等游戏渲染加速能力，解决游戏运行不流畅、卡顿掉帧、长时间运行导致发热发烫等痛点体验问题。

Graphics Accelerate Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Graphics Accelerate Kit开发指南](../harmonyos-guides-V5/graphics-accelerate-kit-guide-V5.md)。

支持Vulkan图形API平台开启超帧内插模式（[指南](../harmonyos-guides-V5/graphics-accelerate-fg-interpolation-vulkan-V5.md)）和超帧外插模式（[指南](../harmonyos-guides-V5/graphics-accelerate-fg-extrapolation-vulkan-V5.md)）。

新增超帧相机扩展信息接口，提升大地图游戏场景超帧预测精度。（[API参考](../harmonyos-references-V5/_graphics_accelerate-V5.md#section1450921818712)）

* 新增API支持获取ABR自适应缩放后的纹理索引。（[API参考](../harmonyos-references-V5/_graphics_accelerate-V5.md#section791920394423)）
* 新增API支持获取下一帧的ABR Buffer分辨率因子。（[API参考](../harmonyos-references-V5/_graphics_accelerate-V5.md#section157311245143415)）

### XEngine Kit（GPU加速引擎服务）

XEngine Kit（GPU加速引擎服务）提供基于马良GPU的性能提升方案，包括GPU/AI超分能力、自适应VRS、Subpass Shading等，通过图形算法以及软硬件优化，让用户拥有更高性能、更低功耗的3D游戏/应用、AR/VR体验。

XEngine Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[XEngine Kit开发指南](../harmonyos-guides-V5/xengine-kit-guide-V5.md)。

## 应用服务

### Account Kit（华为账号服务）

Account Kit（华为账号服务）提供简单、快速、安全的登录功能，让用户快捷地使用华为账号登录应用。用户授权后，华为账号可提供头像、昵称、手机号码等信息，帮助应用更了解用户。

Account Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Account Kit开发指南](../harmonyos-guides-V5/account-kit-guide-V5.md)。

华为账号一键登录按钮新增onClickEvent点击事件。（[API参考](../harmonyos-references-V5/account-api-component-manager-V5.md#section1141051512341)）

新增华为账号登录按钮拓展参数，支持开发者自定义按钮样式、自定义[Style](../harmonyos-references-V5/account-api-component-manager-V5.md#section19823216112610)类型按钮多态样式、设置图文混合样式按钮的图文间距和纯图标按钮的图标半径。（[API参考](../harmonyos-references-V5/account-api-component-manager-V5.md#section87572031102713)）

新增获取手机号一致性状态，实现用户更安全、更便捷的静默登录。（[API参考](../harmonyos-references-V5/account-api-authentication-V5.md#section571965992211)）

* 支持应用在使用未成年模式之前，判断当前设备环境是否支持未成年人模式。（[API参考](../harmonyos-references-V5/account-api-minorsprotection-V5.md#section233519244152)）
* 提供华为账号一键登录按钮显示的文本内容，包括“华为账号一键注册”和“华为账号一键登录”。（[API参考](../harmonyos-references-V5/account-api-component-manager-V5.md#section1645283915811)）

### Ads Kit（广告服务）

Ads Kit（广告服务）依托华为终端平台与数据能力为您提供流量变现服务，帮助您解决流量变现的难题；同时为广告主提供广告服务，配合华为终端平台向用户提供个性化的营销活动或商业广告。

Ads Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Ads Kit开发指南](../harmonyos-guides-V5/ads-introduction-V5.md)。

* 支持注入广告JavaScript对象到Web组件中。（[API参考](../harmonyos-references-V5/js-apis-advertising-V5.md#section4653201571018)）
* 贴片广告增加isPreload预加载参数。（[API参考](../harmonyos-references-V5/js-apis-advertising-V5.md#adrequestparams)）

### Calendar Kit（日历服务）

Calendar Kit提供日历与日程提醒管理能力，包括对日历帐户、日历日程的管理，并支持对日程设置单次、重复提醒，并指定提醒时间。

Calendar Kit在HarmonyOS NEXT阶段提供了全新的编辑器能力，支持开发者实现快速新建日程与保存能力，无需单独开发日程新建界面，降低接入成本。

Calendar Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Calendar Kit开发指南](../harmonyos-guides-V5/calendarmanager-overview-V5.md)。

### Call Kit（通话服务）

Call Kit（VoIP通话管理服务）是华为提供给VoIP通话类应用的VoIP通话管理服务。VoIP通话类应用可通过集成Call Kit，实现便捷的来电接听功能，提升用户使用体验。

Call Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Call Kit开发指南](../harmonyos-guides-V5/call-kit-guide-V5.md)。

* 上报来电时，支持指定通话类型是否为会议、视频会议是否支持语音接听。（[API参考](../harmonyos-references-V5/call-voipcall-V5.md#section4221135015444)）
* 通话状态支持正在接听、正在断开。（[API参考](../harmonyos-references-V5/call-voipcall-V5.md#section24523814719)）
* 上报通话状态改变时，支持指定通话类型。（[API参考](../harmonyos-references-V5/call-voipcall-V5.md#section5360122718341)）

### Cloud Foundation Kit（云开发服务）

Cloud Foundation Kit（云开发服务）可以按需为应用提供云函数、云数据库、云存储等云端服务。应用运行所需的服务器和环境可以皆由云端平台提供，开发者只需关注应用的业务逻辑，而无需关心基础设施（例如：服务器、操作系统、容器等）。

Cloud Foundation Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Cloud Foundation Kit开发指南](../harmonyos-guides-V5/cloud-foundation-kit-guide-V5.md)。

### Contacts Kit（联系人服务）

Contacts Kit （联系人服务）提供联系人管理能力，包括添加联系人、删除联系人、更新联系人等。

Contacts Kit在HarmonyOS NEXT阶段新增查询联系人接口，支持返回联系人id、key、邮箱等更丰富完整的数据。

详细信息请参见[Contacts Kit开发指南](../harmonyos-guides-V5/contacts-kit-V5.md)。

### Game Service Kit（游戏服务）

Game Service Kit（游戏服务）主要提供快速、低成本构建游戏基本能力（实名认证、游戏资产转移、防沉迷等）与游戏场景优化服务，有效提升游戏开发效率，帮助开发者进行游戏运营。

Game Service Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Game Service Kit开发指南](../harmonyos-guides-V5/game-service-kit-guide-V5.md)。

新增UnionLoginResult接口，支持华为账号和游戏官方账号联合登录的返回结果新增绑定用户信息。（[API参考](../harmonyos-references-V5/gameservice-gameplayer-V5.md#section556415719255)）

### Health Service Kit（运动健康服务）

Health Service Kit（运动健康服务）是为华为生态应用打造的基于华为账号和用户授权的运动健康数据开放平台。在获取用户授权后，开发者可以使用Health Service Kit提供的开放能力获取运动健康数据，基于多种类型数据构建运动健康领域应用与服务，为用户打造丰富、便捷、专业的运动健康场景体验。

Health Service Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Health Service Kit开发指南](../harmonyos-guides-V5/health-service-kit-guide-V5.md)。

* 新增静息心率，皮肤体温，血压，体重，身高采样数据类型。（[指南](../harmonyos-guides-V5/health-heart-rate-V5.md)、[API参考](../harmonyos-references-V5/health-api-healthdatatypes-V5.md)）
* 新增户外探险、篮球、滑雪等百种类型锻炼记录类型。（[指南](../harmonyos-guides-V5/health-exercisesequence-summary-V5.md)、[API参考](../harmonyos-references-V5/health-api-healthdatatypes-V5.md)）

### IAP Kit（应用内支付服务）

IAP Kit（应用内支付服务）为App提供便捷的应用内支付体验和简便的接入流程，让开发者聚焦App本身的业务能力，助力您的商业变现。App可通过使用华为应用内提供的系统级支付API快速启动IAP收银台，即可实现应用内支付。

IAP Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[IAP Kit开发指南](../harmonyos-guides-V5/iap-kit-guide-V5.md)。

支持订阅场景下使用优惠促销。（[指南](../harmonyos-guides-V5/iap-subscription-functions-V5.md#section15231185754812)）

### Location Kit（位置服务）

Location kit（位置服务）采用GNSS、WLAN、基站等定位技术，提供优秀的定位能力。

Location Kit涵盖定位服务、地理围栏、地理编码、逆地理编码、国家码等功能。

Location Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 支持地理围栏功能
* 支持定位过程中错误码上报

详细信息请参见[Location Kit开发指南](../harmonyos-guides-V5/location-kit-V5.md)。

### Live View Kit（实况窗服务）

Live View Kit（实况窗服务）支持应用将订单或者服务的实时状态信息变化在设备的关键界面展示，并对展示信息的生命周期、用户界面UI效果等进行管理。

Live View Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Live View Kit开发指南](../harmonyos-guides-V5/live-view-kit-guide-V5.md)。

* 支持在实况窗小折叠屏的外屏显示实况窗的简要信息。（[指南](../harmonyos-guides-V5/liveview-create-locally-V5.md#section11267105154)）
* 实况窗外屏形态模板参数external中新增type和backgroundPicture字段，实现实况窗外屏背景样式类型、外屏背景图片的定制。（[API参考](../harmonyos-references-V5/liveveiw-liveviewmanager-V5.md#section92302515457)）

### Map Kit（地图服务）

Map Kit（地图服务）是鸿蒙生态下的一个地图服务，为开发者提供强大而便捷的地图能力，助力全球开发者实现个性化地图呈现、地图搜索和路线规划等功能，轻松完成地图构建工作。您可以轻松地在HarmonyOS应用/元服务中集成地图相关的功能，全方位提升用户体验。

Map Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Map Kit开发指南](../harmonyos-guides-V5/map-kit-guide-V5.md)。

* 新增绘制3D建筑物功能。（[指南](../harmonyos-guides-V5/map-3dbuilding-V5.md)）
* 新增绘制动态轨迹功能。（[指南](../harmonyos-guides-V5/map-dyntrajectories-V5.md)）
* 逆地理编码新增isNearbyAoi、sortRule入参，支持返回附近的Aoi和设置POI的排序规则。（[API参考](../harmonyos-references-V5/map-site-V5.md#section1170341119303)）
* 驾车批量算路、步行批量算路、骑行批量算路、轨迹绑路新增支持传入Context上下文的接口。（[API参考](../harmonyos-references-V5/map-navi-api-V5.md)）
* 静态图新增支持传入Context上下文的接口。（[API参考](../harmonyos-references-V5/map-staticmap-V5.md)）
* 支持在地图上绘制弧线。（[指南](../harmonyos-guides-V5/map-arc-V5.md)）
* 新增getEventManager()接口，支持地图组件的事件监听。（[API参考](../harmonyos-references-V5/map-map-V5.md#section154601059144812)）
* 以动画形式更新相机状态时，支持传入多个marker。（[API参考](../harmonyos-references-V5/map-map-V5.md#section13597354171415)）
* 支持设置是否始终显示比例尺。（[API参考](../harmonyos-references-V5/map-map-V5.md#section3541416552)）
* 支持设置地图元素压盖顺序。（[指南](../harmonyos-guides-V5/map-display-order-V5.md)）
* 支持根据路由地进行坐标纠偏。（[指南](../harmonyos-guides-V5/map-convert-coordinate-V5.md#section596718526385)）

### Notification Kit（用户通知服务）

Notification Kit（用户通知服务）为开发者提供本地通知发布通道，本地通知根据通知类型及发布场景会产生对应的铃声、震动、横幅、锁屏、息屏、通知栏提醒和显示。

Notification Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 发布通知支持携带唯一标识字段，用于端云消息去重。
* 支持接入上传下载类常驻通知。
* 支持应用申请权益后使用自定义通知铃声。

详细信息请参见[Notification Kit开发指南](../harmonyos-guides-V5/notification-kit-V5.md)。

### Payment Kit（华为支付服务）

Payment Kit（华为支付服务）提供了方便、安全和快捷的支付方式，将强大的支付、营销、运营等能力，通过HarmonyOS系统级接口形式开放给广大开发者，集成便捷且快速。用户可在开发者的应用/元服务内通过支付完成实体商品或服务的购买并展示支付结果。

Payment Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Payment Kit开发指南](../harmonyos-guides-V5/payment-kit-guide-V5.md)。

### PDF Kit（PDF服务）

PDF Kit（PDF服务），提供了打开PDF文件、页面添加批注、页眉页脚、水印、背景及书签等相关的功能，便于用户对PDF文档操作的更多的应用场景。

PDF Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[PDF Kit开发指南](../harmonyos-guides-V5/pdf-kit-guide-V5.md)。

支持通过PdfView组件实现：打开PDF文档、PDF文档与图片格式互转、添加页眉页脚、添加水印、添加背景、添加批注、添加书签。（[指南](../harmonyos-guides-V5/pdf-pdfservice-implements-V5.md)）

### Preview Kit（文件预览服务）

Preview Kit（文件预览服务）为应用提供便捷的文件快速预览服务。应用可以通过Preview Kit提供的预览API，快速启动预览界面，实现对各类文件的预览。

Preview Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Preview Kit开发指南](../harmonyos-guides-V5/preview-kit-guide-V5.md)。

### Push Kit（推送服务）

Push Kit（推送服务）是华为提供的消息推送平台，建立了从云端到终端的消息推送通道。所有HarmonyOS应用可通过集成Push Kit，实现向应用实时推送消息，使消息易见，构筑良好的用户关系，提升用户的感知度和活跃度。

Push Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Push Kit开发指南](../harmonyos-guides-V5/push-kit-guide-V5.md)。

优化开发者接入步骤，开发者无需手动配置公钥指纹和Client ID。（[指南](../harmonyos-guides-V5/push-config-setting-V5.md)）

### Scenario Fusion Kit（融合场景服务）

Scenario Fusion Kit（融合场景服务）基于ArkUI框架原生组件开发，提供跨多个子系统融合的场景化组件，降低开发者接入复杂度，确保鸿蒙生态体验统一。ArkUI一行核心代码启用，智能推荐输入建议，复杂表单一键填充。通过完善应用/元服务的系统开发能力，进一步丰富鸿蒙生态，满足开发者在HarmonyOS系统下的服务闭环诉求。

Scenario Fusion Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Scenario Fusion Kit开发指南](../harmonyos-guides-V5/scenario-fusion-guide-V5.md)。

支持实名认证Button和人脸核身场景化Button。（[API参考](../harmonyos-references-V5/scenario-fusion-functionalbuttoncomponentmanager-V5.md)）

* 新增支持实况窗订阅Button。（[API参考](../harmonyos-references-V5/scenario-fusion-functionalbuttoncomponentmanager-V5.md#section162555482410)）
* 支持三方框架接入智能填充。（[指南](../harmonyos-guides-V5/scenario-fusion-tripartiteframework-V5.md)）

### Share Kit（分享服务）

Share Kit（分享服务）为应用提供文本、图片、视频等内容跨应用分享能力，用于将内容发送到其他应用。应用把需要分享的内容和预览样式配置给Share Kit，Share Kit将根据分享的数据类型、数量等信息构建分享面板，为用户提供内容预览、推荐分享联系人、关联应用及操作界面，便于用户快速选择分享应用或操作，将内容分发到目标应用。

Share Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Share Kit开发指南](../harmonyos-guides-V5/share-kit-guide-V5.md)。

新增支持一碰跨端设备分享，可实现传输图片、共享wifi等场景。（[API参考](../harmonyos-references-V5/share-harmony-share-V5.md)、[指南](../harmonyos-guides-V5/share-mobilephone-harmony-share-V5.md)）

### Store Kit（应用市场服务）

Store Kit（应用市场服务）主要负责应用市场业务的对外开放能力，可以更好的支持应用的下载、推荐和分发等场景。使用Store Kit可以使您的应用具有元服务和应用的推广能力，也能够有效减少用户首次下载应用的等待时长以及减少对用户空间的无效占用。

Store Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Store Kit开发指南](../harmonyos-guides-V5/store-kit-guide-V5.md)。

* 新增隐私管理服务，提供隐私链接查询、隐私签署状态查询和停止隐私协议功能。（[指南](../harmonyos-guides-V5/store-privacy-V5.md)、[API参考](../harmonyos-references-V5/store-privacymanager-V5.md)）
* 新增未上架应用接入隐私管理服务方法。（[指南](../harmonyos-guides-V5/store-privacy-V5.md#section133476117117)）
* 应用市场推荐部分新增通过Link链接的方式拉起应用市场应用详情页功能。（[指南](../harmonyos-guides-V5/store-productview-V5.md#section13070154413)）

### Wallet Kit（钱包服务）

Wallet Kit（钱包服务）集成了终端“芯-端-云”全栈技术的开放能力，可实现车钥匙、交通卡的凭证电子化。让用户能够轻松地将车钥匙和交通卡保存在手机中，以便在适当的时间使用。

Wallet Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Wallet Kit开发指南](../harmonyos-guides-V5/wallet-kit-guide-V5.md)。

## AI

### Intents Kit（意图框架服务）

Intents Kit（意图框架服务）是HarmonyOS级的意图标准体系 ，意图连接了应用/元服务内的业务功能。意图框架能帮开发者将应用/元服务内的业务功能，智能分发到各系统入口，这个过程即智慧分发。其中系统入口包括：小艺对话、小艺搜索、小艺建议等。

Intents Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Intents Kit开发指南](../harmonyos-guides-V5/intents-kit-guide-V5.md)。

新增本地搜索方案，开发者将应用内的功能和内容通过意图框架共享到HarmonyOS，即可实现“一步搜索，内容直达”。（[指南](../harmonyos-guides-V5/intents-search-rec-V5.md)）

### Core Speech Kit（基础语音服务）

Core Speech Kit（基础语音服务）集成了语音类基础AI能力，包括文本转语音（TextToSpeech）及语音识别（SpeechRecognizer）能力，便于用户与设备进行互动，实现将实时输入的语音与文本之间相互转换。

Core Speech Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Core Speech Kit开发指南](../harmonyos-guides-V5/core-speech-kit-guide-V5.md)。

### Core Vision Kit（基础视觉服务）

Core Vision Kit（基础视觉服务）是机器视觉相关的基础能力，例如通用文字识别（即OCR，Optical Character Recognition，也称为光学字符识别）、人脸检测、人脸比对以及主体分割等能力。

Core Vision Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Core Vision Kit开发指南](../harmonyos-guides-V5/core-vision-kit-guide-V5.md)。

* 支持多目标识别，可检测出给定图片中的各种物体，包括风景、动物、植物、建筑、树、人脸、表格、文本等位置，并框选出物体。（[指南](../harmonyos-guides-V5/core-vision-object-detection-V5.md)）。
* 支持人体骨骼点检测，实现对人体骨骼点的检测和骨骼信息的描述。（[指南](../harmonyos-guides-V5/core-vision-skeleton-detection-V5.md)）

### HiAI Foundation Kit（HiAI Foundation 服务）

HiAI Foundation Kit作为芯片使能的基础平台，提供了300+算子的支持，具备业界良好的模型兼容性，为众多业务场景提供了更高性能更低功耗的计算环境。HiAI Foundation Kit衔接智慧业务和计算芯片，支持华为MindSpore、TensorFlow、Caffe、Paddle、ONNX等框架的对接，支持芯片内多计算单元的异构计算，为开发者提供模型轻量化、模型转换、模型可视化等高效工具链。

HiAI Foundation Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[HiAI Foundation Kit开发指南](../harmonyos-guides-V5/hiai-foundation-kit-guide-V5.md)。

新增单算子特性，用于三方框架将部分算子通过单算子对接的方式迁移至NPU，与整网CPU计算相比，性能更优。（[指南](../harmonyos-guides-V5/hiaifoundation-single-operator-application-V5.md)）

### MindSpore Lite Kit（昇思推理框架服务）

MindSpore Lite Kit（昇思推理框架服务）是一个轻量化、高性能的端侧AI引擎，提供了标准的模型推理和训练接口，内置通用硬件高性能算子库，支持Neural Network Runtime Kit使能AI专用芯片加速推理。

MindSpore Lite Kit在HarmonyOS NEXT阶段带来如下能力的新增或增强：

* 运行后端支持配置NNRt Device，使能专用芯片加速推理；
* 提供了端侧模型微训练的能力，支持基于MindSpore导出的训练图，在端侧个性化微调；
* 高性能算子库支持列表扩充，性能进一步优化。

详细信息请参见[MindSpore Lite Kit开发指南](../harmonyos-guides-V5/mindspore-lite-kit-V5.md)。

### Natural Language Kit（自然语言理解服务）

Natural Language Kit（自然语言理解服务）提供了多项文本语义理解相关的基础能力，帮助开发者更好地处理和分析文本数据。

Natural Language Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Natural Language Kit开发指南](../harmonyos-guides-V5/natural-language-kit-guide-V5.md)。

### Neural Network Runtime Kit（Neural Network运行时服务）

Neural Network Runtime Kit（Neural Network运行时服务）是AI领域的跨芯片推理计算运行时，作为中间桥梁打通了上层AI推理框架和底层AI加速芯片，提供了统一的AI硬件加速接口，让推理框架的开发者能够简单快捷地适配和使用底层不同AI加速芯片的能力。

Neural Network Runtime Kit为原有能力整合，涵盖了原有的在线构图、模型编译、编译结果缓存、推理计算等能力。

Neural Network Runtime Kit在HarmonyOS NEXT阶段新增扩充在线构图支持的算子列表的能力。

详细信息请参见[Neural Network Runtime Kit开发指南](../harmonyos-guides-V5/neural-network-runtime-kit-V5.md)。

### Speech Kit（场景化语音服务）

Speech Kit（场景化语音服务）集成了语音类AI能力，包括朗读控件（TextReader）能力，便于用户与设备进行互动，为用户实现朗读文章。

Speech Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Speech Kit开发指南](../harmonyos-guides-V5/speech-kit-guide-V5.md)。

* 支持AI字幕控件，可用于在用户不熟悉音频源语言或者静音时，为用户提供字幕服务。（[指南](../harmonyos-guides-V5/speech-aicaption-guide-V5.md)）
* 支持设置应用是否保持后台运行。（[API参考](../harmonyos-references-V5/speech-textreader-api-V5.md#section6129163245310)）
* 在朗读场景下，支持播放上一篇文章（[API参考](../harmonyos-references-V5/speech-textreader-api-V5.md#section158081432771)）、下一篇文章（[API参考](../harmonyos-references-V5/speech-textreader-api-V5.md#section1272844214712)）、通过id指定的文章（[API参考](../harmonyos-references-V5/speech-textreader-api-V5.md#section1658111564332)）。

### Vision Kit（场景化视觉服务）

Vision Kit（视觉服务）集成了视觉类AI能力，包括人脸活体验证（interactiveLiveness）能力、卡证识别（CardRecognition）能力、文档扫描（DocumentScanner）能力。

Vision Kit是HarmonyOS NEXT全新提供的能力。详细信息请参见[Vision Kit开发指南](../harmonyos-guides-V5/vision-kit-guide-V5.md)。

* 活体检测支持配置隐私模式。（[API参考](../harmonyos-references-V5/vision-interactive-liveness-V5.md#section16532153115517)）
* 新增AI识图控件。（[指南](../harmonyos-guides-V5/vision-imageanalyzer-V5.md)、[API参考](../harmonyos-references-V5/vision-image-analyzer-V5.md)）
* 新增卡证识别新增配置接口，支持自定义拍摄模式、图库按钮以及卡证内容配置。（[API参考](../harmonyos-references-V5/vision-card-recognition-V5.md#section14439151274411)）

## 其他变更

商用系统版本中应用的HiLog日志默认级别由INFO调整为WARN。受此影响，Faultlogger崩溃日志中进程崩溃前的HiLog日志，包含WARN/ERROR/FATAL级别日志，不再包含INFO级别日志。

说明

可通过如下方法确认系统版本为商用版或开发者版本：

* 方法一：通过系统版本号进行确认。在设备的“设置 > 关于手机 > 操作系统”界面查看“软件版本”，版本号最后以log结尾则表示该系统为开发者Log版；版本号结尾无log则表示系统为商用版。
* 方法二：使用hdc调试命令查询。命令为“hdc shell param get const.logsystem.versiontype”，命令返回commercial表示系统为商用版，否则为开发者Log版。但需注意，使用hdc调试命令需打开设备的“开发者模式”，该模式开启后仍可获取INFO级别日志。
