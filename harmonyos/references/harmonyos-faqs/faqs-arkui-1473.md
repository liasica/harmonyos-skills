---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1473
title: 多级筛选功能实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 多级筛选功能实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3789d40d6edadc900cc3184ece0b6cffb5eed0658b789409bf84260ba3f120fa
---

## 问题现象

如何实现多级筛选功能？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/aPC6ONDrS6quDMDaQFWJkg/zh-cn_image_0000002658844615.png "点击放大")

## 背景知识

* [List](../harmonyos-references/ts-container-list.md)列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* [ForEach](../harmonyos-references/ts-rendering-control-foreach.md)接口基于数组循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。例如，ListItem组件要求ForEach的父容器组件必须为List组件。

## 解决方案

1. 分别定义一级分类数组arrOne和二级分类数组arrTwo。
2. 使用ForEach对arrOne数组内容进行循环渲染，并添加onClick方法，当点击某一具体元素时，将selectIndexOne的值设置为index索引，将selectIndexTwo的值设置为0。
3. 使用ForEach对arrTwo数组内容进行循环渲染，并添加onClick方法，当点击某一具体元素时，将selectIndexTwo的值设置为index。获得selectIndexOne和selectIndexTwo参数后即可实现多级筛选页面的功能。

完整示例参考如下：

```ts
@Entry
@Component
struct MultiLevelFilter {
  // 定义一级分类数组，用于显示顶部的分类标题
  arrOne = ['黑色品种', '有色品种', '农产品', '化工品种', '宏观分析'];
  // 定义二级分类数组，每个元素对应一级分类下的子分类
  arrTwo = [
    ['焦炭', '玻璃', '螺纹钢', '动力煤', '钢材', '焦煤', '锰硅', '热卷板', '铁矿石', '线材'],
    ['黄金', '锌', '铝', '铜', '镍', '铅', '锡', '白银', '云南省水电', '工业硅', '碳酸锂'],
    ['菜籽', '豆粕', '玉米淀粉', '白糖', '苹果', '棉花', '玉米', '豆油', '豆二', '鸡蛋'],
    ['玻璃', '20号胶', '橡胶', '聚氯乙烯', '聚烯烃', '塑料', '沥青', '甲醇', '尿素', '聚丙烯', '纸浆'],
    ['中证500指数', '2年期国债', '5年期国债', '上证50指数', '10年期国债', '沪深300指数', '股指']
  ];
  // 用于记录当前选中的一级分类索引
  @State selectIndexOne: number = 0;
  // 用于记录当前选中的二级分类索引
  @State selectIndexTwo: number = 0;
  // 定义两个滚动控制器，用于控制左右两个List的滚动行为
  filterScroller = new Scroller();
  scroller = new Scroller();

  build() {
    Column() {
      // 顶部行布局，包含“筛选”标题和一级分类的水平List
      Row() {
        // 一级分类的水平List
        List({scroller:this.scroller,space:15}) {
          // 使用ForEach对arrOne进行循环渲染
          ForEach(this.arrOne, (name: string, index) => {
            ListItem() {
              Stack({ alignContent: Alignment.Bottom }) {
                // 显示一级分类按钮
                Button(name)
                  .width(100)
                  .fontColor(this.selectIndexOne === index ? Color.White : Color.Black) // 根据是否选中设置字体颜色
                  .height('36vp')
                  .backgroundColor(this.selectIndexOne === index ? '#0A59F7' : '#f1f3f5'); // 根据是否选中设置背景色
              }
              .onClick(() => {
                // 点击事件：设置选中的一级分类索引，并将二级分类索引重置为0
                this.selectIndexOne = index;
                this.selectIndexTwo = 0;
                // 滚动到二级分类的第一个项
                this.filterScroller.scrollToIndex(0);
              });
            };
          }, (name: string): string => name); // 用于ForEach key的唯一标识
        }
        .scrollBar(BarState.Off) // 隐藏滚动条
        .listDirection(Axis.Horizontal) // 设置水平方向滚动
        .height('40vp');
      }
      .height('40vp')

      // 中部行布局，包含“品种”标题和二级分类的水平List
      Row() {
        // 二级分类的水平List，根据selectIndexOne动态显示对应的一级分类下的子分类
        List({ scroller: this.filterScroller ,space:15}) {
          // 使用ForEach对arrTwo中对应一级分类的子分类数组进行循环渲染
          ForEach(this.arrTwo[this.selectIndexOne], (name: string, index) => {
            ListItem() {
              Column() {
                Button(name)
                  .fontColor(this.selectIndexTwo === index ? Color.White : Color.Black)
                  .height('36vp')
                  .backgroundColor(this.selectIndexTwo === index ? '#0A59F7' : '#f1f3f5');
              }
              .onClick(() => {
                this.selectIndexTwo = index;
              });
            };
          }, (name: string): string => name);
        }
        .scrollBar(BarState.Off)
        .listDirection(Axis.Horizontal)
        .height('40vp');
      }
      .height('40vp')
      .margin({ top:'10vp',bottom:'20vp'});
      Row() {
        Text('首页')
          .fontSize(30);
      }
      .height('40vp')
    }
    .padding('20vp')
    .width('100%')
    .height('100%');
  }
}
```
