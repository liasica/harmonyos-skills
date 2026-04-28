---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup
title: ListItemGroup
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > ListItemGroup
category: harmonyos-references
scraped_at: 2026-04-28T08:01:29+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a78d6f01a0ee01886ecfafc5f1600333210b57d16301ead18ff8440592581c78
---

该组件用来展示列表item分组，宽度默认充满[List](ts-container-list.md)组件，必须配合List组件来使用。

ListItemGroup的懒加载是指组件按需加载可见区域可见的子组件。相比全量加载，使用懒加载可以提升应用启动速度，减少内存消耗。ListItemGroup和[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)、[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)结合，懒加载能力存在差异：

* 当ListItemGroup和ForEach结合，会一次性创建所有的子节点，在需要的时候布局和渲染屏幕范围内的节点。当用户滑动时，划出屏幕范围的节点不会下树销毁，划入屏幕范围的节点会布局和渲染。
* 当ListItemGroup和LazyForEach结合，会一次性创建、布局、渲染屏幕范围的节点。当用户滑动时，划出屏幕范围的节点会下树销毁，划入屏幕范围的节点会创建、布局、渲染。
* 当ListItemGroup和带[virtualScroll](ts-rendering-control-repeat.md#virtualscroll)的Repeat结合，它的懒加载行为和LazyForEach一致。当ListItemGroup和不带virtualScroll的Repeat结合，它的懒加载行为和ForEach一致。

ListItemGroup的预加载是指除了加载显示区域内可见的子组件外，还支持空闲时隙提前加载部分显示区域外不可见的子组件。使用预加载可以减少滚动丢帧，提升流畅性。预加载需要结合懒加载才会生效。ListItemGroup和[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)、[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)结合，预加载能力存在差异：

* 当ListItemGroup和ForEach结合，如果设置了[cachedCount](ts-container-list.md#cachedcount)，除了会布局显示区域内子组件外，还会在空闲时隙根据List组件的cachedCount属性预布局显示区域外cachedCount范围内的子节点。
* 当ListItemGroup和LazyForEach结合，如果设置了[cachedCount](ts-container-list.md#cachedcount)，除了会创建和布局显示区域内子组件外，还会在空闲时隙根据List组件的cachedCount属性预创建和预布局显示区域外cachedCount范围内的子节点。
* 当ListItemGroup和带[virtualScroll](ts-rendering-control-repeat.md#virtualscroll)的Repeat结合，它的预加载行为和LazyForEach一致。当ListItemGroup和不带virtualScroll的Repeat结合，它的预加载行为和ForEach一致。

说明

* 该组件从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件的父组件只能是[List](ts-container-list.md)。
* ListItemGroup组件不支持设置[通用属性aspectRatio](ts-universal-attributes-layout-constraints.md#aspectratio)。
* 当ListItemGroup的父组件List的[listDirection](ts-container-list.md#listdirection)属性为Axis.Vertical时，设置[通用属性height](ts-universal-attributes-size.md#height)属性不生效。ListItemGroup的高度为header高度、footer高度和所有ListItem布局后总高度之和。
* 当父组件List的listDirection属性为Axis.Horizontal时，设置[通用属性width](ts-universal-attributes-size.md#width)属性不生效。ListItemGroup的宽度为header宽度、footer宽度和所有ListItem布局后总宽度之和。
* 当前ListItemGroup内部的ListItem组件不支持编辑、拖拽功能，即ListItem组件的[editable](ts-container-listitem.md#editabledeprecated)属性不生效。
* ListItemGroup使用direction属性设置布局方向不生效，ListItemGroup组件布局方向跟随父容器List组件的布局方向。

## 子组件

PhonePC/2in1TabletTVWearable

包含[ListItem](ts-container-listitem.md)子组件。支持通过渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)和[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)）动态生成子组件，更推荐使用LazyForEach或Repeat以优化性能。

## 接口

PhonePC/2in1TabletTVWearable

ListItemGroup(options?: ListItemGroupOptions)

创建ListItemGroup组件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ListItemGroupOptions](ts-container-listitemgroup.md#listitemgroupoptions对象说明) | 否 | 列表item分组组件参数。 |

## ListItemGroupOptions对象说明

PhonePC/2in1TabletTVWearable

ListItemGroup组件参数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| header | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 设置ListItemGroup头部组件。  **说明：**  可以放单个子组件或不放子组件。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| headerComponent13+ | [ComponentContent](js-apis-arkui-componentcontent.md) | 否 | 是 | 使用ComponentContent类型参数设置ListItemGroup头部组件。  **说明：**  可以放单个子组件或不放子组件。 该参数的优先级高于参数header。即同时设置header和headerComponent时，以headerComponent设置的值为准。  同一个headerComponent不推荐同时给不同的ListItemGroup使用，否则会导致显示问题。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| footer | [CustomBuilder](ts-types.md#custombuilder8) | 否 | 是 | 设置ListItemGroup尾部组件。  **说明：**  可以放单个子组件或不放子组件。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| footerComponent13+ | [ComponentContent](js-apis-arkui-componentcontent.md) | 否 | 是 | 使用ComponentContent类型参数设置ListItemGroup尾部组件。  **说明：**  可以放单个子组件或不放子组件。该参数的优先级高于参数footer。 即同时设置footer和footerComponent时，以footerComponent设置的值为准。  同一个footerComponent不推荐同时给不同的ListItemGroup使用，否则会导致显示问题。  **元服务API：** 从API version 13开始，该接口支持在元服务中使用。 |
| space | number | string | 否 | 是 | 列表项间距。只作用于ListItem与ListItem之间，不作用于header与ListItem、footer与ListItem之间。  默认值：0  单位：vp  **说明：**  设置为负数或者大于等于List内容区长度时，按默认值显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| style10+ | [ListItemGroupStyle](ts-container-listitemgroup.md#listitemgroupstyle10枚举说明) | 否 | 是 | 设置List组件卡片样式。  默认值：ListItemGroupStyle.NONE  设置为ListItemGroupStyle.NONE时无样式。  设置为ListItemGroupStyle.CARD时，建议配合[ListItem](ts-container-listitem.md)的ListItemStyle.CARD同时使用，显示默认卡片样式。  卡片样式下，ListItemGroup默认规格：左右外边距12vp，上下左右内边距4vp。  卡片样式下，为卡片内的列表选项提供了默认的focused、hover、pressed、selected和disabled样式。  **说明：**  当设置为ListItemStyle.CARD时，List的listDirection属性值须为Axis.Vertical，如果设置为Axis.Horizontal，会导致显示混乱；List属性[alignListItem](ts-container-list.md#alignlistitem9)默认为ListItemAlign.Center，居中对齐显示。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

### divider

PhonePC/2in1TabletTVWearable

divider(value: [ListDividerOptions](ts-container-list.md#listdivideroptions18对象说明) | null)

设置ListItem分割线样式，默认无分割线。

strokeWidth，startMargin和endMargin不支持设置百分比。

ListItem设置[多态样式](ts-universal-attributes-polymorphic-style.md)时，被按压的子组件上下的分割线不绘制。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ListDividerOptions](ts-container-list.md#listdivideroptions18对象说明) | null | 是 | ListItem分割线样式。  默认值：null |

### childrenMainSize12+

PhonePC/2in1TabletTVWearable

childrenMainSize(value: ChildrenMainSize)

设置ListItemGroup组件的子组件在主轴方向的大小信息。

说明

* 必须同时给所在的List组件设置childrenMainSize属性才可以正常生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ChildrenMainSize](ts-container-scrollable-common.md#childrenmainsize12对象说明) | 是 | 该对象用来维护子组件在主轴方向的大小信息。 |

## ListItemGroupStyle10+枚举说明

PhonePC/2in1TabletTVWearable

ListItemGroup组件卡片样式枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 无样式。 |
| CARD | 1 | 显示默认卡片样式。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置吸顶/吸底）

该示例通过[sticky](ts-container-list.md#sticky9)实现了Header吸顶和Footer吸底的效果。

ListDataSource实现了LazyForEach数据源接口[IDataSource](ts-rendering-control-lazyforeach.md#idatasource)，用于通过LazyForEach给List和ListItemGroup提供子组件。

```
1. // ListDataSource.ets
2. export class TimeTableDataSource implements IDataSource {
3. private list: TimeTable[] = [];
4. private listeners: DataChangeListener[] = [];

6. constructor(list: TimeTable[]) {
7. this.list = list;
8. }

10. totalCount(): number {
11. return this.list.length;
12. }

14. getData(index: number): TimeTable {
15. return this.list[index];
16. }

18. registerDataChangeListener(listener: DataChangeListener): void {
19. if (this.listeners.indexOf(listener) < 0) {
20. this.listeners.push(listener);
21. }
22. }

24. unregisterDataChangeListener(listener: DataChangeListener): void {
25. const pos = this.listeners.indexOf(listener);
26. if (pos >= 0) {
27. this.listeners.splice(pos, 1);
28. }
29. }

31. // 通知控制器数据变化
32. notifyDataChange(index: number): void {
33. this.listeners.forEach(listener => {
34. listener.onDataChange(index);
35. });
36. }

38. // 修改第一个元素
39. public change1stItem(temp: TimeTable): void {
40. this.list[0] = temp;
41. this.notifyDataChange(0);
42. }
43. }

45. export class ProjectsDataSource implements IDataSource {
46. private list: string[] = [];

48. constructor(list: string[]) {
49. this.list = list;
50. }

52. totalCount(): number {
53. return this.list.length;
54. }

56. getData(index: number): string {
57. return this.list[index];
58. }

60. registerDataChangeListener(listener: DataChangeListener): void {
61. }

63. unregisterDataChangeListener(listener: DataChangeListener): void {
64. }
65. }

67. export interface TimeTable {
68. title: string;
69. projects: string[];
70. }
```

```
1. // xxx.ets
2. import { TimeTable, ProjectsDataSource, TimeTableDataSource } from './ListDataSource';
3. @Entry
4. @Component
5. struct ListItemGroupExample {
6. itemGroupArray: TimeTableDataSource = new TimeTableDataSource([]);

8. aboutToAppear(): void {
9. let timeTable: TimeTable[] = [
10. {
11. title: '星期一',
12. projects: ['语文', '数学', '英语']
13. },
14. {
15. title: '星期二',
16. projects: ['物理', '化学', '生物']
17. },
18. {
19. title: '星期三',
20. projects: ['历史', '地理', '政治']
21. },
22. {
23. title: '星期四',
24. projects: ['美术', '音乐', '体育']
25. }
26. ];
27. this.itemGroupArray = new TimeTableDataSource(timeTable);
28. }

30. @Builder
31. itemHead(text: string) {
32. Text(text)
33. .fontSize(20)
34. .backgroundColor(0xAABBCC)
35. .width('100%')
36. .padding(10)
37. }

39. @Builder
40. itemFoot(num: number) {
41. Text('共' + num + '节课')
42. .fontSize(16)
43. .backgroundColor(0xAABBCC)
44. .width('100%')
45. .padding(5)
46. }

48. build() {
49. Column() {
50. List({ space: 20 }) {
51. LazyForEach(this.itemGroupArray, (item: TimeTable) => {
52. ListItemGroup({ header: this.itemHead(item.title), footer: this.itemFoot(item.projects.length) }) {
53. LazyForEach(new ProjectsDataSource(item.projects), (project: string) => {
54. ListItem() {
55. Text(project)
56. .width('100%')
57. .height(100)
58. .fontSize(20)
59. .textAlign(TextAlign.Center)
60. .backgroundColor(0xFFFFFF)
61. }
62. }, (item: string) => item)
63. }
64. .divider({ strokeWidth: 1, color: Color.Blue }) // 每行之间的分界线
65. })
66. }
67. .width('90%')
68. .sticky(StickyStyle.Header | StickyStyle.Footer)
69. .scrollBar(BarState.Off)
70. }.width('100%').height('100%').backgroundColor(0xDCDCDC).padding({ top: 5 })
71. }
72. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/YNOHr-MVRGuzYl-EtARIsA/zh-cn_image_0000002583479617.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000127Z&HW-CC-Expire=86400&HW-CC-Sign=FCF000699730B1043F695638C09051287A5FBFAFBC157FC5B01BDE5F394D4FB2)

### 示例2（设置卡片样式）

该示例展示了ListItemGroup的卡片样式效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ListItemGroupExample2 {
5. private arr: ArrObject[] = [
6. {
7. style: ListItemGroupStyle.CARD,
8. itemStyles: [ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.CARD]
9. },
10. {
11. style: ListItemGroupStyle.CARD,
12. itemStyles: [ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.NONE]
13. },
14. {
15. style: ListItemGroupStyle.CARD,
16. itemStyles: [ListItemStyle.CARD, ListItemStyle.NONE, ListItemStyle.CARD]
17. },
18. {
19. style: ListItemGroupStyle.NONE,
20. itemStyles: [ListItemStyle.CARD, ListItemStyle.CARD, ListItemStyle.NONE]
21. }
22. ];

24. build() {
25. Column() {
26. List({ space: '4vp', initialIndex: 0 }) {
27. ForEach(this.arr, (item: ArrObject, index?: number) => {
28. ListItemGroup({ style: item.style }) {
29. ForEach(item.itemStyles, (itemStyle: number, itemIndex?: number) => {
30. ListItem({ style: itemStyle }) {
31. if (index != undefined && itemIndex != undefined) {
32. Text('第' + (index + 1) + '个Group中第' + (itemIndex + 1) + '个item')
33. .width('100%')
34. .textAlign(TextAlign.Center)
35. }
36. }
37. }, (item: string) => item)
38. }
39. })
40. }
41. .width('100%')
42. .multiSelectable(true)
43. .backgroundColor(0xDCDCDC)
44. }
45. .width('100%')
46. .padding({ top: 5 })
47. }
48. }

50. interface ArrObject {
51. style: number;
52. itemStyles: number[];
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/MiQKcdmyRr-xkgKV4o0jbg/zh-cn_image_0000002552799968.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000127Z&HW-CC-Expire=86400&HW-CC-Sign=1C7775733AD214E7FE38FD0100B5AAC8FF14C480D51B6EEA6D89EC21DACBD54B)

### 示例3（设置Header/Footer）

该示例通过[ComponentContent](js-apis-arkui-componentcontent.md#componentcontent-1)设置Header/Footer。

ListDataSource说明及完整代码参考[示例1设置吸顶/吸底](ts-container-listitemgroup.md#示例1设置吸顶吸底)。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';
3. import { TimeTable, ProjectsDataSource, TimeTableDataSource } from './ListDataSource';

5. class HeadBuilderParams {
6. text: string | Resource;
7. constructor(text: string | Resource) {
8. this.text = text;
9. }
10. }

12. class FootBuilderParams {
13. num: number | Resource;
14. constructor(num: number | Resource) {
15. this.num = num;
16. }
17. }

19. @Builder
20. function itemHead(params: HeadBuilderParams) {
21. Text(params.text)
22. .fontSize(20)
23. .height('48vp')
24. .width('100%')
25. .padding(10)
26. .backgroundColor($r('sys.color.background_tertiary'))
27. }

29. @Builder
30. function itemFoot(params: FootBuilderParams) {
31. Text('共' + params.num.toString() + '节课')
32. .fontSize(20)
33. .height('48vp')
34. .width('100%')
35. .padding(10)
36. .backgroundColor($r('sys.color.background_tertiary'))
37. }

39. @Component
40. struct MyItemGroup {
41. item: TimeTable = { title: '', projects: [] };
42. header?: ComponentContent<HeadBuilderParams> = undefined;
43. footer?: ComponentContent<FootBuilderParams> = undefined;
44. headerParam = new HeadBuilderParams(this.item.title);
45. footerParam = new FootBuilderParams(this.item.projects.length);
46. itemArr: ProjectsDataSource = new ProjectsDataSource([]);

48. aboutToAppear(): void {
49. this.header = new ComponentContent(this.getUIContext(), wrapBuilder(itemHead), this.headerParam);
50. this.footer = new ComponentContent(this.getUIContext(), wrapBuilder(itemFoot), this.footerParam);
51. this.itemArr = new ProjectsDataSource(this.item.projects);
52. }
53. GetHeader() {
54. this.header?.update(new HeadBuilderParams(this.item.title));
55. return this.header;
56. }

58. GetFooter() {
59. this.footer?.update(new FootBuilderParams(this.item.projects.length));
60. return this.footer;
61. }

63. build() {
64. ListItemGroup({
65. headerComponent: this.GetHeader(),
66. footerComponent: this.GetFooter()
67. }) {
68. LazyForEach(this.itemArr, (project: string) => {
69. ListItem() {
70. Text(project)
71. .width('100%')
72. .height(100)
73. .fontSize(20)
74. .textAlign(TextAlign.Center)
75. }
76. }, (item: string) => item)
77. }
78. .divider({ strokeWidth: 1, color: Color.Blue }) // 每行之间的分界线
79. }
80. }

82. @Entry
83. @Component
84. struct ListItemGroupExample {
85. itemGroupArray: TimeTableDataSource = new TimeTableDataSource([]);
86. aboutToAppear(): void {
87. let timeTable: TimeTable[] = [
88. {
89. title: '星期一',
90. projects: ['语文', '数学', '英语']
91. },
92. {
93. title: '星期二',
94. projects: ['物理', '化学', '生物']
95. },
96. {
97. title: '星期三',
98. projects: ['历史', '地理', '政治', '体育']
99. },
100. {
101. title: '星期四',
102. projects: ['美术', '音乐']
103. }
104. ];
105. this.itemGroupArray = new TimeTableDataSource(timeTable);
106. }

108. build() {
109. Column() {
110. Button('update').width(100).height(50).onClick(() => {
111. this.itemGroupArray.change1stItem({
112. title: '更新后的星期一',
113. projects: ['语文', '物理', '历史', '美术']
114. });
115. })
116. List({ space: 20 }) {
117. LazyForEach(this.itemGroupArray, (item: TimeTable) => {
118. MyItemGroup({ item: item })
119. }, (item: TimeTable) => item.title) // LazyForEach依赖键值判断是否刷新子组件
120. }
121. .layoutWeight(1)
122. .sticky(StickyStyle.Header | StickyStyle.Footer)
123. .scrollBar(BarState.Off)
124. }
125. .backgroundColor($r('sys.color.background_primary'))
126. }
127. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/8SLDmWv8TCa6edPwT-ZHoA/zh-cn_image_0000002583439663.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000127Z&HW-CC-Expire=86400&HW-CC-Sign=3128F8F273D0AC149D6D1C73865FAE4A07EEBCB3150CD9161BAF0ACCA62E3BA0)

### 示例4（设置多列布局）

该示例展示了ListItemGroup在多列布局中的使用，通过设置List组件的[lanes](ts-container-list.md#lanes9)属性实现多列布局。

ListDataSource说明及完整代码参考[示例1设置吸顶/吸底](ts-container-listitemgroup.md#示例1设置吸顶吸底)。

```
1. // xxx.ets
2. import { ComponentContent } from '@kit.ArkUI';
3. import { TimeTable, ProjectsDataSource, TimeTableDataSource } from './ListDataSource';

5. class HeadBuilderParams {
6. text: string | Resource;

8. constructor(text: string | Resource) {
9. this.text = text;
10. }
11. }

13. class FootBuilderParams {
14. num: number | Resource;

16. constructor(num: number | Resource) {
17. this.num = num;
18. }
19. }

21. @Builder
22. function itemHead(params: HeadBuilderParams) {
23. Text(params.text)
24. .fontSize(20)
25. .height('48vp')
26. .width('100%')
27. .padding(10)
28. .backgroundColor($r('sys.color.background_tertiary'))
29. }

31. @Builder
32. function itemFoot(params: FootBuilderParams) {
33. Text('共' + params.num.toString() + '节课')
34. .fontSize(20)
35. .height('48vp')
36. .width('100%')
37. .padding(10)
38. .backgroundColor($r('sys.color.background_tertiary'))
39. }

41. @Component
42. struct MyItemGroup {
43. item: TimeTable = { title: '', projects: [] };
44. header?: ComponentContent<HeadBuilderParams> = undefined;
45. footer?: ComponentContent<FootBuilderParams> = undefined;
46. headerParam = new HeadBuilderParams(this.item.title);
47. footerParam = new FootBuilderParams(this.item.projects.length);
48. itemArr: ProjectsDataSource = new ProjectsDataSource([]);

50. aboutToAppear(): void {
51. this.header = new ComponentContent(this.getUIContext(), wrapBuilder(itemHead), this.headerParam);
52. this.footer = new ComponentContent(this.getUIContext(), wrapBuilder(itemFoot), this.footerParam);
53. this.itemArr = new ProjectsDataSource(this.item.projects);
54. }

56. GetHeader() {
57. this.header?.update(new HeadBuilderParams(this.item.title));
58. return this.header;
59. }

61. GetFooter() {
62. this.footer?.update(new FootBuilderParams(this.item.projects.length));
63. return this.footer;
64. }

66. build() {
67. ListItemGroup({
68. headerComponent: this.GetHeader(),
69. footerComponent: this.GetFooter()
70. }) {
71. LazyForEach(this.itemArr, (project: string) => {
72. ListItem() {
73. // 修改ListItem样式以适应多列布局
74. Column() {
75. Text(project)
76. .fontSize(20)
77. .textAlign(TextAlign.Center)
78. }
79. .width('100%')
80. .height(80)
81. .padding(8)
82. .justifyContent(FlexAlign.Center)
83. .backgroundColor($r('sys.color.background_secondary'))
84. .borderRadius(12)
85. .shadow({
86. radius: 4,
87. color: '#20000000',
88. offsetX: 0,
89. offsetY: 2
90. })
91. }
92. }, (item: string) => item)
93. }
94. .divider({
95. strokeWidth: 2,
96. color: $r('sys.color.background_tertiary'),
97. startMargin: 20,
98. endMargin: 20
99. })
100. }
101. }

103. @Entry
104. @Component
105. struct ListItemGroupExample {
106. itemGroupArray: TimeTableDataSource = new TimeTableDataSource([]);

108. aboutToAppear(): void {
109. let timeTable: TimeTable[] = [
110. {
111. title: '星期一',
112. projects: ['语文', '数学', '英语', '物理', '化学', '生物']
113. },
114. {
115. title: '星期二',
116. projects: ['历史', '地理', '政治', '体育', '美术', '音乐']
117. },
118. {
119. title: '星期三',
120. projects: ['计算机', '编程', '算法', '数据结构', '网络']
121. },
122. {
123. title: '星期四',
124. projects: ['文学', '写作', '阅读', '书法']
125. },
126. {
127. title: '星期五',
128. projects: ['实验', '生活', '奥数', '高数', '中医']
129. }
130. ];
131. this.itemGroupArray = new TimeTableDataSource(timeTable);
132. }

134. build() {
135. Column() {
136. List({ space: 15 }) {
137. LazyForEach(this.itemGroupArray, (item: TimeTable) => {
138. MyItemGroup({ item: item })
139. }, (item: TimeTable) => item.title)
140. }
141. .lanes(3) // 设置3列布局
142. .alignListItem(ListItemAlign.Center) // 交叉轴居中对齐
143. .layoutWeight(1)
144. .scrollBar(BarState.Auto)
145. .width('100%')
146. .margin(10)
147. }
148. .backgroundColor($r('sys.color.background_primary'))
149. .width('100%')
150. .height('100%')
151. .padding(10)
152. }
153. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/YX5pWP3GRzuNsnY0Dzu1Pw/zh-cn_image_0000002552959618.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000127Z&HW-CC-Expire=86400&HW-CC-Sign=A11CD031DFF7B26EC05096716A381C8B16D37D446CCC2BADCEFEFB9E2C67873B)
