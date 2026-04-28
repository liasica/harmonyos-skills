---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-5031
title: OS平台API行为的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.3(15) > OS平台能力 > OS平台行为变更说明 > HarmonyOS 5.0.3(15) Beta1引入的行为变更 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:31+08:00
doc_updated_at: 2026-01-16
content_hash: sha256:7bc3fe77ddb97a323486d0cbd215daa1009e83fbdf39c34c2776a3c8539fcb65
---

## Ability

### installSource字段规格变更

**变更原因**

规格变更，支持开发者判断应用是否是预置应用。

**变更影响**

此变更不涉及应用适配。

变更前：

installSource会因为应用更新而改变。

变更前installSource取值范围：

* pre-installed表示应用为第一次开机时安装的预置应用。
* 安装来源的格式为包名表示应用由此包名对应的应用安装。
* unknown表示应用安装来源未知。

变更后：

installSource不会因为应用更新而改变。

变更后installSource取值范围：

* pre-installed表示应用为第一次开机时安装的预置应用。
* ota表示应用为系统升级时新增的预置应用。
* recovery表示卸载后再恢复的预置应用。
* 安装来源的格式为包名表示应用由此包名对应的应用安装。
* unknown表示应用安装来源未知。

例如：预置应用的installSource为pre-installed，应用市场更新此预置应用。变更前installSource变为应用市场包名，变更后此应用的installSource还是pre-installed。

**起始API Level**

12

**变更的接口/组件**

ApplicationInfo中的installSource字段。

**适配指导**

预置应用开发者需根据变更后的规格适配，可根据[ApplicationInfo](../harmonyos-references/js-apis-bundlemanager-applicationinfo.md)中的installSource字段判断应用是否是预置应用。

## AppGallery Kit

### kit.StoreKit.d.ts文件废弃，替换为kit.AppGalleryKit.d.ts文件

**变更原因**

命名优化

**变更影响**

此变更涉及应用适配。

应用导入依赖时，强烈建议使用更名后的kit，即kit.AppGalleryKit。如继续使用kit.StoreKit，可能会在后续版本出现错误。

**起始API Level**

11

**变更的接口/组件**

变更前：kit.StoreKit.d.ts文件

变更后：kit.AppGalleryKit.d.ts文件

**适配指导**

以导入moduleInstallManager为例，导入moduleInstallManager时，需要使用新的kit文件，其他代码不需要修改：

变更前：import { moduleInstallManager } from '@kit.StoreKit';

变更后：import { moduleInstallManager } from '@kit.AppGalleryKit';

## ArkTS

### 信号处理方法注册接口sigaction支持SA\_RESETHAND标志位变更

**变更原因**

sigaction是由C库提供的用于注册信号处理方法的接口，开发者可通过调用此接口,指定应用在接收到特定信号时采取的处理方式。

