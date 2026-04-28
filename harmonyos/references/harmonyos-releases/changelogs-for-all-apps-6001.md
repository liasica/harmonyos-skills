---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-6001
title: OS平台API行为的变更
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > OS平台行为变更说明 > 6.0.0(20) Beta1引入的行为变更 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:07+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:c7dee32fa81a66b469e45c56123cdbf2dbee30138044c8e633db2839f429487a
---

## Ability Kit

### AbilityDelegator.startAbility()接口错误码变更

**变更原因**

AbilityDelegator.startAbility()返回的所有错误码与API描述不一致。

**变更影响**

此变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

变更影响AbilityDelegator.startAbility()返回的所有错误码，错误码对照表如下：

| 变更前 | 变更后 |
| --- | --- |
| 29360128 | 401 |
| 2097199 | 16000001 |
| 2097187 | 16000002 |
| 2097179 | 16000004 |
| 2097208 | 16000005 |
| 2097207 | 16000006 |
| 2097203 | 16000008 |
| 11 | 16000009 |
| 2097206 | 16000010 |
| 2097323 | 16000011 |
| 2097204 | 16000012 |
| 2097215 | 16000013 |
| 2097167 | 16000050 |
| 5242881 | 16000053 |
| 29360300 | 16000055 |
| 2097205 | 16200001 |

**起始API Level**

9

**变更的接口/组件**

AbilityDelegator提供的startAbility()接口。

**适配指导**

无需适配。

