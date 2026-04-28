---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-5101
title: OS平台API行为的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > OS平台行为变更说明 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:00+08:00
doc_updated_at: 2026-02-09
content_hash: sha256:f8e7347f7d3a7c04d2e98b4e97d059a508a1604ce472f19802230a375684fa08
---

## ArkTS

### 默认不合并依赖混淆规则变更说明

**变更原因**

混淆默认合并依赖混淆规则，由于部分开发者不了解混淆机制，在发布的三方库中的obfuscation.txt文件中引入了混淆开关选项，其它应用依赖这些三方库后出现应用启动崩溃，且开发者无法直接感知这些三方库引入了混淆开关。

**变更影响**

此变更涉及应用适配。

变更前:

编译一个模块时，生效的混淆规则为当前模块所有混淆配置与依赖模块及三方库**所有混淆配置**合并后的结果：

即如果当前模块、依赖的HAR模块、依赖的三方库中混淆配置如下：

```
1. // current-obfuscation-rules.txt
2. -enable-toplevel-obfuscation
3. -keep-global-name
4. currentVar

6. // dependencyHar-consumer-rule.txt
7. -enable-property-obfuscation
8. -keep-global-name
9. harVar
10. -keep-property-name
11. harProp

13. // dependencyThirdParty-obfuscation.txt
14. -compact
15. -keep-property-name
16. thirdPartyProp
```

那么编译当前模块时生效的混淆规则为：

```
1. -enable-toplevel-obfuscation
2. -enable-property-obfuscation
3. -compact
4. -keep-global-name
5. currentVar
6. harVar
7. -keep-property-name
8. harProp
9. thirdPartyProp
```

变更后:

编译一个模块时，生效的混淆规则为当前模块所有混淆配置与依赖模块及三方库的**混淆保留选项**合并后的结果：

即对于上面的例子，编译当前模块时生效的混淆规则为：

```
1. -enable-toplevel-obfuscation
2. -keep-global-name
3. currentVar
4. harVar
5. -keep-property-name
6. harProp
7. thirdPartyProp
```

**起始API Level**

10

**变更的接口/组件**

不涉及

**适配指导**

在当前编译模块的混淆配置文件obfuscation-rules.txt中配置混淆开关选项-enable-lib-obfuscation-options，可实现编译当前模块时合并依赖模块及三方库中所有的混淆配置，即规则合并功能与变更前一致。

## ArkUI

### getKeyboardAvoidMode接口返回值变更

**变更原因**

getKeyboardAvoidMode接口实际返回值为字符串，与文档描述返回值为KeyboardAvoidMode枚举值类型不符。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

* 变更前：getKeyboardAvoidMode接口返回字符串类型。
* 变更后：getKeyboardAvoidMode接口返回KeyboardAvoidMode枚举值，为整数类型。

**起始API Level**

11

**变更的接口/组件**

getKeyboardAvoidMode

**适配指导**

如下代码实现：

```
1. //EntryAbility.ets
2. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window } from '@kit.ArkUI';
5. import { KeyboardAvoidMode } from '@kit.ArkUI';

7. const DOMAIN = 0x0000;

9. export default class EntryAbility extends UIAbility {
10. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
11. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
12. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
13. }

15. onDestroy(): void {
16. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
17. }

19. onWindowStageCreate(windowStage: window.WindowStage): void {
20. // Main window is created, set main page for this ability
21. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

23. windowStage.loadContent('pages/Index', (err) => {
24. let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
25. hilog.info(0x0000, '========keyboardAvoidMode========: %{public}s', JSON.stringify(keyboardAvoidMode));
26. if (keyboardAvoidMode === KeyboardAvoidMode.OFFSET) {
27. windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE)
28. }
29. let keyboardAvoidMode1 = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
30. hilog.info(0x0000, '========keyboardAvoidMode========: %{public}s', JSON.stringify(keyboardAvoidMode1));
31. if (err.code) {
32. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
33. return;
34. }
35. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
36. });
37. }

39. onWindowStageDestroy(): void {
40. // Main window is destroyed, release UI related resources
41. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
42. }

44. onForeground(): void {
45. // Ability has brought to foreground
46. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
47. }

49. onBackground(): void {
50. // Ability has back to background
51. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
52. }
53. }
```

```
1. //Index.ets
2. @Entry
3. @Component
4. struct KeyboardAvoidExample1 {
5. build() {
6. Column() {
7. Row().height("30%").width("100%").backgroundColor(Color.Gray)
8. TextArea().width("100%").borderWidth(1)
9. Text("I can see the bottom of the page").width("100%").textAlign(TextAlign.Center).backgroundColor('rgb(179,217,235)').layoutWeight(1)
10. }.width('100%').height("100%")
11. }
12. }
```

### XComponent组件上使用renderFit接口显示效果变更

**变更原因**

优化XComponent组件上使用renderFit接口显示效果的正确性。

**变更影响**

此变更要求涉及XComponent组件上使用renderFit接口的应用进行适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

* 变更前：在XComponent组件上使用renderFit接口，使用部分fit模式的显示效果不符合预期。
* 变更后：XComponent组件上使用renderFit接口后，可以正确显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/GMd5rSfBT3yywGJPLEJsVQ/zh-cn_image_0000002295394565.png?HW-CC-KV=V1&HW-CC-Date=20260427T233458Z&HW-CC-Expire=86400&HW-CC-Sign=5227CD4F5AAFC06A4CBCD6A267168B3261CB6F457EBB44219B64333AAF4E79A7)

