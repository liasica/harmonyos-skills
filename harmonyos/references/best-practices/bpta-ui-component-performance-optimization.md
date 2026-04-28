---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ui-component-performance-optimization
title: UI组件性能优化
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 界面渲染性能优化 > UI组件性能优化
category: best-practices
scraped_at: 2026-04-28T08:22:28+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:ea0e525d15fb68a8378730c13d4c54b6c10020b1908210ae2bdcc726734c4ef4
---

应用启动到UI页面展示过程包含框架初始化、页面加载和布局渲染三个步骤。其中页面加载和布局渲染的主要流程如下：

**图1** 页面首次加载过程流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/gJw67nzCSGun_28mEO8d7A/zh-cn_image_0000002229336857.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=9F91DDDF35D375AEC660F82F260B5983B1D5A815B31FE33D350414762B943CCA "点击放大")

* 在执行页面文件时，前端UI描述会在后端创建相应的FrameNode节点树。该树主要用于处理UI组件属性更新、布局测算、事件处理。每个树节点和前端UI组件是一一对应的关系。
* FrameNode节点树生成之后，根节点开始创建布局任务。该任务遍历所有子节点并创建子节点的布局包装任务。布局包装任务包括执行相关测算和布局任务。
* 布局包装任务完成后，每个FrameNode将创建相应的渲染包装任务并进行内容绘制。

可以看到，应用启动后页面加载和渲染的性能与FrameNode树上的节点数量以及每个节点上的属性相关。因此，为缩短页面加载和布局渲染时长，在前端使用UI组件时可以考虑以下优化方案：

* 避免在自定义组件的生命周期内执行高耗时操作：自定义组件创建后在渲染前会调用其生命周期回调函数，若函数中包含高耗时操作将阻塞UI渲染，将增加主线程负担。
* 按需注册组件属性：后端在创建FrameNode节点树时，对于组件上注册的每个属性也会保存在FrameNode节点上，包括渲染类属性集合（如颜色）和布局类属性集合（如长宽，对齐方式）。在FrameNode执行布局包装任务和渲染包装任务时，属性集合将作为输入参与。因此，在应用开发中应按需注册组件属性，避免设置冗余属性。
* 使用@Builder函数代替自定义组件：前端定义的每一个自定义组件都会在后端FrameNode节点树上创建一对一的CustomNode类型的节点。CustomNode类作为FrameNode的子类，用于处理自定义组件相关业务逻辑。当在页面上大量使用自定义组件时，会成倍增加FrameNode节点树上CustomNode类型的节点数量，增加页面创建和渲染时长。因此，在满足业务需求的前提下，可以优先使用@Builder函数代替自定义组件。
* 合理使用布局容器组件：ArkUI提供了一系列布局容器组件用于开发者快速搭建页面，具体可参考[构建布局](../harmonyos-guides/arkts-build-layout.md)。不同的业务场景应选择合适的布局容器组件，并合理使用该组件的特性功能可以有效缩短页面布局时长。

## 避免在自定义组件的生命周期内执行高耗时操作

**图2** 自定义组件生命周期流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/JP6YKJOvROShk7hs2rssow/zh-cn_image_0000002229451353.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=D5783EAB6058A903BACF778E45F96FFE1318856DE5E5038B9C991CC39C612836 "点击放大")

如上图所示，自定义组件创建完成之后，在build函数执行之前，将先执行aboutToAppear()生命周期回调函数。此时若在该函数中执行耗时操作，将阻塞UI渲染，增加UI主线程负担。因此，应尽量避免在自定义组件的生命周期内执行高耗时操作。对于复杂计算的耗时场景，可以将计算结果进行缓存处理。对于不需要等待结果的高耗时任务，可以采用多线程处理该任务，通过并发的方式避免主线程阻塞。在aboutToAppear()生命周期函数内建议只做当前组件的初始化逻辑，其他业务逻辑可以按需提前或延后处理。假设在首页视频列表中的子组件内需要初始化创建一个复杂播放器对象，该对象的创建非常耗时。若在该组件的aboutToAppear()函数中创建该对象，当首页加载渲染时，列表内每个子组件的渲染都将等待相应的播放器对象初始化创建完成，此时页面加载将非常耗时甚至可能出现白屏。伪代码如下:

