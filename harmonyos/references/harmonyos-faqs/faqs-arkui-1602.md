---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1602
title: 如何实现Swiper控制最边缘时的弹性距离
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现Swiper控制最边缘时的弹性距离
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5773d697da13efdef4274914609945c047d1558d206bf2119e1b96fc9d952dbf
---

## 问题现象

使用Swiper展示内容时，在列表的第一个和最后一个展示时，可以通过上划或者下划触发弹性伸缩。但是，弹性伸缩的距离过长。是否可以设置Swiper中弹性伸缩的高度，如下图拉到最下面伸缩的距离大概有2/5：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/AL2siOY6SKS7K8ZQmbQ4Pw/zh-cn_image_0000002658852597.png "点击放大")

把第一个内容拉到最下面伸缩距离固定：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/c6eDgX5KTxeC4sw6Wozf3w/zh-cn_image_0000002628773238.png "点击放大")

## 背景知识

Swiper相关内容可以参考官方文档[Swiper API](../harmonyos-references/ts-container-swiper.md)。官方文档中没有现成的接口设置边缘回弹距离，需要在原有接口的基础上进行一些更改。

## 解决方案

可以通过禁用Swiper内置的边缘回弹效果，使用自定义边缘的回弹动作。参考如下代码：

```ts
// xxx.ets
class MyDataSource implements IDataSource {
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
export struct SwiperExample {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);
  @State traY: number = 0;
  @State index: number = 0;

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 1; i <= 10; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Text(item.toString())
            .width('90%')
            .height(400)
            .backgroundColor(0xAFEEEE)
            .textAlign(TextAlign.Center)
            .fontSize(30)
            .translate({
              y: this.traY   // 偏移设置为捕获到的偏移量
            });
        }, (item: string) => item);
      }
      .backgroundColor(Color.Orange)
      .onChange((index: number) => {
        this.index = index;
      })
      .loop(false)
      .vertical(true)
      .effectMode(EdgeEffect.None) // 禁用内置边缘效果
      .parallelGesture(
        PanGesture({ direction: PanDirection.Vertical })
          .onActionUpdate((event) => {
            // 这里控制滑动距离，第一个往下滑
            if (this.index == 0 && event.offsetY < 160) {
              this.traY = event.offsetY;
            }
            // 这里控制滑动距离，最后一个往上滑
            if (this.index == this.data.totalCount() - 1 && event.offsetY > -160) {
              this.traY = event.offsetY;
            }
          })
          .onActionEnd(() => {
            animateToImmediately({
              duration: 100, // 这里可以控制回弹速度
              curve: Curve.EaseOut,
              iterations: 1,
              playMode: PlayMode.Normal,
            }, () => {
              this.traY = 0;
            });
          })
      );
    }.width('100%')
    .margin({ top: 50 });
  }
}
```

## 总结

对于系统接口行为与预期不符的情况，可以禁用系统接口的默认功能，并重写相关接口以实现预期效果。
