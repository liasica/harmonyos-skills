---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-counterv2
title: CounterV2
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > CounterV2
category: harmonyos-references
scraped_at: 2026-09-02T15:01:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:947951a36256ce4c4d9c1093aa072a2aa74fc07daf50c422709085cc72c3b312
---

CounterV2组件用于精确调节数值，包含列表型、紧凑型、数值内联型和日期内联型四种类型，适用于购物车数量调节、日期选择等场景。

该组件基于[状态管理（V2）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)实现，相较于[状态管理（V1）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)，状态管理（V2）增强了对数据对象的深度观察与管理能力，不再局限于组件层级。借助状态管理（V2），开发者可以通过该组件更灵活地控制CounterV2的数据和状态，实现更高效的用户界面刷新。

**说明** 

* 如果CounterV2设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到CounterV2本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议为CounterV2设置通用属性和通用事件。
* 该组件接口仅可在Stage模型下使用。

**起始版本：** 26.0.0

## 导入模块

```ts
import { CounterV2Type, CounterV2Component, CounterV2Options, CounterV2DateData } from '@kit.ArkUI';
```

## 子组件

无

## CounterV2Component

CounterV2Component({ options: CounterV2Options })

定义CounterV2。

**起始版本：** 26.0.0

**装饰器类型：** @ComponentV2

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| options | [CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options) | 是 | @Param | 定义CounterV2组件的类型及样式。 |

## CounterV2Options

