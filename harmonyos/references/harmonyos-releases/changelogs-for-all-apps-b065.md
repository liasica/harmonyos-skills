---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-b065
title: 针对所有应用的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Beta引入的接口行为变更 > 针对所有应用的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:09+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:45a7bf8377bb84ef5188a893f9e6edcf19629f2f71daa9512ae0082953e9b2f0
---

## Ability Kit

### 拉起UIExtensionAbility增加调用方为前台应用的校验

**变更原因**

UIExtensionAbility仅支持拥有前台窗口的应用拉起，虽有该约束，但未校验调用方是否为前台应用，存在后台应用拉起UIExtensionAbility的风险。

**变更影响**

此变更涉及应用适配。

变更前：未对后台应用拉起UIExtensionAbility做约束限制。

变更后：后台应用不允许拉起UIExtensionAbility。

**起始API Level**

11

**变更的接口/组件**

1、UIAbilityContext.startAbilityByType、UIExtensionContentSession.startAbilityByType

2、具备拉起UIExtensionAbility能力的接口。

**适配指导**

行为变更：无需适配，变更后不允许后台应用拉起UIExtensionAbility。

### 借助Want分享文件URI时无权限的URI会被拦截

**变更原因**

在want的flags字段设置了授权flag前提下，禁止在want中的URI字段和wantConstant.Params.PARAMS\_STREAM字段中传入无权限的[File URI](../harmonyos-references-V5/js-apis-file-fileuri-V5.md#fileuri10)。

说明

有权限的File URI是指应用通过[getUriFromPath](../harmonyos-references-V5/js-apis-file-fileuri-V5.md#fileurigeturifrompath)接口将自身沙箱路径转换后的URI或持久化过的File URI。

该变更在9月12日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.806。

**变更影响**

此变更涉及应用适配。

变更前：

在want的flags字段设置了授权flag前提下，借助want实现File URI文件分享时，want中的URI字段和wantConstant.Params.PARAMS\_STREAM字段会原封不动地传递给被授权方。

变更后：

在want的flags字段设置了授权flag前提下，借助want实现file URI文件分享时want的URI字段和wantConstant.Params.PARAMS\_STREAM字段中无权限的file URI不会传递给被授权方。file URI拦截规则如下：

1. want中URI字段如果是File URI，且授权方没有该URI的权限, 则URI字段将被擦除。
2. WantConstant.Params.PARAMS\_STREAM字段中授权方无权限的File URI将被擦除。
3. want中的URI字段与WantConstant.Params.PARAMS\_STREAM字段中的File URI合并后超过500的部分将会被截断。

**起始API Level**

9

**变更的接口/组件**

不涉及

**适配指导**

默认行为变更，无需适配。

### childProcessManager增加子进程最大数量限制

**变更原因**

应用可以无限制启动子进程，这个场景存在恶意调用风险，因此需要增加子进程最大数量限制。

说明

该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。

**变更影响**

此变更涉及应用适配。

变更前：每个应用通过childProcessManager启动的子进程总数没有限制。

变更后：每个应用通过childProcessManager(非SELF\_FORK模式)启动的子进程总数上限为512个。

**起始API Level**

11

**变更的接口/组件**

childProcessManager中的startChildProcess(非SELF\_FORK模式)、startArkChildProcess接口。

**适配指导**

行为变更：无需适配，通过childProcessManager最大可以启动的子进程数量为512个，超过后无法启动。

### 包管理@ohos.bundle.bundleManager.d.ts中的bundleManager.verifyAbc接口以及bundleManager.deleteAbc接口变更为system API

**变更原因**

因安全合规要求，包管理@ohos.bundle.bundleManager.d.ts中的bundleManager.verifyAbc接口以及bundleManager.deleteAbc接口变更为system API。

说明

该变更在9月27日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.813。

**变更影响**

此变更涉及应用适配。

变更前：

包管理@ohos.bundle.bundleManager.d.ts中的bundleManager.verifyAbc接口以及bundleManager.deleteAbc接口访问级别为public API，外部开发者可以调用。

变更后：

包管理@ohos.bundle.bundleManager.d.ts中的bundleManager.verifyAbc接口以及bundleManager.deleteAbc接口访问级别变更为system API，仅供系统应用调用，外部开发者将无法调用相关接口，非系统应用调用相关接口会返回202错误。

**起始API Level**

11

**变更的接口/组件**

@ohos.bundle.bundleManager.d.ts中如下接口：

1. function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean, callback: AsyncCallback<void>): void;
2. function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean): Promise<void>;
3. function deleteAbc(abcPath: string): Promise<void>;