**反例**

```
1. @Component
2. export struct VideoCard {
3. // ...
4. aboutToAppear(): void {
5. // Create a complex object task, if the task takes 1s to execute, the component will be rendered again after 1s
6. this.createComplexVideoPlayer();
7. }
8. // ...
9. }

11. @Component
12. export struct CardList {
13. @State videoList: VideoItem[] = getVideoList();

15. build() {
16. List() {
17. ForEach(this.videoList, (item: VideoItem) => {
18. ListItem() {
19. VideoCard({ item })
20. }
21. }, (item: VideoItem) => item.id)
22. }
23. }
24. }
```

[segment.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/UI_Component_Performance_Optimization/entry/src/main/ets/segment/segment.ets#L25-L59)

对于该场景，可以考虑将创建播放器对象任务的时机延后。如，计算当前组件出现在页面中的位置，当子组件滑动到页面的三分之一处时再创建播放器对象并播放视频。此时，页面首次渲染时，不会出现主线程阻塞。示例代码如下：

**正例**

```
1. @Component
2. export struct VideoCard {
3. @State isVideoInit: boolean = false;
4. // ...
5. build() {
6. Column() {
7. // Video Playback Component
8. }
9. .onAreaChange((old, newValue) => {
10. if (!this.isVideoInit) {
11. let positionY: number = newValue.position.y as number
12. if (positionY < screenHeight / 3) {
13. this.createComplexVideoPlayer();
14. this.isVideoInit = true;
15. }
16. }
17. })
18. }
19. // ...
20. }

22. @Component
23. export struct CardList {
24. @State videoList: VideoItem[] = getVideoList();

26. build() {
27. List() {
28. ForEach(this.videoList, (item: VideoItem) => {
29. ListItem() {
30. VideoCard({ item })
31. }
32. }, (item: VideoItem) => item.id)
33. }
34. }
35. }
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/UI_Component_Performance_Optimization/entry/src/main/ets/segment/segment2.ets#L27-L67)

例如在生命周期aboutToAppear中应该避免使用[@ohos.resourceManager (资源管理)](../harmonyos-references/js-apis-resource-manager.md)的getXXXSync接口入参中直接使用资源信息，推荐使用资源id作为入参，推荐用法为：resourceManager.getStringSync($r('app.string.test').id)。 下面以[getStringSync](../harmonyos-references/js-apis-resource-manager.md#getstringsync10)为例，测试一下这两种参数在方法中的使用是否会有耗时区别。

**反例**

```
1. import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. @State message: string = 'getStringSync';
9. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

11. aboutToAppear(): void {
12. hiTraceMeter.startTrace('getStringSync', 1);
13. // The input parameter of the getStringSync interface uses the resource directly, without using the resource ID.
14. try {
15. this.context.resourceManager.getStringSync($r('app.string.app_name'));
16. } catch (error) {
17. let err = error as BusinessError;
18. hilog.warn(0x000, 'testTag', `getStringSync failed, code=${err.code}, message=${err.message}`);
19. }
20. hiTraceMeter.finishTrace('getStringSync', 1);
21. }

23. build() {
24. RelativeContainer() {
25. Text(this.message)
26. .fontSize(50)
27. .fontWeight(FontWeight.Bold)
28. }
29. .height('100%')
30. .width('100%')
31. }
32. }
```

[segment3.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/UI_Component_Performance_Optimization/entry/src/main/ets/segment/segment3.ets#L17-L49)

可以通过[冷启动分析：Launch分析](../harmonyos-guides/ide-launch-overview.md)工具抓取Trace，根据hiTraceMeter性能打点，查看耗时为1.956ms。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/5edF_Xu7RKu39XgT3T3tNQ/zh-cn_image_0000002193851480.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=3D35BD85E9632996885631CE7ADFDF8592F543B0210977614BB5A95D22ABE5D3 "点击放大")

**正例**

```
1. import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. @State message: string = 'getStringSyncAfter';

