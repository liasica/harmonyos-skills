---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/arkts-api-compatibility-warning-elim
title: ArkTS API兼容性保护
breadcrumb: 版本说明 > 应用兼容性说明 > 应用开发中的兼容性场景开发指导 > API兼容性保护 > ArkTS API兼容性保护
category: harmonyos-releases
scraped_at: 2026-04-29T13:25:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e113a6d551d1fa6e4f16f9e5b9a18a59ceeb1db4028771bb6cf06716296db0e3
---

## 简介

随着HarmonyOS 持续迭代，为确保持续兼容老版本用户，开发者常需设置较低的compatibleSdkVersion。但这可能导致应用在低版本系统上因调用未受保护的新 API 而崩溃（如低版本设备误调高版本接口）。为了解决这一痛点，帮助开发者在调用新 API 时做好版本隔离，我们提供了以下几种兼容性保护的最佳实践。

## 通过distributionOSApiVersion和sdkApiVersion接口消除

* 针对HarmonyOS设备独有特性接口，即接口标记为since M.S.F(N)（文档中标记“起始版本：M.S.F(N)”, SDK物理包中hms路径下所包含的接口），使用distributionOSApiVersion接口进行兼容性判断保护。

  ```
  1. import { deviceInfo } from '@kit.BasicServicesKit';
  2. //针对HarmonyOS专有接口，即接口标记为since M.S.F(N)的接口
  3. getTestData(): void {
  4. // 兼容性判断，50001是由新接口的since字段M*10000+S*100+F转换而来
  5. if (deviceInfo.distributionOSApiVersion >= 50001) {
  6. // 调用5.0.1(13)的API新接口
  7. } else {
  8. // 降级方案
  9. }
  10. }
  ```
* 针对OpenHarmony底座接口，即接口标记为since N（文档中标记“起始版本：N”，SDK物理包中openharmony路径下所包含的接口），使用sdkApiVersion接口进行兼容性判断保护。

  ```
  1. import { deviceInfo } from '@kit.BasicServicesKit';
  2. //针对OpenHarmony底座公共接口，即接口标记为since N
  3. getTestData(): void {
  4. // 增加兼容性判断
  5. if (deviceInfo.sdkApiVersion >= 13) {
  6. // 调用5.0.1(13)的API新接口
  7. } else {
  8. // 降级方案
  9. }
  10. }
  ```

说明

* 对于应用能力的兼容性判断，建议使用面向开发者相关的API版本接口（例如：sdkApiVersion或distributionOSApiVersion接口）;
* HarmonyOS设备中“设置 > 点击设备名称 > 关于本机”中显示的各种版本号信息中，开发者只应该关注**API版本**信息。
* 开发者不应该使用面向消费者的HarmonyOS版本信息去进行应用能力兼容性判断（例如distributionOSVersion或displayVersion等字段返回的版本号实际为设备ROM版本号，与开发者严格使用的API版本号并无严格的关联关系，无法保证与API版本号一一对应）。
* 应注意，deviceInfo.sdkApiVersion仅能用于OpenHarmony底座接口的兼容性保护。

