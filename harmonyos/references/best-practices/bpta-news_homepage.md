---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-news_homepage
title: 首页信息流体验优化
breadcrumb: 最佳实践 > 行业场景解决方案 > 新闻阅读 > 首页信息流体验优化
category: best-practices
scraped_at: 2026-04-29T14:13:08+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:b0cf0fb8b7e39c1ff51dd249b0528a9f846fd90965f7cb1bcfc692552aa858ba
---

## 概述

本场景解决方案面向新闻类页面开发人员，指导开发者从零开始构建新闻类首页面。包含地址选择、tabs和tabContent切换的动态图标和流畅动效、下拉刷新、上拉加载、首页feed流等常见功能的实现及流畅体验。

### 整体场景介绍

介绍了用户操作应用的主要流程，包括进入首页后通过页签切换页面内容、上拉加载和下拉刷新页面，以及从首页地址进入地址选择页更换地址等功能。

* 应用的主要流程图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/L8ALE6sOTwu6dC1q17BQ3w/zh-cn_image_0000002194011020.png?HW-CC-KV=V1&HW-CC-Date=20260429T061302Z&HW-CC-Expire=86400&HW-CC-Sign=9C1A563B6D3132500A5E3B10578D761B4409C99BD0D97614EDA2CBA8AC4D5076)

* 应用的运行效果图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/bCix0aKXTqehrkXnjxN1qw/zh-cn_image_0000002193851428.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061302Z&HW-CC-Expire=86400&HW-CC-Sign=D21F74A5C6A8B85BE6A85F5918CE716A3DC668BD2D27BD4FEFB9DF169EE39B9A "点击放大")

* 操作流程如下：

  1. 获取地理位置的权限；

  2. 点击位置信息，跳转地址选择页，可修改当前位置信息；

  3. 点击顶部页签或者滑动切换页面，页签同步切换；

  4. 点击底部页签切换页面，同步切换页签，触发页签切换的动画效果；

  5. 下拉刷新页面信息；

  6. 上拉加载页面信息；

  7. 点击右下角按钮回弹至顶部。

## 场景说明

### 适用范围

本场景适用于新闻类应用的首页，采用原生组件和三方库组件来实现新闻首页及其功能。

### 场景优势

本场景可提升用户的首页体验，使其更加流畅和便捷。具体优势包括：

1. 导航栏点击切换动效流畅，响应时延51ms。
2. 左右滑动切换动效流畅，响应时延67ms。
3. 地址选择页定位精确，选择目标城市便捷。
4. 底部页签跳转流畅，时延349ms。
5. 页面支持上拉加载和下拉刷新功能，动效回弹流畅，无丢帧现象。下拉刷新响应时延为153ms，上拉加载响应时延为150ms。

## 场景分析

### 典型场景与实现方案

* 实现方案如下表：

  | 场景名称 | 描述 | 实现方案 |
  | --- | --- | --- |
  | 导航栏切换动效流畅 | 点击页签或滑动切换页面时，页签同步切换 | tab组件添加动画开始时触发事件 |
  | 底部页签跳转精致流畅 | 底部页签切换时具有动画效果 | 添加lottie动画 |
  | 上拉加载下拉刷新 | 上拉加载更多新闻内容，下拉刷新整个页面，均具有加载动效 | pullToRefresh组件 |
  | 首页feed流 | 首页展示流畅的图文列表 | 使用LazyForEach对子组件进行渲染，实现懒加载功能 |
  | 地址选择页 | 提供地址选择、定位、地址首字母定位及模糊查询功能 | 位置服务与AlphabetIndexer组件 |

## 场景实现

### 导航栏切换动效流畅

通过添加Tab组件的动效触发事件，实现页面内容切换与页签样式切换的同步效果。具体效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/6EsgakzHRl2PujDlhewrRA/zh-cn_image_0000002229336809.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061302Z&HW-CC-Expire=86400&HW-CC-Sign=0BDBCC97CBC3E0E00C063EA49F56D8A1F0D3CF3C6F130448791D137CCFDC7058 "点击放大")