11. aboutToAppear(): void {
12. hiTraceMeter.startTrace('getStringSyncAfter', 2);
13. // The input parameter of the getStringSync interface uses the resource ID.
14. try {
15. this.context.resourceManager.getStringSync($r('app.string.app_name').id);
16. } catch (error) {
17. let err = error as BusinessError;
18. hilog.warn(0x000, 'testTag', `getStringSync failed, code=${err.code}, message=${err.message}`);
19. }
20. hiTraceMeter.finishTrace('getStringSyncAfter', 2);
21. }

23. build() {
24. RelativeContainer() {
25. Text(this.message)
26. .fontSize(50)
27. .fontWeight(FontWeight.Bold)
28. }
29. .height('100%')
30. .width('100%')
31. }
32. }
```

[segment4.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/UI_Component_Performance_Optimization/entry/src/main/ets/segment/segment4.ets#L17-L49)

可以通过[冷启动分析：Launch分析](../harmonyos-guides/ide-launch-overview.md)工具抓取Trace，根据hiTraceMeter性能打点，查看耗时为0.071ms。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/Wly0lLjLTzqmt4n3fktxfg/zh-cn_image_0000002229451345.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=DAAF7CC5C687CE901C2FC3BF77967C8A7B37D819B30D126CB1761E2913868F27 "点击放大")

**表1** 耗时统计

| 写法 | 耗时情况 |
| --- | --- |
| 资源信息为参数：getStringSync($r('app.string.app\_name')) | 1.956ms |
| 资源ID为参数：getStringSync($r('app.string.app\_name').id) | 0.071ms |

可得出结论：参数为资源信息时比参数为资源ID值时耗时更多。所以当需要使用类似方法时，使用资源ID值作为参数更优，可有效减少自定义组件生命周期耗时。

## 按需注册组件属性

在使用组件开发应用UI界面时，会为每个组件设置属性，进行UI样式、行为等逻辑处理。当应用中单个组件设置了大量属性且该组件在应用中被大量使用时，单个组件的设置对应用的整体性能会产生较大影响。比如，在RN框架开发中，单个组件需要设置21个属性，且该组件在ForEach循环中使用。在该场景下，由于不知道应用实际需要使用哪些属性，因此把所有的属性通过属性方法的方式设置到组件上。而在实际使用中，大部分应用只会用到其中很少的几个属性，其他属性均维持默认值，这导致了大量属性的冗余设置。该场景示例代码片段如下：

```
1. build() {
2. Stack() {
3. this.renderChildren()
4. }
5. .width(this.descriptor.layoutMetrics.frame.size.width)
6. .height(this.descriptor.layoutMetrics.frame.size.height)
7. .backgroundColor(convertColorSegmentsToString(this.descriptor.props.backgroundColor))
8. .position({ y: this.descriptor.layoutMetrics.frame.origin.y, x: this.descriptor.layoutMetrics.frame.origin.x })
9. .borderWidth(this.descriptor.props.borderWidth)
10. .borderColor({
11. left: convertColorSegmentsToString(this.descriptor.props.borderColor.left),
12. top: convertColorSegmentsToString(this.descriptor.props.borderColor.top),
13. right: convertColorSegmentsToString(this.descriptor.props.borderColor.right),
14. bottom: convertColorSegmentsToString(this.descriptor.props.borderColor.bottom)
15. })
16. .borderRadius(this.descriptor.props.borderRadius)
17. .borderStyle(this.getBorderStyle())
18. .opacity(this.getOpacity())
19. .transform(this.descriptor.props.transform != undefined ? convertMatrixArrayToMatrix4(this.descriptor.props.transform) : undefined)
20. .clip(this.getClip())
21. .hitTestBehavior(this.getHitTestMode())
22. .shadow(this.getShadow())
23. }
```

[segment9.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/UI_Component_Performance_Optimization/entry/src/main/ets/segment/segment9.ets#L47-L69)

从该场景中可以看到，在应用开发中，当注册了大量冗余属性的组件需要在视图上批量展示时对性能有较大影响。此时，可以考虑采用[动态属性设置](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)动态注册组件属性的方式，替换使用属性方法静态注册组件属性的方式。

使用AttributeModifier动态注册组件属性相比于直接在组件上使用属性方法静态注册组件属性，主要存在以下两点区别：

* 动态注册属性：系统提供AttributeModifier接口，支持开发者自定义AttributeModifier接口的实现类。 当应用运行时，系统调用AttributeModifier接口的实现类中与组件样式相关的方法，在该方法内按照开发者自定义的业务逻辑动态设置组件属性。
* Diff更新属性：当组件创建或者更新时，重新执行组件的样式属性对象的更新接口。属性Diff逻辑基于Map实现，其中key值是属性类型，value值是属性修改器对象。更新场景下，通过key找到对应的属性修改器对象进行Diff对比，若有更新变化再通知native侧进行属性更新。

以一个简单的公共头像组件为例演示AttributeModifier方案的性能收益。公共头像组件要求对于有用户头像的数据，界面展示用户头像图片。对于没有用户头像的数据，界面展示灰色背景和用户名的第一个字符。现列表展示1000个头像组件，界面效果如下：

**图3** 表格展示头像组件界面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/6BgJR3fqToa-arTo2iGk0Q/zh-cn_image_0000002193851484.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=3D874AD3FCA19EB5F324253C1A227C9A670E39194011D62AC270C51E657D77F4 "点击放大")

使用属性方法的方式给头像组件设置属性，代码如下：

```
1. import { util } from '@kit.ArkTS';