CounterV2Options定义CounterV2类型及样式。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [CounterV2Type](ohos-arkui-advanced-counterv2.md#counterv2type) | 否 | 否 | 指定当前CounterV2的类型。需配合对应的样式参数使用，具体对应关系见下表。 |
| direction | [Direction](ts-appendix-enums.md#direction) | 否 | 是 | 布局方向。  默认值：Direction.Auto  值为undefined时，按默认值处理。 |
| numberOptions | [CounterV2NumberStyleOptions](ohos-arkui-advanced-counterv2.md#counterv2numberstyleoptions) | 否 | 是 | 列表型和紧凑型CounterV2的样式。  默认值：undefined，显示数值为0的列表型或紧凑型CounterV2。  当需要自定义列表型或紧凑型CounterV2的标签、初始值、范围、步长等属性时传入此参数；当计数器初始值为0且不需要自定义配置时可以不传入，使用默认样式。  值为undefined时，按默认值处理。 |
| inlineOptions | [CounterV2InlineStyleOptions](ohos-arkui-advanced-counterv2.md#counterv2inlinestyleoptions) | 否 | 是 | 数值内联型CounterV2的样式。  默认值：undefined，显示数值为0的数值内联型CounterV2。  当需要自定义数值内联型CounterV2的初始值、范围、步长、文本宽度、变化回调等属性时传入此参数；当计数器初始值为0且不需要自定义配置时可以不传入，使用默认样式。  值为undefined时，按默认值处理。 |
| dateOptions | [CounterV2DateStyleOptions](ohos-arkui-advanced-counterv2.md#counterv2datestyleoptions) | 否 | 是 | 日期内联型CounterV2的样式。  默认值：undefined，显示0001/01/01的日期内联型CounterV2。  当需要自定义日期内联型CounterV2的初始日期、日期变化回调等属性时传入此参数；当需要显示默认日期0001/01/01且不需要自定义配置时可以不传入，使用默认样式。  值为undefined时，按默认值处理。 |

选择不同的CounterV2类型，需要选择对应的CounterV2样式。若样式参数与类型不匹配，将使用该类型对应的默认样式。

| CounterV2类型 | CounterV2样式 |
| --- | --- |
| CounterV2Type.LIST | CounterV2NumberStyleOptions |
| CounterV2Type.COMPACT | CounterV2NumberStyleOptions |
| CounterV2Type.INLINE | CounterV2InlineStyleOptions |
| CounterV2Type.INLINE\_DATE | CounterV2DateStyleOptions |

## CounterV2Type

CounterV2Type指定CounterV2类型。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LIST | 0 | 列表型CounterV2。 |
| COMPACT | 1 | 紧凑型CounterV2。 |
| INLINE | 2 | 数值内联型CounterV2。 |
| INLINE\_DATE | 3 | 日期内联型CounterV2。 |

各类型CounterV2组件的展示效果可参考[示例1（列表型CounterV2）](ohos-arkui-advanced-counterv2.md#示例1列表型counterv2)、[示例2（紧凑型CounterV2）](ohos-arkui-advanced-counterv2.md#示例2紧凑型counterv2)、[示例3（数值内联型CounterV2）](ohos-arkui-advanced-counterv2.md#示例3数值内联型counterv2)、[示例4（日期内联型CounterV2）](ohos-arkui-advanced-counterv2.md#示例4日期内联型counterv2)。

## OnCounterV2HoverCallback

type OnCounterV2HoverCallback = (isHover: boolean) => void

定义CounterV2的鼠标悬浮回调类型。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isHover | boolean | 是 | 表示鼠标是否悬浮在组件上。  鼠标进入时为true，离开时为false。 |

## CounterV2CommonOptions

CounterV2CommonOptions定义了CounterV2的共通属性和事件。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| focusable | boolean | 否 | 是 | 设置CounterV2是否可获焦。  **说明：**  该属性对列表型和紧凑型CounterV2生效。对数值内联型和日期内联型CounterV2不生效。  默认值：true  true：CounterV2可获焦；false：CounterV2不可获焦。  值为undefined时，按默认值处理。 |
| step | number | 否 | 是 | 设置CounterV2的步长。  **说明：**  该属性对列表型、紧凑型和数值内联型CounterV2生效。对日期内联型CounterV2不生效。  取值范围：大于等于1的整数。  默认值：1  超出取值范围按默认值处理。  值为undefined时，按默认值处理。 |
| onHoverIncrease | [OnCounterV2HoverCallback](ohos-arkui-advanced-counterv2.md#oncounterv2hovercallback) | 否 | 是 | 鼠标进入或退出CounterV2组件的“增加按钮”时，触发该回调。  使用场景：当需要在鼠标悬浮“增加按钮”时执行自定义操作（如改变按钮样式、显示提示信息等）时传入此回调。  **说明：**  该属性对列表型、紧凑型和数值内联型CounterV2生效。对日期内联型CounterV2不生效。  默认值：undefined，表示不触发该回调。  值为undefined时，按默认值处理。 |
| onHoverDecrease | [OnCounterV2HoverCallback](ohos-arkui-advanced-counterv2.md#oncounterv2hovercallback) | 否 | 是 | 鼠标进入或退出CounterV2组件的“减少按钮”时，触发该回调。  使用场景：当需要在鼠标悬浮“减少按钮”时执行自定义操作（如改变按钮样式、显示提示信息等）时传入此回调。  **说明：**  该属性对列表型、紧凑型和数值内联型CounterV2生效。对日期内联型CounterV2不生效。  默认值：undefined，表示不触发该回调。  值为undefined时，按默认值处理。 |

## OnInlineCounterV2Change

type OnInlineCounterV2Change = (value: number) => void

定义数值内联型CounterV2的值变化回调类型。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前显示的数值。  取值范围：[min, max]，其中min和max分别对应CounterV2的最小值和最大值。 |

## CounterV2InlineStyleOptions

CounterV2InlineStyleOptions定义了数值内联型CounterV2的属性和事件。

继承于[CounterV2CommonOptions](ohos-arkui-advanced-counterv2.md#counterv2commonoptions)，包含该接口所有属性。本节仅展示新增属性，继承属性请参见父接口。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 否 | 是 | 设置CounterV2的初始值。  默认值：0  有效值范围：[min, max]，其中min和max分别对应CounterV2的最小值和最大值。  值为undefined时，按默认值处理。  边界处理：若value小于min则按min处理，若value大于max则按max处理。 |
| min | number | 否 | 是 | 设置CounterV2的最小值。  默认值：0  取值范围：(-∞, max]  超出取值范围时（即设置值大于max），按max处理。  值为undefined时，按默认值处理。 |
| max | number | 否 | 是 | 设置CounterV2的最大值。  默认值：999  取值范围：[min, +∞)  超出取值范围时（即设置值小于min），按min处理。  值为undefined时，按默认值处理。 |
| textWidth | number | 否 | 是 | 设置数值文本的宽度。  默认值：自适应文本宽度。  取值范围：[0, +∞)  单位：vp  超出取值范围时（即设置值小于0），按0处理。  值为undefined时，按默认值处理。 |
| onChange | [OnInlineCounterV2Change](ohos-arkui-advanced-counterv2.md#oninlinecounterv2change) | 否 | 是 | 数值改变时，触发该回调。回调参数value表示当前显示的数值。  使用场景：当需要在数值变化时执行自定义操作（如更新关联数据、触发业务逻辑、记录日志等）时传入此回调。  默认值：undefined，表示数值改变时不触发该回调。  值为undefined时，按默认值处理。 |

**说明** 

1. min应小于等于max。若min大于max，则按max处理。

## CounterV2NumberStyleOptions

CounterV2NumberStyleOptions定义了列表型和紧凑型CounterV2的属性和事件。

继承于[CounterV2InlineStyleOptions](ohos-arkui-advanced-counterv2.md#counterv2inlinestyleoptions)，包含该接口及[CounterV2CommonOptions](ohos-arkui-advanced-counterv2.md#counterv2commonoptions)所有属性。本节仅展示新增属性，继承属性请参见父接口。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| label | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置CounterV2的说明文本。  默认值：''  说明：当需要在CounterV2旁边显示说明文字（如“价格”、“数量”等）时传入此参数。  值为undefined时，按默认值处理。 |
| onFocusIncrease | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 当CounterV2组件的“增加按钮”获取焦点时，触发该回调。  使用场景：当需要在增加按钮获焦时执行自定义操作（如改变样式、记录日志等）时传入此回调。  默认值：undefined，表示不触发该回调。  值为undefined时，按默认值处理。 |
| onFocusDecrease | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 当CounterV2组件的“减少按钮”获取焦点时，触发该回调。  使用场景：当需要在减少按钮获焦时执行自定义操作（如改变样式、记录日志等）时传入此回调。  默认值：undefined，表示不触发该回调。  值为undefined时，按默认值处理。 |
| onBlurIncrease | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 当CounterV2组件的“增加按钮”失去焦点时，触发该回调。  使用场景：当需要在增加按钮失焦时执行自定义操作（如验证输入、保存状态等）时传入此回调。  默认值：undefined，表示不触发该回调。  值为undefined时，按默认值处理。 |
| onBlurDecrease | [VoidCallback](ts-types.md#voidcallback12) | 否 | 是 | 当CounterV2组件的“减少按钮”失去焦点时，触发该回调。  使用场景：当需要在减少按钮失焦时执行自定义操作（如验证输入、保存状态等）时传入此回调。  默认值：undefined，表示不触发该回调。  值为undefined时，按默认值处理。 |

## CounterV2DateData

CounterV2DateData定义了日期通用属性和方法，包括年、月、日。

### 属性

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| year | number | 否 | 否 | 表示日期内联型的年份。 |
| month | number | 否 | 否 | 表示日期内联型的月份。 |
| day | number | 否 | 否 | 表示日期内联型的日。 |

### constructor

constructor(year: number, month: number, day: number)

CounterV2DateData的构造函数用于初始化日期对象。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| year | number | 是 | 日期内联型的年份。取值范围：[1, 5000]。超出取值范围按默认值处理。 |
| month | number | 是 | 日期内联型的月份。取值范围：[1, 12]。超出取值范围按默认值处理。 |
| day | number | 是 | 日期内联型的日。取值范围：[1, 31]。必须为合法日期，如month为2月时，day传入30将视为异常值，按默认值处理。超出取值范围按默认值处理。 |

### toString

toString(): string

以字符串格式返回当前日期值。格式为"YYYY-MM-DD"。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 格式为“YYYY-MM-DD”的日期字符串，例如“2024-01-15”。 |

## OnDateCounterV2ChangeCallback

type OnDateCounterV2ChangeCallback = (date: CounterV2DateData) => void

定义日期内联型CounterV2的日期变化回调类型。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| date | [CounterV2DateData](ohos-arkui-advanced-counterv2.md#counterv2datedata) | 是 | 当前显示的日期值。 |

## CounterV2DateStyleOptions

CounterV2DateStyleOptions定义日期内联型CounterV2的属性和事件。

继承于[CounterV2CommonOptions](ohos-arkui-advanced-counterv2.md#counterv2commonoptions)，包含该接口所有属性。本节仅展示新增属性，继承属性请参见父接口。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| year | number | 否 | 是 | 设置日期内联型初始年份。  默认值：1  取值范围：[1, 5000]  超出取值范围按默认值处理。  值为undefined时，按默认值处理。 |
| month | number | 否 | 是 | 设置日期内联型初始月份。  默认值：1  取值范围：[1, 12]  超出取值范围按默认值处理。  值为undefined时，按默认值处理。 |
| day | number | 否 | 是 | 设置日期内联型初始日。  默认值：1  取值范围：[1, 31]  必须为合法日期，如month为2月时，day传入30将视为异常值，按默认值处理。  超出取值范围按默认值处理。  值为undefined时，按默认值处理。 |
| onDateChange | [OnDateCounterV2ChangeCallback](ohos-arkui-advanced-counterv2.md#ondatecounterv2changecallback) | 否 | 是 | 当日期改变时，触发该回调。回调参数date表示当前显示的日期值。  使用场景：当需要在日期变化时执行自定义操作（如更新关联数据、触发业务逻辑、记录日志等）时传入此回调。  默认值：undefined，表示不触发该回调。  值为undefined时，按默认值处理。 |

## 属性

不支持[通用属性](ts-component-general-attributes.md)。

## 事件

不支持[通用事件](ts-component-general-events.md)。

## 示例

### 示例1（列表型CounterV2）

该示例通过设置[CounterV2Type](ohos-arkui-advanced-counterv2.md#counterv2type).LIST和配置[CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options)的numberOptions属性，实现了列表型CounterV2。

从API版本26.0.0开始，[CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options)支持numberOptions属性。

```ts
import { CounterV2Type, CounterV2Component } from '@kit.ArkUI';

@Entry
@ComponentV2
struct ListCounterExample {
  build() {
    Column() {
      // 列表型CounterV2
      CounterV2Component({
        options: {
          type: CounterV2Type.LIST,
          numberOptions: {
            label: '价格',
            min: 0,
            value: 5,
            max: 10,
          }
        }
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/1-JlRoDNTwS9EdGOQsOOuw/zh-cn_image_0000002736435479.gif)

### 示例2（紧凑型CounterV2）

该示例通过设置[CounterV2Type](ohos-arkui-advanced-counterv2.md#counterv2type).COMPACT和配置[CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options)的numberOptions属性，实现紧凑型CounterV2。

从API版本26.0.0开始，[CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options)支持numberOptions属性。

```ts
import { CounterV2Type, CounterV2Component } from '@kit.ArkUI';

@Entry
@ComponentV2
struct CompactCounterExample {
  build() {
    Column() {
      // 紧凑型CounterV2
      CounterV2Component({
        options: {
          type: CounterV2Type.COMPACT,
          numberOptions: {
            label: '数量',
            value: 10,
            min: 0,
            max: 100,
            step: 10
          }
        }
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Oo8e1SOqRgyJVjhgHVlVgQ/zh-cn_image_0000002706836328.gif)

### 示例3（数值内联型CounterV2）

该示例通过设置[CounterV2Type](ohos-arkui-advanced-counterv2.md#counterv2type).INLINE和配置[CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options)的inlineOptions属性，实现数值内联型CounterV2。

从API版本26.0.0开始，[CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options)支持inlineOptions属性。

```ts
import { CounterV2Type, CounterV2Component } from '@kit.ArkUI';

@Entry
@ComponentV2
struct NumberStyleExample {
  build() {
    Column() {
      // 数值内联型CounterV2
      CounterV2Component({
        options: {
          type: CounterV2Type.INLINE,
          inlineOptions: {
            value: 100,
            min: 10,
            step: 2,
            max: 1000,
            textWidth: 100,
            onChange: (value: number) => {
              console.info('onCounterV2Change Counter: ' + value.toString());
            }
          }
        }
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/rCFXIEobQx6NxfU42bvNmA/zh-cn_image_0000002736315433.gif)

### 示例4（日期内联型CounterV2）

该示例通过设置[CounterV2Type](ohos-arkui-advanced-counterv2.md#counterv2type).INLINE\_DATE和配置[CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options)的dateOptions属性，实现日期内联型CounterV2。

从API版本26.0.0开始，[CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options)支持dateOptions属性。

```ts
import { CounterV2Type, CounterV2Component, CounterV2DateData } from '@kit.ArkUI';

@Entry
@ComponentV2
struct DateStyleExample {
  build() {
    Column() {
      // 日期内联型CounterV2
      CounterV2Component({
        options: {
          type: CounterV2Type.INLINE_DATE,
          dateOptions: {
            year: 2016,
            onDateChange: (date: CounterV2DateData) => {
              console.info('onDateChange Date: ' + date.toString());
            }
          }
        }
      })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/6cw-9hcoTeSllcGuYEv7Ow/zh-cn_image_0000002706676394.gif)

### 示例5（镜像布局展示）

该示例通过设置[CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options)的direction属性，实现列表型、紧凑型、数值内联型、日期内联型CounterV2的镜像布局。

从API版本26.0.0开始，[CounterV2Options](ohos-arkui-advanced-counterv2.md#counterv2options)支持direction属性。

```ts
import { CounterV2Type, CounterV2Component, CounterV2DateData } from '@kit.ArkUI';

@Entry
@ComponentV2
struct CounterPage {
  @Local currentDirection: Direction = Direction.Rtl

  build() {
    Column({space: 20}) {

      // 列表型CounterV2
      CounterV2Component({
        options: {
          direction: this.currentDirection,
          type: CounterV2Type.LIST,
          numberOptions: {
            label: '价格',
            min: 0,
            value: 5,
            max: 10,
          }
        }
      })

      // 紧凑型CounterV2
      CounterV2Component({
        options: {
          direction: this.currentDirection,
          type: CounterV2Type.COMPACT,
          numberOptions: {
            label: '数量',
            value: 10,
            min: 0,
            max: 100,
            step: 10
          }
        }
      })

      // 数值内联型CounterV2
      CounterV2Component({
        options: {
          type: CounterV2Type.INLINE,
          direction: this.currentDirection,
          inlineOptions: {
            value: 100,
            min: 10,
            step: 2,
            max: 1000,
            textWidth: 100,
            onChange: (value: number) => {
              console.info('onCounterV2Change Counter: ' + value.toString());
            }
          }
        }
      })

      // 日期内联型CounterV2
      CounterV2Component({
        options: {
          direction: this.currentDirection,
          type: CounterV2Type.INLINE_DATE,
          dateOptions: {
            year: 2024,
            onDateChange: (date: CounterV2DateData) => {
              console.info('onDateChange Date: ' + date.toString());
            }
          }
        }
      })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/j34FgwrpTmmBhwKMUCcI1A/zh-cn_image_0000002736435481.png)