* 动效触发事件节点

  推荐使用onAnimationStart事件设置切换标签动效。使用onChange事件会导致页面切换后再触发动效，造成效果延迟。使用onClick事件会与页面切换冲突。

  ```
  1. // TabBar.ets
  2. @Builder
  3. TabBuilder(id: number, index: number) {
  4. Column() {
  5. Text(this.tabBarArray[id].name)
  6. // ...
  7. }
  8. .alignItems(HorizontalAlign.Start)
  9. }

  11. build() {
  12. Tabs({ barPosition: BarPosition.Start }) {
  13. ForEach(this.tabBarArray, (tabsItem: NewsTypeModel, index: number) => {
  14. TabContent() {
  15. // ...
  16. }
  17. // ...
  18. }, (item: NewsTypeModel) => JSON.stringify(item));
  19. }
  20. // ...
  21. .onAnimationStart((_index: number, targetIndex: number, _event: TabsAnimationEvent) => {
  22. this.currentIndex = targetIndex;
  23. })
  24. }
  ```

  [TabBar.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/TabBar.ets#L30-L75)

### 底部页签跳转精致流畅

底部页签样式添加Lottie动画，使跳转更加精致流畅。效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/xRwoCCJUQlirA8RL7KkcBw/zh-cn_image_0000002229451313.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061302Z&HW-CC-Expire=86400&HW-CC-Sign=8C4B4A751CCBC951762B07A12A634D09B7BBBAC2A9D87A46C9EAB9897E60AC19 "点击放大")

* 底部页签跳转功能时序图

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/4obQLSCiQoqhJXXNlT3SCw/zh-cn_image_0000002194011036.png?HW-CC-KV=V1&HW-CC-Date=20260429T061302Z&HW-CC-Expire=86400&HW-CC-Sign=EEFB7F60CD992BF65FA4E3D4A3DA1728330BBED9498C9C1255EE20DF3E172944 "点击放大")

