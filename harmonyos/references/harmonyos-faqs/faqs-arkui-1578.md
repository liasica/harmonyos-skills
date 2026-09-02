---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1578
title: 如何使子组件间自适应保持相同间距
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使子组件间自适应保持相同间距
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:06ef3ec7c394e8127cf82401d040227b7a3196ee4ef96865b8d2f428e586c9e3
---

## 问题现象

Row组件中展示多个子元素（如多个Text组件），子组件的个数和每个子组件的宽度都不确定。希望实现以下效果：

* 当多个Text组件的宽度之和小于Row组件宽度时，Text组件在Row组件中水平居中排列，并且Text组件之间保持等间距排列。
* 当多个Text组件的宽度之和大于Row组件宽度时，超过可视区域Text组件可以滑动展示，并且Text组件之间保持等间距排列。

## 背景知识

* [Scroll](../harmonyos-references/ts-container-scroll.md)：是可滚动的容器组件，当子组件的布局尺寸超过父组件的尺寸时，内容可以滚动。
* [measureText](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretext12)：用来计算指定文本的宽度。

## 解决方案

* 当子元素（如Text组件）的总宽度大于父组件（如Row组件）的宽度时，将Row嵌套于Scroll组件中，实现水平滚动，支持查看超出可视区域的子元素。各子元素间距通过自定义变量统一设置，通过margin计算逻辑实现间距相等。
* 当子元素（如Text组件）总宽度小于父组件（如Row组件）的宽度时，通过measureText获取各子元素宽度，计算其总和与父容器剩余空间，通过margin计算逻辑实现间距相等。

完整示例代码如下：

```ts
@Entry
@Component
struct MeasureTextDemo {
  private scrollerForScroll: Scroller = new Scroller();
  list: string[] = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7']; // 模拟子元素宽度之和大于Row组件（父组件）宽度
  wid: number = 20;
  parentCompWidth: number = 300; // 父组件宽度
  arrayWidthsSum: number = 0; // 子元素总宽度
  arrayWidths: number[] = []; // 子元素宽度的集合
  @State blockNum: number = 0; // 子元素宽度之和小于Row组件（父组件）宽度时的平均间距

  // 抽取margin计算逻辑为独立方法
  private getItemMargin(index: number): Margin {
    const isFirst = index === 0; // 判断是否为第一个子元素
    const isLast = index === this.list.length - 1; // 判断是否为最后一个子元素
    const defaultMargin = 5; // 子元素宽度之和大于Row组件（父组件），自定义子元素的默认间距，手动自定义

    if (this.parentCompWidth > this.arrayWidthsSum) { // 子元素宽度之和小于Row组件（父组件）宽度时
      // 计算父组件的剩余宽度，设置子元素间距
      // 当渲染第一个和最后一个子元素时，第一个子元素的左间距和最后一个子元素的右间距是平均间距的2倍，中间元素的间距为平均间距
      return {
        left: isFirst ? this.blockNum : this.blockNum / 2,
        right: isLast ? this.blockNum : this.blockNum / 2
      };
    } else {
      // 当渲染第一个和最后一个子元素时，第一个子元素的左间距和最后一个子元素的右间距是默认间距的2倍，中间元素的间距为默认间距
      return {
        left: isFirst ? defaultMargin : defaultMargin / 2,
        right: isLast ? defaultMargin : defaultMargin / 2
      };
    }
  }

  aboutToAppear(): void {
    // 获取集合中元素的宽度集合
    this.arrayWidths = this.list.map(text =>
    this.getUIContext().px2vp(this.getUIContext().getMeasureUtils().measureText({
      textContent: text,
      fontSize: 15
    }))
    );

    // 计算集合中元素的总宽度
    this.arrayWidthsSum = this.arrayWidths.reduce((acc, curr) => acc + curr, 0);
    // 子元素宽度之和小于Row组件（父组件），计算父组件的剩余宽度，将剩余宽度平均分为（子元素总数+1份），记作平均间距
    this.blockNum = (this.parentCompWidth - this.arrayWidthsSum) / (this.list.length + 1);
  }

  build() {
    Column() {
      Scroll(this.scrollerForScroll) {
        Row() {
          ForEach(this.list, (item: string, index: number) => {
            Text(item)
              .fontSize(15)
              .height(100)
              .backgroundColor('#5291FF')
              .margin(this.getItemMargin(index)); // 动态设置子元素间距
          });
        };
      }
      .scrollBar(BarState.Off) // 不显示滚动条组件
      .scrollable(ScrollDirection.Horizontal) // 设置水平滑动
      .width(this.parentCompWidth) // 设置父组件宽度
      .height(200)
      .backgroundColor('#F1F3F5')
      .borderRadius(16);

    }
    .width('100%')
    .height('100%');
  }
}
```

子元素（如Text组件）宽度之和小于父组件（如Row组件）宽度时，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/2IejUUSlQUmEsiwfyH898w/zh-cn_image_0000002628610294.png "点击放大")

子元素（如Text组件）宽度之和大于父组件（如Row组件）宽度时，效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/t9GJxLoCTu-v9ojOlAFVjQ/zh-cn_image_0000002658849557.gif "点击放大")
