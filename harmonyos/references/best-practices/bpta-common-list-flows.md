---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-common-list-flows
title: 常见列表流
breadcrumb: 最佳实践 > 布局与弹窗 > 常见列表流
category: best-practices
scraped_at: 2026-04-29T14:10:21+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:e0fc1b31e0d243f25df9fb96dd852ce25db32de967b4e7882b78e64162e92292
---

## 概述

列表流是采用以“行”为单位进行内容排列的布局形式，每“行”列表项通过文本、图片等不同形式的组合，高效地显示结构化的信息，当列表项内容超过屏幕大小时，可以提供滚动功能。列表流具有排版整齐、重点突出、对比方便、浏览速度快等特点。同时列表流也具有非常广泛的使用场景，例如：应用首页、通讯录、音乐列表、购物清单等。

列表流主要使用[List](../harmonyos-references/ts-container-list.md)组件，按垂直方向线性排列子组件[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)或[ListItem](../harmonyos-references/ts-container-listitem.md)，混合渲染任意数量的图文视图，从而构建列表内容。在实际场景中，一般会根据需要，结合其它基础组件，形成相对复杂的交互功能。

本文将介绍以下列表流场景的实现：

* [多类型列表项场景](bpta-common-list-flows.md#section20614147618)
* [Tabs吸顶场景](bpta-common-list-flows.md#section103354617711)
* [分组吸顶场景](bpta-common-list-flows.md#section16551551888)
* [二级联动场景](bpta-common-list-flows.md#section323632114913)

## 多类型列表项场景

**场景描述**

List组件作为整个首页长列表的容器，通过ListItem对不同模块进行视图界面定制，常用于门户首页、商城首页等多类型视图展示的列表信息流场景。

本场景以应用首页为例，将除页面顶部搜索框区域的其它内容，放在List组件内部，进行整体页面的构建。进入页面后，下滑刷新模拟网络请求；滑动页面列表内容，景区标题吸顶；滑动到页面底部，上滑模拟请求添加数据。

| 页面整体结构图 | 页面效果图 |
| --- | --- |
|  |  |

**实现原理**

根据列表内部各部分视图对应数据类型的区别，渲染不同的ListItem子组件。

Refresh组件可以进行页面下拉操作并显示刷新动效，List组件配合使用Swiper、Grid等基础组件用于页面的整体构建，再通过List组件的[sticky](../harmonyos-references/ts-container-list.md#sticky9)属性、[onReachEnd()](../harmonyos-references/ts-container-list.md#onreachend)事件和Refresh组件的[onRefreshing()](../harmonyos-references/ts-container-refresh.md#onrefreshing)事件，实现下滑模拟刷新、上滑模拟添加数据及列表标题吸顶的效果。

**开发步骤**

1. 顶部搜索框区域。

   ```
   1. Row() {
   2. Text($r('app.string.beijing'))
   3. // ...
   4. TextInput({ placeholder: $r('app.string.want_search')})
   5. // ...
   6. Text($r('app.string.more'))
   7. // ...
   8. }
   ```

   [HomePage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/HomePage.ets#L114-L134)

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/y9zm0TCwSjSPqvlkO37J1Q/zh-cn_image_0000002229337205.png?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=59F19EA3D74F4F10E4530E94EB7F5B8E136A5BDF91E36881296B30331248FAAA "点击放大")
2. 在List的第一个ListItem分组中，使用Swiper组件构建页面轮播图内容。

   ```
   1. List({ space: 12 }) {
   2. // Swiper
   3. ListItem() {
   4. Swiper() {
   5. ForEach(this.swiperContent, (item: SwiperType) => {
   6. Stack({ alignContent: Alignment.BottomStart }) {
   7. Image($r(item.pic))
   8. }
   9. }, (item: SwiperType) => JSON.stringify(item))
   10. }
   11. // ...
   12. .autoPlay(true) // Set the child component to play automatically
   13. .duration(1000) // Set the animation duration of the child component switchover
   14. .curve(Curve.Linear) // Set the animation curve to uniform speed
   15. .indicator( // Set the navigation point indicator
   16. new DotIndicator()
   17. .selectedColor(Color.White)
   18. )
   19. .itemSpace(10) // Set the space between child components
   20. // ...
   21. }
   22. // ...
   23. }
   ```

   [HomePage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/HomePage.ets#L146-L283)

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/ckSVM05wTFyxG5YoF4DEeg/zh-cn_image_0000002194011424.png?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=970F692E3CDB067C001F5D534E7889DA6C16B2FD01DA912BB4BC6A6855F2D2B7 "点击放大")
3. 在List的第二个ListItem分组中，使用Grid组件构建页面网格区域。

   ```
   1. List({ space: 12 }) {
   2. // Swiper
   3. ListItem() {
   4. // ...
   5. }
   6. // Grid
   7. ListItem() {
   8. Grid() {
   9. ForEach(this.gridTitle, (item: Resource) => {
   10. GridItem() {
   11. Column() {
   12. Image($r('app.media.pic1'))
   13. // ...
   14. Text(item)
   15. // ...
   16. }
   17. }
   18. }, (item: Resource) => JSON.stringify(item))
   19. }
   20. .rowsGap(16) // Set the line spacing
   21. .columnsGap(19) // Set the column spacing
   22. .columnsTemplate('1fr 1fr 1fr 1fr 1fr') // Set the proportion of each column
   23. // ...
   24. }
   25. // ...
   26. }
   ```

   [HomePage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/HomePage.ets#L147-L282)

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/XtYzkRICSRyq6DUubzVEfw/zh-cn_image_0000002193851800.png?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=7C029220BF83139ABFBE2B5B8019920AC355F92733820B10459B310E2ECE7114 "点击放大")
4. 推荐内容及列表内容的构建。

   ```
   1. // Scenic spot list content details
   2. @Builder
   3. scenicSpotDetailBuilder(title: Resource) {
   4. Column() {
   5. Image($r('app.media.pic1'))
   6. // ...
   7. Column() {
   8. Text(title)
   9. // ...
   10. Text() {
   11. Span($r('app.string.group_discount'))
   12. // ...
   13. Span('999￥')
   14. // ...
   15. }
   16. .margin({ top: 4, bottom: 4 })

   18. Text() {
   19. Span($r('app.string.group_discount'))
   20. Span('1999￥')
   21. }
   22. // ...
   23. }
   24. // ...
   25. }
   26. }
   ```

   [HomePage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/HomePage.ets#L60-L105)

   ```
   1. List({ space: 12 }) {
   2. // Swiper
   3. ListItem() {
   4. // ...
   5. }
   6. // Grid
   7. ListItem() {
   8. // ...
   9. }
   10. // Customize display area.
   11. ListItem() {
   12. Row() {
   13. Image($r('app.media.pic1'))
   14. // ...
   15. Image($r('app.media.pic1'))
   16. // ...
   17. }
   18. // ...
   19. }

   21. // Scenic spot classification list.
   22. ForEach(this.scenicSpotTitle, (item: Resource) => {
   23. ListItemGroup({ header: this.scenicSpotHeader(item) }) {
   24. ForEach(this.scenicSpotArray, (scenicSpotItem: Resource) => {
   25. ListItem() {
   26. this.scenicSpotDetailBuilder(scenicSpotItem);
   27. }
   28. }, (scenicSpotItem: Resource) => JSON.stringify(scenicSpotItem))
   29. }
   30. .borderRadius(this.borderRadiusVal)
   31. }, (item: Resource) => JSON.stringify(item))

   33. // ...
   34. }
   ```

   [HomePage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/HomePage.ets#L148-L281)

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/wvBJrPe1QB-94NHoxurZzQ/zh-cn_image_0000002194011412.png?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=4E0E836B3D1D3A84FB2BEF721D9AFF9AB64FFC8F578128EEA2AF7CCD927F0E56 "点击放大")
5. 将构建好的页面内容，放在Refresh组件内部，并给List和Refresh组件添加对应的[onReachEnd()](../harmonyos-references/ts-container-list.md#onreachend)和[onRefreshing()](../harmonyos-references/ts-container-refresh.md#onrefreshing)回调，实现下拉模拟刷新和上滑添加列表数据的效果。

   ```
   1. // Top search box.
   2. Row() {
   3. // ...
   4. }
   5. // ...

   7. // Pull down refresh component.
   8. Refresh({ refreshing: $$this.isRefreshing }) {
   9. // List as a long list layout.
   10. List({ space: 12 }) {
   11. // Swiper
   12. ListItem() {
   13. // ...
   14. }
   15. // Grid
   16. ListItem() {
   17. // ...
   18. }
   19. // Customize display area.
   20. ListItem() {
   21. // ...
   22. }

   24. // Scenic spot classification list.
   25. ForEach(this.scenicSpotTitle, (item: Resource) => {
   26. // ...
   27. }, (item: Resource) => JSON.stringify(item))

   29. // Customize bottom loading for more.
   30. ListItem() {
   31. Row() {
   32. if (!this.noMoreData) {
   33. LoadingProgress()
   34. // ...
   35. }
   36. Text(this.noMoreData ? $r('app.string.no_more_data') : $r('app.string.loading_more'))
   37. }
   38. // ...
   39. }
   40. // ...
   41. }
   42. // ...
   43. .onReachEnd(() => { // Callback triggered when the list is added to the end position
   44. if (this.scenicSpotArray.length >= 20) {
   45. // When the list data is greater than or equal to 20, noMoreData is set to true
   46. this.noMoreData = true;
   47. return;
   48. }
   49. setTimeout(() => {
   50. this.scenicSpotArray.push('scenic area' + (this.scenicSpotArray.length + 1));
   51. }, 500)
   52. })
   53. }
   54. // Pull down refresh, simulate network request.
   55. .onRefreshing(() => {
   56. this.isRefreshing = true; // Enter the refresh state
   57. setTimeout(() => {
   58. this.scenicSpotArray =
   59. this.scenicSpotArray = ['scenic area 1', 'scenic area 2', 'scenic area 3', 'scenic area 4', 'scenic area 5'];
   60. this.noMoreData = false;
   61. this.isRefreshing = false;
   62. }, 2000)
   63. })
   ```

   [HomePage.ets](https://gitcode.com/HarmonyOS_Samples/CommonListFlows/blob/master/entry/src/main/ets/pages/HomePage.ets#L112-L315)

**实现效果**

| 模拟下拉刷新+标题吸顶效果 | 上滑加载更多效果 |
| --- | --- |
|  |  |

## Tabs吸顶场景

**场景描述**

Tabs嵌套List的吸顶效果，常用于新闻、资讯类应用的首页。

本场景以Tabs页签首页内容为例，在首页TabContent的内容区域使用List组件配合其它组件，构建下方列表数据内容。进入页面后，向上滑动内容，中间Tabs页签区域实现吸顶展示的效果。

| 页面整体结构图 | 页面效果图 |
| --- | --- |
|  |  |

**实现原理**

Tabs组件可以在页面内快速实现视图内容的切换，让用户能够聚焦于当前显示的内容，并对页面内容进行分类，提高页面空间利用率。

通过Tabs组件，配合使用Stack、Scroll、Search以及List等基础组件构建完整页面，再使用List组件的[nestedScroll](../harmonyos-references/ts-container-list.md#nestedscroll10)属性，结合calc计算高度，实现中间Tabs页签区域吸顶展示的效果。

**开发步骤**

1. 构建Tabs的自定义tabBar内容。

   ```
   1. @Builder
   2. tabBuilder(img: Resource, title: Resource, index: number) {
   3. Column() {
   4. Image(img)
   5. // ...
   6. .fillColor(this.currentIndex === index ? '#0a59f7' : '#66000000')
   7. Text(title)
   8. // ...
   9. .fontColor(this.currentIndex === index ? '#0a59f7' : '#66000000')
   10. }
   11. // ...
   12. .onClick(() => {
   13. this.currentIndex = index;
   14. this.tabsController.changeIndex(this.currentIndex);
   15. })
   16. }
   ```

   [ManagerPage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/ManagerPage.ets#L54-L80)

   ```
   1. Tabs({ barPosition: BarPosition.End, controller: this.tabsController }) {
   2. TabContent() {
   3. // ...
   4. }
   5. .tabBar(this.tabBuilder($r('app.media.mine'), $r('app.string.tabBar1'), 0))

   7. // ...
   8. }
   9. // ...
   10. .onChange((index: number) => {
   11. this.currentIndex = index;
   12. })
   ```

   [ManagerPage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/ManagerPage.ets#L86-L271)

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/IldlVExyS3uWiqdfrEOWlw/zh-cn_image_0000002229451669.png?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=904FD5536241916AD7EBD7B26C3845611621B644BCBB82EA47101FF4E7349570 "点击放大")
2. 构建顶部搜索区域。

   ```
   1. Row() {
   2. Image($r('app.media.app_icon'))
   3. // ...
   4. Search({
   5. placeholder: $r('app.string.want_search'),
   6. })
   7. .searchButton('search', { fontSize: 14 })
   8. // ...
   9. Text($r('app.string.search'))
   10. // ...
   11. }
   ```

   [ManagerPage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/ManagerPage.ets#L206-L229)

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/ju_2n-jnQo6WZlw7eLejmA/zh-cn_image_0000002229337189.png?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=B81A35A83B6D9479A89A3C0900E9EF85842ED3C91221E049C10685D47D84F002 "点击放大")
3. 图片占位区域、自定义导航内容及列表内容构建。

   ```
   1. // Home page content.
   2. Scroll(this.scrollController) {
   3. Column() {
   4. // Image placeholder area.
   5. Image($r('app.media.pic5'))
   6. // ...

   8. Column() {
   9. // Customize tabBar.
   10. Row({ space: 16 }) {
   11. ForEach(this.tabArray, (item: string, index: number) => {
   12. Text(item)
   13. .fontColor(this.currentTabIndex === index ? '#0a59f7' : Color.Black)
   14. .onClick(() => {
   15. // Click to switch tabs content.
   16. this.contentTabController.changeIndex(index);
   17. this.currentTabIndex = index;
   18. })
   19. }, (item: string) => item)
   20. }
   21. // ...

   23. // Tabs
   24. Tabs({ barPosition: BarPosition.Start, controller: this.contentTabController }) {
   25. TabContent() {
   26. List({ space: 10, scroller: this.listScroller }) {
   27. CustomListItem({
   28. imgUrl: $r('app.media.pic1'),
   29. title: $r('app.string.manager_content')
   30. })
   31. // ...
   32. }
   33. // ...
   34. }
   35. .tabBar('follow')
   36. // ...
   37. }
   38. // ...
   39. }
   40. // ...
   41. }
   42. }
   43. // ...
   44. .scrollBar(BarState.Off) // Hide the scroll bar
   ```

   [ManagerPage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/ManagerPage.ets#L91-L201)

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/qen2Zx5ZQsykONumLnux7Q/zh-cn_image_0000002194011428.png?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=5E8956465159C8294002E1D2ABEAD1DEB345A601C844A80069BABF207D01F335 "点击放大")
4. 给List组件添加的[nestedScroll](../harmonyos-references/ts-container-list.md#nestedscroll10)属性，结合calc计算实现中间自定义Tab页签区域吸顶展示的效果。

   ```
   1. Tabs({ barPosition: BarPosition.Start, controller: this.contentTabController }) {
   2. TabContent() {
   3. List({ space: 10, scroller: this.listScroller }) {
   4. // ...
   5. }
   6. // ...
   7. // Customize the tabBar to achieve sticky by combining the nestedScroll attribute with Calc to calculate height.
   8. .nestedScroll({
   9. scrollForward: NestedScrollMode.PARENT_FIRST, // Set the effect of scrolling the component to the end: The parent component rolls first, and then rolls itself to the edge
   10. scrollBackward: NestedScrollMode.SELF_FIRST // Set the effect of rolling the component to the start end: Rolls itself first, and then the parent component scrolls to the edge
   11. })
   12. }
   13. .tabBar('follow')
   14. // ...
   15. }
   16. .barHeight(0)
   17. .height('calc(100% - 100vp)')
   18. .onChange((index: number) => {
   19. this.currentTabIndex = index;
   20. })
   ```

   [ManagerPage.ets](https://gitcode.com/HarmonyOS_Samples/CommonListFlows/blob/master/entry/src/main/ets/pages/ManagerPage.ets#L123-L186)

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/89OC9YqIQeSDRngH8dX38g/zh-cn_image_0000002229337229.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=A7173A4C13BCE47052D1CE077A2A93B5CA043AB372B8F137E47C8CA16DB8EB02 "点击放大")

## 分组吸顶场景

**场景描述**

双列表同向联动，右边字母列表用于快速索引，内容列表根据首字母进行分组，常用于通讯录、城市选择、分组选择等页面。

本场景以城市列表页面为例，左侧城市列表数据和右侧字母导航数据通过List组件来展示，并通过Stack组件使两个列表数据分层显示。在进入页面后，通过滑动左侧城市列表数据，列表字母标题吸顶展示，对应右侧字母导航内容高亮显示；点击右侧字母导航内容，左侧城市列表展示对应内容。

| 页面整体结构图 | 页面效果图 |
| --- | --- |
|  |  |

**实现原理**

左侧List作为城市列表，右侧List为城市首字母快捷导航列表，通过ListItem对对应数据进行渲染展示，并使用Stack堆叠容器组件，字母导航列表覆盖城市列表上方，再给对应List添加[sticky](../harmonyos-references/ts-container-list.md#sticky9)属性和[onScrollIndex()](../harmonyos-references/ts-container-list.md#onscrollindex)方法，实现两个列表数据间的联动效果。

**开发步骤**

1. 城市列表使用ListItemGroup，对“当前城市”“热门城市”“城市数据”进行分组，并通过ListItem展示每个分组中的具体数据。

   ```
   1. // List data content.
   2. @Builder
   3. textContent(content: string) {
   4. Text(content)
   5. // ...
   6. }
   ```

   [CityList.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/CityList.ets#L75-L87)

   ```
   1. List({ scroller: this.cityScroller }) {
   2. // Current city.
   3. ListItemGroup({ header: this.itemHead($r('app.string.current_city')) }) {
   4. ListItem() {
   5. Text(this.currentCity)
   6. .width('100%')
   7. .height(45)
   8. .fontSize(16)
   9. .padding({ left: 16, top: 12, bottom: 12 })
   10. .textAlign(TextAlign.Start)
   11. .backgroundColor(Color.White)
   12. }
   13. }

   15. // Popular cities.
   16. ListItemGroup({ header: this.itemHead($r('app.string.popular_cities')) }) {
   17. ForEach(this.hotCities, (item: string) => {
   18. ListItem() {
   19. this.textContent(item);
   20. }
   21. }, (item: string) => item)
   22. }
   23. .divider({
   24. strokeWidth: 1,
   25. color: '#EDEDED',
   26. startMargin: 10,
   27. endMargin: 45
   28. })

   30. // City data.
   31. ForEach(this.groupWorldList, (item: string) => {
   32. // Traverse the first letter of the city and use it as the header of the city grouping data.
   33. ListItemGroup({ header: this.itemHead(item) }) {
   34. // Retrieve and display corresponding city data based on letters.
   35. ForEach(this.getCitiesWithGroupName(item), (cityItem: City) => {
   36. ListItem() {
   37. this.textContent(cityItem.city);
   38. }
   39. }, (cityItem: City) => cityItem.city)
   40. }
   41. })
   42. }
   ```

   [CityList.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/CityList.ets#L102-L149)
2. 右侧字母导航列表数据，同样通过List组件进行展示。

   ```
   1. // Side letter navigation data.
   2. Column() {
   3. List({ scroller: this.navListScroller }) {
   4. ForEach(this.groupWorldList, (item: string, index: number) => {
   5. ListItem() {
   6. Text(item)
   7. // ...
   8. }
   9. }, (item: string) => item)
   10. }
   11. }
   ```

   [CityList.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/CityList.ets#L168-L202)
3. 使用堆叠容器组件Stack，将字母导航内容覆盖到城市列表内容上方。

   ```
   1. Stack({ alignContent: Alignment.End }) {
   2. // City List Data.
   3. List({ scroller: this.cityScroller }) {
   4. // ...
   5. }
   6. // ...

   8. // Side letter navigation data.
   9. Column() {
   10. List({ scroller: this.navListScroller }) {
   11. // ...
   12. }
   13. }
   14. // ...
   15. }
   ```

   [CityList.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/CityList.ets#L99-L209)
4. 最后，给城市列表添加[sticky](../harmonyos-references/ts-container-list.md#sticky9)属性实现标题吸顶效果，及添加[onScrollIndex()](../harmonyos-references/ts-container-list.md#onscrollindex)方法，通过selectNavIndex变量与字母导航列表内容进行关联，控制的对应字母导航内容的选中状态。

   在字母导航列表中，添加点击事件，在点击事件中通过城市列表控制器cityScroller的[scrollToIndex()](../harmonyos-references/ts-container-scroll.md#scrolltoindex)事件，控制城市列表内容的改变，实现二者数据的联动效果。

   ```
   1. Stack({ alignContent: Alignment.End }) {
   2. // City List Data.
   3. List({ scroller: this.cityScroller }) {
   4. // ...
   5. }
   6. // ...
   7. .onScrollIndex((index: number) => {
   8. // By linking the selectNavIndex state variable with index, control the selection status of the navigation list.
   9. this.selectNavIndex = index - 2;
   10. })

   12. // Side letter navigation data.
   13. Column() {
   14. List({ scroller: this.navListScroller }) {
   15. ForEach(this.groupWorldList, (item: string, index: number) => {
   16. ListItem() {
   17. Text(item)
   18. // ...
   19. .onClick(() => {
   20. this.selectNavIndex = index;
   21. // Select the navigation list and set isClickScroll to true to prevent changes in the navigation list status during the scrolling process with the city list.
   22. this.isClickScroll = true;
   23. /*
   24. * By using the scrollToIndex method of cityScroller, control the sliding city list to specify the Index,
   25. * as there are "current city" and "popular city" in the city list, so the index needs to be incremented by 2.
   26. */
   27. this.cityScroller.scrollToIndex(index + 2, false, ScrollAlign.START);
   28. })
   29. }
   30. }, (item: string) => item)
   31. }
   32. }
   33. // ...
   34. }
   ```

   [CityList.ets](https://gitcode.com/HarmonyOS_Samples/CommonListFlows/blob/master/entry/src/main/ets/pages/CityList.ets#L98-L212)

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/86B0KDA_QlK02afTd2Fw5Q/zh-cn_image_0000002194011392.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=62EAAA0D54D74518017CEF53E6EF474951BF1D6181378C804BEFB80FEBF5BCDE "点击放大")

## 二级联动场景

**场景描述**

通过左边一级列表的选择，联动更新右边二级列表的数据，常用于商品分类选择、编辑风格等二级类别选择页面。

本场景以商品分类列表页面为例，分别通过List组件，对左侧分类导航和右侧导航内容进行展示。在进入页面后，点击左侧分类导航，右侧展示对应导航分类详情列表数据；滑动右侧列表内容，列表标题吸顶展示，左侧对应导航内容则高亮显示。

| 页面整体结构图 | 页面效果图 |
| --- | --- |
|  |  |

**实现原理**

左右各用一个List实现，分别设置其[onScrollIndex()](../harmonyos-references/ts-container-list.md#onscrollindex)事件，左侧List在回调中判断数据项切换时，调用右侧List滚动到相应类别的对应位置，右侧同理。

**开发步骤**

1. 分别通过List组件构建左侧分类导航数据和右侧分类内容数据。

   ```
   1. // Left List Data Display.
   2. List({ scroller: this.navTitleScroller }) {
   3. ForEach(this.categoryList, (item: NavTitleModel, index: number) => {
   4. ListItem() {
   5. Text(item.titleName)
   6. // ...
   7. }
   8. }, (item: NavTitleModel) => JSON.stringify(item.titleName))
   9. }
   10. // ...

   12. // Display of List Content on the Right.
   13. List({ scroller: this.goodsListScroller }) {
   14. ForEach(this.categoryList, (item: NavTitleModel) => {
   15. ListItemGroup({ space: 12, header: this.goodsHeaderBuilder(item.titleName) }) {
   16. ForEach(item.goodsList, (goodsItem: GoodsDataModel) => {
   17. ListItem() {
   18. Row() {
   19. Image(goodsItem.imgUrl)
   20. // ...
   21. Column() {
   22. Text(goodsItem.goodsName)
   23. // ...
   24. Text('￥' + goodsItem.price)
   25. // ...
   26. }
   27. // ...
   28. }
   29. // ...
   30. }
   31. }, (goodsItem: GoodsDataModel) => JSON.stringify(goodsItem.goodsId))
   32. }
   33. }, (item: NavTitleModel) => JSON.stringify(item.goodsList))
   34. }
   ```

   [CategoryPage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/CategoryPage.ets#L71-L151)
2. 给左侧导航列表添加点击事件，右侧分类详情列表添加[onScrollIndex()](../harmonyos-references/ts-container-list.md#onscrollindex)事件，并调用自定义事件listChange方法，在listChange方法内部根据isGoods变量的值，调用对应列表控制器的[scrollToIndex()](../harmonyos-references/ts-container-scroll.md#scrolltoindex)事件，实现导航列表和分类详情数据的联动效果。

   ```
   1. // List sliding event.
   2. listChange(index: number, isGoods: boolean) {
   3. if (this.currentTitleId !== index) {
   4. this.currentTitleId = index;
   5. if (isGoods) {
   6. // IsGoods is true, controlling the data in the right-hand list to slide to the specified index.
   7. this.goodsListScroller.scrollToIndex(index);
   8. } else {
   9. // IsGoods is set to false, controlling the left list data to slide to the specified index.
   10. this.navTitleScroller.scrollToIndex(index);
   11. }
   12. }
   13. }
   ```

   [CategoryPage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/CategoryPage.ets#L51-L63)

   ```
   1. // Left List Data Display.
   2. List({ scroller: this.navTitleScroller }) {
   3. ForEach(this.categoryList, (item: NavTitleModel, index: number) => {
   4. ListItem() {
   5. Text(item.titleName)
   6. // ...
   7. .onClick(() => {
   8. // Pass in the current list item index and true.
   9. this.listChange(index, true);
   10. })
   11. }
   12. }, (item: NavTitleModel) => JSON.stringify(item.titleName))
   13. }
   14. // ...

   16. // Display of List Content on the Right.
   17. List({ scroller: this.goodsListScroller }) {
   18. // ...
   19. }
   20. // ...
   21. .onScrollIndex((index: number) => {
   22. // Pass in the current list item index and false.
   23. this.listChange(index, false)
   24. })
   ```

   [CategoryPage.ets](https://gitcode.com/harmonyos_samples/CommonListFlows/blob/master/entry/src/main/ets/pages/CategoryPage.ets#L70-L165)

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/5urc11wUSNCTJ_nmx5C5YA/zh-cn_image_0000002193851840.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061017Z&HW-CC-Expire=86400&HW-CC-Sign=BDB76C7A83B58AB03581D82A1DD17040BE8588EB1254590BB04233F7AC38166C "点击放大")

## 示例代码

* [基于List组件实现常见列表流场景](https://gitcode.com/harmonyos_samples/CommonListFlows)
