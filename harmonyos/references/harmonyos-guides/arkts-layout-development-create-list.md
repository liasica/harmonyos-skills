---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list
title: 创建列表 (List)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 列表与网格 > 创建列表 (List)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1615504c8baab3d9942f6cf6bbfc518837475b11acede013bfdbb8313025d701
---

## 概述

列表是一种复杂的容器，当列表项达到一定数量，内容超过屏幕大小时，可以自动提供滚动功能。它适合用于呈现同类数据类型或数据类型集，例如图片和文本。在列表中显示数据集合是许多应用程序中的常见要求（如通讯录、音乐列表、购物清单等）。

使用列表可以轻松高效地显示结构化、可滚动的信息。通过在[List](../harmonyos-references/ts-container-list.md)组件中按垂直或者水平方向线性排列子组件[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)或[ListItem](../harmonyos-references/ts-container-listitem.md)，为列表中的行或列提供单个视图，或使用[循环渲染](arkts-rendering-control-foreach.md)迭代一组行或列，或混合任意数量的单个视图和ForEach结构，构建一个列表。List组件支持使用[条件渲染](arkts-rendering-control-ifelse.md)、循环渲染、[懒加载](arkts-rendering-control-lazyforeach.md)等[渲染控制](arkts-rendering-control-overview.md)方式生成子组件。

在圆形屏幕设备上，推荐使用[ArcList](../harmonyos-references/ts-container-arclist.md)组件，使用方式可参考[创建弧形列表 (ArcList)](arkts-layout-development-create-arclist.md)。

## 布局与约束

列表作为一种容器，会自动按其滚动方向排列子组件，向列表中添加组件或从列表中移除组件会重新排列子组件。

如下图所示，在垂直列表中，List按垂直方向自动排列ListItemGroup或ListItem。

ListItemGroup用于列表数据的分组展示，其子组件也是ListItem。ListItem表示单个列表项，可以包含单个子组件。

**图1** List、ListItemGroup和ListItem组件关系

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/EdoM9GQMQAiPC0yButjXiw/zh-cn_image_0000002552798116.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=68D52500EC48D83C560C69716180C289997C0566014D675BD8209B69842FF1D0)

说明

List的子组件必须是ListItemGroup或ListItem，ListItem和ListItemGroup必须配合List来使用。

### 布局

List除了提供垂直和水平布局能力、超出屏幕时可以滚动的自适应延伸能力之外，还提供了自适应交叉轴方向上排列个数的布局能力。

利用垂直布局能力可以构建单列或者多列垂直滚动列表，如下图所示。

**图2** 垂直滚动列表（左：单列；右：多列）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/nBsK_0_mStKnX7sQ5fbBYg/zh-cn_image_0000002552798114.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=056D4AD6A75FA5B1AD41771DDB954323E726DDB84ACEF9140F7ED54AF0B08525)

利用水平布局能力可以构建单行或多行水平滚动列表，如下图所示。

**图3** 水平滚动列表（左：单行；右：多行）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/BU7svtOFQKSuzN6ax9413A/zh-cn_image_0000002583437811.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=9C8B1172D486B34075E655BA091E3360FA88FD1A2D3002A535220250AF4E08DF)

Grid和WaterFlow也可以实现单列、多列布局，如果布局每列等宽，且不需要跨行跨列布局，相比Grid和WaterFlow，则更推荐使用List。

### 约束

列表的主轴方向是指子组件列的排列方向，也是列表的滚动方向。垂直于主轴的轴称为交叉轴，其方向与主轴方向相互垂直。

如下图所示，垂直列表的主轴是垂直方向，交叉轴是水平方向；水平列表的主轴是水平方向，交叉轴是垂直方向。

**图4** 列表的主轴与交叉轴

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/f7-dcIteT2yR5GPbwA31xQ/zh-cn_image_0000002552957766.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=2807B270BE1887E9BAD1C36187BD8642EE6C1D8094E1C5EE3A077D21FBC806C3)

如果List组件主轴或交叉轴方向设置了尺寸，则其对应方向上的尺寸为设置值。

如果List组件主轴方向没有设置尺寸，当List子组件主轴方向总尺寸小于List的父组件尺寸时，List主轴方向尺寸自动适应子组件的总尺寸。

如下图所示，一个垂直列表B没有设置高度时，其父组件A高度为200vp，若其所有子组件C的高度总和为150vp，则此时列表B的高度为150vp。

**图5** 列表主轴高度约束示例1（**A**: List的父组件; **B**: List组件; **C**: List的所有子组件）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/whCFO7vLQn6WejadnJEygw/zh-cn_image_0000002583477767.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=7E98C6E6EAF3F95E630E625B875B39F29E5EE9008DD30557B9618586D8C6E09F)

如果子组件主轴方向总尺寸超过List父组件尺寸时，List主轴方向尺寸适应List的父组件尺寸。

如下图所示，同样是没有设置高度的垂直列表B，其父组件A高度为200vp，若其所有子组件C的高度总和为300vp，则此时列表B的高度为200vp。

**图6** 列表主轴高度约束示例2（**A**: List的父组件; **B**: List组件; **C**: List的所有子组件）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/espZCW_bQ0Seiq6EYyeiTA/zh-cn_image_0000002552798118.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=D37E0527CEB6CF6A81E7FF1FFF1B37A10A55C419AAE46AA2DBA7769908220737)

List组件交叉轴方向在没有设置尺寸时，其尺寸默认自适应父组件尺寸。

## 开发布局

### 设置主轴方向

List组件主轴默认是垂直方向，即默认情况下不需要手动设置List方向，就可以构建一个垂直滚动列表。

