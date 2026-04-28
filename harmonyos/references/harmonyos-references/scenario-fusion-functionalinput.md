---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalinput
title: FunctionalInput（Input组件）
breadcrumb: API参考 > 应用服务 > Scenario Fusion Kit（融合场景服务） > ArkTS组件 > FunctionalInput（Input组件）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a0ae6919b3c0a13074bd55c36400de309c53f4124bfc88cca26472e2d8b7b39b
---

本模块提供FunctionalInput组件，开发者可调用对应FunctionalInput组件快速拉起选择地区页面，供用户选择地区信息。

FunctionalInput需要配合[functionalInputComponentManager](scenario-fusion-functionalinputcomponentmanager.md)一起使用，完成相应功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 5.1.0(18)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';
```

## FunctionalInput

PhonePC/2in1TabletTV

场景化Input组件。

本模块提供FunctionalInput组件，HarmonyOS应用和元服务通过集成FunctionalInput组件完成省市区选择，输入框显示文本修改，样式修改等功能。

FunctionalInput组件需要配合[functionalInputComponentManager](scenario-fusion-functionalinputcomponentmanager.md)一起使用，完成相应功能。

**装饰器类型：** @Component

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| params | functionalInputComponentManager.[FunctionalInputParams](scenario-fusion-functionalinputcomponentmanager.md#functionalinputparams) | 是 | @Prop | FunctionalInput组件参数。 |
| controller | functionalInputComponentManager.[FunctionalInputController](scenario-fusion-functionalinputcomponentmanager.md#functionalinputcontroller) | 是 | - | FunctionalInput组件控制器，用来接收组件的点击事件。 |

### build

PhonePC/2in1TabletTV

build(): void

用于创建FunctionalInput对象的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 5.1.0(18)

**示例：**

```
1. import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { SymbolGlyphModifier, TextInputModifier } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. @State inputContent: string = '';

10. build() {
11. Column() {
12. Row() {
13. Text('所在地区').width(64)
14. // 构建FunctionalInput组件实例。
15. FunctionalInput({
16. params: {
17. // InputType.SELECT_DISTRICT表示输入类型为省/市/区选择器类型。
18. inputType: functionalInputComponentManager.InputType.SELECT_DISTRICT,
19. textInputValue: {
20. text: this.inputContent,
21. placeholder: '省、市、区、街道地址',
22. },
23. // 调整TextInput样式。
24. inputAttributeModifier: new TextInputModifier()
25. .fontColor($r('sys.color.ohos_id_color_badge_red'))
26. .onChange((value) => {
27. if (value !== this.inputContent) {
28. this.inputContent = value;
29. }
30. }),
31. // 将图标设置在末尾。
32. icon: $r('sys.symbol.xmark'),
33. // 设置符号图标的事件和样式。
34. iconSymbolModifier: new SymbolGlyphModifier()
35. .onClick(() => {
36. this.inputContent = '';
37. })
38. .fontSize(32),
39. },
40. // 当InputType为SELECT_DISTRICT时，回调必须为onSelectDistrict。
41. controller: new functionalInputComponentManager.FunctionalInputController().onSelectDistrict((err,
42. data: functionalInputComponentManager.DistrictSelectResult) => {
43. if (err) {
44. // 错误日志处理。
45. hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
46. return;
47. }
48. // 成功日志处理。
49. hilog.info(0x0000, "testTag", "succeeded in selecting district");
50. // 在输入组件中显示所选区域信息。
51. this.inputContent = data.inputContent;
52. })
53. })
54. .layoutWeight(1)
55. }.height('100%')
56. }.width('100%')
57. }
58. }
```
