---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1539
title: 如何实现横向翻页效果的Grid
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现横向翻页效果的Grid
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8f60475907cef168cdc5df8a0bfb22714cc568f8ea3605c1768845bfe6caf847
---

## 问题现象

如何实现有横向翻页效果的Grid网格容器？加载数组时其中超过一页的要能自动放到Grid的下一页当中，由设定Grid的几行几列来做判断该显示多少页。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/UjgbOPBzTo2BZeZP71nyZA/zh-cn_image_0000002658968433.gif "点击放大")

## 背景知识

* [Grid](../harmonyos-references/ts-container-grid.md)是网格容器，由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。[columnsTemplate](../harmonyos-references/ts-container-grid.md#columnstemplate)/[rowsTemplate](../harmonyos-references/ts-container-grid.md#rowstemplate)分别设置当前网格布局列/行的数量。
* [Swiper](../harmonyos-references/ts-container-swiper.md)为滑块视图容器，可以为子组件提供横向滑动轮播显示的能力。

## 解决方案

可以通过Swiper组件嵌套Grid组件来实现横向翻页的网格布局，具体实现如下：

1. getGridData方法将mainArray分割成每页20个元素的子数组，形成二维数组，用于分页显示。
2. 使用[RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md)作为容器，设置全屏大小和背景颜色。内部嵌入Swiper组件，用于实现翻页效果，并绑定swiperController以控制滑动行为。
3. Swiper内部使用ForEach循环遍历getGridData返回的二维数组，每个item对应一页数据。
4. Grid组件设置为4列5行，消除列间和行间间隙，宽度占满容器，高度固定。

```ts
@Entry
@Component
struct HorizontalGrid {
  @State mainArray: Array<string> = ['待办', '人力服务', '薪资查询',
    '信息', '员工贴士', '邮箱', '天翼爱渠道', '营销沙盘', '政企沙盘', '领导测评', 'i用焦点', '迁改管理', '通用报表',
    '美好生活', '经营视窗', '企业知识库', '大模型',
    '快速审批', '网运工具', '智慧党建', 'AI打卡', '楼长履职', '综合', '新待办', 'app测试',
    '智慧网发', '人才云',
    '资金稽核'];
  @State currentIndex: number = 0;
  private swiperController: SwiperController = new SwiperController();

  // getGridData方法将mainArray数组分割成每页20个元素的子数组
  getGridData(arr: string[]): string[][] {
    let result: string[][] = [];
    for (let i = 0; i < arr.length; i += 20) {
      result.push(arr.slice(i, i + 20));
    }
    return result;
  }

  build() {
    RelativeContainer() {
      Swiper(this.swiperController) {
        ForEach(this.getGridData(this.mainArray), (item: string[]) => {
          Grid() {
            ForEach(item, (service: string) => {
              GridItem() {
                Text(service)
                  .fontSize(16)
                  .backgroundColor(0xF9CF93)
                  .width('calc(100% - 20vp)')
                  .height('calc(100% - 20vp)')
                  .margin(10)
                  .textAlign(TextAlign.Center);
              };
            }, (service: string) => service);
          }
          // 此处增加距离也有效果
          .margin({ bottom: 10 })
          .columnsTemplate('1fr 1fr 1fr 1fr') // 设置为四列五行
          .rowsTemplate('1fr 1fr 1fr 1fr 1fr')
          .columnsGap(0)
          .rowsGap(0)
          .width('100%')
          .backgroundColor(0xFAEEE0)
          .height(300);
        }, (item: string[]) => JSON.stringify(item));
      }
      .indicator(
        new DotIndicator()
          .bottom(0) // 此处可以设置指示器属性，如果需要往上调可以通过这个
      )
      .height('65%')
      .cachedCount(2)
      .index(0)
      .autoPlay(true)
      .interval(4000)
      .loop(true)
      .indicatorInteractive(true)
      .duration(1000)
      .itemSpace(0)
      .curve(Curve.Linear)
      .onChange(index => {
        this.currentIndex = index;
      })
      .id('gridOut')
      .alignRules({
        top: { anchor: '__container__', align: VerticalAlign.Top },
        left: { anchor: '__container__', align: HorizontalAlign.Start }
      });
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Gray);
  }
}
```
