---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-tabs
title: 选项卡 (Tabs)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 构建布局 > 选项卡 (Tabs)
category: harmonyos-guides
scraped_at: 2026-09-05T06:13:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a25a168aa6760550815a04732d343257b5390314305aa3c208f675b4a444ee5d
---

## 概述

在日常开发中，开发者经常遇到使用Tabs作为导航的场景，包括多层嵌套的Tabs、自定义Tabs样式、Tabs数据加载和动态变更显示的Tabs等。

当页面信息较多时，为了让用户能够聚焦于当前显示的内容，需要对页面内容进行分类，提高页面空间利用率。[Tabs](../harmonyos-references/ts-container-tabs.md)组件可以在一个页面内快速实现视图内容的切换，一方面提升查找信息的效率，另一方面精简用户单次获取到的信息量。为了帮助开发者更直观和全面地理解Tabs组件，本文通过将这些场景整合到一个应用首页的具体实例中，展示Tabs组件的各项功能及其协同效果，以及与其他组件或数据的联动。

本文将从以下几个方面进行介绍。

* [布局方式](arkts-navigation-tabs.md#布局方式)
* [Tabs显示排版](arkts-navigation-tabs.md#tabs显示排版)
* [Tabs滑动](arkts-navigation-tabs.md#tabs滑动)
* [Tabs页签加载/更新](arkts-navigation-tabs.md#tabs页签加载更新)
* [Tabs切换动效](arkts-navigation-tabs.md#tabs切换动效)

## 布局方式

Tabs组件的页面组成包含两个部分，分别是[TabContent](../harmonyos-references/ts-container-tabcontent.md)和[TabBar](../harmonyos-references/ts-container-tabcontent.md#tabbar)。TabContent是内容页，TabBar是导航页签栏，页面结构如下图所示，根据不同的导航类型，布局会有区别，可以分为底部导航、顶部导航、侧边导航，其导航栏分别位于底部、顶部和侧边。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/slQPNhorTcyLLoh-sIyxHg/zh-cn_image_0000002742122615.png)

**说明** 

* TabContent组件不支持设置通用宽度属性，其宽度默认撑满Tabs父组件。
* TabContent组件不支持设置通用高度属性，其高度由Tabs父组件高度与TabBar组件高度决定。

Tabs使用花括号包裹TabContent，如图，其中TabContent显示相应的内容页。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/ivGNjTvcQYyd847VlBbgJg/zh-cn_image_0000002712243702.png)

每一个TabContent对应的内容需要有一个页签，可以通过TabContent的tabBar属性进行配置。在如下TabContent组件上设置tabBar属性，可以设置其对应页签中的内容，tabBar作为内容的页签。

```typescript
TabContent() {
  // app.string.homepage_content资源文件中的value值为“首页的内容”
  Text($r('app.string.homepage_content'))
    .fontSize(30)
}
// app.string.homepage资源文件中的value值为“首页”
.tabBar($r('app.string.homepage'))
```

设置多个内容时，需在Tabs内按照顺序放置。

```typescript
Tabs() {
  TabContent() {
    // app.string.homepage_content资源文件中的value值为“首页的内容”
    Text($r('app.string.homepage_content'))
      .fontSize(30)
  }
  // app.string.homepage资源文件中的value值为“首页”
  .tabBar($r('app.string.homepage'))

  TabContent() {
    // app.string.recommend_content资源文件中的value值为“推荐的内容”
    Text($r('app.string.recommend_content'))
      .fontSize(30)
  }
  // app.string.recommend资源文件中的value值为“推荐”
  .tabBar($r('app.string.recommend'))

  TabContent() {
    // app.string.discover_content资源文件中的value值为“发现的内容”
    Text($r('app.string.discover_content'))
      .fontSize(30)
  }
  // app.string.discover资源文件中的value值为“发现”
  .tabBar($r('app.string.discover'))

  TabContent() {
    // app.string.mine_content资源文件中的value值为“我的内容”
    Text($r('app.string.mine_content'))
      .fontSize(30)
  }
  // app.string.mine资源文件中的value值为“我的”
  .tabBar($r('app.string.mine'))
}
```

### 底部导航

底部导航是应用中最常见的一种导航方式。底部导航位于应用一级页面的底部，用户打开应用，能够分清整个应用的功能分类，以及页签对应的内容，并且其位于底部更加方便用户单手操作。底部导航一般作为应用的主导航形式存在，其作用是将用户关心的内容按照功能进行分类，迎合用户使用习惯，方便在不同模块间的内容切换。

**图3** 底部导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/SUQLmL1VQH6jNaJYeYY8mA/zh-cn_image_0000002742002655.gif)

导航栏位置使用Tabs的[barPosition](../harmonyos-references/ts-container-tabs.md#tabsoptions15)属性进行设置。默认情况下，导航栏位于顶部，此时，barPosition为BarPosition.Start。设置为底部导航时，需要将barPosition设置为BarPosition.End。

```typescript
Tabs({ barPosition: BarPosition.End }) {
  // TabContent的内容：首页、发现、推荐、我的
  // ···
}
```

底部导航栏可通过设置TabContent的[BottomTabBarStyle](../harmonyos-references/ts-container-tabcontent.md#bottomtabbarstyle9)来实现底部页签样式，详细示例请参考：[示例8（设置底部页签使用symbol图标）](../harmonyos-references/ts-container-tabcontent.md#示例8设置底部页签使用symbol图标)。

### 顶部导航

当内容分类较多，用户对不同内容的浏览概率相差不大，需要经常快速切换时，一般采用顶部导航模式进行设计，作为对底部导航内容的进一步划分，常见一些资讯类应用对内容的分类为关注、视频、数码，或者主题应用中对主题进行进一步划分为图片、视频、字体等。

**图4** 顶部导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/8en9ep-QQ5yrJgqZUS1z8A/zh-cn_image_0000002712403668.gif)

```typescript
Tabs({ barPosition: BarPosition.Start }) {
  // TabContent的内容:关注、视频、游戏、数码、科技、体育、影视
  // ···
}
```

### 侧边导航

侧边导航是应用较为少见的一种导航模式，更多适用于横屏界面，用于对应用进行导航操作，由于用户的视觉习惯是从左到右，侧边导航栏默认为左侧侧边栏。

**图5** 侧边导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/iGmCKUeNSJ6abqgo3k5LUg/zh-cn_image_0000002742122617.png)

实现侧边导航栏需要将Tabs的[vertical](../harmonyos-references/ts-container-tabs.md#vertical)属性设置为true，vertical默认值为false，表明内容页和导航栏垂直方向排列。

```typescript
  Tabs({ barPosition: BarPosition.Start }) {
    // TabContent的内容:首页、发现、推荐、我的
    // ···
  }
// ···
  .vertical(true)
  .barWidth(100)
  .barHeight(200)
```

**说明** 

* vertical为false时，tabbar的宽度默认为撑满屏幕的宽度，需要设置[barWidth](../harmonyos-references/ts-container-tabs.md#barwidth)为合适值。
* vertical为true时，tabbar的高度默认为实际内容的高度，需要设置[barHeight](../harmonyos-references/ts-container-tabs.md#barheight)为合适值。

## Tabs显示排版

在Tabs组件的应用场景中，开发者通常会自定义Tabs的布局和样式。本章节将介绍Tabs组件提供的几种常用的布局和样式功能。

### 页签对齐方式

当页签数量不足，无法铺满屏幕宽度或高度，或者铺满后影响到UI美观时，Tabs提供了自定义导航条页签对齐方式的API。例如，在应用的二级导航中，如果页签较少，可以考虑将页签居左对齐。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/APryvFibTZOYTHPlFH_4-w/zh-cn_image_0000002712243704.png)

**实现原理**

通过[barModifier](../harmonyos-references/ts-container-tabs.md#tabsoptions15)属性设置tabBar的align参数，可以实现页签对齐布局效果。类似于文本对齐，开发者可以自行设置居中、居上、居下、居左或者居右对齐。

**说明** 

* 只有在TabBar的barMode为BarMode.Scrollable时，这些设置才会生效。除此之外，还可以通过barModifier参数设置一系列的通用属性，具体参考：[TabsOptions](../harmonyos-references/ts-container-tabs.md#tabsoptions15)。
* 居上居下对齐仅在侧边导航栏中生效。若要控制顶部和底部导航栏中页签与顶部的距离，同样可以使用barModifier设置padding属性，以保持页签与TabBar顶部的特定间距。

**开发步骤**

定义tabBarModifier属性，并将其作为参数构造Tabs，然后通过tabBarModifier设置对齐方式。

```ts
@Component
export default struct InTabsComponent {
  // ...
  @State tabBarModifier: CommonModifier = new CommonModifier();
  // ...
  async aboutToAppear() {
    // ...
    this.tabBarModifier.margin({ right: 56 }).align(Alignment.Start);
    // ...
  }
  // ...
  build() {
    // ...
            Tabs({
              // ...
              barModifier: this.tabBarModifier
            }) {
              // ...
            }
            // ...
  }
}
```

### 自定义页签

对于底部导航栏，通常用于应用主页面的功能区分。为了更好的用户体验，开发者通常会自定义页签样式。开发者可以使用Tabs组件提供的定制页签样式的API，将页签自定义为图标加文字标题的形式，并且在选中和非选中的状态下，提供不同的样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/kCK4X-X-SbaQwW1nuU4OYQ/zh-cn_image_0000002742002657.gif)

**实现原理**

Tabs组件的[tabBar()](../harmonyos-references/ts-container-tabcontent.md#tabbar)方法接受联合类型的参数，可以将由@Builder修饰的UI构建函数作为参数传入，以自定义TabBar的样式。因此，开发者可以定义一个UI构建函数tabBuilder()，作为参数传递给[tabBar()](../harmonyos-references/ts-container-tabcontent.md#tabbar)方法。由于选中的页签和未选中的页签需要不同的样式，还需定义一个由@State修饰的数值型变量currentIndex，用于在tabBuilder()函数中判断当前页签是否被选中。当currentIndex发生变化时，能够触发tabBar样式的更新。最后，注册Tabs组件的onchange函数，在该函数中更新currentIndex的值。

**开发步骤**

1. 定义currentIndex属性。

   ```ts
   @Component
   export default struct OutTabsComponent {
     @State currentIndex: number = 0;
     // ...
   }
   ```
2. 定义@Builder装饰器修饰的自定义样式构建方法tabBuilder()。

   ```ts
   @Builder
   tabBuilder(index: number, name: string | Resource, icon: Resource) {
     Column() {

       SymbolGlyph(icon).fontColor([this.currentIndex === index
         ? $r('app.color.out_tab_bar_font_active_color')
         : $r('app.color.out_tab_bar_font_inactive_color')])
         .fontSize(25)

       Text(name)
         .margin({ top: 4 })
         .fontSize(10)
         .fontColor(this.currentIndex === index
           ? $r('app.color.out_tab_bar_font_active_color')
           : $r('app.color.out_tab_bar_font_inactive_color'))
     }
     .justifyContent(FlexAlign.Center)
     .height(Constants.FULL_HEIGHT)
     .width(Constants.FULL_WIDTH)
     .padding({ bottom: 60 })
   }
   ```
3. 将tabBuilder()方法传入Tabs，并在Tabs注册onChange()函数，并在其中更新currentIndex属性。

   ```ts
   Tabs({
     // ...
   }) {
     TabContent() {
       InTabsComponent({ switchNext: this.switchNext })
     }.tabBar(this.tabBuilder(0, $r('app.string.out_bar_text_home'), $r('sys.symbol.house')))
     // ...
   }
   // ...
   .onChange((index: number) => {
     this.currentIndex = index;
   })
   ```

### Tabs吸顶

在一些二级导航栏页面中，二级页签的内容上方通常会放置一些banner位或其他优先级较高的内容，并且在向上滑动时会退出显示区域。为了提供更好的用户体验，建议在上划的过程中，导航条能够吸附在顶部，便于用户进行内容切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/ajE3Z4ElR0KnN7ZDz5ZF9Q/zh-cn_image_0000002712403670.gif)

**实现原理**

开发者可以通过设置滑动组件的属性[nestedScroll](../harmonyos-references/ts-container-scroll.md#nestedscroll10)来控制父子组件的滑动顺序，从而实现吸顶效果。具体而言，需确保TabContent内容是可滑动的，并且Tabs的上层父组件也必须是可滑动的。为内容组件添加[nestedScroll](../harmonyos-references/ts-container-scroll.md#nestedscroll10)属性，设置为当向上滑动时父组件先动，而向下滑动时自己先动，从而实现滑动吸顶效果。

**开发步骤**

在Tabs父组件上嵌套Scroll组件，TabContent中的List组件显示内容，List组件本身是可滑动的，仅需设置其滑动触发行为即可。

```ts
Scroll() {
  Column() {
    BannerComponent()

    Stack({ alignContent: Alignment.TopEnd }) {
      // ...
      Column() {
        Tabs({
          // ...
        }) {
          ForEach(this.selectTabsViewModel.selectedTabs, (tab: TabItemViewModel, index: number) => {
            if (index === this.selectTabsViewModel.selectedTabs.length - 1) {
              TabContent() {
                List({ space: 10 }) {
                  // ...
                }
                // ...
                .nestedScroll({
                  scrollForward: NestedScrollMode.PARENT_FIRST,
                  scrollBackward: NestedScrollMode.SELF_FIRST
                })
              }
              // ...
            } else {
              // ...
            }
          }, (tab: TabItemViewModel, index: number) => index + '_' + JSON.stringify(tab))
        }
        // ...
      }
      .width(Constants.FULL_WIDTH)
      .height(Constants.FULL_HEIGHT)
      .backgroundColor($r('app.color.out_tab_bar_background_color'))
    }
  }
}
```

### TabsBar显示效果

在某些UI设计风格中，可能需要为TabBar采用特殊样式，比如首页导航栏的毛玻璃背景效果等。

* 通过设置Tabs组件的[barOverlap](../harmonyos-references/ts-container-tabs.md#baroverlap10)属性，可以实现TabBar变模糊并叠加在TabContent之上，并且配合[barBackgroundBlurStyle](../harmonyos-references/ts-container-tabs.md#barbackgroundblurstyle11)属性实现毛玻璃效果。详情请参见[TabBar背景模糊效果](../architecture-guides/tab_bar_blur-0000002257193008.md)。

  ```ts
  Tabs({
    // ...
  }) {
    // ...
  }
  // ...
  .barOverlap(true)
  .barBackgroundBlurStyle(BlurStyle.Thin)
  ```

  底部导航栏覆盖在内容上方，并具有毛玻璃效果。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/KlRiOLu3SrmTVgP9e046Cw/zh-cn_image_0000002742122619.gif)
* 通过[barModifier](../harmonyos-references/ts-container-tabs.md#tabsoptions15)设置tabBar的clip属性，实现页签超出tabBar区域显示效果。详情请参见[页签超出TabBar区域显示](../harmonyos-references/ts-container-tabs.md#示例15页签超出tabbar区域显示)。

  ```ts
  @Component
  export default struct OutTabComponent {
    // ...
    private controller: TabsController = new TabsController();

    aboutToAppear(): void {
      this.tabBarModifier.clip(false);
    }

    // ...

    build() {
      Column() {
        Tabs({
          // ...
          barModifier: this.tabBarModifier
        }) {
          // ...
        }
        // ...

      }
      .width('100%')
      .height('calc(100% + 60vp)')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
    }
  }
  ```

  底层导航栏图标可超出导航条范围。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/MIrrC8LOQXCFxXqNzhWsNw/zh-cn_image_0000002712243706.gif)
* 通过配置[fadingEdge](../harmonyos-references/ts-container-tabs.md#fadingedge10)(true)实现TabBar边缘渐隐。详情请参见[设置TabBar渐隐](../harmonyos-references/ts-container-tabs.md#示例5设置tabbar渐隐)。

  ```ts
  Tabs({controller: this.subController}){
    // ...
  }
  .fadingEdge(this.isFadingEdge)
  ```

  顶部导航栏页签靠近两侧会模糊化。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/cyr-7GRHRYm1LlFWaNdJcw/zh-cn_image_0000002742002659.gif)
* 通过TabsController的[setTabBarTranslate()](../harmonyos-references/ts-container-tabs.md#settabbartranslate13)、[setTabBarOpacity()](../harmonyos-references/ts-container-tabs.md#settabbaropacity13)方法可以设置TabBar偏移量及透明度。详情请参见[设置TabBar平移距离和不透明度](../harmonyos-references/ts-container-tabs.md#示例12设置tabbar平移距离和不透明度)。

  ```ts
  @Component
  export default struct InTabComponent {
    // ...
    private subController: TabsController = new TabsController();

    onDidBuild(): void {
      if (this.isSetTabBarTranslateAndOpacity) {
        this.subController.setTabBarTranslate({x:-20,y:30});
        this.subController.setTabBarOpacity(0.5);
      }
    }
    // ...

    build() {
      Tabs({controller: this.subController}){
        // ...
      }
      // ...
      .barMode(BarMode.Scrollable)
    }
  }
  ```

  顶部导航栏位置向左下偏移，并且呈现半透明效果。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/MgWOh6swTHe2uSPxLYSavA/zh-cn_image_0000002712403672.jpg)

**说明** 

在以下情况下，该设置无法生效：当显示内容过长时，通常会将其置于可滚动容器组件中，并在向上滑动时隐藏TabBar，向下滑动时显示。此时，会使用[bindTabsToScrollable](../harmonyos-references/arkts-apis-uicontext-uicontext.md#bindtabstoscrollable13)或[bindTabsToNestedScrollable](../harmonyos-references/arkts-apis-uicontext-uicontext.md#bindtabstonestedscrollable13)等接口将Tabs组件与可滚动容器组件绑定。由于TabBar的控制与滚动组件联动，通过setTabBarOpacity接口设置的TabBar偏移量和不透明度将不再生效。

## Tabs滑动

Tabs组件在用户交互方面提供了丰富的特性，其中与滑动动作相关的交互尤为常见。下文将介绍几种与Tabs和滑动动作相关的特性。

### 固定导航栏

当内容分类较为固定且不具有拓展性时，例如底部导航内容分类一般固定，分类数量一般在3-5个，此时使用固定导航栏。固定导航栏不可滚动，无法被拖拽滚动，内容均分tabBar的宽度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/I29CtEgTQL2naoqr7-DNEA/zh-cn_image_0000002742122621.gif)

Tabs的[barMode](../harmonyos-references/ts-container-tabs.md#barmode10)属性用于控制导航栏是否可以滚动，默认值为BarMode.Fixed。

```typescript
Tabs({ barPosition: BarPosition.End }) {
  // TabContent的内容：首页、发现、推荐、我的
  // ···
}
.barMode(BarMode.Fixed)
```

### 双层Tabs嵌套滑动

在应用开发中，开发者经常遇到多层Tabs嵌套使用的场景。如果父子Tabs组件均需滑动切换时，开发者需要对父子Tabs的滑动切换行为进行约束，以避免冲突。通常做法是，让滑动操作优先切换子Tabs页签，当子Tabs页签切换到最后一个后，再触发父Tabs的页签切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/h62aTbsqQaK9p0zCyMmjUg/zh-cn_image_0000002712243708.gif)

**实现原理**

可以通过[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)结合[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)的changeIndex()方法实现双层Tabs的切换。具体操作为：开启子Tabs的滑动切换功能，同时关闭父Tabs的滑动切换。在子Tabs的第一个或者最后一个页面上添加PanGesture事件处理函数，用于判断滑动方向，并根据滑动方向使用TabsController的changeIndex()方法切换到父Tabs的相应页签。这样一来，子Tabs的中间页签滑动时，仅会触发子Tabs页签的切换，而最后一个页签的滑动则会通过changeIndex()方法间接触发父Tabs页签的切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/tR1Yr9MRSCWODDBNTu32JA/zh-cn_image_0000002742002661.png)

**开发步骤**

1. 外层Tabs组件中定义[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)属性，以及内层Tabs双向绑定的状态属性变量switchNext及其监听函数。当监听到需要切换页签时，利用TabsController切换到对应页签。因为本示例外层Tabs和内层Tabs封装到不同的自定义组件中了，所以需要@Link修饰的switchNext变量作为父子组件的交互媒介。

   ```ts
   @Component
   export default struct OutTabsComponent {
     // ...
     @State @Watch('onchangeSwitchNext') switchNext: boolean = false;
     // ...
     onchangeSwitchNext() {
       if (this.switchNext) {
         this.switchNext = false;
         this.tabsController.changeIndex(1);
       }
     }
     // ...
     build() {
       Tabs({
         // ...
         controller: this.tabsController,
       }) {
         TabContent() {
           InTabsComponent({ switchNext: this.switchNext })
         }.tabBar(this.tabBuilder(0, $r('app.string.out_bar_text_home'), $r('sys.symbol.house')))
         // ...
       }
       // ...
     }
   }
   ```
2. 内层Tabs组件在最后一个TabContent中注册滑动事件处理函数，监听向左滑动作，触发时修改switchNext变量值传递给外层Tabs组件触发切换。

   ```ts
   @Component
   export default struct InTabsComponent {
     // ...
     @Link switchNext: boolean;
     // ...
     build() {
       // ...
               Tabs({
                 // ...
               }) {
                 ForEach(this.selectTabsViewModel.selectedTabs, (tab: TabItemViewModel, index: number) => {
                   if (index === this.selectTabsViewModel.selectedTabs.length - 1) {
                     TabContent() {
                       // ...
                     }
                     .tabBar(this.tabBuilder(index, tab))
                     .gesture(PanGesture(new PanGestureOptions({ direction: PanDirection.Left })).onActionStart(() => {
                       this.switchNext = true;
                     }))
                     // ...
                   } else {
                     // ...
                   }
                 }, (tab: TabItemViewModel, index: number) => index + '_' + JSON.stringify(tab))
               }
               // ...
     }
   }
   ```
3. 注意滑动切换在自定义切换动画场景下失效，故需要注释掉切换动画函数注册。

   ```ts
   Tabs({
     barPosition: BarPosition.Start,
     controller: this.subsController,
     barModifier: this.tabBarModifier
   }) {
     // ...
   }
   .customContentTransition(this.customContentTransition)
   ```

### 可滚动Tabs页签栏+更多按钮

可滚动页签栏通常设置在顶部或侧边导航栏，当内容分类较多，屏幕显示区域无法完全展示所有分类页签时，该页签栏允许用户通过滚动来访问隐藏的页签内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/AzVVdZxURZ-0PYRWNiS8Sw/zh-cn_image_0000002712403674.gif)

**实现原理**

通过将Tabs组件的[barMode](../harmonyos-references/ts-container-tabs.md#barmode)属性设置为BarMode.Scrollable，可以实现可滚动的页签栏。若要实现添加更多按钮的效果，可以通过Stack布局结合[barModifier](../harmonyos-references/ts-container-tabs.md#tabsoptions15)功能实现。具体做法是在Tabs组件的TabBar位置的末端上层利用Stack布局添加更多按钮，并且点击该按钮时可以弹出窗口，在弹窗中自定义需要显示的页签。

**开发步骤**

设置barMode属性为BarMode.Scrollable，并利用[Stack](arkts-layout-development-stack-layout.md)布局在TabBar右上角添加更多按钮。

```ts
Stack({ alignContent: Alignment.TopEnd }) {
  Row() {
    Image($r('app.media.more'))
      // ...
      .onClick(() => {
        this.showSelectTabsComponent = !this.showSelectTabsComponent;
      })
  }
  // ...
  .zIndex(1)
  .bindSheet($$this.showSelectTabsComponent, this.sheetBuilder(), {
    detents: [SheetSize.MEDIUM, SheetSize.MEDIUM, 500],
    preferType: SheetType.BOTTOM,
    title: { title: $r('app.string.bind_sheet_title') },
    onWillDismiss: (dismissSheetAction: DismissSheetAction) => {
      this.selectTabsViewModel.updateSelectedTabs();
      if (this.selectTabsViewModel.selectedTabs.length > 0) {
        this.subsController.changeIndex(0);
      }
      dismissSheetAction.dismiss();
    }
  })
  Column() {
    Tabs({
      // ...
    }) {
      // ...
    }
    // ...
    .barMode(BarMode.Scrollable)
    // ...
  }
  .width(Constants.FULL_WIDTH)
  .height(Constants.FULL_HEIGHT)
  .backgroundColor($r('app.color.out_tab_bar_background_color'))
}
```

### 禁用TabContent左右滑动

默认情况下，导航栏支持滑动切换。当存在多级导航栏嵌套或导航栏中的其他组件需要占用滑动动作时，为避免滑动响应冲突，开发者可选择禁用Tabs组件的滑动切换功能。通过将Tabs组件的[scrollable](../harmonyos-references/ts-container-tabs.md#scrollable)属性设置为false，可以禁止通过滑动TabContent来切换页签。同样，若想禁用边缘回弹效果，可将[edgeEffect](../harmonyos-references/ts-container-tabs.md#edgeeffect12)的值设置为EdgeEffect.None。

示例代码：

```ts
build() {
  Tabs({
    // ...
  }) {
    // ...
  }
  // ...
  .scrollable(true)
  // ...
}
```

## Tabs页签加载/更新

在使用Tabs组件进行开发时，特别是当Tabs组件作为二级导航使用时，业务需求往往需要对Tabs的标签页进行更精细的控制。下文将介绍几种定制标签页显示逻辑的场景。

### 显示指定页签与预加载

Tabs组件的TabContent默认在首次切换到该标签页时加载。如果TabContent中的内容或初始化逻辑较为复杂，加载速度较慢，则会影响标签页切换的流畅性，进而影响用户体验。此时，如果应用能在切换前预加载相应的标签页，将显著提升使用流畅度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/MEIGSSfyTYWlRTo2V1ji7A/zh-cn_image_0000002742122623.png)

**实现原理**

通过[TabController](../harmonyos-references/ts-container-tabs.md#tabscontroller)的[preloadItem()](../harmonyos-references/ts-container-tabs.md#preloaditems12)方法可以预加载指定子节点。该方法参数为需要预加载的index数组，无参调用此方法时，会一次性加载所有指定的子节点。因此，为了性能考虑，建议分批加载子节点。代码示例这里做法是当切换到某页签时，预加载所选页签左右两侧的页签内容。

**开发步骤**

定义subsController属性，并在Tabs的onChange函数中调用[preloadItem()](../harmonyos-references/ts-container-tabs.md#preloaditems12)预加载当前页签两侧页签。

```ts
@Component
export default struct InTabsComponent {
  // ...
  private subsController: TabsController = new TabsController();
  // ...
  build() {
    // ...
            Tabs({
              // ...
              controller: this.subsController,
              // ...
            }) {
              // ...
            }
            // ...
            .onChange((index: number) => {
              this.focusIndex = index;
              this.tabBarItemScroller.scrollToIndex(index, true, ScrollAlign.CENTER);
              let preloadItems: number[] = [];
              if (index - 1 >= 0) {
                preloadItems.push(index - 1);
              }
              if (index + 1 < this.selectTabsViewModel.selectedTabs.length) {
                preloadItems.push(index + 1);
              }
              this.subsController.preloadItems(preloadItems);
            })
            // ...
  }
}
```

### 切换至指定页签

在不使用自定义导航栏时，默认的Tabs会实现切换逻辑。在使用了自定义导航栏后，默认的Tabs仅实现滑动内容页和点击页签时内容页的切换逻辑，页签切换逻辑需要自行实现。即用户滑动内容页和点击页签时，页签栏需要同步切换至内容页对应的页签。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/JrW7rMhmQniJ1pbiZ1B7Cg/zh-cn_image_0000002712243710.gif)

从API version 18开始，支持使用Tabs提供的[onSelected](../harmonyos-references/ts-container-tabs.md#onselected18)事件方法，监听索引index的变化，并将选中元素的index值传递给selectIndex，实现页签的切换。

```typescript
// 如需作为页面入口，请取消@Entry的注释并删除export关键字
// @Entry
@Component
export struct ContentPageNoAndTabLinkage {

  @State selectIndex: number = 0;
  @Builder tabBuilder(title: Resource, targetIndex: number) {
    Column() {
      Text(title)
        .fontColor(this.selectIndex === targetIndex ? '#1698CE' : '#6B6B6B')
    }
  }
  build() {
    NavDestination() {
      Column({ space: 12 }) {
        // ...
          Tabs({ barPosition: BarPosition.End }) {
            TabContent() {
              // app.string.homepage_content资源文件中的value值为“首页内容”
              Text($r('app.string.homepage_content')).width('100%').height('100%').backgroundColor('rgb(213,213,213)')
                .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
            // app.string.homepage资源文件中的value值为“首页”
            }.tabBar(this.tabBuilder($r('app.string.homepage'), 0))

            TabContent() {
              // app.string.discover_content资源文件中的value值为“发现内容”
              Text($r('app.string.discover_content')).width('100%').height('100%').backgroundColor('rgb(112,112,112)')
                .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
            // app.string.discover资源文件中的value值为“发现”
            }.tabBar(this.tabBuilder($r('app.string.discover'), 1))

            TabContent() {
              // app.string.recommend_content资源文件中的value值为“推荐内容”
              Text($r('app.string.recommend_content')).width('100%').height('100%').backgroundColor('rgb(39,135,217)')
                .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
            // app.string.recommend资源文件中的value值为“推荐”
            }.tabBar(this.tabBuilder($r('app.string.recommend'), 2))

            TabContent() {
              // app.string.mine_content资源文件中的value值为“我的内容”
              Text($r('app.string.mine_content')).width('100%').height('100%').backgroundColor('rgb(0,74,175)')
                .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
            }
            // app.string.mine资源文件中的value值为“我的”
            .tabBar(this.tabBuilder($r('app.string.mine'), 3))
          }
          .animationDuration(0)
          .backgroundColor('#F1F3F5')
          .onSelected((index: number) => {
            this.selectIndex = index;
          })
        // ...
      }
      .width('100%')
      // ...
    }
    // ...
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/q_Ng4GR7QXqXt8rIeSMdrA/zh-cn_image_0000002742002663.gif)

若希望不滑动内容页和点击页签也能实现内容页和页签的切换，可以将currentIndex传给Tabs的index参数，通过改变currentIndex来实现跳转至指定索引值对应的TabContent内容。也可以使用[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)，TabsController是Tabs组件的控制器，用于控制Tabs组件进行内容页切换。通过TabsController的changeIndex方法来实现跳转至指定索引值对应的TabContent内容。

```typescript
// ...
  @State currentIndex: number = 2;
  @State currentAnimationMode: AnimationMode = AnimationMode.CONTENT_FIRST;
  private controller: TabsController = new TabsController();

  // ...
              Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controller }) {
                // ...
              }
              .animationDuration(0)
              .height(300)
              .animationMode(this.currentAnimationMode)
              .onChange((index: number) => {
                this.currentIndex = index;
              })

              // app.string.ContentWillChange_animationMode资源文件中的value值为“动态修改animationMode”
              Button($r('app.string.ContentWillChange_animationMode')).width('50%').margin({ top: 20 })
                .onClick(()=>{
                  if (this.currentAnimationMode === AnimationMode.CONTENT_FIRST) {
                    this.currentAnimationMode = AnimationMode.ACTION_FIRST;
                  } else if (this.currentAnimationMode === AnimationMode.ACTION_FIRST) {
                    this.currentAnimationMode = AnimationMode.NO_ANIMATION;
                  } else if (this.currentAnimationMode === AnimationMode.NO_ANIMATION) {
                    this.currentAnimationMode = AnimationMode.CONTENT_FIRST_WITH_JUMP;
                  } else if (this.currentAnimationMode === AnimationMode.CONTENT_FIRST_WITH_JUMP) {
                    this.currentAnimationMode = AnimationMode.ACTION_FIRST_WITH_JUMP;
                  } else if (this.currentAnimationMode === AnimationMode.ACTION_FIRST_WITH_JUMP) {
                    this.currentAnimationMode = AnimationMode.CONTENT_FIRST;
                  }
                })

              // app.string.ContentWillChange_changeIndex资源文件中的value值为“动态修改index”
              Button($r('app.string.ContentWillChange_changeIndex')).width('50%').margin({ top: 20 })
                .onClick(() => {
                  this.currentIndex = (this.currentIndex + 1) % 4;
                })

              Button('changeIndex').width('50%').margin({ top: 20 })
                .onClick(() => {
                  let index = (this.currentIndex + 1) % 4;
                  this.controller.changeIndex(index);
                })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/HmwLzvvJSj2dEIyOu7JWpA/zh-cn_image_0000002712403676.gif)

开发者可以通过Tabs组件的[onContentWillChange](../harmonyos-references/ts-container-tabs.md#oncontentwillchange12)接口，设置自定义拦截回调函数。拦截回调函数在下一个页面即将展示时被调用，如果回调返回true，新页面可以展示；如果回调返回false，新页面不会展示，仍显示原来页面。

```typescript
Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controllerTwo }) {
  // ...
}
// ...
.onContentWillChange((currentIndex, comingIndex) => {
  if (comingIndex === 2) {
    return false;
  }
  return true;
})
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/A52uX9PFRwaA4BXenKEWJA/zh-cn_image_0000002742122625.gif)

### 增删Tabs页签

在日常的应用开发中，经常需要实现用户自定义选择频道的功能。通常，这些自定义选择的频道会通过Tabs组件来展示，因此需要动态地更新Tabs的页签。本示例设计了一对父子组件来演示这一功能。父组件负责显示页签及其内容，并在页签栏的最右侧设置一个“更多”按钮。点击此按钮会弹出一个窗口，供用户选择需要显示的页签。该弹窗内容由子组件提供，关闭弹窗后，父组件的页签将被更新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/azMB2v1xStKJYQFLL5NIjw/zh-cn_image_0000002712243712.gif)

**实现原理**

定义selectTabsViewModel对象，其中的数组allTabs表示所有可选择页签，数组selectedTabs表示选中的需要显示的页签，并通过[@Link](arkts-link.md)绑定到父组件InTabComponent和子组件SelectTabsComponent中。子组件SelectTabsComponent作为一个弹窗用于选择需要显示的页签。选择完成后，关闭弹窗并更新 selectTabsViewModel对象中的选中页签数组 selectedTabs，以触发父组件InTabComponent的页签更新。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/MnNqYLchTMSkR63VmWmLuA/zh-cn_image_0000002742002665.png)

**开发步骤**

1. 定义SelectTabsViewModel类，包含所有可选择页签数组allTabs属性，和需要显示的页签数组selectedTabs属性，及更新显示页签数组的方法updateSelectedTabs()。

   ```ts
   @Observed
   class TabItemArray extends Array<TabItemViewModel> {
   }

   @Observed
   export default class SelectTabsViewModel {
     allTabs: TabItemArray = new TabItemArray();
     selectedTabs: TabItemArray = new TabItemArray();
     // ...

     async loadTabs(ctx: Context) {
       // ...
     }

     updateSelectedTabs() {
       let tempTabs: TabItemViewModel[] = [];
       for (let tab of this.allTabs) {
         if (tab.isChecked) {
           tempTabs.push(tab);
         }
       }
       this.selectedTabs = tempTabs;
     }
   }
   ```
2. 在InTabsComponent中定义selectTabsViewModel属性，并且在aboutToAppear()方法中初始化。

   ```ts
   @Component
   export default struct InTabsComponent {
     @State selectTabsViewModel: SelectTabsViewModel = new SelectTabsViewModel();
     // ...
     async aboutToAppear() {
       // ...

       await this.selectTabsViewModel.loadTabs(this.ctx);
       // ...
     }
     // ...
   }
   ```
3. 利用ForEach组件将selectTabsViewModel.selectedTabs属性绑定到Tabs的页签上。

   ```ts
   Tabs({
     // ...
   }) {
     ForEach(this.selectTabsViewModel.selectedTabs, (tab: TabItemViewModel, index: number) => {
       if (index === this.selectTabsViewModel.selectedTabs.length - 1) {
         TabContent() {
           // ...
         }
         .tabBar(this.tabBuilder(index, tab))
         // ...
       } else {
         // ...
       }
     }, (tab: TabItemViewModel, index: number) => index + '_' + JSON.stringify(tab))
   }
   ```
4. 在更多按钮的弹窗中初始化SelectTabsComponent，并将selectTabsViewModel属性作为双向绑定属性传入。在关闭弹窗处理函数中调用selectTabsViewModel.updateSelectedTabs()方法，更新需要显示的组件。

   ```ts
   @Builder
   sheetBuilder() {
     SelectTabsComponent({ selectTabsViewModel: this.selectTabsViewModel })
   }
   build() {
     Scroll() {
       Column() {
         BannerComponent()

         Stack({ alignContent: Alignment.TopEnd }) {
           Row() {
             Image($r('app.media.more'))
               // ...
               .onClick(() => {
                 this.showSelectTabsComponent = !this.showSelectTabsComponent;
               })
           }
           // ...
           .zIndex(1)
           .bindSheet($$this.showSelectTabsComponent, this.sheetBuilder(), {
             detents: [SheetSize.MEDIUM, SheetSize.MEDIUM, 500],
             preferType: SheetType.BOTTOM,
             title: { title: $r('app.string.bind_sheet_title') },
             onWillDismiss: (dismissSheetAction: DismissSheetAction) => {
               this.selectTabsViewModel.updateSelectedTabs();
               if (this.selectTabsViewModel.selectedTabs.length > 0) {
                 this.subsController.changeIndex(0);
               }
               dismissSheetAction.dismiss();
             }
           })
           // ...
         }
       }
     }
     // ...
   }
   ```
5. 在SelectTabsComponent中将selectTabsViewModel.allTabs属性渲染成toggle组件，并且注册toggle组件的切换处理函数onChange()，在其中修改该页签的选择状态isChecked属性，供更新显示页签方法selectTabsViewModel.updateSelectedTabs()使用。

   ```ts
   @Component
   export default struct SelectTabsComponent {
     @State checkedChange: boolean = false;
     @Link selectTabsViewModel: SelectTabsViewModel;

     build() {
       Grid() {
         ForEach(this.selectTabsViewModel.allTabs, (tab: TabItemViewModel) => {
           GridItem() {
             Row() {
               Toggle({ type: ToggleType.Button, isOn: tab.isChecked }) {
                 // ...
               }
               // ...
               .onChange((isOn: boolean) => {
                 tab.isChecked = isOn;
                 this.checkedChange = !this.checkedChange;
               })
             }
           }
         }, (tab: TabItemViewModel, index: number) => index + '_' + JSON.stringify(tab))
       }
       .columnsTemplate(('1fr 1fr 1fr 1fr') as string)
       .height(Constants.FULL_HEIGHT)
     }
   }
   ```

### 控制页面缓存数

从API version 19开始，开发者可以通过[cachedMaxCount](../harmonyos-references/ts-container-tabs.md#cachedmaxcount19)接口，设置子组件的最大缓存个数和缓存模式。默认情况下Tabs创建时会一次性预加载所有TabContent，而且已加载的页面不会释放，可能会带来性能内存问题。此时可以设置[cachedMaxCount](../harmonyos-references/ts-container-tabs.md#cachedmaxcount19)属性控制缓存的页面数量，设置此属性后不会进行页面预加载，使用懒加载机制(仅切换到页面时才加载)，当切换页面时根据所设置的[TabsCacheMode](../harmonyos-references/ts-container-tabs.md#tabscachemode19枚举说明)决定保留缓存或者释放页面。

**说明** 

* TabsCacheMode枚举值为CACHE\_BOTH\_SIDE时，缓存当前显示的子组件和其两侧的子组件。
* TabsCacheMode枚举值为CACHE\_LATEST\_SWITCHED时，缓存当前显示的子组件和最近切换过的子组件。
* 存在翻页动画时，从页面1直接切换到页面3，翻页动画会包含页面2，页面2也会被加载，如果此时页面2不在缓存范围内，页面切换完成后会立马释放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/qIpp22mRQB2imu5Duio-qA/zh-cn_image_0000002712403678.gif)

```typescript
// 如需作为页面入口，请取消@Entry的注释并删除export关键字
// @Entry
@Component
export struct NumberOfCachesTabBar {
  build() {
    // ...
          Tabs({ barPosition: BarPosition.Start }) {
            TabContent() {
              MyComponent({ color: '#00CB87' })
            }.tabBar(SubTabBarStyle.of('green'))

            TabContent() {
              MyComponent({ color: '#007DFF' })
            }.tabBar(SubTabBarStyle.of('blue'))

            TabContent() {
              MyComponent({ color: '#FFBF00' })
            }.tabBar(SubTabBarStyle.of('yellow'))

            TabContent() {
              MyComponent({ color: '#E67C92' })
            }.tabBar(SubTabBarStyle.of('pink'))

            TabContent() {
              MyComponent({ color: '#FF0000' })
            }.tabBar(SubTabBarStyle.of('red'))
          }
          .width(360)
          .height(296)
          .backgroundColor('#F1F3F5')
          .cachedMaxCount(2, TabsCacheMode.CACHE_BOTH_SIDE)
          // ...
  }
}

@Component
struct MyComponent {
  private color: string = '';

  aboutToAppear(): void {
    console.info('aboutToAppear backgroundColor:' + this.color);
  }

  aboutToDisappear(): void {
    console.info('aboutToDisappear backgroundColor:' + this.color);
  }

  build() {
    Column()
      .width('100%')
      .height('100%')
      .backgroundColor(this.color)
  }
}
```

基于以上示例代码为例，不同场景下的缓存策略如下：

1. 如图所示，使用默认翻页动画，CACHE\_BOTH\_SIDE模式，n设置为2，点击TabBar切换到yellow页，TabContent1~3被缓存。再切换到red页，TabContent1、2释放，TabContent3~5被缓存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/NiiCRweaR1yT5JtKBtSNDA/zh-cn_image_0000002742122627.png)
2. 如图所示，使用默认翻页动画，CACHE\_LATEST\_SWITCHED模式，n设置为2，点击TabBar切换到yellow页，TabContent1、3被缓存，TabContent2释放。再切换到red页，TabContent1、3、5被缓存，TabContent4释放。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/rUVjKyUhT4CfJ0Z4vwjyUw/zh-cn_image_0000002712243714.png)
3. 如图所示，关闭翻页动画，CACHE\_BOTH\_SIDE模式，n设置为2，点击TabBar切换到yellow页，TabContent1、3被缓存。再切换到red页，TabContent3、5被缓存，TabContent1释放。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/rXGKzEVPTA6lNfg_OZABPw/zh-cn_image_0000002742002667.png)
4. 如图所示，关闭翻页动画，CACHE\_LATEST\_SWITCHED模式，n设置为2，点击TabBar切换到yellow页，TabContent1、3被缓存。再切换到red页，TabContent1、3、5被缓存。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/5aClHHcyTNGXHGQvTiMbGA/zh-cn_image_0000002712403680.png)

## Tabs切换动效

### TabContent切换动画

Tabs 自带的页签切换动画为平移动画。若开发者需实现更高级的动画效果，可通过Tabs提供的API实现自定义动画。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ru3wGLa0TVSGS0Bmiv8OhA/zh-cn_image_0000002742122629.gif)

**实现原理**

使用[customContentTransition()](../harmonyos-references/ts-container-tabs.md#customcontenttransition11)函数来自定义Tabs页面的切换动画。本场景采用属性动画实现，开发者可以定义由@State修饰的可动画属性，并在build()方法中将这些属性绑定到对应的页签上。这里，淡入淡出动画选用了TabContent的尺寸属性scale和透明度属性opacity作为生成动画属性。然后，在[customContentTransition()](../harmonyos-references/ts-container-tabs.md#customcontenttransition11)函数中，设置动画的起始帧和结束帧对应的可动画属性值，系统将自动补全中间帧从而生成动画。关于属性动画详情可参考：[实现属性动画](arkts-attribute-animation-apis.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/yzsKnVN5SHmxLDQa5z1TKw/zh-cn_image_0000002712243716.png)

**说明** 

* 使用自定义切换动画时，Tabs组件的默认切换动画将被禁用，且页面将无法通过手势滑动切换。
* 将customContentTransition设置为undefined表示不使用自定义切换动画，继续使用组件自带的默认切换动画。
* 当前自定义切换动画不支持中途打断。
* 目前，自定义切换动画仅支持以下两种触发场景：点击页签或通过调用TabsController.changeIndex()方法。

**开发步骤**

1. 定义动画所需用到的属性数组。

   ```ts
   @Component
   export default struct InTabsComponent {
     // ...
     @State scaleList: number[] = [];
     @State opacityList: number[] = [];
     // ...
   }
   ```
2. 将属性数组绑定到对应的页签上。

   ```ts
   Tabs({
     // ...
   }) {
     ForEach(this.selectTabsViewModel.selectedTabs, (tab: TabItemViewModel, index: number) => {
       if (index === this.selectTabsViewModel.selectedTabs.length - 1) {
         TabContent() {
           // ...
         }
         // ...
         .opacity(this.opacityList[index])
         .scale({
           x: this.scaleList[index], y: this.scaleList[index]
         })
       } else {
         // ...
       }
     }, (tab: TabItemViewModel, index: number) => index + '_' + JSON.stringify(tab))
   }
   ```
3. 定义Tabs的自定义转场函数。

   ```ts
   @Component
   export default struct InTabsComponent {
     // ...
     @State scaleList: number[] = [];
     @State opacityList: number[] = [];
     // ...
     private animateDuration: number = 1000;
     private animateTimeout: number = 1000;
     private customContentTransition: (from: number, to: number) => TabContentAnimatedTransition =
       (from: number, to: number) => {
         let tabContentAnimatedTransition = {
           timeout: this.animateTimeout,
           transition: (proxy: TabContentTransitionProxy) => {
             this.scaleList[from] = 1.0;
             this.scaleList[to] = 0.5;
             this.opacityList[from] = 1.0;
             this.opacityList[to] = 0.5;
             this.getUIContext().animateTo({
               duration: this.animateDuration,
               onFinish: () => {
                 proxy.finishTransition();
               }
             }, () => {
               this.scaleList[from] = 0.5;
               this.scaleList[to] = 1.0;
               this.opacityList[from] = 0.5;
               this.opacityList[to] = 1.0;
             });
           }
         } as TabContentAnimatedTransition;
         return tabContentAnimatedTransition;
       };

     // ...
   }
   ```
4. 将转场函数作为参数传递给Tabs的customContentTransition()方法。

   ```ts
   Tabs({
     barPosition: BarPosition.Start,
     controller: this.subsController,
     barModifier: this.tabBarModifier
   }) {
     // ...
   }
   .customContentTransition(this.customContentTransition)
   ```

### 自定义Tabs页签切换联动

在自定义页签样式中，页签的选中和非选中状态显示样式不同时，页签的样式依赖于Tabs组件的切换动作。这种情况下，需要实现Tabs页签的联动，页签切换时，页签样式自动变更。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/I6DAc4iSTKKxaj2J9g0l-w/zh-cn_image_0000002742002669.gif)

**实现原理**

可以通过onChange事件，在切换页签时自定义TabBar和TabContent的联动效果。具体做法是定义一个由@State修饰的变量currentIndex，用于标识当前显示的页签索引。然后，利用onChange()方法注册处理函数，并在处理函数中更新currentIndex，确保其与当前选择的页签的索引一致。在页签样式的实现中，通过判断currentIndex变量与各页签索引是否相等来决定显示的样式，同时currentIndex属性的变化会触发页签样式的更新。

**开发步骤**

定义currentIndex属性，tabBuilder方法，并在onChange函数中更新currentIndex属性值。

```ts
@Component
export default struct OutTabsComponent {
  @State currentIndex: number = 0;
  // ...
  @Builder
  tabBuilder(index: number, name: string | Resource, icon: Resource) {
    Column() {

      SymbolGlyph(icon).fontColor([this.currentIndex === index
        ? $r('app.color.out_tab_bar_font_active_color')
        : $r('app.color.out_tab_bar_font_inactive_color')])
        .fontSize(25)

      Text(name)
        .margin({ top: 4 })
        .fontSize(10)
        .fontColor(this.currentIndex === index
          ? $r('app.color.out_tab_bar_font_active_color')
          : $r('app.color.out_tab_bar_font_inactive_color'))
    }
    // ...
  }
  build() {
    Tabs({
      // ...
    }) {
      // ...
    }
    // ...
    .onChange((index: number) => {
      this.currentIndex = index;
    })
    // ...
  }
}
```

## 支持适老化

在适老化大字体场景下，底部页签提供大字体弹窗显示内容。当组件识别到大字体时，基于设置的文字和图标等内容，构建长按提示弹窗。当用户长按弹窗后，滑动到下一个页签位置时，使用新页签的弹窗提示内容替换上一个页签提示内容，抬手关闭弹窗并切换到对应TabContent内容页。

**说明** 

弹窗只适用于底部页签[BottomTabBarStyle](../harmonyos-references/ts-container-tabcontent.md#bottomtabbarstyle9)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/X0UFMEAKS1GggafJUTF8Kw/zh-cn_image_0000002712403682.gif)

```typescript
// 如需作为页面入口，请取消@Entry的注释并删除export关键字
// @Entry
@Component
export struct AgeFriendlyTabs {
 
  build() {
    NavDestination() {
      Column() {
        Tabs({ barPosition: BarPosition.End }) {
          TabContent() {
            Column().width('100%').height('100%').backgroundColor(Color.Pink)
          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'OverLength'))
 
          TabContent() {
            Column().width('100%').height('100%').backgroundColor(Color.Yellow)
          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'SixLine'))
 
          TabContent() {
            Column().width('100%').height('100%').backgroundColor(Color.Blue)
          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Blue'))
 
          TabContent() {
            Column().width('100%').height('100%').backgroundColor(Color.Green)
          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos_app_icon'), 'Green'))
        }
        .vertical(false)
        .scrollable(true)
        .barMode(BarMode.Fixed)
        .width('100%')
        .backgroundColor(0xF1F3F5)
      }.width('80%').height(200)
      .margin({ top: 200 })
    }
  }
}
```

## 常见问题

### 如何实现页面懒加载效果

Tabs页面不支持懒加载。 若要实现页面懒加载效果，可以通过自定义TabBar与[Swiper](arkts-layout-development-create-looping.md)组件结合[LazyForEach](arkts-rendering-control-lazyforeach.md)来实现页面的懒加载和释放。在使用Tabs组件时，仅保留TabBar，TabContent部分留空，用Swiper组件替代TabContent以显示内容。定义一个数值属性currentIndex，利用[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)、[SwiperController](../harmonyos-references/ts-container-swiper.md#swipercontroller)及onchange函数，使其同时绑定Tabs组件和Swiper组件，从而实现联动。这是因为Swiper组件内支持LazyForEach组件，而原生Tabs组件不支持。在Swiper中利用LazyForEach显示内容，以实现Tabs的懒加载效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/8PwcDXkCS2yEVI2sL8R5HA/zh-cn_image_0000002742122631.png)

详情请参见[页面懒加载和释放](../harmonyos-references/ts-container-tabs.md#示例13页面懒加载和释放)。

## 示例代码

* [基于Tabs组件实现常见导航样式](https://gitcode.com/HarmonyOS_Samples/multi-tab-navigation)
* [基于Tab组件实现增删Tab的功能](https://gitcode.com/HarmonyOS_Samples/handle-tabs)