可通过以下示例进一步理解API版本判断的方法（[点击此处](https://gitcode.com/harmonyos_samples/APILevelAdapt)可获取完整示例工程）：

### 【示例一】

示例代码使用了6.0.0(20)版本开始支持的HdsActionBar组件，该示例展示了应用操作栏（ActionBar）在不同系统版本下的兼容性适配方案。场景中，支持点击操作栏中间的按钮，进行切换图标及展开和收起操作栏。

代码通过判断设备的distributionOSApiVersion是否达到6.0.0(20)（对应的值为60000）来实现适配：在高版本系统（6.0.0(20)及以上）中，直接使用UIDesignKit提供的HdsActionBar组件，利用其原生支持的startButtons、endButtons配置项快速构建操作栏，而在低版本系统中，采用Row容器与基础Button组件组合的降级方案，通过条件渲染模拟按钮的展开和收起状态，并用基本点击事件实现图标切换逻辑，确保核心交互功能在低版本设备上仍可正常使用。

```
1. import { HdsActionBar, ActionBarButton, ActionBarStyle } from '@kit.UIDesignKit';
2. import { deviceInfo } from '@kit.BasicServicesKit';

4. @Component
5. export struct ActionBarAdapter {
6. @State isExpand: boolean = true;
7. @State isPrimaryIconChanged: boolean = false;

9. build() {
10. Column() {
11. // Compatibility judgment, 60000 is derived from the since field of the new interface M*10000 F*100 S.
12. if (deviceInfo.distributionOSApiVersion >= 60000) {
13. // Component that calls the API of version 6.0.0(20)
14. HdsActionBar({
15. startButtons: [new ActionBarButton({
16. baseIcon: $r('sys.symbol.stopwatch_fill')
17. })],
18. endButtons: [new ActionBarButton({
19. baseIcon: $r('sys.symbol.mic_fill')
20. })],
21. primaryButton: new ActionBarButton({
22. baseIcon: $r('sys.symbol.plus'),
23. altIcon: $r('sys.symbol.play_fill'),
24. onClick: () => {
25. this.isExpand = !this.isExpand;
26. this.isPrimaryIconChanged = !this.isPrimaryIconChanged;
27. }
28. }),
29. actionBarStyle: new ActionBarStyle({
30. isPrimaryIconChanged: this.isPrimaryIconChanged
31. }),
32. isExpand: this.isExpand!!
33. })
34. } else {
35. // Downgrading plan
36. Row({ space: 25 }) {
37. if (this.isExpand) {
38. Button({ type: ButtonType.Circle }) {
39. SymbolGlyph($r('sys.symbol.stopwatch_fill'))
40. .fontSize(24)
41. .fontColor([$r('sys.color.font_secondary')])
42. }
43. .aspectRatio(1)
44. .height(45)
45. .backgroundColor($r('sys.color.background_secondary'))
46. .margin({ left: 10 })
47. }

49. Button({ type: ButtonType.Circle }) {
50. SymbolGlyph(this.isExpand ? $r('sys.symbol.plus') : $r('sys.symbol.play_fill'))
51. .fontSize(24)
52. .fontColor([$r('sys.color.white')])
53. }
54. .aspectRatio(1)
55. .height(55)
56. .backgroundColor($r('sys.color.brand'))

58. .onClick(() => {
59. this.isExpand = !this.isExpand;
60. })

62. if (this.isExpand) {
63. Button({ type: ButtonType.Circle }) {
64. SymbolGlyph($r('sys.symbol.mic_fill'))
65. .fontSize(24)
66. .fontColor([$r('sys.color.font_secondary')])
67. }
68. .aspectRatio(1)
69. .height(45)
70. .backgroundColor($r('sys.color.background_secondary'))
71. .margin({ right: 10 })
72. }
73. }
74. .backgroundColor($r('sys.color.background_primary'))
75. .borderRadius(30)
76. }
77. }
78. .width('100%')
79. .justifyContent(FlexAlign.Center)
80. .alignItems(HorizontalAlign.Center)
81. }
82. }
```

### 【示例二】

在图片浏览类应用（如相册或电商商品详情页）的开发中，通常需要实现图片的缩放查看功能。Scroll组件的缩放功能（如设置最大/最小缩放比例以及弹性缩放效果）需要较高的系统API Level支持（API 20及以上版本）。

为了确保应用在低版本系统上不会因调用不支持的API而崩溃，同时在高版本系统上能提供更丰富的交互体验，可以通过设备API Level判断来动态启用这些高级功能。

在本示例中，创建了一个自定义属性修饰器MyModifier，在其applyNormalAttribute方法中检查当前设备的sdkApiVersion。当检测到设备版本符合要求（API Level≥20）时，才会为Scroll容器设置缩放相关的属性（maxZoomScale, minZoomScale, enableBouncesZoom）。这样，高版本设备用户可以享受流畅的图片缩放体验，而低版本设备用户则仍能正常浏览图片，只是无法进行缩放操作，从而实现了兼容性适配。

```
1. import { deviceInfo } from '@kit.BasicServicesKit';
2. class MyModifier implements AttributeModifier<ScrollAttribute> {
3. applyNormalAttribute(instance: ScrollAttribute): void {
4. // Judgment is made by the api version information of deviceInfo
5. if (deviceInfo.sdkApiVersion >= 20) {
6. // To adapt to the Scroll scaling property, you can set the minimum and maximum scaling ratios
7. instance.maxZoomScale(1.2)
8. instance.minZoomScale(0.5)
9. instance.enableBouncesZoom(true)
10. }
11. }
12. }
13. @Component
14. export struct ScrollComponentAdapter {
15. adaptModifier: MyModifier = new MyModifier();
16. build() {
17. Scroll() {
18. // 'app.media.image1' is just an example, please replace the actual image.
19. Image($r('app.media.startIcon'))
20. }
21. .scrollable(ScrollDirection.FREE)
22. .width('100%')
23. .attributeModifier(this.adaptModifier)
24. }
25. }
```

### 【示例三】

在新闻资讯或实时信息展示类应用中，经常需要实现文字跑马灯（Marquee）效果，以便在有限空间内展示较长的文本内容（如新闻标题或重要通知）。Text组件的跑马灯功能需要API 18及以上版本才能支持。

为了确保应用在低版本系统上正常运行，同时在高版本系统上提供更生动的视觉效果，需要根据设备版本动态启用此特性。

本示例展示了如何通过版本判断实现文本跑马灯功能的条件式启用。通过自定义属性修饰器MyModifier，在applyNormalAttribute()方法中检查设备API Level。当设备版本达到18或以上时，才会为Text组件设置文本溢出模式为跑马灯（TextOverflow.MARQUEE）并启动滚动效果（marqueeOptions）。这样，高版本设备用户可以看到动态滚动的文字效果，增强信息展示的吸引力，而低版本设备用户则看到静态文本（可能会被截断或显示为省略号），保证了基础的信息可读性，实现了功能体验与兼容性的平衡。

```
1. import { deviceInfo } from "@kit.BasicServicesKit";
2. class MyModifier implements AttributeModifier<TextAttribute> {
3. applyNormalAttribute(instance: TextAttribute): void {
4. // Judgment is made by the api version information of deviceInfo
5. if (deviceInfo.sdkApiVersion >= 18) {
6. // Adapts to the Text component API 18 marquee property
7. instance.textOverflow({ overflow: TextOverflow.MARQUEE })
8. instance.marqueeOptions({ start: true })
9. }
10. }
11. }
12. @Component
13. export struct TextComponentAdapter {
14. private message: string = 'This a simple Code of Text Marquee';
15. private adaptModifier: MyModifier = new MyModifier();
16. build() {
17. Text(this.message)
18. .fontSize(24)
19. .height(200)
20. .width('100%')
21. .attributeModifier(this.adaptModifier)
22. }
23. }
```

## 通过**@**Available注解标注最低适用版本

在API 22之前版本，开发者仅能通过手动编写注释文本的方式标注方法的最低适用版本，这种方式存在版本约束传递不精准的问题。为此，系统提供**@Available****注解**，助力开发者更规范、高效地管控API的调用过程的版本依赖场景。当然**@Available**本身提供的特性不只是为了提供消除兼容性告警，而是让开发者通过**@Available**标注相关接口，然后根据自己的业务需求再去对需要标注的接口本身的行为进行判断。

### 使用说明

1. **@Available注解参数**
   * minApiVersion表示API最低引入版本，由系统类型和版本号组成，当且仅当系统类型为OpenHarmony时可省略。
   * 在OpenHarmony工程中使用时，minApiVersion字段不支持填写HarmonyOS。

   例如：@Available({minApiVersion: '22'})、@Available({minApiVersion: 'OpenHarmony 22'})、@Available({minApiVersion: 'HarmonyOS 6.0.2'})
2. **@Available声明周期**

   源码级注解，仅参与编译过程。
3. **@Available使用限制**
   * 可以标注在变量声明、类型声明（struct、class、interface、typeAlias、enum）、函数声明、命名空间声明、注解声明以及struct、class、interface的成员上。
   * 不可以标注在非声明式元素上。

### 校验逻辑

编译器依据项目配置的compatibleSdkVersion进行校验，若该版本低于被注解API的引入版本，编译器将触发兼容性告警，提示低版本系统运行时可能因调用未存在的 API 导致崩溃。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/3DlA0YrwS2y5Y498xZr5yQ/zh-cn_image_0000002566867725.png?HW-CC-KV=V1&HW-CC-Date=20260429T052519Z&HW-CC-Expire=86400&HW-CC-Sign=05EA1D19DD01AD95A2917A711B1A004B5391047D9242C96E9FB541D472613AD9 "点击放大")

