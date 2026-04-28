---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicetabs
title: AtomicServiceTabs
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > AtomicService > AtomicServiceTabs
category: harmonyos-references
scraped_at: 2026-04-28T08:02:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2f592708b240ebcd31bca9978d9956c6c02fdfaaf819265971d634158fbc816d
---

AtomicServiceTabs高级组件，对Tabs组件一些不需提供给用户自定义设计的属性进行简化，限制最多显示5个页签，固定页签样式，位置和大小。

说明

该组件从API Version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AtomicServiceTabs, TabBarOptions, TabBarPosition, OnContentWillChangeCallback } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)

## AtomicServiceTabs

PhonePC/2in1TabletTVWearable

```
1. AtomicServiceTabs({
2. tabContents?: [ TabContentBuilder?,
3. TabContentBuilder?,
4. TabContentBuilder?,
5. TabContentBuilder?,
6. TabContentBuilder?
7. ],
8. tabBarOptionsArray: [ TabBarOptions,
9. TabBarOptions,
10. TabBarOptions?,
11. TabBarOptions?,
12. TabBarOptions?
13. ],
14. tabBarPosition?: TabBarPosition,
15. layoutMode?: LayoutMode,
16. barBackgroundColor?: ResourceColor,
17. index?: number,
18. barOverlap?: boolean,
19. controller?: TabsController,
20. onChange?: Callback<number>,
21. onTabBarClick?: Callback<number>,
22. onContentWillChange?: OnContentWillChangeCallback,
23. })
```