3. @Observed
4. class User {
5. id: string;
6. name: string;
7. avatarImage: ResourceStr;

9. constructor(id: string, name: string, avatarImage: ResourceStr) {
10. this.id = id;
11. this.name = name;
12. this.avatarImage = avatarImage;
13. }
14. }

16. //create data
17. const DEFAULT_BACKGROUND_COLOR = Color.Grey;
18. const getUsers = () => {
19. return Array.from(Array(1000), (item: User, i: number) => {
20. return new User(
21. util.generateRandomUUID(),
22. i % 2 === 0 ? '张三' : '李四',
23. i % 2 === 0 ? '' : $r('app.media.startIcon')
24. );
25. });
26. }

28. @Component
29. export struct AvatarGrid {
30. @State users: User[] = getUsers();

32. build() {
33. Grid() {
34. ForEach(this.users, (u: User) => {
35. GridItem() {
36. Avatar({ user: u })
37. }
38. }, (user: User) => user.id)
39. }
40. .columnsTemplate('1fr 1fr 1fr 1fr 1fr 1fr')
41. .columnsGap(4)
42. .rowsGap(4)
43. }
44. }

46. // Avatar component
47. @Component
48. struct Avatar {
49. @ObjectLink user: User;

51. build() {
52. Row() {
53. if (!this.user.avatarImage) {
54. Text(this.user.name.charAt(0))
55. .fontSize(28)
56. .fontColor(Color.White)
57. .fontWeight(FontWeight.Bold)
58. }
59. }
60. .backgroundImage(this.user.avatarImage)
61. .backgroundImageSize(ImageSize.Cover)
62. .backgroundColor(DEFAULT_BACKGROUND_COLOR)
63. .justifyContent(FlexAlign.Center)
64. .size({ width: 50, height: 50 })
65. .borderRadius(25)

67. // .padding(2)
68. // .margin(2)
69. // .opacity(1)
70. // .clip(false)
71. // .layoutWeight(1)
72. // .backgroundBlurStyle(BlurStyle.NONE)
73. // .alignItems(VerticalAlign.Center)
74. // .borderWidth(1)
75. // .borderColor(Color.Pink)
76. // .borderStyle(BorderStyle.Solid)
77. // .expandSafeArea([SafeAreaType.SYSTEM])
78. // .rotate({angle: 5})
79. // .responseRegion({x: 0})
80. // .mouseResponseRegion({x: 0})
81. // .constraintSize({minWidth: 25})
82. // .hitTestBehavior(HitTestMode.Default)
83. // .backgroundImagePosition(Alignment.Center)
84. // .foregroundBlurStyle(BlurStyle.NONE)
85. }
86. }
```

[segment5.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/UI_Component_Performance_Optimization/entry/src/main/ets/segment/segment5.ets#L17-L103)

将方案改为采用AttributeModifier动态注册属性的方式，需要新增自定义类实现AttributeModifier接口，并修改Avatar组件的属性注册逻辑。具体改动代码如下：

```
1. // 1.Custom Attribute Modifier, this class implements the AttributeModifier interface
2. class RowModifier implements AttributeModifier<RowAttribute> {
3. private customImage: ResourceStr = '';
4. private static instance: RowModifier;

6. constructor() {
7. }

9. setCustomImage(customImage: ResourceStr) {
10. this.customImage = customImage;
11. return this;
12. }

14. // Adopting a singleton pattern avoids creating a new modifier for each component, increasing the performance overhead incurred by creating the
15. public static getInstance(): RowModifier {
16. if (!RowModifier.instance) {
17. RowModifier.instance = new RowModifier();
18. }
19. return RowModifier.instance;
20. }

22. // 2.Implement the applyNormalAttribute method of the AttributeModifier interface to customize the logic of attribute setting.
23. applyNormalAttribute(instance: RowAttribute) {
24. if (this.customImage) {
25. instance.backgroundImage(this.customImage);
26. instance.backgroundImageSize(ImageSize.Cover);
27. } else {
28. instance.backgroundColor(Color.Blue);
29. instance.justifyContent(FlexAlign.Center);
30. // instance.padding(2)
31. // instance.margin(2)
32. // instance.opacity(1)
33. // instance.clip(false)
34. // instance.layoutWeight(1)
35. // instance.backgroundBlurStyle(BlurStyle.NONE)
36. // instance.alignItems(VerticalAlign.Center)
37. // instance.borderWidth(1)
38. // instance.borderColor(Color.Pink)
39. // instance.borderStyle(BorderStyle.Solid)
40. // instance.expandSafeArea([SafeAreaType.SYSTEM])
41. // instance.rotate({ angle: 5 })
42. // instance.responseRegion({x: 0})
43. //instance.mouseResponseRegion({x: 0})
44. // instance.constraintSize({minWidth: 25})
45. // instance.hitTestBehavior(HitTestMode.Default)
46. //instance.backgroundImagePosition(Alignment.Center)
47. //instance.foregroundBlurStyle(BlurStyle.NONE)
48. }
49. instance.size({ width: 50, height: 50 });
50. instance.borderRadius(25);
51. }
52. }

