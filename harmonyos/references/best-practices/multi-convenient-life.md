---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/multi-convenient-life
title: 多设备便捷生活界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备便捷生活界面
category: best-practices
scraped_at: 2026-09-02T15:03:19+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:5b39c9d1e805c6c62356a1f35a7f15a0efa7eac58ed1214ca5edc1769d7a70a1
---

## 概述

本文从目前流行的垂类市场中，选择便捷生活类应用作为典型案例详细介绍“一多”在实际开发中的应用。一多便捷生活应用包含首页展示、商品展示、图文详情、视频浏览等功能。本文选择美食列表页、店铺页、商品详情页、图文详情页、视频页等作为典型页面进行开发，遵循多设备的差异性、一致性、灵活性和兼容性，帮助开发者掌握“一多”能力。

便捷生活类应用对垂类内的核心功能进行了独特设计，以展示更多商品选择：

* 店铺页，多端适配不同形态的弹窗用以进行商品规格的选择，贴合用户交互习惯。

* 商品详情页，使用滑动伸缩方式展示商品图，突出商品样式，解决多端大图展示问题。
* 图文详情页，以多种形式实现“一多”布局并加入图片放大和沉浸式浏览的交互设计，让用户有更好的浏览体验。
* 视频详情页，模糊显示直播背景，统一页面主题，实现沉浸式观看。

当前系统的产品形态包括手机、折叠屏、平板。下文将围绕这些产品形态，从UX设计、架构设计、页面开发三个角度，给出符合“一多”应用的参考样例，介绍“一多”便捷生活应用的最佳实践。