AbilityDelegator提供的startAbility()接口参见[startAbility API参考](../harmonyos-references/js-apis-inner-application-abilitydelegator.md#startability9)。

### 借助Want进行文件分享时擦除不合法的URI

**变更原因**

在文件分享场景下（[Want](../harmonyos-references/js-apis-app-ability-want.md#want)的flags字段中配置了[wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION](../harmonyos-references/js-apis-app-ability-wantconstant.md#flags)或[wantConstant.Flags.FLAG\_AUTH\_WRITE\_URI\_PERMISSION](../harmonyos-references/js-apis-app-ability-wantconstant.md#flags)），应用可以通过Want的uri字段传递单个URI、或者通过[wantConstant.Params.PARAMS\_STREAM](../harmonyos-references/js-apis-app-ability-wantconstant.md#params)的Key值传递多个URI。为了确保传递给目标应用的参数合法，系统将主动擦除不满足条件的URI。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

变更前：文件分享场景下，如果Want的uri字段中scheme为空，或wantConstant.Params.PARAMS\_STREAM字段中的URI的scheme不为file，系统不做任何处理。

变更后：文件分享场景下，如果Want的uri字段中scheme为空，或wantConstant.Params.PARAMS\_STREAM字段中的URI的scheme不为file，系统将擦除对应的URI取值。

**起始API Level**

9

**变更的接口/组件**

启动和退出应用的相关接口在文件分享场景下可触发该变更，涉及的接口如下：

[UIAbilityContext](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md):

* startAbility(want: Want, callback: AsyncCallback<void>): void
* startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
* startAbility(want: Want, options?: StartOptions): Promise<void>
* startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void
* startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void
* startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>
* terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void
* terminateSelfWithResult(parameter: AbilityResult): Promise<void>
* connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
* startAbilityByCall(want: Want): Promise<Caller>
* startUIServiceExtensionAbility(want: Want): Promise<void>
* connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>

[UIExtensionContext](../harmonyos-references/js-apis-inner-application-uiextensioncontext.md):

* startAbility(want: Want, callback: AsyncCallback<void>): void
* startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void
* startAbility(want: Want, options?: StartOptions): Promise<void>
* startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void
* startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void
* startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>
* connectServiceExtensionAbility(want: Want, options: ConnectOptions): number
* terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void
* terminateSelfWithResult(parameter: AbilityResult): Promise<void>
* startUIServiceExtensionAbility(want: Want): Promise<void>
* connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>

**适配指导**

排查Want的flags字段中是否设置了文件URI读写Flag（wantConstant.Flags.FLAG\_AUTH\_READ\_URI\_PERMISSION或wantConstant.Flags.FLAG\_AUTH\_WRITE\_URI\_PERMISSION），并且uri字段或wantConstant.Params.PARAMS\_STREAM字段中写入了非[文件URI](../harmonyos-references/js-apis-file-fileuri.md#fileuri10)。

以下两种处理方式任选其一：

* 删除Want中flags字段的文件URI读写Flag。
* 修改uri字段和wantConstant.Params.PARAMS\_STREAM字段中的非文件URI为文件URI。如果原来写入的URI是沙箱路径，可以通过[fileUri.getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)接口将其转为文件URI。

## ArkTS

### 通过字面量定义的数组在删除元素后再使用该字面量定义数组时数组内容异常

**变更原因**

通过字面量定义的数组在删除元素后再使用该字面量定义数组时数组内容异常。

**变更影响**

此变更涉及应用适配。

变更前：通过字面量定义的数组在删除元素后再使用该字面量定义数组时，新数组为被删除元素之后的数组。

变更后：通过字面量定义的数组在删除元素后再使用该字面量定义数组时，新数组为字面量展示的数组。

**起始API Level**

6

**变更的接口/组件**

不涉及

**适配指导**

排查是否有利用字面量定义数组，并且在未经过其他修改操作之前删除其中元素的行为。

例如：

```
1. for (let i = 0; i < 2; i++) {
2. let arr = [0, 0]
3. console.log(JSON.stringify(arr));
4. delete arr[0];
5. }
```

未变更前该用例输出为：

```
1. [0,0]
2. [null,0]
```

变更后该用例输出为:

```
1. [0,0]
2. [0,0]
```

说明

在ets文件中[不支持使用delete](../harmonyos-guides/typescript-to-arkts-migration-guide.md#不支持delete运算符)，但可在三方库中或者js文件中使用。

本变更修复该问题，通过字面量定义的数组在删除元素后再使用该字面量定义数组时，新数组为字面量展示的数组。

## ArkUI

### GridRow组件columns参数和GridCol组件span参数默认值变更

**变更原因**

栅格组件默认值原规格容易引发页面压缩问题，变更后提升组件易用性。

**变更影响**

该变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

| 变更前 | 变更后 |
| --- | --- |
| GridRow中columns不配置时，默认值为12。 | GridRow中columns不配置时，columns使用默认值：{ xs: 2, sm: 4, md: 8, lg: 12, xl: 12, xxl: 12 } |
| GridRow中columns配置部分断点时，取已配置的更小断点的columns列数补全未配置的列数。若未配置更小断点的columns列数，取默认值12。  columns: {xs:2, md:4, lg:8} 等于配置 columns: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}  columns: {md:4, lg:8} 等于配置 columns: {xs:12, sm:12, md:4, lg:8, xl:8, xxl:8} | GridRow中columns配置部分断点时，取已配置的更小断点的columns列数补全未配置的列数。若未配置更小断点的columns列数，取已配置的更大断点的columns列数补全未配置的列数。  columns: {xs:2, md:4, lg:8} 等于配置 columns: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}  columns: {md:4, lg:8} 等于配置 columns: {xs:4, sm:4, md:4, lg:8, xl:8, xxl:8} |
| GridCol中span配置部分断点时，取已配置的更小断点的span列数补全未配置的列数。若未配置更小断点的span列数，取默认值1。  span: {xs:2, md:4, lg:8} 等于配置 span: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}  span: {md:4, lg:8} 等于配置 span: {xs:1, sm:1, md:4, lg:8, xl:8, xxl:8} | GridCol中span配置部分断点时，取已配置的更小断点的span列数补全未配置的列数。若未配置更小断点的span列数，取已配置的更大断点的span列数补全未配置的列数。  span: {xs:2, md:4, lg:8} 等于配置 span: {xs:2, sm:2, md:4, lg:8, xl:8, xxl:8}  span: {md:4, lg:8} 等于配置 span: {xs:4, sm:4, md:4, lg:8, xl:8, xxl:8} |

**起始API Level**

9

**变更的接口/组件**

GridRow组件、GridCol组件。

**适配指导**

默认行为变更，无需适配，但应注意变更后的默认效果是否符合开发者预期，可手动配置所有不同宽度设备下GridRow组件的栅格列数和GridCol组件所占列数，避免使用默认值或默认补全的布局效果不符合预期。

```
1. @Entry
2. @Component
3. struct Example {
4. @State bgColors: ResourceColor[] =
5. ['rgb(213,213,213)', 'rgb(150,150,150)', 'rgb(0,74,175)', 'rgb(39,135,217)', 'rgb(61,157,180)', 'rgb(23,169,141)',
6. 'rgb(255,192,0)', 'rgb(170,10,33)'];
7. @State currentBp: string = "unknown"

9. build() {
10. Column() {
11. Column() {
12. Text(this.currentBp)
13. GridRow({
14. columns: {
15. xs: 2, // 窗口宽度落入xs断点上，栅格栅格容器每一行分为2列。
16. sm: 4, // 窗口宽度落入sm断点上，栅格栅格容器每一行分为4列。
17. md: 8, // 窗口宽度落入md断点上，栅格栅格容器每一行分为8列。
18. lg: 12, // 窗口宽度落入lg断点上，栅格栅格容器每一行分为12列。
19. xl: 12, // 窗口宽度落入xl断点上，栅格栅格容器每一行分为12列。
20. xxl: 12 // 窗口宽度落入xxl断点上，栅格栅格容器每一行分为12列。
21. },
22. breakpoints: {
23. value: ['320vp', '600vp', '840vp', '1440vp', '1600vp'],
24. reference: BreakpointsReference.WindowSize
25. }
26. }) {
27. ForEach(this.bgColors, (color: ResourceColor, index?: number | undefined) => {
28. GridCol({
29. span: {
30. xs: 1, // 窗口宽度落入xs断点上，栅格子容器宽度占1列。
31. sm: 2, // 窗口宽度落入sm断点上，栅格子容器宽度占2列。
32. md: 4, // 窗口宽度落入md断点上，栅格子容器宽度占4列。
33. lg: 6, // 窗口宽度落入lg断点上，栅格子容器宽度占6列。
34. xl: 6, // 窗口宽度落入xl断点上，栅格子容器宽度占6列。
35. xxl: 6 // 窗口宽度落入xxl断点上，栅格子容器宽度占6列。
36. }
37. }) {
38. Row() {
39. Text(`${index}`)
40. }.width("100%").height('50vp')
41. }.backgroundColor(color)
42. })
43. }
44. .onBreakpointChange((breakpoint) => {
45. this.currentBp = breakpoint
46. })
47. }.width('90%')
48. }.width('100%')
49. }
50. }
```

### width和height支持的matchParent接口规格变更

**变更原因**

接口能力增强，使能Row和Column在设置matchParent时仅适应父组件内容区大小。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

变更前：Row和Column的子组件matchParent时，会将其大小设置为父组件包含padding、border以及safeAreaPadding后的大小。

变更后：Row和Column的子组件matchParent时，会将其大小设置为父组件不包含padding、border以及safeAreaPadding后的大小，即与父组件内容区大小保持一致。

例如：运行以下示例，进入页面后，观察matchParent的最终结果。

```
1. @Entry
2. @Component
3. struct Demo {
4. build() {
5. Column(){
6. Row().width(LayoutPolicy.matchParent).height(LayoutPolicy.matchParent).backgroundColor('rgb(0, 74, 175)')
7. }.width(200).height(200).padding(20).backgroundColor('rgb(39, 135, 217)')
8. }
9. }
```

变更前后效果如下:

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

15

**变更的接口/组件**

width(widthValue: Length | LayoutPolicy): T

height(heightValue: Length | LayoutPolicy): T

**适配指导**

默认行为变更，无需适配。

### 文本与输入、信息展示、按钮与选择、滚动与滑动、图形绘制组件接口支持Resource类型

**变更原因**

基础能力增强，文本与输入、信息展示、按钮与选择、滚动与滑动、图形绘制组件的接口支持Resource类型，可以使用资源对象设置默认选项的值。

**变更影响**

此变更涉及应用适配。

* 变更前：TextPickerOptions、Progress、QRCode、TextClock、TextTimer、Badge、Circle、Text、TextArea、TextInput、Search、Span、RichEditor、Rating、Rect、Ellipse、Line、Polyline、Path、Polygon、ProgressButton、SubHeader、SubHeaderV2、Shape、SwipeRefresher中部分接口不支持Resource类型。
* 变更后：TextPickerOptions、Progress、QRCode、TextClock、TextTimer、Badge、Circle、Text、TextArea、TextInput、Search、Span、RichEditor、Rating、Rect、Ellipse、Line、Polyline、Path、Polygon、ProgressButton、SubHeader、SubHeaderV2、Shape、SwipeRefresher中部分接口支持Resource类型。

**起始API Level**

11

**变更的接口/组件**

| 组件名称 | 接口名称 | 参数名称 |
| --- | --- | --- |
| TextPicker | TextPickerOptions | value |
| Progress | CapsuleStyleOptions | content |
| TextPicker | TextPickerOptions | value |
| QRCode | QRCodeInterface | value |
| TextClock | format | value |
| TextTimer | fontWeight | value |
| Badge | BadgeStyle | fontSize、badgeSize、fontWeight |
| Badge | BadgeParamWithString | value |
| Circle | CircleOptions | width、height |
| Text | fontWeight | value、weight |
| Text | letterSpacing | value |
| Text | baselineOffset | value |
| TextArea | fontWeight | value |
| TextInput | fontWeight | value |
| Search | SearchOptions | value |
| Search | searchButton | value |
| Span | fontWeight | value |
| Span | letterSpacing | value |
| RichEditor | RichEditorController.addTextSpan | content |
| Rating | StarStyleOptions | backgroundUri、foregroundUri、secondaryUri |
| Rect | RectOptions | width、height、radius |
| Rect | RoundedRectOptions | width、height、radiusWidth、radiusHeight |
| Rect | radiusWidth | value |
| Rect | radiusHeight | value |
| Rect | radius | value |
| Ellipse | EllipseOptions | width、height |
| Line | LineOptions | width、height |
| Polyline | PolylineOptions | width、height |
| Path | PathOptions | width、height、commands |
| Path | commands | value |
| Polygon | PolygonOptions | width、height |
| ProgressButton | - | content |
| SubHeader | SelectOptions | value |
| SubHeaderV2 | SubHeaderV2SelectOptions | selectedContent |
| SubHeaderV2 | SubHeaderV2Select | selectedContent |
| Shape | ViewportRect | x、y、width、height |
| Shape | strokeDashOffset | value |
| Shape | strokeMiterLimit | value |
| Shape | strokeWidth | value |
| SwipeRefresher | - | content |

**适配指导**

若有继承派生则需要在继承派生定义处增加Resource类型支持，否则无需适配。

### UI Input相关NDK接口行为变更

**变更原因**

修复相关接口在如下场景下的返回值异常问题，以确保开发者能够获取正确的结果：

* 鼠标滚轮或触控板双指滑动；
* 通过Enter键触发点击或单指轻触手势；
* 使用外设键盘等设备与焦点窗口交互；
* 组件节点接收按键事件；
* 为XComponent组件注册自定义事件拦截回调后进行触摸测试；
* 绑定组件接收轴事件；
* 为XComponent组件注册UI输入事件回调后接收UI输入事件。

**变更影响**

此变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

变更前与变更后的变化说明：

| 接口名称 | 起始版本 | 说明 | 变更原因 | 变更影响 |
| --- | --- | --- | --- | --- |
| int32\_t  OH\_ArkUI\_UIInputEvent\_GetType(const ArkUI\_UIInputEvent\* event); | 12 | 获取该裸事件对应的枚举类型ArkUI\_UIInputEvent\_Type，变更前包括触控、轴、鼠标这几种裸事件 | 遗漏支持key事件类型 | 当传入的参数为key事件时，获取的类型为0，修复后可获取正确值（ARKUI\_UIINPUTEVENT\_TYPE\_KEY）。 |
| int32\_t  OH\_ArkUI\_UIInputEvent\_GetAction(const ArkUI\_UIInputEvent\* event); | 12 | 获取裸事件对应的事件action类型，例如，如果裸事件为触控事件，则获取到的事件action类型为DOWN、MOVE、UP、CANCEL之一；若裸事件类型为鼠标事件，则为PRESS、RELEASE、MOVE、CANCEL之一；若为轴事件，则为BEGIN、UPDATE、END、CANCEL之一。因此，action类型的定义和含义存在差异，但在接口设计上，将返回值统一为int类型，以消除这些差异。 | 遗漏支持axis事件类型 | 当传入的参数为axis事件时，获取的类型为0，修复后可获取正确值（BEGIN/UPDATE/END/CANCEL）。 |
| int32\_t  OH\_ArkUI\_UIInputEvent\_GetDeviceId(const ArkUI\_UIInputEvent\* event); | 14 | 获取当前输入事件的触发设备ID | 实现遗漏通过键盘Enter键触发的click事件场景。 | 1. 仅TAB键走焦场景有可能触发该场景；  2.变更前应用无法获取正确的当前输入事件的触发设备ID，修复后可获取正确的当前输入事件的触发设备ID。 |

**起始API Level**

12

**变更的接口/组件**

int32\_t OH\_ArkUI\_UIInputEvent\_GetType(const ArkUI\_UIInputEvent\* event);

int32\_t OH\_ArkUI\_UIInputEvent\_GetAction(const ArkUI\_UIInputEvent\* event);

int32\_t OH\_ArkUI\_UIInputEvent\_GetDeviceId(const ArkUI\_UIInputEvent\* event);

**适配指导**

变更前的接口遗漏对部分事件的支持，导致输入这些事件时会返回默认值，与预期不符；修复后的接口已支持这些遗漏的事件，调用时可获取正确的返回值，应用无需特殊适配。

### 使用字面量初始化CustomDialogController类实例导致的编译行为变更

**变更原因**

在类CustomDialogController中新增接口getState()获取对应弹窗的状态。当原先使用字面量的方式初始化CustomDialogController实例时，会编译报错。字面量的初始化方式是指采用"{}"直接初始化类的实例，例如：

```
1. let controller: CustomDialogController = { open() {}, close() {} }
```

**变更影响**

此变更涉及应用适配，使用字面量初始化CustomDialogController类实例时涉及。

变更前：开发者可以通过字面量的方式初始化CustomDialogController，如：

```
1. let controller: CustomDialogController = { open() {}, close() {} }
```

变更后：由于在CustomDialogController中新增了getState()方法，变更前的上述写法未初始化新增的getState()方法，会编译报错。

**起始API Level**

不涉及

**变更的接口/组件**

编译行为，不涉及接口

**适配指导**

开发者应修改为使用new的方式创建类的实例，如：

```
1. let controller: CustomDialogController = new CustomDialogController()
```

## ArkWeb

### ArkWeb基于上游社区的Chromium内核从114升级为132版本

**变更原因**

为了提升使用ArkWeb内核应用的安全性，开发者使用最新的W3C HTML5特性，以及获得Chromium上游社区最新的性能体验优化成果，故本次进行内核升级（114 -> 132）。

**变更影响**

从上游社区337项功能变更说明，以及社区200+问题单分析，WPT测试集结果分析，当前共发现50项需要开发者注意的变更点，请参考[ArkWeb 版本的差异总结](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/ArkWeb_114_132.md)。

**起始API Level**

不涉及

**变更的接口/组件**

ArkWeb

**适配指导**

如果在应用中使用Web组件展示网页内容，则需要遵循[ArkWeb 版本的差异总结](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/ArkWeb_114_132.md)中所涉及的最新W3C规格变更。

## Connectivity Kit

### 蓝牙BLE接口错误码变更

**变更原因**

蓝牙子系统BLE相关接口错误码不够清晰，开发者无法通过错误信息明确需要如何修复问题，影响开发效率。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

变更前：BLE广播、BLE扫描、GATT Client、GATT Server接口异常时仅返回2900099错误码。

变更后：BLE广播、BLE扫描、GATT Client、GATT Server接口异常时会返回更详细的错误码。

**起始API Level**

10

**变更的接口/组件**

| 模块名 | 命名空间 | 类名 | 接口声明 | 主要变更点说明 |
| --- | --- | --- | --- | --- |
| @ohos.bluetooth.ble.d.ts | ble |  | function startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void; | 新增2900010错误码：广播资源已耗尽；  新增2902054错误码：广播报文数据长度超限； |
| @ohos.bluetooth.ble.d.ts | ble |  | function startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<number>): void; | 新增2900010错误码：广播资源已耗尽；  新增2902054错误码：广播报文数据长度超限； |
| @ohos.bluetooth.ble.d.ts | ble |  | function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>; | 新增2900010错误码：广播资源已耗尽；  新增2902054错误码：广播报文数据长度超限； |
| @ohos.bluetooth.ble.d.ts | ble |  | function enableAdvertising(advertisingEnableParams: AdvertisingEnableParams, callback: AsyncCallback<void>): void; | 新增2902055错误码：无效的广播ID； |
| @ohos.bluetooth.ble.d.ts | ble |  | function enableAdvertising(advertisingEnableParams: AdvertisingEnableParams): Promise<void>; | 新增2902055错误码：无效的广播ID； |
| @ohos.bluetooth.ble.d.ts | ble |  | function disableAdvertising(advertisingDisableParams: AdvertisingDisableParams, callback: AsyncCallback<void>): void; | 新增2902055错误码：无效的广播ID； |
| @ohos.bluetooth.ble.d.ts | ble |  | function disableAdvertising(advertisingDisableParams: AdvertisingDisableParams): Promise<void>; | 新增2902055错误码：无效的广播ID； |
| @ohos.bluetooth.ble.d.ts | ble |  | function stopAdvertising(advertisingId: number, callback: AsyncCallback<void>): void; | 新增2902055错误码：无效的广播ID； |
| @ohos.bluetooth.ble.d.ts | ble |  | function stopAdvertising(advertisingId: number): Promise<void>; | 新增2902055错误码：无效的广播ID； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901000错误码：读失败，对端禁止读操作；  新增2901003错误码：读失败，未与对端建立连接；  新增2901004错误码：读失败，连接链路拥塞；  新增2901005错误码：读失败，连接链路未加密；  新增2901006错误码：读失败，连接链路未认证；  新增2901007错误码：读失败，连接链路未授权； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901000错误码：读失败，对端禁止读操作；  新增2901003错误码：读失败，未与对端建立连接；  新增2901004错误码：读失败，连接链路拥塞；  新增2901005错误码：读失败，连接链路未加密；  新增2901006错误码：读失败，连接链路未认证；  新增2901007错误码：读失败，连接链路未授权； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901000错误码：读失败，对端禁止读操作；  新增2901003错误码：读失败，未与对端建立连接；  新增2901004错误码：读失败，连接链路拥塞；  新增2901005错误码：读失败，连接链路未加密；  新增2901006错误码：读失败，连接链路未认证；  新增2901007错误码：读失败，连接链路未授权； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901000错误码：读失败，对端禁止读操作；  新增2901003错误码：读失败，未与对端建立连接；  新增2901004错误码：读失败，连接链路拥塞；  新增2901005错误码：读失败，连接链路未加密；  新增2901006错误码：读失败，连接链路未认证；  新增2901007错误码：读失败，连接链路未授权； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType, callback: AsyncCallback<void> ): void; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901001错误码：写失败，对端禁止写操作；  新增2901003错误码：写失败，未与对端建立连接；  新增2901004错误码：写失败，连接链路拥塞；  新增2901005错误码：写失败，连接链路未加密；  新增2901006错误码：写失败，连接链路未认证；  新增2901007错误码：写失败，连接链路未授权； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType): Promise<void>; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901001错误码：写失败，对端禁止写操作；  新增2901003错误码：写失败，未与对端建立连接；  新增2901004错误码：写失败，连接链路拥塞；  新增2901005错误码：写失败，连接链路未加密；  新增2901006错误码：写失败，连接链路未认证；  新增2901007错误码：写失败，连接链路未授权； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | writeDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<void>): void; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901001错误码：写失败，对端禁止写操作；  新增2901003错误码：写失败，未与对端建立连接；  新增2901004错误码：写失败，连接链路拥塞；  新增2901005错误码：写失败，连接链路未加密；  新增2901006错误码：写失败，连接链路未认证；  新增2901007错误码：写失败，连接链路未授权； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | writeDescriptorValue(descriptor: BLEDescriptor): Promise<void>; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901001错误码：写失败，对端禁止写操作；  新增2901003错误码：写失败，未与对端建立连接；  新增2901004错误码：写失败，连接链路拥塞；  新增2901005错误码：写失败，连接链路未加密；  新增2901006错误码：写失败，连接链路未认证；  新增2901007错误码：写失败，连接链路未授权； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | getRssiValue(callback: AsyncCallback<number>): void; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901003错误码：未与对端建立连接； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | getRssiValue(): Promise<number>; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901003错误码：未与对端建立连接； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901003错误码：未与对端建立连接； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean): Promise<void>; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901003错误码：未与对端建立连接； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | setCharacteristicChangeIndication( characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901003错误码：未与对端建立连接； |
| @ohos.bluetooth.ble.d.ts | ble | GattClientDevice | setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean): Promise<void>; | 新增2900011错误码：操作忙碌，需等待上一次操作结束；  新增2901003错误码：未与对端建立连接； |