55. @Component
56. struct Avatar {
57. @ObjectLink user: User;

59. build() {
60. Row() {
61. if (!this.user.avatarImage) {
62. Text(this.user.name.charAt(0))
63. .fontSize(28)
64. .fontColor(Color.White)
65. .fontWeight(FontWeight.Bold)
66. }
67. }
68. // 3.Pass a custom RowModifier class as a parameter to enable on-demand property registration
69. .attributeModifier(RowModifier.getInstance().setCustomImage(this.user.avatarImage))
70. }
71. }
```

[segment6.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/UI_Component_Performance_Optimization/entry/src/main/ets/segment/segment6.ets#L28-L99)

对于上述两种方案，逐渐增加注册的属性个数，通过DevEco Studio提供的Launch场景分析能力获取两个方案的页面加载耗时（PageRouterManager::LoadPage）和应用侧首帧耗时（First Frame - App Phase），对比如下：

**表2** 静态注册属性和动态注册属性在不同属性数量下耗时

|  | 静态注册属性 | | | | 动态注册属性 | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 注册的属性个数 | 6个 | 12个 | 18个 | 24个 | 6个 | 12个 | 18个 | 24个 |
| PageRouterManager::LoadPage | 639ms900μs | 668ms624μs | 719ms139μs | 764ms437μs | 640ms989μs | 662ms112μs | 705ms407μs | 717ms294μs |
| First Frame - App Phase | 45ms554μs | 45ms638μs | 52ms918μs | 52ms643μs | 44ms603μs | 43ms923μs | 46ms709μs | 46ms355μs |

**图4** 静态注册属性和动态注册属性在不同属性数量下LoadPage耗时  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/bd3GqQlSQ52aqhzVj7gkJw/zh-cn_image_0000002193851492.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=590AAACD7BBF0764FDA81493D3F003BA99E6D397FEC75A9A6AC039F1F2BA32D2 "点击放大")

**图5** 静态注册属性和动态注册属性在不同属性数量下First Frame - App Phase耗时  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/ooSwUmAuT4q8Mhlz-3ZOJA/zh-cn_image_0000002229451349.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=591E03A9EFEB096A6DDA78C688B390340F9846C62B56CC4574325E391D64DFE9 "点击放大")

可以看到，当注册的属性个数较少时，使用动态注册的方案收益并不明显。当注册的属性个数递增时，动态注册的收益效果同步线性递增。

## 优先使用@Builder方法代替自定义组件

在ArkUI中使用自定义组件时，在build阶段将在后端FrameNode树创建一个相应的CustomNode节点，在渲染阶段时也会创建对应的RenderNode节点，如下图所示。

**图6** 前后端UI组件树关系图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/vHNixVz5TI-xRj0Z3vtdpg/zh-cn_image_0000002229336861.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=DE14C6F4D6310EB6E8E9B42C27B0352CAF088CDDD20EC333729E70053A8F775D "点击放大")

* 前端UI描述结构会在后端创建相应的FrameNode节点树；
* FrameNode节点树主要用于处理UI组件属性更新、布局测算、事件处理等业务逻辑；
* CustomNode作为FrameNode的子类，用于处理自定义组件相关业务逻辑，比如执行build函数。
* FrameNode节点树在渲染阶段生成后端渲染树进行UI渲染。

因此，在应用开发时，减少自定义组件的使用，尤其是自定义组件在循环中的使用，将成倍减少FrameNode节点树上CustomNode节点数量，有效缩短页面的加载和渲染时长。当在应用中使用自定义组件时，可以优先考虑使用@Builder函数代替自定义组件，@Builder函数不会在后端FrameNode节点树上创建一个新的树节点。

注意

@Builder装饰器严格禁止在其内部定义状态变量[状态变量](../harmonyos-guides/arkts-state-management-glossary.md#状态变量state-variables)或使用[生命周期函数](../harmonyos-references/ts-custom-component-lifecycle.md)，必须通过参数传递或者访问所属组件的状态变量完成数据交互。

当组件仅作展示，无需使用@Component自定义组件的内部状态变量、生命周期函数时，可以创建一个@Builder函数代替创建@Component自定义组件。

例如，在使用ForEach循环展示卡片列表信息时，界面展示如下：

**图7** 卡片列表界面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/7_cdBVwjQamntikWk9hi8A/zh-cn_image_0000002194011052.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=5CE4E1DBF1BF8509E341335E9F384944D03FAE32040425E8F58C8E375700E9A2 "点击放大")

使用自定义组件方案，示例代码如下：

```
1. import { util } from '@kit.ArkTS';

