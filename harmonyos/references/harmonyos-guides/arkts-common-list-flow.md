---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-list-flow
title: 常见列表流
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 列表与网格 > 常见列表流
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:49+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:a6dd48240a3c718b264cfb822fc5d8491e9510d0393126be2883876ad2174b3c
---

## 概述

列表流是采用以“行”为单位进行内容排列的布局形式，每“行”列表项通过文本、图片等不同形式的组合，高效地显示结构化的信息，当列表项内容超过屏幕大小时，可以提供滚动功能。列表流具有排版整齐、重点突出、对比方便、浏览速度快等特点。同时列表流也具有非常广泛的使用场景，例如：应用首页、通讯录、音乐列表、购物清单等。

列表流主要使用[List](../harmonyos-references/ts-container-list.md)组件，按垂直方向线性排列子组件[ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md)或[ListItem](../harmonyos-references/ts-container-listitem.md)，混合渲染任意数量的图文视图，从而构建列表内容。在实际场景中，一般会根据需要，结合其它基础组件，形成相对复杂的交互功能。

本文将介绍以下列表流场景的实现：

* [常见列表流](arkts-common-list-flow.md#常见列表流)
  + [概述](arkts-common-list-flow.md#概述)
  + [多类型列表项场景](arkts-common-list-flow.md#多类型列表项场景)
  + [Tabs吸顶场景](arkts-common-list-flow.md#tabs吸顶场景)
  + [分组吸顶场景](arkts-common-list-flow.md#分组吸顶场景)
  + [二级联动场景](arkts-common-list-flow.md#二级联动场景)
  + [示例代码](arkts-common-list-flow.md#示例代码)

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

   ```ts
   Row() {
     Text($r('app.string.beijing'))
       // ...
     TextInput({ placeholder: $r('app.string.want_search')})
       // ...
     Text($r('app.string.more'))
       // ...
   }
   ```

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/TRy7f-ibQVOfbkWaX6FzZw/zh-cn_image_0000002706673594.png)
2. 在List的第一个ListItem分组中，使用Swiper组件构建页面轮播图内容。

   ```ts
   List({ space: 12 }) {
     ListItem() {
       Swiper() {
         ForEach(this.swiperContent, (item: SwiperType) => {
           Stack({ alignContent: Alignment.BottomStart }) {
             Image($r(item.pic))
           }
         }, (item: SwiperType) => JSON.stringify(item))
       }
       // ...
       .autoPlay(true)
       .duration(1000)
       .curve(Curve.Linear)
       .indicator(
         new DotIndicator()
           .selectedColor(Color.White)
       )
       .itemSpace(10)
       // ...
     }
     // ...
   }
   ```

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/syynYXAHTW6tLvw-rX3EHQ/zh-cn_image_0000002736432685.png)
3. 在List的第二个ListItem分组中，使用Grid组件构建页面网格区域。

   ```ts
   List({ space: 12 }) {
     ListItem() {
       // ...
     }
     ListItem() {
       Grid() {
         ForEach(this.gridTitle, (item: Resource) => {
           GridItem() {
             Column() {
               Image($r('app.media.pic1'))
                 // ...
               Text(item)
                 // ...
             }
           }
         }, (item: Resource) => JSON.stringify(item))
       }
       .rowsGap(16)
       .columnsGap(19)
       .columnsTemplate('1fr 1fr 1fr 1fr 1fr')
       // ...
     }
     // ...
   }
   ```

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/71ZRLeTGQfms4OEN7qVlxQ/zh-cn_image_0000002736432663.png)
4. 推荐内容及列表内容的构建。

   ```ts
   @Builder
   scenicSpotDetailBuilder(title: Resource) {
     Column() {
       Image($r('app.media.pic1'))
         // ...
       Column() {
         Text(title)
           // ...
         Text() {
           Span($r('app.string.group_discount'))
             // ...
           Span('999￥')
             // ...
         }
         .margin({ top: 4, bottom: 4 })

         Text() {
           Span($r('app.string.group_discount'))
           Span('1999￥')
         }
         // ...
       }
       // ...
     }
   }
   ```

   ```ts
   List({ space: 12 }) {
     ListItem() {
       // ...
     }
     ListItem() {
       // ...
     }
     ListItem() {
       Row() {
         Image($r('app.media.pic1'))
           // ...
         Image($r('app.media.pic1'))
           // ...
       }
       // ...
     }

     ForEach(this.scenicSpotTitle, (item: Resource) => {
       ListItemGroup({ header: this.scenicSpotHeader(item) }) {
         ForEach(this.scenicSpotArray, (scenicSpotItem: Resource) => {
           ListItem() {
             this.scenicSpotDetailBuilder(scenicSpotItem);
           }
         }, (scenicSpotItem: Resource) => JSON.stringify(scenicSpotItem))
       }
       .borderRadius(this.borderRadiusVal)
     }, (item: Resource) => JSON.stringify(item))

     // ...
   }
   ```

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/yNLuyBV2QZSm2dQ5vwYEGA/zh-cn_image_0000002706833530.png)
5. 将构建好的页面内容，放在Refresh组件内部，并给List和Refresh组件添加对应的[onReachEnd()](../harmonyos-references/ts-container-list.md#onreachend)和[onRefreshing()](../harmonyos-references/ts-container-refresh.md#onrefreshing)回调，实现下拉模拟刷新和上滑添加列表数据的效果。

   ```ts
   Row() {
     // ...
   }
   // ...

   Refresh({ refreshing: $$this.isRefreshing }) {
     List({ space: 12 }) {
       ListItem() {
         // ...
       }
       ListItem() {
         // ...
       }
       ListItem() {
         // ...
       }

       ForEach(this.scenicSpotTitle, (item: Resource) => {
         // ...
       }, (item: Resource) => JSON.stringify(item))

       ListItem() {
         Row() {
           if (!this.noMoreData) {
             LoadingProgress()
               // ...
           }
           Text(this.noMoreData ? $r('app.string.no_more_data') : $r('app.string.loading_more'))
         }
         // ...
       }
       // ...
     }
     // ...
     .onReachEnd(() => {
       if (this.scenicSpotArray.length >= 20) {
         this.noMoreData = true;
         return;
       }
       setTimeout(() => {
         this.scenicSpotArray.push('scenic area' + (this.scenicSpotArray.length + 1));
       }, 500)
     })
   }
   .onRefreshing(() => {
     this.isRefreshing = true;
     setTimeout(() => {
       this.scenicSpotArray =
         this.scenicSpotArray = ['scenic area 1', 'scenic area 2', 'scenic area 3', 'scenic area 4', 'scenic area 5'];
       this.noMoreData = false;
       this.isRefreshing = false;
     }, 2000)
   })
   ```

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

   ```ts
   @Builder
   tabBuilder(img: Resource, title: Resource, index: number) {
     Column() {
       Image(img)
         // ...
         .fillColor(this.currentIndex === index ? '#0a59f7' : '#66000000')
       Text(title)
         // ...
         .fontColor(this.currentIndex === index ? '#0a59f7' : '#66000000')
     }
     // ...
     .onClick(() => {
       this.currentIndex = index;
       this.tabsController.changeIndex(this.currentIndex);
     })
   }
   ```

   ```ts
   Tabs({ barPosition: BarPosition.End, controller: this.tabsController }) {
     TabContent() {
       // ...
     }
     .tabBar(this.tabBuilder($r('app.media.mine'), $r('app.string.tabBar1'), 0))

     // ...
   }
   // ...
   .onChange((index: number) => {
     this.currentIndex = index;
   })
   ```

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/90UJhJcHS5mjPxWJhz7EHg/zh-cn_image_0000002736312641.png)
2. 构建顶部搜索区域。

   ```ts
   Row() {
     Image($r('app.media.app_icon'))
       // ...
     Search({
       placeholder: $r('app.string.want_search'),
     })
       .searchButton('search', { fontSize: 14 })
       // ...
     Text($r('app.string.search'))
       // ...
   }
   ```

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/6T4dpyPZTJOAcNUV4Zl2fA/zh-cn_image_0000002706673598.png)
3. 图片占位区域、自定义导航内容及列表内容构建。

   ```ts
   Scroll(this.scrollController) {
     Column() {
       Image($r('app.media.pic5'))
         // ...

       Column() {
         Row({ space: 16 }) {
           ForEach(this.tabArray, (item: string, index: number) => {
             Text(item)
               .fontColor(this.currentTabIndex === index ? '#0a59f7' : Color.Black)
               .onClick(() => {
                 this.contentTabController.changeIndex(index);
                 this.currentTabIndex = index;
               })
           }, (item: string) => item)
         }
         // ...

         Tabs({ barPosition: BarPosition.Start, controller: this.contentTabController }) {
           TabContent() {
             List({ space: 10, scroller: this.listScroller }) {
               CustomListItem({
                 imgUrl: $r('app.media.pic1'),
                 title: $r('app.string.manager_content')
               })
               // ...
             }
             // ...
           }
           .tabBar('follow')
           // ...
         }
         // ...
       }
       // ...
     }
   }
   // ...
   .scrollBar(BarState.Off)
   ```

   实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/xVGhZ1lkRVmXRua-HL7VnA/zh-cn_image_0000002736432689.png)
4. 给List组件添加的[nestedScroll](../harmonyos-references/ts-container-list.md#nestedscroll10)属性，结合calc计算实现中间自定义Tab页签区域吸顶展示的效果。

   ```ts
   Tabs({ barPosition: BarPosition.Start, controller: this.contentTabController }) {
     TabContent() {
       List({ space: 10, scroller: this.listScroller }) {
         // ...
       }
       // ...
       .nestedScroll({
         scrollForward: NestedScrollMode.PARENT_FIRST,
         scrollBackward: NestedScrollMode.SELF_FIRST
       })
     }
     .tabBar('follow')
     // ...
   }
   .barHeight(0)
   .height('calc(100% - 100vp)')
   .onChange((index: number) => {
     this.currentTabIndex = index;
   })
   ```

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/e9YRlicITsC9xKaNj7rbEg/zh-cn_image_0000002706833534.gif)

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

   ```ts
   @Builder
   textContent(content: string) {
     Text(content)
       // ...
   }
   ```

   ```ts
   List({ scroller: this.cityScroller }) {
     ListItemGroup({ header: this.itemHead($r('app.string.current_city')) }) {
       ListItem() {
         Text(this.currentCity)
           .width('100%')
           .height(45)
           .fontSize(16)
           .padding({ left: 16, top: 12, bottom: 12 })
           .textAlign(TextAlign.Start)
           .backgroundColor(Color.White)
       }
     }

     ListItemGroup({ header: this.itemHead($r('app.string.popular_cities')) }) {
       ForEach(this.hotCities, (item: string) => {
         ListItem() {
           this.textContent(item);
         }
       }, (item: string) => item)
     }
     .divider({
       strokeWidth: 1,
       color: '#EDEDED',
       startMargin: 10,
       endMargin: 45
     })

     ForEach(this.groupWorldList, (item: string) => {
       ListItemGroup({ header: this.itemHead(item) }) {
         ForEach(this.getCitiesWithGroupName(item), (cityItem: City) => {
           ListItem() {
             this.textContent(cityItem.city);
           }
         }, (cityItem: City) => cityItem.city)
       }
     })
   }
   ```
2. 右侧字母导航列表数据，同样通过List组件进行展示。

   ```ts
   Column() {
     List({ scroller: this.navListScroller }) {
       ForEach(this.groupWorldList, (item: string, index: number) => {
         ListItem() {
           Text(item)
             // ...
         }
       }, (item: string) => item)
     }
   }
   ```
3. 使用堆叠容器组件Stack，将字母导航内容覆盖到城市列表内容上方。

   ```ts
   Stack({ alignContent: Alignment.End }) {
     List({ scroller: this.cityScroller }) {
       // ...
     }
     // ...

     Column() {
       List({ scroller: this.navListScroller }) {
         // ...
       }
     }
     // ...
   }
   ```
4. 最后，给城市列表添加[sticky](../harmonyos-references/ts-container-list.md#sticky9)属性实现标题吸顶效果，及添加[onScrollIndex()](../harmonyos-references/ts-container-list.md#onscrollindex)方法，通过selectNavIndex变量与字母导航列表内容进行关联，控制的对应字母导航内容的选中状态。

   在字母导航列表中，添加点击事件，在点击事件中通过城市列表控制器cityScroller的[scrollToIndex()](../harmonyos-references/ts-container-scroll.md#scrolltoindex)事件，控制城市列表内容的改变，实现二者数据的联动效果。

   ```ts
   Stack({ alignContent: Alignment.End }) {
     List({ scroller: this.cityScroller }) {
       // ...
     }
     // ...
     .onScrollIndex((index: number) => {
       this.selectNavIndex = index - 2;
     })

     Column() {
       List({ scroller: this.navListScroller }) {
         ForEach(this.groupWorldList, (item: string, index: number) => {
           ListItem() {
             Text(item)
               // ...
               .onClick(() => {
                 this.selectNavIndex = index;
                 this.isClickScroll = true;
                 this.cityScroller.scrollToIndex(index + 2, false, ScrollAlign.START);
               })
           }
         }, (item: string) => item)
       }
     }
     // ...
   }
   ```

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/xajofzvIRhiYyNDepbjMyQ/zh-cn_image_0000002736432691.gif)

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

   ```ts
   List({ scroller: this.navTitleScroller }) {
     ForEach(this.categoryList, (item: NavTitleModel, index: number) => {
       ListItem() {
         Text(item.titleName)
           // ...
       }
     }, (item: NavTitleModel) => JSON.stringify(item.titleName))
   }
   // ...

   List({ scroller: this.goodsListScroller }) {
     ForEach(this.categoryList, (item: NavTitleModel) => {
       ListItemGroup({ space: 12, header: this.goodsHeaderBuilder(item.titleName) }) {
         ForEach(item.goodsList, (goodsItem: GoodsDataModel) => {
           ListItem() {
             Row() {
               Image(goodsItem.imgUrl)
                 // ...
               Column() {
                 Text(goodsItem.goodsName)
                   // ...
                 Text('￥' + goodsItem.price)
                   // ...
               }
               // ...
             }
             // ...
           }
         }, (goodsItem: GoodsDataModel) => JSON.stringify(goodsItem.goodsId))
       }
     }, (item: NavTitleModel) => JSON.stringify(item.goodsList))
   }
   ```
2. 给左侧导航列表添加点击事件，右侧分类详情列表添加[onScrollIndex()](../harmonyos-references/ts-container-list.md#onscrollindex)事件，并调用自定义事件listChange方法，在listChange方法内部根据isGoods变量的值，调用对应列表控制器的[scrollToIndex()](../harmonyos-references/ts-container-scroll.md#scrolltoindex)事件，实现导航列表和分类详情数据的联动效果。

   ```ts
   listChange(index: number, isGoods: boolean) {
     if (this.currentTitleId !== index) {
       this.currentTitleId = index;
       if (isGoods) {
         this.goodsListScroller.scrollToIndex(index);
       } else {
         this.navTitleScroller.scrollToIndex(index);
       }
     }
   }
   ```

   ```ts
   List({ scroller: this.navTitleScroller }) {
     ForEach(this.categoryList, (item: NavTitleModel, index: number) => {
       ListItem() {
         Text(item.titleName)
           // ...
           .onClick(() => {
             this.listChange(index, true);
           })
       }
     }, (item: NavTitleModel) => JSON.stringify(item.titleName))
   }
   // ...

   List({ scroller: this.goodsListScroller }) {
     // ...
   }
   // ...
   .onScrollIndex((index: number) => {
     this.listChange(index, false)
   })
   ```

**实现效果**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/WRRlJpKuQOSARvxl04AlSQ/zh-cn_image_0000002706673602.gif)

## 示例代码

* [基于List组件实现常见列表流场景](https://gitcode.com/harmonyos_samples/CommonListFlows)
