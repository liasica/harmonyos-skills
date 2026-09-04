---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-lazyvgridlayout
title: LazyVGridLayout
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 滚动与滑动 > LazyVGridLayout
category: harmonyos-references
scraped_at: 2026-09-05T06:17:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:518dcc0569fac15e5b322310288202cce0615c2eb841d706f193be088d08b04e
---

该组件用于实现支持懒加载的网格布局，适用于在滚动容器中按需渲染大量网格项的场景，可减少首帧渲染时间和内存开销。

API版本26.0.0之前，其父组件支持[WaterFlow](ts-container-waterflow.md)和[FlowItem](ts-container-flowitem.md)组件，并支持使用自定义组件或[NodeContainer](ts-basic-components-nodecontainer.md)组件封装后应用在WaterFlow或FlowItem中。

从API版本26.0.0开始，其父组件新增支持[List](ts-container-list.md)、[Scroll](ts-container-scroll.md)和[LazyColumnLayout](ts-container-lazycolumnlayout.md)，同时新增支持使用自定义组件或[NodeContainer](ts-basic-components-nodecontainer.md)组件封装后应用在List、Scroll或LazyColumnLayout中。

更多关于懒加载布局的使用场景和完整示例，可参考[创建懒加载布局](../harmonyos-guides/arkts-layout-development-create-lazy-layout.md)。

**说明** 