### 正反示例

**HarmonyOS工程****正例：**

```
1. @Available({minApiVersion: 'OpenHarmony 22'}) // 表示该API在API version 22及以上的OpenHarmony兼容设备可用。
2. class testClassA {}

4. @Available({minApiVersion: '22'}) // 表示该API在API version 22及以上的OpenHarmony兼容设备可用。
5. class testClassB {}

7. @Available({minApiVersion: 'HarmonyOS 6.0.2'}) // 表示该API在版本为6.0.2(22)及以上的HarmonyOS兼容设备可用。
8. class testClassC {}
```

**HarmonyOS工程反例：**

```
1. // 版本号校验异常,OpenHarmony 版本号正确格式为1-999的整数
2. // 编辑和编译有如下报错：The runtime OS for the current project is HarmonyOS. The OS version number 9999 is invalid. The OpenHarmony version must be an integer between 1 and 999.
3. @Available({minApiVersion: '9999'})
4. class testClassA {}

6. // 版本号校验异常，HarmonyOS的版本号正确格式为M.S.F，M的范围为1-99的整数，S的范围为0-99的整数，F的范围为0-99的整数。
7. // 编辑和编译产生报错：The runtime OS for the current project is HarmonyOS. The OS version number 6.0.0.0 is invalid. The OpenHarmony version must be an integer between 1 and 999,
8. // and the HarmonyOS version must follow the M.S.F format, where M is an integer between 1 and 99, and S and F are integers between 0 and 99.
9. @Available({minApiVersion: 'HarmonyOS 6.0.2.0'})
10. class testClassB {}

12. // 系统类型校验异常，HarmonyOS工程目前仅支持HarmonyOS和OpenHarmony
13. // 编辑和编译产生报错：The runtime OS for the current project is HarmonyOS. @Available is not supported on the OS: OpenHarmonyNew.
14. @Available({minApiVersion: "OpenHarmonyNew 22"})
15. class testClassC {}
```