**适配指导**

应用可将接口调用的错误码打印出来，辅助定位问题。

以广播报文数据超过最大长度限制导致开启BLE广播失败为例：

```
1. let advSettings: ble.AdvertiseSetting = {
2. "interval": 160,
3. "connectable": true,
4. };
5. // 1）开发者构造的广播报文数据长度超过最大长度限制
6. let serviceUuidsArray: Array<string> = new Array();
7. serviceUuidsArray.push("00001111-1111-1000-8000-00805f9b34fb");
8. serviceUuidsArray.push("00001111-2222-1000-8000-00805f9b34fb");
9. serviceUuidsArray.push("00001111-3333-1000-8000-00805f9b34fb");
10. let advData: ble.AdvertiseData = {
11. "serviceUuids": serviceUuidsArray,
12. "manufactureData": new Array(),
13. "serviceData": new Array(),
14. "includeDeviceName": true,
15. };

17. try {
18. ble.startAdvertising(advSettings, advData);
19. } catch (err) {
20. // 2）通过日志打印发现接口调用报错2902054，即表示广播报文数据长度超过最大长度限制
21. console.error("errCode: " + err.code + ", errMessage: " + err.message);
22. }
23. // 3）开发者根据错误码确定广播报文构造方式的合理性。建议：
24. //  - 是否有必要携带本机蓝牙设备名
25. //  - 是否将部分广播报文构造成入参advResponse
```

