---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-list-based-on-scrollcomponents
title: 基于ScrollComponents实现长列表
breadcrumb: 最佳实践 > 布局与弹窗 > 基于ScrollComponents实现长列表
category: best-practices
scraped_at: 2026-04-29T14:10:33+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:1650d83d08ea4f8ec6a9e5b9a7a4c096fd8eac457fd9b4bbdbe1240f165def3e
---

## 概述

列表包含一系列相同宽度的列表项，适合连续、多行展示同类数据，例如图片和文本。List具备动态数据处理能力，可以循环生成列表项，适应数据变化。它采用滚动加载技术，仅渲染可视项目，从而提升长列表的性能。同时，支持自定义交互逻辑与视觉样式，以满足多样化的交互需求。其使用场景广泛，涵盖列表类信息展示（如新闻、商品清单）、导航菜单设计（底部导航、侧边栏）及分页长内容呈现（如社交媒体动态、评论区），是实现高效数据可视化与交互的核心组件。

当长列表上下滑动时，频繁的子组件创建和测量会大量消耗计算资源，容易造成滑动卡顿。图片等资源的短时集中请求会造成明显的页面滑动白块，影响用户体验。

ScrollComponents作为高性能滑动解决方案，主要解决组件复用问题，支持通过少量的代码实现高性能滑动场景开发，同时开发者无需关注复用池管理和其他性能优化方案的交互细节。可以参考[ScrollComponents使用说明](https://gitcode.com/openharmony-sig/scroll_components/blob/master/README.md#快速开始)进行安装配置与快速上手。ScrollComponents三方库提供了下列功能特性：

* 支持List，WaterFlow，Grid 三种常见复杂页面的流畅滑动
* 默认支持懒加载
* 支持组件复用，解决滑动丢帧，提升滑动性能
* 支持复用池共享，满足跨页面跨父组件复用能力
* 支持预创建，减少冷启首次滑动丢帧，提升滑动性能
* 支持预加载，滑动过程提前加载数据，提升浏览体验

ScrollComponents三方库基于系统[NodeAdapter](../harmonyos-references/js-apis-arkui-framenode.md#nodeadapter12)、[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md)、[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)、[Prefetcher](../harmonyos-references/js-apis-arkui-prefetcher.md)、[FrameCallback](../harmonyos-references/arkts-apis-uicontext-framecallback.md)的能力，通过高效的组件复用、分帧预创建组件、动态内容预创建和懒加载等技术，实现了高性能的滑动效果。此外，它还基于FrameNode封装了系统List、WaterFlow、Grid组件，提供了一系列ViewManager，为开发者提供了多种系统滑动组件的能力，如列表项样式设置、首尾偏移量调整、滚动监听、边缘渐隐等，旨在简化开发流程的同时满足开发者的常规需求。

下文将通过长列表的跨页面复用、加速首屏渲染、无限滑动、下拉刷新、上拉加载等场景，详细介绍ScrollComponents库在长列表组件中的应用。

## 实现原理

### 关键技术

ScrollComponents三方库底层封装了NodeContainer+FrameNode，结合NodeAdapter、BuildNode和自定义复用池实现懒加载、组件复用、组件预创建等功能。同时，它为开发者提供了WaterFlowManager、ListManager、GridManager等视图管理组件，以支持系统滑动组件的其他各种能力。在满足开发者正常开发需求的前提下，提供高性能的滑动能力，只需传入数据源和viewManager即可快速实现懒加载和组件复用的开发，使开发者能够更加专注于业务实现。

如下图所示，当节点从可视区域移除时，NodeAdapter会通知视图管理器回收组件，经NodeFactory处理后，组件最终被存入复用池。当需要创建节点时，NodeAdapter通知视图管理器开始创建，NodeFactory会从复用池请求复用节点，获取节点后经过一系列更新和组件拼接，最后由NodeAdapter将节点添加到可视区域。

**图1** RecyclerView整体流程图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/jZbZExB5SmOIb3HEzz7fhA/zh-cn_image_0000002356692034.png?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=EDB995D17746035035D8D3E13248C864E15D672C9F4A7E8CC8E7479E75F49B81 "点击放大")

### 开发流程

1. 创建长列表视图管理器。

   ListManager仅具备基础的视图功能。若开发者需要使用组件复用功能，需定义一个继承自ListManager的类，并实现onWillCreateItem()方法，从复用池中获取组件，以开启复用能力。具体实现可参考[复用子节点模板](bpta-list-based-on-scrollcomponents.md#li18448145318540)。

   在创建视图管理器的实例对象时，defaultNodeItem属性用于指定默认的列表项模板名称，通常传入唯一标识字符串用于组件复用；context属性用于获取UI上下文，通常传入this.getUIContext()。

   ```
   1. import { ListManager, NodeItem, RecyclerView } from '@hadss/scroll_components';
   2. @Component
   3. struct SameItemListPage {
   4. myListManager: MyListManager = new MyListManager({
   5. defaultNodeItem: 'EasyBlogItemContainer',
   6. context: this.getUIContext()
   7. });
   8. // ...
   9. }

   11. class MyListManager extends ListManager {
   12. onWillCreateItem(_index: number, data: BlogData) {
   13. // ...
   14. }
   15. }
   ```

   [SameItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/SameItemListPage.ets#L18-L283)

   说明

   如果开发者希望通过ScrollComponents快速创建长列表，并利用懒加载、预创建等功能来提升滑动效率，而不涉及组件复用，那么可以直接使用ScrollComponents库中提供的ListManager来创建长列表视图管理器。具体的使用方法和配置选项，可以参考[ScrollComponents使用说明-快速开始](https://gitcode.com/openharmony-sig/scroll_components/blob/master/README.md#快速开始)。
2. ListManager初始化

   在页面初始化时，开发者通过视图管理器的setViewStyle接口为视图设置相应的属性。这包括设置布局与约束条件、主轴和交叉轴的方向、自定义列表样式（如内容间距、分割线、滚动条等）以及设置滚动监听。

   ```
   1. this.myListManager.setItemViewStyle((item, index, data: Params) => {
   2. item({ style: ListItemStyle.NONE })
   3. .width('100%')
   4. .height('auto')
   5. .swipeAction({
   6. // ...
   7. })
   8. .onClick(() => Logger.info("index:" + index))
   9. })
   10. this.myListManager.setViewStyle({ space: 10, scroller: this.listScroller })
   11. .cachedCount(2)// Set the number of preloaded ListItemListItemGroups in the list and whether to display the preloaded nodes
   12. .width('100%')
   13. .layoutWeight(1)
   14. .contentStartOffset(20)// Sets the offset at the start of the content area
   15. .contentEndOffset(20)// Sets the offset at the end of the content area
   16. .scrollBar(BarState.Off)// Set the scrollbar status
   17. // ...
   18. .alignListItem(ListItemAlign.Start)// Set the direction of the List cross axis
   19. .lanes(1)// Set the number of layout columns or rows in the List portlet
   20. .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })
   21. // Nested scrolling: Set up a scrolling scheme
   22. .nestedScroll({
   23. scrollForward: NestedScrollMode.PARENT_FIRST, // The parent component scrolls first, scrolls to the edge, and then scrolls itself
   24. scrollBackward: NestedScrollMode.SELF_FIRST // Itself rolls first, and then the parent component scrolls to the edge
   25. })
   ```

   [SameItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/SameItemListPage.ets#L110-L166)
3. 设置数据源渲染组件
   1. 通过视图管理器的setDataSource()方法设置数据。ScrollComponents库默认支持懒加载，提供基于懒加载的数据增删改查功能，开发者无需担心LazyForEach的使用限制，无需定义DataSource，引入即可使用。懒加载接口可参考：[基于NodeAdapter为视图管理器提供懒加载能力](https://gitcode.com/openharmony-sig/scroll_components/blob/master/docs/Reference.md#lazynodeadapter-类)。
   2. 通过视图管理器的registerNodeItem方法注册item子节点模板时，需要传入模板名称和子节点的@Builder构造函数。
   3. ScrollComponents提供了视图占位组件RecyclerView，RecyclerView通过绑定视图容器实例即可渲染长列表。

      ```
      1. import { ListManager, NodeItem, RecyclerView } from '@hadss/scroll_components';
      2. @Component
      3. struct SameItemListPage {
      4. myListManager: MyListManager = new MyListManager({
      5. defaultNodeItem: 'EasyBlogItemContainer',
      6. context: this.getUIContext()
      7. });
      8. @State myViewModel: SameItemViewModel = new SameItemViewModel(this.myListManager);
      9. // ...
      10. aboutToAppear(): void {
      11. // ...
      12. // Register a reuse template
      13. this.myListManager.registerNodeItem('EasyBlogItemContainer', wrapBuilder(EasyBlogItemContainer));
      14. // ...
      15. // Simulate request data
      16. this.myViewModel.loadData();
      17. }
      18. // ...
      19. build() {
      20. // ...
      21. Column() {
      22. RecyclerView({
      23. viewManager: this.myListManager
      24. })
      25. }
      26. // ...
      27. }
      28. }

      30. // Define an item template
      31. @Builder
      32. function EasyBlogItemContainer($$: Params) {
      33. EasyBlogItem({ blogData: $$.blogData })
      34. }
      ```

      [SameItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/SameItemListPage.ets#L17-L290)

      ```
      1. @Observed
      2. export class SameItemViewModel {
      3. @Track dataArray: BlogData[] = [];
      4. myListManager: ListManager;
      5. // ...
      6. loadData() {
      7. generateRandomBlogData(300, false).then((dataArray: BlogData[]) => {
      8. this.dataArray = dataArray;
      9. this.myListManager.setDataSource(dataArray);
      10. });
      11. }
      12. // ...
      13. }
      ```

      [SameItemViewModel.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/viewmodel/SameItemViewModel.ets#L20-L73)

   说明

   1. 在注册子节点模板的方法registerNodeItem()中，目前仅支持使用全局builder函数。

   2. 如果开发者使用this.ListView.myListManager.preCreate()来实现组件的预创建，则必须在注册节点模板之前完成此操作。
4. 复用子节点模板

   开发者自定义模板后，在定义长列表视图管理器时，需要实现onWillCreateItem()接口。在此接口中，通过dequeueReusableNodeByType()获取可复用的node，以实现组件复用。同时，还需要在复用组件的aboutToReuse生命周期中更新数据。
   1. 列表项结构类型相同

      当ListItem组件的结构相同但数据不同时，直接注册节点模板。

      ```
      1. @Component
      2. struct SameItemListPage {
      3. myListManager: MyListManager = new MyListManager({
      4. defaultNodeItem: 'EasyBlogItemContainer',
      5. context: this.getUIContext()
      6. });
      7. // ...
      8. aboutToAppear(): void {
      9. // ...
      10. // Register a reuse template
      11. this.myListManager.registerNodeItem('EasyBlogItemContainer', wrapBuilder(EasyBlogItemContainer));
      12. // ...
      13. }
      14. // ...
      15. }

      17. class MyListManager extends ListManager {
      18. onWillCreateItem(_index: number, data: BlogData) {
      19. let node: NodeItem<Params> | null = this.dequeueReusableNodeByType('EasyBlogItemContainer');
      20. node?.setData({ blogData: data });
      21. return node;
      22. }
      23. }

      25. // Define an item template
      26. @Builder
      27. function EasyBlogItemContainer($$: Params) {
      28. EasyBlogItem({ blogData: $$.blogData })
      29. }
      ```

      [SameItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/SameItemListPage.ets#L39-L291)
   2. 列表项内子组件可拆分组合

      如果复用的ListItem组件结构基本相同，但存在部分差异，例如头部和尾部组件展示相同，而中间内容可能渲染Text组件或Image组件，通常需要定义两个不同的@Builder函数来实现复用。然而，在这种场景下，ScrollComponents提供了PartReuse功能，确保组件复用的实现，只需定义一个@Builder函数。具体可参考[组件复用-列表项子组件可拆分](https://gitcode.com/openharmony-sig/scroll_components/blob/master/README.md#列表项内子组件可拆分)。

      当组件即将被销毁时，会从视图容器中移除并进入item复用池。当组件即将被创建时，会从item复用池中获取item节点。如果item节点与目标节点类型存在差异，会先将差异部分，即PartReuse中的组件回收到对应的组件复用池，然后从对应的组件复用池中取出目标组件所需的差异组件，并与item节点拼接，形成目标组件，再进入视图容器中。

      **图2** 可拆分组件复用创建流程图  
      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/QoJ0VSa6QmiQzaPISgJ0bg/zh-cn_image_0000002390372089.png?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=18BC3BBB99387B5EE54591695A28C9326392FFB9AA3D0260E15BC07119D7AB81 "点击放大")

      ```
      1. import { ListManager, NodeItem, PartReuse, RecyclerView, } from '@hadss/scroll_components';
      2. @Component
      3. struct CombineItemListPage {
      4. myListManager: MyListManager = new MyListManager({
      5. defaultNodeItem: "BlogItemContainer",
      6. context: this.getUIContext()
      7. });
      8. // ...
      9. aboutToAppear(): void {
      10. // ...
      11. // Register a reuse template
      12. this.myListManager.registerNodeItem('BlogItemContainer', wrapBuilder(BlogItemContainer));
      13. this.myListManager.registerNodeItem('AdaptiveTextComponentContainer', wrapBuilder(AdaptiveTextComponentContainer));
      14. this.myListManager.registerNodeItem('GridImageViewContainer', wrapBuilder(GridImageViewContainer));
      15. // ...
      16. }
      17. // ...
      18. }

      20. class MyListManager extends ListManager {
      21. onWillCreateItem(_index: number, data: BlogData) {
      22. let node: NodeItem<Params> | null = this.dequeueReusableNodeByType('BlogItemContainer');
      23. node?.setData({ blogData: data });
      24. return node;
      25. }
      26. }

      28. @Builder
      29. function BlogItemContainer($$: Params) {
      30. BlogItem({ blogData: $$.blogData })
      31. }

      33. @Component
      34. struct BlogItem {
      35. @State blogData: BlogData = new BlogData();

      37. aboutToReuse(params: Record<string, ESObject>): void {
      38. this.blogData = params.blogData;
      39. }

      41. build() {
      42. Column({ space: 12 }) {
      43. BlogItemHeaderView({ blogData: this.blogData })
      44. if (this.blogData?.content.length > 0) {
      45. PartReuse({
      46. type: 'AdaptiveTextComponent',
      47. builder: wrapBuilder(AdaptiveTextComponentContainer),
      48. data: { blogData: this.blogData }
      49. })
      50. }
      51. // Display pictures
      52. if (this.blogData?.images && this.blogData.images.length > 0) {
      53. PartReuse({
      54. type: 'GridImageViewContainer',
      55. builder: wrapBuilder(GridImageViewContainer),
      56. data: { blogData: this.blogData }
      57. })
      58. }
      59. BottomActionView({ blogData: this.blogData })
      60. }
      61. // ...
      62. }
      63. }

      65. @Builder
      66. function AdaptiveTextComponentContainer($$: Params) {
      67. AdaptiveTextComponent({ blogData: $$.blogData })
      68. }

      70. @Builder
      71. function GridImageViewContainer($$: Params) {
      72. GridImageView({ blogData: $$.blogData })
      73. }
      ```

      [CombineItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/CombineItemListPage.ets#L17-L222)

      开发者可以参考下图所示的日志打印内容，以检验是否成功复用，"generateItem reuse" 表示复用。

      **图3** 日志效果图  
      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/yHLRa1_hTjCICHJeOQPVxQ/zh-cn_image_0000002356851962.png?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=6D37618385F684CFF6B437AC5DBC5D3E616E809C73DDE6C80C0D3DFC6B505088 "点击放大")

      说明

      日志默认是关闭的，若需开启日志，应在ListManager的初始化方法中设置Config参数，将debug设为true。
   3. 列表项结构类型不同

      如果ListItem结构存在较大差异，包括布局不同、子组件数量差异大、组件类型不同等因素，导致难以直接复用同一个ListItem，则可以定义多个复用模板。

      ```
      1. @Component
      2. struct DifferentItemListPage {
      3. myListManager: MyListManager = new MyListManager({
      4. defaultNodeItem: 'EasyBlogItemContainer',
      5. context: this.getUIContext()
      6. });
      7. @State dataArray: BlogData[] = [];
      8. @State myViewModel: DifferentItemViewModel = new DifferentItemViewModel(this.myListManager, this.dataArray);
      9. // ...
      10. aboutToAppear(): void {
      11. // ...
      12. this.myListManager.registerNodeItem('EasyBlogItemContainer', wrapBuilder(EasyBlogItemContainer));
      13. this.myListManager.registerNodeItem('HotVideoBlogItemContainer', wrapBuilder(HotVideoBlogItemContainer));
      14. this.myListManager.preCreate('HotVideoBlogItemContainer', 30);
      15. this.myListManager.preCreate('EasyBlogItemContainer', 30);
      16. this.myViewModel.loadData();
      17. }

      19. initView() {
      20. this.myListManager.setItemViewStyle((_item, _index, _data: ESObject) => {
      21. })
      22. this.myListManager.setViewStyle({ space: 10, scroller: this.scroller })
      23. // ...
      24. }

      26. @Builder
      27. buildListView() {
      28. RecyclerView({
      29. viewManager: this.myListManager
      30. })
      31. }

      33. build() {
      34. // ...
      35. PullToRefresh({
      36. // ...
      37. customList: () => {
      38. this.buildListView();
      39. },
      40. // ...
      41. })
      42. // ...
      43. }
      44. }
      45. class MyListManager extends ListManager {
      46. onWillCreateItem(index: number, data: BlogData) {
      47. if (index % 4 === 3) {
      48. let node: NodeItem<Params> | null = this.dequeueReusableNodeByType('HotVideoBlogItemContainer');
      49. node?.setData({ blogData: data });
      50. return node;
      51. }
      52. let node: NodeItem<Params> | null = this.dequeueReusableNodeByType('EasyBlogItemContainer');
      53. node?.setData({ blogData: data });
      54. return node;
      55. }
      56. }

      58. // Reusable EasyBlog Component Template
      59. @Builder
      60. function EasyBlogItemContainer($$: Params) {
      61. EasyBlogItem({ blogData: $$.blogData })
      62. }

      64. // Reusable HotVideoBlog Component Template
      65. @Builder
      66. function HotVideoBlogItemContainer($$: Params) {
      67. HotVideoBlogItem({ blogData: $$.blogData })
      68. }
      ```

      [DifferentItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/DifferentItemListPage.ets#L34-L198)

## 长列表分组布局场景

### 场景描述

在长列表中支持数据的分组展示，可以使列表结构更加清晰，便于查找，从而提高使用效率。分组列表在实际应用中非常常见，例如下图所示的联系人列表和商品分类展示列表。

在分组场景中，通常会设置Group的header和footer，用于展示组内统一的头部和尾部信息。

**图4** 商品分类列表展示效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/TFLPmyndTt-Fkvss4zsGFg/zh-cn_image_0000002390452013.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=1E2130FA3DD618382EE99821820C491558EF48A6E1E97011D5B850ED0C63DEB0 "点击放大")

### 开发步骤

1. 定义Item复用的模板

   ```
   1. @Builder
   2. function GoodItemContainer($$: ParamsGoods) {
   3. GoodItem({ dataModel: $$.dataModel })
   4. }

   6. @Component
   7. struct GoodItem {
   8. @Prop dataModel: GoodsDataModel = {
   9. titleId: 0,
   10. goodsId: 0,
   11. goodsName: '',
   12. imgUrl: $r('app.media.pic2'),
   13. price: 0
   14. };

   16. aboutToReuse(params: Record<string, ESObject>): void {
   17. this.dataModel = params.dataModel;
   18. }

   20. build() {
   21. Row() {
   22. Image(this.dataModel.imgUrl)
   23. .height('100%')
   24. .aspectRatio(1)
   25. .sourceSize({ width: 96, height: 96})
   26. Column() {
   27. Text(this.dataModel.goodsName)
   28. .width('100%')
   29. .fontSize(14)
   30. .maxLines(2)
   31. .textOverflow({ overflow: TextOverflow.Clip })
   32. .lineHeight(20)
   33. Text('￥' + this.dataModel.price)
   34. .fontSize(18)
   35. .fontColor(Color.Red)
   36. }
   37. .height('100%')
   38. .padding(12)
   39. .layoutWeight(1)
   40. .alignItems(HorizontalAlign.Start)
   41. .justifyContent(FlexAlign.SpaceBetween)
   42. }
   43. .clip(true)
   44. .width('100%')
   45. .height(96)
   46. .backgroundColor(Color.White)
   47. .borderRadius(18)
   48. }
   49. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L342-L393)
2. 定义ListItemGroupManager类

   ```
   1. class MyListItemGroupManager extends ListItemGroupManager {
   2. onWillCreateItem(_index: number, data: GoodsDataModel): NodeItem | null {
   3. let node: NodeItem<ParamsGoods> | null = this.dequeueReusableNodeByType('GoodItemContainer');
   4. node?.setData({ dataModel: data });
   5. return node;
   6. }
   7. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L107-L123)
3. 定义ListManager类

   ```
   1. class MyListManager extends ListManager {
   2. context: UIContext;

   4. constructor(config: Config) {
   5. super(config);
   6. this.context = config.context;
   7. }

   9. onWillCreateItem(_index: number, data: CategoryModel): NodeItem {
   10. const groupManager = new MyListItemGroupManager({ defaultNodeItem: 'GoodItemContainer', context: this.context });
   11. groupManager.registerNodeItem('GoodItemContainer', wrapBuilder(GoodItemContainer));
   12. groupManager.setDataSource(data.goodsList);
   13. // The header and footer of the group
   14. groupManager.setViewStyle({
   15. space: 12,
   16. // ...
   17. })
   18. groupManager.setItemViewStyle((listItem, index, data: ParamsGoods) => {
   19. // Used to set the scratch component of ListItem.
   20. listItem().swipeAction({
   21. // ...
   22. })
   23. })
   24. return groupManager.getNodeItem(this);
   25. }
   26. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L32-L100)
4. Group的header和footer设置

   如果需要设置组头和组尾，可以通过ListItemGroupManager的headerComponent和footerComponent属性实现，并实现其对应的Builder函数。

   ```
   1. class MyListManager extends ListManager {
   2. // ...
   3. onWillCreateItem(_index: number, data: CategoryModel): NodeItem {
   4. const groupManager = new MyListItemGroupManager({ defaultNodeItem: 'GoodItemContainer', context: this.context });
   5. groupManager.registerNodeItem('GoodItemContainer', wrapBuilder(GoodItemContainer));
   6. groupManager.setDataSource(data.goodsList);
   7. // The header and footer of the group
   8. groupManager.setViewStyle({
   9. space: 12,
   10. headerComponent: new ComponentContent<Resource>(this.context,
   11. wrapBuilder<[Resource]>(goodsHeaderBuilderPublic),
   12. data.titleName),
   13. // onClick:(...)=>{} can be declared in the DataModel, and data.onClick is used when data is assigned
   14. // headerComponent: new ComponentContent<DataModel>(this.context,
   15. //   wrapBuilder<[DataModel]>(groupHeaderBuilderPublic),
   16. //   dataModel)
   17. footerComponent: new ComponentContent<[Resource, number]>(this.context,
   18. wrapBuilder<[[Resource, number]]>(goodsFooterBuilderPublic),
   19. [data.titleName, data.titleId]),
   20. })
   21. // ...
   22. return groupManager.getNodeItem(this);
   23. }
   24. }
   25. // The global Builder: passes multiple parameters
   26. @Builder
   27. function goodsHeaderBuilderPublic(headerName: Resource) {
   28. // ...
   29. }

   31. // The global Builder: passes multiple parameters
   32. @Builder
   33. function goodsFooterBuilderPublic(args: [Resource, number]) {
   34. // ...
   35. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L33-L337)

   说明

   header目前支持使用headerComponent属性的写法，且goodsHeaderBuilderPublic只支持全局builder。footer的写法与header相同。

   对于需要将内部事件传递到Page页面的场景，可以通过在DataModel中设置一个点击回调属性来实现，并在Page页面传递Data时进行赋值。

   目前这种写法不支持同时设置header和footer。后续，ScrollComponents库将支持这一功能。
5. 页面实现

   ```
   1. @Component
   2. struct GroupLayoutListPage {
   3. // ...
   4. myListManager: MyListManager = new MyListManager({ defaultNodeItem: '', context: this.getUIContext() });
   5. private goodsListScroller: ListScroller = new ListScroller();
   6. @State myViewModel: GroupLayoutViewModel = new GroupLayoutViewModel(this.myListManager, this.goodsListScroller);

   8. aboutToAppear() {
   9. this.initView();
   10. this.myListManager.registerNodeItem('GoodItemContainer', wrapBuilder(GoodItemContainer));
   11. this.myListManager.preCreate('GoodItemContainer', 30);
   12. this.myViewModel.loadData();
   13. }

   15. // ...
   16. build() {
   17. // ...
   18. Column() { // 3.Nested Scrolling: Inner List
   19. RecyclerView({
   20. viewManager: this.myListManager
   21. })
   22. }
   23. .height('100%')
   24. // ...
   25. }
   26. }

   28. // ...
   29. @Builder
   30. function GoodItemContainer($$: ParamsGoods) {
   31. GoodItem({ dataModel: $$.dataModel })
   32. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L129-L347)

## 长列表跨页面复用场景

### 场景描述

开发者可能需要在多个页面间复用List，例如在Tabs切换时。ScrollComponents提供了全局复用的能力。

**图5** Tabs组件子页面跨页面复用效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/kaYt8lgtRf-JcSriyBSKjA/zh-cn_image_0000002356692062.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=6252CB1BFDB4214BDC2EE24CEB6713A993E51D35904C5386C483718F6805412D "点击放大")

### 开发步骤

1. 定义复用池单例

   ScrollComponents默认会生成一个RecycledPool对象，通过定义复用池单例存储该pool对象，以便跨页面使用。以下单例仅做参考，开发者可根据需要自行封装。

   ```
   1. import { RecycledPool } from '@hadss/scroll_components';

   3. export class Utils {
   4. // ...
   5. private static utils_: Utils;
   6. nodePool: RecycledPool | null = null;
   7. // ...
   8. }
   ```

   [Utils.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/common/util/Utils.ets#L17-L34)
2. 复用池单例保存RecycledPool

   HMListManager提供getRecyclePool()方法可获取RecyclePool对象，然后存储到全局单例中。

   ```
   1. if (Utils.getInstance().nodePool) {
   2. this.myListManager.registerRecyclePool(Utils.getInstance().nodePool!);
   3. } else {
   4. Utils.getInstance().nodePool = this.myListManager.getRecyclePool();
   5. }
   ```

   [TabsCeilingListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/TabsCeilingListPage.ets#L212-L216)
3. 跨页面共享单例中的RecyclePool

   通过使用registerRecyclePool()接口，将全局单例中的RecyclePool注册到页面定义的List视图类对象上，实现跨页面HMRecyclerView视图的复用池共享。

   ```
   1. @Component
   2. struct TabsCeilingListPage {
   3. private tabArray: Resource[] = [
   4. // ...
   5. ];
   6. // ...
   7. aboutToDisappear(): void {
   8. Utils.getInstance().nodePool?.clear()
   9. }

   11. // ...
   12. build() {
   13. // ...
   14. Tabs({ barPosition: BarPosition.Start, controller: this.contentTabController }) {
   15. ForEach(this.tabArray, (item: Resource, index: number) => {
   16. TabContent() {
   17. CustomListPage({ index: index })
   18. }
   19. .tabBar(this.tabBuilder(index, item))
   20. .align(Alignment.Center)
   21. }, (item: string) => item)
   22. }
   23. // ...
   24. }
   25. }

   27. @Component
   28. struct CustomListPage {
   29. index: number = 1;
   30. myListManager: MyListManager = new MyListManager({
   31. defaultNodeItem: 'CustomListItemContainer',
   32. context: this.getUIContext()
   33. });
   34. @State myViewModel: TabsCeilingViewModel = new TabsCeilingViewModel(this.myListManager);
   35. scroller: Scroller = new Scroller();

   37. aboutToAppear(): void {
   38. // ...
   39. // Shared multiplexing pools
   40. if (Utils.getInstance().nodePool) {
   41. this.myListManager.registerRecyclePool(Utils.getInstance().nodePool!);
   42. } else {
   43. Utils.getInstance().nodePool = this.myListManager.getRecyclePool();
   44. }
   45. // ...
   46. this.myListManager.registerNodeItem('CustomListItemContainer', wrapBuilder(CustomListItemContainer));
   47. this.myListManager.preCreate('CustomListItemContainer', 5);
   48. this.myViewModel.loadData();
   49. }

   51. build() {
   52. RecyclerView({
   53. viewManager: this.myListManager
   54. })
   55. }
   56. }
   ```

   [TabsCeilingListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/TabsCeilingListPage.ets#L33-L239)

## 长列表加速首屏渲染场景

### 场景描述

冷启动后首次打开长列表页面时，由于页面包含大量图片或视频等媒体资源，可能会出现白屏或白块，需要等待几秒内容才会逐渐加载出来。ScrollComponents库支持组件预创建，使用后可以在打开页面后立即看到文字和图片的骨架，从而减少卡顿。

**图6** 加速首屏渲染效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/0_uRkj9XTbu6ONjL6ab25A/zh-cn_image_0000002390372125.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=1A53F5FCF4638B67612B5C5393F7F2D8DB0A4BA2C276BB4EF482871F4E411C58 "点击放大")

### 开发步骤

包括注册模板和复用模板的预创建。重点：必须在注册复用模板之后使用preCreate()接口。

```
1. aboutToAppear(): void {
2. // ...
3. // Register a reuse template
4. this.myListManager.registerNodeItem('BlogItemContainer', wrapBuilder(BlogItemContainer));
5. this.myListManager.registerNodeItem('AdaptiveTextComponentContainer', wrapBuilder(AdaptiveTextComponentContainer));
6. this.myListManager.registerNodeItem('GridImageViewContainer', wrapBuilder(GridImageViewContainer));
7. // Pre-creation Important: preCreate pre-creates a reusable template, which must be done after the reuse template is registered
8. // Pre-create 30 list items to optimize the first-screen performance; the number can be adjusted according to actual needs.
9. this.myListManager.preCreate('BlogItemContainer', 30);
10. this.myListManager.preCreate('AdaptiveTextComponentContainer', 30);
11. this.myListManager.preCreate('GridImageViewContainer', 30);
12. // ...
13. }
```

[CombineItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/CombineItemListPage.ets#L46-L74)

### 性能测试

在冷启动场景下加载相同数据的完成时延情况，通过延迟1s来模拟冷启动后的网络请求场景。

@Reusable：在网络请求期间，主线程有大段空闲时间，请求结束后首屏组件的绘帧耗时较长。

**图7** @Reusable测试结果  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/0glcZjSiSLu3zQXSpbmWZw/zh-cn_image_0000002356852002.png?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=667B5FF36323984F974940355156200FE07AE06B38838A85C7501EBF12B072E8 "点击放大")

在ScrollComponents中，网络请求期间主线程空闲时间较少，请求结束后首屏组件的绘帧耗时较短。

**图8** ScrollComponents测试结果  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/j6Q2acWPTLy-S2ganDEgtQ/zh-cn_image_0000002390452049.png?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=67D8E551C351BCBC35234E7A596A33E3EC6C00DC6C38EE6AB18E1D50B0E08D4A "点击放大")

**表1** ScrollComponents与@Reusable性能时延数据对比

|  | 冷启动完成时延 | 主线程空闲时间 | 首屏组件创建时间 |
| --- | --- | --- | --- |
| ScrollComponents | 2.5s | 281ms | 223ms |
| @Reusable | 2.8s | 997ms | 467ms |

结论：ScrollComponents在冷启动场景下，完成时延优于原生@Reusable。整体完成时延优化300ms。

## 长列表下拉刷新场景

### 场景描述

下拉刷新是提升用户体验的关键功能，它既要确保数据无缝加载，又要保持流畅的交互效果。建议采用懒加载方式刷新数据，以避免媒体资源加载导致的UI渲染阻塞。实现逻辑可参考[实现下拉刷新上拉加载更多](../harmonyos-references/ts-container-refresh.md#示例6实现下拉刷新上拉加载更多)。

**图9** 下拉刷新效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/ncJLy2_JT9eEV1eN3ShDqQ/zh-cn_image_0000002356692086.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=909E57C2304057ADAF2F1DF2739735143BEDB7D716E84446D9D0DEF5E269D345 "点击放大")

### 开发步骤

可以通过PullToRefresh组件实现页面下拉操作，并绑定显示刷新Loading动效的容器组件，以达到下拉加载的效果。之后，使用onRefresh回调重新设置数据，模拟刷新数据的操作。

```
1. @Component
2. struct DifferentItemListPage {
3. myListManager: MyListManager = new MyListManager({
4. defaultNodeItem: 'EasyBlogItemContainer',
5. context: this.getUIContext()
6. });
7. @State dataArray: BlogData[] = [];
8. @State myViewModel: DifferentItemViewModel = new DifferentItemViewModel(this.myListManager, this.dataArray);
9. // ...
10. @Builder
11. buildListView() {
12. RecyclerView({
13. viewManager: this.myListManager
14. })
15. }

17. build() {
18. // ...
19. PullToRefresh({
20. data: $dataArray,
21. scroller: this.scroller,
22. refreshConfigurator: this.refreshConfigurator,
23. customList: () => {
24. this.buildListView();
25. },
26. onRefresh: () => {
27. return new Promise<string>((resolve, _reject) => {
28. this.myViewModel.loadData((isSuccess) => {
29. // ...
30. });
31. });
32. },
33. // ...
34. })
35. // ...
36. }
37. }
```

[DifferentItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/DifferentItemListPage.ets#L35-L170)

```
1. @Observed
2. export class DifferentItemViewModel {
3. @Track dataArray: BlogData[] = [];
4. myListManager: ListManager;
5. // ...
6. loadData(callBack?: (isSuccess: boolean) => void): void {
7. generateRandomBlogData().then((data: BlogData[]) => {
8. this.dataArray = data;
9. this.myListManager.setDataSource(data);
10. if (callBack) {
11. callBack(true);
12. }
13. });
14. }
15. // ...
16. }
```

[DifferentItemViewModel.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/viewmodel/DifferentItemViewModel.ets#L20-L65)

## 长列表上拉加载场景

### 场景描述

在开发涉及大量数据的长列表页面时，需要通过分页请求来加载数据。结合ScrollComponents提供的懒加载功能，可以实现加载更多数据的效果。

**图10** 上拉加载效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/YyFZ8xu5TuGRcSZLuu-BSw/zh-cn_image_0000002390372141.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=223343B22D33E7ABEA88E21CB448BA2BBB933861805180DA82E0AF8BD459A0FB "点击放大")

### 开发步骤

可以通过PullToRefresh组件实现页面上拉操作，并绑定显示刷新Loading动效的容器组件，以达到上拉加载的效果。之后，使用onLoadMore回调来新增数据，模拟加载数据的操作。

```
1. @Component
2. struct DifferentItemListPage {
3. myListManager: MyListManager = new MyListManager({
4. defaultNodeItem: 'EasyBlogItemContainer',
5. context: this.getUIContext()
6. });
7. @State dataArray: BlogData[] = [];
8. @State myViewModel: DifferentItemViewModel = new DifferentItemViewModel(this.myListManager, this.dataArray);
9. // ...
10. @Builder
11. buildListView() {
12. RecyclerView({
13. viewManager: this.myListManager
14. })
15. }

17. build() {
18. // ...
19. PullToRefresh({
20. data: $dataArray,
21. scroller: this.scroller,
22. refreshConfigurator: this.refreshConfigurator,
23. customList: () => {
24. this.buildListView();
25. },
26. // ...
27. onLoadMore: () => {
28. return new Promise<string>((resolve) => {
29. this.myViewModel.loadDataMore((isSuccess) => {
30. // ...
31. });
32. });
33. }
34. })
35. // ...
36. }
37. }
```

[DifferentItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/DifferentItemListPage.ets#L36-L171)

```
1. @Observed
2. export class DifferentItemViewModel {
3. // ...
4. private isLoadingMore: boolean = false;
5. // ...
6. loadDataMore(callBack?: (isSuccess: boolean) => void): void {
7. if (!this.isLoadingMore) {
8. this.isLoadingMore = true;
9. setTimeout(() => {
10. generateRandomBlogData().then((data: BlogData[]) => {
11. this.myListManager.nodeAdapter.pushData(data);
12. this.isLoadingMore = false;
13. if (callBack) {
14. callBack(true);
15. }
16. })
17. }, this.NetworkTime);
18. }
19. }
20. }
```

[DifferentItemViewModel.ets](https://gitcode.com/HarmonyOS_Samples/ListScrollComponent/blob/master/entry/src/main/ets/viewmodel/DifferentItemViewModel.ets#L21-L66)

## 长列表无限滑动场景

### 场景描述

为了解决手动上拉加载操作的繁琐问题，在即将下滑到最底端时，提前触发新数据的加载，并将其显示在长列表的最底部，从而实现无限滑动的效果。

* 痛点问题：当长列表页面包含大量图片或视频时，下滑至列表底部后快速继续下滑可能会导致“滑动白块”现象。特别是在用户使用大量在线数据的情况下，弱网环境和快速滑动会使滑动过程中的白块现象更加明显。
* 解决方案：为了减少滑动过程中的白块和页面数据加载的等待时间，ScrollComponents内置了内容预取功能Prefetcher，支持根据网络状态动态自适应。通过提前下载图片或资源，确保在需要时能够立即显示，从而减少白块的出现。
* 适用场景：动态预加载特别适用于数据请求耗时较长的场景，例如滑动列表中包含大量图片资源。

以下介绍具体的使用：

**图11** 无限滑动效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/O31KegzqTx22GWNV0OODWA/zh-cn_image_0000002356852014.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=9FAAA3186CC972C244E3DE3E218A8F157E92C7A6BC21371DDB2D589E0ED41EF7 "点击放大")

### 开发步骤

1. 修改数据体参数，增加位图

   ```
   1. @Observed
   2. class ObservedArray<T> extends Array<T> {
   3. }

   5. @Observed
   6. export class ImagePixelMap {
   7. imageUrl: string = '';
   8. imagePixelMap: image.PixelMap | undefined = undefined;
   9. }

   11. @Observed
   12. export class BlogData {
   13. // ...
   14. // Multiple graphs define imagePixelMapArray, corresponding to images
   15. imagePixelMapArray: ObservedArray<ImagePixelMap> = [];
   16. // A single graph defines an imagePixelMap, which corresponds to an imageUrl
   17. // imageUrl: string = ''
   18. // imagePixelMap: image.PixelMap | undefined = undefined;

   20. callback: Function | undefined = undefined;
   21. fetchUrl: string | ImageContent = ImageContent.EMPTY;
   22. }
   ```

   [types.ets](https://gitcode.com/HarmonyOS_Samples/ListScrollComponent/blob/master/entry/src/main/ets/model/types.ets#L19-L50)
2. 实现fetchCallback()和cancelCallback()方法

   ```
   1. fetchCallback: (item: ESObject, fetchId: number) => Promise<void> = (item: ESObject, fetchId: number) => {
   2. // Simulate a simple pre-loading scenario ,This is where you can migrate the preloaded scenarios for your project
   3. // 1、When the component is not displayed or created, the image is obtained. PixelMap, when the component is displayed, load the image directly. PixelMap and show no need to wait for the network
   4. // 2、If the image is displayed but the pixelMap is not obtained, the data is bound to the Image component first, and the image can be refreshed immediately after the pixelMap is obtained
   5. let data = item as BlogData;
   6. this.fetchesMore.set(fetchId, new Map());
   7. return new Promise(resolve => {
   8. this.loadImagesInBatches(data.imagePixelMapArray, fetchId, 0, resolve);
   9. })
   10. }

   12. private loadImagesInBatches(images: ImagePixelMap[], fetchId: number, startIndex: number, resolve: () => void): void {
   13. if (startIndex >= images.length) {
   14. const fetchMap = this.fetchesMore.get(fetchId);
   15. if (fetchMap && fetchMap.size === 0) {
   16. this.fetchesMore.delete(fetchId);
   17. }
   18. resolve();
   19. return;
   20. }
   21. const batchSize = 1;
   22. const endIndex = Math.min(startIndex + batchSize, images.length);
   23. for (let i = startIndex; i < endIndex; i++) {
   24. const pixMap = images[i];
   25. if (pixMap.imagePixelMap) {
   26. continue;
   27. }
   28. let httpRequest = HttpGet(pixMap.imageUrl, (error: number, pixelMap?: image.PixelMap) => {
   29. let fetchMap = this.fetchesMore.get(fetchId);
   30. if (fetchMap) {
   31. fetchMap.delete(i);
   32. if (fetchMap?.size === 0) {
   33. this.fetchesMore.delete(fetchId);
   34. }
   35. }
   36. if (error === -1) {
   37. return;
   38. }
   39. if (pixelMap) {
   40. // You need to create an array to store the pixelMap, because there is a change in the internal data of the array to make the component respond, which is more complicated, the developer can choose the preloading scheme by himself:
   41. // Define the ImagePixelMap class to store the pixelMap, encapsulate the Image component as an ObservedImage, add @ObjectLink imagePixelMap: ImagePixelMap property to bind the data object,
   42. // In the preloaded callback fetchCallback, after the image pixelMap is obtained, set ImagePixelMap.imagePixelMap, and the image can be refreshed by ObservedImage
   43. pixMap.imagePixelMap = pixelMap;
   44. }
   45. });
   46. let fetchMap = this.fetchesMore.get(fetchId);
   47. if (fetchMap) {
   48. fetchMap.set(i, httpRequest);
   49. }
   50. }
   51. setTimeout(() => {
   52. this.loadImagesInBatches(images, fetchId, endIndex, resolve);
   53. }, 80);
   54. }

   56. cancelCallback: (fetchId: number) => void = (fetchId: number) => {
   57. const fetchMap = this.fetchesMore.get(fetchId);
   58. if (fetchMap) {
   59. Array.from(fetchMap.values()).forEach(element => {
   60. element.destroy();
   61. });
   62. fetchMap.clear();
   63. }
   64. this.fetchesMore.delete(fetchId);
   65. }
   ```

   [CombineItemViewModel.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/viewmodel/CombineItemViewModel.ets#L66-L130)
3. 创建组件实例时，注册fetch和cancel方法到视图管理器

   ```
   1. aboutToAppear(): void {
   2. this.initView();
   3. // Register a preload function callback
   4. this.myViewModel.registerPrefetch();
   5. // ...
   6. }
   ```

   [CombineItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/CombineItemListPage.ets#L44-L73)

   ```
   1. registerPrefetch() {
   2. this.myListManager?.registerFetchCallback(this.fetchCallback);
   3. this.myListManager?.registerCancelCallback(this.cancelCallback);
   4. }
   ```

   [CombineItemViewModel.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/viewmodel/CombineItemViewModel.ets#L60-L63)
4. 监听滑动组件子组件变化事件

   ```
   1. @Component
   2. struct CombineItemListPage {
   3. // ...
   4. initView() {
   5. this.myListManager.setViewStyle({ space: 10, scroller: this.scroller })
   6. // ...
   7. .onScrollIndex((start: number, end: number) => {
   8. // Infinite swipe, when the 10th data is counted, new data is requested in advance
   9. if (end > this.myViewModel.dataArray.length - 10) {
   10. this.myViewModel.loadDataMore();
   11. }
   12. // Trigger a preload callback, request an image in advance, and resolve the white block of the image
   13. if (end > 0) {
   14. this.myListManager.visibleAreaChanged(start, end);
   15. }
   16. })
   17. }
   18. // ...
   19. }
   ```

   [CombineItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/CombineItemListPage.ets#L32-L131)
5. 自定义Image组件，双向绑定数据

   ```
   1. @Component
   2. struct GridImageView {
   3. @State blogData: BlogData = new BlogData();

   5. aboutToReuse(params: Record<string, ESObject>): void {
   6. this.blogData = params.blogData;
   7. }

   9. build() {
   10. Grid() {
   11. ForEach(this.blogData.imagePixelMapArray, (image: ImagePixelMap | undefined, _index: number) => {
   12. GridItem() {
   13. Stack() {
   14. ObservedImage({ imagePixelMap: image })
   15. }
   16. }
   17. })
   18. }
   19. .columnsTemplate("1fr 1fr 1fr")
   20. .rowsGap(5)
   21. .columnsGap(5)
   22. }
   23. }

   25. @Component
   26. struct ObservedImage {
   27. @ObjectLink imagePixelMap: ImagePixelMap;

   29. build() {
   30. Image(this.imagePixelMap.imagePixelMap)
   31. .sourceSize({ width: 100, height: 100 })
   32. .width('100%')
   33. .aspectRatio(1)
   34. .objectFit(ImageFit.Cover)
   35. .borderRadius(8)
   36. }
   37. }
   ```

   [CombineItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/CombineItemListPage.ets#L225-L262)

## 长列表侧滑删除场景

### 场景描述

侧滑菜单在许多应用中十分常见。例如，在通讯类应用中，通常会为消息列表提供侧滑删除功能，即用户可以通过向左滑动列表中的某一项，然后点击删除按钮来删除消息。

**图12** 侧滑删除效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/VYf0bpIXTfKAXTpgWVu-Zg/zh-cn_image_0000002390452057.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=7C7413326A69C619E9B7F2469A69E591A32BF4FDFD38E7D3BF0A65DE9823BBA0 "点击放大")

### 开发步骤

1. 标准列表侧滑删除

   ```
   1. @Component
   2. struct SameItemListPage {
   3. // ...
   4. initView() {
   5. this.myListManager.setItemViewStyle((item, index, data: Params) => {
   6. item({ style: ListItemStyle.NONE })
   7. .width('100%')
   8. .height('auto')
   9. .swipeAction({
   10. end: { builder: () => this.ItemActionEnd(data.blogData) },
   11. start: { builder: () => this.ItemActionStart(data.blogData) },
   12. onOffsetChange: (offset: number) => Logger.info("offset:" + offset)
   13. })
   14. .onClick(() => Logger.info("index:" + index))
   15. })
   16. // ...
   17. }

   19. @Builder
   20. ItemActionStart(data: BlogData) {
   21. Row() {
   22. Text($r('app.string.collection'))
   23. // ...
   24. }
   25. // ...
   26. }

   28. @Builder
   29. ItemActionEnd(data: BlogData) {
   30. Row() {
   31. Text($r('app.string.delete'))
   32. // ...
   33. }
   34. // ...
   35. }

   37. build() {
   38. // ...
   39. Column() {
   40. RecyclerView({
   41. viewManager: this.myListManager
   42. })
   43. }
   44. // ...
   45. }
   46. }
   ```

   [SameItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/SameItemListPage.ets#L42-L269)
2. 分组列表侧滑删除

   目前ListItemGroupManage是写在ListManager内部的，侧滑组件groupManager.setItemViewStyle()需要在ListManager.onWillCreateItem()内部设置。

   ```
   1. class MyListManager extends ListManager {
   2. // ...
   3. onWillCreateItem(_index: number, data: CategoryModel): NodeItem {
   4. const groupManager = new MyListItemGroupManager({ defaultNodeItem: 'GoodItemContainer', context: this.context });
   5. groupManager.registerNodeItem('GoodItemContainer', wrapBuilder(GoodItemContainer));
   6. // ...
   7. groupManager.setItemViewStyle((listItem, index, data: ParamsGoods) => {
   8. // Used to set the scratch component of ListItem.
   9. listItem().swipeAction({
   10. end: {
   11. builderComponent: new ComponentContent<[number, GoodsDataModel, ListItemGroupManager]>(this.context,
   12. wrapBuilder<[[number, GoodsDataModel, ListItemGroupManager]]>(GroupItemActionEnd),
   13. [index, data.dataModel, groupManager]),
   14. onEnterActionArea: () => Logger.info("onEnterActionArea"),
   15. onExitActionArea: () => Logger.info("onExitActionArea"),
   16. onStateChange: (state: SwipeActionState) => Logger.info("onStateChange" + state)
   17. },
   18. start: {
   19. builderComponent: new ComponentContent<[number, GoodsDataModel]>(this.context,
   20. wrapBuilder<[[number, GoodsDataModel]]>(GroupItemActionStart),
   21. [index, data.dataModel]),
   22. },
   23. onOffsetChange: (offset: number) => Logger.info("offset:" + offset),
   24. edgeEffect: SwipeEdgeEffect.Spring,
   25. })
   26. })
   27. return groupManager.getNodeItem(this);
   28. }
   29. }
   30. class MyListItemGroupManager extends ListItemGroupManager {
   31. // ...
   32. }

   34. @Builder
   35. function GroupItemActionStart(args: [number, GoodsDataModel]) {
   36. // ...
   37. }

   39. @Builder
   40. function GroupItemActionEnd(args: [number, GoodsDataModel, ListItemGroupManager]) {
   41. // ...
   42. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L31-L452)

   说明

   swipeAction目前仅支持builderComponent属性的写法，且GroupItemActionEnd只能是全局builder。end和start的写法相同。

   对于需要将内部事件传递到Page页面的场景，可以通过在DataModel中设置一个点击回调属性来实现，并在Page页面进行数据传递时赋值。

## 长列表多类型列表项场景

### 场景描述

List组件作为整个首页长列表的容器，通过ListItem对不同模块进行视图界面的定制，常用于门户首页、商城首页等多类型视图展示的列表信息流场景。多类型列表项场景（List+ListHeaderView）参考：[常见列表流开发实践：多类型列表项场景](bpta-common-list-flows.md#section20614147618)。

**图13** ListHeaderView滑动效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/i7ZpSWe6ShSrfn2CoMh9rA/zh-cn_image_0000002356692098.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=CDB9D9E672CF4FA48E193F33417B58091EBCB65F0862B26F232DFD6645E38B0F "点击放大")

### 开发步骤

通过Scroll内部包含HeaderView+RecyclerView的方式实现，并通过nestedScroll()接口设置RecyclerView的嵌套滚动方式，来达到上图所示的效果。

```
1. @Component
2. struct GroupLayoutListPage {
3. // ...
4. initView() {
5. // ...
6. this.myListManager.setViewStyle({ space: 10, scroller: this.goodsListScroller })
7. // ...
8. .nestedScroll({
9. // 1.Nested scrolling: Set up a scrolling scheme
10. scrollForward: NestedScrollMode.PARENT_FIRST,
11. scrollBackward: NestedScrollMode.SELF_FIRST
12. })
13. }

15. // ...
16. build() {
17. // ...
18. // Nested scrolling: Implement the ListHeader effect
19. Scroll() { // 2.Nested Scroll: Outer Scroll
20. Column() {
21. ListHeaderView()
22. Column() { // 3.Nested Scrolling: Inner List
23. RecyclerView({
24. viewManager: this.myListManager
25. })
26. }
27. .height('100%')
28. }
29. }
30. .layoutWeight(1)
31. .scrollBar(BarState.Off)
32. // ...
33. }
34. }

36. @Component
37. export struct ListHeaderView {
38. build() {
39. Column() {
40. // ListHeaderView: You can set up various types of subassemblies
41. // Swiper(...){...}
42. // Grid(...){...}
43. // CustomComponent(...){...}
44. Stack({ alignContent: Alignment.Center }) {
45. Image($r('app.media.pic1'))
46. Row() {
47. Text($r('app.string.i_am'))
48. .fontSize(16)
49. .fontColor('#333')
50. Text(' ListHeaderView')
51. .fontSize(16)
52. .fontColor('#333')
53. }
54. }
55. }
56. .alignItems(HorizontalAlign.Center)
57. }
58. }
```

[GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L128-L478)

说明

在ArkUI中，可通过List内部包含HeaderView+ForEach实现。HeaderView支持添加多种类型组件以实现与List同步滑动的效果，ForEach展示具体的Item。

ScrollComponents中采用了FrameNode实现并自动管理数据源，可通过Scroll内部包含HeaderView+RecyclerView的方式实现。

## 长列表Tabs吸顶场景

### 场景描述

Tabs嵌套List的吸顶效果，常用于新闻和资讯类应用的首页。长列表Tabs吸顶功能参考：[常见列表流开发实践：Tabs吸顶场景](bpta-common-list-flows.md#section103354617711)

**图14** Tabs的TabBar吸顶效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/V_so5wrZS3-cXMZ2y9DSXA/zh-cn_image_0000002390372145.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=CDEAE04B9AA802FF4CB2D96F19226E30FDE5CB9A86B663B3DBC930467E235514 "点击放大")

### 开发步骤

1. 实现Tabs组件TabContent骨架

   ```
   1. @Component
   2. struct TabsCeilingListPage {
   3. // ...
   4. build() {
   5. // ...
   6. Column() {
   7. Tabs({ barPosition: BarPosition.Start, controller: this.contentTabController }) {
   8. ForEach(this.tabArray, (item: Resource, index: number) => {
   9. TabContent() {
   10. CustomListPage({ index: index })
   11. }
   12. .tabBar(this.tabBuilder(index, item))
   13. .align(Alignment.Center)
   14. }, (item: string) => item)
   15. }
   16. // Set the height of the tab to 'calc(100% - 63vp)' to ensure that the Tabs component leaks out just when the nest slides
   17. .height('calc(100% - 58vp)')
   18. .barHeight(56)
   19. // ...
   20. .onChange((index: number) => this.currentTabIndex = index)
   21. }
   22. .backgroundColor($r('app.color.home_background_color'))
   23. // ...
   24. }
   25. }
   ```

   [TabsCeilingListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/TabsCeilingListPage.ets#L32-L168)
2. RecyclerView实现TabContent内部List页面

   ```
   1. @Component
   2. struct CustomListPage {
   3. // ...
   4. aboutToAppear(): void {
   5. this.myListManager.setItemViewStyle((_item, _index, _data: ESObject) => {
   6. })
   7. this.myListManager.setViewStyle({ space: 10, scroller: this.scroller, })
   8. // ...
   9. }

   11. build() {
   12. RecyclerView({
   13. viewManager: this.myListManager
   14. })
   15. }
   16. }

   18. class MyListManager extends ListManager {
   19. // ...
   20. }

   22. @Builder
   23. function CustomListItemContainer($$: ParamsItemData) {
   24. CustomListItem({ itemData: $$.itemData })
   25. }
   ```

   [TabsCeilingListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/TabsCeilingListPage.ets#L173-L259)
3. 设置嵌套滚动模式

   ```
   1. @Component
   2. struct CustomListPage {
   3. // ...
   4. aboutToAppear(): void {
   5. // ...
   6. this.myListManager.setViewStyle({ space: 10, scroller: this.scroller, })
   7. // ...
   8. .nestedScroll({
   9. scrollForward: NestedScrollMode.PARENT_FIRST, // Set the effect of scrolling the component to the end: The parent component rolls first, and then rolls itself to the edge
   10. scrollBackward: NestedScrollMode.SELF_FIRST // Set the effect of rolling the component to the start end: Rolls itself first, and then the parent component scrolls to the edge
   11. })
   12. // Shared multiplexing pools
   13. // ...
   14. }
   15. // ...
   16. }
   ```

   [TabsCeilingListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/TabsCeilingListPage.ets#L172-L237)
4. 设置List组件的高度在滑动到顶部时漏出Tabs组件

   ```
   1. @Component
   2. struct TabsCeilingListPage {
   3. // ...
   4. build() {
   5. // ...
   6. Column() {
   7. Tabs({ barPosition: BarPosition.Start, controller: this.contentTabController }) {
   8. // ...
   9. }
   10. // Set the height of the tab to 'calc(100% - 63vp)' to ensure that the Tabs component leaks out just when the nest slides
   11. .height('calc(100% - 58vp)')
   12. .barHeight(56)
   13. // ...
   14. }
   15. }
   ```

   [TabsCeilingListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/TabsCeilingListPage.ets#L31-L167)

说明

存在的问题：当Tabs设置为吸顶时，nestedScroll属性设置不生效。

解决方案：RecyclerView内部默认使用.layoutWeight(1)自动填充高度，需在最外层添加一个布局组件，并设置其高度为.height(calc(100% - 50vp))，以正确设置RecyclerView的高度。

## 分组吸顶场景

### 场景描述

双列表同向联动，左侧分类列表用于快速索引，内容列表依据分类进行分组，常用于商品分类选择、通讯录、城市选择、分组选择等页面。长列表分组吸顶功能参考：[常见列表流开发实践：分组吸顶场景](bpta-common-list-flows.md#section16551551888)。

本案例实现商品分类选择页面列表头部分类吸顶效果，如下图所示。

**图15** 分组布局组头吸顶效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/GPsw6ytwTgeD1D81WFHaKw/zh-cn_image_0000002356852018.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=3FBAA9D44721659CA78FEF720D9290E5787B18AE7BEEAFC9967DB9882C02E375 "点击放大")

### 开发步骤

1. 实现商品分类页面的分组展示

   ```
   1. class MyListManager extends ListManager {
   2. // ...
   3. }
   4. class MyListItemGroupManager extends ListItemGroupManager {
   5. // ...
   6. }

   8. @Component
   9. struct GroupLayoutListPage {
   10. // ...
   11. build() {
   12. NavDestination() {
   13. Row() {
   14. List({ scroller: this.categoryScroller }) {
   15. // ...
   16. }
   17. .width(100)
   18. .height('100%')
   19. .scrollBar(BarState.Off)

   21. // Nested scrolling: Implement the ListHeader effect
   22. Scroll() { // 2.Nested Scroll: Outer Scroll
   23. Column() {
   24. ListHeaderView()
   25. Column() { // 3.Nested Scrolling: Inner List
   26. RecyclerView({
   27. viewManager: this.myListManager
   28. })
   29. }
   30. .height('100%')
   31. }
   32. }
   33. .layoutWeight(1)
   34. .scrollBar(BarState.Off)
   35. }
   36. // ...
   37. }
   38. // ...
   39. }
   40. }

   42. @Builder
   43. function GoodItemContainer($$: ParamsGoods) {
   44. GoodItem({ dataModel: $$.dataModel })
   45. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L30-L346)
2. 设置吸顶属性

   ```
   1. initView() {
   2. // ...
   3. this.myListManager.setViewStyle({ space: 10, scroller: this.goodsListScroller })
   4. // ...
   5. .sticky(StickyStyle.Header)// Set up grouped ceilings
   6. // ...
   7. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L155-L196)

## 长列表二级联动场景

### 场景描述

通过选择左侧的一级列表，右侧的二级列表数据将相应更新，常用于商品分类选择、编辑风格等二级类别选择页面。长列表二级联动功能参考：[常见列表流开发实践：二级联动场景](bpta-common-list-flows.md#section323632114913)。

本场景以商品分类列表页面为例，分别使用List组件展示左侧分类导航和右侧导航内容。进入页面后，点击左侧分类导航，右侧将展示对应的分类详情列表数据；滑动右侧列表内容时，列表标题将吸顶显示，同时左侧对应的导航内容高亮显示。

**图16** 长列表二级联动效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/SoKgEIJDRz2ZcK5Sy3Lf_g/zh-cn_image_0000002390452065.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=9D247C4204C3E5D5CAB1163DC527FF09C7D59038267272668D3E0DC9B73BEF80 "点击放大")

### 开发步骤

1. 通过List组件构建左侧分类导航数据

   ```
   1. List({ scroller: this.categoryScroller }) {
   2. ForEach(this.myViewModel.categoryList, (item: CategoryModel, index: number) => {
   3. ListItem() {
   4. Text(item.titleName)
   5. // ...
   6. }
   7. }, (item: CategoryModel) => JSON.stringify(item.titleName))
   8. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L224-L244)
2. 通过RecyclerView构建右侧分类内容数据，以及Item复用相关代码

   ```
   1. class MyListManager extends ListManager {
   2. // ...
   3. }
   4. class MyListItemGroupManager extends ListItemGroupManager {
   5. // ...
   6. }

   8. @Component
   9. struct GroupLayoutListPage {
   10. // ...
   11. aboutToAppear() {
   12. this.initView();
   13. this.myListManager.registerNodeItem('GoodItemContainer', wrapBuilder(GoodItemContainer));
   14. this.myListManager.preCreate('GoodItemContainer', 30);
   15. this.myViewModel.loadData();
   16. }

   18. // ...
   19. build() {
   20. // ...
   21. Column() { // 3.Nested Scrolling: Inner List
   22. RecyclerView({
   23. viewManager: this.myListManager
   24. })
   25. }
   26. .height('100%')
   27. // ...
   28. }
   29. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L29-L290)
3. 为左侧导航列表添加点击事件，为右侧分类详情列表添加[onScrollIndex()](../harmonyos-references/ts-container-list.md#onscrollindex)事件，并调用自定义的listChange方法。在listChange方法内部，根据isGoods变量的值，调用相应列表控制器的[scrollToIndex()](../harmonyos-references/ts-container-scroll.md#scrolltoindex)方法，以实现导航列表和分类详情数据的联动效果。

   ```
   1. List({ scroller: this.categoryScroller }) {
   2. ForEach(this.myViewModel.categoryList, (item: CategoryModel, index: number) => {
   3. ListItem() {
   4. Text(item.titleName)
   5. // ...
   6. .onClick(() => this.listChange(index, true))
   7. }
   8. }, (item: CategoryModel) => JSON.stringify(item.titleName))
   9. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L223-L245)

   ```
   1. initView() {
   2. // ...
   3. this.myListManager.setViewStyle({ space: 10, scroller: this.goodsListScroller })
   4. // ...
   5. .onScrollIndex((index: number) => { // Scrolling listeners
   6. this.listChange(index, false);
   7. })
   8. // ...
   9. }

   11. listChange(index: number, isGoods: boolean) {
   12. if (this.currentTitleId !== index) {
   13. this.currentTitleId = index;
   14. if (isGoods) {
   15. this.goodsListScroller.scrollToIndex(index);
   16. } else {
   17. this.categoryScroller.scrollToIndex(index);
   18. }
   19. }
   20. }
   ```

   [GroupLayoutListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/GroupLayoutListPage.ets#L152-L210)

## 长列表动态切换列数场景

### 场景描述

当设备在横屏和竖屏之间切换，或折叠屏在小屏、中屏和大屏状态之间切换时，长列表的显示列数将根据当前屏幕宽度进行调整，以展示更合适大小的Item。

**图17** 动态切换列数效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/eUZBbUUUT9-sLcnCW0nmQA/zh-cn_image_0000002356692102.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=013C582F78B2811D43F885E8A562DE97E1DE8BCB5065BF1918ED416392BDEAAD "点击放大")

### 开发步骤

首先，设置页面可自由旋转，然后监听屏幕尺寸的变化。当发现宽度大于高度时，设置为2列。

```
1. @Component
2. struct SameItemListPage {
3. // ...
4. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
5. private windowClass = (this.context as common.UIAbilityContext).windowStage.getMainWindowSync();

7. aboutToDisappear(): void {
8. this.windowClass.off('windowSizeChange');
9. }
10. aboutToAppear(): void {
11. // The settings page is free to rotate
12. let orientation = window.Orientation.AUTO_ROTATION;
13. this.windowClass.setPreferredOrientation(orientation, (err: BusinessError) => {
14. const errCode: number = err.code;
15. if (errCode) {
16. Logger.error('Failed to set window orientation. Cause:' + JSON.stringify(err));
17. return;
18. }
19. Logger.info('Succeed to setting window orientation');
20. })
21. // Listen for screen size changes
22. this.windowClass.on('windowSizeChange', (size) => {
23. let viewWidth = size.width;
24. let viewHeight = size.height;
25. if (viewWidth > viewHeight) { // Criteria are judged based on business settings
26. this.myListManager.setViewStyle().lanes(2);
27. } else {
28. this.myListManager.setViewStyle().lanes(1);
29. }
30. })

32. this.initView();
33. // ...
34. }
35. initView() {
36. // ...
37. this.myListManager.setViewStyle({ space: 10, scroller: this.listScroller })
38. // ...
39. .alignListItem(ListItemAlign.Start)// Set the direction of the List cross axis
40. .lanes(1)// Set the number of layout columns or rows in the List portlet
41. // ...
42. }
43. // ...
44. }
```

[SameItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/SameItemListPage.ets#L38-L269)

说明

在Item高度一致的情况下，推荐使用动态改变列数的场景。当Item大小不一致时，动态设置显示的列数，当前行的高度将以最高的Item为准，这可能导致部分空白区域的出现。此时，需要开发者自行选择合适的布局方案。

目前不支持使用@State属性对List的属性进行双向绑定，需通过this.myListManager.setViewStyle().xxxx的格式进行设置。

## 设置边缘渐隐场景

### 场景描述

通过设置[fadingEdge](../harmonyos-references/ts-container-scrollable-common.md#fadingedge14)属性来实现边缘渐隐效果，效果如图所示。

**图18** 边缘渐隐效果图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/8r34_XWRQhivsUAqmulI0g/zh-cn_image_0000002390372153.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061023Z&HW-CC-Expire=86400&HW-CC-Sign=129014B63CB1FA3FE2D0F03CD85F49D3A8F282D4DFCCB7EC08B5797967542988 "点击放大")

### 开发步骤

可以直接在setViewStyle接口中设置渐隐效果。

```
1. this.myListManager.setViewStyle({ space: 10, scroller: this.listScroller })
2. // ...
3. .fadingEdge(true, { fadingEdgeLength: LengthMetrics.vp(80) })
```

[SameItemListPage.ets](https://gitcode.com/harmonyos_samples/ListScrollComponent/blob/master/entry/src/main/ets/pages/SameItemListPage.ets#L124-L158)

## 示例代码

[基于ScrollComponents实现长列表](https://gitcode.com/harmonyos_samples/ListScrollComponent)
