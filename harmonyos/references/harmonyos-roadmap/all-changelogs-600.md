---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-roadmap/all-changelogs-600
title: 6.0.0(20)的行为变更汇总
breadcrumb: 变更预告 > 变更预告 > 6.0.0(20)的行为变更汇总
category: harmonyos-roadmap
scraped_at: 2026-09-02T14:55:01+08:00
doc_updated_at: 2026-08-04
content_hash: sha256:c19b9666e8ccbf240e8c5d660052a3b81fe6d36a721443ab27832ef2a9fc649f
---

## OS平台API行为的变更

| Kit | 变更描述 | 变更引入版本 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- |
| Ability Kit | [AbilityDelegator.startAbility()接口错误码变更](../harmonyos-releases/changelogs-for-all-apps-6001.md#section284) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| [借助Want进行文件分享时擦除不合法的URI](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025041851851) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| ArkTS | [通过字面量定义的数组在删除元素后再使用该字面量定义数组时数组内容异常](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025042210344) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | 全部生效 |
| ArkUI | [GridRow组件columns参数和GridCol组件span参数默认值变更](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025040702131) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| [width和height支持的matchParent接口规格变更](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025040275645) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| [文本与输入、信息展示、按钮与选择、滚动与滑动、图形绘制组件接口支持Resource类型](../harmonyos-releases/changelogs-for-all-apps-6001.md#section383) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | 全部生效 |
| [UI Input相关NDK接口行为变更](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025040107071) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| [使用字面量初始化CustomDialogController类实例导致的编译行为变更](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025071721132) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| ArkWeb | [ArkWeb基于上游社区的Chromium内核从114升级为132版本](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025050804757) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | 全部生效 |
| Connectivity Kit | [蓝牙BLE接口错误码变更](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025040175433) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| Core File Kit | [@ohos.file.fs.d.ts中copy接口在拷贝后，对目标文件原有数据处理方式发生变更](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025040165962) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| Driver Development Kit | [SendPipeRequest和SendPipeRequestWithAshmem传入错误参数时，返回值由USB\_DDK\_SUCCESS变更为USB\_DDK\_INVALID\_PARAMETER](../harmonyos-releases/changelogs-for-all-apps-6001.md#section336) | 6.0.0(20) Beta1 | 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| Image Kit | [ImageInfo对象mimeType返回值变更](../harmonyos-releases/changelogs-for-all-apps-6001.md#section406) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| Media Kit | [播放器所使用的内存归属变更](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025040590071) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| User Authentication Kit | [@ohos.useriam.userAuth限制应用从后台发起带交互界面的身份认证变更](../harmonyos-releases/changelogs-for-all-apps-6001.md#section390) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | 全部生效 |
| 其他 | [mincore接口功能补齐至与Linux一致](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025033190005) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | 全部生效 |
| [ptrace syscall操作未被停住的线程由返回0改为返回ESRCH.1](../harmonyos-releases/changelogs-for-all-apps-6001.md#section170) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | 全部生效 |
| [限制ptrace接口仅可在开发者调试模式下使用](../harmonyos-releases/changelogs-for-all-apps-6001.md#ch2025040675033) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | 全部生效 |
| Ability Kit | [Ability Kit相关公共事件行为变更，增加管控](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025051312838) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 全部生效 |
| ArkTS | [TreeSet/TreeMap扩容导致比较器丢失问题正向修复](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025062036364) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| ArkUI | [位置控件功能变更](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025051227329) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 全部生效 |
| [通用属性drawModifier接口行为变更](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025061956154) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 全部生效 |
| [半模态SIDE侧边样式新增避让软键盘能力](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025061805350) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 全部生效 |
| [CanvasRenderer的font接口支持自定义字体行为变更](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025062517095) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 全部生效 |
| [去除保存控件系统提示弹框变更](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025070747763) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 6.0.0(20) Beta1新增接口，仅对使用6.0.0(20) Beta1开发的应用生效 |
| Basic Services Kit | [zlib.unzipFile和zlib.decompressFile解压文件接口变更](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025061279339) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 全部生效 |
| Data Augmentation Kit | [retrieval.VectorQuery接口value字段变更为可选](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025070161508) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 6.0.0(20) Beta1新增接口，仅对使用6.0.0(20) Beta1开发的应用生效 |
| Localization Kit | [泰国、沙特阿拉伯、阿富汗和伊朗的默认历法变更](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025063039411) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 全部生效 |
| NDK开发 | [libc++ condition\_variable::wait\_for接口变更](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025062308656) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 全部生效 |
| Share Kit | [on('dataReceive')接口新增必填参数capabilities](../harmonyos-releases/changelogs-for-all-apps-6002.md#ch2025071525869) | 6.0.0(20) Beta2 | phone, tablet, 2in1 | 6.0.0(20) Beta1新增接口，仅对使用6.0.0(20) Beta1开发的应用生效 |
| Car Kit | [Car Kit接口新增801、1003810001、1003810002错误码](../harmonyos-releases/changelogs-for-all-apps-6003.md#ch2025082874213) | 6.0.0(20) Beta3 | phone, tablet, 2in1 | 全部生效 |
| Data Augmentation Kit | [rag.streamRun接口思考过程输出变更](../harmonyos-releases/changelogs-for-all-apps-6003.md#ch2025080515191) | 6.0.0(20) Beta3 | phone, tablet, 2in1 | 6.0.0(20) Beta2新增接口，仅对使用6.0.0(20) Beta2开发的应用生效 |
| Device Security Kit | [SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED、FILE\_INTERCEPTED枚举值变更](../harmonyos-releases/changelogs-for-all-apps-6003.md#ch2025072609886) | 6.0.0(20) Beta3 | phone, tablet, 2in1 | 6.0.0(20) Beta2新增接口，仅对使用6.0.0(20) Beta2开发的应用生效 |
| ArkTS | [禁止在编译产物为JS的HAR包中使用注解](../harmonyos-releases/changelogs-for-all-apps-6004.md#ch2025081914674) | 6.0.0(20) Beta5 | phone, tablet, 2in1 | 全部生效 |

## UX样式或效果的变更

| 变更描述 | 变更引入版本 | 变更影响 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- |
| [bindSheet在2in1设备中默认避让窗口安全区](../harmonyos-releases/changelogs-ux-6001.md#section393) | 6.0.0(20) Beta1 | 小 | 2in1 | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| [FullScreenLaunchComponent嵌入式运行元服务内容区避让系统安全区行为变更](../harmonyos-releases/changelogs-ux-6001.md#ch2025050666880) | 6.0.0(20) Beta1 | 小 | phone, tablet | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| [半模态跟手样式弹窗显示位置避让规则变更](../harmonyos-releases/changelogs-ux-6001.md#section395) | 6.0.0(20) Beta1 | 小 | phone, tablet | targetSdkVersion ≥ 6.0.0(20)变更生效 |
| [selectDynamicIcon接口新增错误码](../harmonyos-releases/changelogs-ux-6002.md#ch2025061689518) | 6.0.0(20) Beta2 | 小 | phone, tablet, 2in1 | 6.0.0(20) Beta1新增接口，仅对使用6.0.0(20) Beta1开发的应用生效 |

## 开发工具的变更

| 工具分类 | 变更描述 | 变更引入版本 | 影响设备类型 | 变更生效规则 |
| --- | --- | --- | --- | --- |
| DevEco Studio | [DevEco Studio底座升级，语言切换方式变更，部分插件不可使用](../harmonyos-releases/change-description-600-beta1.md#section1072421614238) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | 使用DevEco Studio 6.0.0 Beta1及以上版本时生效 |
| DevEco Studio | [ArkTS日志位置调整](../harmonyos-releases/change-description-600-beta1.md#section246452662412) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | 使用DevEco Studio 6.0.0 Beta1及以上版本时生效 |
| DevEco Studio | [ArkUI-X工程配套的gradle版本变更](../harmonyos-releases/change-description-600-beta1.md#section1348865316243) | 6.0.0(20) Beta1 | phone, tablet, 2in1 | 使用DevEco Studio 6.0.0 Beta1及以上版本时生效 |
| DevEco Studio | [hot reload不再支持箭头函数内this变量的首次新增或彻底删除](../harmonyos-releases/change-description-600-beta1.md#section1352793517268) | 6.0.0(20) Beta3 | phone, tablet, 2in1 | 使用DevEco Studio 6.0.0 Beta3及以上版本时生效 |
