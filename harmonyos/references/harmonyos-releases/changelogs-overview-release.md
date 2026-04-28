---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-overview-release
title: 总览
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > 总览
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:08+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:65669fb6f9c2910b0312c48c710f0febf5c552e0d5ae9c30b55a86e8853b07b8
---

## 概述

HarmonyOS NEXT每次新版本发布均会或多或少引入一些变更，这些变更可能会影响到您的应用。为了使开发者更清晰的感知变更对应用的影响，我们将变更做如下分类：

* **针对所有应用的变更**

  此类变更可能影响在HarmonyOS最新版本的镜像设备上运行的所有应用，无论您的应用是使用API 12或是更早的API版本进行开发。

  此类变更均需应用进行适配。
* **针对API 12应用的变更**

  此类变更仅影响您基于API 12的SDK进行开发和编译的应用。这类变更存在于以下两种场景：

  + API 11及以下版本的API在API 12发生变更，但变更仅影响使用API 12的SDK进行增量开发或重新编译。如应用已在API 11及以下版本完成编译，则不受变更影响。
  + 在API 12的Beta版本中新增的API仍可能发生变更，此类变更可能影响基于API 12进行开发的应用。
* **UX样式或效果的变更**

  仅对系统提供的UX样式和效果进行变更，开发者可以根据变更说明来判断是否影响应用整体风格或预期效果。

## 针对所有应用的变更