## Core File Kit

### @ohos.file.fs.d.ts中copy接口在拷贝后，对目标文件原有数据处理方式发生变更

**变更原因**

在目标文件存在且size大于源文件的场景下使用copy接口，拷贝后的目标文件的size会大于源文件且尾部存在冗余内容。

**变更影响**

此变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

变更前：在目标文件存在且size大于源文件的场景下使用copy接口，拷贝后的目标文件的size会大于源文件且尾部存在冗余内容。

变更后：API version 20及以上版本开始，在目标文件存在且size大于源文件的场景下使用copy接口，拷贝后的目标文件与源文件内容及size相同；API version 20以下版本与变更前行为一致。

**起始API Level**

11

**变更的接口/组件**

@ohos.file.fs.d.ts中的copy接口

**适配指导**

默认行为变更，无需适配。

## Driver Development Kit

### SendPipeRequest和SendPipeRequestWithAshmem传入错误参数时，返回值由USB\_DDK\_SUCCESS变更为USB\_DDK\_INVALID\_PARAMETER

**变更原因**

调用OH\_Usb\_SendPipeRequest和OH\_Usb\_SendPipeRequestWithAshmem接口时，如果入参中的devMmap的bufferlen的长度大于设备的MaxPacketSize，会导致接口执行失败，但是之前未将错误上报，开发者无法感知。

