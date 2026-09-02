---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-progressbuttonv2
title: ProgressButtonV2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > ProgressButtonV2
category: harmonyos-references
scraped_at: 2026-09-02T15:01:09+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:585be28466741c912b07a92418862cbcf5204855dbf472bd29664e73062b4ccb
---

文本下载按钮，可显示具体的下载进度。

该组件基于[状态管理（V2）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)实现，相较于[状态管理（V1）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制文本下载按钮的数据和状态，实现更高效的用户界面刷新。

**说明** 

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果ProgressButtonV2设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到ProgressButtonV2本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ProgressButtonV2设置通用属性和通用事件。

## 导入模块

```ts
import { ColorMetrics, LengthMetrics, ProgressButtonV2, ProgressButtonV2Color } from '@kit.ArkUI';
```

## ProgressButtonV2

ProgressButtonV2({progress: number, content: ResourceStr, progressButtonWidth?: LengthMetrics, onClicked: ClickCallback, isEnabled: boolean, colorOptions?: ProgressButtonColorOptions, progressButtonRadius?: LengthMetrics})

文本下载按钮，可显示具体下载进度。

**装饰器类型：**@ComponentV2

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 是 | @Require  @Param | 下载按钮的当前进度值。  取值范围：[0,100]。设置小于0的数值时置为0，设置大于100的数值置为100。  默认值：0 |
| content | [ResourceStr](ts-types.md#resourcestr) | 是 | @Require  @Param | 下载按钮的文本。 |
| progressButtonWidth | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | @Param  @Once | 下载按钮的宽度。  默认值：44vp |
| onClicked | [ClickCallback](ohos-arkui-advanced-progressbuttonv2.md#clickcallback) | 是 | @Param | 下载按钮的点击回调。 |
| isEnabled | boolean | 是 | @Param | 下载按钮是否可以点击。  true：可以点击。  false：不可点击。 |
| colorOptions | [ProgressButtonV2Color](ohos-arkui-advanced-progressbuttonv2.md#progressbuttonv2color) | 否 | @Param | 下载按钮颜色选项。 |
| progressButtonRadius | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | @Param | 下载按钮的圆角（不支持百分比设置）。  取值范围：[0, height/2]  默认值：height/2  设置非法数值时，按照默认值处理。 |

## 属性

不支持[通用属性](ts-component-general-attributes.md)。

## ClickCallback

type ClickCallback = () => void

下载按钮的点击回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

## ProgressButtonV2Color

下载按钮颜色选项。

**装饰器类型：**@ObservedV2

### 属性

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progressColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 进度条颜色。  默认值：#330A59F7  装饰器类型：@Trace |
| borderColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 按钮描边颜色。  默认值：#330A59F7  装饰器类型：@Trace |
| textColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 按钮文本颜色。  默认值：系统默认值，#CE000000  装饰器类型：@Trace |
| backgroundColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 按钮背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_foreground\_contrary')  装饰器类型：@Trace |

### constructor

constructor(options: ProgressButtonV2ColorOptions);

下载按钮颜色选项构造函数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ProgressButtonV2ColorOptions](ohos-arkui-advanced-progressbuttonv2.md#progressbuttonv2coloroptions) | 是 | 色彩信息。 |

## ProgressButtonV2ColorOptions

下载按钮色彩信息选项。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progressColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 进度条颜色。  默认值：#330A59F7 |
| borderColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 按钮描边颜色。  默认值：#330A59F7 |
| textColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 按钮文本颜色。  默认值：系统默认值(#CE000000) |
| backgroundColor | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 否 | 是 | 按钮背景颜色。  默认值：$r('sys.color.ohos\_id\_color\_foreground\_contrary') |

## 事件

不支持[通用事件](ts-component-general-events.md)。

## 示例

该示例实现了一个简单的带加载进度的文本下载按钮。

```ts
import { LengthMetrics, ProgressButtonV2 } from '@kit.ArkUI';

@Entry
@ComponentV2
struct Index {
  @Local progressIndex: number = 0;
  @Local textState: string = '下载';
  @Local buttonWidth: LengthMetrics = LengthMetrics.vp(200);
  @Local isRunning: boolean = false;
  @Local enableState: boolean = true;

  build() {
    Column() {
      Scroll() {
        Column({ space: 20 }) {
          ProgressButtonV2({
            progress: this.progressIndex,
            progressButtonWidth: this.buttonWidth,
            content: this.textState,
            isEnabled: this.enableState,
            onClicked: () => {
              if (this.textState && !this.isRunning && this.progressIndex < 100) {
                this.textState = '继续';
              }
              this.isRunning = !this.isRunning;
              let timer = setInterval(() => {
                if (this.isRunning) {
                  if (this.progressIndex === 100) {
                    clearInterval(timer);
                  } else {
                    this.progressIndex++;
                    if (this.progressIndex === 100) {
                      this.textState = '已完成';
                      this.enableState = false;
                    }
                  }
                } else {
                  clearInterval(timer);
                }
              }, 20);
            }
          })
        }.alignItems(HorizontalAlign.Center).width('100%').margin({ top: 20 });
      }
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/gOZaS4BERa2SuoKDEFikAw/zh-cn_image_0000002736435455.png)