| Kit | 变更描述 | 变更引入版本 |
| --- | --- | --- |
| Ability Kit | [禁止通过wantAgent拉起ExtensionAbility](changelogs-for-all-apps-b071.md#禁止通过wantagent拉起extensionability) | HarmonyOS NEXT Release |
| ArkUI | [startAbility/openLink锁屏时限制拉起行为](changelogs-for-all-apps-b071.md#startabilityopenlink锁屏时限制拉起行为) | HarmonyOS NEXT Release |
| Media Library Kit | [@ohos.file.photoAccessHelper相册添加资产、移除资产等接口行为变更](changelogs-for-all-apps-b071.md#ohosfilephotoaccesshelper相册添加资产移除资产等接口行为变更)  \* 该变更在10月17日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.906。 | HarmonyOS NEXT Release |
| Ability Kit | [拉起UIExtensionAbility增加调用方为前台应用的校验](changelogs-for-all-apps-b065.md#拉起uiextensionability增加调用方为前台应用的校验) | HarmonyOS NEXT Beta |
| Ability Kit | [借助Want分享文件URI时无权限的URI会被拦截](changelogs-for-all-apps-b065.md#借助want分享文件uri时无权限的uri会被拦截)  \* 该变更在9月12日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.806。 | HarmonyOS NEXT Beta |
| Ability Kit | [childProcessManager增加子进程最大数量限制](changelogs-for-all-apps-b065.md#childprocessmanager增加子进程最大数量限制)  \* 该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。 | HarmonyOS NEXT Beta |
| Ability Kit | [startAbility从后台发起时，即使应用正在运行长时任务，也不能调用成功。](changelogs-for-all-apps-b065.md#startability从后台发起时即使应用正在运行长时任务也不能调用成功)  \* 该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。 | HarmonyOS NEXT Beta |
| Ability Kit | [包管理@ohos.bundle.bundleManager.d.ts中的bundleManager.verifyAbc接口以及bundleManager.deleteAbc接口变更为system API](changelogs-for-all-apps-b065.md#包管理ohosbundlebundlemanagerdts中的bundlemanagerverifyabc接口以及bundlemanagerdeleteabc接口变更为system-api)  \* 该变更在9月27日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.814。 | HarmonyOS NEXT Beta |
| ArkTS | [util.TextEncoder模块utf-16le和utf-16be编码数据行为变更](changelogs-for-all-apps-b065.md#utiltextencoder模块utf-16le和utf-16be编码数据行为变更)  \* 该变更在9月12日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.806。 | HarmonyOS NEXT Beta |
| ArkTS | [Worker模块中RestrictedWorker的接口变更为system API](changelogs-for-all-apps-b065.md#worker模块中restrictedworker的接口变更为system-api)  \* 该变更在9月27日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.814。 | HarmonyOS NEXT Beta |
| ArkUI | [优化状态变量场景下ForEach的冗余刷新行为](changelogs-for-all-apps-b065.md#优化状态变量场景下foreach的冗余刷新行为)  \* 该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。 | HarmonyOS NEXT Beta |
| AVCodec Kit | [OH\_AVCodecBufferAttr 接口行为变更](changelogs-for-all-apps-b065.md#oh_avcodecbufferattr-接口行为变更) | HarmonyOS NEXT Beta |
| Camera Kit | [CameraPosition.CAMERA\_POSITION\_FOLD\_INNER接口废弃](changelogs-for-all-apps-b065.md#camerapositioncamera_position_fold_inner接口废弃) | HarmonyOS NEXT Beta |
| Core File Kit | [file-access-across-devices 接口行为变更](changelogs-for-all-apps-b065.md#file-access-across-devices-接口行为变更) | HarmonyOS NEXT Beta |
| Core File Kit | [setSecurityLabel接口行为变更](changelogs-for-all-apps-b065.md#setsecuritylabel接口行为变更) | HarmonyOS NEXT Beta |
| Core File Kit | [getSecurityLabel接口行为变更](changelogs-for-all-apps-b065.md#getsecuritylabel接口行为变更) | HarmonyOS NEXT Beta |
| Core File Kit | [文件授权接口行为变更](changelogs-for-all-apps-b065.md#文件授权接口行为变更)  \* 该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。 | HarmonyOS NEXT Beta |
| Distributed Service Kit | [使用udid-hash与appid和盐值基于sha256混淆截断后保留前16位值作为deviceid，调用行为变更](changelogs-for-all-apps-b065.md#使用udid-hash与appid和盐值基于sha256混淆截断后保留前16位值作为deviceid调用行为变更)  \* 该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。 | HarmonyOS NEXT Beta |
| 调试命令 | [命令行调试工具使用权限缩小](changelogs-for-all-apps-b065.md#命令行调试工具使用权限缩小) | HarmonyOS NEXT Beta |
| 调试命令 | [hdc工具tmode usb命令功能废弃](changelogs-for-all-apps-b065.md#hdc工具tmode-usb命令功能废弃) | HarmonyOS NEXT Beta |
| 调试命令 | [aa工具不支持对Release模式的应用进行调试](changelogs-for-all-apps-b065.md#aa工具不支持对release模式的应用进行调试)  \* 该变更在9月12日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.806。 | HarmonyOS NEXT Beta |
| Ability Kit | [bm命令行工具变更](changelogs-for-all-apps-b060.md#bm命令行工具变更) | HarmonyOS NEXT Developer Beta5 |
| ArkTS | [util.TextDecoder模块ignoreBOM功能行为变更](changelogs-for-all-apps-b060.md#utiltextdecoder模块ignorebom功能行为变更) | HarmonyOS NEXT Developer Beta5 |
| ArkTS | [Base64Helper、StringDecoder模块部分接口参数异常错误码由undefined变更为401](changelogs-for-all-apps-b060.md#base64helperstringdecoder模块部分接口参数异常错误码由undefined变更为401) | HarmonyOS NEXT Developer Beta5 |
| Background Tasks Kit | [reminderAgentManager.publishReminder权限管控](changelogs-for-all-apps-b060.md#reminderagentmanagerpublishreminder权限管控) | HarmonyOS NEXT Developer Beta5 |
| Media Library Kit | [@ohos.multimedia.medialibrary变更](changelogs-for-all-apps-b060.md#ohosmultimediamedialibrary变更) | HarmonyOS NEXT Developer Beta5 |
| Ability Kit | [入口图标和入口标签规格变动](changelogs-for-all-apps-b035.md#入口图标和入口标签规格变动) | HarmonyOS NEXT Developer Beta3 |
| ArkTS | [TextEncoder.encodeInto()接口变更](changelogs-for-all-apps-b035.md#textencoderencodeinto接口变更) | HarmonyOS NEXT Developer Beta3 |
| ArkUI | [Search/TextInput/TextArea onchange回调新增可选参数预上屏文本](changelogs-for-all-apps-b035.md#searchtextinputtextarea-onchange回调新增可选参数预上屏文本) | HarmonyOS NEXT Developer Beta3 |
| Localization Kit | [资源匹配逻辑变更](changelogs-for-all-apps-b035.md#资源匹配逻辑变更) | HarmonyOS NEXT Developer Beta3 |
| Localization Kit | [raw\_file模块头文件变更](changelogs-for-all-apps-b035.md#raw_file模块头文件变更) | HarmonyOS NEXT Developer Beta3 |
| Network Kit | [webSocket.connect接口新增2302998错误码](changelogs-for-all-apps-b035.md#websocketconnect接口新增2302998错误码) | HarmonyOS NEXT Developer Beta3 |
| NDK开发 | [匿名内存执行权限管控策略变更说明](changelogs-for-all-apps-b031.md#匿名内存执行权限管控策略变更说明) | HarmonyOS NEXT Developer Beta2 |
| NDK开发 | [应用编译构建对不支持命令强校验](changelogs-for-all-apps-b031.md#应用编译构建对不支持命令强校验) | HarmonyOS NEXT Developer Beta2 |
| NDK开发 | [应用编译构建建议cmake\_minimum\_required修改为不低于3.5.0的版本](changelogs-for-all-apps-b031.md#应用编译构建建议cmake_minimum_required修改为不低于350的版本) | HarmonyOS NEXT Developer Beta2 |
| ArkWeb | [fileAccess接口行为变更](changelogs-for-all-apps-b031.md#fileaccess接口行为变更) | HarmonyOS NEXT Developer Beta2 |
| ArkData | [Asset属性类型变更](changelogs-for-all-apps-b031.md#asset属性类型变更) | HarmonyOS NEXT Developer Beta2 |
| ArkData | [setSessionId接口行为变更](changelogs-for-all-apps-b031.md#setsessionid接口行为变更) | HarmonyOS NEXT Developer Beta2 |
| ArkGraphics 2D | [OH\_Drawing\_RegisterFont()、OH\_Drawing\_RegisterFontBuffer()接口增加报错码](changelogs-for-all-apps-b031.md#oh_drawing_registerfontoh_drawing_registerfontbuffer接口增加报错码) | HarmonyOS NEXT Developer Beta2 |
| ArkTS | [编译语法检查场景补齐](changelogs-for-all-apps-b031.md#编译语法检查场景补齐) | HarmonyOS NEXT Developer Beta2 |
| ArkTS | [TreeSet.clear()和TreeMap.clear()接口行为变更](changelogs-for-all-apps-b031.md#treesetclear和treemapclear接口行为变更) | HarmonyOS NEXT Developer Beta2 |
| ArkTS | [TreeMap.setAll()接口行为变更](changelogs-for-all-apps-b031.md#treemapsetall接口行为变更) | HarmonyOS NEXT Developer Beta2 |
| ArkTS | [TreeMap、TreeSet的hasKey和has接口行为变更](changelogs-for-all-apps-b031.md#treemaptreeset的haskey和has接口行为变更) | HarmonyOS NEXT Developer Beta2 |
| ArkTS | [URLParams类append接口添加的值中包含连续空格时行为变更](changelogs-for-all-apps-b031.md#urlparams类append接口添加的值中包含连续空格时行为变更) | HarmonyOS NEXT Developer Beta2 |
| ArkTS | [URLParams类在入参字符串中包含大小写不同编码值时，toString()接口表现结果不一致变更](changelogs-for-all-apps-b031.md#urlparams类在入参字符串中包含大小写不同编码值时tostring接口表现结果不一致变更) | HarmonyOS NEXT Developer Beta2 |
| ArkTS | [URLParams类append接口行为变更](changelogs-for-all-apps-b031.md#urlparams类append接口行为变更) | HarmonyOS NEXT Developer Beta2 |
| ArkUI | [@Component和@ComponentV2修饰的自定义组件使用@Observed或者@ObservedV2修饰的类增加相关校验](changelogs-for-all-apps-b031.md#component和componentv2修饰的自定义组件使用observed或者observedv2修饰的类增加相关校验) | HarmonyOS NEXT Developer Beta2 |
| ArkUI | [TextTimer的onTimer回调频率与参数单位调整](changelogs-for-all-apps-b031.md#texttimer的ontimer回调频率与参数单位调整) | HarmonyOS NEXT Developer Beta2 |
| ArkUI | [RichEditor组件builderSpan支持绑定自定义菜单](changelogs-for-all-apps-b031.md#richeditor组件builderspan支持绑定自定义菜单) | HarmonyOS NEXT Developer Beta2 |
| ArkUI | [RichEditor的lineHeight、letterSpacing、lineSpacing属性返回值单位变更](changelogs-for-all-apps-b031.md#richeditor的lineheightletterspacinglinespacing属性返回值单位变更) | HarmonyOS NEXT Developer Beta2 |
| ArkUI | [RichEditor的fontSize属性的返回值单位变更](changelogs-for-all-apps-b031.md#richeditor的fontsize属性的返回值单位变更) | HarmonyOS NEXT Developer Beta2 |
| ArkUI | [文本计算接口fontSize参数默认单位实现修正](changelogs-for-all-apps-b031.md#文本计算接口fontsize参数默认单位实现修正) | HarmonyOS NEXT Developer Beta2 |
| Media Library Kit | [@ohos.multimedia.medialibrary变更](changelogs-for-all-apps-b031.md#ohosmultimediamedialibrary变更) | HarmonyOS NEXT Developer Beta2 |
| 公共能力 | [开发态下代码签名强制管控策略变更](changelogs-for-all-apps-b031.md#开发态下代码签名强制管控策略变更) | HarmonyOS NEXT Developer Beta2 |

## 针对API 12应用的变更

| Kit | 变更描述 | 历史工程适配建议 | 变更引入版本 |
| --- | --- | --- | --- |
| ArkUI | [Navigation嵌套使用时的生命周期行为优化](changelogs-targeting-api12-b071.md#navigation嵌套使用时的生命周期行为优化) | 建议适配 | HarmonyOS NEXT Release |
| Ability | [禁止BackupExtensionAbility进程拉起启动框架](changelogs-targeting-api12-b065.md#禁止backupextensionability进程拉起启动框架)  \* 该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。 | 必须适配 | HarmonyOS NEXT Beta |
| ArkTS | [StringDecoder中特定场景下解码错误数据行为变更](changelogs-targeting-api12-b065.md#stringdecoder中特定场景下解码错误数据行为变更) | 必须适配 | HarmonyOS NEXT Beta |
| ArkUI | [状态管理V2版本组件内的@Local,@Param,@Event,@Provider,@Consumer,@BuilderParam,必须声明类型](changelogs-targeting-api12-b065.md#状态管理v2版本组件内的localparameventproviderconsumerbuilderparam必须声明类型) | 必须适配 | HarmonyOS NEXT Beta |
| ArkUI | [修复C-API场景下NODE\_TIME\_PICKER\_DISAPPEAR\_TEXT\_STYLE的get接口的错误行为](changelogs-targeting-api12-b065.md#修复c-api场景下node_time_picker_disappear_text_style的get接口的错误行为) | 必须适配 | HarmonyOS NEXT Beta |
| ArkUI | [component3d获取资源的路径格式由Resource类型变更到ResourceStr类型](changelogs-targeting-api12-b065.md#component3d获取资源的路径格式由resource类型不兼容变更到resourcestr类型) | 必须适配 | HarmonyOS NEXT Beta |
| ArkWeb | [CustomDialog内嵌Web组件软键盘避让方式由改变Web高度避让软键盘变更为抬升CustomDialog避让软键盘](changelogs-targeting-api12-b065.md#customdialog内嵌web组件软键盘避让方式由改变web高度避让软键盘变更为抬升customdialog避让软键盘) | 建议适配 | HarmonyOS NEXT Beta |
| Crypto Architecture Kit | [通用密钥库SystemCapability变更](changelogs-targeting-api12-b065.md#通用密钥库systemcapability变更)  \* 该变更在9月12日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.806。 | 必须适配 | HarmonyOS NEXT Beta |
| Crypto Architecture Kit | [@ohos.security.cryptoFramework 接口SysCap变更](changelogs-targeting-api12-b065.md#ohossecuritycryptoframework-接口syscap变更)  \* 该变更在9月12日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.806。 | 必须适配 | HarmonyOS NEXT Beta |
| IME Kit | [系统增加对基础访问模式输入法的管控](changelogs-targeting-api12-b065.md#系统增加对基础访问模式输入法的管控) | 必须适配 | HarmonyOS NEXT Beta |
| ArkData | [RelationalStore execute，executeSync接口执行不合法SQL语句错误码变更](changelogs-targeting-api12-b060.md#relationalstore-executeexecutesync接口执行不合法sql语句错误码变更) | 必须适配 | HarmonyOS NEXT Developer Beta5 |
| ArkTS | [xml.XmlPullParser.parse接口解析实体引用事件的行为变更](changelogs-targeting-api12-b060.md#xmlxmlpullparserparse接口解析实体引用事件的行为变更) | 建议适配 | HarmonyOS NEXT Developer Beta5 |
| ArkUI | [FrameNode的isModifiable值为false时，无法通过addComponentContent挂载节点](changelogs-targeting-api12-b060.md#framenode的ismodifiable值为false时无法通过addcomponentcontent挂载节点) | 建议适配 | HarmonyOS NEXT Developer Beta5 |
| Device Security Kit | [可信应用服务接口增加端云认证服务开通检测](changelogs-targeting-api12-b060.md#可信应用服务接口增加端云认证服务开通检测) | 必须适配 | HarmonyOS NEXT Developer Beta5 |
| ArkTS | [JSON.parse解析非法字符串行为变更](changelogs-targeting-api12-b035.md#jsonparse解析非法字符串行为变更) | 必须适配 | HarmonyOS NEXT Developer Beta3 |
| ArkTS | [JSON.parse解析浮点数下溢或-0行为变更](changelogs-targeting-api12-b035.md#jsonparse解析浮点数下溢或-0行为变更) | 必须适配 | HarmonyOS NEXT Developer Beta3 |
| ArkTS | [Sendable及共享模块语法规则编译检查完善](changelogs-targeting-api12-b035.md#sendable及共享模块语法规则编译检查完善) | 必须适配 | HarmonyOS NEXT Developer Beta3 |
| ArkUI | [命令式渲染节点RenderNode属性clipToFrame行为变更](changelogs-targeting-api12-b035.md#命令式渲染节点rendernode属性cliptoframe行为变更) | 建议适配 | HarmonyOS NEXT Developer Beta3 |
| ArkUI | [使用局部@Builder方法引用传参时，使用bind(this)后，状态管理的父子关系和组件的父子关系不一致，比如使用@ohos.arkui.advanced.ChipGroup高级组件崩溃解决方法](changelogs-targeting-api12-b035.md#使用局部builder方法引用传参时使用bindthis后状态管理的父子关系和组件的父子关系不一致比如使用ohosarkuiadvancedchipgroup高级组件崩溃解决方法) | 必须适配 | HarmonyOS NEXT Developer Beta3 |
| ArkUI | [RichEditor设置预设样式的接口传入默认值时，文本样式效果变更](changelogs-targeting-api12-b035.md#richeditor设置预设样式的接口传入默认值时文本样式效果变更) | 建议适配 | HarmonyOS NEXT Developer Beta3 |
| ArkUI | [RichEditor占位文本接口中文本样式属性传入异常值/默认值时，占位文本样式的效果变更](changelogs-targeting-api12-b035.md#richeditor占位文本接口中文本样式属性传入异常值默认值时占位文本样式的效果变更) | 建议适配 | HarmonyOS NEXT Developer Beta3 |
| ArkUI | [自定义MenuItem的onChange触发逻辑变更](changelogs-targeting-api12-b035.md#自定义menuitem的onchange触发逻辑变更) | 建议适配 | HarmonyOS NEXT Developer Beta3 |
| ArkUI | [Repeat设置totalCount属性行为变更](changelogs-targeting-api12-b035.md#repeat设置totalcount属性行为变更) | 建议适配 | HarmonyOS NEXT Developer Beta3 |
| ArkUI | [Refresh组件promptText参数设置为undefined时清空文本内容](changelogs-targeting-api12-b035.md#refresh组件prompttext参数设置为undefined时清空文本内容) | 建议适配 | HarmonyOS NEXT Developer Beta3 |
| ArkWeb | [onBeforeUnload接口行为变更](changelogs-targeting-api12-b035.md#onbeforeunload接口行为变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| Ability Kit | [restartApp接口变更](changelogs-targeting-api12-b031.md#restartapp接口变更) | 建议适配 | HarmonyOS NEXT Developer Beta2 |
| ArkData | [ValueType增加类型](changelogs-targeting-api12-b031.md#valuetype增加类型) | 建议适配 | HarmonyOS NEXT Developer Beta2 |
| ArkTS | [Sendable容器TypedArray提供的map方法的回调函数声明变更](changelogs-targeting-api12-b031.md#sendable容器typedarray提供的map方法的回调函数声明变更) | 必须适配 | HarmonyOS NEXT Developer Beta2 |
| ArkTS | [Sendable语法规则编译检查完善](changelogs-targeting-api12-b031.md#sendable语法规则编译检查完善) | 必须适配 | HarmonyOS NEXT Developer Beta2 |
| ArkTS | [Sendable赋值语法规则编译检查完善](changelogs-targeting-api12-b031.md#sendable赋值语法规则编译检查完善) | 必须适配 | HarmonyOS NEXT Developer Beta2 |
| ArkUI | [按下鼠标任意按键移动鼠标情况下不再上报鼠标事件的行为变更](changelogs-targeting-api12-b031.md#按下鼠标任意按键移动鼠标情况下不再上报鼠标事件的行为变更) | 建议适配 | HarmonyOS NEXT Developer Beta2 |
| ArkUI | [构造@ComponentV2修饰的自定义组件时，增加对常规变量的构造赋值校验](changelogs-targeting-api12-b031.md#构造componentv2修饰的自定义组件时增加对常规变量的构造赋值校验) | 必须适配 | HarmonyOS NEXT Developer Beta2 |
| ArkUI | [@ohos.arkui.advanced.SubHeader删除SymbolRenderingStrategy和SymbolEffectStrategy](changelogs-targeting-api12-b031.md#ohosarkuiadvancedsubheader删除symbolrenderingstrategy和symboleffectstrategy) | 必须适配 | HarmonyOS NEXT Developer Beta2 |
| ArkUI | [setWindowSystemBarEnable、setSystemBarEnable不在2in1设备生效](changelogs-targeting-api12-b031.md#setwindowsystembarenablesetsystembarenable不在2in1设备生效) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| User Authentication Kit | [@ohos.useriam.userAuthIcon导出命名变更](changelogs-targeting-api12-b031.md#ohosuseriamuserauthicon导出命名变更) | 必须适配 | HarmonyOS NEXT Developer Beta2 |

## UX样式或效果的变更

| 变更描述 | 历史工程适配建议 | 变更引入版本 |
| --- | --- | --- |
| [showToast接口TOP\_MOST模式行为变更](changelogs-ux-b071.md#showtoast接口top_most模式行为变更) | 建议适配 | HarmonyOS NEXT Release |
| [模态UIExtension创建默认行为变更](changelogs-ux-b071.md#模态uiextension创建默认行为变更) | 建议适配 | HarmonyOS NEXT Release |
| [安全控件offset属性设置行为变更](changelogs-ux-b071.md#安全控件offset属性设置行为变更)  \* 该变更在10月17日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.906。 | 建议适配 | HarmonyOS NEXT Release |
| [移动窗口布局模式瀑布流行为变更](changelogs-ux-b060.md#移动窗口布局模式瀑布流行为变更) | 无需适配 | HarmonyOS NEXT Developer Beta5 |
| [滚动类组件默认最大抛划限速变更](changelogs-ux-b060.md#滚动类组件默认最大抛划限速变更) | 无需适配 | HarmonyOS NEXT Developer Beta5 |
| [RichEditor收起键盘后，选中区状态变更](changelogs-ux-b060.md#richeditor收起键盘后选中区状态变更) | 无需适配 | HarmonyOS NEXT Developer Beta5 |
| [Toast弹窗UX样式变更](changelogs-ux-b060.md#toast弹窗ux样式变更) | 建议适配 | HarmonyOS NEXT Developer Beta5 |
| [安全控件宽度设定默认行为变更](changelogs-ux-b060.md#安全控件宽度设定默认行为变更) | 无需适配 | HarmonyOS NEXT Developer Beta5 |
| [bindContentCover动效参数变更](changelogs-ux-b035.md#bindcontentcover动效参数变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [DatePickerDialog显示时间时分割线延长](changelogs-ux-b035.md#datepickerdialog显示时间时分割线延长) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [子窗显示的Toast不响应返回事件](changelogs-ux-b035.md#子窗显示的toast不响应返回事件) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [带按钮的气泡样式变更](changelogs-ux-b035.md#带按钮的气泡样式变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [半模态挡位内容经过开发者动态改变后，挡位索引默认为0](changelogs-ux-b035.md#半模态挡位内容经过开发者动态改变后挡位索引默认为0) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [Toast样式变更](changelogs-ux-b035.md#toast样式变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [高级组件ComposeListItem右边按钮OperateItem类型为arrow或者arrow+text时，在没有配置action的时候，不需要单独响应点击效果，应显示全局的按压效果](changelogs-ux-b035.md#高级组件composelistitem右边按钮operateitem类型为arrow或者arrowtext时在没有配置action的时候不需要单独响应点击效果应显示全局的按压效果) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [Navigation分割线触摸直接响应](changelogs-ux-b035.md#navigation分割线触摸直接响应) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [BindContextMenu上下文菜单内容可滚动时快滑不再关闭菜单](changelogs-ux-b035.md#bindcontextmenu上下文菜单内容可滚动时快滑不再关闭菜单) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [Menu组件箭头离宿主节点默认安全边距变更](changelogs-ux-b035.md#menu组件箭头离宿主节点默认安全边距变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [MenuItemGroup嵌套MenuItem且MenuItem设置margin top或者bottom时，布局效果变更](changelogs-ux-b035.md#menuitemgroup嵌套menuitem且menuitem设置margin-top或者bottom时布局效果变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [Menu中MenuItem全部设置margin后，左右边距布局效果变更](changelogs-ux-b035.md#menu中menuitem全部设置margin后左右边距布局效果变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [菜单避让手机挖孔变更](changelogs-ux-b035.md#菜单避让手机挖孔变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [TimePickerDialog标题高度变更](changelogs-ux-b035.md#timepickerdialog标题高度变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [SubMenu避让底部导航条距离变更](changelogs-ux-b035.md#submenu避让底部导航条距离变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [MenuItem组件禁用状态下字体颜色变更](changelogs-ux-b035.md#menuitem组件禁用状态下字体颜色变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [Menu、Toast修改阴影参数](changelogs-ux-b035.md#menutoast修改阴影参数) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [Scroll、List、Grid、WaterFlow组件scrollBarColor接口变更](changelogs-ux-b035.md#scrolllistgridwaterflow组件scrollbarcolor接口变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [手机横屏及其他设备，上下文菜单placement变更](changelogs-ux-b035.md#手机横屏及其他设备上下文菜单placement变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [Toggle/Switch按压反馈样式变更](changelogs-ux-b035.md#toggleswitch按压反馈样式变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [Tabs组件的页签可滚动且为非子页签样式时增加页签默认切换动效](changelogs-ux-b035.md#tabs组件的页签可滚动且为非子页签样式时增加页签默认切换动效) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [Popup（气泡组件）UX样式变更](changelogs-ux-b035.md#popup气泡组件ux样式变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [Contextmenu组件hoverScale接口过渡动效默认行为变更](changelogs-ux-b035.md#contextmenu组件hoverscale接口过渡动效默认行为变更) | 无需适配 | HarmonyOS NEXT Developer Beta3 |
| [TextInput、TextArea 设置TextAlign.Center且显示PlaceHolder文字时，光标位置的变更](changelogs-ux-b031.md#textinputtextarea-设置textaligncenter且显示placeholder文字时光标位置的变更) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [bindSheet半模态组件横屏支持设置档位与高度](changelogs-ux-b031.md#bindsheet半模态组件横屏支持设置档位与高度) | 建议适配 | HarmonyOS NEXT Developer Beta2 |
| [bindSheet支持嵌套滚动](changelogs-ux-b031.md#bindsheet支持嵌套滚动) | 建议适配 | HarmonyOS NEXT Developer Beta2 |
| [ListItem横滑跟手比变更](changelogs-ux-b031.md#listitem横滑跟手比变更) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [DrawableDescriptor显示效果](changelogs-ux-b031.md#drawabledescriptor显示效果) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [TimePickerDialog、DatePickerDialog支持设置前导零](changelogs-ux-b031.md#timepickerdialogdatepickerdialog支持设置前导零) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [AlphabetIndexer组件popupPosition属性设置为undefined时重置为默认值](changelogs-ux-b031.md#alphabetindexer组件popupposition属性设置为undefined时重置为默认值) | 建议适配 | HarmonyOS NEXT Developer Beta2 |
| [bindContentCover动效参数变更](changelogs-ux-b031.md#bindcontentcover动效参数变更) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [RichEditor长按交互调整](changelogs-ux-b031.md#richeditor长按交互调整) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [滚动类组件（List、Grid、WaterFlow、Scroll）Friction接口默认值变更](changelogs-ux-b031.md#滚动类组件listgridwaterflowscrollfriction接口默认值变更) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [ListItem卡片样式行为变更](changelogs-ux-b031.md#listitem卡片样式行为变更) | 建议适配 | HarmonyOS NEXT Developer Beta2 |
| [List的constraintSize设置生效](changelogs-ux-b031.md#list的constraintsize设置生效) | 建议适配 | HarmonyOS NEXT Developer Beta2 |
| [AlphabetIndexer组件autoCollapse属性默认值由false改为true](changelogs-ux-b031.md#alphabetindexer组件autocollapse属性默认值由false改为true) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [光标默认样式变更](changelogs-ux-b031.md#光标默认样式变更) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [高级组件SelectionMenu默认样式变更](changelogs-ux-b031.md#高级组件selectionmenu默认样式变更) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [SVG根节点视窗外图片内容裁剪](changelogs-ux-b031.md#svg根节点视窗外图片内容裁剪) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [Symbol系统资源变更](changelogs-ux-b031.md#symbol系统资源变更) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
| [安全控件的背景板变更](changelogs-ux-b031.md#安全控件的背景板变更) | 无需适配 | HarmonyOS NEXT Developer Beta2 |