若是水平滚动列表场景，将List的[listDirection](../harmonyos-references/ts-container-list.md#listdirection)属性设置为Axis.Horizontal即可实现。listDirection默认为Axis.Vertical，即主轴默认是垂直方向。

```
1. List(
2. // ···
3. ) {
4. // ···
5. }
6. .listDirection(Axis.Horizontal)
```

[ListLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ListLayout.ets#L27-L44)

### 设置交叉轴布局

List组件的交叉轴布局可以通过[lanes](../harmonyos-references/ts-container-list.md#lanes9)和[alignListItem](../harmonyos-references/ts-container-list.md#alignlistitem9)属性进行设置，lanes属性用于确定交叉轴排列的列表项数量，alignListItem用于设置子组件在交叉轴方向的对齐方式。

List组件的lanes属性通常用于在不同尺寸的设备自适应构建不同行数或列数的列表，即一次开发、多端部署的场景。lanes属性的取值类型是"number | [LengthConstrain](../harmonyos-references/ts-types.md#lengthconstrain)"，即整数或者LengthConstrain类型。以垂直列表为例，如果将lanes属性设为2，表示构建的是一个两列的垂直列表，如图2中右图所示。lanes的默认值为1，即默认情况下，垂直列表的列数是1。

```
1. List(
2. // ···
3. ) {
4. // ···
5. }
6. .lanes(2)
```

[ListLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ListLayout.ets#L77-L103)

当其取值为LengthConstrain类型时，表示会根据LengthConstrain与List组件的尺寸自适应决定行或列数。

```
1. @Entry
2. @Component
3. export struct ListLayout {
4. @State egLanes: LengthConstrain = { minLength: 200, maxLength: 300 };
5. build() {
6. // ···
7. List(
8. // ···
9. ) {
10. // ···
11. }
12. .lanes(this.egLanes)
13. // ···
14. }
15. }
```

[ListLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ListLayout.ets#L17-L119)

例如，假设在垂直列表中设置了lanes的值为{ minLength: 200, maxLength: 300 }。此时：

* 当List组件宽度为300vp时，由于minLength为200vp，此时列表为一列。
* 当List组件宽度变化至400vp时，符合两倍的minLength，则此时列表自适应为两列。

同样以垂直列表为例，当alignListItem属性设置为ListItemAlign.Center表示列表项在水平方向上居中对齐。alignListItem的默认值是ListItemAlign.Start，即列表项在列表交叉轴方向上默认按首部对齐。

```
1. List(
2. // ···
3. ) {
4. // ···
5. }
6. // ···
7. .alignListItem(ListItemAlign.Center)
```

[ListLayout.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ListLayout.ets#L76-L107)

## ListItem生命周期

### 使用ForEach创建ListItem

List组件创建时，所有ListItem将会被创建。显示区域内的ListItem在首帧进行布局，预加载范围内的ListItem在空闲时完成布局。预加载范围之外的ListItem仅创建ListItem自身，ListItem其内部的子组件不会被创建。

当List组件滑动时，进入预加载及显示区域的ListItem将会创建其内部的子组件并完成布局，而滑出预加载及显示区域的ListItem将不会被销毁。

**图7** ForEach创建ListItem的生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/uuKNViSAQnS4AlJnBVKbjQ/zh-cn_image_0000002583437813.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=88C3ACE4D127D020B3EA69A6817005C3D8AE19E5808354F1A4FFD2275C58A299)

### 使用LazyForEach创建ListItem

List组件创建时，显示区域中的ListItem会被创建与布局。预加载范围内的ListItem在空闲时创建与布局，但是不会被挂载到组件树上。预加载范围外的ListItem则不会被创建。

当List组件滑动时，进入预加载及显示区域的ListItem将被创建与布局，创建ListItem过程中，若ListItem内部包含@Reusable标记的自定义组件，则会优先从缓存池中复用。滑出预加载及显示区域的ListItem将被销毁，其内部若含@Reusable标记的自定义组件，则会被回收并加入缓存池。

**图8** LazyForEach创建ListItem的生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/DKHHEL7ITiy951B1HQElxw/zh-cn_image_0000002552957768.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=A781F66847F832FFCCD4C395A6938A2B8F19BE44D45FCB016EE88111D93D1AD5)

### 使用Repeat创建ListItem

**使用virtualScroll**

List组件创建时，使用设置了[virtualScroll](../harmonyos-references/ts-rendering-control-repeat.md#virtualscroll)的Repeat生成ListItem，此时显示区域内的ListItem将被创建和布局。预加载范围内的ListItem在渲染线程空闲时创建和布局，并且挂载至组件树上。预加载范围外的ListItem则不会被创建。

当List组件滑动时，进入预加载及显示区域的ListItem，将从缓存池中获取ListItem并复用及布局，若缓存池中无ListItem，则会新创建并布局。滑出预加载及显示区域的ListItem将被回收至缓存池。

**图9** Repeat使用virtualScroll创建ListItem的生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/7ica8U_HRUe1i9HGVePaYw/zh-cn_image_0000002583477769.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=5515B715331B36368D2B7450371FD3505A97117034A048222861CA0F0CF0BB92)

**不使用virtualScroll**

List组件创建时，所有ListItem均被创建。显示区域内的ListItem在首帧完成布局，预加载范围内的ListItem在空闲时完成布局。预加载范围外的ListItem不会进行布局。

当List组件滑动时，进入预加载及显示区域的ListItem将进行布局。滑出预加载及显示区域的ListItem不会销毁。

**图10** Repeat不使用virtualScroll创建ListItem的生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/zPNfXz0sRUKVt5x4cht3kg/zh-cn_image_0000002552798120.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=C3AD3D96CB8ECB5D51365AE650258AF2DE2E7ECDF0079CCBE0DAD499102BA650)

## 在列表中显示数据

列表视图垂直或水平显示项目集合，在行或列超出屏幕时提供滚动功能，使其适合显示大型数据集合。在最简单的列表形式中，List静态地创建其列表项ListItem的内容。

**图11** 城市列表

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/MnixXNeUSmGQwuzPDmegfA/zh-cn_image_0000002583437815.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=7F8762A1CBAFF091ED7C9DF4C5C9660324F7BA61CDB7C8A5A8075B99A2DDC1D9)

```
1. @Entry
2. @Component
3. export struct DataInList {
4. build() {
5. // ···
6. List() {
7. ListItem() {
8. // app.string.city_beijing 资源文件中的value值为'北京'
9. Text($r('app.string.city_beijing'))
10. .fontSize(24)
11. }

13. ListItem() {
14. // app.string.city_hangzhou 资源文件中的value值为'杭州'
15. Text($r('app.string.city_hangzhou'))
16. .fontSize(24)
17. }

19. ListItem() {
20. // app.string.city_shanghai 资源文件中的value值为'上海'
21. Text($r('app.string.city_shanghai'))
22. .fontSize(24)
23. }
24. }
25. .backgroundColor('#FFF1F3F5')
26. .alignListItem(ListItemAlign.Center)
27. // ···
28. }
29. }
```

[DataInList.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/DataInList.ets#L19-L96)

由于在ListItem中只能有一个根节点组件，不支持以平铺形式使用多个组件。因此，若列表项是由多个组件元素组成的，则需要将这多个元素组合到一个容器组件内或组成一个自定义组件。

**图12** 联系人列表项示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/y3MR45vCQrW3mQLo-aeNzw/zh-cn_image_0000002552957770.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=F764E4BE063FA9F8049A713D3E75E5E35A20EA2E6E6EC10F0FE1A718A43A7B73)

如上图所示，联系人列表的列表项中，每个联系人都有头像和名称。此时，需要将Image和Text封装到一个Row容器内。

```
1. List() {
2. ListItem() {
3. Row() {
4. // app.media.iconE为自定义资源
5. Image($r('app.media.iconE'))
6. .width(40)
7. .height(40)
8. .margin(10)

10. // app.string.peopleOne 资源文件中的value值为'小明'
11. Text($r('app.string.peopleOne'))
12. .fontSize(20)
13. }
14. }

16. ListItem() {
17. Row() {
18. // app.media.iconF为自定义资源
19. Image($r('app.media.iconF'))
20. .width(40)
21. .height(40)
22. .margin(10)

24. // app.string.peopleTwo 资源文件中的value值为'小红'
25. Text($r('app.string.peopleTwo'))
26. .fontSize(20)
27. }
28. }
29. }
```

[DataInList.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/DataInList.ets#L54-L84)

## 迭代列表内容

通常，应用通过数据集合动态地创建列表。使用[循环渲染](arkts-rendering-control-foreach.md)可从数据源中迭代获取数据，并在每次迭代过程中创建相应的组件，降低代码复杂度。

ArkTS通过[ForEach](arkts-rendering-control-foreach.md)提供了组件的循环渲染能力。以简单形式的联系人列表为例，将联系人名称和头像数据以Contact类结构存储到contacts数组，使用ForEach中嵌套ListItem的形式来代替多个平铺的、内容相似的ListItem，从而减少重复代码。

```
1. import { util } from '@kit.ArkTS';

3. class Contact {
4. public key: string = util.generateRandomUUID(true);
5. public name: ResourceStr;
6. public icon: Resource;

8. constructor(name: ResourceStr, icon: Resource) {
9. this.name = name;
10. this.icon = icon;
11. }
12. }

14. @Entry
15. @Component
16. export struct ListIteration {
17. private contacts: Array<Contact> = [

19. // app.string.peopleOne 资源文件中的value值为'小明'，app.media.iconA为自定义资源
20. new Contact($r('app.string.peopleOne'), $r('app.media.iconA')),
21. // app.string.peopleTwo 资源文件中的value值为'小红'，app.media.iconB为自定义资源
22. new Contact($r('app.string.peopleTwo'), $r('app.media.iconB'))
23. ];

25. build() {
26. // ...
27. List() {
28. ForEach(this.contacts, (item: Contact) => {
29. ListItem() {
30. Row() {
31. Image(item.icon)
32. .width(40)
33. .height(40)
34. .margin(10)
35. Text(item.name).fontSize(20)
36. }
37. .width('100%')
38. .justifyContent(FlexAlign.Start)
39. }
40. }, (item: Contact) => JSON.stringify(item))
41. }
42. .width('100%')
43. // ...
44. }
45. }
```

[ListIteration.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ListIteration.ets#L17-L76)

在List组件中，ForEach除了可以用来循环渲染ListItem，也可以用来循环渲染ListItemGroup。ListItemGroup的循环渲染详细使用请参见[支持分组列表](arkts-layout-development-create-list.md#支持分组列表)。

## 自定义列表样式

### 设置内容间距

在初始化列表时，如需在列表项之间添加间距，可以使用[ListOptions](../harmonyos-references/ts-container-list.md#listoptions18对象说明)的space参数。例如，在每个列表项之间沿主轴方向添加10vp的间距。

```
1. List({ space: 10 }) {
2. // ···
3. }
```

[CustomListStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/CustomListStyle.ets#L49-L61)

### 添加分隔线

分隔线用来将界面元素隔开，使单个元素更加容易识别。以系统设置场景为例（如下图所示），列表项左侧为图标（如蓝牙图标），右侧为文字描述且分割线在文字下方。

**图13** 设置列表分隔线样式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/-es60hhiTUWCJnk-FFU7Vg/zh-cn_image_0000002583477771.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=E746F246438BE10369F50885E593942326D4BD2E7E91507C530D8357A43D49FF)

List提供了[divider](../harmonyos-references/ts-container-list.md#divider)属性用于给列表项之间添加分隔线。在设置divider属性时，可以通过strokeWidth和color属性设置分隔线的粗细和颜色。

startMargin和endMargin属性分别用于设置分隔线距离列表侧边起始端的距离和距离列表侧边结束端的距离。

```
1. class DividerTmp {
2. public strokeWidth: Length = 1;
3. public startMargin: Length = 60;
4. public endMargin: Length = 10;
5. public color: ResourceColor = '#ffe9f0f0';

7. constructor(strokeWidth: Length, startMargin: Length, endMargin: Length, color: ResourceColor) {
8. this.strokeWidth = strokeWidth;
9. this.startMargin = startMargin;
10. this.endMargin = endMargin;
11. this.color = color;
12. }
13. }

15. @Entry
16. @Component
17. export struct CustomListStyle {
18. @State egDivider: DividerTmp = new DividerTmp(1, 60, 10, '#ffe9f0f0');

20. // ···

22. build() {
23. // ···
24. List(
25. // ···
26. ) {
27. // ···
28. }
29. .divider(this.egDivider)
30. // ···
31. }
32. }
```

[CustomListStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/CustomListStyle.ets#L18-L159)

此示例表示从距离列表侧边起始端60vp开始到距离结束端10vp的位置，画一条粗细为1vp的分割线，可以实现图9设置列表分隔线的样式。

说明

1. 分隔线的宽度会使ListItem之间存在一定间隔，当List设置的内容间距小于分隔线宽度时，ListItem之间的间隔会使用分隔线的宽度。
2. 当List存在多列时，分割线的startMargin和endMargin作用于每一列上。
3. List组件的分隔线画在两个ListItem之间，第一个ListItem上方和最后一个ListItem下方不会绘制分隔线。

### 添加滚动条

当列表项高度（宽度）超出屏幕高度（宽度）时，列表可以沿垂直（水平）方向滚动。在页面内容很多时，若用户需快速定位，可拖拽滚动条，如下图所示。

**图14** 列表的滚动条

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/HVutsqv4SRianYQXVB7CMw/zh-cn_image_0000002552798122.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=3ABCC83D0C3F3B6D8200BE155A1EF6B0F72019C1E882507D04CB3BC5235DE141)

在使用List组件时，可通过scrollBar属性控制列表滚动条的显示。scrollBar的取值类型为[BarState](../harmonyos-references/ts-appendix-enums.md#barstate)，当取值为BarState.Auto表示按需显示滚动条。此时，当触摸到滚动条区域时显示控件，可上下拖拽滚动条快速浏览内容，拖拽时会变粗。若不进行任何操作，2秒后滚动条自动消失。

scrollBar属性API version 9及以下版本默认值为BarState.Off，从API version 10版本开始默认值为BarState.Auto。

```
1. List(
2. // ···
3. ) {
4. // ···
5. }
6. // ···
7. .scrollBar(BarState.Auto)
```

[CustomListStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/CustomListStyle.ets#L89-L113)

## 添加外置滚动条

列表[List](../harmonyos-references/ts-container-list.md)可与[ScrollBar](../harmonyos-references/ts-basic-components-scrollbar.md)组件配合使用，为列表添加外置滚动条。两者通过绑定同一个[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)滚动控制器对象实现联动。

1. 首先，需要创建一个[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)类型的对象listScroller。

   ```
   1. private listScroller: Scroller = new Scroller();
   ```

   [CustomListStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/CustomListStyle.ets#L39-L41)
2. 然后，列表通过[scroller](../harmonyos-references/ts-container-list.md#listoptions18对象说明)参数绑定滚动控制器。

   ```
   1. // listScroller初始化List组件的scroller参数，绑定listScroller与列表。
   2. List({ scroller: this.listScroller }) {
   3. // ···
   4. }
   ```

   [CustomListStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/CustomListStyle.ets#L120-L137)
3. 最后，滚动条通过[scroller](../harmonyos-references/ts-basic-components-scrollbar.md#scrollbaroptions对象说明)参数绑定滚动控制器。

   ```
   1. // listScroller初始化ScrollBar组件的scroller参数，绑定listScroller与列表。
   2. ScrollBar({ scroller: this.listScroller})
   ```

   [CustomListStyle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/CustomListStyle.ets#L141-L144)

**图15** 列表的外置滚动条

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/KPeLgfxITeOcpuZMSPWvLA/zh-cn_image_0000002583437817.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=EE1882B2865173529DF3974BE35F4897AC91966FA8255898651D6AA989A92166)

说明

* 滚动条组件[ScrollBar](../harmonyos-references/ts-basic-components-scrollbar.md)，还可配合其他可滚动组件使用，如[ArcList](../harmonyos-references/ts-container-arclist.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)。
* 在圆形屏幕设备上，[List](../harmonyos-references/ts-container-list.md)可以与弧形滚动条组件[ArcScrollBar](../harmonyos-references/ts-basic-components-arcscrollbar.md)配合使用为列表添加弧形外置滚动条，使用方式可参考[创建弧形列表 (ArcList)](arkts-layout-development-create-arclist.md)的[添加外置滚动条ArcScrollBar](arkts-layout-development-create-arclist.md#添加外置滚动条arcscrollbar)章节。

## 支持分组列表

在列表中支持数据的分组展示，可以使列表显示结构清晰，查找方便，从而提高使用效率。分组列表在实际应用中十分常见，如下图所示联系人列表。

**图16** 联系人分组列表

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/1pN-R68gSqWiSd7C_qL5zA/zh-cn_image_0000002552957772.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=702FE383E9CABA64ACF14126BE578F9EDE59ABE5BD9D4E813488D6133C36C566)

在List组件中使用ListItemGroup对项目进行分组，可以构建二维列表。

在List组件中可以直接使用一个或者多个ListItemGroup组件，ListItemGroup的宽度默认充满List组件。在初始化ListItemGroup时，可通过header参数设置列表分组的头部组件。

```
1. @Entry
2. @Component
3. export struct GroupedList {
4. @Builder
5. itemHead(text: string) {
6. // 列表分组的头部组件，对应联系人分组A、B等位置的组件
7. Text(text)
8. .fontSize(20)
9. .backgroundColor('#fff1f3f5')
10. .width('100%')
11. .padding(5)
12. }

14. build() {
15. // ···
16. List(
17. // ···
18. ) {
19. ListItemGroup({ header: this.itemHead('A') }) {
20. // 循环渲染分组A的ListItem
21. // ···
22. }

24. ListItemGroup({ header: this.itemHead('B') }) {
25. // 循环渲染分组B的ListItem
26. // ···
27. }
28. }
29. // ···
30. }
31. }
```

[GroupedList.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/GroupedList.ets#L18-L81)

如果多个ListItemGroup结构类似，可以将多个分组的数据组成数组，然后使用ForEach对多个分组进行循环渲染。例如在联系人列表中，将每个分组的联系人数据contacts（可参考[迭代列表内容](arkts-layout-development-create-list.md#迭代列表内容)章节）和对应分组的标题title数据进行组合，定义为数组contactsGroups。然后在ForEach中对contactsGroups进行循环渲染，即可实现多个分组的联系人列表。可参考[添加粘性标题](arkts-layout-development-create-list.md#添加粘性标题)章节示例代码。

## 添加粘性标题

粘性标题是一种常见的标题模式，常用于定位字母列表的头部元素。如下图所示，在联系人列表中滚动A部分时，B部分开始的头部元素始终处于A的下方。而在开始滚动B部分时，B的头部会固定在屏幕顶部，直到所有B的项均完成滚动后，才被后面的头部替代。

粘性标题不仅有助于阐明列表中数据的表示形式和用途，还可以帮助用户在大量信息中进行数据定位，从而避免用户在标题所在的表的顶部与感兴趣区域之间反复滚动。

**图17** 粘性标题

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/-wp7knAyS_C1NE08Uc3iIw/zh-cn_image_0000002583477773.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=32486C5D77B233190910007DBD1505B728441B31D539ED36189C9839FD70F3A9)

List组件的[sticky](../harmonyos-references/ts-container-list.md#sticky9)属性配合ListItemGroup组件使用，用于设置ListItemGroup中的头部组件是否呈现吸顶效果或者尾部组件是否呈现吸底效果。

通过给List组件设置sticky属性为StickyStyle.Header，即可实现列表的粘性标题效果。如果需要支持吸底效果，可以通过footer参数初始化ListItemGroup的底部组件，并将sticky属性设置为StickyStyle.Footer。

```
1. import { util } from '@kit.ArkTS';

3. class Contact {
4. public key: string = util.generateRandomUUID(true);
5. public name: string | Resource;
6. public icon: Resource;

8. constructor(name: string | Resource, icon: Resource) {
9. this.name = name;
10. this.icon = icon;
11. }
12. }

14. class ContactsGroup {
15. public title: string = '';
16. public contacts: Array<object> | null = null;
17. public key: string = '';
18. }

20. export class ContactsGroupDataSource implements IDataSource {
21. private list: object[] = [];

23. constructor(list: object[]) {
24. this.list = list;
25. }

27. totalCount(): number {
28. return this.list.length;
29. }

31. getData(index: number): object {
32. return this.list[index];
33. }

35. registerDataChangeListener(listener: DataChangeListener): void {
36. }

38. unregisterDataChangeListener(listener: DataChangeListener): void {
39. }
40. }

42. export let contactsGroups: object[] = [
43. {
44. title: 'A',
45. contacts: [
46. // app.string.contacts_A_one 资源文件中的value值为'艾佳'，app.media.iconA为自定义资源
47. new Contact($r('app.string.contacts_A_one'), $r('app.media.iconA')),
48. // app.string.contacts_A_two 资源文件中的value值为'安安'，app.media.iconB为自定义资源
49. new Contact($r('app.string.contacts_A_two'), $r('app.media.iconB')),
50. // app.media.iconC为自定义资源
51. new Contact('Angela', $r('app.media.iconC')),
52. ],
53. key: util.generateRandomUUID(true)
54. } as ContactsGroup,
55. {
56. title: 'B',
57. contacts: [
58. // app.string.contacts_B_one 资源文件中的value值为'白叶'，app.media.iconD为自定义资源
59. new Contact($r('app.string.contacts_B_one'), $r('app.media.iconD')),
60. // app.string.contacts_B_three 资源文件中的value值为'伯明'，app.media.iconE为自定义资源
61. new Contact($r('app.string.contacts_B_three'), $r('app.media.iconE'))
62. ],
63. key: util.generateRandomUUID(true)
64. } as ContactsGroup
65. ];
66. export let contactsGroupsDataSource: ContactsGroupDataSource = new ContactsGroupDataSource(contactsGroups);

68. @Entry
69. @Component
70. export struct StickyHeaderList {
71. // 定义分组联系人数据集合contactsGroups数组
72. @Builder
73. itemHead(text: string) {
74. // 列表分组的头部组件，对应联系人分组A、B等位置的组件
75. Text(text)
76. .fontSize(20)
77. .backgroundColor('#fff1f3f5')
78. .width('100%')
79. .padding(5)
80. }

82. build() {
83. // ...
84. List() {
85. // 懒加载ListItemGroup，contactsGroups为多个分组联系人contacts和标题title的数据集合
86. LazyForEach(contactsGroupsDataSource, (itemGroup: ContactsGroup) => {
87. ListItemGroup({ header: this.itemHead(itemGroup.title) }) {
88. // 循环渲染ListItem
89. if (itemGroup.contacts) {
90. LazyForEach(new ContactsGroupDataSource(itemGroup.contacts), (item: Contact) => {
91. ListItem() {
92. Row() {
93. Image(item.icon).width(40).height(40).margin(10)
94. Text(item.name).fontSize(20)
95. }.width('100%').justifyContent(FlexAlign.Start)
96. }
97. }, (item: Contact) => JSON.stringify(item))
98. }
99. }
100. }, (itemGroup: ContactsGroup) => JSON.stringify(itemGroup))
101. }
102. .sticky(StickyStyle.Header) // 设置吸顶，实现粘性标题效果
103. // ...
104. }
105. }
```

[StickyHeaderList.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/StickyHeaderList.ets#L17-L139)

## 控制滚动位置

控制滚动位置在实际应用中十分常见，例如当新闻页列表项数量庞大，用户滚动列表到一定位置时，希望快速滚动到列表底部或返回列表顶部。此时，可以通过控制滚动位置来实现列表的快速定位，如下图所示。

**图18** 返回列表顶部

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/czmlb3B5RnqXeW0sW-Djsg/zh-cn_image_0000002552798124.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=58A4136A0EFC638D043FDED49F507733B15A96ECBF9101D6348483131092B7E1)

List组件初始化时，可以通过scroller参数绑定一个[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)对象，进行列表的滚动控制。例如，用户在新闻应用中，点击新闻页面底部的返回顶部按钮时，就可以通过Scroller对象的scrollToIndex方法使列表滚动到指定的列表项索引位置。

首先，需要创建一个Scroller的对象listScroller。

```
1. private listScroller: Scroller = new Scroller();
```

[ControlledScrollPositionList.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ControlledScrollPositionList.ets#L22-L24)

然后，通过将listScroller用于初始化List组件的scroller参数，完成listScroller与列表的绑定。在需要跳转的位置指定scrollToIndex的参数为0，表示返回列表顶部。

```
1. Stack({ alignContent: Alignment.Bottom }) {
2. // 将listScroller用于初始化List组件的scroller参数，完成listScroller与列表的绑定。
3. List({ space: 20, scroller: this.listScroller }) {
4. // ...
5. }

7. Button() {
8. // ...
9. }
10. // ...
11. .onClick(() => {
12. // 点击按钮时，指定跳转位置，返回列表顶部
13. this.listScroller.scrollToIndex(0);
14. })
15. }
```

[ControlledScrollPositionList.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ControlledScrollPositionList.ets#L32-L66)

## 响应滚动位置

许多应用需要监听列表的滚动位置变化并作出响应。例如，在联系人列表滚动时，如果跨越了不同字母开头的分组，则侧边字母索引栏也需要更新到对应的字母位置。

除了字母索引之外，滚动列表结合多级分类索引在应用开发过程中也很常见，例如购物应用的商品分类页面，多级分类也需要监听列表的滚动位置。

**图19** 字母索引响应联系人列表滚动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/PdYjmn7TS72CJst-WRo2yw/zh-cn_image_0000002583437819.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=275806126C041D2882A5D786268815848A15AFDF854D29174F8B1BD3002A0E15)

如上图所示，当联系人列表从A滚动到B时，右侧索引栏也需要同步从选中A状态变成选中B状态。此场景可以通过监听List组件的[onScrollIndex](../harmonyos-references/ts-container-list.md#onscrollindex)事件来实现，右侧索引栏需要使用字母表索引组件[AlphabetIndexer](../harmonyos-references/ts-container-alphabet-indexer.md)。

在列表滚动时，根据列表此时所在的索引值位置firstIndex，重新计算字母索引栏对应字母的位置selectedIndex。由于AlphabetIndexer组件通过selected属性设置了选中项索引值，当selectedIndex变化时会触发AlphabetIndexer组件重新渲染，从而显示为选中对应字母的状态。

```
1. const alphabets = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
2. 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

4. // ...

6. @Entry
7. @Component
8. export struct ResponsiveScrollPositionList {
9. @State selectedIndex: number = 0;
10. private listScroller: Scroller = new Scroller();
11. // ...

13. build() {
14. // ...
15. Stack({ alignContent: Alignment.End }) {
16. // 此为响应滚动位置示例List容器
17. // listScroller初始化List组件的scroller参数，绑定listScroller与列表。
18. List({ scroller: this.listScroller }) {
19. // ...
20. }
21. .onScrollIndex((firstIndex: number) => {
22. // 根据列表滚动到的索引值，重新计算对应联系人索引栏的位置this.selectedIndex
23. // ...
24. })

26. // 字母表索引组件
27. AlphabetIndexer({ arrayValue: alphabets, selected: 0 })
28. .selected(this.selectedIndex)
29. .onSelect((index: number) => {
30. this.listScroller.scrollToIndex(index);
31. })
32. }
33. // ...
34. }
35. }
```

[ResponsiveScrollPositionList.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ResponsiveScrollPositionList.ets#L19-L198)

说明

计算索引值时，ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值。

## 响应列表项侧滑

侧滑菜单在许多应用中都很常见。例如，通讯类应用通常会给消息列表提供侧滑删除功能，即用户可以通过向左侧滑列表的某一项，再点击删除按钮删除消息，如下图所示。其中，列表项头像右上角标记设置参考[给列表项添加标记](arkts-layout-development-create-list.md#给列表项添加标记)。

**图20** 侧滑删除列表项

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/JCUAZljYTGCbBVQJOrV81Q/zh-cn_image_0000002552957774.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=829D24BAB57E3298D0DB23749D02B9B61EE6C4C6539BD25752528575A3CC4413)

ListItem的[swipeAction属性](../harmonyos-references/ts-container-listitem.md#swipeaction9)可用于实现列表项的左右滑动功能。swipeAction属性方法初始化时有必填参数SwipeActionOptions，其中，start参数表示设置列表项右滑时起始端滑出的组件，end参数表示设置列表项左滑时尾端滑出的组件。

在消息列表中，end参数表示设置ListItem左滑时尾端划出自定义组件，即删除按钮。在初始化end方法时，将滑动列表项的索引传入删除按钮组件，当用户点击删除按钮时，可以根据索引值来删除列表项对应的数据，从而实现侧滑删除功能。

1. 实现尾端滑出组件的构建。

   ```
   1. @Builder
   2. itemEnd(index: number) {
   3. // 构建尾端滑出组件
   4. Button({ type: ButtonType.Circle }) {
   5. Image($r('sys.media.ohos_ic_bottomsheet_close'))
   6. .width(40)
   7. .height(40)
   8. }
   9. // ...
   10. .onClick(() => {
   11. // this.arr为列表数据源，可根据实际场景构造。点击后从数据源删除指定数据项。
   12. this.arr.splice(index, 1);
   13. })
   14. }
   ```

   [SwipeableListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/SwipeableListItem.ets#L24-L41)
2. 绑定swipeAction属性到可左滑的ListItem上。

   ```
   1. // 构建List时，通过ForEach基于数据源this.messages循环渲染ListItem。
   2. ListItem() {
   3. // ···
   4. }.swipeAction({
   5. end: {
   6. // index为该ListItem在List中的索引值。
   7. builder: () => {
   8. // ···
   9. this.itemEnd(this.index);
   10. },
   11. }
   12. }) // 设置侧滑属性.
   ```

   [SwipeableListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/SwipeableListItem.ets#L49-L72)

## 给列表项添加标记

添加标记是一种无干扰性且直观的方法，用于显示通知或将注意力集中到应用内的某个区域。例如，当消息列表接收到新消息时，通常对应消息列表的右上方会出现标记，提示有若干条未读消息，如下图所示。

**图21** 给列表项添加标记

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/wAvzP2rWRYGsCQ9JBV7k9w/zh-cn_image_0000002583477775.png?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=D3D4286B1031EF7D74BB8F3A192D4AD19B8BB168BEA6B19DF3AC05ECFB77E351)

在ListItem中使用[Badge](../harmonyos-references/ts-container-badge.md)组件可实现给列表项添加标记功能。Badge是可以附加在单个组件上用于信息标记的容器组件。

在消息列表中，若希望在消息的右上角添加标记，可在实现消息列表项ListItem中，将对应的组件作为Badge的子组件。

在Badge组件中，count和position参数用于设置需要展示的消息数量和提示点显示位置，还可以通过style参数灵活设置标记的样式。

```
1. ListItem() {
2. // Badge组件实现消息右上角添加标记功能
3. Badge({
4. count: 1,
5. position: BadgePosition.RightTop,
6. style: { badgeSize: 16, badgeColor: '#FA2A2D' }
7. }) {
8. // ...
9. }
10. }
```

[TaggedListItems.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/TaggedListItems.ets#L31-L51)

## 下拉刷新与上拉加载

页面的下拉刷新与上拉加载功能在移动应用中十分常见，例如，新闻页面的内容刷新和加载。这两种操作的原理都是通过响应用户的[触摸事件](../harmonyos-references/ts-universal-events-touch.md)，在顶部或者底部显示一个刷新或加载视图，完成后再将此视图隐藏。

以下拉刷新为例，其实现主要分成三步：

1. 监听手指按下事件，记录其初始位置的值。
2. 监听手指按压移动事件，记录并计算当前移动的位置与初始值的差值，大于0表示向下移动，同时设置一个允许移动的最大值。
3. 监听手指抬起事件，若此时移动达到最大值，则触发数据加载并显示刷新视图，加载完成后将此视图隐藏。

说明

页面的下拉刷新操作推荐使用[Refresh](../harmonyos-references/ts-container-refresh.md)组件实现。

下拉刷新与上拉加载的具体实现可参考[新闻数据加载](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-NewsDataArkTS)。

## 编辑列表

列表的编辑模式用途十分广泛，常见于待办事项管理、文件管理、备忘录的记录管理等应用场景。在列表的编辑模式下，新增和删除列表项是最基础的功能，其核心是对列表项对应的数据集合进行数据添加和删除。

下面以待办事项管理为例，介绍如何快速实现新增和删除列表项功能。

### 新增列表项

如下图所示，当用户点击添加按钮时，提供用户新增列表项内容选择或填写的交互界面，用户点击确定后，列表中新增对应的项目。

**图22** 新增待办

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/zfSjW_kwQS-Vf3-1ZsTDkQ/zh-cn_image_0000002552798126.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=704E69F6E3152D052E3F1C88AA4E4DDCCE670599200B5799D12DB0A276489525)

添加列表项功能实现主要流程如下：

1. 定义列表项数据结构，以待办事项管理为例，首先定义待办数据结构。

   ```
   1. // ToDo.ets
   2. import { util } from '@kit.ArkTS';

   4. export class ToDo {
   5. public key: string = util.generateRandomUUID(true);
   6. public name: string;

   8. constructor(name: string) {
   9. this.name = name;
   10. }
   11. }
   ```

   [ToDo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ToDo.ets#L16-L28)
2. 构建列表整体布局和列表项。

   ```
   1. import { ToDo } from './ToDo';

   3. @Component
   4. export struct ToDoListItem {
   5. @Link isEditMode: boolean;
   6. @Link selectedItems: ToDo[];
   7. private toDoItem: ToDo = new ToDo('');

   9. build() {
   10. Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
   11. // ···
   12. }
   13. // ···
   14. .width('100%')
   15. .height(80)
   16. // .padding() 根据具体使用场景设置
   17. .borderRadius(24)
   18. // .linearGradient() 根据具体使用场景设置
   19. .gesture(
   20. GestureGroup(GestureMode.Exclusive,
   21. LongPressGesture()
   22. .onAction(() => {
   23. })
   24. )
   25. )
   26. }
   27. }
   ```

   [ToDoListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ToDoListItem.ets#L16-L51)
3. 初始化待办列表数据和可选事项，最后，构建列表布局和列表项。

   ```
   1. import { ToDo } from './ToDo';
   2. import { ToDoListItem } from './ToDoListItem';

   4. @Entry
   5. @Component
   6. export struct AddListItem {
   7. @State toDoData: ToDo[] = [];
   8. @Watch('onEditModeChange') @State isEditMode: boolean = false;
   9. @State selectedItems: ToDo[] = [];
   10. private availableThings: string [] = [];

   12. aboutToAppear(): void {
   13. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   14. const reading = context.resourceManager.getStringByNameSync('Reading')
   15. this.availableThings.push(reading)
   16. const exercise = context.resourceManager.getStringByNameSync('Exercise')
   17. this.availableThings.push(exercise)
   18. const travel = context.resourceManager.getStringByNameSync('Travel')
   19. this.availableThings.push(travel)
   20. const listening = context.resourceManager.getStringByNameSync('Listening_Music')
   21. this.availableThings.push(listening)
   22. const watching = context.resourceManager.getStringByNameSync('Watching_Films')
   23. this.availableThings.push(watching)
   24. const singing = context.resourceManager.getStringByNameSync('Singing')
   25. this.availableThings.push(singing)
   26. }

   28. onEditModeChange() {
   29. if (!this.isEditMode) {
   30. this.selectedItems = [];
   31. }
   32. }

   34. build() {
   35. // ...
   36. Column(
   37. // ...
   38. ) {
   39. // ...
   40. Row() {
   41. if (this.isEditMode) {
   42. Text('X')
   43. .fontSize(20)
   44. .onClick(() => {
   45. this.isEditMode = false;
   46. })
   47. .margin({ left: 20, right: 20 })
   48. } else {
   49. // app.string.TodoItem 资源文件中的value值为'待办'
   50. Text($r('app.string.TodoItem'))
   51. .fontSize(36)
   52. .margin({ left: 40 })
   53. Blank()
   54. Text('+')// 提供新增列表项入口，即给新增按钮添加点击事件
   55. // ...
   56. .onClick(() => {
   57. this.getUIContext().showTextPickerDialog({
   58. range: this.availableThings,
   59. onAccept: (value: TextPickerResult) => {
   60. let arr = Array.isArray(value.index) ? value.index : [value.index];
   61. for (let i = 0; i < arr.length; i++) {
   62. this.toDoData.push(new ToDo(this.availableThings[arr[i]])); // 新增列表项数据toDoData(可选事项)
   63. }
   64. },
   65. })
   66. })
   67. }
   68. // ...

   70. List({ space: 10 }) {
   71. ForEach(this.toDoData, (toDoItem: ToDo) => {
   72. ListItem() {
   73. // 将toDoData的每个数据放入到以model的形式放进ListItem里
   74. ToDoListItem({
   75. isEditMode: this.isEditMode,
   76. toDoItem: toDoItem,
   77. selectedItems: this.selectedItems
   78. })
   79. }
   80. }, (toDoItem: ToDo) => toDoItem.name.toString())
   81. }
   82. }
   83. }
   84. // ...
   85. }
   86. }
   ```

   [AddListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/AddListItem.ets#L19-L133)

### 删除列表项

如下图所示，当用户长按列表项进入删除模式时，提供用户删除列表项选择的交互界面，用户勾选完成后点击删除按钮，列表中删除对应的项目。

**图23** 长按删除待办事项

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/FtUHGxGhQ02lkN-Mi1PNiw/zh-cn_image_0000002583437821.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=957E37492D2A52A2C999A700729AD90AA9E2FE242314855D9C0B8190066519A9)

删除列表项功能实现主要流程如下：

1. 列表的删除功能一般进入编辑模式后才可使用，所以需要提供编辑模式的入口。

   以待办列表为例，通过监听列表项的长按事件，当用户长按列表项时，进入编辑模式。

   ```
   1. import { util } from '@kit.ArkTS';

   3. // 结构参考
   4. export class ToDo {
   5. public key: string = util.generateRandomUUID(true);
   6. public name: string;
   7. public toDoData: ToDo[] = [];

   9. constructor(name: string) {
   10. this.name = name;
   11. }
   12. }
   ```

   [DeleteListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/DeleteListItem.ets#L18-L31)

   实现参考：

   ```
   1. Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
   2. // ...
   3. }
   4. // ...
   5. .gesture(
   6. GestureGroup(GestureMode.Exclusive,
   7. LongPressGesture()
   8. .onAction(() => {
   9. if (!this.isEditMode) {
   10. this.isEditMode = true; // 进入编辑模式
   11. }
   12. })
   13. )
   14. )
   ```

   [DeleteListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/DeleteListItem.ets#L40-L80)
2. 需要响应用户的选择交互，记录要删除的列表项数据。

   在待办列表中，通过勾选框的勾选或取消勾选，响应用户勾选列表项变化，记录所有选择的列表项。

   ```
   1. import { util } from '@kit.ArkTS';

   3. // 结构参考
   4. export class ToDo {
   5. public key: string = util.generateRandomUUID(true);
   6. public name: string;
   7. public toDoData: ToDo[] = [];

   9. constructor(name: string) {
   10. this.name = name;
   11. }
   12. }
   ```

   [DeleteListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/DeleteListItem.ets#L18-L31)

   实现参考：

   ```
   1. if (this.isEditMode) {
   2. Checkbox()
   3. .onChange((isSelected) => {
   4. if (isSelected) {
   5. this.selectedItems.push(new ToDo(this.toDoItem.name)); // this.selectedItems为勾选时，记录选中的列表项，可根据实际场景构造
   6. } else {
   7. let index = this.selectedItems.indexOf(new ToDo(this.toDoItem.name));
   8. if (index !== -1) {
   9. this.selectedItems.splice(index, 1); // 取消勾选时，则将此项从selectedItems中删除
   10. }
   11. }
   12. })
   13. }
   ```

   [DeleteListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/DeleteListItem.ets#L47-L61)
3. 需要响应用户点击删除按钮事件，删除列表中对应的选项。

   ```
   1. import { util } from '@kit.ArkTS';

   3. // 结构参考
   4. export class ToDo {
   5. public key: string = util.generateRandomUUID(true);
   6. public name: string;
   7. public toDoData: ToDo[] = [];

   9. constructor(name: string) {
   10. this.name = name;
   11. }
   12. }
   ```

   [DeleteListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/DeleteListItem.ets#L18-L31)

   实现参考：

   ```
   1. // app.string.delete 资源文件中的value值为'删除'
   2. Button($r('app.string.delete'))
   3. // ···
   4. .onClick(() => {
   5. // this.toDoData为待办的列表项，可根据实际场景构造。点击后删除选中的列表项对应的toDoData数据
   6. this.toDoData = this.toDoData.filter(toDoItem =>
   7. !this.selectedItems.some(selectedItem => selectedItem.name === toDoItem.name));
   8. this.isEditMode = false;
   9. })
   ```

   [DeleteListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/DeleteListItem.ets#L192-L205)

## 长列表的处理

[循环渲染](arkts-rendering-control-foreach.md)适用于短列表，当构建具有大量列表项的长列表时，如果直接采用循环渲染方式，会一次性加载所有的列表元素，会导致页面启动时间过长，影响用户体验。因此，推荐使用[数据懒加载](arkts-rendering-control-lazyforeach.md)（LazyForEach）方式实现按需迭代加载数据，从而提升列表性能。

关于长列表按需加载优化的具体实现可参考[数据懒加载](arkts-rendering-control-lazyforeach.md)章节中的示例。

当使用懒加载方式渲染列表时，为了更好的列表滚动体验，减少列表滑动时出现白块，List组件提供了[cachedCount](../harmonyos-references/ts-container-list.md#cachedcount)参数用于设置列表项缓存数，懒加载方式只会预加载List显示区域外cachedCount的内容，而非懒加载会全部加载。无论懒加载还是非懒加载都只布局List显示区域+List显示区域外cachedCount的内容。

```
1. List(
2. // ···
3. ) {
4. // ···
5. }.cachedCount(3)
```

[DeleteListItem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/DeleteListItem.ets#L162-L181)

以垂直列表为例：

* List设置cachedCount后，显示区域外上下各会预加载并布局cachedCount行ListItem。计算ListItem行数时，会计算ListItemGroup内部的ListItem行数。如果ListItemGroup内没有ListItem，则整个ListItemGroup算一行。
* List下嵌套使用LazyForEach，并且LazyForEach下嵌套使用ListItemGroup时，LazyForEach会在List显示区域外上下各会创建cachedCount个ListItemGroup。

说明

1. cachedCount的增加会增大UI的CPU、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。
2. 列表使用数据懒加载时，除了显示区域的列表项和前后缓存的列表项，其他列表项会被销毁。

## 折叠与展开

列表项的折叠与展开用途广泛，常用于信息清单的展示、填写等应用场景。

**图24** 列表项的折叠与展开

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/a7e0rsoqQ0qRJgdmjaNfCw/zh-cn_image_0000002552957776.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=F17A5A2796B987D19D349F3D11398F9D45DBCE49AB42616D064F7A753793344E)

列表项折叠与展开效果实现主要流程如下：

1. 定义列表项数据结构。

   ```
   1. import { curves } from '@kit.ArkUI';

   3. interface ItemInfo {
   4. index: number,
   5. name: ResourceStr,
   6. label: ResourceStr,
   7. type?: string,
   8. }

   10. interface ItemGroupInfo extends ItemInfo {
   11. children: ItemInfo[]
   12. }
   ```

   [CollapseAndExpand.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/CollapseAndExpand.ets#L18-L31)
2. 构造列表结构。

   ```
   1. @State routes: ItemGroupInfo[] = [
   2. {
   3. index: 0,
   4. name: 'basicInfo',
   5. // app.string.Personal_Basic_Information 资源文件中的value值为'个人基本资料'
   6. label: $r('app.string.Personal_Basic_Information'),
   7. children: [
   8. {
   9. index: 0,
   10. // app.string.nick_name 资源文件中的value值为'昵称'
   11. name: $r('app.string.nick_name'),
   12. label: 'xxxx',
   13. type: 'Text'
   14. },
   15. {
   16. index: 1,
   17. // app.string.avatar 资源文件中的value值为'头像'
   18. name: $r('app.string.avatar'),
   19. label: $r('sys.media.ohos_user_auth_icon_face'),
   20. type: 'Image'
   21. },
   22. {
   23. index: 2,
   24. // app.string.age 资源文件中的value值为'年龄'
   25. name: $r('app.string.age'),
   26. label: 'xxxx',
   27. type: 'Text'
   28. },
   29. {
   30. index: 3,
   31. // app.string.birthday 资源文件中的value值为'性别'
   32. name: $r('app.string.birthday'),
   33. label: 'xxxxxxxxx',
   34. type: 'Text'
   35. },
   36. {
   37. index: 4,
   38. // app.string.gender 资源文件中的value值为''
   39. name: $r('app.string.gender'),
   40. label: 'xxxxxxxx',
   41. type: 'Text'
   42. },
   43. ]
   44. },
   45. {
   46. index: 1,
   47. name: 'equipInfo',
   48. // app.string.Device_Information 资源文件中的value值为'设备信息'
   49. label: $r('app.string.Device_Information'),
   50. children: []
   51. },
   52. {
   53. index: 2,
   54. name: 'appInfo',
   55. // app.string.Application_usage_information 资源文件中的value值为'应用使用信息'
   56. label: $r('app.string.Application_usage_information'),
   57. children: []
   58. },
   59. {
   60. index: 3,
   61. name: 'uploadInfo',
   62. // app.string.data_you_voluntarily_uploaded 资源文件中的value值为'您主动上传的数据'
   63. label: $r('app.string.data_you_voluntarily_uploaded'),
   64. children: []
   65. },
   66. {
   67. index: 4,
   68. name: 'tradeInfo',
   69. // app.string.Trading_and_asset_information 资源文件中的value值为'交易与资产信息'
   70. label: $r('app.string.Trading_and_asset_information'),
   71. children: []
   72. },
   73. {
   74. index: 5,
   75. name: 'otherInfo',
   76. // app.string.Other_materials 资源文件中的value值为'其他资料'
   77. label: $r('app.string.Other_materials'),
   78. children: []
   79. },
   80. ];
   81. @State expandedItems: boolean[] = Array(this.routes.length).fill(false);
   82. @State selection: string | null = null;

   84. // ...

   86. build() {
   87. // ...
   88. Column() {
   89. List({ space: 10 }) {
   90. ForEach(this.routes, (itemGroup: ItemGroupInfo) => {
   91. ListItemGroup({
   92. header: this.ListItemGroupHeader(itemGroup),
   93. style: ListItemGroupStyle.CARD,
   94. }) {
   95. if (this.expandedItems[itemGroup.index] && itemGroup.children) {
   96. ForEach(itemGroup.children, (item: ItemInfo) => {
   97. ListItem({ style: ListItemStyle.CARD }) {
   98. Row() {
   99. Text(item.name)
   100. Blank()
   101. if (item.type === 'Image') {
   102. Image(item.label)
   103. .height(20)
   104. .width(20)
   105. } else {
   106. Text(item.label)
   107. }
   108. Image($r('sys.media.ohos_ic_public_arrow_right'))
   109. .fillColor($r('sys.color.ohos_id_color_fourth'))
   110. .height(30)
   111. .width(30)
   112. }
   113. .width('100%')
   114. }
   115. .width('100%')
   116. .animation({ curve: curves.interpolatingSpring(0, 1, 528, 39) })
   117. })
   118. }
   119. }.clip(true)
   120. })
   121. }
   122. .width('100%')
   123. }
   124. .width('100%')
   125. .height('100%')
   126. .justifyContent(FlexAlign.Start)
   127. .backgroundColor($r('sys.color.ohos_id_color_sub_background'))
   128. // ...
   129. }
   130. }
   ```

   [CollapseAndExpand.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/CollapseAndExpand.ets#L36-L208)
3. 通过改变ListItem的状态，来控制每个列表项是否展开，并通过[animation](../harmonyos-references/ts-animatorproperty.md#animation)和[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)来实现展开与折叠过程中的动效效果。

   ```
   1. @Builder
   2. ListItemGroupHeader(itemGroup: ItemGroupInfo) {
   3. Row() {
   4. Text(itemGroup.label)
   5. Blank()
   6. Image($r('sys.media.ohos_ic_public_arrow_down'))
   7. .fillColor($r('sys.color.ohos_id_color_fourth'))
   8. .height(30)
   9. .width(30)
   10. .rotate({ angle: !!itemGroup.children.length ? (this.expandedItems[itemGroup.index] ? 180 : 0) : 180 })
   11. .animation({ curve: curves.interpolatingSpring(0, 1, 228, 22) })
   12. }
   13. .width('100%')
   14. .padding(10)
   15. .animation({ curve: curves.interpolatingSpring(0, 1, 528, 39) })
   16. .onClick(() => {
   17. if (itemGroup.children.length) {
   18. this.getUIContext()?.animateTo({ curve: curves.interpolatingSpring(0, 1, 528, 39) }, () => {
   19. this.expandedItems[itemGroup.index] = !this.expandedItems[itemGroup.index];
   20. })
   21. }
   22. })
   23. }
   ```

   [CollapseAndExpand.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/CollapseAndExpand.ets#L121-L145)

## 切换布局方向

部分业务场景需要列表底部插入数据时，自动向上滚动，把新插入的节点展示出来。例如，直播评论、即时聊天等应用场景。而List组件正常布局时, 在内容下方增加节点，内容是保持不变的。此时，可以通过切换布局方向来实现所需效果。

**图25** 实时消息滚动显示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/N20TyqvZSKWkVAGFg7nTtw/zh-cn_image_0000002583477777.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=0FBB97449B144D9F82855A86C7431E5F5C3A849E2643196FDD29FB02F4D9A7C6)

1. 定义列表项数据结构。

   ```
   1. interface Message {
   2. id: number
   3. content: ResourceStr
   4. sender: ResourceStr
   5. }
   ```

   [ListChatRoom.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ListChatRoom.ets#L19-L25)
2. 构造列表结构，同时把[stackFromEnd](../harmonyos-references/ts-container-list.md#stackfromend19)接口参数值设置为true，即可实现List列表在底部插入数据时，内容向上滚动。

   ```
   1. @Builder
   2. MessageItem(message: Message) {
   3. Column() {
   4. Text(`${message.sender}: ${message.content}`)
   5. .fontSize(16)
   6. .textAlign(TextAlign.Start)
   7. .padding(10)
   8. .backgroundColor(message.sender === 'system' ? '#F0F0F0' : '#E6F3FF')
   9. .borderRadius(8)
   10. }
   11. .width('100%')
   12. .alignItems(HorizontalAlign.Start)
   13. .margin({ bottom: 8 })
   14. }

   16. @State messages: Message[] = [];

   18. aboutToAppear(): void {
   19. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   20. // app.string.welcome_live_room资源文件中的value值为'欢迎来到直播间'
   21. const welcomeLiveRoom = context.resourceManager.getStringByNameSync('welcome_live_room');
   22. // app.string.system资源文件中的value值为'系统'
   23. const system = context.resourceManager.getStringByNameSync('system');
   24. // app.string.hello_everyone资源文件中的value值为'大家好啊~'
   25. const helloEveryone = context.resourceManager.getStringByNameSync('hello_everyone');
   26. // app.string.anchors资源文件中的value值为'主播'
   27. const anchors = context.resourceManager.getStringByNameSync('anchors');
   28. this.messages = [
   29. { id: 1, content: welcomeLiveRoom, sender: system },
   30. { id: 2, content: helloEveryone, sender: anchors }
   31. ];
   32. }

   34. build() {
   35. // ...
   36. Column() {
   37. // 聊天消息区域
   38. List({ space: 10 }) {
   39. ForEach(this.messages, (item: Message) => {
   40. ListItem() {
   41. this.MessageItem(item)
   42. }
   43. }, (item: Message) => item.id.toString())
   44. }
   45. .stackFromEnd(true)
   46. .layoutWeight(1)  // 占据剩余空间
   47. .alignListItem(ListItemAlign.Center)

   49. // ...
   50. }
   51. .width('100%')
   52. .height('100%')
   53. // ...
   54. }
   ```

   [ListChatRoom.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/ListChatRoom.ets#L61-L137)

## 支持滑动离手事件

从API version 20开始，滚动类组件（[Grid](../harmonyos-references/ts-container-grid.md)、[List](../harmonyos-references/ts-container-list.md)、[Scroll](../harmonyos-references/ts-container-scroll.md)、[WaterFlow](../harmonyos-references/ts-container-waterflow.md)）支持滑动离手事件回调功能，当用户手指离开屏幕时，会触发该事件并上报离手瞬间的滑动速度。开发者可利用此接口实现类似新闻浏览页面的自定义限位滚动效果，短新闻限位滚动，长新闻自由滚动。

**图26** 自定义限位滚动效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/OYerKNNDS7qv5-qW2-eJpg/zh-cn_image_0000002552798128.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=FF22DC9B852D838AB33F17C5BA4095494BE1F9FE46F0859F70783DF5AB825D70)

1. 定义新闻条目数据结构。

   ```
   1. class News {
   2. public id: string;
   3. public title: ResourceStr;
   4. public content: ResourceStr;
   5. public type: string;

   7. constructor(id: string, title: ResourceStr, content: ResourceStr, type: string) {
   8. this.id = id;
   9. this.title = title;
   10. this.content = content;
   11. this.type = type;
   12. }
   13. }
   ```

   [SupportSlidingHand.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/SupportSlidingHand.ets#L18-L32)
2. 构造新闻条目结构，通过type属性来区分长新闻，短新闻。

   ```
   1. @State newsData: Array<News> = [
   2. // app.string.new_title 资源文件中的value值为'新闻标题'
   3. // app.string.new_short 资源文件中的value值为'这是第一条短新闻，内容较少，快速滑动切换'
   4. new News('1', $r('app.string.new_title'), $r('app.string.new_short'), 'short'),
   5. new News('2', $r('app.string.new_title'), $r('app.string.new_short'), 'short'),
   6. // app.string.new_long 资源文件中的value值为'这是第二条长新闻，内容较多，可以自由滑动查看完整内容。'
   7. new News('3', $r('app.string.new_title'), $r('app.string.new_long'), 'long'),
   8. new News('4', $r('app.string.new_title'), $r('app.string.new_short'), 'short'),
   9. new News('5', $r('app.string.new_title'), $r('app.string.new_long'), 'long'),
   10. ];
   ```

   [SupportSlidingHand.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/SupportSlidingHand.ets#L40-L51)
3. 滑动离手事件onWillStopDragging及新闻处理逻辑：

   * 上报离手瞬间滑动速度，支持正负方向速度检测，向上滑动为正，向下滑动为负。

     ```
     1. .onWillStopDragging((velocity: number) => {
     2. if (velocity < 0) {
     3. // 向下滑动处理
     4. } else {
     5. // 向上滑动处理
     6. }
     7. // ...
     8. })
     ```

     [SupportSlidingHand.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/SupportSlidingHand.ets#L100-L150)
   * 通过[getItemRect](../harmonyos-references/ts-container-scroll.md#getitemrect11)接口方法获取当前项位置信息。

     ```
     1. let rect = this.scrollerForList.getItemRect(this.currentIndex);
     ```

     [SupportSlidingHand.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/SupportSlidingHand.ets#L121-L123)
   * 处理短新闻：直接跳转相邻项。

     ```
     1. if (velocity > 10) {
     2. this.scrollerForList.scrollToIndex(this.currentIndex, true, ScrollAlign.START)
     3. } else if (velocity < -10) {
     4. this.scrollerForList.scrollToIndex(this.currentIndex + 1, true, ScrollAlign.START)
     5. }
     ```

     [SupportSlidingHand.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/SupportSlidingHand.ets#L110-L116)
   * 处理长新闻：计算剩余显示范围决定滚动终点。

     ```
     1. let rect = this.scrollerForList.getItemRect(this.currentIndex);
     2. if (velocity < -30) {
     3. if (rect) {
     4. // 当前节点在页面内的剩余显示范围
     5. let leftRect = rect.y + rect.height;
     6. // 终点位置
     7. let mainPosition = -velocity * DEFAULT_FRICTION / FRICTION_SCALE;
     8. if (leftRect + mainPosition > 0.75 * this.listHeight) {
     9. this.scrollerForList.scrollToIndex(this.currentIndex + 1, true, ScrollAlign.START);
     10. return;
     11. } else if (leftRect + mainPosition < 0.25 * this.listHeight) {
     12. this.scrollerForList.scrollToIndex(this.currentIndex, true, ScrollAlign.END,
     13. { extraOffset: LengthMetrics.vp(this.listHeight * 0.3) })
     14. return;
     15. }
     16. }
     17. } else if (velocity > 30) {
     18. let leftRect = rect?.y + rect?.height;
     19. let mainPosition = velocity * DEFAULT_FRICTION / FRICTION_SCALE;
     20. if (leftRect + mainPosition > 0.75 * this.listHeight) {
     21. this.scrollerForList.scrollToIndex(this.currentIndex, true, ScrollAlign.START);
     22. return;
     23. }
     24. }
     ```

     [SupportSlidingHand.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/list/SupportSlidingHand.ets#L120-L147)

## 设置边缘滑动效果

边缘滑动效果是指当用户滑动滚动组件至边缘后，继续滑动时触发的交互效果。当前List支持通过[edgeEffect](../harmonyos-references/ts-container-list.md#edgeeffect)属性设置三种边缘滑动效果，分别为弹簧效果（即回弹效果）、阴影效果、无效果。具体效果说明请参见[EdgeEffect](../harmonyos-references/ts-appendix-enums.md#edgeeffect)的枚举说明。

当List组件的内容区大于等于一屏时，List的边缘滑动效果默认为回弹效果，如下图所示。

**图27** 边缘回弹效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/yoBcNyfWSRyetWfzkdKhKg/zh-cn_image_0000002583437823.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=5B3A06B66FEA0B79A5BEDCEC7AF5E7AC5C10B68FF94D9E4022F0AFF019D06CB8)

设置.edgeEffect(EdgeEffect.None)时，List无边缘滑动效果，如下图所示。

**图28** 无边缘滑动效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/RcfRxRsjRK-q0Sx0wbUnPg/zh-cn_image_0000002552957778.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=75A31EB006D6B446FEF4FFF4BC22BF0ACD3BAF02D4F5104113D51C585C72FE0A)

从API version 18开始，List还支持只设置单边的边缘滑动效果，如设置.edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true, effectEdge: EffectEdge.START })来实现起始边有边缘回弹效果，末尾边无效果，如下图所示。

**图29** 单边边缘滑动效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/b5ujIEn3TzmRInEgklqtPQ/zh-cn_image_0000002583477779.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233932Z&HW-CC-Expire=86400&HW-CC-Sign=950B072076A768BB4C7427E16B3D693D242439607186BE505AC81982F279506F)

需要注意的是，当List组件的内容区小于一屏时，List默认无边缘滑动效果。若要启用边缘回弹效果，可以通过设置.edgeEffect(EdgeEffect.Spring, { alwaysEnabled: true })来实现。

## 示例代码

* [二维列表](https://gitcode.com/HarmonyOS_Samples/two-dimension-list)
* [List组件嵌套滑动](https://gitcode.com/HarmonyOS_Samples/nested-list)
* [列表编辑效果](https://gitcode.com/HarmonyOS_Samples/list-item-edit)
