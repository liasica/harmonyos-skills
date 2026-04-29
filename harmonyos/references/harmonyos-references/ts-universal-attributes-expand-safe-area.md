---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area
title: 安全区域
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 布局与边框 > 安全区域
category: harmonyos-references
scraped_at: 2026-04-29T13:51:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8b8b14ec4732053a1a1fdeb80d7f8ea990c393c594630224ef891531434a5c0e
---

安全区域是指页面的显示区域，默认情况下开发者开发的界面都布局在安全区域内，不与系统设置的避让区比如状态栏、导航栏区域重叠。提供属性方法允许开发者设置组件绘制内容突破安全区域的限制，通过[expandSafeArea](ts-universal-attributes-expand-safe-area.md#expandsafearea)属性支持组件不改变布局情况下扩展其绘制区域至安全区外，通过设置[setKeyboardAvoidMode](ts-universal-attributes-expand-safe-area.md#setkeyboardavoidmode11)来配置虚拟键盘弹出时页面的避让模式。页面中有标题栏等文字不希望和避让区重叠时，建议对组件设置expandSafeArea属性实现沉浸式效果，也可直接通过窗口接口[setWindowLayoutFullScreen](arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现全屏沉浸式效果。

说明

从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

摄像头挖孔区域不属于避让区，页面默认不避让挖孔。

从API version 12开始，可在module.json5中添加以下配置项，摄像头挖孔区域会视为避让区，实现页面默认避让挖孔：

"metadata": [

{

"name": "avoid\_cutout",

"value": "true",

}

],

## expandSafeArea

PhonePC/2in1TabletTVWearable

expandSafeArea(types?: Array<SafeAreaType>, edges?: Array<SafeAreaEdge>): T

控制组件扩展其安全区域。

说明

* 设置expandSafeArea属性进行组件绘制扩展时，建议组件尺寸不要设置固定宽高（百分比除外），当设置固定宽高（包括设置'auto'）时，扩展安全区域的方向只支持[SafeAreaEdge.TOP, SafeAreaEdge.START]，扩展后的组件尺寸保持不变。
* 安全区域不会限制内部组件的布局和大小，不会裁剪内部组件。
* 当父容器为滚动容器时，组件设置expandSafeArea属性后，自身不会延伸，但仍可触发其子节点中设置了expandSafeArea的延伸范围更新。
* 设置expandSafeArea()时，不传参，走默认值处理；设置expandSafeArea([],[])时，相当于入参是空数组，此时expandSafeArea属性设置无效。
* 组件设置expandSafeArea生效的条件为：

  1.type为SafeAreaType.KEYBOARD时默认生效，表现为组件不避让键盘。

  2.设置其他type，组件的边界与安全区域重合时组件能够延伸到安全区域下。例如：设备顶部状态栏高度100，那么组件在屏幕中的绝对位置需要为0 <= y <= 100。
* 组件延伸到避让区时，在避让区的事件如点击事件等可能会被系统拦截，优先给状态栏等系统组件响应。
* 滚动类容器内的组件不建议设置expandSafeArea属性，如果设置，需要按照组件嵌套关系，将当前节点到滚动类祖先容器间所有直接节点设置expandSafeArea属性，否则expandSafeArea属性在滚动后可能会失效，写法参考[示例7](ts-universal-attributes-expand-safe-area.md#示例7滚动类容器扩展安全区)。
* expandSafeArea属性仅作用于当前组件，不会向父组件或子组件传递，因此使用过程中，所有相关组件均需配置。
* 同时设置expandSafeArea和position属性时，position属性会优先生效，expandSafeArea属性会后生效。对于未设置position、offset等绘制属性的组件，如果其边界未与避让区重叠，设置expandSafeArea属性将不生效，如弹窗和半模态组件。
* 对于expandSafeArea属性无法生效的场景，若要将组件部署在避让区，需要手动调整组件的坐标。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array <[SafeAreaType](ts-universal-attributes-expand-safe-area.md#safeareatype)> | 否 | 配置扩展安全区域的类型。未添加[Metadata](js-apis-bundlemanager-metadata.md)配置项时，页面不避让挖孔，CUTOUT类型不生效。  默认值：[SafeAreaType.SYSTEM, SafeAreaType.CUTOUT, SafeAreaType.KEYBOARD]  非法值：按默认值处理。 |
| edges | Array <[SafeAreaEdge](ts-universal-attributes-expand-safe-area.md#safeareaedge)> | 否 | 配置扩展安全区域的边缘。  默认值：[SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM, SafeAreaEdge.START, SafeAreaEdge.END]  非法值：按默认值处理。  扩展至所有避让区域。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## SafeAreaType

PhonePC/2in1TabletTVWearable

扩展安全区域的枚举类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYSTEM | 0 | 系统默认非安全区域，包括状态栏、导航栏。 |
| CUTOUT | 1 | 设备的非安全区域，例如刘海屏或挖孔屏区域。 |
| KEYBOARD | 2 | 软键盘区域。 |

## SafeAreaEdge

PhonePC/2in1TabletTVWearable

扩展安全区域的边缘。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP | 0 | 上方区域。 |
| BOTTOM | 1 | 下方区域。 |
| START | 2 | 前部区域。 |
| END | 3 | 尾部区域。 |

## setKeyboardAvoidMode11+

PhonePC/2in1TabletTVWearable

setKeyboardAvoidMode(value: KeyboardAvoidMode): void

控制虚拟键盘抬起时页面的避让模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [KeyboardAvoidMode](arkts-apis-uicontext-e.md#keyboardavoidmode11) | 是 | 配置虚拟键盘抬起时页面的避让模式。  默认值：KeyboardAvoidMode.OFFSET，键盘抬起时默认避让模式为上抬。  setKeyboardAvoidMode传入异常值时，该属性设置不生效。 |

说明

KeyboardAvoidMode.RESIZE模式会压缩页面大小，页面中设置百分比宽高的组件会跟随页面压缩，而直接设置宽高的组件会按设置的固定大小布局。设置KeyboardAvoidMode的RESIZE模式时，expandSafeArea([SafeAreaType.KEYBOARD],[SafeAreaEdge.BOTTOM])不生效。

KeyboardAvoidMode.NONE模式配置页面不避让键盘，页面会被抬起的键盘遮盖。

setKeyboardAvoidMode针对页面生效，对于弹窗类组件不生效，比如Dialog、Popup、Menu、BindSheet、BindContentCover、Toast、OverlayManager。弹窗类组件的避让模式可以参考[CustomDialogControllerOptions对象说明](ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)。

## getKeyboardAvoidMode11+

PhonePC/2in1TabletTVWearable

getKeyboardAvoidMode(): KeyboardAvoidMode

返回虚拟键盘抬起时页面的避让模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 名称 | 说明 |
| --- | --- |
| [KeyboardAvoidMode](arkts-apis-uicontext-e.md#keyboardavoidmode11) | 返回虚拟键盘抬起时的页面避让模式。 |

## ignoreLayoutSafeArea20+

PhonePC/2in1TabletTVWearable

ignoreLayoutSafeArea(types?: Array<LayoutSafeAreaType>, edges?: Array<LayoutSafeAreaEdge>): T

扩展组件布局时的安全区。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| types | Array <[LayoutSafeAreaType](ts-universal-attributes-expand-safe-area.md#layoutsafeareatype12)> | 否 | 扩展布局安全区域的类型。  默认值：[LayoutSafeAreaType.SYSTEM]，扩展至所有安全区域，比如：状态栏，导航栏和组件级安全区（[safeAreaPadding](ts-universal-attributes-size.md#safeareapadding14)）。  非法值：按默认值处理。 |
| edges | Array <[LayoutSafeAreaEdge](ts-universal-attributes-expand-safe-area.md#layoutsafeareaedge12)> | 否 | 扩展布局安全区的边缘，并且支持镜像能力。  默认值：[LayoutSafeAreaEdge.ALL]，扩展组件所有边缘。  非法值：按默认值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

忽略布局安全区边缘的组件，如果其宽度或高度设置了[LayoutPolicy.matchParent](ts-universal-attributes-size.md#layoutpolicy15)，其大小和位置都会改变，否则仅改变其位置。

依据safeAreaPadding累积功能，组件可扩展其安全区边缘到所有能感知的连续安全区域。

滚动类组件的子元素忽略布局安全区边缘时在滚动方向不考虑滚动组件自身及其父组件的安全区域，包括：List、ArcListItem、Grid、WaterFlow、Swiper和Tabs。

忽略布局安全区属性.ignoreLayoutSafeArea和忽略渲染安全区属性.expandSafeArea都设置时，.ignoreLayoutSafeArea先生效，.expandSafeArea在前者基础上再生效。

## LayoutSafeAreaType12+

PhonePC/2in1TabletTVWearable

扩展布局安全区域的枚举类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SYSTEM | 0 | 设置后，组件的布局范围可扩展至组件级安全区（[safeAreaPadding](ts-universal-attributes-size.md#safeareapadding14)）和页面级安全区（状态栏、导航栏、挖孔区）。 |

## LayoutSafeAreaEdge12+

PhonePC/2in1TabletTVWearable

扩展安全区域的边缘。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOP | 0 | 上方区域。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BOTTOM | 1 | 下方区域。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| START20+ | 2 | 前部区域。LTR模式时表示左侧区域，RTL模式表示右侧区域。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| END20+ | 3 | 尾部区域。LTR模式时表示右侧区域，RTL模式表示左侧区域。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| VERTICAL20+ | 4 | 垂直区域。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| HORIZONTAL20+ | 5 | 水平区域。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| ALL20+ | 6 | 全部区域。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（实现沉浸式效果）

该示例通过设置expandSafeArea属性向顶部和底部扩展安全区实现沉浸式效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SafeAreaExample1 {
5. @State text: string = ''
6. controller: TextInputController = new TextInputController()

8. build() {
9. Row() {
10. Column()
11. .width('100%')
12. .height('100%')
13. // $r('app.media.bg')需要替换为开发者所需的图像资源文件
14. .backgroundImage($r('app.media.bg'))
15. .backgroundImageSize(ImageSize.Cover)
16. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
17. }.height('100%')
18. }
19. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/lToDiVNaTsGXDalFodd57Q/zh-cn_image_0000002558766018.png?HW-CC-KV=V1&HW-CC-Date=20260429T055115Z&HW-CC-Expire=86400&HW-CC-Sign=849B9F5C49F4FDF51DA81EE5EB7B7D3C858F86DAC3252624C52027E0CABB95E1)

### 示例2（同时设置固定宽高和expandSafeArea属性）

该示例展示了同时设置固定宽高和expandSafeArea属性的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SafeAreaExample2 {
5. @State text: string = ''
6. controller: TextInputController = new TextInputController()

8. build() {
9. Column() {
10. TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
11. .placeholderFont({ size: 14, weight: 400 })
12. .width(320).height(40).offset({y: 120})
13. .fontSize(14).fontColor(Color.Black)
14. .backgroundColor(Color.White)
15. }
16. .height('780')
17. .width('100%')
18. .backgroundColor('rgb(179,217,235)')
19. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
20. }
21. }
```

如下图：Column组件扩展至了顶部状态栏[SafeAreaEdge.TOP]，未扩展至底部导航条[SafeAreaEdge.BOTTOM]，扩展后的组件高度维持设置值不变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/YcuAN5YMQhWD_EorkY5FdQ/zh-cn_image_0000002558606360.png?HW-CC-KV=V1&HW-CC-Date=20260429T055115Z&HW-CC-Expire=86400&HW-CC-Sign=7862254779D6CAF4A34027DB9010C6DF396C319E331D3E7DD6BB3CF05682B1B7)

### 示例3（键盘避让时固定背景图位置）

该示例通过为背景图组件设置expandSafeArea属性，来实现拉起键盘进行避让时，背景图保持不动的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SafeAreaExample3 {
5. @State text: string = ''
6. controller: TextInputController = new TextInputController()

8. build() {
9. Row() {
10. Stack() {
11. Column()
12. .width('100%')
13. .height('100%')
14. // $r('app.media.bg')需要替换为开发者所需的图像资源文件
15. .backgroundImage($r('app.media.bg'))
16. .backgroundImageSize(ImageSize.Cover)
17. .expandSafeArea([SafeAreaType.KEYBOARD, SafeAreaType.SYSTEM])
18. Column() {
19. Button('Set caretPosition 1')
20. .onClick(() => {
21. this.controller.caretPosition(1)
22. })
23. TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
24. .placeholderFont({ size: 14, weight: 400 })
25. .width(320)
26. .height(40)
27. .offset({ y: 120 })
28. .fontSize(14)
29. .fontColor(Color.Black)
30. .backgroundColor(Color.White)
31. }.width('100%').alignItems(HorizontalAlign.Center)
32. }
33. }.height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/l_1ToHTbTwOmm16v5t1E_Q/zh-cn_image_0000002589325887.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055115Z&HW-CC-Expire=86400&HW-CC-Sign=1D1801784C39408DB06E107F1259BC85AF897E2A49F479DC0577D2D2707F8ABD)

### 示例4（设置键盘避让模式为压缩）

该示例通过调用setKeyboardAvoidMode设置键盘避让模式为RESIZE模式，实现键盘抬起时page的压缩效果。

```
1. // EntryAbility.ets
2. import { KeyboardAvoidMode } from '@kit.ArkUI';
3. export default class EntryAbility extends UIAbility{
4. onWindowStageCreate(windowStage: window.WindowStage) {
5. // Main window is created, set main page for this ability
6. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

8. windowStage.loadContent('pages/Index', (err, data) => {
9. let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
10. // 设置虚拟键盘抬起时压缩页面大小为减去键盘的高度
11. windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
12. if (err.code) {
13. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
14. return;
15. }
16. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
17. });
18. }
19. }
```

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct KeyboardAvoidExample1 {
5. build() {
6. Column() {
7. Row()
8. .width('100%')
9. .height('30%')
10. .backgroundColor(Color.Gray)
11. TextArea()
12. .width('100%')
13. .borderWidth(1)
14. Text('I can see the bottom of the page')
15. .width('100%')
16. .textAlign(TextAlign.Center)
17. .backgroundColor('rgb(179,217,235)')
18. .layoutWeight(1)
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/F7LtSKspR9mPvQeKv3C5oQ/zh-cn_image_0000002589245829.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055115Z&HW-CC-Expire=86400&HW-CC-Sign=00D3015B8DD38C3F61B91BBB7AF5610EC8955053AAC6BAD831F6E93C1B56228E)

### 示例5（设置键盘避让模式为上抬）

该示例通过调用setKeyboardAvoidMode设置键盘避让模式为OFFSET模式，实现键盘抬起时page的上抬效果。但当输入光标距离屏幕底部的高度大于键盘高度时，page不会抬起，如本例中所示。

```
1. // EntryAbility.ets
2. import { KeyboardAvoidMode } from '@kit.ArkUI';
3. export default class EntryAbility extends UIAbility{
4. onWindowStageCreate(windowStage: window.WindowStage) {
5. // Main window is created, set main page for this ability
6. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

8. windowStage.loadContent('pages/Index', (err, data) => {
9. let keyboardAvoidMode = windowStage.getMainWindowSync().getUIContext().getKeyboardAvoidMode();
10. // 设置虚拟键盘抬起时把页面上抬直到露出光标
11. windowStage.getMainWindowSync().getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET);
12. if (err.code) {
13. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
14. return;
15. }
16. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
17. });
18. }
19. }
```

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct KeyboardAvoidExample2 {
5. build() {
6. Column() {
7. Row()
8. .width('100%')
9. .height('30%')
10. .backgroundColor(Color.Gray)
11. TextArea()
12. .width('100%')
13. .borderWidth(1)
14. Text('I can see the bottom of the page')
15. .width('100%')
16. .textAlign(TextAlign.Center)
17. .backgroundColor('rgb(179,217,235)')
18. .layoutWeight(1)
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/FmuwJwy1RZaMjKN7SHfhHw/zh-cn_image_0000002558766020.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055115Z&HW-CC-Expire=86400&HW-CC-Sign=73C87527F0584EB02905E39279893DF85E290DC7B2CBA4214C714F5FEFEC46D5)

### 示例6（切换避让模式）

该示例通过调用setKeyboardAvoidMode来实现OFFSET、RESIZE和NONE模式之间的切换，实现三种不同的键盘避让效果。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { KeyboardAvoidMode } from '@kit.ArkUI';
3. @Entry
4. @Component

6. struct KeyboardAvoidExample3 {
7. build() {
8. Column() {
9. Row({space:15}) {
10. Button('OFFSET')
11. .onClick(() => {
12. this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.OFFSET);
13. hilog.info(0x0000, 'keyboardAvoidMode: %{public}s', JSON.stringify(this.getUIContext().getKeyboardAvoidMode()));
14. })
15. .layoutWeight(1)
16. Button('RESIZE')
17. .onClick(() => {
18. this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
19. hilog.info(0x0000, 'keyboardAvoidMode: %{public}s', JSON.stringify(this.getUIContext().getKeyboardAvoidMode()));
20. })
21. .layoutWeight(1)
22. Button('NONE')
23. .onClick(() => {
24. this.getUIContext().setKeyboardAvoidMode(KeyboardAvoidMode.NONE);
25. hilog.info(0x0000, 'keyboardAvoidMode: %{public}s', JSON.stringify(this.getUIContext().getKeyboardAvoidMode()));
26. })
27. .layoutWeight(1)
28. }
29. .height('30%')
30. .width('100%')
31. .backgroundColor(Color.Gray)

33. TextArea()
34. .width('100%')
35. .borderWidth(1)

37. Text('I can see the bottom of the page')
38. .width('100%')
39. .textAlign(TextAlign.Center)
40. .backgroundColor('rgb(179,217,235)')
41. .layoutWeight(1)

43. TextArea()
44. .width('100%')
45. .borderWidth(1)
46. }
47. .width('100%')
48. .height('100%')
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/EOhCqxMXR72uCJ-w3JEUng/zh-cn_image_0000002558606362.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055115Z&HW-CC-Expire=86400&HW-CC-Sign=9D902537702B810F901C27EB1CE4B61BFED7A3723065302EDCA38BFE7D8A7156)

### 示例7（滚动类容器扩展安全区）

该示例通过在滚动类容器内调用expandSafeArea属性实现沉浸式效果，Scroll内的Swiper可以延伸到状态栏上。

```
1. class SwiperDataSource implements IDataSource {
2. private list: Array<Color> = []
3. constructor(list: Array<Color>) {
4. this.list = list
5. }
6. totalCount(): number {
7. return this.list.length
8. }
9. getData(index: number): Color {
10. return this.list[index]
11. }
12. registerDataChangeListener(listener: DataChangeListener): void {
13. }
14. unregisterDataChangeListener(listener: DataChangeListener): void {
15. }
16. }
17. @Entry
18. @Component
19. struct ExpandSafeAreaTest {
20. private swiperController: SwiperController = new SwiperController()
21. private swiperData: SwiperDataSource = new SwiperDataSource([])
22. private list: Array<Color> = [
23. Color.Pink,
24. Color.Blue,
25. Color.Green
26. ]
27. aboutToAppear(): void {
28. this.swiperData = new SwiperDataSource(this.list)
29. }
30. build() {
31. Scroll() {
32. Column() {
33. Swiper(this.swiperController) {
34. LazyForEach(this.swiperData, (item: Color, index: number) => {
35. Column() {
36. Text('banner' + index).fontSize(50).fontColor(Color.White)
37. }
38. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
39. .width('100%')
40. .height(400)
41. .backgroundColor(item)
42. })
43. }
44. .loop(true)
45. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
46. .clip(false)
47. Column(){
48. Text('Tab页Content').fontSize(50)
49. }.width('100%').height(1000)
50. .backgroundColor(Color.Grey)
51. }.expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
52. }
53. .clip(false)
54. .edgeEffect(EdgeEffect.None)
55. .width('100%').height('100%')
56. }
57. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/Fke-XfuJTICekup9gSpbhg/zh-cn_image_0000002589325889.png?HW-CC-KV=V1&HW-CC-Date=20260429T055115Z&HW-CC-Expire=86400&HW-CC-Sign=D1F16AD3670C2238FBB9D079079F9A4B7010FB3D6DA04FFBD2DC69D934A6775E)

### 示例8（ignoreLayoutSafeArea延伸组件布局范围）

该示例利用[ignoreLayoutSafeArea](ts-universal-attributes-expand-safe-area.md#ignorelayoutsafearea20)改变组件位置。相比未使用该属性，配置ignoreLayoutSafeArea后，Row组件基于Stack内容区、Stack组件级安全区、系统状态栏共同组成的范围，取其左上部分，作左上对齐。

```
1. import { LengthMetrics } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct IgnoreLayoutSafeAreaTest1 {
6. build() {
7. Column() {
8. Stack() {
9. Row()
10. .backgroundColor('rgb(39, 135, 217)')
11. .width(75)  // 固定宽度
12. .height(75) // 固定高度
13. .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.START, LayoutSafeAreaEdge.TOP])  // 设置布局区域延伸取左和上方向，至系统避让区SYSTEM

15. Row()
16. .backgroundColor('rgb(0, 74, 175)')
17. .width(75)
18. .height(75)

20. }
21. .width(200)
22. .height(200)
23. .backgroundColor(Color.Gray)
24. .align(Alignment.TopStart)  // 子组件相对于Stack容器左上对齐
25. .padding({
26. left: 10  // 设置左侧10vp普通内边距
27. })
28. .safeAreaPadding(LengthMetrics.vp(10))  // 设置10vp安全区内边距（即组件级安全区）
29. }
30. .width('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/6GoDWee2RtSXqQ1nNIDtUw/zh-cn_image_0000002589245831.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055115Z&HW-CC-Expire=86400&HW-CC-Sign=54E6E703026500E232904DA4ED14B24BAD9921ED9B97836E23F4808666DDBF01)

### 示例9（ignoreLayoutSafeArea配合LayoutPolicy.matchParent延伸组件布局范围）

该示例利用[ignoreLayoutSafeArea](ts-universal-attributes-expand-safe-area.md#ignorelayoutsafearea20)和[LayoutPolicy.matchParent](ts-universal-attributes-size.md#layoutpolicy15)同时改变组件大小和位置。相比未使用该属性，配置ignoreLayoutSafeArea后，Row组件基于Stack内容区、Stack组件级安全区，取其右下部分并撑满可用空间。

```
1. import { LengthMetrics } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct IgnoreLayoutSafeAreaTest2 {
6. build() {
7. Column() {
8. Stack() {
9. Row()
10. .backgroundColor('rgb(39, 135, 217)')
11. .width(LayoutPolicy.matchParent)  // 自适应宽度
12. .height(LayoutPolicy.matchParent) // 自适应高度
13. .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.END, LayoutSafeAreaEdge.BOTTOM])  // 设置布局区域延伸取右和下方向，至系统避让区SYSTEM

15. Row()
16. .backgroundColor('rgb(0, 74, 175)')
17. .width(LayoutPolicy.matchParent)
18. .height(LayoutPolicy.matchParent)

20. }
21. .width(200)
22. .height(200)
23. .backgroundColor(Color.Gray)
24. .align(Alignment.TopStart)  // 子组件相对于Stack容器左上对齐
25. .padding(10) // 设置10vp普通内边距
26. .safeAreaPadding(LengthMetrics.vp(10))  // 设置10vp安全区内边距（即组件级安全区）
27. }
28. .width('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Zo_X1NHGSnSU4WgWD8Zohw/zh-cn_image_0000002558766022.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055115Z&HW-CC-Expire=86400&HW-CC-Sign=3FAFFB90BDAC36152EFD742F2B70E4212C02355B233046BF4F44DD09BFA2EDC5)

### 示例10（expandSafeArea与ignoreLayoutSafeArea的区别）

该示例展示了容器分别设置了expandSafeArea和ignoreLayoutSafeArea的布局效果和各自对子组件布局效果的影响。两种设置下，容器都可见地进行了延伸，但前者的子组件不受延伸影响，后者的子组件因父容器的延伸改变了位置。

```
1. import { LengthMetrics } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct IgnoreLayoutSafeAreaTest3 {
6. build() {
7. Row(){
8. Column(){
9. Stack(){
10. Stack(){

12. }
13. .width(30)
14. .height(30)
15. .backgroundColor('rgb(0, 74, 175)')
16. }
17. .width(100)
18. .height(100)
19. .backgroundColor('rgb(39, 135, 217)')
20. .align(Alignment.TopStart)

22. Text('基准效果').fontColor(Color.White)
23. }

25. Column(){
26. Stack(){
27. Stack(){

29. }
30. .width(30)
31. .height(30)
32. .backgroundColor('rgb(0, 74, 175)')
33. }
34. .width(100)
35. .height(100)
36. .backgroundColor('rgb(39, 135, 217)')
37. .align(Alignment.TopStart)
38. .expandSafeArea()  // 设置绘制区域延伸，自身绘制区域上抬，子组件相对屏幕位置不变

40. Text('expandSafeArea').fontColor(Color.White)
41. }

43. Column(){
44. Stack(){
45. Stack(){

47. }
48. .width(30)
49. .height(30)
50. .backgroundColor('rgb(0, 74, 175)')
51. }
52. .width(100)
53. .height(100)
54. .backgroundColor('rgb(39, 135, 217)')
55. .align(Alignment.TopStart)
56. .ignoreLayoutSafeArea()  // 设置布局区域延伸，自身布局区域上抬，子组件相对容器位置不变

58. Text('ignoreLayoutSafeArea').fontColor(Color.White)
59. }
60. }
61. .width('100%')
62. .backgroundColor(Color.Gray)
63. .justifyContent(FlexAlign.SpaceEvenly)
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/MreRD-5HR7eHOIED2lLufg/zh-cn_image_0000002558606364.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055115Z&HW-CC-Expire=86400&HW-CC-Sign=718837ABE52329920E8B0FA9BF0265D12EE17F45BACFD781F9AA2770FC050B89)
