---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-563
title: Swiper组件在删除数据时如何实现切换到前一个元素而非第一个
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Swiper组件在删除数据时如何实现切换到前一个元素而非第一个
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b68fbbd544d063f8e4f912081957eb0acbd9ad57fdd6e6cf2d67177e9f1c9ba0
---

## 问题现象

如何实现Swiper组件在删除数据时切换到前一个元素而非第一个？切换时的动画怎么实现？

## 背景知识

* 使用[Swiper](../harmonyos-references/ts-container-swiper.md)管理一个可以横滑切换的组件，发现在删除列表数据时Swiper会默认切到第一个元素。
* [pop](../harmonyos-references/arkts-apis-arkts-collections-array.md#pop)从ArkTS Array中移除并返回最后一个元素。可以支持转场动画。[push](../harmonyos-references/arkts-apis-arkts-collections-array.md#push)在ArkTS Array的末尾添加元素，并返回新的Array长度。
* [showNext](../harmonyos-references/ts-container-swiper.md#shownext)和[showPrevious](../harmonyos-references/ts-container-swiper.md#showprevious)方法分别可以使Swiper在数据源变化时翻至下一页和翻至上一页。翻页带动效切换过程，时长通过Swiper的duration属性设置。

## 解决方案

* 场景一：实现Swiper组件在删除数据时切换到前一个元素而非第一个，无切换动画。

  通过绑定index属性，该属性支持通过$$双向绑定变量，使用数组管理Swiper的数据，删除操作通过pop()方法来实现。Swiper默认在数据源变化时会重置到第一个元素，需通过控制器强制指定目标位置。

  ```ts
  @Entry
  @Component
  struct SwiperDeletesDataToPreviousElementOne {
    private swiperController: SwiperController = new SwiperController();
    @State data: number[] = [];
    @State total: number = 2;
    @State index: number = 0;

    aboutToAppear(): void {
      for (let i = 0; i <= this.total; i++) {
        this.data.push(i);
      }
    }

    build() {
      Column({ space: 5 }) {
        Swiper(this.swiperController) {
          ForEach(this.data, (item: number) => {
            Text((item + 1) + '')
              .width('90%')
              .height(160)
              .backgroundColor('#f1f3f5')
              .textAlign(TextAlign.Center)
              .fontSize(30);
          }, (item: string) => item);
        }
        .index($$this.index) // 绑定索引状态变量
        .indicator(Indicator.digit()
          .top(200)
          .fontColor(Color.Gray)
          .selectedFontColor(Color.Gray)
          .digitFont({ size: 20, weight: FontWeight.Bold })
          .selectedDigitFont({ size: 20, weight: FontWeight.Normal }))
        .displayArrow(true, false)
        .cachedCount(3)
        .loop(false);

        Row({ space: 10 }) {
          Button('Add').onClick(() => {
            this.data.push(++this.total);
            this.index = this.total; // 修改索引，触发UI更新
          });
          Button('Remove').onClick(() => {
            this.data.pop();
            this.index -= 1; // 修改索引，触发UI更新
          });
        };
      }
      .width('100%')
      .margin({ top: 5 });
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/dpIP7reyRCeTRh4bqJ-upg/zh-cn_image_0000002658791415.png "点击放大")
* 场景二：实现Swiper组件在删除数据时切换到前一个元素而非第一个，有切换动画。

  可以通过使用Swiper组件的showNext和showPrevious方法解决，翻页默认带动效。

  ```ts
  @Entry
  @Component
  struct SwiperDeletesDataToPreviousElementTwo {
    private swiperController: SwiperController = new SwiperController();
    @State data: number[] = [];
    @State total: number = 2;
    index: number = 0;

    aboutToAppear(): void {
      for (let i = 0; i <= this.total; i++) {
        this.data.push(i);
      }
    }

    build() {
      Column({ space: 5 }) {
        Swiper(this.swiperController) {
          ForEach(this.data, (item: number) => {
            Text((item + 1) + '')
              .width('90%')
              .height(160)
              .backgroundColor('#f1f3f5')
              .textAlign(TextAlign.Center)
              .fontSize(30);
          }, (item: string) => item);
        }
        .index($$this.index) // 绑定索引状态变量
        .indicator(Indicator.digit()
          .top(200)
          .fontColor(Color.Gray)
          .selectedFontColor(Color.Gray)
          .digitFont({ size: 20, weight: FontWeight.Bold })
          .selectedDigitFont({ size: 20, weight: FontWeight.Normal }))
        .displayArrow(true, false)
        .cachedCount(3)
        .loop(false);

        Row({ space: 10 }) {
          Button('Add').onClick(() => {
            this.data.push(this.total++);
            this.swiperController.showNext();
          });
          Button('Remove').onClick(() => {
            this.data.pop();
            this.swiperController.showPrevious();
          });
        };
      }
      .width('100%')
      .margin({ top: 5 });
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/PWQxazXqRliPgMb-IVucRA/zh-cn_image_0000002628552030.png "点击放大")
