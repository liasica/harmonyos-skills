---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1493
title: 如何实现Flex组件的宽高自适应子组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现Flex组件的宽高自适应子组件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:11+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:29d1d3cc4c9a2eb6ca369b1a150367c7d88b96f1de1eb2da307da5a8d35b7a38
---

## 问题现象

问题1：Flex方向为Column时，默认高度会撑满Flex的父容器。如何让Flex的高度自适应子组件的高度？

问题2：Flex方向为Row时，默认宽度会撑满Flex的父容器，如何让Flex宽度自适应子组件的宽度？

问题1效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/iOsHcGtvQUS3o8AX5y3gjg/zh-cn_image_0000002658845079.png "点击放大")

问题2效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ceUlwK5ESE6pAny9PMaHlg/zh-cn_image_0000002628765708.png "点击放大")

## 背景知识

* [Flex](../harmonyos-references/ts-container-flex.md)是以弹性方式布局子组件的容器组件，提供更加有效的方式对容器内的子元素进行排列、对齐和分配剩余空间。
* Flex主轴不设置长度时默认撑满父容器。主轴长度可设置为auto使Flex自适应子组件布局，自适应时，Flex长度受[constraintSize](../harmonyos-references/ts-universal-attributes-size.md#constraintsize)属性以及父容器传递的最大最小长度限制，且constraintSize属性优先级更高。
* [组件区域变化事件](../harmonyos-references/ts-universal-component-area-change-event.md)，组件显示的尺寸、位置等发生变化时触发[onAreaChange](../harmonyos-references/ts-universal-component-area-change-event.md#onareachange)，仅会响应由布局变化所导致的组件大小、位置发生变化时的回调，可以获取组件位置和尺寸信息。
* [组件尺寸变化事件](../harmonyos-references/ts-universal-component-size-change-event.md)，组件显示的尺寸发生变化时触发[onSizeChange](../harmonyos-references/ts-universal-component-size-change-event.md#onsizechange)，仅会响应由布局变化所导致的组件尺寸发生变化时的回调，可以获取组件尺寸信息。

## 解决方案

* **方案一**：参考背景知识，Flex组件主轴方向设置长度为auto时，Flex自适应子组件布局。

  问题1：Flex方向为Column，可以将Flex组件高度设置为auto，使Flex自适应子组件布局的高度。

  ```ts
  @Entry
  @Component
  struct FlexExample1 {
    build() {
      Column({ space: 10 }) {
        Text('Flex方向为Column');
        Flex({ direction: FlexDirection.Column }) {
          Text('Flex的子组件\nHello World!')
            .backgroundColor('#330a59f7')
            .textAlign(TextAlign.Center)
            .borderRadius(30)
            .padding(20);
        }
        .backgroundColor('#f1f3f5')
        .height('auto');
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/RxhwmEbEQ2-KXHD7I4JXWg/zh-cn_image_0000002658965033.png "点击放大")

  问题2：Flex方向为Row时同理，设置宽度为auto，使Flex自适应子组件布局的宽度。

  ```ts
  @Entry
  @Component
  struct FlexExample2 {
    build() {
      Column({ space: 10 }) {
        Text('Flex方向为Row');
        Flex({ direction: FlexDirection.Row }) {
          Text('Flex的子组件\nHello World!')
            .backgroundColor('#330a59f7')
            .textAlign(TextAlign.Center)
            .borderRadius(30)
            .padding(20);
        }
        .backgroundColor('#f1f3f5')
        .width('auto');
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/AqnucAeOQPmnZultTIqxAA/zh-cn_image_0000002628605828.png "点击放大")
* **方案二**：Flex主轴方向长度默认设置'100%'，子组件布局完成时通过onSizeChange/onAreaChange获取尺寸信息，根据子组件尺寸设置Flex主轴方向长度。

  问题1：Flex方向为Column时，通过onSizeChange获取子组件高度，设置Flex高度。

  ```ts
  @Entry
  @Component
  struct FlexExample3 {
    @State flexHeight: number | string = '100%'; // 默认情况主轴占满

    build() {
      Column({ space: 10 }) {
        Text('Flex方向为Column');
        Flex({ direction: FlexDirection.Column }) {
          Text('Flex的子组件\nHello World!')
            .backgroundColor('#330a59f7')
            .textAlign(TextAlign.Center)
            .borderRadius(30)
            .padding(20)
            .onSizeChange((oldSize, newSize) => { // 也可以使用onAreaChange
              this.flexHeight = newSize.height as number; // 获取子组件高
            });
        }
        .backgroundColor('#f1f3f5')
        .height(this.flexHeight);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/p-eTNGliQ16fM4H1R9rlEQ/zh-cn_image_0000002658845081.png "点击放大")

  问题2：Flex方向为Row时，通过onSizeChange获取子组件宽度，设置Flex宽度。

  ```ts
  @Entry
  @Component
  struct FlexExample4 {
    @State flexWidth: number | string = '100%'; // 默认情况主轴占满

    build() {
      Column({ space: 10 }) {
        Text('Flex方向为Row');
        Flex({ direction: FlexDirection.Row }) {
          Text('Flex的子组件\nHello World!')
            .backgroundColor('#330a59f7')
            .textAlign(TextAlign.Center)
            .borderRadius(30)
            .padding(20)
            .onSizeChange((oldSize, newSize) => { // 也可以使用onAreaChange
              this.flexWidth = newSize.width as number; // 获取子组件宽
            });
        }
        .backgroundColor('#f1f3f5')
        .width(this.flexWidth);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/i3jifXYhQCud2muvSI2Gmw/zh-cn_image_0000002628765710.png "点击放大")
