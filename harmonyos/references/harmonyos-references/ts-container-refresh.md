---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh
title: Refresh
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > Refresh
category: harmonyos-references
scraped_at: 2026-04-29T13:51:50+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:626947cf20b570d1e7c133ec67670d84ddab4d5fd04c4bb3e35b284a7038024a
---

可以进行页面下拉操作并显示刷新动效的容器组件。

说明

* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件从API version 12开始支持与垂直滚动的[Swiper](ts-container-swiper.md)和[Web](js-components-basic-web.md)的联动。当[Swiper](ts-container-swiper.md)设置[loop](ts-container-swiper.md#loop)属性为true时，Refresh无法和[Swiper](ts-container-swiper.md)产生联动。
* Refresh和内容大小小于组件自身的[List](ts-container-list.md)组件嵌套使用并且中间还有其他组件时，手势可能会被中间组件响应，导致Refresh未产生下拉刷新效果，可以将[alwaysEnabled](ts-container-scrollable-common.md#edgeeffectoptions11对象说明)参数设为true，此时[List](ts-container-list.md)会响应手势并通过嵌套滚动带动Refresh组件产生下拉刷新效果，具体可以参考[示例9不满一屏实现下拉刷新](ts-container-refresh.md#示例9不满一屏场景实现下拉刷新)。
* 组件内部已绑定手势实现跟手滚动等功能，需要增加自定义手势操作时请参考[手势拦截增强](ts-gesture-blocking-enhancement.md)进行处理。
* 组件无法通过鼠标按下拖动操作进行下拉刷新。

## 子组件

PhonePC/2in1TabletTVWearable

支持单个子组件。

从API version 11开始，Refresh子组件会跟随手势下拉而下移。

## 接口

PhonePC/2in1TabletTVWearable

Refresh(value: RefreshOptions)

创建Refresh容器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [RefreshOptions](ts-container-refresh.md#refreshoptions对象说明) | 是 | 刷新组件参数。 |

## RefreshOptions对象说明

PhonePC/2in1TabletTVWearable

用于设置Refresh组件参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| refreshing | boolean | 否 | 否 | 组件当前是否处于刷新中状态。true表示处于刷新中状态，false表示未处于刷新中状态。  默认值：false  该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| offset(deprecated) | number | string | 否 | 是 | 下拉起点距离组件顶部的距离。  默认值：16，单位vp。类型为string时，需要显式指定像素单位，如'10px'；未指定像素单位时，如'10'，单位为vp。  **说明：** 从API version 8开始支持，从API version 11开始废弃，无替代接口。  **说明：**  offset取值范围[0vp,64vp]。大于64vp按照64vp处理。不支持百分比，不支持负数。 |
| friction(deprecated) | number | string | 否 | 是 | 下拉摩擦系数，取值范围为0到100。  默认值：62  - 0表示下拉刷新容器不跟随手势下拉而下拉。  - 100表示下拉刷新容器紧紧跟随手势下拉而下拉。  - 数值越大，下拉刷新容器跟随手势下拉的反应越灵敏。  **说明：** 从API version 8开始支持，从API version 11开始废弃，建议使用[pullDownRatio](ts-container-refresh.md#pulldownratio12)替代。 |
| builder10+ | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 自定义刷新区域显示内容。  **说明：**  API version 10及之前版本，自定义组件的高度限制在64vp之内。API version 11及以后版本没有此限制。  自定义组件设置了固定高度时，自定义组件会以固定高度显示在刷新区域下方；自定义组件未设置高度时，自定义组件高度会自适应刷新区域高度，会发生自定义组件高度跟随刷新区域变化至0的现象。建议对自定义组件设置最小高度约束来避免自定义组件高度小于预期的情况发生，具体可参照[示例3](ts-container-refresh.md#示例3自定义刷新区域显示内容-builder)。  从API version 12开始，建议使用refreshingContent参数替代builder参数自定义刷新区域显示内容，以避免刷新过程中因自定义组件销毁重建造成的动画中断问题。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| promptText12+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置刷新区域底部显示的自定义文本。  **说明：**  输入文本的限制参考Text组件，使用builder或refreshingContent参数自定义刷新区域显示内容时，promptText不显示。  promptText设置有效时，[refreshOffset](ts-container-refresh.md#refreshoffset12)属性默认值为96vp。  自定义文本最大的字体缩放倍数[maxFontScale](ts-basic-components-text.md#maxfontscale12)为2。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| refreshingContent12+ | [ComponentContent](js-apis-arkui-componentcontent.md) | 否 | 是 | 自定义刷新区域显示内容。  **说明：**  与builder参数同时设置时builder参数不生效。  自定义组件设置了固定高度时，自定义组件会以固定高度显示在刷新区域下方；自定义组件未设置高度时，自定义组件高度会自适应刷新区域高度，会发生自定义组件高度跟随刷新区域变化至0的现象。建议对自定义组件设置最小高度约束来避免自定义组件高度小于预期的情况发生，具体可参照[示例4](ts-container-refresh.md#示例4自定义刷新区域显示内容-refreshingcontent)。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

说明

* 当未设置builder或refreshingContent时，是通过更新子组件的[translate](ts-universal-attributes-transformation.md#translate)属性实现的下拉位移效果，下拉位移过程中不会触发子组件的[onAreaChange](ts-universal-component-area-change-event.md#onareachange)事件，子组件设置[translate](ts-universal-attributes-transformation.md#translate)属性时不会生效。
* 当设置了builder或refreshingContent时，是通过更新子组件相对于Refresh组件的位置实现的下拉位移效果，下拉位移过程中可以触发子组件的[onAreaChange](ts-universal-component-area-change-event.md#onareachange)事件，子组件设置[position](ts-universal-attributes-location.md#position)属性时会固定子组件相对于Refresh组件的位置导致子组件不会跟手进行下拉位移。
* 通过builder参数设置的自定义组件在未指定宽度和高度时，其尺寸将自适应子组件，在指定宽度而未指定高度时，其高度将自适应下拉距离。通过refreshingContent参数设置的自定义组件若未指定高度，其高度同样会自适应下拉距离。当自定义组件高度自适应下拉距离时，随着下拉距离的增加，该组件的高度亦随之增加；当自定义组件的高度设定为固定值或达到最大高度限制时，随着下拉距离的增加，自定义组件与Refresh组件上边界之间的间距亦会随之增加。

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### refreshOffset12+

PhonePC/2in1TabletTVWearable

refreshOffset(value: number)

设置触发刷新的下拉偏移量，当下拉距离小于该属性设置值时离手不会触发刷新。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 下拉偏移量，单位vp。  默认值：未设置[promptText](ts-container-refresh.md#refreshoptions对象说明)参数时为64vp，设置了[promptText](ts-container-refresh.md#refreshoptions对象说明)参数时为96vp。  如果取值为0或负数的时候此接口采用默认值。 |

### pullToRefresh12+

PhonePC/2in1TabletTVWearable

pullToRefresh(value: boolean)

设置当下拉距离超过[refreshOffset](ts-container-refresh.md#refreshoffset12)时是否能触发刷新。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 当下拉距离超过[refreshOffset](ts-container-refresh.md#refreshoffset12)时是否能触发刷新。true表示能触发刷新，false表示不能触发刷新。  默认值：true |

### pullUpToCancelRefresh23+

PhonePC/2in1TabletTVWearable

pullUpToCancelRefresh(enabled: boolean | undefined)

设置上划是否取消刷新。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | undefined | 是 | 设置上划是否取消刷新。  true表示取消刷新；false表示不取消刷新。  值为undefined时，上划取消刷新。 |

### pullDownRatio12+

PhonePC/2in1TabletTVWearable

pullDownRatio(ratio: [Optional](ts-universal-attributes-custom-property.md#optionalt)<number>)

设置下拉跟手系数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ratio | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 下拉跟手系数。数值越大，跟随手势下拉的反应越灵敏。0表示不跟随手势下拉，1表示等比例跟随手势下拉。  没有设置或设置为undefined时，默认使用动态下拉跟手系数，下拉距离越大，跟手系数越小。  有效值为0-1之间的值，小于0的值会被视为0，大于1的值会被视为1。 |

### maxPullDownDistance20+

PhonePC/2in1TabletTVWearable

maxPullDownDistance(distance: Optional<number>)

设置最大下拉距离。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| distance | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 最大下拉距离。最大下拉距离的最小值为0，小于0按0处理。当该值小于刷新的下拉偏移量refreshOffset时，Refresh下拉离手不会触发刷新。  undefined和null按没有设置此属性处理。  默认值：undefined  单位：vp |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onStateChange

PhonePC/2in1TabletTVWearable

onStateChange(callback: (state: RefreshStatus) => void)

当前刷新状态变更时，触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [RefreshStatus](ts-container-refresh.md#refreshstatus枚举说明) | 是 | 刷新状态。 |

### onRefreshing

PhonePC/2in1TabletTVWearable

onRefreshing(callback: () => void)

进入刷新状态时触发回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 进入刷新状态时触发的回调。 |

### onOffsetChange12+

PhonePC/2in1TabletTVWearable

onOffsetChange(callback: Callback<number>)

下拉距离发生变化时触发回调。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<number> | 是 | 回调函数，用于监听下拉距离的变化。当下拉距离发生变化时触发，回调参数为当前的下拉距离。  单位：vp |

## RefreshStatus枚举说明

PhonePC/2in1TabletTVWearable

RefreshStatus刷新状态枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Inactive | 0 | 默认未下拉状态。 |
| Drag | 1 | 下拉中，下拉距离小于刷新距离。  若此时松手，组件进入Inactive状态；若此时继续下拉使下拉距离超过刷新距离，组件进入OverDrag状态。 |
| OverDrag | 2 | 下拉中，下拉距离超过刷新距离。  若此时松手，组件进入Refresh状态；若此时上滑使下拉距离小于刷新距离，组件进入Drag状态。 |
| Refresh | 3 | 下拉结束，回弹至刷新距离，进入刷新中状态。 |
| Done | 4 | 刷新结束，返回初始状态（顶部）。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（默认刷新样式）

刷新区域使用默认刷新样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RefreshExample {
5. @State isRefreshing: boolean = false;
6. @State arr: String[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

8. build() {
9. Column() {
10. Row() {
11. Button('开始刷新').onClick(() => {
12. this.isRefreshing = true;
13. })
14. Button('停止刷新').onClick(() => {
15. this.isRefreshing = false;
16. })
17. }

19. Refresh({ refreshing: $$this.isRefreshing }) {
20. List() {
21. ForEach(this.arr, (item: string) => {
22. ListItem() {
23. Text('' + item)
24. .width('70%')
25. .height(80)
26. .fontSize(16)
27. .margin(10)
28. .textAlign(TextAlign.Center)
29. .borderRadius(10)
30. .backgroundColor(0xFFFFFF)
31. }
32. }, (item: string) => item)
33. }
34. .onScrollIndex((first: number) => {
35. console.info(first.toString());
36. })
37. .width('100%')
38. .height('100%')
39. .alignListItem(ListItemAlign.Center)
40. .scrollBar(BarState.Off)
41. }
42. .onStateChange((refreshStatus: RefreshStatus) => {
43. console.info('Refresh onStateChange state is ' + refreshStatus);
44. })
45. .onOffsetChange((value: number) => {
46. console.info('Refresh onOffsetChange offset:' + value);
47. })
48. .onRefreshing(() => {
49. setTimeout(() => {
50. this.isRefreshing = false;
51. }, 2000)
52. console.info('onRefreshing test');
53. })
54. .backgroundColor(0x89CFF0)
55. .refreshOffset(64)
56. .pullToRefresh(true)
57. }
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/V40JKTKQTDa8-BmLumZ4Ew/zh-cn_image_0000002589245985.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=AC2796EBFEC9E985F1A741BD7C3509FB98A57F12E92F4CCA92AAC4E653643A10)

### 示例2（设置刷新区域显示文本）

通过[promptText](ts-container-refresh.md#refreshoptions对象说明)参数设置刷新区域显示文本。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RefreshExample {
5. @State isRefreshing: boolean = false;
6. @State promptText: string = "Refreshing...";
7. @State arr: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

9. build() {
10. Column() {
11. Refresh({ refreshing: $$this.isRefreshing, promptText: this.promptText }) {
12. List() {
13. ForEach(this.arr, (item: string) => {
14. ListItem() {
15. Text(item)
16. .width('70%')
17. .height(80)
18. .fontSize(16)
19. .margin(10)
20. .textAlign(TextAlign.Center)
21. .borderRadius(10)
22. .backgroundColor(0xFFFFFF)
23. }
24. }, (item: string) => item)
25. }
26. .onScrollIndex((first: number) => {
27. console.info(first.toString());
28. })
29. .width('100%')
30. .height('100%')
31. .alignListItem(ListItemAlign.Center)
32. .scrollBar(BarState.Off)
33. }
34. .backgroundColor(0x89CFF0)
35. .pullToRefresh(true)
36. .refreshOffset(96)
37. .onStateChange((refreshStatus: RefreshStatus) => {
38. console.info('Refresh onStateChange state is ' + refreshStatus);
39. })
40. .onOffsetChange((value: number) => {
41. console.info('Refresh onOffsetChange offset:' + value);
42. })
43. .onRefreshing(() => {
44. setTimeout(() => {
45. this.isRefreshing = false;
46. }, 2000)
47. console.info('onRefreshing test');
48. })
49. }
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/NktgzhOyRbSQi-oC8tVLdg/zh-cn_image_0000002558766176.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=7A2983E47AE46D340134D56E7B4BCF17D65E40A054F9036DA282D01BD8F81061)

### 示例3（自定义刷新区域显示内容-builder）

通过[builder](ts-container-refresh.md#refreshoptions对象说明)参数自定义刷新区域显示内容。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RefreshExample {
5. @State isRefreshing: boolean = false;
6. @State arr: String[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

8. @Builder
9. customRefreshComponent() {
10. Stack() {
11. Row() {
12. LoadingProgress().height(32)
13. Text("Refreshing...").fontSize(16).margin({ left: 20 })
14. }
15. .alignItems(VerticalAlign.Center)
16. }
17. .align(Alignment.Center)
18. .clip(true)
19. // 设置最小高度约束保证自定义组件高度随刷新区域高度变化时自定义组件高度不会低于minHeight。
20. .constraintSize({ minHeight: 32 })
21. .width('100%')
22. }

24. build() {
25. Column() {
26. Refresh({ refreshing: $$this.isRefreshing, builder: this.customRefreshComponent() }) {
27. List() {
28. ForEach(this.arr, (item: string) => {
29. ListItem() {
30. Text('' + item)
31. .width('70%')
32. .height(80)
33. .fontSize(16)
34. .margin(10)
35. .textAlign(TextAlign.Center)
36. .borderRadius(10)
37. .backgroundColor(0xFFFFFF)
38. }
39. }, (item: string) => item)
40. }
41. .onScrollIndex((first: number) => {
42. console.info(first.toString());
43. })
44. .width('100%')
45. .height('100%')
46. .alignListItem(ListItemAlign.Center)
47. .scrollBar(BarState.Off)
48. }
49. .backgroundColor(0x89CFF0)
50. .pullToRefresh(true)
51. .refreshOffset(64)
52. .onStateChange((refreshStatus: RefreshStatus) => {
53. console.info('Refresh onStateChange state is ' + refreshStatus);
54. })
55. .onRefreshing(() => {
56. setTimeout(() => {
57. this.isRefreshing = false;
58. }, 2000)
59. console.info('onRefreshing test');
60. })
61. }
62. }
63. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ObVGUJrsQeGC_3MWbwA-Sg/zh-cn_image_0000002558606518.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=9CCD1BF8885BC5011EA050535EB0C1F10B08A6AF0F98274D545F5AF6DC0D4909)

### 示例4（自定义刷新区域显示内容-refreshingContent）

通过[refreshingContent](ts-container-refresh.md#refreshoptions对象说明)参数自定义刷新区域显示内容。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';

4. class Params {
5. refreshStatus: RefreshStatus = RefreshStatus.Inactive;

7. constructor(refreshStatus: RefreshStatus) {
8. this.refreshStatus = refreshStatus;
9. }
10. }

12. @Builder
13. function customRefreshingContent(params: Params) {
14. Stack() {
15. Row() {
16. LoadingProgress().height(32)
17. Text("refreshStatus: " + params.refreshStatus).fontSize(16).margin({ left: 20 })
18. }
19. .alignItems(VerticalAlign.Center)
20. }
21. .align(Alignment.Center)
22. .clip(true)
23. // 设置最小高度约束保证自定义组件高度随刷新区域高度变化时自定义组件高度不会低于minHeight。
24. .constraintSize({ minHeight: 32 })
25. .width('100%')
26. }

28. @Entry
29. @Component
30. struct RefreshExample {
31. @State isRefreshing: boolean = false;
32. @State arr: String[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
33. @State refreshStatus: RefreshStatus = RefreshStatus.Inactive;
34. private contentNode?: ComponentContent<Object> = undefined;
35. private params: Params = new Params(RefreshStatus.Inactive);

37. aboutToAppear(): void {
38. let uiContext = this.getUIContext();
39. this.contentNode = new ComponentContent(uiContext, wrapBuilder(customRefreshingContent), this.params);
40. }

42. build() {
43. Column() {
44. Refresh({ refreshing: $$this.isRefreshing, refreshingContent: this.contentNode }) {
45. List() {
46. ForEach(this.arr, (item: string) => {
47. ListItem() {
48. Text('' + item)
49. .width('70%')
50. .height(80)
51. .fontSize(16)
52. .margin(10)
53. .textAlign(TextAlign.Center)
54. .borderRadius(10)
55. .backgroundColor(0xFFFFFF)
56. }
57. }, (item: string) => item)
58. }
59. .onScrollIndex((first: number) => {
60. console.info(first.toString());
61. })
62. .width('100%')
63. .height('100%')
64. .alignListItem(ListItemAlign.Center)
65. .scrollBar(BarState.Off)
66. }
67. .backgroundColor(0x89CFF0)
68. .pullToRefresh(true)
69. .refreshOffset(96)
70. .onStateChange((refreshStatus: RefreshStatus) => {
71. this.refreshStatus = refreshStatus;
72. this.params.refreshStatus = refreshStatus;
73. // 更新自定义组件内容。
74. this.contentNode?.update(this.params);
75. console.info('Refresh onStateChange state is ' + refreshStatus);
76. })
77. .onRefreshing(() => {
78. setTimeout(() => {
79. this.isRefreshing = false;
80. }, 2000)
81. console.info('onRefreshing test');
82. })
83. }
84. }
85. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/2WC7oZAISTKNpLMUjNr1Dg/zh-cn_image_0000002589326045.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=961E3F356ADA97C2792F3491FCB07782B9A36A16EDC08047884E63BEDB117C68)

### 示例5（实现最大下拉距离）

通过[pullDownRatio](ts-container-refresh.md#pulldownratio12)属性和[onOffsetChange](ts-container-refresh.md#onoffsetchange12)事件实现最大下拉距离。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';

4. @Builder
5. function customRefreshingContent() {
6. Stack() {
7. Row() {
8. LoadingProgress().height(32)
9. }
10. .alignItems(VerticalAlign.Center)
11. }
12. .align(Alignment.Center)
13. .clip(true)
14. // 设置最小高度约束保证自定义组件高度随刷新区域高度变化时自定义组件高度不会低于minHeight。
15. .constraintSize({ minHeight: 32 })
16. .width('100%')
17. }

19. @Entry
20. @Component
21. struct RefreshExample {
22. @State isRefreshing: boolean = false;
23. @State arr: String[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
24. @State maxRefreshingHeight: number = 100.0;
25. @State ratio: number = 1;
26. private contentNode?: ComponentContent<Object> = undefined;

28. aboutToAppear(): void {
29. let uiContext = this.getUIContext();
30. this.contentNode = new ComponentContent(uiContext, wrapBuilder(customRefreshingContent));
31. }

33. build() {
34. Column() {
35. Refresh({ refreshing: $$this.isRefreshing, refreshingContent: this.contentNode }) {
36. List() {
37. ForEach(this.arr, (item: string) => {
38. ListItem() {
39. Text('' + item)
40. .width('70%')
41. .height(80)
42. .fontSize(16)
43. .margin(10)
44. .textAlign(TextAlign.Center)
45. .borderRadius(10)
46. .backgroundColor(0xFFFFFF)
47. }
48. }, (item: string) => item)
49. }
50. .onScrollIndex((first: number) => {
51. console.info(first.toString());
52. })
53. .width('100%')
54. .height('100%')
55. .alignListItem(ListItemAlign.Center)
56. .scrollBar(BarState.Off)
57. }
58. .backgroundColor(0x89CFF0)
59. .pullDownRatio(this.ratio)
60. .pullToRefresh(true)
61. .refreshOffset(64)
62. .onOffsetChange((offset: number) => {
63. // 越接近最大距离，下拉跟手系数越小。
64. this.ratio = 1 - Math.pow((offset / this.maxRefreshingHeight), 3);
65. })
66. .onStateChange((refreshStatus: RefreshStatus) => {
67. console.info('Refresh onStateChange state is ' + refreshStatus);
68. })
69. .onRefreshing(() => {
70. setTimeout(() => {
71. this.isRefreshing = false;
72. }, 2000)
73. console.info('onRefreshing test');
74. })
75. }
76. }
77. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/5_l9z1BNTYaBHNDHTOguKw/zh-cn_image_0000002589245987.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=90B84C30C66850E5EC1A35D8FB1AD4D5CB1553867D0F508E0204FE3EF7EB52EC)

### 示例6（实现下拉刷新上拉加载更多）

Refresh组件与[List](ts-container-list.md)组件组合实现下拉刷新上拉加载更多效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListRefreshLoad {
5. @State arr: Array<number> = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
6. @State refreshing: boolean = false;
7. @State refreshOffset: number = 0;
8. @State refreshState: RefreshStatus = RefreshStatus.Inactive;
9. @State isLoading: boolean = false;

11. @Builder
12. refreshBuilder() {
13. Stack({ alignContent: Alignment.Bottom }) {
14. // 可以通过刷新状态控制是否存在Progress组件。
15. // 当刷新状态处于下拉中或刷新中状态时Progress组件才存在。
16. if (this.refreshState != RefreshStatus.Inactive && this.refreshState != RefreshStatus.Done) {
17. Progress({ value: this.refreshOffset, total: 64, type: ProgressType.Ring })
18. .width(32).height(32)
19. .style({ status: this.refreshing ? ProgressStatus.LOADING : ProgressStatus.PROGRESSING })
20. .margin(10)
21. }
22. }
23. .clip(true)
24. .height('100%')
25. .width('100%')
26. }

28. @Builder
29. footer() {
30. Row() {
31. LoadingProgress().height(32).width(48)
32. Text("加载中")
33. }.width('100%')
34. .height(64)
35. .justifyContent(FlexAlign.Center)
36. // 当不处于加载中状态时隐藏组件。
37. .visibility(this.isLoading ? Visibility.Visible : Visibility.Hidden)
38. }

40. build() {
41. Refresh({ refreshing: $$this.refreshing, builder: this.refreshBuilder() }) {
42. List() {
43. ForEach(this.arr, (item: number) => {
44. ListItem() {
45. Text('' + item)
46. .width('100%')
47. .height(80)
48. .fontSize(16)
49. .textAlign(TextAlign.Center)
50. .backgroundColor(0xFFFFFF)
51. }.borderWidth(1)
52. }, (item: string) => item)

54. ListItem() {
55. this.footer();
56. }
57. }
58. .onScrollIndex((start: number, end: number) => {
59. // 当达到列表末尾时，触发新数据加载。
60. if (end >= this.arr.length - 1) {
61. this.isLoading = true;
62. // 模拟新数据加载。
63. setTimeout(() => {
64. for (let i = 0; i < 10; i++) {
65. this.arr.push(this.arr.length);
66. }
67. this.isLoading = false;
68. }, 700)
69. }
70. })
71. .scrollBar(BarState.Off)
72. // 开启边缘滑动效果。
73. .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })
74. }
75. .width('100%')
76. .height('100%')
77. .backgroundColor(0xDCDCDC)
78. .onOffsetChange((offset: number) => {
79. this.refreshOffset = offset;
80. })
81. .onStateChange((state: RefreshStatus) => {
82. this.refreshState = state;
83. })
84. .onRefreshing(() => {
85. // 模拟数据刷新。
86. setTimeout(() => {
87. this.refreshing = false;
88. }, 2000)
89. })
90. }
91. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/ZQ14SXACQTC3QmRVmF_uNw/zh-cn_image_0000002558766178.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=719F77150E0C2E88B9DAC7E69E42AEB0D797FCA1917C944C0777BA97914BC056)

### 示例7（设置最大下拉距离）

从API version 20开始，通过[maxPullDownDistance](ts-container-refresh.md#maxpulldowndistance20)属性设置最大下拉距离。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RefreshExample {
5. @State isRefreshing: boolean = false
6. @State arr: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

8. build() {
9. Column() {
10. Refresh({ refreshing: $$this.isRefreshing }) {
11. List() {
12. ForEach(this.arr, (item: string) => {
13. ListItem() {
14. Text('' + item)
15. .width('70%')
16. .height(80)
17. .fontSize(16)
18. .margin(10)
19. .textAlign(TextAlign.Center)
20. .borderRadius(10)
21. .backgroundColor(0xFFFFFF)
22. }
23. }, (item: string) => item)
24. }
25. .onScrollIndex((first: number) => {
26. console.info(first.toString())
27. })
28. .width('100%')
29. .height('100%')
30. .alignListItem(ListItemAlign.Center)
31. .scrollBar(BarState.Off)
32. }
33. .maxPullDownDistance(150)
34. .onStateChange((refreshStatus: RefreshStatus) => {
35. console.info('Refresh onStateChange state is ' + refreshStatus)
36. })
37. .onOffsetChange((value: number) => {
38. console.info('Refresh onOffsetChange offset:' + value)
39. })
40. .onRefreshing(() => {
41. setTimeout(() => {
42. this.isRefreshing = false
43. }, 2000)
44. console.info('onRefreshing test')
45. })
46. .backgroundColor(0x89CFF0)
47. .refreshOffset(64)
48. .pullToRefresh(true)
49. }
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/HcB_7XUERKGhqlDmqCB2mw/zh-cn_image_0000002558606520.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=59E168F9C9478A9F264B5FE373C53B000000553655B3F0FBE3A54270538931B2)

### 示例8（禁止下拉刷新）

通过[pullDownRatio](ts-container-refresh.md#pulldownratio12)属性禁止下拉刷新。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RefreshExample {
5. @State isRefreshing: boolean = false;
6. @State ratio: number | undefined = undefined;
7. @State arr: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

9. build() {
10. Column() {
11. Row() {
12. Button('禁止下拉刷新').onClick(() => {
13. this.ratio = 0
14. })
15. Button('允许下拉刷新').onClick(() => {
16. this.ratio = undefined
17. })
18. }
19. Refresh({ refreshing: $$this.isRefreshing }) {
20. List() {
21. ForEach(this.arr, (item: string) => {
22. ListItem() {
23. Text('' + item)
24. .width('70%')
25. .height(80)
26. .fontSize(16)
27. .margin(10)
28. .textAlign(TextAlign.Center)
29. .borderRadius(10)
30. .backgroundColor(0xFFFFFF)
31. }
32. }, (item: string) => item)
33. }
34. .onScrollIndex((first: number) => {
35. console.info(first.toString());
36. })
37. .width('100%')
38. .height('100%')
39. .alignListItem(ListItemAlign.Center)
40. .scrollBar(BarState.Off)
41. }
42. .backgroundColor(0x89CFF0)
43. .refreshOffset(64)
44. .pullToRefresh(true)
45. .pullDownRatio(this.ratio)
46. .onStateChange((refreshStatus: RefreshStatus) => {
47. console.info('Refresh onStateChange state is ' + refreshStatus);
48. })
49. .onOffsetChange((value: number) => {
50. console.info('Refresh onOffsetChange offset:' + value);
51. })
52. .onRefreshing(() => {
53. setTimeout(() => {
54. this.isRefreshing = false;
55. }, 2000)
56. console.info('onRefreshing test');
57. })
58. }
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/cHSolAdETTyzpvN72SyXOg/zh-cn_image_0000002589326047.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=7DD01B893BA98F131B5E3002CD059455A44F7ABAB450E2F111302088AD0AB5E1)

### 示例9（不满一屏场景实现下拉刷新）

调用[edgeEffect](ts-container-scrollable-common.md#edgeeffect11)时，将options参数的[alwaysEnabled](ts-container-scrollable-common.md#edgeeffectoptions11对象说明)设置为true，可以在不满一屏的情况下实现Refresh组件的下拉刷新效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RefreshExample {
5. @State isRefreshing: boolean = false;
6. @State alwaysEnabled: boolean = false;

8. build() {
9. Column() {
10. Refresh({ refreshing: $$this.isRefreshing }) {
11. Column() {
12. List() {
13. ListItem() {
14. Text('alwaysEnabled:' + this.alwaysEnabled)
15. .width('70%')
16. .height(80)
17. .fontSize(16)
18. .margin(10)
19. .textAlign(TextAlign.Center)
20. .borderRadius(10)
21. .backgroundColor(0xFFFFFF)
22. .onClick(() => {
23. this.alwaysEnabled = !this.alwaysEnabled;
24. })
25. }
26. }
27. .width('100%')
28. .height('100%')
29. .alignListItem(ListItemAlign.Center)
30. .scrollBar(BarState.Auto)
31. // List组件内容大小小于组件自身且alwaysEnabled为false时，List不会响应手势，此时手势会被Column组件响应，不会产生下拉刷新效果
32. // alwaysEnabled设为true，List会响应手势并通过嵌套滚动带动Refresh组件产生下拉刷新效果
33. .edgeEffect(EdgeEffect.Spring, { alwaysEnabled: this.alwaysEnabled })
34. }
35. .gesture(
36. PanGesture({ direction: PanDirection.Vertical })
37. )
38. }
39. .onStateChange((refreshStatus: RefreshStatus) => {
40. console.info('Refresh onStateChange state is ' + refreshStatus);
41. })
42. .onOffsetChange((value: number) => {
43. console.info('Refresh onOffsetChange offset:' + value);
44. })
45. .onRefreshing(() => {
46. setTimeout(() => {
47. this.isRefreshing = false;
48. }, 2000)
49. })
50. .backgroundColor(0x89CFF0)
51. .refreshOffset(64)
52. .pullToRefresh(true)
53. }
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/imvjAKLGSpKrV0CG-7WV4g/zh-cn_image_0000002589245989.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=16C63758A9FD99886FF9F4ABFAFDD3C5D4588E0165C21637180406D51B378EE0)

### 示例10（上划不取消刷新）

该示例通过[pullUpToCancelRefresh](ts-container-refresh.md#pulluptocancelrefresh23)接口设置上划不取消刷新。

从API version 23开始，新增pullUpToCancelRefresh接口。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';

4. class Params {
5. refreshStatus: RefreshStatus = RefreshStatus.Inactive;

7. constructor(refreshStatus: RefreshStatus) {
8. this.refreshStatus = refreshStatus;
9. }
10. }

12. @Builder
13. function customRefreshingContent(params: Params) {
14. Stack() {
15. Row() {
16. LoadingProgress().height(32)
17. Text('refreshStatus: ' + params.refreshStatus).fontSize(16).margin({ left: 20 })
18. }
19. .alignItems(VerticalAlign.Center)
20. }
21. .align(Alignment.Center)
22. .clip(true)
23. .constraintSize({ minHeight: 32 })
24. .width('100%')
25. }

27. @Entry
28. @Component
29. struct RefreshExample {
30. @State isRefreshing: boolean = false;
31. @State arr: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']; // 改为原始类型string[]
32. @State refreshStatus: RefreshStatus = RefreshStatus.Inactive;
33. private contentNode?: ComponentContent<Object> = undefined;
34. private params: Params = new Params(RefreshStatus.Inactive);

36. aboutToAppear(): void {
37. let uiContext = this.getUIContext();
38. this.contentNode = new ComponentContent(uiContext, wrapBuilder(customRefreshingContent), this.params);
39. }

41. build() {
42. Column() {
43. Refresh({ refreshing: $$this.isRefreshing, refreshingContent: this.contentNode }) {
44. List() {
45. ForEach(this.arr, (item: string) => {
46. ListItem() {
47. Text('' + item)
48. .width('70%')
49. .height(80)
50. .fontSize(16)
51. .margin(10)
52. .textAlign(TextAlign.Center)
53. .borderRadius(10)
54. .backgroundColor(0xFFFFFF)
55. }
56. }, (item: string) => item)
57. }
58. .onScrollIndex((first: number) => {
59. console.info(first.toString());
60. })
61. .width('100%')
62. .height('100%')
63. .alignListItem(ListItemAlign.Center)
64. .scrollBar(BarState.Off)
65. }
66. .backgroundColor(0x89CFF0)
67. .pullToRefresh(true)
68. .pullUpToCancelRefresh(false)
69. .refreshOffset(96)
70. .onStateChange((refreshStatus: RefreshStatus) => {
71. this.refreshStatus = refreshStatus;
72. this.params.refreshStatus = refreshStatus;
73. this.contentNode?.update(this.params);
74. console.info('Refresh onStateChange state is ' + refreshStatus);
75. })
76. .onRefreshing(() => {
77. setTimeout(() => {
78. const newArr: string[] = [];
79. const lastNum = parseInt(this.arr[this.arr.length - 1]);
80. for (let i = 0; i < 11; i++) {
81. newArr.push((lastNum + 1 + i).toString());
82. }
83. this.arr = newArr;

85. this.isRefreshing = false;
86. }, 6000)
87. console.info('onRefreshing test');
88. })
89. }
90. }
91. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/561ob9xTSUmI6IjdM9Cokg/zh-cn_image_0000002558766180.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055146Z&HW-CC-Expire=86400&HW-CC-Sign=58019F0B8ECDD2BA51A67DC697185E480E56ED3EAFF187FF1AAC86C51DC63E42)
