---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-705
title: LazyForEach实现骨架屏预加载效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > LazyForEach实现骨架屏预加载效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:02770dcd5721b785473fc6b502424ba226f6837ee211e27ab09d4ea255a72e1d
---

## 问题现象

如何实现骨架屏预加载效果？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/hAvegf_SSiuumkuMhGG5pw/zh-cn_image_0000002658914207.png "点击放大")

## 背景知识

* [LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)为开发者提供了基于数据源渲染出一系列子组件的能力。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会销毁并回收组件以降低内存占用。
* 骨架屏通过显示简单的灰色块和线条，让用户在等待内容加载时获得视觉反馈。

## 解决方案

1. 使用LazyForEach对数据源中的每个数据进行预加载。
2. 在Stack组件中，首先设置背景色为rgba(0,0,0,0.1)，然后通过linearGradient设置组件的颜色渐变效果，并结合animation方法设置动画的持续时间和循环次数。

```ts
// 用户自定义数据源
class MyDataSourceLOne implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct BackGroundColorGradualChange {
  private arr: MyDataSourceLOne = new MyDataSourceLOne([]);
  private listScroller: ListScroller = new ListScroller();
  @State translateX: string = '-100%';

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 1; i <= 7; i++) {
      list.push(i);
    }
    this.arr = new MyDataSourceLOne(list);
  }

  build() {
    Column() {
      List({ space: 20, initialIndex: 100, scroller: this.listScroller }) {
        LazyForEach(this.arr, () => {
          ListItem() {
            Stack() {
              // 设置组件的背景色
              Text()
                .width('100%')
                .height(100)
                .backgroundColor('rgba(0,0,0,0.1)');

              Text()
                .width('100%')
                .height(100)
                .translate({ x: this.translateX })
                .onAppear(() => {
                  this.translateX = '100%';
                })
                // 设置动画的持续时间和循环次数
                .animation({
                  duration: 1500,
                  iterations: -1
                })
                // 设置颜色渐变效果
                .linearGradient({
                  angle: 90,
                  colors: [
                    ['rgba(255,255,255,0)', 0],
                    ['rgba(255,255,255,1)', 0.5],
                    ['rgba(255,255,255,0)', 1]
                  ]
                });
            }
            .width('100%')
            .height(100)
            .backgroundColor(0xFFFFFF);
          };
        });
      }
      .listDirection(Axis.Vertical)
      .scrollBar(BarState.Off)
      .friction(0.6)
      .edgeEffect(EdgeEffect.Spring)
      .width('90%')
      .cachedCount(3);
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 });
  }
}
```

## 总结

使用linearGradient设置骨架屏的渐变效果，可增强用户体验，提升用户停留时长。