**适配指导**

取消对相关接口的调用，非系统应用调用相关接口会返回202错误。

### startAbility从后台发起时，即使应用正在运行长时任务，也不能调用成功。

**变更原因**

应用从后台使用startAbility拉起自己或者其他应用，这种行为是禁止的。但是利用长时任务，当前可以达到应用在后台依然startAbility成功的效果。这个场景存在恶意弹窗等风险，因此现在禁止应用在运行长时任务时，从后台调用startAbility的行为。

说明

该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。

**变更影响**

此变更涉及应用适配。

变更前：应用运行长时任务时，可以在后台调用startAbility成功。

变更后：应用运行长时任务时，在后台调用startAbility会失败。

**起始API Level**

9

**变更的接口/组件**

各个context中的startAbility接口。

**适配指导**

行为变更：无需适配，变更后即使应用正在运行长时任务，在后台调用startAbility也会失败。如工程中已使用此种行为，建议删除。

## ArkTS

### util.TextEncoder模块utf-16le和utf-16be编码数据行为变更

**变更原因**

TextEncoder编码器在编码格式设置为utf-16le和utf-16be时，获得的编码数据相反。

utf-16le为小端编码格式，编码出数据应该符合小端编码数据，但是实际表现为大端编码数据。

utf-16be为大端编码格式，编码出数据应该符合大端编码数据，但是实际表现为小端编码数据。

这两种编码格式所编码出的数据行为与标准定义不符合，需要修复此问题。

说明

该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。

**变更影响**

此变更涉及应用适配。

变更前：

utf-16le为小端编码格式，编码出数据应该符合小端编码数据，但是实际表现为大端编码数据。

utf-16be为大端编码格式，编码出数据应该符合大端编码数据，但是实际表现为小端编码数据。

变更后：

utf-16le为小端编码格式，实际表现为小端编码数据。

utf-16be为大端编码格式，实际表现为大端编码数据。

**起始API Level**

9

**变更的接口/组件**

util.TextEncoder模块的接口：

encodeInto(input?: string): Uint8Array;

encodeIntoUint8Array(input: string, dest: Uint8Array): EncodeIntoUint8ArrayInfo;

**适配指导**

变更描述： 修复TextEncoder编码器在编码格式设置为utf-16le和utf-16be时获取编码数据与定义不相符的BUG。

encodeInto接口的表现：

```
1. import { util } from '@kit.ArkTS';

3. let encoderUtf16Le = new util.TextEncoder("utf-16le");
4. let encoderUtf16Be = new util.TextEncoder("utf-16be");

6. // 变更前：
7. // let u16_le = encoderUtf16Le.encodeInto('abcdefg'); // u16_le: 0,97,0,98,0,99,0,100,0,101,0,102,0,103
8. // let u16_be = encoderUtf16Be.encodeInto('abcdefg'); // u16_be: 97,0,98,0,99,0,100,0,101,0,102,0,103,0

11. // 变更后：
12. let u16_le = encoderUtf16Le.encodeInto('abcdefg'); // u16_le: 97,0,98,0,99,0,100,0,101,0,102,0,103,0
13. let u16_be = encoderUtf16Be.encodeInto('abcdefg'); // u16_be: 0,97,0,98,0,99,0,100,0,101,0,102,0,103
```

encodeIntoUint8Array接口的表现：