**起始API Level**

10

**变更的接口/组件**

涉及接口: renderFit。

涉及组件: XComponent组件。

**适配指导**

默认行为变更，涉及XComponent组件上使用renderFit接口的应用进行适配，若出现显示效果变更，则需要按照正确效果进行布局。

### 当使用自定义组件名和内置属性重名时编译报错变更

**变更原因**

当使用自定义组件名和内置属性重名时，编译会根据指定的白名单进行拦截报错，如果白名单中不存在，编译就拦截不到，导致编译转换后的产物出现问题。

**变更影响**

该变更涉及应用适配。

举例说明，执行以下用例：

```
1. @Entry
2. @Component
3. struct enableAnalyzer {
4. build() {
5. Canvas()
6. .enableAnalyzer(true)
7. }
8. }
```

变更前：

不在白名单的内置组件属性与自定义组件重名时，编译没有拦截报错，导致运行时crash。

变更后：

在白名单的内置组件属性与自定义组件重名时，编译拦截报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/YcqoScOgSOC4uBnwOnSiVg/zh-cn_image_0000002260714460.png?HW-CC-KV=V1&HW-CC-Date=20260427T233458Z&HW-CC-Expire=86400&HW-CC-Sign=ABBB611FDCEA44E8E5F293F7A7E08B66D88D480B0F87538215D4D4C5CBFB5811)

**起始API Level**

10

**变更的接口/组件**

ArkUI 内置组件属性API。

**适配指导**

自定义组件名和内置组件属性重名时，编译报错，修改自定义组件名为其他非内置组件属性名即可解决。

修改前：

自定义组件enableAnalyzer和Canvas的enableAnalyzer重名。

```
1. @Entry
2. @Component
3. struct enableAnalyzer {
4. build() {
5. Canvas()
6. .enableAnalyzer(true)
7. }
8. }
```

修改后：

将自定义组件名改为任意不和内置组件重名的名称，如EnableAnalyzerComp。

```
1. @Entry
2. @Component
3. struct EnableAnalyzerComp {
4. build() {
5. Canvas()
6. .enableAnalyzer(true)
7. }
8. }
```

### CanvasRenderingContext2D方法传NaN和Infinity值后执行的其他绘制方法由不绘制变更为正常绘制

**变更原因**

CanvasRenderingContext2D绘制路径时，若存在方法的number类型参数传入NaN或Infinity值，部分内容无法绘制或绘制异常，与Html5的行为不一致。

**变更影响**

此变更不涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

变更前：绘制路径时，若存在路径方法的number类型参数传入NaN或Infinity值，整个路径无法绘制；对画布进行缩放、旋转、移动或使用变换矩阵进行图形变化时，number类型参数传入NaN或Infinity值，后面执行的方法无法绘制。

变更后：绘制路径时，传入NaN或Infinity值的方法不做处理，根据有效的路径参数进行绘制；对画布进行缩放、旋转、移动或使用变换矩阵进行图形变化时，number类型参数传入NaN或Infinity值，其他传入有效参数的方法正常绘制。

具体接口的差异如下：

| 方法 | 变更前 | 变更后 |
| --- | --- | --- |
| moveTo | 任一路径绘制方法的number类型参数传入NaN或Infinity值时，整个路径无法绘制。 | 路径绘制方法的number类型参数传入NaN或Infinity值时，该方法不生效。其他传入有效参数的路径绘制方法正常绘制。 |
| lineTo | 任一路径绘制方法的number类型参数传入NaN或Infinity值时，整个路径无法绘制。 | 路径绘制方法的number类型参数传入NaN或Infinity值时，该方法不生效。其他传入有效参数的路径绘制方法正常绘制。 |
| bezierCurveTo | 任一路径绘制方法的number类型参数传入NaN或Infinity值时，整个路径无法绘制。 | 路径绘制方法的number类型参数传入NaN或Infinity值时，该方法不生效。其他传入有效参数的路径绘制方法正常绘制。 |
| quadraticCurveTo | 任一路径绘制方法的number类型参数传入NaN或Infinity值时，整个路径无法绘制。 | 路径绘制方法的number类型参数传入NaN或Infinity值时，该方法不生效。其他传入有效参数的路径绘制方法正常绘制。 |
| arc | 任一路径绘制方法的number类型参数传入NaN或Infinity值时，整个路径无法绘制。 | 路径绘制方法的number类型参数传入NaN或Infinity值时，该方法不生效。其他传入有效参数的路径绘制方法正常绘制。 |
| ellipse | 任一路径绘制方法的number类型参数传入NaN或Infinity值时，整个路径无法绘制。 | 路径绘制方法的number类型参数传入NaN或Infinity值时，该方法不生效。其他传入有效参数的路径绘制方法正常绘制。 |
| rect | 任一路径绘制方法的number类型参数传入NaN或Infinity值时，整个路径无法绘制。 | 路径绘制方法的number类型参数传入NaN或Infinity值时，该方法不生效。其他传入有效参数的路径绘制方法正常绘制。 |
| arcTo | 任一路径绘制方法的number类型参数传入NaN或Infinity值时，整个路径无法绘制。 | 路径绘制方法的number类型参数传入NaN或Infinity值时，该方法不生效。其他传入有效参数的路径绘制方法正常绘制。 |
| globalAlpha | 绘制方法的number类型参数传入NaN或Infinity值，在该方法后执行的绘制方法无法绘制。 | number类型参数传入NaN或Infinity值参数时该方法不生效。其他传入有效参数的绘制方法正常绘制。 |
| rotate | 绘制方法的number类型参数传入NaN或Infinity值，在该方法后执行的绘制方法无法绘制。 | number类型参数传入NaN或Infinity值参数时该方法不生效。其他传入有效参数的绘制方法正常绘制。 |
| scale | 绘制方法的number类型参数传入NaN或Infinity值，在该方法后执行的绘制方法无法绘制。 | number类型参数传入NaN或Infinity值参数时该方法不生效。其他传入有效参数的绘制方法正常绘制。 |
| transform | 绘制方法的number类型参数传入NaN或Infinity值，在该方法后执行的绘制方法无法绘制。 | number类型参数传入NaN或Infinity值参数时该方法不生效。其他传入有效参数的绘制方法正常绘制。 |
| setTransform | 绘制方法的number类型参数传入NaN或Infinity值，在该方法后执行的绘制方法无法绘制。 | number类型参数传入NaN或Infinity值参数时该方法不生效。其他传入有效参数的绘制方法正常绘制。 |
| translate | 绘制方法的number类型参数传入NaN或Infinity值，在该方法后执行的绘制方法无法绘制。 | number类型参数传入NaN或Infinity值参数时该方法不生效。其他传入有效参数的绘制方法正常绘制。 |
| lineDashOffset | 设置了虚线样式的线条绘制出来是实线。 | 设置了虚线样式的线条绘制出来是虚线。 |

