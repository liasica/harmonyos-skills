---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-grid
title: 创建网格 (Grid/GridItem)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 列表与网格 > 创建网格 (Grid/GridItem)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:33+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:9dbca2f1a3deb3a6843aa28530a7383f87af1656a47247506a96028d2c9f4ed3
---

## 概述

网格布局是由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。网格布局具有较强的页面均分能力，子组件占比控制能力，是一种重要自适应布局，其使用场景有九宫格图片展示、日历、计算器等。

ArkUI提供了[Grid](../harmonyos-references/ts-container-grid.md)容器组件和子组件[GridItem](../harmonyos-references/ts-container-griditem.md)，用于构建网格布局。Grid用于设置网格布局相关参数，GridItem定义子组件相关特征。Grid组件支持使用[条件渲染](arkts-rendering-control-ifelse.md)、[循环渲染](arkts-rendering-control-foreach.md)、[懒加载](arkts-rendering-control-lazyforeach.md)等方式生成子组件。

说明

本文仅展示关键代码片段，可运行的完整代码请参考[创建网格代码](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid)。

## 布局与约束

Grid组件为网格容器，其中容器内各条目对应一个GridItem组件，如下图所示。

**图1** Grid与GridItem组件关系

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/quevuft0TE-HemIHBl8VUA/zh-cn_image_0000002552798134.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=02E609E10B7320F0BC4EB70CF8EED9EBB3EB63E6FB08582C4991453AFB628EAA)

说明

Grid的子组件必须是GridItem组件。

网格布局是一种二维布局。Grid组件支持自定义行列数和每行每列尺寸占比、设置子组件横跨几行或者几列，同时提供了垂直和水平布局能力。当网格容器组件尺寸发生变化时，所有子组件以及间距会等比例调整，从而实现网格布局的自适应能力。根据Grid的这些布局能力，可以构建出不同样式的网格布局，如下图所示。

**图2** 网格布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/rF-F0U_6REqVsqDT9i2auQ/zh-cn_image_0000002583437809.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=BFF827547377311D5A5844672D6C0D8B6540228920298D1EA0549B98C4AA3D38)

如果Grid组件设置了宽高属性，则其尺寸为设置值。如果没有设置宽高属性，Grid组件的尺寸默认适应其父组件的尺寸。

Grid组件根据行列数量与占比属性的设置，可以分为三种布局情况：

* 行、列数量与占比同时设置：Grid只展示固定行列数的元素，其余元素不展示，且Grid不可滚动。（推荐使用该种布局方式）
* 只设置行、列数量与占比中的一个：元素按照设置的方向进行排布，超出的元素可通过滚动的方式展示。
* 行列数量与占比都不设置：元素在布局方向上排布，其行列数由布局方向、单个网格的宽高等多个属性共同决定。超出行列容纳范围的元素不展示，且Grid不可滚动。

## 设置排列方式

### 设置行列数量与占比

通过设置行列数量与尺寸占比可以确定网格布局的整体排列方式。Grid组件提供了[rowsTemplate](../harmonyos-references/ts-container-grid.md#rowstemplate)和[columnsTemplate](../harmonyos-references/ts-container-grid.md#columnstemplate)属性用于设置网格布局行列数量与尺寸占比。

rowsTemplate和columnsTemplate属性值是一个由多个空格和'数字+fr'间隔拼接的字符串，fr的个数即网格布局的行或列数，fr前面的数值大小，用于计算该行或列在网格布局宽度上的占比，最终决定该行或列宽度。

**图3** 行列数量占比示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/s1CTmOHvSk2ljzi7EBOHuQ/zh-cn_image_0000002583437829.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=20109FA9738357DCB08306524C8AC53B29FC61EA32BA527E6A6CA4421BFE67C6)

如上图所示，构建的是一个三行三列的网格布局，其在垂直方向上分为三等份，每行占一份；在水平方向上分为四等份，第一列占一份，第二列占两份，第三列占一份。

只要将rowsTemplate设置为'1fr 1fr 1fr'，同时将columnsTemplate设置为'1fr 2fr 1fr'，即可实现上述网格布局。