```
1. import { util } from '@kit.ArkTS';

3. let encoderUtf16Le = new util.TextEncoder("utf-16le");
4. let encoderUtf16Be = new util.TextEncoder("utf-16be");

6. // 变更前：
7. // let dest_le = new Uint8Array(14);
8. // let dest_be = new Uint8Array(14);
9. // let res_le = encoderUtf16Le.encodeIntoUint8Array('abcdefg', dest_le); // dest_le: 0,97,0,98,0,99,0,100,0,101,0,102,0,103
10. // let res_be = encoderUtf16Be.encodeIntoUint8Array('abcdefg', dest_be); // dest_be: 97,0,98,0,99,0,100,0,101,0,102,0,103,0

12. // 变更后：
13. let dest_le = new Uint8Array(14);
14. let dest_be = new Uint8Array(14);
15. let res_le = encoderUtf16Le.encodeIntoUint8Array('abcdefg', dest_le); // dest_le: 97,0,98,0,99,0,100,0,101,0,102,0,103,0
16. let res_be = encoderUtf16Be.encodeIntoUint8Array('abcdefg', dest_be); // dest_be: 0,97,0,98,0,99,0,100,0,101,0,102,0,103
```

### Worker模块中RestrictedWorker的接口变更为system API

**变更原因**

因安全合规要求，RestrictedWorker的接口由public API变更为system API。

说明

该变更在9月27日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.813。

**变更影响**

此变更涉及应用适配。

变更前：

Worker模块中RestrictedWorker类中的接口访问级别为public API，外部开发者可以调用。

变更后：

Worker模块中RestrictedWorker类中的接口访问级别变更为system API，相关接口将不再对外暴露，仅供系统应用调用，外部开发者使用时会出现无法找到RestrictedWorker相关接口的编译失败问题。

**起始API Level**

11

**变更的接口/组件**

worker模块下的两个接口：

1. class RestrictedWorker extends ThreadWorker;
2. constructor(scriptURL: string, options?: WorkerOptions);

**适配指导**

如果业务场景只涉及线程间通信，可以选择使用worker.ThreadWorker类创建worker线程。

## ArkUI

### 优化状态变量场景下ForEach的冗余刷新行为

**变更原因**

开发者使用ForEach，在旧节点下树的时候会被刷新一次，属于规格外的行为，当刷新调用方法中存在对全局变量的修改时会发生异常。

说明

该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。

**变更影响**

此变更涉及应用适配。

变更前：开发者在使用ForEach时，节点下树的时候会被刷新一次。

变更后：开发者在使用ForEach时，节点下树的时候不会被刷新。

**起始API Level**

9

**变更的接口/组件**

ForEach

**适配指导**

之前使用ForEach涉及节点刷新时调用的方法存在对全局变量值修改的，需要根据具体情况对代码进行相应的修改，使当前修改等效于原来的两次修改叠加，以保证效果不变。

示例：

变更前：

```
1. let g_data = 0;

3. @Entry
4. @Component
5. struct MyComponent {
6. @State simpleList: number[] = [0, 1, 2]

8. fn(item: number, index: number) {
9. g_data++;
10. return 80;
11. }

13. build() {
14. Row() {
15. Column() {
16. Button('click button []')
17. .onClick(() => {
18. this.simpleList = [4, 5, 6]
19. })
20. ForEach(this.simpleList, (item: number, index: number) => {
21. Text(item.toString())
22. .fontSize(this.fn(item, index))
23. .onAppear(()=>{
24. console.log('g_data: ' + g_data);
25. })
26. }, (item: string) => item)
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
32. }
```

变更后：

