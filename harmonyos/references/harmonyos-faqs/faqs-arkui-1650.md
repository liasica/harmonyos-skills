---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1650
title: Stack组件中子组件超出边界显示问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Stack组件中子组件超出边界显示问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3b4df0e00f5c7f0213085bb1c7bd926ef5877517f29b09c5a2d01a90414762fc
---

## 问题现象

* 场景一：Stack组件中Text子组件因边缘约束导致宽度压缩、文字溢出，如何设置Text宽度自适应或调整Stack布局策略，使其保持原始文本宽度并扩展容器边界。代码如下：

  ```ts
  @Entry
  @Component
  struct StackPageOne {
    build() {
      Column() {
        Stack() {
          Text(' 测试 ')
            .borderRadius(10)
            .fontSize(40)
            .margin({ left: 150 })
            .backgroundColor('#989ba1')
            .maxLines(1);
        }
        .width(200)
        .height(100)
        .borderRadius(10)
        .backgroundColor('#f1f3f5');
      }
      .alignItems(HorizontalAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/x7ZF0kadST2_mzfO1wmccA/zh-cn_image_0000002659060259.png "点击放大")
* 场景二：如何实现图片超出容器右上角展示效果？

## 背景知识

* [position](../harmonyos-references/ts-universal-attributes-location.md#position)：属性属于通用属性，可对适用组件应用绝对定位，使子组件相对于最近的定位组件元素进行精确布局。
* [Stack](../harmonyos-references/js-components-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [margin](../harmonyos-references/ts-universal-attributes-size.md#margin)：设置组件的外边距属性。在布局计算过程中，外边距被视为组件尺寸的一部分，从而影响组件位置。

## 解决方案

* 场景一：

  Stack容器的默认层叠布局模式限制了Text组件的宽度，通过.margin({ left: 150 })设置的左侧外边距仅调整了文本位置，若需实现Text组件突破父容器边界显示，可通过绝对定位（position）明确设置其位置和宽度，从而使Text组件能够突破Stack容器边界，完整显示内容。

  ```ts
  @Entry
  @Component
  struct StackPageTwo {
    build() {
      Column() {
        Stack() {
          Text(' 测试测试 ')
            .borderRadius(10)
            .fontSize(30)
            .backgroundColor('#989ba1')
            .maxLines(1)
            .position({
              top: 25,
              right: 0,
              left: 100
            });
        }
        .width(200)
        .height(100)
        .borderRadius(10)
        .backgroundColor('#f1f3f5');
      }
      .alignItems(HorizontalAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/OMC4pBNYRImseiyxQGEOlQ/zh-cn_image_0000002628820886.png "点击放大")
* 场景二：

  使用Stack容器的默认层叠布局模式结合子组件position属性实现图片超出父组件右上角堆叠效果。示例代码如下：

  ```ts
  @Entry
  @Component
  struct StackPageThree {
    num: number[] = [1, 2];

    build() {
      Column() {
        ForEach(this.num, (item: number) => {
          Stack() {
            Text()
              .borderRadius(10)
              .backgroundColor('#989ba1')
              .maxLines(1)
              .width(50)
              .height(50)
              .position({
                top: -20,
                right: 0,
                left: 180
              });

            Text(`${item}`);
          }
          .margin({ top: 50 })
          .width(200)
          .height(100)
          .borderRadius(10)
          .backgroundColor('#f1f3f5');
        }, (item: number) => JSON.stringify(item));
      }
      .alignItems(HorizontalAlign.Center)
      .width('100%')
      .height('100%');
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/5MzM7zh0R1e6CbDYTDlQTA/zh-cn_image_0000002659020191.png "点击放大")
