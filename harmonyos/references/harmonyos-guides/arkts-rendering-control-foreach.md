---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach
title: ForEach：循环渲染
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:44b9e3997c5f2905d391c3eb0932fedbb526e007a63ab2e11760cf68516a7ee8
---

ForEach接口基于数组循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。例如，ListItem组件要求ForEach的父容器组件必须为[List组件](../harmonyos-references/ts-container-list.md)。

API参数说明见：[ForEach API参数说明](../harmonyos-references/ts-rendering-control-foreach.md)。

说明

从API version 9开始，该接口支持在ArkTS卡片中使用。

## 键值生成规则

在ForEach循环渲染过程中，系统会为每个数组元素生成一个唯一且持久的键值，用于标识对应的组件。当键值变化时，ArkUI框架会视为该数组元素已被替换或修改，并会基于新的键值创建一个新的组件。

ForEach提供了一个名为keyGenerator的参数，这是一个函数，开发者可以通过它自定义键值的生成规则。如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即(item: Object, index: number) => { return index + '\_\_' + JSON.stringify(item); }。

ArkUI框架对于ForEach的键值生成有一套特定的判断规则，这主要与itemGenerator函数和keyGenerator函数的第二个参数index有关。具体的键值生成规则判断逻辑如下图所示。

**图1** ForEach键值生成规则

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/p7ikXq3FQsuVYcxQpo8Hrw/zh-cn_image_0000002552957644.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=6FA1729BE5FF050F3222FFDC2D72AC9C414035AD7C5178D53C3AABF6FA2C64AA)

说明

