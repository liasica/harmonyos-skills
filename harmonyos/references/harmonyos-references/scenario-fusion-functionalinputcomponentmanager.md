---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalinputcomponentmanager
title: functionalInputComponentManager(场景化融合Input组件管理)
breadcrumb: API参考 > 应用服务 > Scenario Fusion Kit（融合场景服务） > ArkTS组件 > functionalInputComponentManager(场景化融合Input组件管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:18:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9becb98d5ac1386dddc4c9b2220c9c403fac6c50ad3d63b2e33254a0ff95ce95
---

本模块提供FunctionalInput组件的逻辑管理，辅助HarmonyOS应用和元服务通过FunctionalInput组件完成快速拉起选择地区页面，供用户选择地区信息的功能。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 5.1.0(18)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { functionalInputComponentManager } from '@kit.ScenarioFusionKit';
```

## InputType

PhonePC/2in1TabletTV

该枚举定义省市区选择器的功能类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECT\_DISTRICT | 0 | 默认值为0，省市区选择器类型。 |

## FunctionalInputParams

PhonePC/2in1TabletTV

该接口定义了FunctionalInput组件的参数，包括省市区选择器的类型，样式，图标等。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inputType | [InputType](scenario-fusion-functionalinputcomponentmanager.md#inputtype) | 否 | 否 | Input组件功能场景类型。默认值：SELECT\_DISTRICT。 |
| textInputValue | [TextInputOptions](ts-basic-components-textinput.md#textinputoptions对象说明) | 否 | 否 | TextInput组件无输入时的提示文本和文本内容。 |
| inputAttributeModifier | [TextInputModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 设置组件的事件和属性。支持部分[通用事件](ts-component-general-events.md)和[通用属性](ts-component-general-attributes.md)，以及部分TextInput的事件和属性。  icon参数为空时，无默认值。icon参数不为空时，默认值为：  padding({  top: 8,  bottom: 8,  left: 16,  right: 48,  })  当设备是镜像语言时，默认值为  padding({  top: 8,  bottom: 8,  left: 48,  right: 16,  })  **说明：**  inputAttributeModifier参数失效的事件和属性：  事件：onFocus、onBlur、onClick、onKeyEvent、onKeyPreIme、onSubmit、onEditChange、onCopy、onCut、onPaste、onTextSelectionChange、onSecurityStateChange、onWillInsert、onDidInsert、onWillDelete、onDidDelete。  属性：focusable、tabIndex、defaultFocus、groupDefaultFocus、focusOnTouch、focusBox、type、enterKeyType、caretColor、copyOption、showPasswordIcon、selectedBackgroundColor、caretStyle、caretPosition、passwordIcon、enableKeyboardOnFocus、customKeyboard、passwordRules、selectAll、contentType、showPassword。 |
| icon | [Resource](ts-types.md#resource) | 否 | 是 | 设置组件显示图标，支持symbol和image两种类型。默认不显示图标。 |
| iconImgModifier | [ImageModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 当“icon”设置为image时，可使用该参数进行图标的事件和样式设置。  iconImgModifier  .size({ width: 24, height: 24 })  .margin({  start: 8,  end: 16,  }) |
| iconSymbolModifier | [SymbolGlyphModifier](ts-universal-attributes-attribute-modifier.md#自定义modifier) | 否 | 是 | 当“icon”设置为symbol时，可使用该参数进行图标的事件和样式设置。  iconSymbolModifier  .fontColor([$r('sys.color.ohos\_id\_color\_fourth')])  .margin({  start: 8,  end: 16  }) |

## DistrictSelectResult

PhonePC/2in1TabletTV

该接口定义了选择地区的返回体。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inputContent | string | 否 | 否 | 返回选择的区域信息。格式为：省、市、区、街道。 |
| districtSelectResult | [sceneMap.DistrictSelectResult](map-scenemap.md#districtselectresult) | 否 | 否 | 返回区划选择的结果。 |

## 事件

PhonePC/2in1TabletTV

不支持通用事件，仅支持以下事件：

## FunctionalInputController

PhonePC/2in1TabletTV

FunctionalInput组件控制器，用来回调组件内部的点击事件。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 5.1.0(18)

### onSelectDistrict

PhonePC/2in1TabletTV

onSelectDistrict(callback: AsyncCallback<DistrictSelectResult>): FunctionalInputController

注册FunctionalInput组件为区域选择的点击事件，使用callback异步回调。

该接口功能依赖Map Kit，参见[selectDistrict](map-scenemap.md#selectdistrict)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**设备行为差异：** 该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[DistrictSelectResult](scenario-fusion-functionalinputcomponentmanager.md#districtselectresult)> | 是 | 回调函数。callback返回区划选择请求的结果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [FunctionalInputController](scenario-fusion-functionalinputcomponentmanager.md#functionalinputcontroller) | [FunctionalInput](scenario-fusion-functionalinput.md)组件控制器。 |

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
