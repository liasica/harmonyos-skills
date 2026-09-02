---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-horizontal-vertical-scrolling-list
title: 基于List和Scroller实现双向滚动列表
breadcrumb: 最佳实践 > 行业场景解决方案 > 新闻阅读 > 基于List和Scroller实现双向滚动列表
category: best-practices
scraped_at: 2026-09-02T15:03:20+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:8454ebc72e60595a413eef0c692c87e8a82d61aae6c667d1a6ba4450778843eb
---

## 概述

在移动端应用开发中，经常需要展示包含多行多列的表格数据，例如汽车参数表、股票信息表等。这类表格的数据量通常较大，行列数量远超屏幕显示范围，需要同时支持纵向和横向滚动以便用户查看完整信息。

然而，当表格需要同时支持纵向和横向滚动（下文简称为双向滚动）时，单一列表组件无法满足需求。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/nTi7wZkPTn6x6Dri0o0S7A/zh-cn_image_0000002683157325.gif "点击放大")

本文基于List组件和Scroller控制器，封装核心组件[DualScrollTable](https://gitcode.com/HarmonyOS_Samples/DualScrollList/blob/master/tableview/src/main/ets/components/DualScrollTable.ets)（双向滚动列表组件）。提供满足基础功能的双向滚动列表解决方案，助力开发者快速实现表格双向滚动功能。

[DualScrollTable](https://gitcode.com/HarmonyOS_Samples/DualScrollList/blob/master/tableview/src/main/ets/components/DualScrollTable.ets)提供以下核心功能：

* 支持横向滚动联动：顶部列标题、当前行子列表、其他行子列表同步滚动，确保列对齐。
* 支持纵向滚动联动：左侧行名称与右侧数据行同步滚动，确保行对齐。
* 支持自定义表格样式：可配置分组标题、边框线、文本样式的外观（如颜色、字号、尺寸）。

## 实现原理

[DualScrollTable](https://gitcode.com/HarmonyOS_Samples/DualScrollList/blob/master/tableview/src/main/ets/components/DualScrollTable.ets)将表格拆分为"顶部横向列表+底部左右分区"三个独立的List区域，每个List/Scroll组件配备独立的[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)控制器。利用[onScrollFrameBegin()](../harmonyos-references/ts-container-list.md#onscrollframebegin9)回调方法在列表滚动开始前拦截偏移量，再通过[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)方法将偏移量同步到关联列表，实现横向和纵向双向联动。

### 布局结构

双向滚动列表的布局架构采用"顶部横向列表+底部左右分区"的三区域设计：

* 顶部区域：横向滚动列表（TopList），显示列标题（如车型名称），左侧固定显示"参数/车型"标题。
* 底部左侧区域：纵向滚动列表（LeftList），显示行标题（如车辆参数名称）。
* 底部右侧区域：纵向/横向滚动列表（RightList）。外层为横向排列的Scroll组件，控制RightList横向滚动；内层为纵向排列的List组件，控制RightList纵向滚动。List组件的每个ListItem均内嵌一个横向滚动的RightSubList，用于展示该行所有的列数据（如车辆参数信息）。

列表整体布局结构如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/LUlQSRxbRQey9eTFmoEijg/zh-cn_image_0000002652957852.png "点击放大")

### 关键API和模块介绍

* [List](../harmonyos-references/ts-container-list.md)组件：滚动列表容器，支持横向（[Axis](../harmonyos-references/ts-appendix-enums.md#axis).Horizontal）和纵向（[Axis](../harmonyos-references/ts-appendix-enums.md#axis).Vertical）滚动方向配置。
* [Scroller](../harmonyos-references/ts-container-scroll.md#scroller)控制器：List组件的滚动控制器，提供[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)、[currentOffset()](../harmonyos-references/ts-container-scroll.md#currentoffset)等方法用于精确控制滚动位置。
* [onScrollFrameBegin()](../harmonyos-references/ts-container-list.md#onscrollframebegin9)：List组件的回调接口，在每帧滚动开始前触发，可拦截并修改滚动偏移量，是实现滚动同步的核心入口。
* [LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)懒加载数据：是一种高性能列表渲染方式，配合组件复用，提升长列表渲染性能。
* [@ReusableV2装饰器：V2组件复用](../harmonyos-guides/arkts-new-reusablev2.md)：使用组件复用优化长列表渲染性能。

### 同步滚动时序图

同步滚动时序图，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/3wEc0YmATOuj80Ouo2zFjw/zh-cn_image_0000002653117762.png "点击放大")

* 横向滚动TopList时，通过[onScrollFrameBegin()](../harmonyos-references/ts-container-list.md#onscrollframebegin9)回调方法拦截滚动偏移量，调用RightList的[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)方法同步横向滚动。
* 横向滚动RightList时，通过[onScrollFrameBegin()](../harmonyos-references/ts-container-list.md#onscrollframebegin9)回调方法拦截滚动偏移量，调用TopList的[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)方法同步横向滚动。
* 纵向滚动LeftList时，通过[onScrollFrameBegin()](../harmonyos-references/ts-container-list.md#onscrollframebegin9)回调方法拦截滚动偏移量，调用RightList的[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)方法同步纵向滚动。
* 纵向滚动RightList时，通过[onScrollFrameBegin()](../harmonyos-references/ts-container-list.md#onscrollframebegin9)回调方法拦截滚动偏移量，调用LeftList的[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)方法同步纵向滚动。

## 自定义双向滚动列表实现

本章将介绍双向滚动列表DualScrollTable的封装关键代码和步骤，具体代码实现开发者可以参考[示例代码](bpta-horizontal-vertical-scrolling-list.md#section91421919195114)。为了让开发者理解本章节内容，首先简单介绍几个关键的自定义代码类：

* DualScrollTable：双向滚动列表组件封装，便于给不同场景使用。
* BaseTableViewModel：定义了不同区域列表的Scroller对象、列表之间同步滚动的方法，主要用于列表滚动的控制。
* TableDataModel：包含列表数据结构的定义，列表数据获取的方法。

### 定义数据类型与布局配置

在TableDataModel中定义TableGroup和TableRow类，用于封装分组数据与行数据，每行通过Scroller控制器关联横向滚动同步逻辑。

```typescript
/**
 * Table group data
 * Used to store the group name and array of parameter items under this group
 */
export class TableGroup {
  /**
   * Unique identifier for the group, used as LazyForEach key for stable component reuse
   */
  public id: string = '';
  /**
   * List data group name, e.g.: Basic Info, Body, Engine
   */
  public sticky: string = '';
  /**
   * Group data array, detailed parameters for different parameter items
   */
  public sub: TableRow[] = [];
  /**
   * Group sub data DataSource for inner LazyForEach rendering
   */
  public subDataSource: BasicDataSource<TableRow> = new BasicDataSource<TableRow>();

}
```

```typescript
/**
 * Table row data
 * Used to store the name and info for each parameter item
 */
export class TableRow {
  /**
   * Unique identifier for the row, used as LazyForEach key for stable component reuse
   */
  public id: string = '';
  /**
   * Parameter item name, e.g.: Dealer Quote, Stock Name
   */
  public part: string = '';
  /**
   * Detailed parameter info array, corresponding to parameter values for each column
   */
  public info: string[] = [];
  /**
   * Cell text color array, corresponding one-to-one with the info array
   * When not set, default cell color is used in RightSubList
   */
  public cellFontColors: ResourceColor[] = [];
}
```

在DualScrollTable中定义TableSceneConfig接口用于自定义表格样式，包括是否显示分割线、表格宽高等。

```typescript
/**
 * Table scene configuration interface
 * Used to customize display differences for different scenarios
 */
export interface TableSceneConfig {
  /**
   * Whether to use grouped list (ListItemGroup + sticky headers).
   * true: grouped list for multi-section tables (e.g. car spec).
   * false: flat list without ListItemGroup (e.g. stock table).
   */
  showGroupHeader: boolean;

  /**
   * Whether to show top list top border
   */
  showTopListTopBorder: boolean;

  /**
   * Whether to show top list bottom border
   */
  showTopListBottomBorder: boolean;

  /**
   * Whether to show vertical divider lines (column dividers)
   */
  showVerticalLine?: boolean;

  /**
   * Text style configuration
   */
  textStyleConfig?: TextStyleConfig;

  /**
   * Layout dimension configuration
   */
  layoutConfig: TableLayoutConfig;
}
```

```typescript
/**
 * Table layout configuration interface
 * Defines the dimensions of each table area to ensure row and column alignment
 */
export interface TableLayoutConfig {
  /**
   * Top horizontal list height (vp), also controls left title area height
   */
  topListHeight: number;

  /**
   * Left vertical list width (vp), also controls top title area width
   */
  leftListWidth: number;

  /**
   * Sub-component width (vp), shared by top list items and bottom sub-list items to ensure column alignment
   */
  listItemWidth: number;

  /**
   * Sub-list row height (vp), shared by left list rows and bottom sub-list rows to ensure row alignment
   */
  subListHeight: number;

  /**
   * Group header height (vp)
   */
  groupHeaderHeight?: number;
}
```

### 加载列表数据

在TableDataModel中定义了loadTableData()方法，主要负责从本地rawfile目录读取JSON文件并进行解析。

本文示例采用本地模拟数据（存放于工程rawfile目录下）以方便演示。在实际开发中，开发者可根据业务需求自行重构loadTableData()方法，例如将其替换为从网络接口异步获取数据。

```typescript
export class TableDataModel {
  /**
   * Load table data
   * @param context Application context
   * @param jsonFileName JSON data file name
   * @returns Group data array
   */
  static loadTableData(context: Context, jsonFileName: string): TableGroup[] {
    const groupDataArray: TableGroup[] = [];
    try {
      // 1. Read raw byte data of JSON file from rawfile
      const jsonData: Uint8Array = context.resourceManager.getRawFileContentSync(jsonFileName);
      // 2. Decode byte data to UTF-8 string
      const stringData: string = util.TextDecoder.create('utf-8').decodeToString(jsonData);
      // 3. Parse JSON string to raw data object array
      const rawData: RawTableData[] = JSON.parse(stringData) as RawTableData[];
      // 4. Convert raw data to model objects
      rawData.forEach((dataItem: RawTableData, groupIndex: number) => {
        const groupData: TableGroup = new TableGroup();
        groupData.id = `group_${groupIndex}`;
        groupData.sticky = dataItem.sticky;
        groupData.sub = dataItem.sub.map((subItem: RawTableItem, subIndex: number) => {
          const item: TableRow = new TableRow();
          item.id = `row_${groupIndex}_${subIndex}`;
          item.part = subItem.part;
          item.info = subItem.info;
          return item;
        });
        groupDataArray.push(groupData);
      });
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      Logger.error(TAG, `loadTableData error: ${err.code}, ${err.message}.`);
    }
    return groupDataArray;
  }
}
```

### 构建布局列表

在DualScrollTable中采用Column嵌套Row布局方式，顶部放置TopList横向列表，底部Row内放置LeftList与RightList横向排列。同时定义BaseTableViewModel对象参数，用于后续在列表组件中调用同步滚动方法；定义TableSceneConfig对象参数，用于后续自定义表格样式。

```typescript
export struct DualScrollTable {
  /**
   * ViewModel instance, provides data and scroll synchronization logic,
   * must be provided externally with concrete implementation
   */
  @Param @Require viewModel: BaseTableViewModel;
  /**
   * Scene configuration
   */
  @Param config: TableSceneConfig = {
    // ...
  };
  // ...
  build() {
    Column() {
      this.TopList();
      Row() {
        this.LeftList();
        this.RightList();
      }
      .layoutWeight(1)
    }
  }
  // ...
}
```

关于UI布局和列表加载，下面仅以TopList为例进行简单介绍。本文重点讲解列表联动实现思路，UI布局的具体实现，开发者可参考[示例代码](bpta-horizontal-vertical-scrolling-list.md#section91421919195114)。TopList主要通过以下能力来实现：

* 使用LazyForEach循环渲染列表，提升了列表的整体性能。
* 给List绑定Scroller对象topListScroller，以便和其他列表进行滚动联动。
* 给列表设置可配置参数，如表格的宽度itemWidth、字体颜色fontColor、字体大小fontSize等。

```typescript
@Builder
TopList() {
  Row() {
    this.TopListHeader(this.viewModel.leftTitle);
    List({ scroller: this.viewModel.topListScroller }) {
      LazyForEach(this.viewModel.topListDataSource,
        (item: ResourceStr, _index: number) => {
          ListItem() {
             TopListItem({
              info: item,
              itemWidth: this.config.layoutConfig.listItemWidth,
              fontColor: this.config.textStyleConfig?.topListItemFontColor ?? DEFAULT_TOP_LIST_ITEM_FONT_COLOR,
              fontSize: this.config.textStyleConfig?.topListItemFontSize ?? $r('sys.float.Body_L'),
              fontWeight: this.config.textStyleConfig?.topListItemFontWeight ?? FontWeight.Medium
            }).reuse({ reuseId: () => TOP_TABLE_CELL_REUSE_ID })
          }
        },
        (_item: ResourceStr, index: number) => `top_${index}`)
    }
    .cachedCount(CommonConstants.LIST_HORIZONTAL_CACHED_COUNT)
    .listDirection(Axis.Horizontal)
    .width(`calc(100% - ${this.config.layoutConfig.leftListWidth}vp)`)
    .height('100%')
    // ...
}
```

### 定义滚动控制器对象

在BaseTableViewModel中给每个列表区域定义滚动控制器对象，便于控制列表横向和纵向联动。

```typescript
/**
 * Dual scroll table ViewModel base class
 * Provides common data loading and scroll synchronization logic
 */
export class BaseTableViewModel {
  /**
   * Top list horizontal scroller, syncs with rightAreaScroller
   */
  public topListScroller: Scroller = new Scroller();
  /**
   * Right area horizontal scroller, syncs with topListScroller
   */
  public rightAreaScroller: Scroller = new Scroller();
  /**
   * Left list vertical scroller, syncs with rightListScroller
   */
  public leftListScroller: Scroller = new Scroller();
  /**
   * Right list vertical scroller, syncs with leftListScroller
   */
  public rightListScroller: Scroller = new Scroller();
  // ...
}
```

### 同步列表横向滚动

1. 横向滚动顶部列表TopList时，底部右边列表RightList同步滚动。

   在TopList的[onScrollFrameBegin()](../harmonyos-references/ts-container-list.md#onscrollframebegin9)回调方法中获取列表滚动预估偏移量，调用syncTopListScrollToSubList()方法同步RightList横向滚动位置。

   ```typescript
   @Builder
   TopList() {
     Row() {
       this.TopListHeader(this.viewModel.leftTitle);
       List({ scroller: this.viewModel.topListScroller }) {
         // ...
       }
       // ...
       // Triggered before list scrolls, the list will scroll according to the actual scroll amount returned
       .onScrollFrameBegin((offset: number, _state: ScrollState) => {
         this.viewModel.syncTopListScrollToSubList(offset);
         return { offsetRemain: offset };
       })
     }
     // ...
   }
   ```

   调用RightList内Scroll组件的滚动控制器rightAreaScroller的scrollTo()方法，实现横向同步滚动。

   ```typescript
   public syncTopListScrollToSubList(offsetX: number): void {
     // Calculate target xOffset = current offset + per-frame delta
     const xOffset: number = offsetX + this.topListScroller.currentOffset().xOffset;
     this.scrollToX(this.rightAreaScroller, xOffset);
   }
   ```

   ```typescript
   private scrollToX(scroller: Scroller, xOffset: number): void {
     // ...
     scroller.scrollTo({ xOffset: xOffset, yOffset: 0, animation: false });
   }
   ```
2. 横向滚动右边列表RightList时，顶部列表TopList同步滚动。

   横向滚动右边列表RightList时，实际Scroll组件带着所有RightSubList一起滚动，所以需要在Scroll的[onScrollFrameBegin()](../harmonyos-references/ts-container-list.md#onscrollframebegin9)回调方法中获取列表滚动预估偏移量offset，同时调用syncSubListScrollToTopList()方法同步顶部列表TopList滚动。

   ```typescript
   @Builder
   RightGroupList() {
     Scroll(this.viewModel.rightAreaScroller) {
       List({ scroller: this.viewModel.rightListScroller }) {
         // ...
       }
       .onScrollFrameBegin((offset: number, _state: ScrollState) => {
         this.viewModel.syncRightListScrollToLeftList(offset);
         return { offsetRemain: offset };
       })
       // ...
     }
     // ...
   }
   ```

   在syncSubListScrollToTopList()中调用topListScroller的[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)方法，同步顶部列表TopList横向滚动。

   ```typescript
   public syncSubListScrollToTopList(offsetX: number): void {
     // Calculate target xOffset = current offset + per-frame delta
     const xOffset: number = offsetX + this.rightAreaScroller.currentOffset().xOffset;
     this.scrollToX(this.topListScroller, xOffset);
   }
   ```

   ```typescript
   private scrollToX(scroller: Scroller, xOffset: number): void {
     // ...
     scroller.scrollTo({ xOffset: xOffset, yOffset: 0, animation: false });
   }
   ```

### 同步列表纵向滚动

1. 纵向滚动左侧列表LeftList时，右侧列表RightList同步纵向滚动。

   在LeftList的[onScrollFrameBegin()](../harmonyos-references/ts-container-list.md#onscrollframebegin9)回调方法中获取列表滚动预估偏移量，调用syncBottomLeftScroll()方法。

   ```typescript
   @Builder
   LeftGroupList() {
     List({ scroller: this.viewModel.leftListScroller }) {
       // ...
     }
     .onScrollFrameBegin((offset: number, _state: ScrollState) => {
       this.viewModel.syncLeftListScrollToRightList(offset);
       return { offsetRemain: offset };
     })
     // ...
   }
   ```

   在syncLeftListScrollToRightList()中调用rightListScroller的[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)方法，使右侧列表RightList纵向同步滚动。

   ```typescript
   public syncLeftListScrollToRightList(offset: number): void {
     // Calculate target yOffset = current offset + per-frame delta
     const yOffset: number = this.leftListScroller.currentOffset().yOffset + offset;
     this.scrollToY(this.rightListScroller, yOffset);
   }
   ```

   ```typescript
   private scrollToY(scroller: Scroller, yOffset: number): void {
     // ...
     scroller.scrollTo({ xOffset: 0, yOffset: yOffset, animation: false });
   }
   ```
2. 纵向滚动右侧列表RightList时，左侧列表LeftList同步纵向滚动。

   在RightList下的[onScrollFrameBegin()](../harmonyos-references/ts-container-list.md#onscrollframebegin9)回调方法中获取列表滚动预估偏移量，调用syncBottomRightScroll()方法。

   ```typescript
   @Builder
   RightGroupList() {
     Scroll(this.viewModel.rightAreaScroller) {
       List({ scroller: this.viewModel.rightListScroller }) {
         // ...
       }
       .onScrollFrameBegin((offset: number, _state: ScrollState) => {
         this.viewModel.syncRightListScrollToLeftList(offset);
         return { offsetRemain: offset };
       })
       // ...
     }
     // ...
   }
   ```

   在syncRightListScrollToLeftList()中调用leftListScroller的[scrollTo()](../harmonyos-references/ts-container-scroll.md#scrollto)方法，使左侧列表LeftList纵向同步滚动。

   ```typescript
   public syncRightListScrollToLeftList(offset: number): void {
     // Calculate target yOffset = current offset + per-frame delta
     const yOffset: number = this.rightListScroller.currentOffset().yOffset + offset;
     this.scrollToY(this.leftListScroller, yOffset);
   }
   ```

   ```typescript
   private scrollToY(scroller: Scroller, yOffset: number): void {
     // ...
     scroller.scrollTo({ xOffset: 0, yOffset: yOffset, animation: false });
   }
   ```

以上完成了DualScrollTable组件的封装，下面将通过使用它分别实现汽车参数表格和股票信息表格场景。

## 股票信息表格场景实现

### 场景描述

在股票行情场景中，多只股票的最新价、涨跌额、涨跌幅等指标需要横向排列展示。该场景不启用分组标题和列分割线，表格布局尺寸更紧凑。股票信息表如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/irMunKDMRYObDRmuSNI8Kw/zh-cn_image_0000002682997519.gif "点击放大")

### 开发步骤

1. 创建StockInfoTableViewModel并加载股票数据。

   继承BaseTableViewModel，在loadTableData()方法中调用loadData()方法加载stock.json数据。

   ```typescript
   /**
    * Stock info table column data
    */
   const STOCK_TOP_LIST_DATA: ResourceStr[] = [
     $r('app.string.stock_latest_price'),
     $r('app.string.stock_change'),
     $r('app.string.stock_change_rate'),
     $r('app.string.stock_total_volume'),
     $r('app.string.stock_current_volume'),
     $r('app.string.stock_turnover'),
     $r('app.string.stock_highest'),
     $r('app.string.stock_lowest'),
     $r('app.string.stock_today_open')
   ];

   /**
    * Stock info table ViewModel
    * Manages stock data loading and rise/fall color parsing
    */
   export default class StockInfoTableViewModel extends BaseTableViewModel {
     /**
      * Load table data
      * Initialize column headers and left title, load stock data from stock.json, and parse rise/fall colors
      * @param context Application context
      */
     public loadTableData(context: Context): void {
       this.loadData(context, 'stock.json');
       this.resolveCellFontColors();
       this.topListData = STOCK_TOP_LIST_DATA;
       this.leftTitle = $r('app.string.stock_name_title');
       this.syncTopListDataSource();
     }
     // ...
   }
   ```
2. 配置股票表格场景参数。

   通过TableSceneConfig配置隐藏以下元素：

   * 分组标题（showGroupHeader）：false。
   * 顶部列表的上边框（showTopListTopBorder）：false。
   * 顶部列表的下边框（showTopListBottomBorder）：false。
   * 列表纵向分割线（showVerticalLine）：false。

   通过LayoutConfig配置列表各区域的尺寸：

   * 顶部列表高度（topListHeight）：60vp。
   * 左侧列表宽度（leftListWidth）：90vp。
   * 表格列宽（listItemWidth）：100vp。
   * 表格行高（subListHeight）：60vp。

   ```typescript
   @ComponentV2
   struct StockInfoTable {
     /**
      * ViewModel instance
      */
     private viewModel: StockInfoTableViewModel = new StockInfoTableViewModel();
     // ...
     /**
       * Table scene configuration
      */
     private config: TableSceneConfig = {
       showGroupHeader: false,
       showTopListTopBorder: false,
       showTopListBottomBorder: false,
       showVerticalLine: false,
       layoutConfig: {
         topListHeight: 60,
         leftListWidth: 90,
         listItemWidth: 100,
         subListHeight: 60
       }
     };
     // ...
   }
   ```
3. 构建StockInfoTable页面并接入DualScrollTable。

   在NavDestination中添加StockTableToolbar工具栏组件和DualScrollTable表格组件，在aboutToAppear()方法中调用viewModel.loadTableData()方法加载数据。

   ```typescript
   @ComponentV2
   struct StockInfoTable {
     /**
      * ViewModel instance
      */
     private viewModel: StockInfoTableViewModel = new StockInfoTableViewModel();
     /**
      * UIAbility context, used to get resources
      */
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     /**
       * Table scene configuration
      */
     private config: TableSceneConfig = {
       // ...
     };
     aboutToAppear(): void {
       this.viewModel.loadTableData(this.context);
     }
     // ...

     build() {
       NavDestination() {
         Column() {
           this.StockTableToolbar()

           DualScrollTable({
             viewModel: this.viewModel,
             config: this.config
           }).padding({ bottom: $r('sys.float.padding_level24') })
         }
       }
       .title($r('app.string.stock_table_scene_title'))
     }
   }
   ```

## 汽车参数表格场景实现

### 场景描述

在车型配置对比场景中，开发者需要在同一页面展示多个车型的参数信息，参数项按分组（基本信息、车身、发动机等）排列，每个参数项对应多个车型的数值。

左侧参数名称与右侧数据行纵向同步滚动，顶部车型名称与底部数据列横向同步滚动。汽车参数表如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/-L_mExsIR1WYqf_JhwZSPQ/zh-cn_image_0000002683157331.gif "点击放大")

### 开发步骤

1. 创建CarSpecTableViewModel并加载车型数据。

   继承BaseTableViewModel，在loadTableData()方法中调用loadData()方法加载car.json数据。

   ```typescript
   export default class CarSpecTableViewModel extends BaseTableViewModel {
     /**
      * Load table data
      * Load car spec data from car.json and dynamically generate column headers
      * @param context Application context
      */
     public loadTableData(context: Context): void {
       this.loadData(context, 'car.json');
       this.topListData = [];
       if (this.groupDataArray[0]?.sub[0]?.info?.length > 0) {
         const count: number = this.groupDataArray[0].sub[0].info.length;
         for (let i = 1; i <= count; i++) {
           this.topListData.push($r('app.string.car_model_name', i));
         }
         this.leftTitle = $r('app.string.car_count_title', this.topListData.length);
       }
       this.syncTopListDataSource();
     }
   }
   ```
2. 在汽车参数列表页面中配置车型表格场景参数。

   通过TableSceneConfig配置显示分组标题（showGroupHeader）、顶部列表的上边框（showTopListTopBorder），隐藏顶部列表的下边框（showTopListBottomBorder）。

   通过layoutConfig配置列表的布局尺寸（如表格条目宽度listItemWidth为155vp）。

   ```typescript
   @ComponentV2
   struct CarSpecTable {
     /**
      * ViewModel instance
      */
     private viewModel: CarSpecTableViewModel = new CarSpecTableViewModel();
     // ...
     /**
      * Table scene configuration
      */
     private config: TableSceneConfig = {
       showGroupHeader: true,
       showTopListTopBorder: true,
       showTopListBottomBorder: false,
       layoutConfig: {
         topListHeight: 80,
         leftListWidth: 100,
         listItemWidth: 155,
         subListHeight: 80,
         groupHeaderHeight: 44
       }
     };
     // ...
   }
   ```
3. 在汽车参数列表页面中使用DualScrollTable组件。

   在aboutToAppear()方法中调用viewModel.loadTableData()方法加载数据，将viewModel和config传入DualScrollTable组件。

   ```screen
   @ComponentV2
   struct CarSpecTable {
     /**
      * ViewModel instance
      */
     private viewModel: CarSpecTableViewModel = new CarSpecTableViewModel();
     /**
      * UIAbility context, used to get resources
      */
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     /**
      * Table scene configuration
      */
     private config: TableSceneConfig = {
       // ...
     };
     aboutToAppear(): void {
       this.viewModel.loadTableData(this.context);
     }

     build() {
       NavDestination() {
         DualScrollTable({
           viewModel: this.viewModel,
           config: this.config
         })
       }
       .title($r('app.string.car_table_scene_title'))
     }
   }
   ```

## 性能检测

双向滚动列表在数据量较大的场景下，因加载组件较多，易导致滚动卡顿和掉帧。因此，开发完成后需进行性能检测。开发者可使用[应用与元服务体检](../harmonyos-guides/ide-app-analyzer.md)工具AppAnalyzer，或通过性能调优工具DevEco Profile的[Frame分析](../harmonyos-guides/ide-insight-session-frame.md)功能进行性能测试。

本示例通过Frame分析结果显示，卡顿帧数为0，滚动过程流畅，无卡顿或掉帧现象。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Qz22o5cHQa6pIciPUHTjzw/zh-cn_image_0000002652957856.png "点击放大")

## 示例代码

* [基于List和Scroller实现双向滚动列表](https://gitcode.com/HarmonyOS_Samples/DualScrollList)