```
1. Grid() {
2. // ···
3. }
4. .rowsTemplate('1fr 1fr 1fr')
5. .columnsTemplate('1fr 2fr 1fr')
```

[GridLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/GridLayout.ets#L40-L73)

说明

当Grid组件设置了rowsTemplate或columnsTemplate时，Grid的layoutDirection、maxCount、minCount、cellLength属性不生效，属性说明可参考[Grid-属性](../harmonyos-references/ts-container-grid.md#属性)。

### 设置子组件所占行列数

除了大小相同的等比例网格布局，由不同大小的网格组成不均匀分布的网格布局场景在实际应用中十分常见，如下图所示。在Grid组件中，可以通过创建Grid时传入合适的[GridLayoutOptions](../harmonyos-references/ts-container-grid.md#gridlayoutoptions10对象说明)实现如图所示的单个网格横跨多行或多列的场景，其中，irregularIndexes和onGetIrregularSizeByIndex可对仅设置rowsTemplate或columnsTemplate的Grid使用；onGetRectByIndex可对同时设置rowsTemplate和columnsTemplate的Grid使用。

**图4** 不均匀网格布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/XMA3PdmESqGAQoKT_tYwVA/zh-cn_image_0000002552957784.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=DC5D5797326E37BB3A51035CBCCE9792EE7421CE3B6C86ABD87365EF0460F26D)

例如计算器的按键布局就是常见的不均匀网格布局场景。如下图，计算器中的按键“0”和“=”，按键“0”横跨第一、二两列，按键“=”横跨第五、六两行。使用Grid构建的网格布局，其行列标号从0开始，依次编号。

**图5** 计算器

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/xZhjEK9vStmsyqYNG_bA-Q/zh-cn_image_0000002583477785.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=A78FE31CF2829260DF8F622E6A69FB099128617A12211B4FCA8BC5DE0273BAF6)

在网格中，可以通过onGetRectByIndex返回的[rowStart,columnStart,rowSpan,columnSpan]来实现跨行跨列布局，其中rowStart和columnStart属性表示指定当前元素起始行号和起始列号，rowSpan和columnSpan属性表示指定当前元素的占用行数和占用列数。

所以“0”按键横跨第一列和第二列，“=”按键横跨第五行和第六行，只要将“0”对应onGetRectByIndex的rowStart和columnStart设为6和0，rowSpan和columnSpan设为1和2，将“=”对应onGetRectByIndex的rowStart和columnStart设为5和3，rowSpan和columnSpan设为2和1即可。

```
1. layoutOptions: GridLayoutOptions = {
2. regularSize: [1, 1],
3. onGetRectByIndex: (index: number) => {
4. // ···
5. if (index == key1) { // key1是“0”按键对应的index
6. return [6, 0, 1, 2];
7. } else if (index == key2) { // key2是“=”按键对应的index
8. return [5, 3, 2, 1];
9. }
10. // ···
11. // 这里需要根据具体布局返回其他item的位置
12. }
13. }
14. // ···
15. Grid(undefined, this.layoutOptions) {
16. // ···
17. }
18. .columnsTemplate('1fr 1fr 1fr 1fr')
19. .rowsTemplate('1fr 1fr 1fr 1fr 1fr 1fr 1fr')
```

[GridCalculator.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/GridCalculator.ets#L24-L107)

### 设置主轴方向

使用Grid构建网格布局时，若没有设置行列数量与占比，可以通过[layoutDirection](../harmonyos-references/ts-container-grid.md#layoutdirection8)设置网格布局的主轴方向，决定子组件的排列方式。此时可以结合[minCount](../harmonyos-references/ts-container-grid.md#mincount8)和[maxCount](../harmonyos-references/ts-container-grid.md#maxcount8)属性来约束主轴方向上的网格数量。

**图6** 主轴方向示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/GrMKrVa6QO6CKOd7PgkNMw/zh-cn_image_0000002552798136.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=29D4827D89DBAE52E9B24A2A37C709198812F73852D0A704B6F0B2E94CB168B6)

当前layoutDirection设置为Row时，先从左到右排列，排满一行再排下一行。当前layoutDirection设置为Column时，先从上到下排列，排满一列再排下一列，如上图所示。此时，将maxCount属性设为3，表示主轴方向上最大显示的网格单元数量为3。

```
1. Grid() {
2. // ···
3. }
4. .maxCount(3)
5. .layoutDirection(GridDirection.Row)
```

[GridLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/GridLayout.ets#L101-L143)

说明

* layoutDirection属性仅在不设置rowsTemplate和columnsTemplate时生效，此时元素在layoutDirection方向上排列。
* 仅设置rowsTemplate时，Grid主轴为水平方向，交叉轴为垂直方向。
* 仅设置columnsTemplate时，Grid主轴为垂直方向，交叉轴为水平方向。

## 在网格布局中显示数据

网格布局采用二维布局的方式组织其内部元素，如下图所示。

**图7** 通用办公服务

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/vunOEZwtSXKFa0CgxGR-Iw/zh-cn_image_0000002583437831.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=A0F1E8F12D9DBC0FDC67292C0F40AC79B662F209C17E0F28B2816A80E728C0F7)

Grid组件可以通过二维布局的方式显示一组GridItem子组件。

```
1. Grid() {
2. GridItem() {
3. // app.string.Meeting资源文件中的value值为‘会议’
4. Text($r('app.string.Meeting'))
5. // ...
6. }

8. GridItem() {
9. // app.string.Check_in资源文件中的value值为‘签到’
10. Text($r('app.string.Check_in'))
11. // ...
12. }

14. GridItem() {
15. // app.string.Voting资源文件中的value值为‘投票’
16. Text($r('app.string.Voting'))
17. // ...
18. }

20. GridItem() {
21. // app.string.Printing资源文件中的value值为‘打印’
22. Text($r('app.string.Printing'))
23. // ...
24. }
25. }
26. // ...
27. .rowsTemplate('1fr 1fr')
28. .columnsTemplate('1fr 1fr')
```

[DataInGrid.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/DataInGrid.ets#L58-L101)

对于内容结构相似的多个GridItem，通常更推荐使用ForEach语句中嵌套GridItem的形式，来减少重复代码。

```
1. @Entry
2. @Component
3. export struct DataInGrid {
4. // ...

6. @State services: Array<string> = [
7. // app.string.Meeting资源文件中的value值为‘会议’
8. this.context!.resourceManager.getStringSync($r('app.string.Meeting').id),
9. // app.string.Check_in资源文件中的value值为‘签到’
10. this.context!.resourceManager.getStringSync($r('app.string.Check_in').id),
11. // app.string.Voting资源文件中的value值为‘投票’
12. this.context!.resourceManager.getStringSync($r('app.string.Voting').id),
13. // app.string.Printing资源文件中的value值为‘打印’
14. this.context!.resourceManager.getStringSync($r('app.string.Printing').id)
15. ];
16. // ...

18. build() {
19. // ...
20. Column() {
21. // ...
22. Grid() {
23. ForEach(this.services, (service: string) => {
24. GridItem() {
25. Text(service)
26. }
27. // ...
28. }, (service: string): string => service)
29. }
30. .rowsTemplate(('1fr 1fr') as string)
31. .columnsTemplate(('1fr 1fr') as string)
32. // ...
33. }
34. // ...
35. }
36. }
```

[DataInGrid.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/DataInGrid.ets#L18-L138)

## 设置行列间距

在两个网格单元之间的网格横向间距称为行间距，网格纵向间距称为列间距，如下图所示。

**图8** 网格的行列间距

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/qqi7rAg1QfO5cf3Zu0B3PQ/zh-cn_image_0000002552957786.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=7FA02253D60BF8E78CFD4D5BE3C3EA8337B45862D1D27048833A966FBA902BAC)

通过Grid的[rowsGap](../harmonyos-references/ts-container-grid.md#rowsgap)和[columnsGap](../harmonyos-references/ts-container-grid.md#columnsgap)可以设置网格布局的行列间距。在图5所示的计算器中，行间距为15vp，列间距为10vp。

```
1. Grid() {
2. // ···
3. }
4. .columnsGap(10)
5. .rowsGap(15)
```

[GridColumnsGap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/GridColumnsGap.ets#L39-L72)

## 构建可滚动的网格布局

可滚动的网格布局常用在文件管理、购物或视频列表等页面中，如下图所示。在设置Grid的行列数量与占比时，如果仅设置行、列数量与占比中的一个，即仅设置rowsTemplate或仅设置columnsTemplate属性，网格单元按照设置的方向排列，超出Grid显示区域后，Grid拥有可滚动能力。

**图9** 横向可滚动网格布局

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/1QKpBBjdSbm-n1fOFWWDFA/zh-cn_image_0000002583477787.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=D41072B1C4B601ABD1431E5C7669981E38376572CBF6565729527DBE7172862B)

如果设置的是columnsTemplate，Grid的滚动方向为垂直方向；如果设置的是rowsTemplate，Grid的滚动方向为水平方向。

如上图所示的横向可滚动网格布局，只要设置rowsTemplate属性的值且不设置columnsTemplate属性，当内容超出Grid组件宽度时，Grid可横向滚动进行内容展示。

```
1. @Entry
2. @Component
3. export struct ScrollableGrid {
4. // ...
5. @State services: Array<string> = [
6. // 请将$r('app.string.Live_Streaming')替换为实际资源文件，在本示例中该资源文件的value值为"直播"
7. this.context!.resourceManager.getStringSync($r('app.string.Live_Streaming').id),
8. // 请将$r('app.string.Imported')替换为实际资源文件，在本示例中该资源文件的value值为"进口"
9. this.context!.resourceManager.getStringSync($r('app.string.Imported').id)
10. ];
11. // ...
12. build() {
13. // ...

15. Column({ space: 5 }) {
16. // ...

18. Grid() {
19. ForEach(this.services, (service: string, index: number) => {
20. GridItem() {
21. // ...
22. }
23. .width('25%')
24. // ...
25. }, (service: string): string => service)
26. }
27. .rowsTemplate('1fr 1fr') // 只设置rowsTemplate属性，当内容超出Grid区域时，可水平滚动。
28. .rowsGap(15)

30. // ...
31. }
32. }
33. // ...
34. }
```

[ScrollableGrid.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/ScrollableGrid.ets#L18-L99)

## 控制滚动位置

与新闻列表的返回顶部场景类似，控制滚动位置功能在网格布局中也很常用，例如下图所示日历的翻页功能。

**图10** 日历翻页

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/sXcz2LXqRxS5IusqzPihuQ/zh-cn_image_0000002552798138.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=87F9F18A919C4B5971F03036598F175660E454FEE8B37F0E07ACAFC6A44B5A24)

Grid组件初始化时，可以绑定一个[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)对象，用于进行滚动控制，例如通过Scroller对象的[scrollPage](../harmonyos-references/ts-container-scroll.md#scrollpage9)方法进行翻页。

```
1. private scroller: Scroller = new Scroller();
```

[ScrollPositionGrid.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/ScrollPositionGrid.ets#L23-L25)

在日历页面中，用户在点击“下一页”按钮时，应用响应点击事件，通过指定scrollPage方法的参数next为true，滚动到下一页。

```
1. Column({ space: 5 }){
2. Grid(this.scroller) {
3. // ...
4. }
5. .columnsTemplate('1fr 1fr 1fr 1fr 1fr 1fr 1fr')
6. // ...
7. Row({ space: 20 }) {
8. // 请将$r('app.string.Previous_Page')替换为实际资源文件，在本示例中该资源文件的value值为"上一页"
9. Button($r('app.string.Previous_Page'))
10. .onClick(() => {
11. this.scroller.scrollPage({
12. next: false
13. });
14. })
15. // 请将$r('app.string.Next_page')替换为实际资源文件，在本示例中该资源文件的value值为"下一页"
16. Button($r('app.string.Next_page'))
17. .onClick(() => {
18. this.scroller.scrollPage({
19. next: true
20. });
21. })
22. }
23. }
```

[GridSideToSide.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/GridSideToSide.ets#L46-L87)

## 添加外置滚动条

网格组件[Grid](../harmonyos-references/ts-container-grid.md)可与[ScrollBar](../harmonyos-references/ts-basic-components-scrollbar.md)组件配合使用，为网格添加外置滚动条。两者通过绑定同一个[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)滚动控制器对象实现联动。

1. 首先，需要创建一个[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)类型的对象gridScroller。

   ```
   1. private gridScroller: Scroller = new Scroller();
   ```

   [GridScrollbar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/GridScrollbar.ets#L23-L25)
2. 然后，通过[scroller](../harmonyos-references/ts-container-grid.md#接口)参数绑定滚动控制器。

   ```
   1. // gridScroller初始化Grid组件的scroller参数，绑定gridScroller与网格。
   2. Grid( this.gridScroller) {
   3. // ···
   4. }
   ```

   [GridScrollbar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/GridScrollbar.ets#L44-L60)
3. 最后，滚动条通过[scroller](../harmonyos-references/ts-basic-components-scrollbar.md#scrollbaroptions对象说明)参数绑定滚动控制器。

   ```
   1. // gridScroller初始化ScrollBar组件的scroller参数，绑定gridScroller与滚动条。
   2. ScrollBar({ scroller: this.gridScroller })
   ```

   [GridScrollbar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/GridScrollbar.ets#L76-L79)

**图11** 网格的外置滚动条

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/R6HR5vNcS4yPi6pqN8jeCQ/zh-cn_image_0000002583437833.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=92D273A2D7C490F8DF00D7005E628E08D67E3ED464B6B96504DC52A93912CCC2)

说明

* 滚动条组件[ScrollBar](../harmonyos-references/ts-basic-components-scrollbar.md)，还可配合其他可滚动组件使用，如[ArcList](../harmonyos-references/ts-container-arclist.md)、[List](../harmonyos-references/ts-container-list.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)。
* 在圆形屏幕设备上，[Grid](../harmonyos-references/ts-container-grid.md)可以与弧形滚动条组件[ArcScrollBar](../harmonyos-references/ts-basic-components-arcscrollbar.md)配合使用为网格添加弧形外置滚动条，使用方式可参考[创建弧形列表 (ArcList)](arkts-layout-development-create-arclist.md)的[添加外置滚动条ArcScrollBar](arkts-layout-development-create-arclist.md#添加外置滚动条arcscrollbar)章节。

## 性能优化

与[长列表的处理](arkts-layout-development-create-list.md#长列表的处理)类似，[循环渲染](arkts-rendering-control-foreach.md)适用于数据量较小的布局场景，当构建具有大量网格项的可滚动网格布局时，推荐使用[数据懒加载](arkts-rendering-control-lazyforeach.md)方式实现按需迭代加载数据，从而提升网格性能。

关于按需加载优化的具体实现可参考[数据懒加载](arkts-rendering-control-lazyforeach.md)章节中的示例。

当使用懒加载方式渲染网格时，为了更好的滚动体验，减少滑动时出现白块，Grid组件中也可通过[cachedCount](../harmonyos-references/ts-container-grid.md#cachedcount)属性设置GridItem的预加载数量，只在懒加载[LazyForEach](arkts-rendering-control-lazyforeach.md)中生效。

设置预加载数量后，会在Grid显示区域前后各缓存cachedCount\*列数个GridItem，超出显示和缓存范围的GridItem会被释放。

```
1. Grid() {
2. LazyForEach(this.dataSource, () => {
3. GridItem() {
4. }
5. })
6. }
7. .cachedCount(3)
```

[LongGrid.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/grid/LongGrid.ets#L41-L49)

说明

cachedCount的增加会增大UI的CPU、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。

## 示例代码

* [基于Grid的嵌套混合布局](https://gitcode.com/HarmonyOS_Samples/grid-hybrid)