3. interface User {
4. id: string;
5. name: string;
6. age?: number;
7. avatarImage?: ResourceStr;
8. //introduction: string;
9. // ...
10. }

12. // create data
13. const DEFAULT_BACKGROUND_COLOR = Color.Pink;
14. const getUsers = () => {
15. const USERS: User[] = [{
16. id: '1',
17. name: '张三',
18. }, {
19. id: '2',
20. name: '李四',
21. }, {
22. id: '3',
23. name: '王五',
24. }];
25. return Array.from(Array(30), (item: User, i: number) => {
26. return {
27. id: util.generateRandomUUID(),
28. name: USERS[i%3].name,
29. avatarImage: $r('app.media.startIcon'),
30. age: 18 + i
31. } as User;
32. });
33. }

35. // User Card List Component
36. @Component
37. export struct UserCardList {
38. @State users: User[] = getUsers();

40. build() {
41. List({ space: 8 }) {
42. ForEach(this.users, (item: User) => {
43. ListItem() {
44. UserCard({ name: item.name, age: item.age, avatarImage: item.avatarImage })
45. }
46. }, (item: User) => item.id)
47. }
48. .alignListItem(ListItemAlign.Center)
49. }
50. }

52. // User Card Customization Component
53. @Component
54. struct UserCard {
55. @Prop avatarImage: ResourceStr;
56. @Prop name: string;
57. @Prop age: number;

59. build() {
60. Row() {
61. Row() {
62. Image(this.avatarImage)
63. .size({ width: 50, height: 50 })
64. .borderRadius(25)
65. .margin(8)
66. Text(this.name)
67. .fontSize(30)
68. }
69. Text(`age：${this.age.toString()}`)
70. .fontSize(20)
71. }
72. .backgroundColor(DEFAULT_BACKGROUND_COLOR)
73. .justifyContent(FlexAlign.SpaceBetween)
74. .borderRadius(8)
75. .padding(8)
76. .height(66)
77. .width('80%')
78. }
79. }
```

[segment7.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/UI_Component_Performance_Optimization/entry/src/main/ets/segment/segment7.ets#L17-L95)

改用@Builder函数的方式代替自定义组件UserCard的方案，具体修改的代码如下:

```
1. // 1. Customizing @Builder Function Components
2. @Builder
3. function UserCardBuilder(name: string, age?: number, avatarImage?: ResourceStr) {
4. Row() {
5. Row() {
6. Image(avatarImage)
7. .size({ width: 50, height: 50 })
8. .borderRadius(25)
9. .margin(8)
10. Text(name)
11. .fontSize(30)
12. }
13. Text(`age：${age?.toString()}`)
14. .fontSize(20)
15. }
16. .backgroundColor(Color.Blue)
17. .justifyContent(FlexAlign.SpaceBetween)
18. .borderRadius(8)
19. .padding(8)
20. .height(66)
21. .width('80%')
22. }

