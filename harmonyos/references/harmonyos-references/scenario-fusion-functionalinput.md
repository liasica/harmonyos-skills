---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scenario-fusion-functionalinput
title: FunctionalInput（Input组件）
breadcrumb: API参考 > 应用服务 > Scenario Fusion Kit（融合场景服务） > ArkTS组件 > FunctionalInput（Input组件）
category: harmonyos-references
scraped_at: 2026-09-02T15:03:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:552483ba9927a996a9e9bd1fe79b88e7d8bcbf05a8303077d85fd3666602eba7
---

本模块提供FunctionalInput组件，开发者可调用对应FunctionalInput组件快速拉起选择地区页面，供用户选择地区信息。

FunctionalInput需要配合[functionalInputComponentManager](scenario-fusion-functionalinputcomponentmanager.md)一起使用，完成相应功能。

**起始版本：** 5.1.0(18)

## 导入模块

```typescript
import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';
```

## FunctionalInput

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

build(): void

用于创建FunctionalInput对象的构造函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.1.0(18)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AtomicserviceComponent.UIComponent

**起始版本：** 5.1.0(18)

**示例：**

```typescript
import { FunctionalInput, functionalInputComponentManager } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { SymbolGlyphModifier, TextInputModifier } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State inputContent: string = '';

  build() {
    Column() {
      Row() {
        Text('所在地区').width(64)
        // 构建FunctionalInput组件实例。
        FunctionalInput({
          params: {
            // InputType.SELECT_DISTRICT表示输入类型为省/市/区选择器类型。
            inputType: functionalInputComponentManager.InputType.SELECT_DISTRICT,
            textInputValue: {
              text: this.inputContent,
              placeholder: '省、市、区、街道地址'
            },
            // 调整TextInput样式。
            inputAttributeModifier: new TextInputModifier()
              .fontColor($r('sys.color.ohos_id_color_badge_red'))
              .onChange((value) => {
                if (value !== this.inputContent) {
                  this.inputContent = value;
                }
              }),
            // 将图标设置在末尾。
            icon: $r('sys.symbol.xmark'),
            // 设置符号图标的事件和样式。
            iconSymbolModifier: new SymbolGlyphModifier()
              .onClick(() => {
                this.inputContent = '';
              })
              .fontSize(32)
          },
          // 当InputType为SELECT_DISTRICT时，回调必须为onSelectDistrict。
          controller: new functionalInputComponentManager.FunctionalInputController().onSelectDistrict((err,
            data: functionalInputComponentManager.DistrictSelectResult) => {
            if (err) {
              // 错误日志处理。
              hilog.error(0x0000, 'testTag', 'Failed to select district, error: %{public}d %{public}s', err.code, err.message);
              return;
            }
            // 成功日志处理。
            hilog.info(0x0000, 'testTag', 'succeeded in selecting district');
            // 在输入组件中显示所选区域信息。
            this.inputContent = data.inputContent;
          })
        })
          .layoutWeight(1)
      }.height('100%')
    }.width('100%')
  }
}
```