| 示例 | 变更前 | 变更后 |
| --- | --- | --- |
| context.moveTo(100, 100)  context.lineTo(NaN, 100)  context.lineTo(200, 200)  context.stroke() | 无绘制内容 |  |

**起始API Level**

9

**变更的接口/组件**

CanvasRenderingContext2D

OffscreenCanvasRenderingContext2D

Path2D

**适配指导**

默认行为变更，无需适配，但应注意变更后的行为是否对整体应用逻辑产生影响。

### CanvasRenderingContext2D的drawImage接口默认单位变更

**变更原因**

当drawImage传入9个参数时，若首个参数（image）为PixelMap类型，则第2至第5个参数（sx、sy、sw和sh）以px为单位进行解析。与文档描述不一致，且绘制得到的图片大小存在问题。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

当drawImage传入9个参数时，且首个参数为PixelMap类型时：

* 变更前：第2至第5个参数都会以px为单位进行解析。
* 变更后：第2至第5个参数会以vp为单位进行解析。

|  | 变更前 | 变更后 |
| --- | --- | --- |
| 第2至第5个参数以vp为单位传入 |  |  |
| 第2至第5个参数以px为单位传入 |  |  |

**起始API Level**

9

**变更的接口/组件**

CanvasRenderingContext2D的drawImage接口

**适配指导**

变更后，使用drawImage接口时，若传入9个参数，且首个参数为PixelMap类型时，要注意第2至第5个参数会以vp为单位进行解析。

示例:

```
1. import { image } from '@kit.ImageKit'

3. @Entry
4. @Component
5. struct Demo {
6. private settings: RenderingContextSettings = new RenderingContextSettings(true)
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .onReady(() => {
15. let context = getContext(this)
16. let imageSourceApi = image.createImageSource(context.filesDir + "/view.jpg")
17. let pixelmap = imageSourceApi.createPixelMapSync();
18. let imageInfo = pixelmap.getImageInfoSync()
19. let width = px2vp(imageInfo.size.width)
20. let height = px2vp(imageInfo.size.height)
21. this.context.drawImage(pixelmap, 0, 0, width, height, 50, 50, 250, 200)
22. this.context.drawImage(pixelmap, 0, 0, imageInfo.size.width, imageInfo.size.height, 50, 300, 250, 200)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

### 修复blendMode接口离屏模式会影响组件设置的不透明度的问题

**变更原因**

blendMode离屏模式与不透明度属性（opacity）同时使用时，组件的不透明度并不等于设置的不透明度，效果异常。

**变更影响**

此变更涉及应用适配，仅针对组件设置了blendMode离屏模式且具有不透明度的场景。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

变更前：组件设置了blendMode离屏模式，同时设置了opacity不透明度 A，则组件实际不透明度为 A \* A

变更后：组件设置了blendMode离屏模式，同时设置了opacity不透明度 A，则组件实际不透明度为 A

变更前后效果如下:

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

11

**变更的接口/组件**

blendMode

**适配指导**

如果开发者希望在同时使用blendMode离屏模式和opacity接口时保持组件的不透明度不变，则需要手动调整原本设定的不透明度。例如，在下方示例代码中，在 Stack()上额外设置.opacity(0.5)，以确保实际的透明度为 0.5 \* 0.5。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Stack() {
7. }
8. .height('50%')
9. .width('50%')
10. .backgroundColor(0x0A59F7)
11. .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN)
12. .opacity(0.5)  // 变更后需要额外设置0.5的不透明度保证实际透明度为 0.5*0.5
13. }
14. .height('100%')
15. .width('100%')
16. .backgroundColor(0xFFFFFF)
17. .opacity(0.5)
18. }
19. }
```

