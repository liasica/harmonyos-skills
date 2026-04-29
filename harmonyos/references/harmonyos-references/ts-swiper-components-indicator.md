---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-swiper-components-indicator
title: Indicator
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 导航与切换 > Indicator
category: harmonyos-references
scraped_at: 2026-04-29T13:51:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:034811cd568471d05f1ada409dd91a5564e204112ba8a6dcd9ae149bd6cfa215
---

导航点组件，提供圆点导航点以及数字导航点两种导航点样式。

将原[Swiper](ts-container-swiper.md)组件中的[indicator](ts-container-swiper.md#indicator)已有的能力作为一个单独组件提供给开发者使用。开发者可以不依赖Swiper组件单独显示导航点，也可以通过IndicatorComponentController与Swiper组件绑定使用。

当多个导航点组件和同一个Swiper绑定时，只有最后一个导航点组件能成功和Swiper绑定。

当一个导航点组件和多个Swiper绑定时，只有最后一个Swiper能成功和导航点组件绑定。

说明

该组件从API version 15开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

不包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

### IndicatorComponent

PhonePC/2in1TabletTVWearable

IndicatorComponent(controller?: IndicatorComponentController)

单独导航点组件的构造函数，可配置该组件的控制器。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| controller | [IndicatorComponentController](ts-swiper-components-indicator.md#indicatorcomponentcontroller) | 否 | 设置控制器，可通过该参数控制单独导航点进行导航点之间的跳转。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性。

### style

PhonePC/2in1TabletTVWearable

style(indicatorStyle: DotIndicator | DigitIndicator)

设置可选导航点指示器样式。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| indicatorStyle | [DotIndicator](ts-container-swiper.md#dotindicator10) | [DigitIndicator](ts-container-swiper.md#digitindicator10) | 是 | 可选导航点指示器样式。  - DotIndicator：圆点指示器样式。  - DigitIndicator：数字指示器样式。  默认类型：DotIndicator。 |

说明

当indicatorStyle类型为DotIndicator且未与Swiper组件绑定时，[maxDisplayCount](ts-container-swiper.md#maxdisplaycount12)不生效。

### count

PhonePC/2in1TabletTVWearable

count(totalCount: number)

设置导航点总数量。

单独导航点组件和Swiper绑定的时候，以Swiper的页面数量为准。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| totalCount | number | 是 | 导航点总数量。  默认值：2。 |

### initialIndex

PhonePC/2in1TabletTVWearable

initialIndex(index: number)

设置首次显示时当前导航点的索引值。设置小于0或大于等于导航点数量时，按照默认值0处理。

单独导航点组件和Swiper绑定的时候，该属性不生效。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 首次显示时当前导航点的索引值。  默认值：0。 |

### loop

PhonePC/2in1TabletTVWearable

loop(isLoop: boolean)

设置是否开启循环。

单独导航点组件和Swiper绑定的时候，该属性不生效。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isLoop | boolean | 是 | 是否开启循环。true为开启循环，false为不开启循环。  默认值：true。 |

### vertical

PhonePC/2in1TabletTVWearable

vertical(isVertical: boolean)

设置是否为纵向滑动。

单独导航点组件和Swiper绑定的时候，该属性不生效。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isVertical | boolean | 是 | 是否为纵向滑动。true为纵向滑动，false为横向滑动。  默认值：false |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onChange

PhonePC/2in1TabletTVWearable

onChange(event: Callback<number>)

当前显示的选中导航点索引变化时触发该事件，可通过回调函数获取当前选中导航点的索引值。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [Callback](ts-types.md#callback12)<number> | 是 | 当前显示元素的索引变化时触发的回调。 |

## IndicatorComponentController

PhonePC/2in1TabletTVWearable

Indicator组件的控制器，可以将此对象绑定至Indicator组件来控制翻页。

### constructor

PhonePC/2in1TabletTVWearable

constructor()

IndicatorComponentController的构造函数。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### showNext

PhonePC/2in1TabletTVWearable

showNext(): void

跳转到下一导航点。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### showPrevious

PhonePC/2in1TabletTVWearable

showPrevious(): void

跳转到上一导航点。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### changeIndex

PhonePC/2in1TabletTVWearable

changeIndex(index: number, useAnimation?: boolean): void

翻至指定导航点。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 指定导航点在Swiper中的索引值。  **说明：**  设置的值小于0或大于最大导航点索引时，取0。 |
| useAnimation | boolean | 否 | 设置翻至指定导航点时是否有动效，true表示有动效，false表示没有动效。  默认值：false。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（圆点单独导航点与Swiper绑定使用）

该示例通过[Swiper](ts-container-swiper.md)组件的[indicator](ts-container-swiper.md#indicator)接口与[IndicatorComponent](ts-swiper-components-indicator.md#indicatorcomponent)的构造函数绑定同一[IndicatorComponentController](ts-swiper-components-indicator.md#indicatorcomponentcontroller)对象，实现了圆点单独导航点与Swiper的交互。

```
1. @Entry
2. @Component
3. struct DotIndicatorDemo {
4. private indicatorController: IndicatorComponentController = new IndicatorComponentController();
5. private swiperController: SwiperController = new SwiperController();
6. @State list: number[] = [];
7. aboutToAppear(): void {
8. for (let i = 1; i <= 6; i++) {
9. this.list.push(i);
10. }
11. }

13. build() {
14. Column() {
15. Swiper(this.swiperController) {
16. ForEach(this.list, (item: string) => {
17. Text(item.toString())
18. .width('100%')
19. .height(160)
20. .backgroundColor(0xAFEEEE)
21. .textAlign(TextAlign.Center)
22. .fontSize(30)
23. }, (item: string) => item)
24. }
25. .cachedCount(2)
26. .index(0)
27. .autoPlay(true)
28. .interval(2000)
29. .indicator(this.indicatorController)
30. .loop(true)
31. .duration(1000)
32. .itemSpace(0)
33. .curve(Curve.Linear)
34. .onChange((index: number) => {
35. console.info(index.toString());
36. })

38. IndicatorComponent(this.indicatorController)
39. .initialIndex(0)
40. .style(
41. new DotIndicator()
42. .itemWidth(15)
43. .itemHeight(15)
44. .selectedItemWidth(15)
45. .selectedItemHeight(15)
46. .color(Color.Gray)
47. .selectedColor(Color.Blue))
48. .loop(true)
49. .count(6)
50. .vertical(true)
51. .onChange((index: number) => {
52. console.info("current index: " + index );
53. })
54. }
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/HECigvXkQe2Lcoq4zEVGWQ/zh-cn_image_0000002558606524.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055149Z&HW-CC-Expire=86400&HW-CC-Sign=7A825B6619B8643C9DB6505688FC7E7F2C667987870DB5B6CED7A1D03C3115D4)

### 示例2（数字单独导航点与Swiper绑定使用）

该示例通过[Swiper](ts-container-swiper.md)组件的[indicator](ts-container-swiper.md#indicator)接口与[IndicatorComponent](ts-swiper-components-indicator.md#indicatorcomponent)的构造函数绑定同一[IndicatorComponentController](ts-swiper-components-indicator.md#indicatorcomponentcontroller)对象，实现了数字单独导航点与Swiper的交互。

```
1. @Entry
2. @Component
3. struct DigitIndicatorDemo {
4. private indicatorController: IndicatorComponentController = new IndicatorComponentController();
5. private swiperController: SwiperController = new SwiperController();
6. @State list: number[] = [];
7. aboutToAppear(): void {
8. for (let i = 1; i <= 6; i++) {
9. this.list.push(i);
10. }
11. }

13. build() {
14. Column() {
15. Swiper(this.swiperController) {
16. ForEach(this.list, (item: string) => {
17. Text(item.toString())
18. .width('100%')
19. .height(160)
20. .backgroundColor(0xAFEEEE)
21. .textAlign(TextAlign.Center)
22. .fontSize(30)
23. }, (item: string) => item)
24. }
25. .cachedCount(2)
26. .index(0)
27. .autoPlay(true)
28. .interval(2000)
29. .indicator(this.indicatorController)
30. .loop(true)
31. .duration(1000)
32. .itemSpace(0)
33. .curve(Curve.Linear)
34. .onChange((index: number) => {
35. console.info(index.toString());
36. })

38. IndicatorComponent(this.indicatorController)
39. .initialIndex(0)
40. .style(Indicator.digit()
41. .fontColor(Color.Gray)
42. .selectedFontColor(Color.Gray)
43. .digitFont({ size: 20, weight: FontWeight.Bold })
44. .selectedDigitFont({ size: 20, weight: FontWeight.Normal }))
45. .loop(true)
46. .count(6)
47. .vertical(true)
48. .onChange((index: number) => {
49. console.info("current index: " + index );
50. })
51. }
52. }
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/D7JcPSFSRZGq1Mg_YfBKMQ/zh-cn_image_0000002589326051.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055149Z&HW-CC-Expire=86400&HW-CC-Sign=08D4836CC1BC4593E78234DFA0F3F6EAB02150DC9FBFB75EEF40C4F16327E9F6)
