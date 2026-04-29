---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle
title: Toggle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > Toggle
category: harmonyos-references
scraped_at: 2026-04-29T13:51:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:78f7f88edeb48e74fe7647f4259b935da8e6db202377c96c4169fb7db879e8f2
---

组件提供勾选框样式、状态按钮样式和开关样式。

说明

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

仅当ToggleType设置为Button时，可包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

Toggle(options: ToggleOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ToggleOptions](ts-basic-components-toggle.md#toggleoptions18对象说明) | 是 | Toggle组件的配置选项，用于配置开关的样式类型和初始状态。 |

## ToggleOptions18+对象说明

PhonePC/2in1TabletTVWearable

Toggle的信息。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type8+ | [ToggleType](ts-basic-components-toggle.md#toggletype枚举说明) | 否 | 否 | 开关的样式。  默认值：ToggleType.Switch  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| isOn8+ | boolean | 否 | 是 | 开关是否打开。  true：打开；false：关闭。  默认值：false  该属性支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  该属性支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## ToggleType枚举说明

PhonePC/2in1TabletTVWearable

Toggle的样式。

说明

Toggle的样式继承对应组件样式的默认值，且不支持设置。例如，如果ToggleType为Button，则该组件样式继承[ButtonType](ts-basic-components-button.md#buttontype枚举说明)的默认值。由于Button.type从API version 18开始，默认类型从胶囊型变更为圆角矩形，胶囊型按钮不支持设置[borderRadius](ts-universal-attributes-border.md#borderradius)，此时使用Toggle组件设置borderRadius也不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Checkbox | 0 | 提供单选框样式。  **说明：**  API version 11开始，Checkbox默认样式由圆角方形变为圆形。  [通用属性margin](ts-universal-attributes-size.md#margin)的默认值为：  {  top: '14px',  right: '14px',  bottom: '14px',  left: '14px'  }。  默认尺寸为：  {width:'20vp', height:'20vp'}。 |
| Switch | 1 | 提供开关样式。  **说明：**  [通用属性margin](ts-universal-attributes-size.md#margin)默认值为：  {  top: '6px',  right: '14px',  bottom: '6px',  left: '14px'  }。  默认尺寸为：  {width:'36vp', height:'20vp'}。 |
| Button | 2 | 提供状态按钮样式。如子组件设置文本，文本内容将显示在按钮内。默认高度为28vp，宽度无默认值。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### selectedColor

PhonePC/2in1TabletTVWearable

selectedColor(value: ResourceColor)

设置组件在打开状态下的背景颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 组件打开状态的背景颜色。  默认值：  当ToggleType为Switch时，默认值为$r('sys.color.ohos\_id\_color\_emphasize')。  当ToggleType为Checkbox时，默认值为$r('sys.color.ohos\_id\_color\_emphasize')。  当ToggleType为Button时，默认值为$r('sys.color.ohos\_id\_color\_emphasize')混合$r('sys.float.ohos\_id\_alpha\_highlight\_bg')的透明度。 |

### switchPointColor

PhonePC/2in1TabletTVWearable

switchPointColor(color: ResourceColor)

设置Switch类型的圆形滑块颜色。仅当type为ToggleType.Switch生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 是 | Switch类型的圆形滑块颜色。  默认值：$r('sys.color.ohos\_id\_color\_foreground\_contrary') |

### switchStyle12+

PhonePC/2in1TabletTVWearable

switchStyle(value: SwitchStyle)

设置Switch类型的样式。仅当type为ToggleType.Switch生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SwitchStyle](ts-basic-components-toggle.md#switchstyle12对象说明) | 是 | Switch样式风格。 |

### contentModifier12+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: ContentModifier<ToggleConfiguration>)

定制Toggle内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](ts-universal-attributes-content-modifier.md#contentmodifiert)[<ToggleConfiguration>](ts-basic-components-toggle.md#toggleconfiguration12对象说明) | 是 | 在Toggle组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

## SwitchStyle12+对象说明

PhonePC/2in1TabletTVWearable

Switch类型的样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pointRadius | number | [Resource](ts-types.md#resource) | 否 | 是 | 设置Switch类型的圆形滑块半径，单位为vp。  **说明：**  不支持百分比，设定值小于0时按照默认算法设置，设定值大于等于0时按照设定值设置。  未设定此属性时，圆形滑块半径根据默认算法设置。  默认算法：（组件高度（单位：vp） / 2） - （2vp \* 组件高度（单位：vp） / 20vp）。 |
| unselectedColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置Switch类型关闭状态的背景颜色。  默认值：深色和浅色模式下均为0x337F7F7F。从API version 20开始，如果开启了[优化深浅色模式切换开销](../harmonyos-guides/ui-dark-light-color-adaptation.md#优化深浅色模式切换开销)能力，浅色模式下默认值为0x19000000，表现效果为10%透明度的黑色；深色模式下默认值为0x19FFFFFF，表现效果为10%透明度的白色。 |
| pointColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置Switch类型的圆形滑块颜色。  默认值：$r('sys.color.ohos\_id\_color\_foreground\_contrary') |
| trackBorderRadius | number | [Resource](ts-types.md#resource) | 否 | 是 | 设置Switch类型的滑轨的圆角，单位为vp。  **说明：**  不支持百分比，设定值小于0时按照默认算法设置，设定值大于组件高度一半时按照组件高度一半设置，其他场合按照设定值设置。  未设定此属性时，滑轨圆角根据默认算法设置。  默认算法：组件高度（单位：vp） / 2。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback: (isOn: boolean) => void)

开关状态切换时触发该事件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isOn | boolean | 是 | 开关的状态。  true：状态从关切换为开；false：状态从开切换为关。 |

## ToggleConfiguration12+对象说明

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isOn | boolean | 否 | 否 | 开关是否打开。  true：开关打开；false：开关关闭。  默认值：false |
| enabled | boolean | 否 | 否 | 是否可以切换状态。  true：可以切换状态；false：不可以切换状态。  默认值：true |
| triggerChange | Callback<boolean> | 否 | 否 | 触发switch选中状态变化。  true：状态从关切换为开；false：状态从开切换为关。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置开关的样式）

该示例通过配置ToggleType设置Toggle的勾选框样式、状态按钮样式及开关样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ToggleExample {
5. build() {
6. Column({ space: 10 }) {
7. Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
8. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
9. Toggle({ type: ToggleType.Switch, isOn: false })
10. .selectedColor('#007DFF')
11. .switchPointColor('#FFFFFF')
12. .onChange((isOn: boolean) => {
13. console.info('Component status:' + isOn);
14. })

16. Toggle({ type: ToggleType.Switch, isOn: true })
17. .selectedColor('#007DFF')
18. .switchPointColor('#FFFFFF')
19. .onChange((isOn: boolean) => {
20. console.info('Component status:' + isOn);
21. })
22. }

24. Text('type: Checkbox').fontSize(12).fontColor(0xcccccc).width('90%')
25. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
26. Toggle({ type: ToggleType.Checkbox, isOn: false })
27. .size({ width: 20, height: 20 })
28. .selectedColor('#007DFF')
29. .onChange((isOn: boolean) => {
30. console.info('Component status:' + isOn);
31. })

33. Toggle({ type: ToggleType.Checkbox, isOn: true })
34. .size({ width: 20, height: 20 })
35. .selectedColor('#007DFF')
36. .onChange((isOn: boolean) => {
37. console.info('Component status:' + isOn);
38. })
39. }

41. Text('type: Button').fontSize(12).fontColor(0xcccccc).width('90%')
42. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
43. Toggle({ type: ToggleType.Button, isOn: false }) {
44. Text('status button').fontColor('#182431').fontSize(12)
45. }.width(106)
46. .selectedColor('rgba(0,125,255,0.20)')
47. .onChange((isOn: boolean) => {
48. console.info('Component status:' + isOn);
49. })

51. Toggle({ type: ToggleType.Button, isOn: true }) {
52. Text('status button').fontColor('#182431').fontSize(12)
53. }.width(106)
54. .selectedColor('rgba(0,125,255,0.20)')
55. .onChange((isOn: boolean) => {
56. console.info('Component status:' + isOn);
57. })
58. }
59. }.width('100%').padding(24)
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/n0ZmVArqTOunSxy-1sHOOA/zh-cn_image_0000002558766218.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055153Z&HW-CC-Expire=86400&HW-CC-Sign=3FB5F1EF7F2750A72372EF3F3F5742A10455C7E78BB043E63C53085E655DC6BD)

### 示例2（自定义开关类型的样式）

该示例实现了自定义设置Toggle组件Switch样式，包括圆形滑块半径、关闭状态的背景颜色、圆形滑块颜色、滑轨的圆角。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ToggleExample {
5. build() {
6. Column({ space: 10 }) {
7. Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
8. Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
9. Toggle({ type: ToggleType.Switch, isOn: false })
10. .selectedColor('#007DFF')
11. .switchStyle({
12. pointRadius: 15,
13. trackBorderRadius: 10,
14. pointColor: '#D2B48C',
15. unselectedColor: Color.Pink })
16. .onChange((isOn: boolean) => {
17. console.info('Component status:' + isOn);
18. })

20. Toggle({ type: ToggleType.Switch, isOn: true })
21. .selectedColor('#007DFF')
22. .switchStyle({
23. pointRadius: 15,
24. trackBorderRadius: 10,
25. pointColor: '#D2B48C',
26. unselectedColor: Color.Pink })
27. .onChange((isOn: boolean) => {
28. console.info('Component status:' + isOn);
29. })
30. }
31. }.width('100%').padding(24)
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/k-z-ewD-Tzy4YRqImZML4w/zh-cn_image_0000002558606560.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055153Z&HW-CC-Expire=86400&HW-CC-Sign=2315447932A82D801C945BC7D2ED6EF177996A266C58144653B3A54712AC524A)

### 示例3（自定义Toggle样式）

该示例实现自定义Toggle样式，通过按钮切换圆形背景颜色：点击蓝圆按钮，背景变蓝色；点击黄圆按钮，背景变黄色。

```
1. // xxx.ets
2. class MySwitchStyle implements ContentModifier<ToggleConfiguration> {
3. selectedColor: Color = Color.White;
4. lamp: string = 'string';

6. constructor(selectedColor: Color, lamp: string) {
7. this.selectedColor = selectedColor;
8. this.lamp = lamp;
9. }

11. applyContent(): WrappedBuilder<[ToggleConfiguration]> {
12. return wrapBuilder(buildSwitch);
13. }
14. }

16. @Builder
17. function buildSwitch(config: ToggleConfiguration) {
18. Column({ space: 50 }) {
19. Circle({ width: 150, height: 150 })
20. .fill(config.isOn ? (config.contentModifier as MySwitchStyle).selectedColor : Color.Blue)
21. Row() {
22. Button('蓝' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))
23. .onClick(() => {
24. config.triggerChange(false);
25. })
26. Button('黄' + JSON.stringify((config.contentModifier as MySwitchStyle).lamp))
27. .onClick(() => {
28. config.triggerChange(true);
29. })
30. }
31. }
32. }

34. @Entry
35. @Component
36. struct Index {
37. build() {
38. Column({ space: 50 }) {
39. Toggle({ type: ToggleType.Switch })
40. .enabled(true)
41. .contentModifier(new MySwitchStyle(Color.Yellow, '灯'))
42. .onChange((isOn: boolean) => {
43. console.info('Switch Log:' + isOn);
44. })
45. }.height('100%').width('100%')
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/6krXMNM8SeOqKKjQMaVLPw/zh-cn_image_0000002589326087.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055153Z&HW-CC-Expire=86400&HW-CC-Sign=467C66D9F49F8F4221FA07EA1606A2260E04B54D117ABEE7B4386DF8186ED16D)