**变更影响**

此变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

变更前：调用OH\_Usb\_SendPipeRequest和OH\_Usb\_SendPipeRequestWithAshmem接口时，如传参错误导致中断传输失败，不会上报错误信息。

变更后：调用OH\_Usb\_SendPipeRequest和OH\_Usb\_SendPipeRequestWithAshmem接口时，如传参错误导致中断传输失败，会上报相关的错误信息，使得开发者获得接口的真实反馈，提升开发体验。

**起始API Level**

* SendPipeRequest ：10
* SendPipeRequestWithAshmem：12

**变更的接口/组件**

drivers/external\_device\_manager: OH\_Usb\_SendPipeRequest、OH\_Usb\_SendPipeRequestWithAshmem。

**适配指导**

只要开发者传入正确的参数，接口功能不变，因此无需开发者适配。

OH\_Usb\_SendPipeRequest和OH\_Usb\_SendPipeRequestWithAshmem接口开发适配指导：

```
1. ...
2. static uint8_t g_configIndex = 0;
3. static uint64_t g_interfaceHandle = 0;
4. static std::tuple<bool, uint8_t, uint8_t, uint16_t> FindForEachInterface(const UsbDdkInterface &interface)
5. {
6. struct UsbDdkInterfaceDescriptor *intDesc = interface.altsetting;
7. uint32_t numSetting = interface.numAltsetting;
8. for (uint32_t setIdx = PARAM_0; setIdx < numSetting; ++setIdx) {
9. uint32_t numEp = intDesc[setIdx].interfaceDescriptor.bNumEndpoints;
10. struct UsbDdkEndpointDescriptor *epDesc = intDesc[setIdx].endPoint;
11. for (uint32_t epIdx = PARAM_0; epIdx < numEp; ++epIdx) {
12. if (!IsInterruptInEndpoint(epDesc[epIdx].endpointDescriptor)) {
13. continue;
14. }
15. return { true, intDesc[setIdx].interfaceDescriptor.bInterfaceNumber,
16. epDesc[epIdx].endpointDescriptor.bEndpointAddress, epDesc[epIdx].endpointDescriptor.wMaxPacketSize };
17. }
18. }
19. return { false, {}, {}, {} };
20. }

22. static std::tuple<bool, uint8_t, uint8_t, uint16_t> GetEndpointInfo(const struct UsbDdkConfigDescriptor *config)
23. {
24. for (uint32_t intIdx = PARAM_0; intIdx < config->configDescriptor.bNumInterfaces; ++intIdx) {
25. auto result = FindForEachInterface(config->interface[intIdx]);
26. if (std::get<0>(result)) {
27. return result;
28. }
29. }
30. return { false, {}, {}, {} };
31. }

33. struct UsbDdkConfigDescriptor *config = nullptr;
34. // deviceId通过ts接口queryDevice获取
35. int32_t ret = OH_Usb_GetConfigDescriptor(deviceId, g_configIndex, &config);
36. if (ret != USB_DDK_SUCCESS) {
37. // 打印错误信息，调用OH_Usb_GetConfigDescriptor失败
38. return;
39. }

41. // 通过解析config可以获取设备的maxPktSize
42. auto [result, interface, endpoint, maxPktSize] = GetEndpointInfo(config);
43. if (!result) {
44. // 打印错误信息，调用GetEndpointInfo失败
45. return;
46. }

48. ret = OH_Usb_ClaimInterface(deviceId, interface, &g_interfaceHandle);
49. if (ret != USB_DDK_SUCCESS) {
50. // 打印错误信息，调用OH_Usb_ClaimInterface失败
51. return;
52. }

54. // 调用OH_Usb_SendPipeRequest
55. struct UsbDeviceMemMap *devMemMap = nullptr;
56. size_t bufferLen = maxPktSize;
57. ret = OH_Usb_CreateDeviceMemMap(deviceId, bufferLen, &devMemMap);
58. if (ret != USB_DDK_SUCCESS) {
59. // 打印错误信息，调用OH_Usb_CreateDeviceMemMap失败
60. return;
61. }
62. struct UsbRequestPipe pipe;
63. pipe.interfaceHandle = g_interfaceHandle;
64. pipe.endpoint = endpoint;
65. pipe.timeout = UINT32_MAX;
66. ret = OH_Usb_SendPipeRequest(&pipe, devMemMap);
67. ...

69. // 调用OH_Usb_SendPipeRequestWithAshmem
70. size_t bufferLen = maxPktSize;
71. const uint8_t name[100] = "TestAshmem";
72. DDK_Ashmem *ashmem = nullptr;
73. int32_t result = OH_DDK_CreateAshmem(name, bufferLen, &ashmem);
74. if (result != USB_DDK_SUCCESS) {
75. // 打印错误信息，调用OH_DDK_CreateAshmem失败
76. return;
77. }
78. const uint8_t ashmemMapType = 0x03;
79. result = OH_DDK_MapAshmem(ashmem, ashmemMapType);
80. if (result != USB_DDK_SUCCESS) {
81. // 打印错误信息，调用OH_DDK_MapAshmem失败
82. return;
83. }
84. struct UsbRequestPipe pipe;
85. pipe.interfaceHandle = g_interfaceHandle;
86. pipe.endpoint = endpoint;
87. pipe.timeout = UINT32_MAX;
88. int32_t returnValue = OH_Usb_SendPipeRequestWithAshmem(&pipe, ashmem);
89. ...
```