```
1. let g_data = 0;

3. @Entry
4. @Component
5. struct MyComponent {
6. @State simpleList: number[] = [0, 1, 2]

8. fn(item: number, index: number) {
9. // 变更前总会调用两次，变更后只会调用一次，保证变更前后效果一致
10. g_data+=2;
11. return 80;
12. }

14. build() {
15. Row() {
16. Column() {
17. Button('click button []')
18. .onClick(() => {
19. this.simpleList = [4, 5, 6]
20. })
21. ForEach(this.simpleList, (item: number, index: number) => {
22. Text(item.toString())
23. .fontSize(this.fn(item, index))
24. .onAppear(()=>{
25. console.log('g_data: ' + g_data);
26. })
27. }, (item: string) => item)
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
33. }
```

## AVCodec Kit

### OH\_AVCodecBufferAttr 接口行为变更

**变更原因**

针对视频轨获取的 OH\_AVCodecBufferAttr 中 pts 属性，会在文件实际封装信息的基础上减去轨道起始时间，使其从0开始，

导致音视频轨道 pts 处理不一致，调用方依赖 pts 实现音画同步时，部分视频效果异常。

**变更影响**

此变更涉及应用适配。用户获取的视频轨 pts 属性值变更，不再统一从0开始，统一提供文件实际封装的原始 pts 信息。

**起始API Level**

10

**变更的接口/组件**

| 名称 | 描述 |
| --- | --- |
| OH\_AVCodecBufferAttr | 定义OH\_AVCodec的缓冲区描述信息 |

**适配指导**

变更后 pts 获取方式不变，内部不再进行额外处理，为文件实际封装的时间戳信息，调用方可使用变更后 pts，结合业务逻辑进行使用和处理，

获取方式如下所示：

```
1. OH_AVBuffer *buffer = OH_AVBuffer_Create(w * h * 3 >> 1);
2. if (buffer == nullptr) {
3. // 处理异常
4. }
5. int32_t ret = OH_AVDemuxer_ReadSampleBuffer(demuxer, trackIndex, buffer);
6. if (ret != AV_ERR_OK) {
7. // 处理异常
8. }

10. OH_AVCodecBufferAttr info;
11. ret = OH_AVBuffer_GetBufferAttr(buffer, &info);
12. if (ret != AV_ERR_OK) {
13. // 处理异常
14. }
15. int64_t newPts = info.pts;
```

并且从API12开始，支持获取轨道起始时间信息 OH\_MD\_KEY\_TRACK\_START\_TIME，用户也可通过变更后 pts，结合轨道起始时间，转换为变更前 pts，代码如下：

```
1. OH_AVFormat *trackFormat = OH_AVSource_GetTrackFormat(source, trackIndex);
2. if (trackFormat == nullptr) {
3. // 处理异常
4. }
5. int64_t startTime = 0;
6. if (!OH_AVFormat_GetLongValue(trackFormat, OH_MD_KEY_TRACK_START_TIME, &startTime)) {
7. // 处理异常
8. }
9. int64_t oldPts = newPts - startTime;
```

## Camera Kit

### CameraPosition.CAMERA\_POSITION\_FOLD\_INNER接口废弃

**废弃原因**

原方案采集镜头的位置信息只能满足部分产品，为了满足其他不同形态产品，需要将@ohos.multimedia.camera.d.ts文件内CameraPosition.CAMERA\_POSITION\_FOLD\_INNER接口废弃。

**废弃影响**

此变更涉及应用适配。

使用CameraPosition.CAMERA\_POSITION\_FOLD\_INNER接口会有废弃提示。需要开发者进行适配。

**起始API Level**

11

**废弃的接口/组件**

| 接口声明 | 废弃说明 | 代替接口 |
| --- | --- | --- |
| CAMERA\_POSITION\_FOLD\_INNER | 废弃 | 无替代接口 |

**适配指导**