**装饰器类型：**@Component

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| tabContents | [[TabContentBuilder?](ohos-atomicservice-atomicservicetabs.md#tabcontentbuilder),[TabContentBuilder?](ohos-atomicservice-atomicservicetabs.md#tabcontentbuilder), [TabContentBuilder?](ohos-atomicservice-atomicservicetabs.md#tabcontentbuilder),[TabContentBuilder?](ohos-atomicservice-atomicservicetabs.md#tabcontentbuilder), [TabContentBuilder?](ohos-atomicservice-atomicservicetabs.md#tabcontentbuilder)] | 否 | @BuilderParam | 内容视图容器数组，默认值为空，无内容展示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| tabBarOptionsArray | [[TabBarOptions](ohos-atomicservice-atomicservicetabs.md#tabbaroptions),[TabBarOptions](ohos-atomicservice-atomicservicetabs.md#tabbaroptions), [TabBarOptions?](ohos-atomicservice-atomicservicetabs.md#tabbaroptions),[TabBarOptions?](ohos-atomicservice-atomicservicetabs.md#tabbaroptions), [TabBarOptions?](ohos-atomicservice-atomicservicetabs.md#tabbaroptions)] | 是 | @Prop | 页签容器数组。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| tabBarPosition | [TabBarPosition](ohos-atomicservice-atomicservicetabs.md#tabbarposition) | 否 | @Prop | 设置页签栏位置，默认值为TabBarPosition.Bottom。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| layoutMode18+ | [LayoutMode](ts-container-tabcontent.md#layoutmode10) | 否 | @Prop | 设置底部页签的图片、文字排布的方式，默认值为LayoutMode.VERTICAL。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| barBackgroundColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | @Prop | 设置TabBar的背景颜色，默认值为透明。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| index | number | 否 | @Prop | 设置当前显示页签的索引，索引值从0开始。默认值为0。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| barOverlap | boolean | 否 | @Prop | 设置TabBar是否背景变模糊并叠加在TabContent之上。true表示TabBar背景变模糊并叠加在TabContent之上。默认值：true。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| controller | [TabsController](ts-container-tabs.md#tabscontroller) | 否 | - | Tabs组件的控制器，用于控制Tabs组件进行页签切换。默认值为new TabsController()。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onChange | Callback<number> | 否 | - | Tabs页签切换后触发的事件。默认值为空。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onTabBarClick | Callback<number> | 否 | - | Tabs页签点击后触发的事件。默认值为空。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| onContentWillChange | [OnContentWillChangeCallback](ohos-atomicservice-atomicservicetabs.md#oncontentwillchangecallback) | 否 | - | Tabs页面切换拦截事件能力，新页面即将显示时触发该回调。默认值为空。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## TabContentBuilder

PhonePC/2in1TabletTVWearable

type TabContentBuilder = () => void

内容视图容器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## TabBarOptions

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor(icon: ResourceStr | TabBarSymbol, text: ResourceStr, unselectedColor?: ResourceColor, selectedColor?: ResourceColor)

TabBarOptions的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | [TabBarSymbol](ts-container-tabcontent.md#tabbarsymbol12对象说明) | 是 | 页签内的图片内容。 |
| text | [ResourceStr](ts-types.md#resourcestr) | 是 | 页签内的文字内容。 |
| unselectedColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 未选择时的页签颜色，默认值：#99182431。 |
| selectedColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 被选择时的页签颜色，默认值：#FF007DFF。 |

## TabBarPosition

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 设置TabBar位于屏幕左侧 |
| BOTTOM | 1 | 设置TabBar位于屏幕底部 |

## OnContentWillChangeCallback

PhonePC/2in1TabletTVWearable

type OnContentWillChangeCallback = (currentIndex: number, comingIndex: number) => boolean

页面内容发生变化时触发的回调函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| currentIndex | number | 是 | 当前页签索引。 |
| comingIndex | number | 是 | 即将切换的页签索引。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 回调函数正常执行则返回true，反之返回false。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1(纯文本样式)

```
1. // Index.ets
2. import { AtomicServiceTabs, TabBarOptions, TabBarPosition, OnContentWillChangeCallback } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = '首页';
8. @State onClickNumber: number = 0;
9. @State currentIndex: number = 0;
10. @State comingIndex: number = 0;
11. onContentWillChangeCallBack:  OnContentWillChangeCallback = (currentIndex: number, comingIndex: number): boolean => {
12. this.currentIndex = currentIndex;
13. this.comingIndex = comingIndex;
14. console.info('OnContentWillChangeCallback')
15. return true;
16. }
17. onTabClick: Callback<number> = (index:number)=>{
18. this.onClickNumber ++;
19. console.info('onTabClick');
20. }
21. @Builder
22. tabContent1() {
23. Column().width('100%').height('100%').alignItems(HorizontalAlign.Center).backgroundColor('#00CB87')
24. }

26. @Builder
27. tabContent2() {
28. Column().width('100%').height('100%').backgroundColor('#007DFF')
29. }

31. @Builder
32. tabContent3() {
33. Column().width('100%').height('100%').backgroundColor('#FFBF00')
34. }

36. build() {
37. Stack() {
38. AtomicServiceTabs({
39. tabContents: [
40. () => {
41. this.tabContent1()
42. },
43. () => {
44. this.tabContent2()
45. },
46. () => {
47. this.tabContent3()
48. }
49. ],
50. tabBarOptionsArray: [
51. new TabBarOptions('', '绿色', Color.Black, Color.Green),
52. new TabBarOptions('', '蓝色', Color.Black, Color.Blue),
53. new TabBarOptions('', '黄色', Color.Black, Color.Yellow),
54. ],
55. tabBarPosition: TabBarPosition.BOTTOM,
56. barBackgroundColor: $r('sys.color.ohos_id_color_bottom_tab_bg'),
57. onTabBarClick:this.onTabClick,
58. onContentWillChange: this.onContentWillChangeCallBack,
59. })
60. Column() {
61. Text("onchange回调次数:" + this.onClickNumber)
62. Text("comingIndex = " + this.comingIndex + ", currentIndex = " + this.currentIndex)
63. }.margin({top:500})
64. }.height('100%')
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/u_9z6z1uTxeu4pVrUNzoDQ/zh-cn_image_0000002552960086.png?HW-CC-KV=V1&HW-CC-Date=20260428T000226Z&HW-CC-Expire=86400&HW-CC-Sign=3A067C797BA753A294F4271F306FDE99ABCB31C1C92C869BF119E68DC1159201)

### 示例2(纯图标样式)

```
1. // Index.ets
2. import { AtomicServiceTabs, TabBarOptions, TabBarPosition, OnContentWillChangeCallback } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = '首页';
8. @State onClickNumber: number = 0;
9. @State currentIndex: number = 0;
10. @State comingIndex: number = 0;
11. onContentWillChangeCallBack: OnContentWillChangeCallback = (currentIndex: number, comingIndex: number): boolean => {
12. this.currentIndex = currentIndex;
13. this.comingIndex = comingIndex;
14. console.info('OnContentWillChangeCallback');
15. return true;
16. }
17. onTabClick: Callback<number> = (index:number)=>{
18. this.onClickNumber ++;
19. console.info('onTabClick');
20. }
21. @Builder
22. tabContent1() {
23. Column().width('100%').height('100%').alignItems(HorizontalAlign.Center).backgroundColor('#00CB87')
24. }

26. @Builder
27. tabContent2() {
28. Column().width('100%').height('100%').backgroundColor('#007DFF')
29. }

31. @Builder
32. tabContent3() {
33. Column().width('100%').height('100%').backgroundColor('#FFBF00')
34. }

36. build() {
37. Stack() {
38. AtomicServiceTabs({
39. tabContents: [
40. () => {
41. this.tabContent1()
42. },
43. () => {
44. this.tabContent2()
45. },
46. () => {
47. this.tabContent3()
48. }
49. ],
50. tabBarOptionsArray: [
51. new TabBarOptions($r('sys.media.ohos_ic_public_phone'), '', Color.Black, Color.Blue),
52. new TabBarOptions($r('sys.media.ohos_ic_public_location'), '', Color.Black, Color.Blue),
53. new TabBarOptions($r('sys.media.ohos_ic_public_more'), '', Color.Black, Color.Blue),
54. ],
55. tabBarPosition: TabBarPosition.BOTTOM,
56. barBackgroundColor: $r('sys.color.ohos_id_color_bottom_tab_bg'),
57. onTabBarClick:this.onTabClick,
58. onContentWillChange: this.onContentWillChangeCallBack,
59. })
60. Column() {
61. Text("onchange回调次数:" + this.onClickNumber)
62. Text("comingIndex = " + this.comingIndex + ", currentIndex = " + this.currentIndex)
63. }.margin({top:500})
64. }.height('100%')
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/OFpNglNJRMmFTEZZN_qz6A/zh-cn_image_0000002583480087.png?HW-CC-KV=V1&HW-CC-Date=20260428T000226Z&HW-CC-Expire=86400&HW-CC-Sign=721CA4EE0B36380EF32D7027D5D0D7B35A5A66A273C5B36CEFCDD50E37EFA17D)

### 示例3(图标加文本，自定义图文排布)

```
1. // Index.ets
2. import { AtomicServiceTabs, TabBarOptions, TabBarPosition, OnContentWillChangeCallback } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct AtomicserviceTabs  {
7. @State flag: boolean = false;
8. @State message: string = '首页';
9. @State onClickNumber: number = 0;
10. @State currentIndex: number = 0;
11. @State comingIndex: number = 0;
12. @State layoutMode: LayoutMode = LayoutMode.VERTICAL;
13. onContentWillChangeCallBack: OnContentWillChangeCallback = (currentIndex: number, comingIndex: number): boolean => {
14. this.currentIndex = currentIndex;
15. this.comingIndex = comingIndex;
16. console.info('OnContentWillChangeCallback');
17. return true;
18. }
19. onTabClick: Callback<number> = (index: number) => {
20. this.onClickNumber++;
21. console.info('onTabClick');
22. }
23. onChange: Callback<number, void> = (Index: number) => {
24. console.info('onChange');
25. console.info('onChange2');
26. }

28. @Builder
29. tabContent1() {
30. Column().width('100%').height('100%').alignItems(HorizontalAlign.Center).backgroundColor('#00CB87')
31. }

33. @Builder
34. tabContent2() {
35. Column().width('100%').height('100%').backgroundColor(Color.Blue)
36. }

38. @Builder
39. tabContent3() {
40. Column().width('100%').height('100%').backgroundColor('#FFBF00')
41. }

43. build() {
44. Stack() {
45. AtomicServiceTabs({
46. tabContents: [
47. () => {
48. this.tabContent1()
49. },
50. () => {
51. this.tabContent2()
52. },
53. () => {
54. this.tabContent3()
55. },
56. ],
57. tabBarOptionsArray: [
58. new TabBarOptions($r('sys.media.ohos_ic_public_phone'), '绿色', Color.Black, Color.Blue),
59. new TabBarOptions($r('sys.media.ohos_ic_public_location'), '蓝色', Color.Black, Color.Blue),
60. new TabBarOptions($r('sys.media.ohos_ic_public_more'), '黄色', Color.Black, Color.Blue),
61. ],
62. tabBarPosition: TabBarPosition.BOTTOM,
63. barBackgroundColor: $r('sys.color.ohos_id_color_bottom_tab_bg'),
64. onTabBarClick: this.onTabClick,
65. onContentWillChange: this.onContentWillChangeCallBack,
66. onChange: this.onChange,
67. layoutMode: this.layoutMode,
68. })

70. Column() {
71. Button("layoutMode垂直 ")
72. .width('30%')
73. .height(50)
74. .margin({ top: 5 })
75. .onClick((event?: ClickEvent) => {
76. this.layoutMode = LayoutMode.VERTICAL;
77. })
78. Button("layoutMode水平 ")
79. .width('30%')
80. .height(50)
81. .margin({ top: 5 })
82. .onClick((event?: ClickEvent) => {
83. this.layoutMode = LayoutMode.HORIZONTAL;
84. })
85. }.margin({ top: 10 })
86. }.height('100%')
87. }
88. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/YjYrQgpwTaup0HMboCYXRQ/zh-cn_image_0000002552800438.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000226Z&HW-CC-Expire=86400&HW-CC-Sign=8CA348BC1B83B865700B0D6F8C03E08FD513AC2F806D66138707D1665F5A220B)