## Image Kit

### ImageInfo对象mimeType返回值变更

**变更原因**

该接口为图片信息查询接口，当前返回值与实际不符。

* 当处理raw格式图片时，实际mimeType应返回实际格式。因当前实际解码为raw格式图片的"previewImage"或"JpgFromRaw"字段，因此错误返回"image/jpeg"。
* 当处理icon格式图片时，未使用标准名称返回。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

| 实际格式 | 变更前返回 | 变更后返回 | 解码支持情况 | 编码支持情况 |
| --- | --- | --- | --- | --- |
| jpeg | image/jpeg | image/jpeg | 支持 | 支持 |
| icon | image/ico | image/x-icon | 支持 | 不支持 |
| dng | image/jpeg | image/x-adobe-dng | 支持 | 不支持 |
| cr2 | image/jpeg | image/x-canon-cr2 | 支持解码预览图 | 不支持 |
| raf | image/jpeg | image/x-fuji-raf | 支持解码预览图 | 不支持 |
| nef | image/jpeg | image/x-nikon-nef | 支持解码预览图 | 不支持 |
| nrw | image/jpeg | image/x-nikon--nrw | 支持解码预览图 | 不支持 |
| orf | image/jpeg | image/x-olympus-orf | 支持解码预览图 | 不支持 |
| rw2 | image/jpeg | image/x-panasonic-rw2 | 支持解码预览图 | 不支持 |
| pef | image/jpeg | image/x-pentax-pef | 支持解码预览图 | 不支持 |
| srw | image/jpeg | image/x-samsung-srw | 支持解码预览图 | 不支持 |
| arw | image/jpeg | image/x-sony-arw | 支持解码预览图 | 不支持 |