### XComponent设置为Texture模式使用blendMode接口的行为由不生效变更为正常生效

**变更原因**

用户使用XComponent组件并设置为Texture模式时，使用blendMode接口没有效果，不符合接口正常规格，需要变更为blendMode接口正常生效。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

变更前：XComponent组件设置为Texture模式，使用blendMode接口不生效。

变更后：XComponent组件设置为Texture模式，使用blendMode接口正常生效。

**起始API Level**

11

**变更的接口/组件**

common.d.ts文件的blendMode接口。

**适配指导**

需适配场景：

当应用使用XComponent组件并设置为Texture模式（type设置为XComponentType.TEXTURE）时，使用blendMode接口，可能会出现显示效果变更前后不一致的情况，以下是使用场景示意：

```
1. @Entry
2. @Component
3. struct Index {
4. private contextOne: Record<string, () => void> = {};
5. private contextTwo: Record<string, () => void> = {};

7. build() {
8. Column() {
9. Stack() {
10. XComponent({
11. id: 'circle',
12. type: XComponentType.TEXTURE,
13. libraryname: 'nativerender'
14. }).height(50)
15. .backgroundColor(Color.Transparent)
16. .onLoad((contextOne?: object | Record<string, () => void>) => {
17. if (contextOne) {
18. this.contextOne = contextOne as Record<string, () => void>;
19. }
20. })

22. XComponent({
23. id: 'rect',
24. type: XComponentType.TEXTURE,
25. libraryname: 'nativerender'
26. }).height(50)
27. .backgroundColor(Color.Transparent)
28. .onLoad((contextTwo?: object | Record<string, () => void>) => {
29. if (contextTwo) {
30. this.contextTwo = contextTwo as Record<string, () => void>;
31. }
32. })
33. .blendMode(BlendMode.XOR) // 变更后生效，若需保持变更前行为，可使用BlendMode.None入参
34. }
35. .height(50)
36. .onClick(() => {
37. if (this.contextOne) {
38. this.contextOne.drawCircle();
39. }
40. if (this.contextTwo) {
41. this.contextTwo.drawRectangle();
42. }
43. })
44. }
45. .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN)
46. .width('100%')
47. .height('100%')
48. }
49. }
```

| 混合类型 | 变更前 | 变更后 |
| --- | --- | --- |
| BlendMode.XOR |  |  |
| BlendMode.NONE |  |  |

应用若需保持变更前行为，XComponent组件上的blendMode接口使用BlendMode.None入参即可。

### setSpecificSystemBarEnabled接口在横屏的行为变更

**变更原因**

修正接口规格，保证接口调用在不同场景下均可正常控制状态栏显隐。

**变更影响**

此变更涉及应用适配。

变更前：应用窗口处于横屏状态时，应用使用该接口设置状态栏显隐不生效，状态栏始终处于隐藏状态。

变更后：应用启动之后，若使用该接口设置过状态栏的显隐，状态栏的显隐状态则以应用的设置（多次设置，以最后一次设置状态为准）为准来生效。

**起始API Level**

12

**变更的接口/组件**

Window#setSpecificSystemBarEnabled(name: SpecificSystemBar, enable: boolean, enableAnimation?: boolean): Promise<void>

**适配指导**

针对应用预期在横屏时隐藏状态栏的场景，需确认应用自启动之后是否使用该接口主动设置过状态栏显示，若应用设置过状态栏显示，需再次设置状态栏隐藏，才能实现应用横屏时隐藏状态栏。

### 滚动组件通用接口backToTop属性默认值变更

**变更原因**

List、Grid、Scroll和WaterFlow组件默认不支持点击状态栏回到顶部，为了推广点击状态栏回到顶部特性，提升应用体验，List、Grid、Scroll和WaterFlow组件修改为默认支持点击状态栏回到顶部。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

* 变更前：List、Grid、Scroll和WaterFlow组件backToTop属性默认值为false，默认不支持点击状态栏回到顶部。
* 变更后：API 18及以后版本，List、Grid、Scroll和WaterFlow组件滚动方向为垂直方向时，backToTop属性默认值为true，默认支持点击状态栏回到顶部。

**起始API Level**

15

**变更的接口/组件**

涉及接口：backToTop属性。

涉及组件：List、Grid、Scroll和WaterFlow组件。

**适配指导**

默认行为变更，涉及List、Grid、Scroll和WaterFlow组件的应用需进行适配，若期望不支持点击状态栏回到顶部功能，则需要设置backToTop属性为false。

### 页面退出场景自定义组件删除前移

**变更原因**

在页面退出动画的过程中，UI处于空闲状态。动画结束后，由于释放大量组件导致页面卡顿。可以将页面中自定义组件的释放提前，显著减轻卡顿并优化性能。

**变更影响**

此变更涉及应用适配（仅针对Router和Navigation页面默认的退出动画场景）。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

* 变更前：页面退出动画结束后，依次执行自定义组件生命周期aboutToDisappear、onDisappear。
* 变更后：页面退出动画过程中，执行自定义组件生命周期aboutToDisappear。退出动画执行结束后，执行生命周期onDisappear。