24. @Component
25. export struct UserCardList {
26. @State users: User[] = getUsers();

28. build() {
29. List({ space: 8 }) {
30. ForEach(this.users, (item: User) => {
31. ListItem() {
32. // 2. Using the @Builder function in a build function
33. UserCardBuilder(item.name, item.age, item.avatarImage)
34. }
35. }, (item: User) => item.id)
36. }
37. .alignListItem(ListItemAlign.Center)
38. }
39. }
```

[segment8.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/UI_Component_Performance_Optimization/entry/src/main/ets/segment/segment8.ets#L28-L66)

将组件数量从30个递增到3000个，通过profiler获取页面加载标签PageRouterManager::LoadPage和页面UI刷新任务标签UITaskScheduler::FlushTask的耗时，对比两种方案的耗时如下：

**图8** 两种方案LoadPage标签耗时对比  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/x9vv7TnhQwmDw2TwHYRYvg/zh-cn_image_0000002193851476.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=FED5A70FC56F070DA32FCE256A17B699EACA4F0E3A34ADF185914B45D0B5C729 "点击放大")

**图9** 两种方案UITaskSchedule标签耗时对比  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/d1Qxc7tGSTGZmiXP5_L9cA/zh-cn_image_0000002229451369.png?HW-CC-KV=V1&HW-CC-Date=20260428T002227Z&HW-CC-Expire=86400&HW-CC-Sign=23BD3C3C430A8B6310C24A6AEF4D879C153CEBEF6738DD82FF4E7A29D37AFD88 "点击放大")

通过对比图可以看到，@Builder方案在页面加载和刷新UI页面（包括布局、渲染和动画）方面优于自定义组件方案。随着组件个数增加，收益也线性增加。

## 合理使用布局容器组件

对于需要展示大量组件的场景，通常会使用布局容器组件，以达到快速实现页面布局的需求。在使用布局容器组件时，由于一次需要展示多个组件，可能出现首帧耗时过长甚至掉帧问题。此时可以考虑对容器组件内的子组件进行按需加载或懒加载等处理，对于相同结构的组件也可以使用组件复用能力。针对每个布局容器组件的性能优化可以参考[布局优化指导](bpta-improve-layout-performance.md)。

## 示例代码

* [UI组件性能优化同源示例代码](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/ArkUI/UI_Component_Performance_Optimization)