**起始API Level**

12

**变更的接口/组件**

ImageInfo对象mimeType返回值变更。

**适配指导**

图片信息查询接口返回值变更，调用方式无需改变。

```
1. import { image } from '@kit.ImageKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. function getImageMimeType(context: Context) {
4. //此处'test.dng'仅作示例，请开发者自行替换。否则imageSource会创建失败，导致后续无法正常执行。
5. const path: string = context.filesDir + "/test.dng";
6. const imageSourceApi: image.ImageSource = image.createImageSource(path);
7. if (imageSourceApi != undefined) {
8. imageSourceApi.getImageInfo().then((imageInfo: image.ImageInfo) => {
9. console.info("Succeeded in obtaining the image mimeType information.");
10. // 调用方式无需修改，返回值修改后因支持识别实际raw格式，需要将此处判断更新。
11. if (imageInfo.mimeType == "image/x-adobe-dng") {
12. console.info("Image mimeType is image/x-adobe-dng.");
13. }
14. }).catch((error: BusinessError) => {
15. console.error(`Failed to obtain the image information. code is ${error.code}, message is ${error.message}`);
16. })
17. }
18. }
```

## Media Kit

### 播放器所使用的内存归属变更

**变更原因**

应用创建的播放器实例当前使用的内存统一归属到操作系统侧，导致内存无法根据应用做精细化管理，也容易导致应用滥用播放器行为。本次变更将播放器使用的内存缓存关联到创建播放器的应用，便于应用使用资源的统计。

**变更影响**

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

此变更不涉及应用适配。

变更前：应用通过AVPlayer使用播放器时，所使用的内存在内存管理时计入操作系统所用内存。

变更后：应用通过AVPlayer使用播放器时，所使用的内存在内存管理时计入本应用所用内存。