**OpenHarmony工程正例：**

```
1. @Available({minApiVersion: 'OpenHarmony 22'}) // 表示该API在API version 22及以上的OpenHarmony兼容设备可用。
2. class testClassA {}

4. @Available({minApiVersion: '22'}) //表示该API从API version为22及以上的OpenHarmony兼容设备可用。
5. class testClassB {}
```

**OpenHarmony工程反例：**

```
1. // 版本号校验异常，OpenHarmony 版本号正确格式为1-999的整数
2. // 编辑和编译产生报错：The runtime OS for the current project is OpenHarmony. The OS version number 9999 is invalid. The OpenHarmony version must be an integer between 1 and 999.
3. @Available({minApiVersion: '9999'})
4. class testClassA {}

6. // OSName校验异常，OpenHarmony工程目前使用@Available注解时，注解参数中的系统类型只支持OpenHarmony
7. // 编辑和编译产生报错：The runtime OS for the current project is OpenHarmony. @Available is not supported on the OS: HarmonyOS.
8. @Available({minApiVersion: 'HarmonyOS 6.0.2'})
9. class testClassB {}

11. // 系统类型校验异常，OpenHarmony工程目前使用@Available注解时，注解参数中的系统类型只支持OpenHarmony
12. // 编辑和编译产生报错：The runtime OS for the current project is OpenHarmony. @Available is not supported on the OS: OpenHarmonyNew.
13. @Available({minApiVersion: "OpenHarmonyNew 22"})
14. class testClassC {}
```

### 场景示例

应用开发者在使用其他开发者提供的API时，可以通过查看其@Available注解来判断该API是否能在自己应用所支持的最低系统版本上运行。

当应用开发者提供有版本约束的API给其他开发者（例如通过 HAR 包）使用时，也应该在提供的API上使用@Available注解，以标明这些API是在哪个系统版本中引入的。

**场景**

当应用开发者在版本迭代中新增调用系统能力的公共API时，需通过@Available注解为该API标注最低可用版本。当API调用方的运行环境版本低于注解中声明的最低版本要求时，编译及编辑阶段会触发兼容性告警，提示开发者注意版本适配问题。针对此类兼容性告警，调用方可通过可使用兼容性告警消除的几种方式消除告警提示。

**提供方示例**

```
1. import { Available } from '@kit.BasicServicesKit';

3. @Available({minApiVersion: '22'})
4. export function commonPrintUtil(): void {
5. // 调用6.0.2(22)版本的新接口
6. }
```

**调用方示例**

```
1. import { Available, deviceInfo } from '@kit.BasicServicesKit';
2. import { commonPrintUtil} from '../../util';

4. // 不建议写法：如果HarmonyOS工程根目录下build-profile.json5文件设置的compatibleSdkVersion值小于22，假设当前HarmonyOS工程的compatibleSdkVersion是5.0.3(15)
5. // 直接调用myFunc方法且没有做版本判断处理，编译器会在myFunc方法调用处抛出告警，提示该方法可能在低版本设备上运行失败
6. function businessFuncA(): void {
7. commonPrintUtil(); // 告警：The 'commonPrintUtil' API is available since SDK version 22. However, the current compatible SDK version is 5.0.3(15).
8. }

10. // 建议写法1：使用deviceInfo.sdkApiVersion获取系统软件API版本进行判断，可以避免低版本设备运行异常，消除编译告警
11. function businessFuncB(): void {
12. if (deviceInfo.sdkApiVersion >= 22) {
13. commonPrintUtil();
14. } else {
15. // 根据业务处理
16. }
17. }

19. // 建议写法2：在myFunc调用处的父级函数（或类）上，标记@Available起始版本信息，当新标记的版本号不低于 myFunc的最低可用版本, 消除编译告警
20. @Available({minApiVersion: '22'})
21. function businessFuncC(): void {
22. commonPrintUtil();
23. }
```
