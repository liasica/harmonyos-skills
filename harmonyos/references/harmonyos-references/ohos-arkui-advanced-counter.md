---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-counter
title: advanced.Counter
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > advanced.Counter
category: harmonyos-references
scraped_at: 2026-04-29T13:53:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9909620f7fc044d5f3a9036c59c3baf031bef5d1944349994f4ce2952b693fc6
---

Counter组件用于精确调节数值。

说明

该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

如果Counter设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到Counter本身。这可能导致开发者设置的通用属性或通用事件的效果不生效或不符合预期，因此，不建议Counter设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { CounterType, CounterComponent, CounterOptions, DateData } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## CounterComponent

PhonePC/2in1TabletTVWearable

CounterComponent({ options: CounterOptions })

定义Counter。

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数**：

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| options | [CounterOptions](ohos-arkui-advanced-counter.md#counteroptions) | 是 | @Prop | 定义Counter组件的类型。 |

## CounterOptions

PhonePC/2in1TabletTVWearable

CounterOptions定义Counter类型及样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [CounterType](ohos-arkui-advanced-counter.md#countertype) | 否 | 否 | 指定当前Counter的类型。 |
| direction12+ | [Direction](ts-appendix-enums.md#direction) | 否 | 是 | 布局方向。  默认值：Direction.Auto  值为undefined时，按默认值处理。 |
| numberOptions | [NumberStyleOptions](ohos-arkui-advanced-counter.md#numberstyleoptions) | 否 | 是 | 列表型和紧凑型Counter的样式。  默认值：显示计数器为0的列表型或紧凑型Counter。  值为undefined时，按默认值处理。 |
| inlineOptions | [InlineStyleOptions](ohos-arkui-advanced-counter.md#inlinestyleoptions) | 否 | 是 | 普通数字内联调节型Counter的样式。  默认值：显示计数器为0的普通数字内联调节型Counter。  值为undefined时，按默认值处理。 |
| dateOptions | [DateStyleOptions](ohos-arkui-advanced-counter.md#datestyleoptions) | 否 | 是 | 日期型内联型Counter的样式。  默认值：显示0001/01/01的日期型内联型Counter。  值为undefined时，按默认值处理。 |

选择不同的Counter类型，需要选择对应的Counter样式。

| counter类型 | counter样式 |
| --- | --- |
| CounterType.LIST | NumberStyleOptions |
| CounterType.COMPACT | NumberStyleOptions |
| CounterType.INLINE | InlineStyleOptions |
| CounterType.INLINE\_DATE | DateStyleOptions |

## CounterType

PhonePC/2in1TabletTVWearable

CounterType指定Counter类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LIST | 0 | 列表型Counter。 |
| COMPACT | 1 | 紧凑型Counter。 |
| INLINE | 2 | 普通数字内联调节型Counter。 |
| INLINE\_DATE | 3 | 日期型内联型Counter。 |

## CommonOptions

PhonePC/2in1TabletTVWearable

CommonOptions定义了Counter的共通属性和事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| focusable | boolean | 否 | 是 | 设置Counter是否可获焦。  **说明：**  该属性对列表型和紧凑型Counter生效。  默认值：true  true：Counter可获焦；false：Counter不可获焦。  值为undefined时，按默认值处理。 |
| step | number | 否 | 是 | 设置Counter的步长。  取值范围：大于等于1的整数。  默认值：1  超出取值范围按默认值处理。 |
| onHoverIncrease | (isHover: boolean) => void | 否 | 是 | 鼠标进入或退出Counter组件的增加按钮时触发该回调。  isHover：表示鼠标是否悬浮在组件上，鼠标进入时为true，退出时为false。  默认值：不触发鼠标进入或退出Counter组件的增加按钮时的回调。  值为undefined时，按默认值处理。 |
| onHoverDecrease | (isHover: boolean) => void | 否 | 是 | 鼠标进入或退出Counter组件的减小按钮时触发该回调。  isHover：表示鼠标是否悬浮在组件上，进入时为true，离开时为false。  默认值：不触发鼠标进入或退出Counter组件的减小按钮时的回调。  值为undefined时，按默认值处理。 |

## InlineStyleOptions

PhonePC/2in1TabletTVWearable

InlineStyleOptions定义了数值内联型Counter的属性和事件。

继承于[CommonOptions](ohos-arkui-advanced-counter.md#commonoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 否 | 是 | 设置Counter的初始值。  默认值：0  取值范围：[min, max]，其中min和max分别对应下述Counter的最小值和最大值。  超出取值范围时，如果值为undefined，按默认值处理，否则按最大值处理。 |
| min | number | 否 | 是 | 设置Counter的最小值。  默认值：0  取值范围：(-∞, +∞)  值为undefined时，按默认值处理。 |
| max | number | 否 | 是 | 设置Counter的最大值。  默认值：999  取值范围：(-∞, +∞)  值为undefined时，按默认值处理。 |
| textWidth | number | 否 | 是 | 设置数值文本的宽度。  默认值：自适应文本宽度。  取值范围：[0, +∞)  单位：vp  超出取值范围时，如果值为undefined，按默认值处理，否则按最大值处理。 |
| onChange | (value: number) => void | 否 | 是 | 数值改变时，返回当前值。  value：当前显示的数值。  默认值：数值改变时，不返回值。  值为undefined时，按默认值处理。 |

## NumberStyleOptions

PhonePC/2in1TabletTVWearable

NumberStyleOptions定义了列表型和紧凑型Counter的属性和事件。

继承于[InlineStyleOptions](ohos-arkui-advanced-counter.md#inlinestyleoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| label | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置Counter的说明文本。  默认值：' '  值为undefined时，按默认值处理。 |
| onFocusIncrease | () => void | 否 | 是 | 当前Counter组件的增加按钮获取焦点时触发的回调。  默认值：不触发增加按钮获取焦点时的回调。  值为undefined时，按默认值处理。 |
| onFocusDecrease | () => void | 否 | 是 | 当前Counter组件的减小按钮获取焦点时触发的回调。  默认值：不触发减少按钮获取焦点时的回调。  值为undefined时，按默认值处理。 |
| onBlurIncrease | () => void | 否 | 是 | 当前Counter组件的增加按钮失去焦点时触发的回调。  默认值：不触发增加按钮失去焦点时的回调。  值为undefined时，按默认值处理。 |
| onBlurDecrease | () => void | 否 | 是 | 当前Counter组件的减小按钮失去焦点时触发的回调。  默认值：不触发减少按钮失去焦点时的回调。  值为undefined时，按默认值处理。 |

## DateStyleOptions

PhonePC/2in1TabletTVWearable

DateStyleOptions定义日期内联型Counter的属性和事件。

继承于[CommonOptions](ohos-arkui-advanced-counter.md#commonoptions)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| year | number | 否 | 是 | 设置日期内联型初始年份。  默认值：1  取值范围：[1, 5000]  超出取值范围按默认值处理。 |
| month | number | 否 | 是 | 设置日期内联型初始月份。  默认值：1  取值范围：[1, 12]  超出取值范围按默认值处理。 |
| day | number | 否 | 是 | 设置日期内联型初始日。  默认值：1  取值范围：[1, 31]  超出取值范围按默认值处理。 |
| onDateChange | (date: [DateData](ohos-arkui-advanced-counter.md#datedata)) => void | 否 | 是 | 当日期改变时，返回当前日期。  date：当前显示的日期值。  值为undefined时，不显示当前的日期值。 |

## DateData

PhonePC/2in1TabletTVWearable

DateData定义了日期通用属性和方法，包括年、月、日。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| year | number | 否 | 否 | 设置日期内联型初始年份。  默认值：1  取值范围：[1, 5000]  超出取值范围按默认值处理。 |
| month | number | 否 | 否 | 设置日期内联型初始月份。  默认值：1  取值范围：[1, 12]  超出取值范围按默认值处理。 |
| day | number | 否 | 否 | 设置日期内联型初始日。  默认值：1  取值范围：[1, 31]  超出取值范围按默认值处理。 |

### constructor

PhonePC/2in1TabletTVWearable

constructor(year: number, month: number, day: number)

DateData的构造函数用于初始化日期对象。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| year | number | 是 | 设置日期内联型初始年份。 |
| month | number | 是 | 设置日期内联型初始月份。 |
| day | number | 是 | 设置日期内联型初始日。 |

### toString

PhonePC/2in1TabletTVWearable

toString(): string

以字符串格式返回当前日期值。格式为’YYYY-MM-DD'。

**元服务API**：从API version 12 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前日期值。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（列表型Counter）

该示例通过设置type为CounterType.LIST和配置numberOptions，实现了列表型Counter。

```
1. import { CounterType, CounterComponent } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ListCounterExample {
6. build() {
7. Column() {
8. //列表型Counter
9. CounterComponent({
10. options: {
11. type: CounterType.LIST,
12. numberOptions: {
13. label: '价格',
14. min: 0,
15. value: 5,
16. max: 10
17. }
18. }
19. })
20. }
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/lKy8qJwOQUeHQvOSjHERrQ/zh-cn_image_0000002558766666.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=B724D3FFCF7F3ED26F96DBE77C24009FA6ECE44028F0F1D5A51FA7697264CDD2)

### 示例2（紧凑型Counter）

该示例通过设置type为CounterType.COMPACT和numberOptions，实现紧凑型Counter。

```
1. import { CounterType, CounterComponent } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct CompactCounterExample {
6. build() {
7. Column() {
8. //紧凑型Counter
9. CounterComponent({
10. options: {
11. type: CounterType.COMPACT,
12. numberOptions: {
13. label: '数量',
14. value: 10,
15. min: 0,
16. max: 100,
17. step: 10
18. }
19. }
20. })
21. }
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/V8I4ZBwoScKWgP_vTXSZOA/zh-cn_image_0000002558607006.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=6B2CE3CDC26C34DB548634A00E7A97F0863040D6FEA1E495AD9F22162DBAFB70)

### 示例3（数值内联型Counter）

设置type为CounterType.INLINE和inlineOptions，实现数值内联型Counter。

```
1. import { CounterType, CounterComponent } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct NumberStyleExample {
6. build() {
7. Column() {
8. //数值内联型Counter
9. CounterComponent({
10. options: {
11. type: CounterType.INLINE,
12. inlineOptions: {
13. value: 100,
14. min: 10,
15. step: 2,
16. max: 1000,
17. textWidth: 100,
18. onChange: (value: number) => {
19. console.info('onCounterChange Counter: ' + value.toString());
20. }
21. }
22. }
23. })
24. }
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/eVChhyDHQiyNMvgjYZHRWg/zh-cn_image_0000002589326533.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=9BADBE1A90BA4AAC45A8F133C12487A4440490931A9B92C90B4326A0F5920CD4)

### 示例4（日期内联型Counter）

设置type为CounterType.INLINE\_DATE和dateOptions，实现日期内联型Counter。

```
1. import { CounterType, CounterComponent, DateData } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct DataStyleExample {
6. build() {
7. Column() {
8. //日期内联型counter
9. CounterComponent({
10. options: {
11. type: CounterType.INLINE_DATE,
12. dateOptions: {
13. year: 2016,
14. onDateChange: (date: DateData) => {
15. console.info('onDateChange Date: ' + date.toString());
16. }
17. }
18. }
19. })
20. }
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/EBNt8bcHTbm6kkMZS6-efA/zh-cn_image_0000002589246475.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=9E00B7584CF706D8D105A8947645C8EBFDEDB1390B61D318B3A9E3069470FA56)

### 示例5（镜像布局展示）

设置direction属性，实现列表型、紧凑型、数字内联型、日期内联型Counter的镜像布局。

```
1. import { CounterType, CounterComponent, DateData } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct CounterPage {
6. @State currentDirection: Direction = Direction.Rtl

8. build() {
9. Column({}) {

11. //列表型Counter
12. CounterComponent({
13. options: {
14. direction: this.currentDirection,
15. type: CounterType.LIST,
16. numberOptions: {
17. label: '价格',
18. min: 0,
19. value: 5,
20. max: 10,
21. }
22. }
23. })
24. .width('80%')

26. //数值型Counter
27. CounterComponent({
28. options: {
29. direction: this.currentDirection,
30. type: CounterType.COMPACT,
31. numberOptions: {
32. label: '数量',
33. value: 10,
34. min: 0,
35. max: 100,
36. step: 10
37. }
38. }
39. }).margin({ top: 20 })

41. //数值内联型Counter
42. CounterComponent({
43. options: {
44. type: CounterType.INLINE,
45. direction: this.currentDirection,
46. inlineOptions: {
47. value: 100,
48. min: 10,
49. step: 2,
50. max: 1000,
51. textWidth: 100,
52. onChange: (value: number) => {
53. console.info('onCounterChange Counter: ' + value.toString());
54. }
55. }
56. }
57. }).margin({ top: 20 })
58. //日期内联型counter
59. CounterComponent({
60. options: {
61. direction: this.currentDirection,
62. type: CounterType.INLINE_DATE,
63. dateOptions: {
64. year: 2024,
65. onDateChange: (date: DateData) => {
66. console.info('onDateChange Date: ' + date.toString());
67. }
68. }
69. }
70. }).margin({ top: 20 })
71. }
72. .width('100%')
73. .height('100%')
74. .justifyContent(FlexAlign.Center)
75. .alignItems(HorizontalAlign.Center)
76. }
77. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/VCAJHB2rT9iqoU8a0bAxyA/zh-cn_image_0000002558766668.png?HW-CC-KV=V1&HW-CC-Date=20260429T055304Z&HW-CC-Expire=86400&HW-CC-Sign=8C113BBB0CFC238BADDFC0CB0743D8E1ED563C6BA09EC2048AF56BF54EE01013)