* TabBar集成lottie动画

  lottie是适用于OpenHarmony的动画库，可解析AdobeAfterEffects通过Bodymovin插件导出的JSON格式动画，并在移动设备上本地渲染。支持动画交互，通过添加触摸事件与TabBar结合，实现动态图标效果。

  引入lottie三方库。

  ```
  1. ohpm install @ohos/lottie
  ```

  准备lottie动画资源，建议放置在Entry目录的common文件夹中。如果放置在本模块中，使用相对路径将无法读取。

  导入lottie模块。

  ```
  1. // Home.ets
  2. import lottie, { AnimationItem } from '@ohos/lottie';
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/Home.ets#L18-L19)

  使用RenderingContext在Canvas组件上进行绘制，声明CanvasRenderingContext2D变量。使用RenderingContextSettings配置CanvasRenderingContext2D对象的参数，设置canvas是否开启抗锯齿。

  ```
  1. // Home.ets
  2. private renderingSettings1: RenderingContextSettings = new RenderingContextSettings(true);
  3. private canvasRenderingContext1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.renderingSettings1);
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/Home.ets#L36-L38)

  定义所需数据类型的接口，初始化变量。接口中包含资源路径信息和CanvasRenderingContext2D。

  ```
  1. // Home.ets
  2. interface TabBarOption {
  3. index: number;
  4. text: ResourceStr;
  5. name: string;
  6. path: string;
  7. canvasRenderingContext: CanvasRenderingContext2D;
  8. lottieItem?: AnimationItem;
  9. currentBottomIndex?: number;
  10. currentBreakpoint?: string;
  11. }
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/Home.ets#L223-L234)

  实现动画播放的方法。

  ```
  1. // Home.ets
  2. lottieController(): void {
  3. if (this.currentBottomIndex === 0) {
  4. lottie.stop();
  5. lottie.play(this.tabOption1.name);
  6. }
  7. if (this.currentBottomIndex === 1) {
  8. lottie.stop();
  9. lottie.play(this.tabOption2.name);
  10. }
  11. if (this.currentBottomIndex === 2) {
  12. lottie.stop();
  13. lottie.play(this.tabOption3.name);
  14. }
  15. }
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/Home.ets#L147-L162)

  在TabBar样式中实现Canvas子组件。

  ```
  1. // Home.ets
  2. Canvas(tabBarOption.canvasRenderingContext)
  3. .width($r('app.float.canvas_size'))
  4. .height($r('app.float.canvas_size'))
  5. .onReady(() => {
  6. tabBarOption.canvasRenderingContext.imageSmoothingEnabled = true;
  7. tabBarOption.canvasRenderingContext.imageSmoothingQuality = 'medium';
  8. lottie.destroy(tabBarOption.name);
  9. const item = lottie.loadAnimation({
  10. container: tabBarOption.canvasRenderingContext,
  11. renderer: 'canvas',
  12. loop: false,
  13. autoplay: false,
  14. autoSkip: false,
  15. name: tabBarOption.name,
  16. path: tabBarOption.path,
  17. });
  18. tabBarOption.lottieItem = item;
  19. item.addEventListener('DOMLoaded', (args: Object): void => {
  20. if (tabBarOption.index === tabBarOption.currentBottomIndex) {
  21. item.play();
  22. }
  23. })
  24. })
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/Home.ets#L179-L202)

  在tab组件的onAnimationStart事件中调用播放方法。

  ```
  1. // Home.ets
  2. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
  3. this.currentBottomIndex = targetIndex;
  4. this.lottieController();
  5. this.updateTabText(targetIndex);
  6. })
  ```

  [Home.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/Home.ets#L136-L141)

### 上拉加载下拉刷新

通过三方库组件pullToRefresh实现下拉刷新页面和上拉加载更多数据的效果。具体效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/cQLGHiyGRD-U8R2LM-rI3w/zh-cn_image_0000002229451321.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061302Z&HW-CC-Expire=86400&HW-CC-Sign=1381DDAFBFD86E441E4DF660D5DB617943AD59DF1F9BA7257C83B0CECAA09C03 "点击放大")

* 上拉加载和下拉刷新时序图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/lOqoRP3DT1CLz6BZbZ4_vw/zh-cn_image_0000002229336825.png?HW-CC-KV=V1&HW-CC-Date=20260429T061302Z&HW-CC-Expire=86400&HW-CC-Sign=65901CA5A96599BB3B5F9212734C89777CCE4DEB877854F0D7A71A1162A4D734 "点击放大")

* pullToRefresh组件

  使用第三方库的pullToRefresh组件，将列表组件、绑定的数据对象和scroller对象包含在内，并添加上滑和下拉方法。支持lazyForEach数据作为数据源。设置List组件的edgeEffect属性为EdgeEffect.None。

  引入三方库pullToRefresh。

  ```
  1. ohpm install @ohos/pulltorefresh
  ```

  ```
  1. // PullToRefreshNews.ets
  2. import { PullToRefresh } from '@ohos/pulltorefresh/index';
  ```

  [PullToRefreshNews.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/PullToRefreshNews.ets#L20-L21)

  准备数据源，本场景使用本地资源模拟效果，资源文件在resources/rawfile目录下，实际情况可替换为从网络获取。

  ```
  1. // PullToRefreshNews.ets
  2. const MOCK_DATA_FILE_ONE_DIR: string =
  3. uiContext!.getHostContext()!.resourceManager.getStringSync($r('app.string.mock1').id);
  4. const MOCK_DATA_FILE_TWO_DIR: string =
  5. uiContext!.getHostContext()!.resourceManager.getStringSync($r('app.string.mock2').id);
  ```

  [PullToRefreshNews.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/PullToRefreshNews.ets#L38-L42)

  包含列表组件、数据对象和scroller对象，并添加上滑和下拉方法。

  ```
  1. // PullToRefreshNews.ets
  2. PullToRefresh({
  3. data: $newsData,
  4. scroller: this.scroller,
  5. customList: () => {
  6. this.getListView();
  7. },
  8. onRefresh: () => {
  9. return new Promise<string>((resolve, reject) => {
  10. // ...
  11. }, NEWS_REFRESH_TIME);
  12. });
  13. },
  14. onLoadMore: () => {
  15. return new Promise<string>((resolve, reject) => {
  16. // ...
  17. });
  18. },
  19. customLoad: null,
  20. customRefresh: null,
  21. })
  ```

  [PullToRefreshNews.ets](https://gitcode.com/HarmonyOS_Samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/PullToRefreshNews.ets#L70-L112)

### 首页feed流

使用懒加载实现首页 feed 流的快速渲染和流畅滑动。效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/RbAtt_J3TDy8_yqyB3wbLQ/zh-cn_image_0000002194011028.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061302Z&HW-CC-Expire=86400&HW-CC-Sign=0BA6C0BEA841F31F5B410AD728D24097E6D5695200CD93C6A8FB867859CA91C9 "点击放大")

* 懒加载

  新闻应用列表数据可能达到数万条。针对这类数据加载的长列表应用，使用懒加载可以解决一次性加载数据耗时长、占用资源多的问题，从而提升页面响应速度。

  准备需要加载的数据源：

  ```
  1. // PullToRefreshNews.ets
  2. @State newsData: NewsDataSource = new NewsDataSource();
  ```

  [PullToRefreshNews.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/PullToRefreshNews.ets#L49-L50)

  创建子组件：

  ```
  1. // PullToRefreshNews.ets
  2. @Component
  3. struct newsItem {
  4. // ...
  5. }
  ```

  [PullToRefreshNews.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/PullToRefreshNews.ets#L194-L274)

  使用LazyForEach对子组件进行渲染：

  ```
  1. // PullToRefreshNews.ets
  2. List({ space: CommonConstants.LIST_SPACE, scroller: this.scroller }) {
  3. LazyForEach(this.newsData, (item: NewsData) => {
  4. ListItem() {
  5. newsItem({
  6. // ...
  7. })
  8. }
  9. // ...
  10. }, (item: NewsData, index?: number) => JSON.stringify(item) + index);
  11. }
  ```

  [PullToRefreshNews.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/PullToRefreshNews.ets#L124-L150)

### 地址选择页

使用位置服务实现定位功能，AlphabetIndexer组件实现地址首字母定位导航条。效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/XCSKZRsjQ0W2iFMRyFoLXQ/zh-cn_image_0000002229336813.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061302Z&HW-CC-Expire=86400&HW-CC-Sign=E932F3477F98A35AA619DD2EBEBC3D31BE8F084D1F90684B0E76AB0F49E06265 "点击放大")

* 地址选择页效果功能时序图

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/rT3ygoLKR6CP5w0q9paw2Q/zh-cn_image_0000002229336833.png?HW-CC-KV=V1&HW-CC-Date=20260429T061302Z&HW-CC-Expire=86400&HW-CC-Sign=DC0B6B2810F1B98344A047DDFD85A7EB215606B85245F4B210D31C9ED41E000D "点击放大")

* 位置服务与索引条导航

  开启手机位置服务功能，使用位置服务获取当前地理位置信息，通过AlphabetIndexer组件实现首字母快速定位城市的索引条导航。

  申请权限时，API9及之后的版本，需要申请ohos.permission.APPROXIMATELY\_LOCATION，或同时申请ohos.permission.APPROXIMATELY\_LOCATION和ohos.permission.LOCATION；无法单独申请ohos.permission.LOCATION。

  ```
  1. "requestPermissions": [
  2. {
  3. "name": "ohos.permission.APPROXIMATELY_LOCATION",
  4. "reason": "$string:approximately_location_desc",
  5. "usedScene": {
  6. "abilities": [
  7. "EntryAbility"
  8. ],
  9. "when": "always"
  10. }
  11. },
  12. {
  13. "name": "ohos.permission.LOCATION",
  14. "reason": "$string:location_desc",
  15. "usedScene": {
  16. "abilities": [
  17. "EntryAbility"
  18. ],
  19. "when": "always"
  20. }
  21. }
  22. ],
  ```

  [module.json5](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/module.json5#L11-L32)

  申请用户安全权限：

  ```
  1. // Index.ets
  2. onPageShow(): void {
  3. abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.getUIContext().getHostContext(), [
  4. 'ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION']).then(() => {
  5. if (this.status) {
  6. geoLocationManager.getCurrentLocation(locationChange);
  7. this.status = false;
  8. }
  9. }).catch((err: BusinessError) => {
  10. hilog.error(0x0000, 'Index', `requestPermissionsFromUser fail, code: ${err.code}, message: ${err.message}`);
  11. });
  12. }
  ```

  [Index.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/pages/Index.ets#L66-L78)

  导入位置服务：

  ```
  1. // Index.ets
  2. import { geoLocationManager } from '@kit.LocationKit';
  ```

  [Index.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/pages/Index.ets#L17-L18)

  获取地理位置信息，进行逆地理编码以确定当前位置：

  ```
  1. // Index.ets
  2. let locationChange: (err: BusinessError, location: geoLocationManager.Location) => void = (err, location) => {
  3. if (err) {
  4. hilog.error(0x00000, 'locationChanger: err=', JSON.stringify(err));
  5. }
  6. if (location) {
  7. let reverseGeocodeRequest: geoLocationManager.ReverseGeoCodeRequest = {
  8. 'latitude': location.latitude,
  9. 'longitude': location.longitude,
  10. 'maxItems': CommonConstants.MAX_ITEMS
  11. };
  12. geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, (err, data) => {
  13. if (data) {
  14. hilog.info(0x00000, 'getAddressesFromLocation: data=', JSON.stringify(data));
  15. if (data[0].locality !== undefined) {
  16. if (i18n.System.getSystemLanguage() === 'zh-Hans') {
  17. AppStorage.setOrCreate('local', data[0].locality.replace(/"/g, '').slice(0, -1));
  18. AppStorage.setOrCreate('currentLocal', data[0].locality.replace(/"/g, '').slice(0, -1));
  19. } else {
  20. AppStorage.setOrCreate('local', data[0].locality.replace(/"/g, ''));
  21. AppStorage.setOrCreate('currentLocal', data[0].locality.replace(/"/g, ''));
  22. }
  23. }
  24. }
  25. });
  26. }
  27. };
  ```

  [Index.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/pages/Index.ets#L29-L56)

  使用AlphabetIndexer组件实现导航条。通过onSelect事件获取选中索引值，并使用Scroller的scrollToIndex()方法滑动到指定索引位置：

  ```
  1. // CityView.ets
  2. AlphabetIndexer({ arrayValue: TAB_VALUE, selected: this.stabIndex })
  3. .height(CommonConstants.FULL_PERCENT)
  4. .selectedColor($r('app.color.alphabet_select_color'))
  5. .popupColor($r('app.color.alphabet_pop_color'))
  6. .selectedBackgroundColor($r('app.color.alphabet_selected_bgc'))
  7. .popupBackground($r('app.color.alphabet_pop_bgc'))
  8. .popupPosition({ x: $r('app.integer.pop_position_x'), y: $r('app.integer.pop_position_y') })
  9. .usingPopup(true)
  10. .selectedFont({ size: $r('app.integer.select_font'), weight: FontWeight.Bolder })
  11. .popupFont({ size: $r('app.integer.pop_font'), weight: FontWeight.Bolder })
  12. .alignStyle(IndexerAlign.Right)
  13. .itemSize(CommonConstants.ITEM_SIZE)
  14. .onSelect((tabIndex: number) => {
  15. this.scroller.scrollToIndex(tabIndex);
  16. })
  ```

  [CityView.ets](https://gitcode.com/harmonyos_samples/fluent-news-homepage/blob/master/entry/src/main/ets/view/CityView.ets#L131-L146)

## 示例代码

* [基于原生组件实现新闻类首页流畅体验](https://gitcode.com/harmonyos_samples/fluent-news-homepage)