**起始API Level**

9

**变更的接口/组件**

AVPlayer

**适配指导**

1、正常使用AVPlayer实例的应用（同时工作的实例＜16个）无需任何变更。

2、超出正常使用范围的应用，需要根据实际使用情况，调整到合适的实例个数，避免退后台后，被RSS查杀。

## User Authentication Kit

### @ohos.useriam.userAuth限制应用从后台发起带交互界面的身份认证变更

**变更原因**

需要限制应用从后台发起带交互界面的身份认证。

**变更影响**

此变更涉及应用适配。

变更前：应用申请了权限ohos.permission.ACCESS\_BIOMETRIC，可以从前台和后台调用start()发起身份认证。

变更后：如果需要从后台调用start()发起认证，需要申请系统权限ohos.permission.USER\_AUTH\_FROM\_BACKGROUND。

**起始API Level**

10

**变更的接口/组件**

start(): void;

变更前：

```
1. * @permission ohos.permission.ACCESS_BIOMETRIC
2. * @throws { BusinessError } 201 - Permission verification failed.
3. start(): void;
```

变更后：

```
1. * @permission ohos.permission.ACCESS_BIOMETRIC or ohos.permission.USER_AUTH_FROM_BACKGROUND
2. * @throws { BusinessError } 201 - Permission verification failed. Possible causes:
3. * <br>1. No permission to access biometric.
4. * <br>2. No permission to start authentication from background.
5. start(): void;
```

**适配指导**

不涉及从后台调用start()发起身份认证场景，无需适配。

如果涉及从后台调用start()发起身份认证，系统应用需要申请系统权限ohos.permission.USER\_AUTH\_FROM\_BACKGROUND；三方应用不能从后台发起身份认证。

## 其他

### mincore接口功能补齐至与Linux一致

**变更原因**

由于部分应用需要使用mincore做内存相关的性能调优，出参结果影响使用者调优的准确性。

本次变更对齐Linux中的实现，mincore支持判断出对应的物理页是否在pagecache或swapcache中。

**变更影响**

此变更不涉及应用适配。

mincore详细使用方法可见[man mincore](https://man7.org/linux/man-pages/man2/mincore.2.html)。

变更前：判断对应物理页是否有有效物理地址，若有则mincore出参返回1，反之则返回0。

变更后：增加对pagecache和swapcache的校验，若对应物理页在RAM中，则mincore出参返回1，反之则返回0。

**起始API Level**

不涉及

**变更的接口/组件**

mincore

**适配指导**

本变更不涉及应用适配。

### ptrace syscall操作未被停住的线程由返回0改为返回ESRCH.1

**变更原因**

部分外部应用反调试功能预期对未被ptrace停住的线程调用PTRACE\_DETACH会返回ESRCH否则会crash，本次修改鸿蒙返回值使其与Linux保持一致，解决此类应用因反调试功能crash的问题。

**变更影响**

此变更涉及应用适配。

变更前：调用ptrace syscall对未被ptrace停住的线程执行PTRACE\_DETACH等request会成功执行并返回0。

变更后：调用ptrace syscall对未被ptrace停住的线程执行PTRACE\_DETACH等request会执行错误并返回ESRCH，导致detach等request执行失败。

**起始API Level**

11

**变更的接口/组件**

内核ptrace系统调用

**适配指导**

1. 排查代码调用PTRACE\_DETACH等request的位置。
2. 确认调用request前线程是否已被ptrace停住。
3. 若线程未被停住，则应先通过向被调试线程发送信号来打断被调试线程。

```
1. /* 错误用法: 对未进入 PTRACE_STOP 的线程调用 PTRACE_DETACH */
2. ret = ptrace(PTRACE_CONT, pid, NULL, NULL);
3. if (ret < 0) {
4. perror("PTRACE_CONT");
5. return -1;
6. }

8. ret = ptrace(PTRACE_DETACH, pid, NULL, NULL);
9. if (ret < 0) {
10. perror("PTRACE_DETACH");
11. return -1;
12. }

14. /* 正确用法: 先调用 kill 发送 SIGSTOP 使线程进入 PTRACE_STOP，再对其调用 PTRACE_DETACH */
15. ret = ptrace(PTRACE_CONT, pid, NULL, NULL);
16. if (ret < 0) {
17. perror("PTRACE_CONT");
18. return -1;
19. }

21. kill(pid, SIGSTOP);
22. ret = waitpid(pid, &status, 0);
23. if (ret < 0) {
24. perror("waitpid");
25. return -1;
26. }

28. ret = ptrace(PTRACE_DETACH, pid, NULL, NULL);
29. if (ret < 0) {
30. perror("PTRACE_DETACH");
31. return -1;
32. }
```

### 限制ptrace接口仅可在开发者调试模式下使用

**变更原因**

为进一步保障安全隐私，将对非开发者模式，且不具备开发者证书情况下使用ptrace进行应用调试的行为进行限制。

**变更影响**

此变更涉及应用适配。

变更前：三方应用可以在任意模式下调用ptrace接口。

变更后：三方应用仅可在设备为开发者模式，且应用使用debug模式编译的情况下调用ptrace接口。

**起始API Level**

不涉及

**变更的接口/组件**

sys/ptrace.h

**适配指导**

三方应用申请开发者证书，使用debug模式编译应用，开启设备开发者模式情况下，调用ptrace接口进行调试。
