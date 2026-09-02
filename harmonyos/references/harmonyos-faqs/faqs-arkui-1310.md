---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1310
title: Tabs和同方向滑动的子组件的滑动动作隔离
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Tabs和同方向滑动的子组件的滑动动作隔离
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:eb6d51b8d9291d6d253ba602c4a1e827655d421d84b2da1e0c848ec75802abc9
---

## 问题现象

如何设置在横向拖动子组件中的第三方图标时，禁止触发Tabs的切换功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/IkeT1TvPRI69HfQ4YYKeEQ/zh-cn_image_0000002658838299.png "点击放大")

## 背景知识

* [!!双向绑定语法](../harmonyos-guides/arkts-new-binding.md)：在状态管理V2中，提供!!语法糖统一处理双向绑定。
* [Tabs.scrollable](../harmonyos-references/ts-container-tabs.md#scrollable)：设置是否可以通过滑动页面进行页面切换。
* [TouchType](../harmonyos-references/ts-appendix-enums.md#touchtype)：触摸事件的类型。
* [@ohos/mpchart](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fmpchart)：MPChart是一个包含各种类型图表的图表库，主要用于业务数据汇总，包括线形图、柱状图、饼状图、蜡烛图、气泡图、雷达图、瀑布图等自定义图表库。

## 解决方案

1. 该方案基于@ohos/mpchart，执行ohpm i @ohos/mpchart命令安装MPChart三方库。
2. 使用!!语法，把判断Tabs是否可以通过滑动页面进行页面切换的isAllowScroll属性，在主页面和子组件中关联。
3. 子组件中图表触摸时，设置isAllowScroll属性为false，触摸结束手指抬起时，设置isAllowScroll属性为true。

```ts
import {
  JArrayList, // 工具类：数据集合
  EntryOhos,// 图表数据结构基础类
  LineDataSet, //线形图数据集合
  ILineDataSet, // 线形图数据集合的操作类
  LineData, //线形图数据包
  LineChart, // 线形图图表类
  LineChartModel,// 线形图配置构建类
  MarkerView, //图例形状
} from '@ohos/mpchart';

@Entry
@ComponentV2
struct Index {
  @Local fontColor: string = '#182431';
  @Local selectedFontColor: string = '#007DFF';
  @Local currentIndex: number = 0;
  @Local selectedIndex: number = 0;
  @Local isAllowScroll: boolean = true;
  private controller: TabsController = new TabsController();

  private model: LineChartModel = new LineChartModel();
  // 构造数据选择监听器

  @Builder tabBuilder(index: number, name: string) {
    Column() {
      Text(name)
        .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
        .fontSize(16)
        .fontWeight(this.selectedIndex === index ? 500 : 400)
        .lineHeight(22)
        .margin({ top: 17, bottom: 7 })
      Divider()
        .strokeWidth(2)
        .color('#007DFF')
        .opacity(this.selectedIndex === index ? 1 : 0)
    }.width('100%')
  }

  build() {
    Column() {
      Tabs({ barPosition: BarPosition.Start, index: this.selectedIndex, controller: this.controller }) {
        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#007DFF')
        }.tabBar(this.tabBuilder(0, 'blue'))

        TabContent() {
          Star({ isAllowScroll: this.isAllowScroll!! })
        }.tabBar(this.tabBuilder(1, 'LineChart'))

        TabContent() {
          Column().width('100%').height('100%').backgroundColor('#FFBF00')
        }.tabBar(this.tabBuilder(2, 'yellow'))
      }
      .scrollable(this.isAllowScroll)
      .vertical(false)
      .barMode(BarMode.Fixed)
      .barWidth(360)
      .barHeight(56)
      .animationDuration(400)
      .animationMode(AnimationMode.CONTENT_FIRST)
      .onChange((index: number) => {
        console.log(`onChange index:${index}`);
        this.selectedIndex = index;
      })
      .width('100%')
      .height('100%')
      .backgroundColor('#F1F3F5')
    }.width('100%')
  }

}

@ComponentV2
struct Star {
  private model: LineChartModel = new LineChartModel();
  @Param isAllowScroll: boolean = true;
  @Event $isAllowScroll: (val: boolean) => void = () => {};

  // 图表数据初始化
  aboutToAppear() {

    // 初始化图表配置构建类
    this.model = new LineChartModel();
    this.model.setDragEnabled(true);
    this.model.setScaleEnabled(true);
    // 为图表设置markerView
    let normalMarker = new MarkerView();
    this.model.setMarker(normalMarker);
    // 也可设置定义图表MarkerView
    // 生成图表数据
    let lineData: LineData = this.getLineData();
    // 将数据与图表配置类绑定
    this.model.setData(lineData);
    // 设置图表最大的X轴显示范围，如不设置，则默认显示全部数据
    this.model.setVisibleXRangeMaximum(20);
  }

  private getLineData(): LineData {

    let start: number = 1;
    let values: JArrayList<EntryOhos> = new JArrayList<EntryOhos>();
    for (let i = start; i < 30; i++) {
      values.add(new EntryOhos(i, i));
    }
    let dataSet = new LineDataSet(values, 'DataSet');
    let dataSetList: JArrayList<ILineDataSet> = new JArrayList<ILineDataSet>();
    dataSetList.add(dataSet);

    let lineData: LineData = new LineData(dataSetList);
    return lineData;
  }

  build() {
    Column() {
      LineChart({ model: this.model })
        .width('100%')
        .height('30%')
        .onTouch((event) => {
          if (event.type === TouchType.Down || event.type === TouchType.Move) {
            this.$isAllowScroll(false);
          } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
            this.$isAllowScroll(true);
          }
        })
    }

  }
}
```