本次变更是对齐[POSIX标准](https://pubs.opengroup.org/onlinepubs/007904875/functions/sigaction.html)，信号处理方法注册接口sigaction支持SA\_RESETHAND标志位。

**变更影响**

此变更涉及应用适配。

若应用调用sigaction接口设置信号处理方法时，未指定SA\_RESETHAND标志位，则变更前后无影响。

若应用设置信号处理方法时，指定了SA\_RESETHAND标志位，则变更前后存在如下差异：

变更前：sigaction接口未支持SA\_RESETHAND标志位，应用每次收到信号，均会执行其注册的信号处理方法。

变更后：sigaction接口支持SA\_RESETHAND标志位，应用首次收到信号会执行其注册的信号处理方法，其后根据POSIX标准，处理方法被重置为默认值

SIG\_DFL，后续收到信号会按照内核默认方式处理。内核默认处理方式与信号编号有关，包括忽略信号、终止进程、终止进程并生成转储文件，若误用了SA\_RESETHAND标志位，在本次变更后，可能会导致应用退出，请开发者务必重视排查。

**起始API Level**

11

**变更的接口/组件**

musl/signal.h中sigaction接口

**适配指导**

1. 全局搜索sigaction接口调用，查看设置信号处理方法相关代码。
2. 排查入参sigaction结构体中sa\_flags中是否指定了SA\_RESETHAND标志位(SA\_RESETHAND是POSIX标准名字，SA\_ONESHOT是过时的非标准名字，二者作用一致)。
3. 若应用的预期是信号处理方法只生效一次，需要显式指定SA\_RESETHAND标志位，若应用预期信号处理方法多次生效，则移除SA\_RESETHAND标志位，避免该标志位使能后信号处理方法恢复为默认值SIG\_DFL，对应用造成闪退影响。
4. 在调用sigaction方法前，请按需设置sa\_flags标志位，避免未初始化的随机值(可能包含SA\_RESETHAND标志位)产生应用预期外的行为。

示例代码：

```
1. // 情况一：若应用预期是信号处理方法注册后只生效一次，其后恢复为默认值SIG_DFL，需要显式指定SA_RESETHAND标志位
2. struct sigaction sa;

4. // 请重点排查sigaction结构体的sa_flags标志位，该示例中显式指定SA_RESETHAND标志位，此处可根据业务需要，合理添加其它标志位
5. sa.sa.sa_flags = SA_RESETHAND;
6. sa.sa_handler = func;
7. ret = sigaction(SIGUSR1, &sa, NULL);
8. if (ret < 0) {
9. perror("sigaction error");
10. return -1;
11. }

13. //情况二：若应用预期是信号处理方法注册后持续生效，则sa_flags不允许包含SA_RESETHAND标志位
14. struct sigaction sa;

16. // 请重点排查sigaction结构体的sa_flags标志位，确保不包含SA_RESETHAND标志位，此处可根据业务需要，合理添加其它标志位，此处示例为0
17. sa.sa_flags = 0
18. sa.sa_handler = func;
19. ret = sigaction(SIGUSR1, &sa, NULL);
20. if (ret < 0) {
21. perror("sigaction error");
22. return -1;
23. }
```

## ArkUI

### FrameNode被UINode包裹时isVisible接口返回值发生变更

**变更原因**

用户使用FrameNode的isVisible接口时，节点会依次向上层父节点查询可见性，如果父节点不可见，子节点也不可见。但如果子节点被UINode类型节点（如IfElse、ForEach、LazyForEach等）包裹，则向上查找过程被阻塞，无法继续查询父节点可见性。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.3(15)时生效。

变更前：父节点设为不可见、子节点设为可见时，如果子节点和父节点之间存在UINode类型节点，子节点调用isVisible结果为true。

变更后：父节点设为不可见、子节点设为可见时，如果子节点和父节点之间存在UINode类型节点，子节点调用isVisible结果为false。

父节点设为不可见、子节点设为可见时，如果子节点和父节点之间存在UINode类型节点，调用isVisible接口返回值结果变更前后会不一致，例如：

```
1. import { FrameNode } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct Index {
6. private stackNode: FrameNode | null = null
7. private columnNode: FrameNode | null = null

9. build() {
10. Column() {
11. Stack() {
12. if (true) {
13. Column()
14. .id("column")
15. .visibility(Visibility.Visible)
16. }
17. }
18. .id("stack")
19. .visibility(Visibility.Hidden)

21. Button("print")
22. .onClick(() => {
23. this.stackNode = this.getUIContext().getFrameNodeById("stack")
24. this.columnNode = this.getUIContext().getFrameNodeById("column")
25. if (this.stackNode) {
26. // Stack节点的可见性，为false
27. console.log("stackNode.isVisible:", this.stackNode.isVisible())
28. }
29. if (this.columnNode) {
30. // Column节点的可见性，变更前为true，变更后为false
31. console.log("columnNode.isVisible:", this.columnNode.isVisible())
32. }
33. })
34. }
35. }
36. }
```

**起始API Level**

12

**变更的接口/组件**

FrameNode.d.ts文件isVisible接口。

**适配指导**

默认行为变更，但开发者需审视此变更是否对自身相关业务代码逻辑产生影响，若有影响需根据自身业务代码进行对应适配。

### 富文本组件RichEditor的onCopy回调中设置preventDefault()时的行为变更

**变更原因**

在富文本组件RichEditor的onCopy回调中，当调用preventDefault()时，复制操作完成后，选中区消失。这导致了一个接口同时管理了复制功能和选中区关闭这两个相互独立的行为。

**变更影响**

此变更不涉及应用适配。

变更前：富文本组件RichEditor的onCopy回调中设置preventDefault()时，复制之后选中区消失，触发OnSelectionChange回调。

变更后：富文本组件RichEditor的onCopy回调中设置preventDefault()时，复制之后选中区不消失，不触发OnSelectionChange回调。

**起始API Level**

12

**变更的接口/组件**

富文本组件RichEditor

**适配指导**

默认行为变更，应注意变更后的行为是否对整体应用逻辑产生影响。

## AVCodec Kit

### OH\_AVCodecOnStreamChanged在音频解码场景的默认行为变更

**变更原因**

音频解码存在采样率等参数发生变化的场景，需要回调通知调用者。

**变更影响**

此变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.3(15)时生效。

变更前：应用通过OH\_AudioCodec\_RegisterCallback注册了OH\_AVCodecOnStreamChanged回调，音频解码发生采样率、声道数等格式变化时，未触发该回调。

变更后：应用通过OH\_AudioCodec\_RegisterCallback注册了OH\_AVCodecOnStreamChanged回调，音频解码发生采样率、声道数等格式变化时，会触发该回调。

**起始API Level**

9

**变更的接口/组件**

native\_avcodec\_audiocodec.h 下的接口OH\_AudioCodec\_RegisterCallback注册的native\_avcodec\_base.h 下的OH\_AVCodecOnStreamChanged。

**适配指导**

默认行为变更，无需适配。

## Localization Kit

### 变更缅甸文，马来文和泰文的显示名称

**变更原因**

缅甸文，马来文和泰文显示名称错误。

**变更影响**

该变更不涉及应用适配。

变更前：如设置和开机向导中，缅甸文显示名称为မြန်မာ，马来文显示名称Melayu，泰文显示名称为ไทย。

变更后：如设置和开机向导中，缅甸文显示名称为မြန်မာစာ，马来文显示名称为Bahasa Melayu，泰文显示名称为ภาษาไทย。

**起始API Level**

9

**变更的接口/组件**

i18n.System.getDisplayLanguage

**适配指导**

无需对接口返回值做特殊判断，仅用于界面显示。

## Media Kit

### 系统录屏应用调用的截屏接口变更

**变更原因**

系统录屏在结束时会调用窗口模块提供的截屏API，生成屏幕缩略图，此时会返回一个截屏事件。多个三方应用通过窗口模块订阅了屏幕截屏事件，系统录屏产生的截屏事件会对三方应用的监听造成干扰。

为了提升用户体验，让系统录屏的截屏事件不对用户产生影响，窗口模块新增一个system类型的截屏API供系统录屏使用。系统录屏使用新接口，三方应用不会再捕获到系统录屏的截屏事件。

**变更影响**

此变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.3(15)时生效。

变更前：录屏结束时，监听截屏事件的应用会收到回调事件。

变更后：录屏结束时，监听截屏事件的应用不会收到回调事件。

**起始API Level**

9

**变更的接口/组件**

无变更接口

**适配指导**

默认行为变更，无需适配。

## 应用配置文件

### supportWindowMode选项配置fullscreen和split时，窗口全屏启动

**变更原因**

PC/2in1设备上，在module.json5的[supportWindowMode](../harmonyos-guides/module-configuration-file.md#abilities标签)属性配置fullscreen和split时，或在startOptions的[supportWindowModes](../harmonyos-references/js-apis-app-ability-startoptions.md#startoptions)属性配置FULL\_SCREEN和SPLIT时，窗口将以自由窗口状态启动，与预期效果不符。

**变更影响**

该变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.0.3(15)时生效。

变更前：module.json5的supportWindowMode属性配置fullscreen和split时，或在startOptions的supportWindowModes属性配置FULL\_SCREEN和SPLIT时，PC/2in1设备上以自由窗口启动。

变更后：module.json5的supportWindowMode属性配置fullscreen和split时，或在startOptions的supportWindowModes属性配置FULL\_SCREEN和SPLIT时，PC/2in1设备上窗口全屏启动。

**起始API Level**

9

**变更的接口/组件**

module.json5的supportWindowMode属性从API version 9开始支持。

startOptions的supportWindowModes属性从API version 14开始支持。

**适配指导**

API version 15及之后的版本, 开发者需要关注在module.json5的supportWindowMode属性配置fullscreen和split时或startOptions的supportWindowModes属性配置FULL\_SCREEN和SPLIT时，2in1设备上窗口全屏启动。

若预期是以自由窗口启动，则需要在module.json5的supportWindowMode属性配置增加floating配置项或startOptions的supportWindowModes属性中增加FLOATING配置项。

## 调试工具

### hilog日志在商用版本（nolog版本）开发者模式下默认日志级别由info变为warning

**变更原因**

hilog目前商用版本在打开开发者模式时日志级别设置为Info，为加强日志落盘安全性及提高性能，默认日志级别修改Warning。

**变更影响**

此变更不涉及应用适配。

变更前行为：hilog 商用版本在打开开发者模式时日志级别设置为Info。

变更后行为：hilog 商用版本在打开开发者模式时日志级别设置为Warning。

**起始API Level**

9

**变更的接口/组件**

不涉及接口/组件变更。

**适配指导**

行为变更：默认行为变更，无需适配，但应注意变更后的行为是否对整体应用逻辑产生影响。

针对本文所述变更，适配命令为：hdc shell hilog -b I；

执行该命令后，可以将允许打印的日志级别恢复至变更前，即能够打印INFO及以上级别的日志。

日志级别从低到高：DEBUG < INFO < WARN < ERROR < FATAL。

具体可参考：[hilog查看和设置日志级别](../harmonyos-guides/hilog.md#查看和设置日志级别)

说明

商用版本（nolog版本）确认方法：

查看设置->关于本机->软件版本，版本号最末尾不包含log。

如：BRA-AL00 5.0.0.36(C00E15R4P92DEVUlog)不是商用版本，BRA-AL00 5.0.0.36(C00E15R4P92DEVU)是商用版本。
