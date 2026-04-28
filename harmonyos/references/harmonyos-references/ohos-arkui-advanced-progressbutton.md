---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-progressbutton
title: ProgressButton
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > ProgressButton
category: harmonyos-references
scraped_at: 2026-04-28T08:02:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:43fe8782e381611e6ffc528b8503f4e1200bcf159568fe41ffcb5650b11e1b2c
---

文本下载按钮，可显示具体下载进度。

说明

* 该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件仅可在Stage模型下使用。
* 如果ProgressButton设置[通用属性](ts-component-general-attributes.md)和[通用事件](ts-component-general-events.md)，编译工具链会额外生成节点\_\_Common\_\_，并将通用属性或通用事件挂载在\_\_Common\_\_上，而不是直接应用到ProgressButton本身。这可能导致开发者设置的通用属性或通用事件不生效或不符合预期，因此，不建议ProgressButton设置通用属性和通用事件。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ProgressButton } from '@kit.ArkUI';
```

## ProgressButton

PhonePC/2in1TabletTVWearable

ProgressButton({progress: number, content: ResourceStr, progressButtonWidth?: Length, clickCallback: () => void, enable: boolean, colorOptions?: ProgressButtonColorOptions, progressButtonRadius?: LengthMetrics})

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 是 | @Prop | 下载按钮的当前进度值。  取值范围：[0,100]。设置小于0的数值时置为0，设置大于100的数值时置为100。  默认值：0  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| content | [ResourceStr](ts-types.md#resourcestr) | 是 | @Prop | 下载按钮的文本。  默认值：空字符串。  **说明**：最长显示组件宽度，超出部分用省略号代替。从API version 20开始，支持Resource类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| progressButtonWidth | [Length](ts-types.md#length) | 否 | - | 下载按钮的宽度，单位vp。  取值范围：大于等于44vp。  默认值：44vp。当取值为非Resource类型且小于默认值或取值为非法值时，识别值为默认值。当取值为Resource类型且小于默认值时识别为默认值，为非法值时下载按钮的宽度显示为容器宽度的100%。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| clickCallback | () => void | 是 | - | 下载按钮的点击回调。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| enable | boolean | 是 | @Prop | 下载按钮是否可以点击。  true：可以点击。  false：不可点击。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| colorOptions18+ | [ProgressButtonColorOptions](ohos-arkui-advanced-progressbutton.md#progressbuttoncoloroptions18) | 否 | @Prop | 下载按钮颜色。用于自定义按钮各部分的颜色（进度条、描边、文本、背景）。需要自定义颜色时传入此参数，不传入时使用系统默认配色方案。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| progressButtonRadius18+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | @Prop | 下载按钮的圆角（不支持百分比百分比设置）。  取值范围：[0, height/2]  默认值：height/2  设置值小于0时按照0处理，设置其他非法数值时，按照默认值处理。当直接入参为undefined时，按照默认值处理，入参为LengthMetrics.vp时，建议传入具体数值，传入null/undefined会导致显示异常。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## ProgressButtonColorOptions18+

PhonePC/2in1TabletTVWearable

下载按钮颜色选项

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**设备行为差异：** 该接口在Wearable设备上使用时，应用程序运行异常，异常信息中提示接口未定义，在其他设备中可正常调用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progressColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 进度条颜色。  默认值：#330A59F7 |
| borderColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮描边颜色。  默认值：#330A59F7 |
| textColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮文本颜色。  默认值：系统默认值（#CE000000） |
| backgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 按钮背景色。  默认值：$r('sys.color.ohos\_id\_color\_foreground\_contrary') |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（进度条下载按钮）

该示例实现了一个简单的带加载进度的文本下载按钮。

```
1. import { ProgressButton } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State progressIndex: number = 0;
7. @State textState: string = '下载';
8. @State buttonWidth: number = 200;
9. @State isRunning: boolean = false;
10. @State enableState: boolean = true;