方案1：开发者可以使用@ohos.display.d.ts模块的[display.on('foldStatusChange')](../harmonyos-references-V5/js-apis-display-V5.md#displayonfoldstatuschange10)监听折叠屏折叠状态变化，

在监听到折叠屏折叠状态变化后需要重新通过@ohos.multimedia.camera.d.ts模块的[getSupportedCameras](../harmonyos-references-V5/js-apis-camera-V5.md#getsupportedcameras)接口获取镜头信息，再按需选择要打开的镜头。

其中[display.on('foldStatusChange')](../harmonyos-references-V5/js-apis-display-V5.md#displayonfoldstatuschange10)回调返回的数据[FoldStatus](../harmonyos-references-V5/js-apis-display-V5.md#foldstatus10)为FOLD\_STATUS\_HALF\_FOLDED或者FOLD\_STATUS\_EXPANDED状态时在[getSupportedCameras](../harmonyos-references-V5/js-apis-camera-V5.md#getsupportedcameras)接口获取镜头信息是一致的。

方案2：开发者可以使用@ohos.multimedia.camera.d.ts模块的[CameraManager.on('foldStatusChange')](../harmonyos-references-V5/js-apis-camera-V5.md#onfoldstatuschange12)监听折叠屏折叠状态变化，

在监听到折叠屏折叠状态变化后会回调[FoldStatusInfo](../harmonyos-references-V5/js-apis-camera-V5.md#foldstatusinfo12)，包含了当前设备的折叠状态和当前折叠状态所支持的相机列表信息，再按需选择要打开的镜头。

## Core File Kit

### file-access-across-devices 接口行为变更

**变更原因**

分布式文件业务在检测到可信设备连接同一个Wi-Fi会自动触发建链，但该规格存在以下两个问题：

1.只适用于同Wi-Fi设备场景，不同Wi-Fi间无法建链，导致分布式文件业务无法使用。

2.自动建链功能也存在功耗开销，即使用户不使用分布式文件功能，但链路一直存在。

鉴于以上两个原因，需要在新版本上对该规格进行整改。

**变更影响**

此变更涉及应用适配。

变更前：由分布式文件业务监测同Wi-Fi可信设备并自动触发建链，应用无需主动建链，但仅适用同Wi-Fi场景。

变更后：新增主动建链接口，由应用通过主动调用接口触发建链，适用于同Wi-Fi和不同Wi-Fi的场景。

**起始API Level**

11

**变更的接口/组件**

本次变更仅涉及新增以下接口：

| 名称 | 描述 |
| --- | --- |
| connectDfs(networkId: string, listeners: DfsListeners) | 应用调用该接口主动触发建链，执行结果通过DfsListeners回调内onStatus上报。 |

**适配指导**

应用使用新接口可以同时支持用同Wi-Fi和不同Wi-Fi场景下的跨设备文件访问能力，详见[跨设备文件访问](../harmonyos-guides-V5/file-access-across-devices-V5.md)。

### setSecurityLabel接口行为变更

**变更原因**

setSecurityLabel接口未对设置的安全等级进行校验，未阻止应用将高风险等级数据设置为低风险等级，有安全风险，需要进行整改。

**变更影响**

此变更涉及应用适配。

变更前：应用数据如果已设置过等级，仍可以降低数据安全等级，调用以下代码接口可设置成功。

变更后：应用数据设置过数据风险等级后，无法降低数据风险等级，接口抛错13900020。

```
1. import {fileIo,securityLabel} from '@kit.CoreFileKit';
2. try {
3. let path = getContext().filesDir + '/text.txt';
4. let file = fileIo.openSync(path,fileIo.OpenMode.CREATE);
5. securityLabel.setSecurityLabelSync(file.path, "s4");
6. securityLabel.setSecurityLabelSync(file.path, "s3");
7. console.log( "set security label s3 success");
8. } catch (err) {
9. console.log( "set security label s3  fail, " + err.message + err.code);
10. }
```

**起始API Level**

9

**变更的接口/组件**

| 接口声明 | 变更前 | 变更后 |
| --- | --- | --- |
| setSecurityLabel(path:string, type:DataLevel):Promise<void> | 数据风险等级由高向低设置未做拦截 | 数据风险等级由高向低设置时抛错 |
| setSecurityLabel(path:string, type:DataLevel, callback: AsyncCallback<void>):void | 数据风险等级由高向低设置未做拦截 | 数据风险等级由高向低设置时抛错 |
| setSecurityLabelSync(path:string, type:DataLevel):void | 数据风险等级由高向低设置未做拦截 | 数据风险等级由高向低设置时抛错 |

**适配指导**

此修改为Bugfix，如果应用未多次设置数据风险等级，则无需适配，没有影响。

如果应用需多次设置数据风险等级，需注意设置数据风险等级应该符合安全规范，数据风险等级仅可由低向高或设置相同的等级。将高风险等级数据设置为低风险等级接口将会抛错。

### getSecurityLabel接口行为变更

**变更原因**

getSecurityLabel接口获取未对设置过的数据风险等级的数据返回值为空字符串，不符合安全设计。需要修改实现返回“s3”。

**变更影响**

此变更涉及应用适配。

变更前：使用接口获取未设置过数据风险等级标签的数据时，默认返回了空字符。运行以下代码，日志中会打印label为空字符串。

变更后：使用接口获取未设置过数据风险等级标签的数据时，默认返回“s3”。运行以下代码，日志中会打印label为“s3”。

```
1. import {fileIo,securityLabel} from '@kit.CoreFileKit';
2. try {
3. let path = getContext().filesDir + '/text.txt';
4. let file = fileIo.openSync(path,fileIo.OpenMode.CREATE);
5. let label = securityLabel.getSecurityLabelSync(file.path);
6. console.log( "get security label success, label is" + label);
7. } catch (err) {
8. console.log( "get security label fail, " + err.message + err.code);
9. }
```

**起始API Level**

9

**变更的接口/组件**

| 接口声明 | 变更前 | 变更后 |
| --- | --- | --- |
| getSecurityLabel(path:string, callback:AsyncCallback<string>): void | 默认返回空字符串 | 默认返回“s3” |
| getSecurityLabel(path:string):Promise<string> | 默认返回空字符串 | 默认返回“s3” |
| getSecurityLabelSync(path:string):string | 默认返回空字符串 | 默认返回“s3” |

**适配指导**

此变更属于Bugfix，应用无需适配。使用getSecurityLabel接口获取未设置过数据风险等级标签的数据时，默认返回“s3”。

### 文件授权接口行为变更

**变更原因**

基于对用户个人文件资产保护，文件必须先授权后使用。文件授权接口实行强管控，提供目录授权和文件持久化授权。

说明

该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。

**变更影响**

此变更涉及应用适配。

变更前：

应用退出后再次打开访问获取到URI的文件时获得该文件的持久化未做强制校验；3D目录（下载/文档/桌面)目录预授权未做强制校验。

变更后：

应用退出后再次打开访问获取到URI的文件时需先获得该文件的持久化，即调用文件持久化授权；3D目录授权应用需先申请才可访问对应目录下的文件。

**起始API Level**

11

**变更的接口/组件**

接口未变更，行为变更；变更后对文件/目录授权实行强管控。授权接口见下表：

| 权限 | 变更前所属权限组 | 变更后所属权限组 | 替代权限 |
| --- | --- | --- | --- |
| ohos.fileshare.persistPermission | 文件 | 文件 | 不涉及 |
| ohos.permission.READ\_WRITE\_DOWNLOAD\_DIRECTORY | 文件 | 文件 | 不涉及 |
| ohos.permission.READ\_WRITE\_DOCUMENTS\_DIRECTORY | 文件 | 文件 | 不涉及 |
| ohos.permission.READ\_WRITE\_DESKTOP\_DIRECTORY | 文件 | 文件 | 不涉及 |

**适配指导**

行为变更：默认行为变更，需应用适配，如应用未按申请应用无法访问文件。

参考开发指南的指导进行文件[授权持久化](../harmonyos-guides-V5/file-persistpermission-V5.md)，或者参考[获取并使用公共目录](../harmonyos-guides-V5/request-dir-permission-V5.md)使用公共资源。

## Distributed Service Kit

### 使用udid-hash与appid和盐值基于sha256混淆截断后保留前16位值作为deviceid，调用行为变更

**变更原因**

分布式设备管理deviceid接口存在安全漏洞，应用获取的deviceid在设备重置后或者应用卸载重装后不变，对于同一个应用可以标识设备。

说明

该变更在9月21日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.810。

**变更影响**

此变更涉及应用适配。

变更前：

同一个应用在设备重置后，或者app卸载重装后，获取的deviceid相同。

变更后：

1. 同一个应用在设备重置后获取的deviceid不同；
2. 应用卸载后重装，获取的deviceid不同；
3. 不同应用在同一个设备上获取的deviceid不同；
4. 同一个应用在不同设备上获取的同一个设备的deviceid不同。

**起始API Level**

10

**变更的接口/组件**

不涉及

**适配指导**

1. 设备间传递deviceid比较：将networkid发送到对端进行比较；
2. 应用将deviceid与SA获取的deviceid进行比较：使用networkid进行比较。

## 调试命令

### 命令行调试工具使用权限缩小

**变更原因**

基于对应用的安全隐私保护，调试能力遵循以下原则进行调整：

1.在开发者模式下，开发者只能调试自己的应用，无法调试其他三方APP。

2.调试信息不包含开发者无权读取的信息。

**变更影响**

此变更涉及应用适配。

调试命令使用权限缩小，部分命令仅debug应用可用，详见“变更的接口/组件”。

**起始API Level**

不涉及

**变更的接口/组件**

| 组件 | 命令 | 变更前 | 变更后 |
| --- | --- | --- | --- |
| hidumper | hidumper --mem-smaps pid [-v] | 有内存信息打印，且能获取内存地址信息 | 将打印帮助信息，不支持该命令 |
| hidumper | hidumper -p [pid] | 可以导出任意进程的maps信息以及/proc/pid/mountinfo等信息 | 只支持导出debug应用的基础信息，所有进程均不支持导出maps信息 |
| hiprofiler | nativehook | nativehook插件可以对任意进程进行调优 | 使用nativehook插件仅支持对debug应用进行调试 |
| hiperf | hiperf record/stat | 支持对release应用进行调试 | 仅支持对debug应用进行调试 |
| hiperf | hiperf dump | 可以输出采集进程的maps信息以及其他信息 | 不输出maps信息，其他信息不变 |
| hiperf | 日志输出 | 可以输出hiperf日志信息 | 不支持该功能 |

**适配指导**

将应用的编译模式由release修改为debug，重新编译调试。

### hdc工具tmode usb命令功能废弃

**变更原因**

按照开发者需求，hdc应同时支持USB调试和无线调试。

**变更影响**

变更前：hdc tmode usb命令执行后将关闭无线调试通道，同时打开USB调试通道。

变更后：hdc tmode usb命令功能废弃，可通过调测设备的开发者选项界面中USB调试开关控制USB调试通道开启和关闭。如需关闭无线调试通道请使用hdc tmode port close命令。

**起始API Level**

不涉及

**变更的接口/组件**

| 组件 | 命令 |
| --- | --- |
| hdc | hdc tmode usb |

**适配指导**

根据功能变更后命令进行调整适配.

### aa工具不支持对Release模式的应用进行调试

**变更原因**

aa工具是DevEco Studio调试能力的底层依赖，正常的调试场景都通过DevEco Studio进行，正常情况下DevEco Studio会限制对Release模式的应用进行调试，但存在绕过DevEco Studio直接使用aa工具的调试命令进行调试的风险，应当从根本上限制此行为。

说明

该变更在9月12日发布的patch版本引入，对应开发工具DevEco Studio版本为5.0.3.806。

**变更影响**

此变更涉及应用适配。

变更前：

存在绕过DevEco Studio直接通过aa工具的命令调试Release模式的应用的风险。

变更后：

aa工具不支持对Release模式的应用进行调试。

**起始API Level**

不涉及

**变更的接口/组件**

aa工具

**适配指导**

默认行为变更，无需适配。