* [UX设计](multi-convenient-life.md#section389361912304)章节介绍便捷生活应用的交互逻辑和设计要点，开发者可直接应用。
* [架构设计](multi-convenient-life.md#section161011524314)章节建议“一多”应用采用结构清晰的三层目录。
* [页面开发](multi-convenient-life.md#section380651612378)章节将页面划分为不同区域，按开发顺序介绍如何使用自适应布局和响应式布局实现不同的UI效果。

**说明** 

阅读本文前，开发者需熟悉[ArkUI（方舟UI框架）](../harmonyos-guides/arkui.md)和页面开发的“一多”能力（参考[一次开发，多端部署概览](bpta-multi-device-overview.md)）。下文将详细介绍它们在“一多”开发实践中如何使用。

## UX设计

便捷生活类的多设备响应式设计指南，参见文章[便捷生活类](../design-guides/convenient-life-0000001957252465.md)。

## 架构设计

HarmonyOS的分层架构包括产品定制层、基础特性层和公共能力层，构建清晰、高效、可扩展的设计架构。更多详情信息请参考[分层架构设计](bpta-layered-architecture-design.md)的逻辑设计。

## 页面开发

本章介绍便捷生活应用中如何使用“一多”的布局能力，完成页面层级的一套代码、多端适配。下文将从不同页面展开，介绍每个页面区域使用到具体的布局能力，帮助开发者从0到1进行便捷生活应用的开发。

### 布局能力

本节介绍不同页面的具体布局能力，帮助开发者进行便捷生活应用的开发。

**首页**

首页包含入口图标和商品卡片等页面跳转入口及商品推荐信息，帮助用户浏览和挑选商品。观察首页在不同设备上的UX设计图，可以进行以下设计：

* 将首页划分为5个区域，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 首页 |  |  |  |

  首页的5个基础区域介绍及实现方案如下表所示：

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部功能区 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，在lg断点采用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域。 |
  | 2 | 菜单列表 | 使用[Grid](../harmonyos-references/ts-container-grid.md)组件，借助栅格组件能力监听断点变化改变列数，设置aspectRatio属性实现缩放能力。 |
  | 3 | 秒杀列表 | [List](../harmonyos-references/ts-container-list.md)组件实现延伸能力。 |
  | 4 | 商品列表 | 使用[WaterFlow](../harmonyos-references/ts-container-waterflow.md)容器，实现一列到多列的切换。在sm断点下依赖断点控制设置WaterFlow的columnsTemplate属性为2，在md断点下设置columnsTemplate为3，在lg断点下设置columnsTemplate为4。 |
  | 5 | 菜单导航栏 | 借助[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)监听断点变化改变位置。 |

**美食列表**

美食列表页显示推荐美食。在大屏设备上，通过增加列数来优化布局，从而提升用户获取信息的效率。观察美食列表页在不同设备上的UX设计图，可以采取以下设计策略：

* 将美食列表页划分为3个区域，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 美食列表页 |  |  |  |

  美食列表页的3个基础区域介绍及实现方案如下表所示：

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部功能区 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，在lg断点采用[Blank](../harmonyos-references/ts-basic-components-blank.md)填充中间空白区域。 |
  | 2 | 菜单列表 | [List](../harmonyos-references/ts-container-list.md)组件实现延伸能力。 |
  | 3 | 美食列表 | 响应式布局的[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)布局，设置aspectRatio属性实现缩放能力。 |

**店铺页**

店铺页展示店铺信息和所有商品，侧边栏支持快速切换。用户可以选择商品规格，弹窗以不同形态显示，贴合操作习惯。观察店铺页在不同设备上的 UX 设计图，可以进行如下设计：

* 将店铺页划分为4个区域，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 店铺页 |  |  |  |
  | 店铺页-侧边栏 |  |  |  |
  | 店铺页-选规格 |  |  |  |

  店铺页的4个基础区域介绍及实现方案如下表所示：

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 店铺信息展示区 | 在父元素上使用[Flex](../harmonyos-references/ts-container-flex.md)组件实现挪移布局和visibility属性实现样式切换。 |
  | 2 | 菜单列表 | 使用[Tabs](../harmonyos-references/ts-container-tabs.md)组件嵌套[Scroll](../harmonyos-references/ts-container-scroll.md)组件实现顶部页签嵌套列表。 |
  | 3 | 购物车 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，在lg断点采用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域。 |
  | 4 | 选规格弹窗 | 使用[BindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)属性和[PopUp](../harmonyos-references/ts-universal-attributes-popup.md)属性实现不同设备上的弹窗显示。 |
* 店铺信息展示区

  使用Flex属性的direction属性根据断点切换上下或左右布局。使用visibility属性根据断点切换显隐。

  ```typescript
  Flex({
    direction: this.currentBreakpoint === BreakpointConstants.BREAKPOINT_LG && !this.ifShowSides ?
    FlexDirection.Row : FlexDirection.Column,
    justifyContent: FlexAlign.Start
  }) {
    ShopHeader()
      .visibility(this.currentBreakpoint !== BreakpointConstants.BREAKPOINT_LG || this.ifShowSides ?
      Visibility.Visible : Visibility.None)
    ShopSideBar()
      .width(CommonConstants.THIRTY_SEVEN_PERCENT)
      .flexShrink(0)
      .visibility(this.currentBreakpoint === BreakpointConstants.BREAKPOINT_LG && !this.ifShowSides ?
      Visibility.Visible : Visibility.None)
    ShopOrderList()
      .height(CommonConstants.FULL_PERCENT)
    // ...
  }
  ```
* 菜单列表

  使用Tabs嵌套Scroll组件实现菜单页签切换。

  ```typescript
  Tabs({ controller: this.topTabsController }) {
    ForEach(this.tabsList, () => {
      TabContent() {
        ShopMenu().width(CommonConstants.FULL_PERCENT)
      }
    })
  }
  ```

  ```typescript
  Row() {
    Column() {
      // ...
    }
    // ...
    Scroll(this.scroller) {
      Column() {
        // ...
      }
    }
    // ...
    .nestedScroll({ scrollForward: NestedScrollMode.PARENT_FIRST, scrollBackward: NestedScrollMode.SELF_FIRST })
  }
  ```
* 选规格弹窗

  在sm和md时使用bindSheet（半模态转场）组件实现。在lg规格屏幕使用PopUp实现跟手弹窗。

  ```typescript
  Text($r('app.string.select_specification'))
  // ...
    .onClick(() => {
      if (this.currentBreakpoint !== BreakpointConstants.BREAKPOINT_LG) {
        this.showPop = true;
      } else {
        this.showPopUp = true;
        this.showPopUpChange = true;
      }
    })
    .bindSheet($$this.showPop, this.popBuilder(), {
      height: SheetSize.FIT_CONTENT,
      backgroundColor: Color.White,
      title: {
        title: $r('app.string.select_specification')
      },
      maskColor: $r('app.color.forty_black')
    })
    .bindPopup(this.showPopUp, {
      builder: this.popBuilder,
      placement: Placement.Left,
      width: $r('app.float.popup_width'),
      mask: { color: $r('app.color.forty_black') },
      onStateChange: (e) => {
        if (!e.isVisible) {
          this.showPopUp = false;
        }
      }
    })
  ```

**商品详情**

商品详情页展示商品信息，加入上下滑动查看完整商品缩略图的交互设计，使商品全貌展现更直观。侧边栏可查看商品，交互更便捷。观察商品详情页在不同设备上的UX设计图，可以进行以下设计：

* 将商品详情页划分为3个区域，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 商品详情页 |  |  |  |
  | 商品详情页-侧边栏 |  |  |  |

  商品详情页包含3个基础区域，具体介绍及实现方案如下表所示：

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 商品信息展示区 | 绑定onScrollFrameBegin()监听滑动，改变图片高度，实现上下滑动查看缩略图的交互效果。 |
  | 2 | 商品信息区 | [Column](../harmonyos-references/ts-container-column.md)组件实现，内部使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，同时采用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域。 |
  | 3 | 购物车 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，同时采用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域。 |
* 效果图-交互动画（上下滑动查看完整缩略图）

  绑定onScrollFrameBegin()监听滑动，以改变图片高度：

  ```typescript
  @State ifPictureExpansion: Boolean = false;
  @State imageHeightExtension: number = 0;
  @State imageHeightFold: number = 0;
  @State imageHeight: number = 0;
  // ...
  build() {
    NavDestination() {
      Scroll(this.informationScroller) {
        GridRow({
          columns: this.currentBreakpoint === BreakpointConstants.BREAKPOINT_LG && !this.ifShowSides ?
          BreakpointConstants.GRID_ROW_COLUMNS[2] : 1
        }) {
          GridCol({
            span: this.currentBreakpoint === BreakpointConstants.BREAKPOINT_LG && !this.ifShowSides ?
            BreakpointConstants.GRID_COLUMN_SPANS[7] : 1
          }) {
            if (this.currentBreakpoint !== BreakpointConstants.BREAKPOINT_LG || this.ifShowSides) {
              DishHead({
                ifPictureExpansion: this.ifPictureExpansion,
                imageHeightExtension: this.imageHeightExtension,
                imageHeightFold: this.imageHeightFold,
                imageHeight: this.imageHeight
              })
            } else {
              DishSideBar()
            }
          }

          // ...
        }
      }
      // ...
      .onScrollFrameBegin((offset: number, state: ScrollState) => {
        if (!this.ifPictureExpansion && offset < 0) {
          this.imageHeight = this.imageHeightExtension;
          this.ifPictureExpansion = true;
          return { offsetRemain: 0 };
        } else if (this.ifPictureExpansion && offset > 0) {
          this.imageHeight = this.imageHeightFold;
          this.ifPictureExpansion = false;
          return { offsetRemain: 0 };
        } else {
          return { offsetRemain: offset };
        }
      })
    }
    // ...
  }
  ```

**微详情页**

微详情页显示推荐商品信息，不同设备上列数不同，以增加信息量。观察折叠屏上的UX设计图，可进行以下设计：

* 效果图如下：

| 示意图 | sm | md | lg |
| --- | --- | --- | --- |
| 微详情页 |  |  |  |

| 简介 | 实现方案 |
| --- | --- |
| 微详情页 | 使用[WaterFlow](../harmonyos-references/ts-container-waterflow.md)容器，实现一列到多列的切换。在sm断点下依赖断点控制设置WaterFlow的columnsTemplate属性为1，在md断点下设置columnsTemplate为2，在lg断点下设置columnsTemplate为3。 |

**电影列表页**

电影列表页展示推荐的电影信息，为LG规格的屏幕提供了三种设计范式，开发者可自行选择参考。观察电影列表页在不同设备上的UX设计图，可以进行如下设计：

* 将电影列表页划分为3个区域，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 电影列表页-范式1 |  |  |  |
  | 电影列表页-范式2 |  |  |  |
  | 电影列表页-范式3 |  |  |  |

  电影列表页的3个基础区域介绍及实现方案如下表所示

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部功能区 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，同时采用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域。 |
  | 2 | 即将上映 | [List](../harmonyos-references/ts-container-list.md)组件实现延伸能力，通过listDirection调整方向。 |
  | 3 | 正在热映 | 使用[WaterFlow](../harmonyos-references/ts-container-waterflow.md)容器，实现一列到多列的切换。在sm断点下依赖断点控制设置WaterFlow的columnsTemplate属性为1，在md断点下设置columnsTemplate为2，在lg断点下设置columnsTemplate为3。 |

**电影简介页**

电影简介页展示电影的具体信息，在LG规格的屏幕上采用左右布局，充分利用空间。观察电影简介页在不同设备上的UX设计图，可进行如下设计：

* 将电影简介页划分为3个区域，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 电影简介页 |  |  |  |

  电影简介页的3个基础区域介绍及实现方案如表所示：

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部功能区 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸。 |
  | 2 | 电影信息 | 利用响应式布局的栅格布局，使用[Grid](../harmonyos-references/ts-container-grid.md)组件实现挪移布局，设置aspectRatio属性实现缩放能力。 |
  | 3 | 电影详情区 | 使用tabs嵌套column，不同模块标题使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，同时采用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域。同多设备长视频界面 搜索发现，内容使用[List](../harmonyos-references/ts-container-list.md)组件实现延伸能力。 |

**选影院页**

选影院页展示影院列表供用户选择，并提供电影海报预览。观察选影院页在不同设备上的UX设计图，可以进行以下设计：

* 将选影院页划分为3个区域。效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 选影院页-范式1 |  |  |  |

  选影院页面的3个基础区域介绍及实现方案见下表：

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部功能区 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸。 |
  | 2 | 电影海报 | [Swiper](../harmonyos-references/ts-container-swiper.md)组件，指定displayCount属性实现占比能力，设置aspectRatio属性实现缩放能力。 |
  | 3 | 电影列表 | 使用[Tabs](../harmonyos-references/ts-container-tabs.md)组件+[List](../harmonyos-references/ts-container-list.md)组件，实现重复布局。 |

**首页-推荐页**

首页-推荐页展示推荐的图文简略信息，不同设备上以不同列数呈现，增加信息量。观察首页-推荐页在不同设备上的UX设计图，可以进行如下设计：

* 将首页-推荐页划分为3个区域，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 首页-推荐页 |  |  |  |

  推荐页的3个基础区域及其实现方案见下表：

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部功能区 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，同时采用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域。 |
  | 2 | 推荐展示区 | 使用[WaterFlow](../harmonyos-references/ts-container-waterflow.md)容器，实现一列到多列的切换。在sm断点下依赖断点控制设置WaterFlow的columnsTemplate属性为2，在md断点下设置columnsTemplate为3，在lg断点下设置columnsTemplate为4。 |
  | 3 | 菜单导航栏 | 通过监听断点的变化来调整菜单导航栏的位置。 |

  **首页-关注页**

  首页-关注页展示用户的关注列表及其最新发布的图文信息。提供了三种范式，开发者可自行选择参考。观察首页-关注页在不同设备上的UX设计图，可以进行如下设计：

  + 将首页-关注页划分为4个区域，效果图如下：

    | 示意图 | sm | md | lg |
    | --- | --- | --- | --- |
    | 首页-关注页-范式1 |  |  |  |
    | 首页-关注页-范式2 |  |  |  |
    | 首页-关注页-范式3 |  |  |  |

    首页的4个基础区域介绍及实现方案见下表：

    | 编号 | 简介 | 实现方案 |
    | --- | --- | --- |
    | 1 | 顶部功能区 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，同时采用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域。 |
    | 2 | 关注列表 | [List](../harmonyos-references/ts-container-list.md)组件实现延伸能力。 |
    | 3 | 关注详情 | 使用[List](../harmonyos-references/ts-container-list.md)组件实现重复布局。 |
    | 4 | 菜单导航栏 | 通过监听断点的变化来调整菜单导航栏的位置。 |

**短视频详情页**

短视频详情页提供视频播放及相关功能按钮，支持边看视频边看评论的页面设计。观察短视频页在不同设备上的UX设计图，设计如下：

* 将短视频页划分为4个区域，具体效果如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 短视频详情页-范例1 |  |  |  |
  | 短视频详情页-范例2 |  |  |  |
  | 侧边栏-评论 |  |  |  |
  | 短视频详情页-标签页信息栏 |  |  |  |

  短视频详情页包含4个基础区域，具体介绍及实现方案如下表所示：

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 短视频展示区 | 使用[Stack](../harmonyos-references/ts-container-stack.md)组件实现Video组件和Text组件、Image组件的堆叠效果，其中Video组件使用.align(Alignment.Center)实现居中。 |
  | 2 | 菜单导航栏 | 通过监听断点的变化来调整菜单导航栏的位置。 |
  | 3 | 视频评论区 | 使用[List](../harmonyos-references/ts-container-list.md)组件实现重复布局，在sm规格使用bindSheet实现半模态，在md和lg规格下使用[Row](../harmonyos-references/ts-container-row.md)组件呈左右布局。 |
  | 4 | 标签页信息栏 | 使用[List](../harmonyos-references/ts-container-list.md)组件实现重复布局。 |

**直播页**

直播页播放直播并展示用户评论，背景使用模糊图片以增强观看体验。观察直播页在不同设备上的UX设计图，可以进行以下设计：

* 直播页划分为3个区域，具体效果如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 直播页 |  |  |  |

  直播页的基础区域介绍及实现方案如下表所示：

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 直播区 | 使用[Stack](../harmonyos-references/ts-container-stack.md)容器组件实现Video组件和Text组件、Image组件的堆叠效果，其中Video组件使用.align(Alignment.Center)实现居中，背景模糊效果参考下方代码。 |
  | 2 | 评论区 | 使用[List](../harmonyos-references/ts-container-list.md)组件实现重复布局。 |
  | 3 | 评论输入区域 | 使用[TextInput](../harmonyos-references/ts-basic-components-textinput.md)组件实现。 |

* 直播区-背景模糊效果

  ```typescript
  SideBarContainer(SideBarContainerType.Embed) {
    LivingComments()
      .width(this.currentBreakpoint === BreakpointConstants.BREAKPOINT_LG ?
      CommonConstants.FORTY_PERCENT_STRING : CommonConstants.THIRTY_SEVEN_PERCENT)
    LivingHome()
  }
  .width(CommonConstants.FULL_PERCENT)
  .backgroundImage($r('app.media.fm2_img'))
  .backgroundBlurStyle(BlurStyle.BACKGROUND_THICK, {
    colorMode: ThemeColorMode.DARK,
    adaptiveColor: AdaptiveColor.DEFAULT
  })
  .backgroundImageSize({
    width: CommonConstants.FULL_PERCENT,
    height: CommonConstants.FULL_PERCENT
  })
  ```

**图文详情页**

图文详情页展示商品具体信息。观察不同设备上的UX设计图，可以进行如下设计：

* 将图文详情页划分为7个区域，效果图如下：

  | 示意图 | sm | md | lg |
  | --- | --- | --- | --- |
  | 图文详情页 |  |  |  |
  | 图文详情页-上图下文 |  |  |  |
  | 侧边栏-商品详情 |  |  |  |
  | 侧边栏-个人主页 |  |  |  |

  图文详情页的7个基础区域及其实现方案如下表所示：

  | 编号 | 简介 | 实现方案 |
  | --- | --- | --- |
  | 1 | 顶部功能区 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸，同时采用[Blank](../harmonyos-references/ts-basic-components-blank.md)组件填充中间空白区域。 |
  | 2 | 图片展示区 | [Swiper](../harmonyos-references/ts-container-swiper.md)组件，设置aspectRatio属性实现缩放能力。 |
  | 3 | 文章详情 | 使用column组件展示文章详情。 |
  | 4 | 底部功能区 | 使用[拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力)结合断点控制元素尺寸。 |
  | 5 | 评论区 | 使用TextInput组件实现。 |
  | 6 | 商品详情 | 使用column组件，设置aspectRatio属性实现缩放能力。 |
  | 7 | 个人主页 | 使用[List](../harmonyos-references/ts-container-list.md)组件实现重复布局。 |
* 上图下文有三种范式，可以通过调节swiper展示

  | 范式一 | 范式二 | 范式三 |
  | --- | --- | --- |
  |  |  |  |
* 交互效果

  | 点击缩放 | 双指滑动缩放 | 上滑沉浸式浏览 |
  | --- | --- | --- |
  |  |  |  |

  ```typescript
  Image(item)
  // ...
    .onClick(() => {
      this.getUIContext().animateTo({
        duration: CommonConstants.ANIMATE_DURATION,
        curve: Curve.Friction
      }, () => {
        this.isFullScreen = true;
        this.fullImageIndex = index;
      });
    })
    .gesture(
      PinchGesture({ fingers: 2 })
        .onActionUpdate((event: GestureEvent) => {
          this.getUIContext().animateTo({
            duration: CommonConstants.ANIMATE_DURATION,
            curve: Curve.Friction
          }, () => {
            this.isFullScreen = true;
            this.fullImageIndex = index;
          });
        })
    )
  ```

## 示例代码

* [多设备便捷生活界面](https://gitcode.com/harmonyos_samples/multi-convenient-life)