**起始API Level**

7

**变更的接口/组件**

自定义组件的onDisappear生命周期回调。

**适配指导**

在全局复用场景中，当复用的自定义组件的aboutToDisappear生命周期回调中涉及节点移除操作时，应将节点移除操作安排在页面退出完成后，例如onDetach生命周期。

### V1和V2组件冻结能力增强

**变更原因**

开发者使用组件冻结功能后，以下场景冻结功能实际未生效：支持冻结的组件嵌套使用的解冻场景、V2自定义组件的解冻场景、Repeat VirtualScroll的复用场景。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

变更前：启用组件冻结，组件冻结实际功能未生效，因此在组件嵌套使用的解冻场景、V2自定义组件的冻结场景、Repeat VirtualScroll的复用场景，其相关的状态变量能够刷新、@Watch/@Monitor方法会执行。

变更后：启用组件冻结，组件冻结实际功能会生效，在组件嵌套使用的解冻场景、V2自定义组件的冻结场景、Repeat VirtualScroll的复用场景，其相关的状态变量不再刷新、@Watch/@Monitor方法不会执行。

举例说明，执行以下用例：

```
1. @Entry
2. @ComponentV2
3. struct RepeatVirtualScrollDemo {
4. @Local simpleList: Array<string> = [];
5. @Local bgColor: Color = Color.Pink;

7. aboutToAppear(): void {
8. for (let i = 0; i < 7; i++) {
9. this.simpleList.push(`item${i}`);
10. }
11. }

13. build() {
14. Column() {
15. Row() {
16. Button(`Reduce length to 5`)
17. .onClick(() => {
18. this.simpleList = this.simpleList.slice(0, 5);
19. })
20. Button(`Change bgColor`)
21. .onClick(() => {
22. this.bgColor = this.bgColor == Color.Pink ? Color.Blue : Color.Pink;
23. })
24. }

26. List() {
27. Repeat(this.simpleList)
28. .each((obj: RepeatItem<string>) => {
29. })
30. .key((item: string, index: number) => item)
31. .virtualScroll({ totalCount: this.simpleList.length })
32. .templateId(() => `a`)
33. .template(`a`, (ri) => {
34. ChildComponent({
35. message: ri.item,
36. bgColor: this.bgColor
37. })
38. }, { cachedCount: 2 })
39. }
40. .cachedCount(0)
41. .height(500)
42. }
43. .height(`100%`)
44. }
45. }

47. @ComponentV2({ freezeWhenInactive: true })
48. struct ChildComponent {
49. @Param @Require message: string;
50. @Param @Require bgColor: Color;
51. // 支持后二级缓存中的组件不刷新，不会打印相应日志
52. @Monitor(`bgColor`)
53. onMessageChange(monitor: IMonitor) {
54. monitor.dirty.forEach((path: string) => {
55. console.log(`repeat---${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`)
56. })
57. }

59. build() {
60. Text(`[a]: ${this.message}`)
61. .fontSize(50)
62. .backgroundColor(this.bgColor)
63. }
64. }
```

**起始API Level**

12

**变更的接口/组件**

freezeWhenInactive。

**适配指导**

展示效果不变，组件冻结生效后，@Monitor/@Watch将不再执行。如果需要刷新缓存中的数据，可以关闭组件冻结。

```
1. // 关闭组件冻结，freezeWhenInactive设置为false
2. @ComponentV2({ freezeWhenInactive: false })
3. struct ChildComponent {
4. @Param @Require message: string;
5. @Param @Require bgColor: Color;
6. // 关闭冻结后，二级缓存中的组件会刷新，并打印相应日志
7. @Monitor(`bgColor`)
8. onMessageChange(monitor: IMonitor) {
9. monitor.dirty.forEach((path: string) => {
10. console.log(`repeat---${path} change from ${monitor.value(path)?.before} to ${monitor.value(path)?.now}`)
11. })
12. }

14. build() {
15. Text(`[a]: ${this.message}`)
16. .fontSize(50)
17. .backgroundColor(this.bgColor)
18. }
19. }
```

示例中仅展示了Repeat VirtualScroll的复用场景，其他场景如下：

* 组件嵌套使用的解冻场景：在组件冻结开启之后，明确了节点解冻的范围，子组件的非屏上节点不会再被父组件解冻，例子可见[Navigation和TabContent的混用](../harmonyos-guides/arkts-custom-components-freeze.md#组件混用)。
* V2自定义组件的冻结场景：在状态管理V2组件冻结从父组件激活冻结状态的场景中，如果仅子组件开启了冻结，父组件未开启冻结，子组件也能冻结。例子可见[仅子组件开启组件冻结](../harmonyos-guides/arkts-custom-components-freezev2.md#仅子组件开启组件冻结)。

### ArkUI双指长按行为变更

**变更原因**

在手机、平板设备上，优先响应系统双指操作，默认禁用应用内双指长按。

**变更影响**

此变更涉及应用适配。变更后双指长按手势事件默认为系统事件。如果应用需使用双指长按，可通过[IssueReporter平台](https://issuereporter.developer.huawei.com/my-created)向华为申请白名单例外处理。

变更前：应用可通过LongPressGesture长按手势的fingers参数指定触发长按的最少手指数，手指数大于等于1时，即可触发长按手势事件。不指定触发长按的最小手指数时，默认为1。

变更后：使用两根手指长按组件时，不会触发长按手势。使用一根及多根手指长按组件时，长按手势事件触发不受影响。

**起始API Level**

7

**变更的接口/组件**

长按手势 LongPressGesture

## Audio Kit

### 音频框架识别USB音频设备类型行为变更

**变更原因**

原有的USB音频设备在系统侧均识别为耳机输入/输出设备。为了提高识别的准确度，满足应用的UX显示需求，系统侧区分USB耳机和普通的USB音频设备(如音箱)。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

ArkTS API

| 平台 | 变更前 | 变更后 |
| --- | --- | --- |
| 通用 | 同USB地址下只有输入设备，识别为USB\_HEADSET。 | 同USB地址下只有输入设备，识别为USB\_DEVICE。 |
| PC/2in1 | 同USB地址下只有输出设备，识别为USB\_HEADSET。 | 同USB地址下只有输出设备，识别为USB\_DEVICE。 |

C API

| 平台 | 变更前 | 变更后 |
| --- | --- | --- |
| 通用 | 同USB地址下只有输入设备，识别为AUDIO\_DEVICE\_USB\_HEADSET。 | 同USB地址下只有输入设备，识别为AUDIO\_DEVICE\_USB\_DEVICE。 |
| PC/2in1 | 同USB地址下只有输出设备，识别为AUDIO\_DEVICE\_USB\_HEADSET。 | 同USB地址下只有输出设备，识别为AUDIO\_DEVICE\_USB\_DEVICE。 |

**起始API Level**

9

**变更的接口/组件**

ArkTS：@ohos.multimedia.audio.d.ts中DeviceType的USB\_HEADSET接口。

C API: native\_audio\_device\_base.h中OH\_AudioDevice\_Type的AUDIO\_DEVICE\_USB\_HEADSET接口。

**适配指导**

ArkTS API

如应用对USB音频设备有特殊处理需求，现在不仅需要处理USB\_HEADSET类型的音频设备，还需将USB\_DEVICE类型也纳入到处理范围内。

```
1. // 针对usb音频设备做特殊处理
2. if (devicetype == DeviceType.USB_HEADSET) {
3. // do sth
4. }
```

变更后：如应用对USB音频设备有特殊处理需求，不仅要考虑USB\_HEADSET类型，也要考虑USB\_DEVICE类型的音频设备。

```
1. // 针对usb音频设备做特殊处理
2. if (devicetype == DeviceType.USB_HEADSET || devicetype == DeviceType.USB_DEVICE) {
3. // do sth
4. }
```

C API

如应用对USB音频设备有特殊处理需求，现在不仅需要处理AUDIO\_DEVICE\_USB\_HEADSET类型的音频设备，还需将AUDIO\_DEVICE\_USB\_DEVICE类型也纳入到处理范围内。

变更前：如应用对USB音频设备有特殊处理需求，仅处理AUDIO\_DEVICE\_USB\_HEADSET类型的音频设备即可。

```
1. // 针对usb音频设备做特殊处理
2. if (devicetype == OH_AudioDevice_Type.AUDIO_DEVICE_USB_HEADSET) {
3. // do sth
4. }
```

变更后：如应用对USB音频设备有特殊处理需求，不仅要考虑AUDIO\_DEVICE\_USB\_HEADSET类型，也要考虑AUDIO\_DEVICE\_USB\_DEVICE类型的音频设备。

```
1. // 针对usb音频设备做特殊处理
2. if (devicetype == OH_AudioDevice_Type.AUDIO_DEVICE_USB_HEADSET || devicetype == OH_AudioDevice_Type.AUDIO_DEVICE_USB_DEVICE) {
3. // do sth
4. }
```

## Basic Services Kit

### osAccount.distributedAccount.DistributedAccountAbility.getOsAccountDistributedInfo接口返回值生成规则变更

**变更原因**

原接口返回值生成规则与设计不符。

**变更影响**

此变更不涉及应用适配。

变更前：接口返回值中name、id、nickname、avatar 和 scalableData 生成规则与设计不符。

变更后：修正相关属性的生成规则，较变更前，同一分布式账号信息查询结果有差异。

**起始API Level**

9

**变更的接口/组件**

@ohos.account.distributedAccount.d.ts中如下接口:

* getOsAccountDistributedInfo(callback: AsyncCallback<DistributedInfo>): <void>
* getOsAccountDistributedInfo(): Promise<DistributedInfo>

**适配指导**

默认行为变更，无需适配。

## CANN Kit（原HiAI Foundation Kit）

### 原hiai\_foundation目录下的头文件废弃，替换为CANNKit下的头文件

**变更原因**

命名优化。

**变更影响**

此变更涉及应用适配。

在应用导入依赖时，强烈建议使用更名后的kit，即CANNKit目录下的文件。原hiai\_foundation目录将在短暂保留若干版本提供过度之后删除，建议应用择机完成适配。

| C API头文件变更前 | C API头文件变更后 |
| --- | --- |
| hiai\_foundation/hiai\_aipp\_param.h | CANNKit/hiai\_aipp\_param.h |
| hiai\_foundation/hiai\_helper.h | CANNKit/hiai\_helper.h |
| hiai\_foundation/hiai\_options.h | CANNKit/hiai\_options.h |
| hiai\_foundation/hiai\_tensor.h | CANNKit/hiai\_tensor.h |
| hiai\_foundation/hiai\_single\_op.h | CANNKit/hiai\_single\_op.h |

**起始API Level**

4.1.0(11)

**变更的接口/组件**

不涉及

**适配指导**

C API：以导入hiai\_aipp\_param.h为例

导入hiai\_aipp\_param.h时，需要使用新的kit路径，其他代码不需要修改：

变更前：#include "hiai\_foundation/hiai\_aipp\_param.h"

变更后：#include "CANNKit/hiai\_aipp\_param.h"

## Device Security Kit

### Device Security Kit优化错误码上报

**变更原因**

Device Security Kit优化错误码类型，新增更明细的错误码。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

| 变更前 | 变更后 |
| --- | --- |
| 已有错误码：  201 权限校验失败  401 参数检查失败  1010800001 内部异常  1010800002 设备网络异常  1010800003 访问云端服务器异常 | 新增错误码：  801 API不支持  1010800005 调用数量超过并行阈值  1010800006 调用频率超过阈值  1010800007 操作超时  1010800008 云服务流量超过阈值 |

**起始API Level**

12

**变更的接口/组件**

* checkUrlThreat
* checkSysIntegrity

**适配指导**

调用接口需要try...catch捕获异常，获取到异常时可以判断对应错误码信息，做对应的处理。

```
1. const TAG = "SafetyDetectJsTest";
2. try {
3. // 调用URL检测接口或者系统完整性检测接口
4. } catch (err) {
5. let e: BusinessError = err as BusinessError;
6. hilog.error(0x0000, TAG, 'CheckSysIntegrity failed: %{public}d %{public}s', e.code, e.message);
7. // 对不同错误码做处理：
8. // 如果返回801，则该设备不支持当前API，不应再次调用该接口。
9. // 如果返回401，则检查参数规格是否与资料规格一致。
10. // 如果返回1010800005，则当前请求超出请求次数，过一天可恢复使用，此时不应重试。
11. // 如果返回1010800006 ，则可延迟1秒后重试
12. // 如果返回1010800008 ，则延迟5秒重试，如果重试再次失败，则每次以指数递增间隔重试。
13. // 如果返回1010800007，则可重试处理。
14. }
```

## Form Kit

### 卡片支持的接口能力增加校验

**变更原因**

针对支持卡片能力的接口，增加校验。

**变更影响**

此变更不涉及应用适配。

变更后针对未标识卡片能力的接口或模块，卡片UI侧代码会调用失败导致卡片加载显示失败。

**起始API Level**

不涉及

**变更的接口/组件**

不涉及

**适配指导**

默认行为变更，无需适配。

## Media Kit

### 应用创建SoundPool时调用media.createSoundPool接口变更

**变更原因**

原来的应用创建SoundPool实例，一个应用进程只能够创建一个SoundPool实例，为单实例模式，无法满足应用的使用场景。例如很多应用在使用SoundPool的能力的同时，还需要使用TimePicker组件(该组件中封装了SoundPool的能力)，单实例模式会使得SoundPool对象之间互相干扰，影响应用的使用体验。

**变更影响**

此变更不涉及应用适配。

变更前：创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。

变更后：创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

**起始API Level**

18

**变更的接口/组件**

无变更接口

**适配指导**

默认行为变更，无需适配。

## Performance Analysis Kit

### 用户态trace打点格式变更

**变更原因**

优化调整原有用户态trace打点格式，提高用户态trace打点格式的前向兼容性。

**变更影响**

此变更不涉及应用适配。

此变更涉及自研Trace解析工具适配，具体变更内容如表中所示。

变更前：taskId和count字段前的分隔符为空格。

变更后：各字段均使用竖线作为分隔符。

| 打点类型 | API\_C接口 | API\_JS接口 | 变更前打点格式 | 变更后打点格式 |
| --- | --- | --- | --- | --- |
| 开启异步Trace打点 | OH\_HiTrace\_StartAsyncTrace | startTrace | S|PID|H:name taskId | S|PID|H:name|taskId |
| 结束异步Trace打点 | OH\_HiTrace\_FinshAsyncTrace | finishTrace | F|PID|H:name taskId | F|PID|H:name|taskId |
| 整数Trace打点 | OH\_HiTrace\_CountTrace | traceByValue | C|PID|H:name count | C|PID|H:name|count |

**用户态trace格式拓展规则**

对后续新增字段，将以**竖线+字段**的方式，追加在当前打点格式的末尾。

假设 S|PID|H:name|taskId 新增字段args1和args2，用户态trace格式变化如下所示：

* 原格式

  ```
  1. S|PID|H:name|taskId
  ```
* 新增args1和args2字段后格式

  ```
  1. S|PID|H:name|taskId|args1|args2
  ```

  **特殊场景说明** ：因为后续新增字段并不是所有场景都会使用，所以实际字段值可能为空字符串，当有字段为空字符串时，trace格式变化如下所示：

  + args1为空字符串，args2不为空字符串

    ```
    1. S|PID|H:name|taskId||args2
    ```
  + args1不为空字符串，args2为空字符串

    ```
    1. S|PID|H:name|taskId|args1
    ```
  + args1和args2均为空字符串

    ```
    1. S|PID|H:name|taskId
    ```

详细的用户态trace格式说明参考文档[hitracemeter-view](../harmonyos-guides/hitracemeter-view.md)。

**起始API Level**

* OH\_HiTrace\_StartAsyncTrace：10
* OH\_HiTrace\_FinshAsyncTrace：10
* OH\_HiTrace\_CountTrace：10
* startTrace：12
* finishTrace
* traceByValue

**变更的接口/组件**

* OH\_HiTrace\_StartAsyncTrace
* OH\_HiTrace\_FinshAsyncTrace
* OH\_HiTrace\_CountTrace
* startTrace
* finishTrace
* traceByValue

**适配指导**

默认行为变更，无需适配。

自研Trace解析工具可根据前述**变更影响**中对打点格式变更的介绍自行适配。

## Remote Communication Kit

### fetch接口新增错误码返回

**变更原因**

系统决策使用蜂窝网络发送网络请求时，如果不满足拉起蜂窝网络的条件，返回1007900986错误码。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于5.1.0(18)时生效。

API version 18以下不满足拉起蜂窝条件不会抛出1007900986错误码。

API version 18不满足拉起蜂窝条件抛出1007900986错误码。

**起始API Level**

4.1.0(11)

**变更的接口/组件**

fetch接口

**适配指导**

调用接口需要try ctach异常，获取到异常时可以判断对应错误码信息，如果是1007900986错误码，代表当前不满足拉起蜂窝条件（比如用户开启飞行模式、去激活SIM卡等场景）。

```
1. const session = rcp.createSession();
2. let request = new rcp.Request("http://example.com/fetch"); // 请在使用中将其替换为实际的网址。
3. request.configuration = {
4. transfer: {
5. pathPreference: 'cellular', // 系统自动决策是否使用蜂窝网络发送网络请求。
6. }
7. }

9. try {
10. let response = await session.fetch(request);
11. session.close();
12. } catch (err) {
13. let e: BusinessError = err as BusinessError;
14. console.error("testRcpCellular err: " + JSON.stringify(e));
15. session.close();
16. // 对不同错误码做处理：
17. // 如果返回201，可能是没有申请ohos.permission.GET_NETWORK_INFO权限。
18. // 如果返回1007900986，代表该请求适合使用蜂窝网络，但未正确打开或配置蜂窝网络，可以提示用户进行检查。
19. // 其他可能的网络错误。
20. }
```

## NDK开发

### JIT功能默认关闭，需申请权限证书并通过审核后启用

**变更原因**

JIT（Just In Time）即时编译功能可能带来任意代码注入的风险。为了保护应用安全并维护鸿蒙系统的纯净生态，系统默认关闭JSVM的JIT功能，采用解释执行方式执行JS代码。

**变更影响**

此变更涉及应用适配。

变更前：

API 18以下版本，默认开启JIT。

变更后：

API 18及以上版本，默认关闭JIT，需申请权限证书后启用。关闭后，依赖JIT的wasm接口将无法执行，且JIT与解释执行在特定场景下存在些许性能差异。

**起始API Level**

11

**变更的接口/组件**

OH\_JSVM\_CompileWasmModule：无JIT权限会返回JIT\_MODE\_EXPECTED状态码

OH\_JSVM\_CompileWasmFunction：无JIT权限会返回JIT\_MODE\_EXPECTED状态码

OH\_JSVM\_CreateWasmCache：无JIT权限会返回JIT\_MODE\_EXPECTED状态码

OH\_JSVM\_RunScript：无JIT权限执行wasm相关脚本会失败，在特定场景下存在些许性能差异

**适配指导**

新上架应用若期望使用JIT权限，需向应用市场（AppGallery Connect，简称AGC）提交ohos.permission.kernel.ALLOW\_EXECUTABLE\_FORT\_MEMORY受限ACL权限的申请， 并在附带材料中说明使用JSVM引擎JIT功能的具体场景。在权限审批通过后， 开发者可从AGC网站上更新profile证书， 并对应用重新打包上架。权限申请及适配流程可参考《[申请使用受限权限](../harmonyos-guides/declare-permissions-in-acl.md)》指导完成。

说明

适配注意事项：

1. 如果应用未申请相应的权限证书，却试图在配置文件中声明此权限，将会导致应用安装失败。
2. 若在编译时报以下错误日志The ohos.permission.kernel.ALLOW\_EXECUTABLE\_FORT\_MEMORY permission under requestPermissions must be a value that is predefined within the SDK or a custom one that you have included under definePermissions.， 请将SDK更新到最新版本(大于等于5.0.3.130版本)。

## 调试工具

### hiperf命令行调试工具使用权限缩小

**变更原因**

基于对应用的安全隐私保护，调试能力遵循以下原则进行调整：

1.在开发者模式下，开发者只能调试自己的应用，无法调试其他三方APP。

2.调试信息不包含开发者无权读取的信息。

**变更影响**

此变更涉及应用适配。

变更后仅支持对debug应用进行调试。

**起始API Level**

不涉及

**变更的接口/组件**

hiperf命令行工具。

**适配指导**

将release应用修改为debug应用，重新编译调试。
