---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popup
title: Popup
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > Popup
category: harmonyos-references
scraped_at: 2026-04-29T13:53:01+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:98e93254d2852d24142ac94f9ba1825fe6e0b61c65dc01b5da9d87c15d251a6e
---

Popup是用于显示特定样式气泡。

说明

* 该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 建议结合[Popup控制](ts-universal-attributes-popup.md)中的自定义气泡功能。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Popup, PopupOptions, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## Popup

PhonePC/2in1TabletTVWearable

Popup(options: PopupOptions): void

**装饰器类型：**@Builder

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PopupOptions](ohos-arkui-advanced-popup.md#popupoptions) | 是 | 定义Popup组件的类型。 |

## PopupOptions

PhonePC/2in1TabletTVWearable

PopupOptions定义Popup的具体样式参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [PopupIconOptions](ohos-arkui-advanced-popup.md#popupiconoptions) | 否 | 是 | 设置popup图标。  **说明：**  当width和height设置异常值或0时不显示。  默认不显示图标。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| title | [PopupTextOptions](ohos-arkui-advanced-popup.md#popuptextoptions) | 否 | 是 | 设置popup标题文本。  默认不显示标题文本。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| message | [PopupTextOptions](ohos-arkui-advanced-popup.md#popuptextoptions) | 否 | 否 | 设置popup内容文本。  **说明：**  message不支持设置fontWeight。  默认不显示内容文本。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| showClose | boolean | [Resource](ts-types.md#resource) | 否 | 是 | 设置popup关闭按钮。  true：显示关闭按钮；false：不显示关闭按钮。  Resource：显示对应的图标。  默认值：true  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onClose | () => void | 否 | 是 | 设置popup关闭按钮回调函数。  默认不设置关闭按钮回调函数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| buttons | [[PopupButtonOptions](ohos-arkui-advanced-popup.md#popupbuttonoptions)?,[PopupButtonOptions](ohos-arkui-advanced-popup.md#popupbuttonoptions)?] | 否 | 是 | 设置popup操作按钮，按钮最多设置两个。  默认不显示按钮。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| direction12+ | [Direction](ts-appendix-enums.md#direction) | 否 | 是 | 布局方向。  默认值：Direction.Auto  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| maxWidth18+ | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置popup的最大宽度，通过此接口popup可以自定义宽度显示。  **说明：**  1. 在使用引用资源类型时，规定其参数类型要与属性方法本身类型一致。  2. maxWidth是数字类型，支持float和integer，例如$r('app.float.maxWidth')、$r('app.integer.maxWidth')。  3. 当类型为Resource时，如果未设置单位，默认单位为px。  默认值：400vp  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## PopupTextOptions

PhonePC/2in1TabletTVWearable

设置文本样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 设置文本内容。 |
| fontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置文本字体大小。  默认值：$r('sys.float.ohos\_id\_text\_size\_body2')  string类型可选值：可以转化为数字的字符串（如'10'）或带长度单位的字符串（如'10px'），不支持设置百分比字符串。  number：取值范围(0,+∞)。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置文本字体颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_secondary') |
| fontWeight | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | 否 | 是 | 设置文本字体粗细。  number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。  string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Regular |

## PopupButtonOptions

PhonePC/2in1TabletTVWearable

PopupButtonOptions定义按钮的相关属性和事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| text | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 设置按钮内容。 |
| action | () => void | 否 | 是 | 设置按钮click回调。  默认不执行任何操作。 |
| fontSize | number | string | [Resource](ts-types.md#resource) | 否 | 是 | 设置按钮文本字体大小。  默认值：$r('sys.float.ohos\_id\_text\_size\_button2')  string类型可选值：可以转化为数字的字符串（如'10'）或带长度单位的字符串（如'10px'），不支持设置百分比字符串。  设置值为异常值时取默认值。 |
| fontColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置按钮文本字体颜色。  默认值：$r('sys.color.ohos\_id\_color\_text\_primary\_activated') |

## PopupIconOptions

PhonePC/2in1TabletTVWearable

PopupIconOptions定义图标的属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| image | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 设置图标内容。 |
| width | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置图标宽度。  默认值：32VP |
| height | [Dimension](ts-types.md#dimension10) | 否 | 是 | 设置图标高度。  默认值：32VP |
| fillColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 设置图标填充颜色。仅针对svg图源生效。  默认不改变图标颜色。 |
| borderRadius | [Length](ts-types.md#length) | [BorderRadiuses](ts-types.md#borderradiuses9) | 否 | 是 | 设置图标圆角。  默认值：$r('sys.float.ohos\_id\_corner\_radius\_default\_s') |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置气泡样式）

该示例通过配置PopupIconOptions、PopupTextOptions、PopupButtonOptions实现气泡的样式。

```
1. // xxx.ets
2. import { Popup, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct PopupExample {
7. build() {
8. Row() {
9. // popup 自定义高级组件
10. Popup({
11. // PopupIconOptions类型设置图标内容
12. icon: {
13. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
14. image: $r('app.media.icon'),
15. width: 32,
16. height: 32,
17. fillColor: Color.White,
18. borderRadius: 16
19. } as PopupIconOptions,
20. // PopupTextOptions类型设置文字内容
21. title: {
22. text: 'This is a popup with PopupOptions',
23. fontSize: 20,
24. fontColor: Color.Black,
25. fontWeight: FontWeight.Normal
26. } as PopupTextOptions,
27. // PopupTextOptions类型设置文字内容
28. message: {
29. text: 'This is the message',
30. fontSize: 15,
31. fontColor: Color.Black
32. } as PopupTextOptions,
33. showClose: false,
34. onClose: () => {
35. console.info('close Button click');
36. },
37. // PopupButtonOptions类型设置按钮内容
38. buttons: [{
39. text: 'confirm',
40. action: () => {
41. console.info('confirm button click');
42. },
43. fontSize: 15,
44. fontColor: Color.Black,
45. },
46. {
47. text: 'cancel',
48. action: () => {
49. console.info('cancel button click');
50. },
51. fontSize: 15,
52. fontColor: Color.Black
53. },] as [PopupButtonOptions?, PopupButtonOptions?]
54. })
55. }
56. .width(300)
57. .height(200)
58. .borderWidth(2)
59. .justifyContent(FlexAlign.Center)
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/rGQtmNB1RUGmEz77DMbLZQ/zh-cn_image_0000002589246453.png?HW-CC-KV=V1&HW-CC-Date=20260429T054912Z&HW-CC-Expire=86400&HW-CC-Sign=A7091219948F0A606BB0DA9E845E5C1E661F45E3D10D8EEB25FB3413EE87B086)

### 示例 2（设置镜像效果）

该示例通过配置direction参数实现Popup的镜像布局效果。

```
1. // xxx.ets
2. import { Popup, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct PopupPage {
7. @State currentDirection: Direction = Direction.Rtl;

9. build() {
10. Column() {
11. // popup 自定义高级组件
12. Popup({
13. // PopupIconOptions 类型设置图标内容
14. direction: this.currentDirection,
15. icon: {
16. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
17. image: $r('app.media.icon'),
18. width: 32,
19. height: 32,
20. fillColor: Color.White,
21. borderRadius: 16,
22. } as PopupIconOptions,
23. // PopupTextOptions 类型设置文字内容
24. title: {
25. text: 'This is a popup with PopupOptions',
26. fontSize: 20,
27. fontColor: Color.Black,
28. fontWeight: FontWeight.Normal,

30. } as PopupTextOptions,
31. // PopupTextOptions 类型设置文字内容
32. message: {
33. text: 'This is the message',
34. fontSize: 15,
35. fontColor: Color.Black,
36. } as PopupTextOptions,
37. showClose: true,
38. onClose: () => {
39. console.info('close Button click');
40. },
41. // PopupButtonOptions 类型设置按钮内容
42. buttons: [{
43. text: 'confirm',
44. action: () => {
45. console.info('confirm button click');
46. },
47. fontSize: 15,
48. fontColor: Color.Black,

50. },
51. {
52. text: 'cancel',
53. action: () => {
54. console.info('cancel button click');
55. },
56. fontSize: 15,
57. fontColor: Color.Black,
58. },] as [PopupButtonOptions?, PopupButtonOptions?],
59. })

61. }
62. .justifyContent(FlexAlign.Center)
63. .width('100%')
64. .height('100%')
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/uXIWcsHEQGqGtgBfEl5xyg/zh-cn_image_0000002558766646.png?HW-CC-KV=V1&HW-CC-Date=20260429T054912Z&HW-CC-Expire=86400&HW-CC-Sign=8D10A1530BDCF1804ABAE31674A7780604704E93404E3A89A49514E2FAAA1705)

### 示例3（设置自定义宽度）

该示例通过配置maxWidth实现Popup的自定义宽度效果。

```
1. // xxx.ets
2. import { Popup, PopupTextOptions, PopupButtonOptions, PopupIconOptions } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct PopupPage {
7. @State currentDirection: Direction = Direction.Rtl;

9. build() {
10. Row() {
11. // popup 自定义高级组件
12. Popup({
13. // 设置自定义宽度
14. maxWidth: '50%',
15. // PopupIconOptions 类型设置图标内容
16. icon: {
17. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
18. image: $r('app.media.startIcon'),
19. width: 32,
20. height: 32,
21. fillColor: Color.White,
22. borderRadius: 16,
23. } as PopupIconOptions,
24. // PopupTextOptions类型设置文字内容
25. message: {
26. text: 'This is the message,This is the message,This is the message,This is the message',
27. fontSize: 15,
28. fontColor: Color.Black
29. } as PopupTextOptions,
30. showClose: false,
31. onClose: () => {
32. console.info('close Button click');
33. },
34. // PopupButtonOptions类型设置按钮内容
35. buttons: [{
36. text: 'confirm',
37. action: () => {
38. console.info('confirm button click');
39. },
40. fontSize: 15,
41. fontColor: Color.Black,
42. },
43. {
44. text: 'cancel',
45. action: () => {
46. console.info('cancel button click');
47. },
48. fontSize: 15,
49. fontColor: Color.Black
50. },] as [PopupButtonOptions?, PopupButtonOptions?]
51. })
52. }
53. .width(400)
54. .height(200)
55. .borderWidth(2)
56. .justifyContent(FlexAlign.Center)
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/uownckouT9WT0Ci_3peXqQ/zh-cn_image_0000002558606986.png?HW-CC-KV=V1&HW-CC-Date=20260429T054912Z&HW-CC-Expire=86400&HW-CC-Sign=1568B8329729003A20F2CA04E011E189631ABF5A9182FA549F6CC7091614EDCC)