* 该组件从API version 19开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 本模块接口仅可在Stage模型下使用。
* LazyVGridLayout组件高度默认自适应内容，不建议设置会固定或约束组件垂直方向尺寸的属性，设置后会导致显示异常或无法正常滚动。涉及的属性包括[height](ts-universal-attributes-size.md#height)、[size](ts-universal-attributes-size.md#size)中的height、[constraintSize](ts-universal-attributes-size.md#constraintsize)中的minHeight/maxHeight、[aspectRatio](ts-universal-attributes-layout-constraints.md#aspectratio)、[layoutWeight](ts-universal-attributes-size.md#layoutweight)，以及[height](ts-universal-attributes-size.md#height15)取[LayoutPolicy](ts-universal-attributes-size.md#layoutpolicy15)值的场景。
* 当父组件设置主轴方向尺寸时，LazyVGridLayout按照父组件可视区域进行懒加载；当父组件未设置主轴方向尺寸时，LazyVGridLayout会被内容撑开，导致所有子组件都会被加载布局。
* 该组件在不同父组件下的懒加载支持条件如下：

  1. 在WaterFlow组件下，仅在WaterFlow组件的单列模式或分段布局中的单列分段，并且布局方向[FlexDirection](ts-appendix-enums.md#flexdirection)设置为FlexDirection.Column的情况下支持懒加载。在WaterFlow的多列模式或横向布局（FlexDirection.Row或FlexDirection.RowReverse）下使用该组件，则不支持懒加载。此外，在布局方向为FlexDirection.ColumnReverse的WaterFlow组件下使用该组件会导致显示异常。
  2. 在List组件下，要求List组件布局方向必须是竖直方向（即[listDirection](ts-container-list.md#listdirection)属性设置为Axis.Vertical）。在非竖直方向的List中使用该组件会导致应用崩溃。当List设置了[lanes](ts-container-list.md#lanes9)、[chainAnimation](ts-container-list.md#chainanimation)、[scrollSnapAlign](ts-container-list.md#scrollsnapalign10)属性中的任意一个或多个时，该组件的懒加载功能会失效。
  3. 在Scroll组件下，要求Scroll组件布局方向必须是竖直方向（即[scrollable](ts-container-scroll.md#scrollable)属性设置为ScrollDirection.Vertical）。在非竖直方向的Scroll中使用该组件会导致应用崩溃。
* 当懒加载功能生效时，该组件仅加载父组件可视区域内的子组件，并在帧间空闲时隙预加载可视区域上方和下方各半屏的内容。
* 此处的父组件指最靠近当前组件的上层滚动组件，其他文档下的具体含义请参考对应内容。

## 接口

LazyVGridLayout()

创建垂直方向懒加载网格布局容器。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### columnsTemplate

columnsTemplate(value: string)

设置当前网格布局列的数量、固定列宽或最小列宽值，不设置时默认1列。

例如，'1fr 1fr 2fr' 表示将父组件分为3列，将父组件允许的宽度分为4等份，第一列占1份，第二列占1份，第三列占2份。

columnsTemplate('repeat(auto-fit, track-size)')是设置最小列宽值为track-size，自动计算列数和实际列宽。

columnsTemplate('repeat(auto-fill, track-size)')是设置固定列宽值为track-size，自动计算列数。

columnsTemplate('repeat(auto-stretch, track-size)')是设置固定列宽值为track-size，使用[columnsGap](ts-container-lazyvgridlayout.md#columnsgap)作为最小列间距，自动计算列数和实际列间距。

其中repeat、auto-fit、auto-fill、auto-stretch为关键字。track-size为列宽，支持的单位包括px、vp、%或有效数字，默认单位为vp，track-size至少包括一个有效列宽。

auto-fit模式和auto-stretch模式只支持track-size为一个有效列宽值，并且auto-stretch模式中的track-size只支持px、vp和有效数字，不支持%。auto-fill模式支持一个或多个有效列宽，如columnsTemplate('repeat(auto-fill, 20)')、columnsTemplate('repeat(auto-fill, 20 80px)')。

使用效果可以参考[示例3](ts-container-lazyvgridlayout.md#示例3设置自适应列数)。

设置为'0fr'时，该列的列宽为0，不显示子组件。设置为其他非法值时，子组件显示为固定1列。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 当前网格布局列的数量、固定列宽或最小列宽值。 |

### columnsGap

columnsGap(value: LengthMetrics): T

设置列与列的间距。默认值为0vp，设置为小于0的值时，按默认值显示。当[columnsTemplate](ts-container-lazyvgridlayout.md#columnstemplate)设置为auto-stretch模式时，columnsGap作为最小列间距，实际列间距由系统自动计算。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 列与列的间距。  取值范围：[0, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前LazyVGridLayout组件自身，用于支持链式调用。 |

### rowsGap

rowsGap(value: LengthMetrics): T

设置行与行的间距。默认值为0vp，设置为小于0的值时，按默认值显示。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 行与行的间距。  取值范围：[0, +∞) |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前LazyVGridLayout组件自身，用于支持链式调用。 |

### header

header(builder: CustomBuilder | undefined): T

设置当前LazyVGridLayout的头部组件。

**说明** 

头部组件位于容器顶部区域，通常用于展示标题、分组说明或其他固定在内容前方的元素。

当本组件随滚动容器滚动至可视区域内，且通过[sticky](ts-container-lazyvgridlayout.md#sticky)设置了header吸顶模式时，header会吸附在滚动容器可视区域顶部。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | undefined | 是 | 头部组件构造函数。  方法入参为undefined时，当前LazyVGridLayout不设置头部组件，如果已有头部组件，也会被移除。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前LazyVGridLayout组件自身，用于支持链式调用。 |

### footer

footer(builder: CustomBuilder | undefined): T

设置当前LazyVGridLayout的尾部组件。

**说明** 

尾部组件位于容器底部区域，通常用于展示补充信息、加载状态或其他固定在内容后方的元素。

当本组件随滚动容器滚动至可视区域内，且通过[sticky](ts-container-lazyvgridlayout.md#sticky)设置了footer吸底模式时，footer会吸附在滚动容器可视区域底部。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| builder | [CustomBuilder](ts-types.md#custombuilder8) | undefined | 是 | 尾部组件构造函数。  方法入参为undefined时，当前LazyVGridLayout不设置尾部组件，如果已有尾部组件，也会被移除。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前LazyVGridLayout组件自身，用于支持链式调用。 |

### sticky

sticky(sticky: StickyStyle | undefined): T

设置[header](ts-container-lazyvgridlayout.md#header)和[footer](ts-container-lazyvgridlayout.md#footer)的吸附效果。

当本组件随滚动容器滚动至可视区域内，且通过sticky设置header吸顶或footer吸底时，header会吸附在滚动容器可视区域顶部，footer会吸附在滚动容器可视区域底部。

**说明** 

由于浮点数计算精度问题，设置sticky后，在滚动过程中可能产生缝隙，可以通过[pixelRound](ts-universal-attributes-pixelroundforcomponent.md#pixelround)指定当前组件向下像素取整解决该问题。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sticky | [StickyStyle](ts-container-list.md#stickystyle9枚举说明) | undefined | 是 | 头部组件和尾部组件的吸附模式。sticky属性可以设置为StickyStyle.Header或StickyStyle.Footer，也可以设置为StickyStyle.BOTH，以同时支持头部组件吸顶和尾部组件吸底。  方法入参为undefined时，恢复为默认值StickyStyle.None。  未通过该接口设置时，默认头部组件不吸顶、尾部组件不吸底。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前LazyVGridLayout组件自身，用于支持链式调用。 |

## 事件

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onVisibleIndexesChange

onVisibleIndexesChange(callback: OnVisibleIndexesChangeCallback | undefined): T

设置onVisibleIndexesChange回调函数。当LazyVGridLayout在可视区域内的子组件的索引值发生变化时触发回调，返回可视区域内子组件的起始索引值和结束索引值。

**说明** 

当父组件设置主轴方向尺寸时，LazyVGridLayout按照父组件可视区域进行懒加载。此时onVisibleIndexesChange回调中start返回当前可视区域起始位置子组件的索引值，end返回当前可视区域结束位置子组件的索引值。

当父组件未设置主轴方向尺寸时，LazyVGridLayout会被内容撑开，导致所有子组件都会被加载布局。此时onVisibleIndexesChange回调中start返回0，end返回数据源最后一个子组件的索引值。

当该组件懒加载功能因上述父组件配置条件失效时，所有子组件都会被加载布局。此时onVisibleIndexesChange回调中start返回0，end返回数据源最后一个子组件的索引值。

此处的父组件指最靠近当前组件的上层滚动组件，其他文档下的具体含义请参考对应内容。

**起始版本：** 26.0.0

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnVisibleIndexesChangeCallback](ts-container-scrollable-common.md#onvisibleindexeschangecallback) | undefined | 是 | onVisibleIndexesChange事件的回调函数。方法入参为undefined时，取消监听。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前LazyVGridLayout组件自身，用于支持链式调用。 |

## 示例

### 示例1（实现懒加载网格布局）

该示例通过[WaterFlow](ts-container-waterflow.md)和LazyVGridLayout实现懒加载网格布局，并通过[onVisibleIndexesChange](ts-container-lazyvgridlayout.md#onvisibleindexeschange)在可视区域发生变化时触发回调，返回当前可视区域内子组件的起始索引值和结束索引值。

MyDataSource实现了[LazyForEach](ts-rendering-control-lazyforeach.md)数据源接口[IDataSource](ts-rendering-control-lazyforeach.md#idatasource)，用于通过LazyForEach给LazyVGridLayout提供子组件。

从API版本26.0.0开始，新增onVisibleIndexesChange事件。

```ts
import { LengthMetrics } from '@kit.ArkUI';
// MyDataSource是自定义数据源类，实现了LazyForEach所需的IDataSource接口
import { MyDataSource } from './MyDataSource';

@Entry
@Component
struct LazyVGridLayoutSample1 {
  private arr1:MyDataSource<number> = new MyDataSource<number>();
  private arr2:MyDataSource<number> = new MyDataSource<number>();
  build() {
    Column() {
      WaterFlow() {
        // 第一个LazyVGridLayout：单列布局
        LazyVGridLayout() {
          LazyForEach(this.arr1, (item:number)=>{
            Text('item' + item.toString())
              .height(64)
              .width('100%')
              .borderRadius(5)
              .backgroundColor(Color.White)
              .textAlign(TextAlign.Center)
          })
        }
        .columnsTemplate('1fr') // 单列布局
        .rowsGap(LengthMetrics.vp(10)) // 行间距10vp
        // 从API版本26.0.0开始，新增onVisibleIndexesChange事件。
        .onVisibleIndexesChange((start: number, end: number) => {
          console.info('visible indexes: start: ' + start + ', end: ' + end);
        })

        // 第二个LazyVGridLayout：双列布局
        LazyVGridLayout() {
          LazyForEach(this.arr2, (item:number)=>{
            Text('item' + item.toString())
              .height(128)
              .width('100%')
              .borderRadius(5)
              .backgroundColor(Color.White)
              .textAlign(TextAlign.Center)
          })
        }
        .columnsTemplate('1fr 1fr') // 双列布局，两列等宽
        .rowsGap(LengthMetrics.vp(10)) // 行间距10vp
        .columnsGap(LengthMetrics.vp(10)) // 列间距10vp
      }.padding(10)
      .rowsGap(10)
    }
    .width('100%').height('100%')
    .backgroundColor('#DCDCDC')
  }

  // 初始化数据源
  aboutToAppear(): void {
    for (let i = 0; i < 6; i++) {
      this.arr1.pushData(i);
    }
    for (let i = 0; i < 100; i++) {
      this.arr2.pushData(i);
    }
  }
}
```

```ts
// MyDataSource.ets
export class BasicDataSource<T> implements IDataSource {
  private listeners: DataChangeListener[] = [];
  protected dataArray: T[] = [];

  public totalCount(): number {
    return this.dataArray.length;
  }

  public getData(index: number): T {
    return this.dataArray[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }

  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    })
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    })
  }

  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }

  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    })
  }

  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    })
  }

  notifyDatasetChange(operations: DataOperation[]): void {
    this.listeners.forEach(listener => {
      listener.onDatasetChange(operations);
    })
  }
}

export class MyDataSource<T> extends BasicDataSource<T> {
  public shiftData(): void {
    this.dataArray.shift();
    this.notifyDataDelete(0);
  }
  public unshiftData(data: T): void {
    this.dataArray.unshift(data);
    this.notifyDataAdd(0);
  }
  public pushData(data: T): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
  public popData(): void {
    this.dataArray.pop();
    this.notifyDataDelete(this.dataArray.length);
  }
  public clearData(): void {
    this.dataArray = [];
    this.notifyDataReload();
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/pkXKLZJPQ3WYe1rZIAh52Q/zh-cn_image_0000002742124957.gif)

### 示例2（设置头部组件或尾部组件及吸附效果）

该示例通过[WaterFlow](ts-container-waterflow.md)嵌套LazyVGridLayout，并通过[header](ts-container-lazyvgridlayout.md#header)、[footer](ts-container-lazyvgridlayout.md#footer)、[sticky](ts-container-lazyvgridlayout.md#sticky)实现网格顶部和底部吸附效果。滚动过程中header吸附在可视区域顶部，footer吸附在可视区域底部。

从API版本26.0.0开始，新增支持header、footer和sticky属性。

```ts
import { LengthMetrics } from '@kit.ArkUI';
// MyDataSource是自定义数据源类，实现了LazyForEach所需的IDataSource接口
import { MyDataSource } from './MyDataSource';

@Entry
@Component
struct LazyVGridLayoutStickyDemo {
  private arr:MyDataSource<number> = new MyDataSource<number>();

  // 构建头部组件
  @Builder
  HeaderBuilder() {
    Column() {
      Text('Header')
        .fontSize(16)
    }
    .width('100%')
    .height(64)
    .borderRadius(5)
    .backgroundColor(Color.White)
    .justifyContent(FlexAlign.Center)
  }

  @Builder
  FooterBuilder() {
    Column() {
      Text('Footer')
        .fontSize(16)
    }
    .width('100%')
    .height(64)
    .borderRadius(5)
    .backgroundColor(Color.White)
    .justifyContent(FlexAlign.Center)
  }

  build() {
    Column() {
      WaterFlow() {
        LazyVGridLayout() {
          LazyForEach(this.arr, (item:number)=>{
            Text('item' + item.toString())
              .height(128)
              .width('100%')
              .borderRadius(5)
              .backgroundColor(Color.White)
              .textAlign(TextAlign.Center)
          })
        }
        .columnsTemplate('1fr 1fr')
        .rowsGap(LengthMetrics.vp(10))
        .columnsGap(LengthMetrics.vp(10))
        .header(this.HeaderBuilder)
        .footer(this.FooterBuilder)
        // 设置头部和尾部同时吸附
        .sticky(StickyStyle.BOTH)
      }.padding(10)
      .rowsGap(10)
    }
    .width('100%').height('100%')
    .backgroundColor('#DCDCDC')
  }

  aboutToAppear(): void {
    for (let i = 0; i < 100; i++) {
      this.arr.pushData(i);
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/_BMtitzxQmy8usKj658a7Q/zh-cn_image_0000002712246050.gif)

### 示例3（设置自适应列数）

该示例通过设置[columnsTemplate](ts-container-lazyvgridlayout.md#columnstemplate)属性实现了LazyVGridLayout组件自适应列数，并使用了属性[columnsTemplate](ts-container-lazyvgridlayout.md#columnstemplate)中的auto-fill、auto-fit和auto-stretch。

从API version 19开始，新增[columnsTemplate](ts-container-lazyvgridlayout.md#columnstemplate)接口。

```ts
import { LazyColumnLayout, LazyColumnLayoutAttribute, LengthMetrics } from '@kit.ArkUI';
// MyDataSource是自定义数据源类，实现了LazyForEach所需的IDataSource接口
import { MyDataSource } from './MyDataSource';

@Entry
@Component
struct LazyVGridLayoutColumnsTemplateDemo {
  private autoFillData: MyDataSource<number> = new MyDataSource<number>();
  private autoFitData: MyDataSource<number> = new MyDataSource<number>();
  private autoStretchData: MyDataSource<number> = new MyDataSource<number>();

  aboutToAppear(): void {
    // 初始化固定数量的数据，不进行滚动触底加载
    for (let i = 0; i < 12; i++) {
      this.autoFillData.pushData(i);
      this.autoFitData.pushData(i);
      this.autoStretchData.pushData(i);
    }
  }

  @Builder
  ModeTitle(title: string, description: string) {
    Column() {
      Text(title)
        .fontSize(16)
        .fontWeight(FontWeight.Medium)
        .fontColor('#182230')
      Text(description)
        .fontSize(12)
        .fontColor('#667085')
    }
    .alignItems(HorizontalAlign.Start)
    .width('100%')
    .padding({ bottom: 8 })
  }

  @Builder
  AutoFillHeader() {
    this.ModeTitle('auto-fill', '固定列宽为96vp，自动计算列数，剩余空间保留在行尾')
  }

  @Builder
  AutoFitHeader() {
    this.ModeTitle('auto-fit', '以96vp为最小列宽，剩余空间均分到每一列，列宽会被拉伸')
  }

  @Builder
  AutoStretchHeader() {
    this.ModeTitle('auto-stretch', '固定列宽为96vp，剩余空间均分到列间距中，列间距会被拉伸')
  }

  @Builder
  GridItemBuilder(item: number, backgroundColor: string) {
    Text(item.toString())
      .height(56)
      .width('100%')
      .borderRadius(6)
      .backgroundColor(backgroundColor)
      .fontColor('#182230')
      .textAlign(TextAlign.Center)
  }

  build() {
    Column() {
      Scroll() {
        LazyColumnLayout() {
          // auto-fill：固定列宽为96vp，根据可用宽度自动计算列数
          LazyVGridLayout() {
            LazyForEach(this.autoFillData, (item: number) => {
              this.GridItemBuilder(item, '#CDE7FF')
            })
          }
          .columnsTemplate('repeat(auto-fill, 96)')
          .rowsGap(LengthMetrics.vp(8))
          .columnsGap(LengthMetrics.vp(8))
          .header(this.AutoFillHeader)
          .padding(8)
          .backgroundColor('#F7F9FC')
          .border({ width: 1, color: '#D0D5DD' })
          .borderRadius(8)

          // auto-fit：以96vp为最小列宽，剩余空间均分到每一列
          LazyVGridLayout() {
            LazyForEach(this.autoFitData, (item: number) => {
              this.GridItemBuilder(item, '#D8F5D0')
            })
          }
          .columnsTemplate('repeat(auto-fit, 96)')
          .rowsGap(LengthMetrics.vp(8))
          .columnsGap(LengthMetrics.vp(8))
          .header(this.AutoFitHeader)
          .padding(8)
          .backgroundColor('#F7F9FC')
          .border({ width: 1, color: '#D0D5DD' })
          .borderRadius(8)

          // auto-stretch：固定列宽为96vp，剩余空间均分到列间距中
          LazyVGridLayout() {
            LazyForEach(this.autoStretchData, (item: number) => {
              this.GridItemBuilder(item, '#FFE6A8')
            })
          }
          .columnsTemplate('repeat(auto-stretch, 96)')
          .rowsGap(LengthMetrics.vp(8))
          .columnsGap(LengthMetrics.vp(8))
          .header(this.AutoStretchHeader)
          .padding(8)
          .backgroundColor('#F7F9FC')
          .border({ width: 1, color: '#D0D5DD' })
          .borderRadius(8)
        }
        .space(LengthMetrics.vp(16))
        .width('100%')
      }
      .width('100%')
      .scrollable(ScrollDirection.Vertical)
      .layoutWeight(1)
    }
    .width('100%')
    .height('100%')
    .padding({ top: 48, left: 12, right: 12, bottom: 12 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/bvCVyNYdR3WsuIqxUKfNtg/zh-cn_image_0000002742004999.gif)