12. build() {
13. Column() {
14. Scroll() {
15. Column({ space: 20 }) {
16. ProgressButton({
17. progress: this.progressIndex,
18. progressButtonWidth: this.buttonWidth,
19. content: this.textState,
20. enable: this.enableState,
21. clickCallback: () => {
22. if (this.textState && !this.isRunning && this.progressIndex < 100) {
23. this.textState = '继续';
24. }
25. this.isRunning = !this.isRunning;
26. let timer = setInterval(() => {
27. if (this.isRunning) {
28. if (this.progressIndex === 100) {
29. clearInterval(timer);
30. } else {
31. this.progressIndex++;
32. if (this.progressIndex === 100) {
33. this.textState = '已完成';
34. this.enableState = false;
35. }
36. }
37. } else {
38. clearInterval(timer);
39. }
40. }, 20)
41. }
42. })
43. }.alignItems(HorizontalAlign.Center).width('100%').margin({ top: 20 })
44. }
45. }
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/LqHlvGKbSRCJFR4rxbEsaQ/zh-cn_image_0000002583480121.png?HW-CC-KV=V1&HW-CC-Date=20260428T000237Z&HW-CC-Expire=86400&HW-CC-Sign=BB78E832B61EE01ABFD4FD3669CFEB9007735FA23FAD7B849A811C884C6F55A7)

### 示例2（自定义颜色按钮）

该示例实现了一个简单的自定义颜色的文本下载按钮。

```
1. import { ProgressButton } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State progressIndex: number = 0;
7. @State textState: string = '下载';
8. @State buttonWidth: number = 200;
9. @State isRunning: boolean = false;
10. @State enableState: boolean = true;

12. build() {
13. Column() {
14. Scroll() {
15. Column({ space: 20 }) {
16. ProgressButton({
17. // 设置下载按钮颜色
18. colorOptions: {
19. progressColor: Color.Orange,
20. borderColor: Color.Black,
21. textColor: Color.Blue,
22. backgroundColor: Color.Pink
23. },
24. progress: this.progressIndex,
25. progressButtonWidth: this.buttonWidth,
26. content: this.textState,
27. enable: this.enableState,
28. clickCallback: () => {
29. if (this.textState && !this.isRunning && this.progressIndex < 100) {
30. this.textState = '继续';
31. }
32. this.isRunning = !this.isRunning;
33. let timer = setInterval(() => {
34. if (this.isRunning) {
35. if (this.progressIndex === 100) {
36. clearInterval(timer);
37. } else {
38. this.progressIndex++;
39. if (this.progressIndex === 100) {
40. this.textState = '已完成';
41. this.enableState = false;
42. }
43. }
44. } else {
45. clearInterval(timer);
46. }
47. }, 20)
48. }
49. })
50. }.alignItems(HorizontalAlign.Center).width('100%').margin({ top: 20 })
51. }
52. }
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/wP_Q6V7jTJ-Z3AYi3xGjMw/zh-cn_image_0000002552800472.png?HW-CC-KV=V1&HW-CC-Date=20260428T000237Z&HW-CC-Expire=86400&HW-CC-Sign=63C89E72CBAC80F803D2CD1375C5C6CCB3CFDBB62D76CF52EB71ECD6163589DA)

### 示例3（自定义圆角按钮）

该示例实现了一个简单的自定义圆角的文本下载按钮。

```
1. import { ProgressButton, LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State progressIndex: number = 0;
7. @State textState: string = '下载';
8. @State buttonWidth: number = 200;
9. @State isRunning: boolean = false;
10. @State enableState: boolean = true;

12. build() {
13. Column() {
14. Scroll() {
15. Column({ space: 20 }) {
16. ProgressButton({
17. progressButtonRadius: LengthMetrics.vp(8), // 自定义圆角值为8vp
18. progress: this.progressIndex,
19. progressButtonWidth: this.buttonWidth,
20. content: this.textState,
21. enable: this.enableState,
22. clickCallback: () => {
23. if (this.textState && !this.isRunning && this.progressIndex < 100) {
24. this.textState = '继续';
25. }
26. this.isRunning = !this.isRunning;
27. let timer = setInterval(() => {
28. if (this.isRunning) {
29. if (this.progressIndex === 100) {
30. clearInterval(timer);
31. } else {
32. this.progressIndex++;
33. if (this.progressIndex === 100) {
34. this.textState = '已完成';
35. this.enableState = false;
36. }
37. }
38. } else {
39. clearInterval(timer);
40. }
41. }, 20)
42. }
43. })
44. }.alignItems(HorizontalAlign.Center).width('100%').margin({ top: 20 })
45. }
46. }
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/Ej9uvcwMTdecAWELIQezEw/zh-cn_image_0000002583440167.png?HW-CC-KV=V1&HW-CC-Date=20260428T000237Z&HW-CC-Expire=86400&HW-CC-Sign=291F91EF98AC97E8C96CD2D19055345736A22283CBB437D80D0B70545B18F110)
