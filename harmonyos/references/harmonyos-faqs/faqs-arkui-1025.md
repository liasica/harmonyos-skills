---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1025
title: 如何让轮播图根据进度条指示器进行切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何让轮播图根据进度条指示器进行切换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:57e41be57c34efce70250ca94f8f005af4c4cc66a8d58696e40a1d64108fb8ef
---

## 问题现象

需要自定义轮播图的指示器，如何通过进度条的方式展示轮播进度？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/eKkORyMRR-auPpkuy6FCiA/zh-cn_image_0000002628404814.png "点击放大")

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)滑块视图容器，提供子组件滑动轮播显示的能力。通过接口中的controller参数可以给组件绑定一个控制器，类型为[SwiperController](../harmonyos-references/ts-container-swiper.md#swipercontroller)。SwiperController可用于实现控制Swiper翻页等功能。
* [Progress](../harmonyos-references/ts-basic-components-progress.md)进度条组件，用于显示内容加载或操作处理等进度。[style](../harmonyos-references/ts-basic-components-progress.md#style8)属性可用于设置进度条的样式。在样式选项中可以通过enableSmoothEffect[设置进度平滑动效](../harmonyos-references/ts-basic-components-progress.md#示例5设置进度平滑动效)的开关。

## 解决方案

可以通过Swiper和多个进度条完成布局效果，定时器实现进度条自增。具体实现步骤如下：

1. 创建Swiper组件，绑定SwiperController控制器。根据要展示的资源数组长度，通过ForEach创建同样数量的进度条。
2. 在Swiper组件的style属性中将enableSmoothEffect设置为false，关闭进度条的平滑动效果。
3. 定义一个定时器，每隔一段时间增加当前轮播图索引下进度条的value。当进度达到最大值后（可以设置超过最大值，让进度条满了后还能预留一点时间），利用SwiperController控制器的[showNext](../harmonyos-references/ts-container-swiper.md#shownext)方法进行翻页。轮播图索引变化后修改进度条的值。

完整代码如下：

```ts
@Entry
@Component
struct ProgressSwiper {
  swiperController: SwiperController = new SwiperController(); // Swiper组件的控制器，用于翻页
  list: ResourceColor[] = ['#f1f3f5', '#f1f3f5', '#f1f3f5', '#f1f3f5', '#f1f3f5', '#f1f3f5', '#f1f3f5', '#f1f3f5'];
  @State valueList: number[] = [0, 0, 0, 0, 0, 0, 0];
  @State index: number = 0;
  intervalID: number = 0;

  aboutToAppear(): void {
    // 启动定时器，用于进度条自增
    this.intervalID = setInterval(() => {
      this.valueList[this.index] = this.valueList[this.index] + 1;
      // 设置为60可以在进度条满后延迟(60-50)*50=500ms翻页
      if (this.valueList[this.index] === 60) {
        this.swiperController.showNext();
      }
    }, 50);
  }

  aboutToDisappear(): void {
    clearInterval(this.intervalID);
  }

  build() {
    Column() {
      Stack() {
        Swiper(this.swiperController) {
          ForEach(this.list, (res: ResourceColor, index: number) => {
            Text(`图${index + 1}`)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center)
              .backgroundColor(res)
              .borderRadius(6);
          });
        }
        .indicator(false)
        .index($$this.index)
        .loop(true)
        .itemSpace(20)
        .onChange((index) => {
          // 当索引发生变化时修改进度条的进度
          for (let i = 0; i < this.valueList.length; i++) {
            if (i < index) {
              this.valueList[i] = 50;
            } else {
              this.valueList[i] = 0;
            }
          }
        });

        Row({ space: 4 }) {
          ForEach(this.valueList, (value: number, index: number) => {
            Progress({ value: this.valueList[index], total: 50, type: ProgressType.Linear })
              .layoutWeight(1)
              .color('#fff')
              .height(5)
              .style({ strokeWidth: 2, enableSmoothEffect: false }) // 关闭进度条的平滑动效果
              .onClick(() => {
                this.index = index;
              });
          }, (value: number, index: number) => {
            return index + '';
          });
        }.width('100%')
        .position({ bottom: 10 })
        .padding({ left: 10, right: 10 });
      }
      .width('100%')
      .height(200);
    }.width('100%')
    .height('100%')
    .padding(16);
  }
}
```