1. ArkUI框架会对重复的键值发出运行时警告。在UI更新时，如果出现重复的键值，框架可能无法正常工作，具体请参见[渲染结果非预期](arkts-rendering-control-foreach.md#渲染结果非预期)。
2. 不建议在键值中包含数据项索引index，这可能会导致[渲染结果非预期](arkts-rendering-control-foreach.md#渲染结果非预期)和[渲染性能降低](arkts-rendering-control-foreach.md#渲染性能降低)。
3. 如果开发者在itemGenerator函数中声明了index参数，但未在keyGenerator函数中声明index参数，框架会在keyGenerator函数返回值的基础上拼接index，作为最终的键值，这将会引发上述第二点中的问题。为避免此现象，请在keyGenerator函数中声明index参数。

键值生成示例:

```
1. interface ChildItemType {
2. str: string;
3. num: number;
4. }

6. @Entry
7. @Component
8. struct Index {
9. @State simpleList: Array<ChildItemType> = [
10. { str: 'one', num: 1 },
11. { str: 'two', num: 2 },
12. { str: 'three', num: 3 }
13. ];

15. build() {
16. Row() {
17. Column() {
18. ForEach(this.simpleList, (item: ChildItemType, index: number) => {
19. ChildItem({ str: item.str, num: index }) // 组件生成函数中使用index参数
20. }, (item: ChildItemType, index: number) => {
21. return item.str; // 建议在键值生成函数中使用与UI界面相关的数据属性str
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. .height('100%')
28. .backgroundColor(0xF1F3F5)
29. }
30. }

32. @Component
33. struct ChildItem {
34. @Prop str: string = '';
35. @Prop num: number = 0;

37. build() {
38. Text(this.str)
39. .fontSize(50)
40. }
41. }
```

在上述示例中，当组件生成函数声明index时，建议键值生成函数也声明index参数，以避免渲染性能降低和渲染结果非预期。同时建议在键值生成函数实现中使用与UI相关的数据属性，在本示例中，数据属性str与UI界面显示相关，因此建议将其作为键值生成函数的返回值。

## 组件创建规则

在确定键值生成规则后，ForEach的第二个参数itemGenerator函数会根据键值生成规则为数据源的每个数组项创建组件。组件的创建包括两种情况：[ForEach首次渲染](arkts-rendering-control-foreach.md#首次渲染)和[ForEach非首次渲染](arkts-rendering-control-foreach.md#非首次渲染)。

### 首次渲染

在ForEach首次渲染时，会根据前述键值生成规则为数据源的每个数组项生成唯一键值，并创建相应的组件。

```
1. @Entry
2. @Component
3. struct ForEachFirstRender {
4. @State simpleList: Array<string> = ['one', 'two', 'three'];

6. build() {
7. Row() {
8. Column() {
9. ForEach(this.simpleList, (item: string) => {
10. ForEachChildItem({ item: item })
11. }, (item: string) => item) // 需要保证key唯一
12. }
13. .width('100%')
14. .height('100%')
15. }
16. .height('100%')
17. .backgroundColor(0xF1F3F5)
18. }
19. }

21. @Component
22. struct ForEachChildItem {
23. @Prop item: string;

25. build() {
26. Text(this.item)
27. .fontSize(50)
28. }
29. }
```

[ForEach1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/ForEach1.ets#L16-L48)

运行效果如下图所示。

**图2** ForEach数据项不存在相同键值案例首次渲染运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/hh2FMjapQ76JthZkedOUOw/zh-cn_image_0000002583477645.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=CB92D65ACC3DA468805F627E7360F3E7EC2B19B3B19483047186198853E355D4)

在上述代码中，keyGenerator函数的返回值是item。在ForEach渲染循环时，为数组项依次生成键值one、two和three，并创建对应的ForEachChildItem组件渲染到界面上。

当不同数组项生成的键值相同时，框架的行为是未定义的。例如，在以下代码中，ForEach渲染相同的数据项two时，只创建了一个SameKeyChildItem组件，而没有创建多个具有相同键值的组件。

```
1. @Entry
2. @Component
3. struct ForEachSameKey {
4. @State simpleList: Array<string> = ['one', 'two', 'two', 'three'];

6. build() {
7. Row() {
8. Column() {
9. ForEach(this.simpleList, (item: string) => {
10. SameKeyChildItem({ item: item })
11. }, (item: string) => item)
12. }
13. .width('100%')
14. .height('100%')
15. }
16. .height('100%')
17. .backgroundColor(0xF1F3F5)
18. }
19. }

21. @Component
22. struct SameKeyChildItem {
23. @Prop item: string;

25. build() {
26. Text(this.item)
27. .fontSize(50)
28. }
29. }
```

[ForEach2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/ForEach2.ets#L16-L46)

运行效果如下图所示。

**图3** ForEach数据源存在相同值案例首次渲染运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Vrj-3UuQRLuDtOiI5jFSvg/zh-cn_image_0000002552797996.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=0785FDFF300634C72984D2B8B6DC35BE7AD884C651D80C98114602652AADE867)

在该示例中，最终键值生成规则为item。当ForEach遍历数据源simpleList，遍历到索引为1的two时，创建键值为two的组件并记录。当遍历到索引为2的two时，当前项的键值也为two，此时不再创建新的组件。

### 非首次渲染

在ForEach组件进行非首次渲染时，它会检查新生成的键值是否在上次渲染中已经存在。如果键值不存在，则会创建一个新的组件；如果键值存在，则不会创建新的组件，而是直接渲染该键值所对应的组件。例如，在以下的代码示例中，通过点击事件修改了数组的第三项值为"new three"，这将触发ForEach组件进行非首次渲染。

```
1. @Entry
2. @Component
3. struct ForEachNotFirstRender {
4. @State simpleList: Array<string> = ['one', 'two', 'three'];

6. build() {
7. Row() {
8. Column() {
9. Text('Click to change the value of the third array item')
10. .fontSize(24)
11. .fontColor(Color.Red)
12. .onClick(() => {
13. this.simpleList[2] = 'new three';
14. })

16. ForEach(this.simpleList, (item: string) => {
17. NotFirstRenderChildItem({ item: item })
18. .margin({ top: 20 })
19. }, (item: string) => item)
20. }
21. .justifyContent(FlexAlign.Center)
22. .width('100%')
23. .height('100%')
24. }
25. .height('100%')
26. .backgroundColor(0xF1F3F5)
27. }
28. }

30. @Component
31. struct NotFirstRenderChildItem {
32. @Prop item: string;

34. build() {
35. Text(this.item)
36. .fontSize(30)
37. }
38. }
```

[ForEach3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/ForEach3.ets#L16-L55)

运行效果如下图所示。

**图4** ForEach非首次渲染案例运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/lHN6MTGsSQCt2Q-DPqd8eQ/zh-cn_image_0000002583437691.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=79B6DD1796D3390A7DC296C57BF50BD576C6FC7D5D69391EFACFC849468CA057)

从本例可以看出[@State](arkts-state.md)能够监听到简单数据类型数组simpleList数组项的变化。

1. 当simpleList数组项发生变化时，会触发ForEach重新渲染。
2. ForEach遍历新的数据源['one', 'two', 'new three']，并生成对应的键值one、two和new three。
3. 其中，键值one和two在上次渲染中已经存在，所以 ForEach 复用了对应的组件并进行了渲染。对于第三个数组项 "new three"，由于其通过键值生成规则 item 生成的键值new three在上次渲染中不存在，因此 ForEach 为该数组项创建了一个新的组件。

## 使用场景

ForEach组件在开发过程中的主要应用场景包括：[数据源不变](arkts-rendering-control-foreach.md#数据源不变)、[数据源数组项发生变化](arkts-rendering-control-foreach.md#数据源数组项发生变化)（如插入、删除操作）、[数据源数组项子属性变化](arkts-rendering-control-foreach.md#数据源数组项子属性变化)。

### 数据源不变

在数据源保持不变的场景中，数据源可以直接采用基本数据类型。例如，页面加载状态时，可以使用骨架屏列表进行渲染展示。

```
1. @Entry
2. @Component
3. struct ArticleList {
4. @State simpleList: Array<number> = [1, 2, 3, 4, 5];

6. build() {
7. Column() {
8. ForEach(this.simpleList, (item: number) => {
9. ArticleSkeletonView()
10. .margin({ top: 20 })
11. }, (item: number) => item.toString())
12. }
13. .padding(20)
14. .width('100%')
15. .height('100%')
16. }
17. }

19. @Builder
20. function textArea(width: number | Resource | string = '100%', height: number | Resource | string = '100%') {
21. Row()
22. .width(width)
23. .height(height)
24. .backgroundColor('#FFF2F3F4')
25. }

27. @Component
28. struct ArticleSkeletonView {
29. build() {
30. Row() {
31. Column() {
32. textArea(80, 80)
33. }
34. .margin({ right: 20 })

36. Column() {
37. textArea('60%', 20)
38. textArea('50%', 20)
39. }
40. .alignItems(HorizontalAlign.Start)
41. .justifyContent(FlexAlign.SpaceAround)
42. .height('100%')
43. }
44. .padding(20)
45. .borderRadius(12)
46. .backgroundColor('#FFECECEC')
47. .height(120)
48. .width('100%')
49. .justifyContent(FlexAlign.SpaceBetween)
50. }
51. }
```

[ArticleSkeletonView.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/ArticleSkeletonView.ets#L16-L68)

运行效果如下图所示。

**图5** 骨架屏运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/fBimHY3RSJ69Luikc_nJ4g/zh-cn_image_0000002552957646.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=CBAA8618F990B4F4D1338BFF2542089D34D57A21AD03D9F75A01602B9C78533E)

在本示例中，采用数据项item作为键值生成规则，由于数据源simpleList的数组项各不相同，因此能够保证键值的唯一性。

### 数据源数组项发生变化

在数据源数组项发生变化的场景下，如数组插入、删除操作或者数组项索引位置交换时，数据源应为对象数组类型，并使用对象的唯一ID作为键值。

```
1. class ArticleChangeSource {
2. public id: string;
3. public title: string;
4. public brief: string;

6. constructor(id: string, title: string, brief: string) {
7. this.id = id;
8. this.title = title;
9. this.brief = brief;
10. }
11. }

13. @Entry
14. @Component
15. struct ArticleListViewChangeSource {
16. isListReachEnd: boolean = false;
17. @State articleList: Array<ArticleChangeSource> = [
18. new ArticleChangeSource('001', 'Article 1', 'Abstract'),
19. new ArticleChangeSource('002', 'Article 2', 'Abstract'),
20. new ArticleChangeSource('003', 'Article 3', 'Abstract'),
21. new ArticleChangeSource('004', 'Article 4', 'Abstract'),
22. new ArticleChangeSource('005', 'Article 5', 'Abstract'),
23. new ArticleChangeSource('006', 'Article 6', 'Abstract')
24. ];

26. loadMoreArticles() {
27. this.articleList.push(new ArticleChangeSource('007', 'New Article', 'Abstract'));
28. }

30. build() {
31. Column({ space: 5 }) {
32. List() {
33. ForEach(this.articleList, (item: ArticleChangeSource) => {
34. ListItem() {
35. ArticleCardChangeSource({ article: item })
36. .margin({ top: 20 })
37. }
38. }, (item: ArticleChangeSource) => item.id)
39. }
40. .onReachEnd(() => {
41. this.isListReachEnd = true;
42. })
43. .parallelGesture(
44. PanGesture({ direction: PanDirection.Up, distance: 80 })
45. .onActionStart(() => {
46. if (this.isListReachEnd) {
47. this.loadMoreArticles();
48. this.isListReachEnd = false;
49. }
50. })
51. )
52. .padding(20)
53. .scrollBar(BarState.Off)
54. }
55. .width('100%')
56. .height('100%')
57. .backgroundColor(0xF1F3F5)
58. }
59. }

61. @Component
62. struct ArticleCardChangeSource {
63. @Prop article: ArticleChangeSource;

65. build() {
66. Row() {
67. // 此处'app.media.startIcon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
68. Image($r('app.media.startIcon'))
69. .width(80)
70. .height(80)
71. .margin({ right: 20 })

73. Column() {
74. Text(this.article.title)
75. .fontSize(20)
76. .margin({ bottom: 8 })
77. Text(this.article.brief)
78. .fontSize(16)
79. .fontColor(Color.Gray)
80. .margin({ bottom: 8 })
81. }
82. .alignItems(HorizontalAlign.Start)
83. .width('80%')
84. .height('100%')
85. }
86. .padding(20)
87. .borderRadius(12)
88. .backgroundColor('#FFECECEC')
89. .height(120)
90. .width('100%')
91. .justifyContent(FlexAlign.SpaceBetween)
92. }
93. }
```

[ArticleListView.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/ArticleListView.ets#L16-L110)

初始运行效果（左图）和手势上滑加载后效果（右图）如下图所示。

**图6** 数据源数组项变化案例运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/LDdlRcqPStqXDciInGgY6w/zh-cn_image_0000002583477647.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=0E1C4FF6543B91AA55129E6CE7E8C3FA703FAD71E24A7975799C8752F1AB2141)

在本示例中，ArticleCardChangeSource组件作为ArticleListViewChangeSource组件的子组件，通过[@Prop](arkts-prop.md)装饰器接收一个ArticleChangeSource对象，用于渲染文章卡片。

1. 当列表滚动到底部且手势滑动距离超过80vp时，触发loadMoreArticles()函数。此函数在articleList数据源尾部添加新数据项，增加数据源长度。
2. 数据源被@State装饰器修饰，ArkUI框架能够感知数据源长度的变化并触发ForEach进行重新渲染。

### 数据源数组项子属性变化

当数据源的数组项为对象数据类型，并且只修改某个数组项的属性值时，由于数据源为复杂数据类型，ArkUI框架无法监听到@State装饰器修饰的数据源数组项的属性变化，从而无法触发ForEach的重新渲染。为实现ForEach子组件重新渲染，需要结合[@Observed和@ObjectLink](arkts-observed-and-objectlink.md)装饰器使用。例如，在文章列表卡片上点击“点赞”按钮，从而修改文章的点赞数量。

```
1. @Observed
2. class ArticleChangeChild {
3. public id: string;
4. public title: string;
5. public brief: string;
6. public isLiked: boolean;
7. public likesCount: number;

9. constructor(id: string, title: string, brief: string, isLiked: boolean, likesCount: number) {
10. this.id = id;
11. this.title = title;
12. this.brief = brief;
13. this.isLiked = isLiked;
14. this.likesCount = likesCount;
15. }
16. }

18. @Entry
19. @Component
20. struct ArticleListChangeView {
21. @State articleList: Array<ArticleChangeChild> = [
22. new ArticleChangeChild('001', 'Article 0', 'Abstract', false, 100),
23. new ArticleChangeChild('002', 'Article 1', 'Abstract', false, 100),
24. new ArticleChangeChild('003', 'Article 2', 'Abstract', false, 100),
25. new ArticleChangeChild('004', 'Article 4', 'Abstract', false, 100),
26. new ArticleChangeChild('005', 'Article 5', 'Abstract', false, 100),
27. new ArticleChangeChild('006', 'Article 6', 'Abstract', false, 100),
28. ];

30. build() {
31. List() {
32. ForEach(this.articleList, (item: ArticleChangeChild) => {
33. ListItem() {
34. ArticleCardChangeChild({
35. article: item
36. })
37. .margin({ top: 20 })
38. }
39. }, (item: ArticleChangeChild) => item.id)
40. }
41. .padding(20)
42. .scrollBar(BarState.Off)
43. .backgroundColor(0xF1F3F5)
44. }
45. }

47. @Component
48. struct ArticleCardChangeChild {
49. @ObjectLink article: ArticleChangeChild;

51. handleLiked() {
52. this.article.isLiked = !this.article.isLiked;
53. this.article.likesCount = this.article.isLiked ? this.article.likesCount + 1 : this.article.likesCount - 1;
54. }

56. build() {
57. Row() {
58. // 此处'app.media.startIcon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
59. Image($r('app.media.startIcon'))
60. .width(80)
61. .height(80)
62. .margin({ right: 20 })

64. Column() {
65. Text(this.article.title)
66. .fontSize(20)
67. .margin({ bottom: 8 })
68. Text(this.article.brief)
69. .fontSize(16)
70. .fontColor(Color.Gray)
71. .margin({ bottom: 8 })

73. Row() {
74. // 此处app.media.iconLiked'，'app.media.iconUnLiked'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
75. Image(this.article.isLiked ? $r('app.media.iconLiked') : $r('app.media.iconUnLiked'))
76. .width(24)
77. .height(24)
78. .margin({ right: 8 })
79. Text(this.article.likesCount.toString())
80. .fontSize(16)
81. }
82. .onClick(() => this.handleLiked())
83. .justifyContent(FlexAlign.Center)
84. }
85. .alignItems(HorizontalAlign.Start)
86. .width('80%')
87. .height('100%')
88. }
89. .padding(20)
90. .borderRadius(12)
91. .backgroundColor('#FFECECEC')
92. .height(120)
93. .width('100%')
94. .justifyContent(FlexAlign.SpaceBetween)
95. }
96. }
```

[ArticleListView2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/ArticleListView2.ets#L16-L113)

上述代码的初始运行效果（左图）和点击第1个文章卡片上的点赞图标后的运行效果（右图）如下图所示。

**图7** 数据源数组项子属性变化案例运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/TpZbrrXeS2K_ndTFZaU52w/zh-cn_image_0000002552797998.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=47FE7E7F4DACC892A7DA7B5F8AD662F11E01BE2B27C55A7A537C408D86C0B832)

在本示例中，ArticleChangeChild类被@Observed装饰器修饰。父组件ArticleListChangeView传入ArticleChangeChild对象实例给子组件ArticleCardChangeChild，子组件使用@ObjectLink装饰器接收该实例。

1. 当点击第1个文章卡片上的点赞图标时，会触发ArticleCardChangeChild组件的handleLiked函数。该函数修改第1个卡片对应组件里ArticleChangeChild实例的isLiked和likesCount属性值。
2. ArticleChangeChild实例是@ObjectLink装饰的状态变量，其属性值变化，会触发ArticleCardChangeChild组件渲染，此时读取的isLiked和likesCount为修改后的新值。

### 拖拽排序

在List组件下使用ForEach，并设置[onMove](../harmonyos-references/ts-universal-attributes-drag-sorting.md#onmove)事件，每次迭代生成一个ListItem时，可以使能拖拽排序。拖拽排序离手后，如果组件位置发生变化，将触发onMove事件，上报组件移动原始索引号和目标索引号。在onMove事件中，需要根据上报的起始索引号和目标索引号修改数据源。数据源修改前后，要保持每个数据的键值不变，只是顺序发生变化，才能保证落位动画正常执行。

```
1. @Entry
2. @Component
3. struct ForEachSort {
4. @State arr: Array<string> = [];

6. build() {
7. Column() {
8. // 点击此按钮会触发ForEach重新渲染
9. Button('Add one item')
10. .onClick(() => {
11. this.arr.push('10');
12. })
13. .width(300)
14. .margin(10)

16. List() {
17. ForEach(this.arr, (item: string) => {
18. ListItem() {
19. Text(item.toString())
20. .fontSize(16)
21. .textAlign(TextAlign.Center)
22. .size({ height: 100, width: '100%' })
23. }.margin(10)
24. .borderRadius(10)
25. .backgroundColor('#FFFFFFFF')
26. }, (item: string) => item)
27. .onMove((from: number, to: number) => {
28. // 以下两行代码是为了确保拖拽后屏幕上组件的顺序与数组arr中每一项的顺序保持一致。
29. // 若注释以下两行，第一步拖拽排序，第二步在arr末尾插入一项，触发ForEach渲染，此时屏上组件的顺序会跟数组arr中每一项的顺序一致，而不是维持第一步拖拽后的顺序，意味着拖拽排序在ForEach渲染后失效了。
30. let tmp = this.arr.splice(from, 1);
31. this.arr.splice(to, 0, tmp[0]);
32. })
33. }
34. .width('100%')
35. .height('100%')
36. .backgroundColor('#FFDCDCDC')
37. }
38. }

40. aboutToAppear(): void {
41. for (let i = 0; i < 10; i++) {
42. this.arr.push(i.toString());
43. }
44. }
45. }
```

[ForEachSort.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/ForEachSort.ets#L16-L62)

**图8** ForEach拖拽排序效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/yrv6WbWHRw2foKWLo6eLAg/zh-cn_image_0000002583437693.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=6412296E0E9F390C63127822509E91CAC37DF994CD5CF2719A084AEFC509DB67)

注释掉onMove事件调用中的两行代码，点击Add one item触发渲染后的效果如下图所示。

**图9** ForEach拖拽排序效果在重新渲染后没有保留

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/pic_58o2TNi_zOnrzaDfrA/zh-cn_image_0000002552957648.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=0D67D0CF26328A6940CC2849EAA1F85CE97890B7031994F777F13492BB78DB8C)

## 使用建议

* 为满足键值的唯一性，对于对象数据类型，建议使用对象数据中的唯一id作为键值。
* 不建议在键值中包含数据项索引index，可能会导致[渲染结果非预期](arkts-rendering-control-foreach.md#渲染结果非预期)和[渲染性能降低](arkts-rendering-control-foreach.md#渲染性能降低)。如果确实需要使用index，例如列表通过index进行条件渲染，开发者需接受ForEach在数据源变更后重新创建组件导致的性能损耗。
* 基本类型数组的数据项没有唯一ID属性。如果使用数据项作为键值，必须确保数据项无重复。对于数据源会变化的场景，建议将基本类型数组转换为具有唯一ID属性的Object类型数组，再使用唯一ID属性作为键值。
* 对于以上限制规则，index参数存在的意义为：index是开发者保证键值唯一性的最终手段；对数据项进行修改时，由于itemGenerator中的item参数是不可修改的，所以须用index索引值对数据源进行修改，进而触发UI重新渲染。
* ForEach在滚动容器组件 [List](../harmonyos-references/ts-container-list.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[Swiper](../harmonyos-references/ts-container-swiper.md)以及[WaterFlow](../harmonyos-references/ts-container-waterflow.md) 内使用的时候，不建议与[LazyForEach](arkts-rendering-control-lazyforeach.md) 同时使用。
* 在大量子组件的场景下，ForEach可能会导致卡顿。请考虑使用[LazyForEach](arkts-rendering-control-lazyforeach.md)替代。最佳实践请参考[使用懒加载优化性能](../best-practices/bpta-lazyforeach-optimization.md)。
* 当数组项为对象类型时，不建议用内容相同的数组项替换旧项。若数组项发生变更但键值未变，会导致[数据变化不渲染](arkts-rendering-control-foreach.md#数据变化不渲染)。

## 常见问题

对ForEach键值的错误使用会导致功能和性能问题。详见案例[渲染结果非预期](arkts-rendering-control-foreach.md#渲染结果非预期)和[渲染性能降低](arkts-rendering-control-foreach.md#渲染性能降低)。

### 渲染结果非预期

在本示例中，通过设置ForEach的第三个参数KeyGenerator函数，自定义键值生成规则为数据源的索引index的字符串类型值。当点击父组件ForEachAbnormal中“Insert Item After First Item”文本组件后，界面会出现非预期的结果。

```
1. @Entry
2. @Component
3. struct ForEachAbnormal {
4. @State simpleList: Array<string> = ['one', 'two', 'three'];

6. build() {
7. Column() {
8. Button() {
9. Text('Insert Item After First Item').fontSize(30)
10. }
11. .onClick(() => {
12. this.simpleList.splice(1, 0, 'new item');
13. })

15. ForEach(this.simpleList, (item: string) => {
16. ForEachAbnormalChildItem({ item: item })
17. }, (item: string, index: number) => index.toString())
18. }
19. .justifyContent(FlexAlign.Center)
20. .width('100%')
21. .height('100%')
22. .backgroundColor(0xF1F3F5)
23. }
24. }

26. @Component
27. struct ForEachAbnormalChildItem {
28. @Prop item: string;

30. build() {
31. Text(this.item)
32. .fontSize(30)
33. }
34. }
```

[AbnormalExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/AbnormalExample.ets#L16-L51)

上述代码的初始渲染效果和点击“在第1项后插入新项”文本组件后的渲染效果如下图所示。

**图10** 渲染结果非预期运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/6Mu_HEWkR9CKMTjVt1oZ6Q/zh-cn_image_0000002583477649.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=21C7A4F55AA7A50073B02A35EFD15E252895C4B57BD6041C31D1BEA539A30C2B)

ForEach在首次渲染时，创建的键值依次为"0"、"1"、"2"。

插入新项后，数据源simpleList变为['one', 'new item', 'two', 'three']，框架监听到@State装饰的数据源长度变化触发ForEach重新渲染。

ForEach依次遍历新数据源，遍历数据项"one"时生成键值"0"，存在相同键值，因此不创建新组件。继续遍历数据项"new item"时生成键值"1"，存在相同键值，因此不创建新组件。继续遍历数据项"two"生成键值"2"，存在相同键值，因此不创建新组件。最后遍历数据项"three"时生成键值"3"，不存在相同键值，创建内容为"three"的新组件并渲染。

从以上可以看出，当键值包含数据项索引index时，期望的界面渲染结果为['one', 'new item', 'two', 'three']，而实际的渲染结果为['one', 'two', 'three', 'three']，不符合开发者预期。因此，开发者在使用ForEach时应避免键值包含索引index。

### 渲染性能降低

在本示例中，ForEach的第三个参数KeyGenerator函数缺省。根据上述[键值生成规则](arkts-rendering-control-foreach.md#键值生成规则)，此例使用框架默认的键值，即最终键值为字符串index + '\_\_' + JSON.stringify(item)。点击文本组件“在第1项后插入新项”后，ForEach将为第2个数组项及后面的所有数据项重新创建组件。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const TAG = '[Sample_RenderingControl]';
3. const DOMAIN = 0xF811;

5. @Entry
6. @Component
7. struct ReducedRenderingPerformance {
8. @State simpleList: Array<string> = ['one', 'two', 'three'];

10. build() {
11. Column() {
12. Button() {
13. Text('Insert Item After First Item').fontSize(30)
14. }
15. .onClick(() => {
16. this.simpleList.splice(1, 0, 'new item');
17. hilog.info(DOMAIN, 'testTag', '[onClick]: simpleList is [${this.simpleList.join(', ')}]');
18. })

20. ForEach(this.simpleList, (item: string) => {
21. ReducedChildItem({ item: item })
22. })
23. }
24. .justifyContent(FlexAlign.Center)
25. .width('100%')
26. .height('100%')
27. .backgroundColor(0xF1F3F5)
28. }
29. }

31. @Component
32. struct ReducedChildItem {
33. @Prop item: string;

35. aboutToAppear() {
36. hilog.info(DOMAIN, TAG, '[aboutToAppear]: item is ${this.item}');
37. }

39. build() {
40. Text(this.item)
41. .fontSize(50)
42. }
43. }
```

[BadPerformance.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/BadPerformance.ets#L16-L60)

以上代码的初始渲染效果和点击"Insert Item After First Item"文本组件后的渲染效果如下图所示。

**图11** 渲染性能降低案例运行效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/FzqifsSMQoqr5CVa1Xx4kw/zh-cn_image_0000002552798000.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=44D8FE4EECE1E13EB2CA20F1920A348EFF9E9E99EDC59D5424DA49BAA6409632)

点击“Insert Item After First Item”文本组件后，DevEco Studio的日志打印结果如下所示。

**图12** 渲染性能降低案例日志打印图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/JOnNZoMbQ1ydptCIft_EZA/zh-cn_image_0000002583437695.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=C07E288DCD441FC419D1AF2B2BC023CC680229F77188AF1E7B89D04984949B33)

插入新项后，ForEach为new item、 two、 three三个数组项创建了对应的ReducedChildItem组件，并执行了组件的[aboutToAppear()](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)生命周期函数。这是因为：

1. ForEach首次渲染时，生成的键值依次为0\_\_one、1\_\_two和2\_\_three。
2. 插入新项后，数据源simpleList变为['one', 'new item', 'two', 'three']，ArkUI框架监听到@State装饰的数据源长度变化触发ForEach重新渲染。
3. ForEach依次遍历新数据源，遍历数据项one时生成键值0\_\_one，键值已存在，因此不创建新组件。继续遍历数据项new item时生成键值1\_\_new item，不存在相同键值，创建内容为new item的新组件并渲染。继续遍历数据项two生成键值2\_\_two，不存在相同键值，创建内容为two的新组件并渲染。最后遍历数据项three时生成键值3\_\_three，不存在相同键值，创建内容为three的新组件并渲染。

尽管本例中界面渲染结果符合预期，但在每次向数组中间插入新数组项时，ForEach会为该数组项及其后面的所有数组项重新创建组件。当数据源数据量较大或组件结构复杂时，组件无法复用会导致性能下降。因此，不建议省略第三个参数KeyGenerator函数，也不建议在键值中使用数据项索引index。

正确渲染并保证效率的ForEach写法是：

```
1. ForEach(this.simpleList, (item: string) => {
2. ForEachChildItem({ item: item })
3. }, (item: string) => item) // 需要保证key唯一
```

[ForEach1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/ForEach1.ets#L25-L29)

提供了第三个参数KeyGenerator，在这个例子中，对数据源的不同数据项生成不同的key，并且对同一个数据项每次生成相同的key。

### 数据变化不渲染

点击按钮Like/UnLike first article，第一个组件会切换点赞手势和后面的点赞数量，但是点击按钮Replace first article之后再点击按钮Like/UnLike first article就不生效了。原因是替换articleList[0]之后，articleList状态变量发生变化，触发ForEach重新渲染，但是新的articleList[0]生成的key没有变，ForEach不会将数据更新同步给子组件，因此第一个组件仍然绑定旧的articleList[0]。新articleList[0]的属性发生变更，第一个组件感知不到，不会重新渲染。点击点赞手势，会触发渲染。因为变更的是跟组件绑定的数组项的属性，组件会感知并重新渲染。

```
1. @Observed
2. class ArticleChangeData {
3. public id: string;
4. public title: string;
5. public brief: string;
6. public isLiked: boolean;
7. public likesCount: number;

9. constructor(id: string, title: string, brief: string, isLiked: boolean, likesCount: number) {
10. this.id = id;
11. this.title = title;
12. this.brief = brief;
13. this.isLiked = isLiked;
14. this.likesCount = likesCount;
15. }
16. }

18. @Entry
19. @Component
20. struct ArticleListChangeData {
21. @State articleList: Array<ArticleChangeData> = [
22. new ArticleChangeData('001', 'Article 0', 'Abstract', false, 100),
23. new ArticleChangeData('002', 'Article 1', 'Abstract', false, 100),
24. new ArticleChangeData('003', 'Article 2', 'Abstract', false, 100),
25. new ArticleChangeData('004', 'Article 4', 'Abstract', false, 100),
26. new ArticleChangeData('005', 'Article 5', 'Abstract', false, 100),
27. new ArticleChangeData('006', 'Article 6', 'Abstract', false, 100),
28. ];

30. build() {
31. Column() {
32. Button('Replace first article')
33. .onClick(() => {
34. this.articleList[0] = new ArticleChangeData('001', 'Article 0', 'Abstract', false, 100);
35. })
36. .width(300)
37. .margin(10)

39. Button('Like/Unlike first article')
40. .onClick(() => {
41. this.articleList[0].isLiked = !this.articleList[0].isLiked;
42. this.articleList[0].likesCount =
43. this.articleList[0].isLiked ? this.articleList[0].likesCount + 1 : this.articleList[0].likesCount - 1;
44. })
45. .width(300)
46. .margin(10)

48. List() {
49. ForEach(this.articleList, (item: ArticleChangeData) => {
50. ListItem() {
51. ArticleCardChangeData({
52. article: item
53. })
54. .margin({ top: 20 })
55. }
56. }, (item: ArticleChangeData) => item.id)
57. }
58. .padding(20)
59. .scrollBar(BarState.Off)
60. .backgroundColor(0xF1F3F5)
61. }
62. }
63. }

65. @Component
66. struct ArticleCardChangeData {
67. @ObjectLink article: ArticleChangeData;

69. handleLiked() {
70. this.article.isLiked = !this.article.isLiked;
71. this.article.likesCount = this.article.isLiked ? this.article.likesCount + 1 : this.article.likesCount - 1;
72. }

74. build() {
75. Row() {
76. // 此处'app.media.startIcon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
77. Image($r('app.media.startIcon'))
78. .width(80)
79. .height(80)
80. .margin({ right: 20 })

82. Column() {
83. Text(this.article.title)
84. .fontSize(20)
85. .margin({ bottom: 8 })
86. Text(this.article.brief)
87. .fontSize(16)
88. .fontColor(Color.Gray)
89. .margin({ bottom: 8 })

91. Row() {
92. // 此处app.media.iconLiked'，'app.media.iconUnLiked'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
93. Image(this.article.isLiked ? $r('app.media.iconLiked') : $r('app.media.iconUnLiked'))
94. .width(24)
95. .height(24)
96. .margin({ right: 8 })
97. Text(this.article.likesCount.toString())
98. .fontSize(16)
99. }
100. .onClick(() => this.handleLiked())
101. .justifyContent(FlexAlign.Center)
102. }
103. .alignItems(HorizontalAlign.Start)
104. .width('80%')
105. .height('100%')
106. }
107. .padding(20)
108. .borderRadius(12)
109. .backgroundColor('#FFECECEC')
110. .height(120)
111. .width('100%')
112. .justifyContent(FlexAlign.SpaceBetween)
113. }
114. }
```

[ArticleListView3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/ArticleListView3.ets#L16-L131)

**图13** 数据变化不渲染

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/Y0cgXcTIRdGacQCY6EMmbA/zh-cn_image_0000002552957650.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=92A953D064A86EB4138469FD197A018FE8BF2D70EA3883F87EBD36E46E36F495)

### 非必要内存消耗

如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即(item: Object, index: number) => { return index + '\_\_' + JSON.stringify(item); }。当item是复杂对象时，将其JSON序列化会得到长字符串，占用更多的内存。

```
1. class MemoryData {
2. public longStr: string;
3. public key: string;

5. constructor(longStr: string, key: string) {
6. this.longStr = longStr;
7. this.key = key;
8. }
9. }

11. @Entry
12. @Component
13. struct NonNecessaryMemory {
14. @State simpleList: Array<MemoryData> = [];

16. aboutToAppear(): void {
17. let longStr = '';
18. for (let i = 0; i < 2000; i++) {
19. longStr += i.toString();
20. }
21. for (let index = 0; index < 3000; index++) {
22. let data: MemoryData = new MemoryData(longStr, 'a' + index.toString());
23. this.simpleList.push(data);
24. }
25. }

27. build() {
28. List() {
29. ForEach(this.simpleList, (item: MemoryData) => {
30. ListItem() {
31. Text(item.key)
32. }
33. }
34. // 如果不定义下面的keyGenerator函数，则ArkUI框架会使用默认的键值生成函数
35. , (item: MemoryData) => {
36. return item.key;
37. }
38. )
39. }.height('100%')
40. .width('100%')
41. }
42. }
```

[NonNecessaryMem.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/NonNecessaryMem.ets#L16-L59)

对比自定义keyGenerator函数和使用默认键值生成函数两种情况下的内存占用（通过DevEco->Profiler->Realtime Monitor工具，可以获取相关进程的内存数据）。自定义keyGenerator函数，这个示例代码的内存占用降低了约70MB。

**图14** 使用默认键值生成函数下的内存占用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/LGY6EPgAQm-41nansevqJw/zh-cn_image_0000002583477651.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=23AC840E86865E12A1EAE876651227962F2E64EB1A5C9092FEE0BE3A8521E0F2)

**图15** 自定义键值生成函数下的内存占用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/G6ZkfJgQRRSATP6v039hBA/zh-cn_image_0000002552798002.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=854658CCC4E63EABE4E2F215D0269C2E1DC0E2775A6F8915B618EE988FD49F0D)

### 键值生成失败

如果开发者没有定义keyGenerator函数，则ArkUI框架会使用默认的键值生成函数，即(item: Object, index: number) => { return index + '\_\_' + JSON.stringify(item); }。然而，JSON.stringify序列化在某些数据结构上会失败，导致应用发生jscrash并退出。例如，bigint无法被JSON.stringify序列化：

```
1. class KeyData {
2. public content: bigint;

4. constructor(content: bigint) {
5. this.content = content;
6. }
7. }

9. @Entry
10. @Component
11. struct GenerationKeyExample {
12. @State simpleList: Array<KeyData> = [new KeyData(1234567890123456789n), new KeyData(2345678910987654321n)];

14. build() {
15. Row() {
16. Column() {
17. ForEach(this.simpleList, (item: KeyData) => {
18. GenerationKeyChildItem({ item: item.content.toString() })
19. }
20. // 如果不定义下面的keyGenerator函数，则ArkUI框架会使用默认的键值生成函数
21. // KeyData中的content: bigint在JSON序列化时失败
22. , (item: KeyData) => item.content.toString()
23. )
24. }
25. .width('100%')
26. .height('100%')
27. }
28. .height('100%')
29. .backgroundColor(0xF1F3F5)
30. }
31. }

33. @Component
34. struct GenerationKeyChildItem {
35. @Prop item: string;

37. build() {
38. Text(this.item)
39. .fontSize(50)
40. }
41. }
```

[CrashNormalExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/RenderingControl/entry/src/main/ets/pages/RenderingForeach/CrashNormalExample.ets#L16-L58)

开发者定义keyGenerator函数，应用正常启动：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/V_MLbo4fSK2IJkMFmDB3fQ/zh-cn_image_0000002583437697.png?HW-CC-KV=V1&HW-CC-Date=20260427T233923Z&HW-CC-Expire=86400&HW-CC-Sign=F42D569B515AB1C96232F7BE4A99A662C5A1ECA212E9D68F964D713320CE5915)

使用默认的键值生成函数，应用发生jscrash：

```
1. Error message:@Component 'Parent'[4]: ForEach id 7: use of default id generator function not possible on provided data structure. Need to specify id generator function (ForEach 3rd parameter). Application Error!
2. Stacktrace:
3. ...
4. at anonymous (entry/src/main/ets/pages/Index.ets:18:52)
```
