---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-630
title: 如何实现子组件对角线分布效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现子组件对角线分布效果
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:989f923cba1d77e784c8d62d09bb7445a79ae3eb3fcd03dff517026c3f790765
---

## 问题现象

如何实现组件对角线布局效果，如一个子组件位于父组件的左上角，另一个子组件位于父组件的右下角。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/vqHHx8ZXS5mbbKzKuxkepw/zh-cn_image_0000002658913489.png "点击放大")

## 背景知识

* [层叠布局](../harmonyos-guides/arkts-layout-development-stack-layout.md)用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过[Stack](../harmonyos-references/ts-container-stack.md)容器组件实现位置的固定定位与层叠，容器中的子元素依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。
* [相对布局](../harmonyos-guides/arkts-layout-development-relative-layout.md)是一种采用相对布局的容器，支持容器内部的子元素设置相对位置关系，适用于处理界面复杂的场景，对多个子元素进行对齐和排列。子元素可以指定兄弟元素或父容器作为锚点，基于锚点进行相对位置布局。
* [position属性](../harmonyos-references/ts-universal-attributes-location.md#position)：确定子组件相对父组件内容区的位置。

## 解决方案

* **方案一**：使用相对布局。

  实现原理：通过相对布局RelativeContainer，指定容器中两个子组件的相对关系，使它们互为对角线。

  ```ts
  @Entry
  @Component
  struct RelativeContainerPage {
    build() {
      Column() {
        Text('使用相对布局')
          .fontSize(20)
        RelativeContainer() {
          Row()
            .width(100)
            .height(100)
            .justifyContent(FlexAlign.Center)
            .backgroundColor('#0A59F7')
            .alignRules({
              top: { anchor: '__container__', align: VerticalAlign.Top },
              left: { anchor: '__container__', align: HorizontalAlign.Start }
            })

          Row()
            .width(100)
            .height(100)
            .justifyContent(FlexAlign.Center)
            .backgroundColor('#F1F3F5')
            .alignRules({
              bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
              right: { anchor: '__container__', align: HorizontalAlign.End }
            })
        }
        .width(300)
        .height(300)
        .border({ width: 2, color: '#6699FF' })
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/MK6T1cHWSS2x6za0-bkduQ/zh-cn_image_0000002658793541.png "点击放大")
* **方案二**：使用Stack组件。

  实现原理：设置多个子组件在容器内的对齐方式，但需要定义里面Stack组件的宽高，来控制子组件重叠情况。

  **说明** 

  当Stack组件中有多个节点触摸区域重叠时，如两个节点，默认只会对显示在最上层的节点做触摸测试，若需要显示在下层的节点触发触摸测试，需给显示在上层的节点设置hitTestBehavior为HitTestMode.Transparent。

  ```ts
  @Entry
  @Component
  struct StackPage {
    build() {
      Column() {
        Text('使用Stack组件')
          .fontSize(20)
        Stack({ alignContent: Alignment.TopStart }) {
          Row()
            .size({ width: '100', height: '100' })
            .backgroundColor('#F1F3F5')
          Stack({ alignContent: Alignment.BottomEnd }) {
            Row()
              .size({ width: '100', height: '100' })
              .backgroundColor('#0A59F7')
          }
          .width('300')
          .height('300')
          .border({ width: 2, color: '#6699FF' })
          // 若需要触发下层组件的触摸测试，需要进行下述设置
          .hitTestBehavior(HitTestMode.Transparent)
        }
      }
      .height('100%')
      .width('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/2aVgSvTrRdS6BnEkWdf6fg/zh-cn_image_0000002628554174.png "点击放大")
* **方案三**：设置position属性。

  实现原理： 基于父组件内容区四边确定位置，top/left/right/bottom分别为组件各边距离父组件内容区相应边的边距，通过边距来确定组件相对于父组件内容区的位置。

  ```ts
  @Entry
  @Component
  struct PositionPage {
    build() {
      Column() {
        Text('使用绝对定位')
          .fontSize(20)
        Stack() {
          Text('Text1')
            .width(100)
            .height(100)
            .backgroundColor('#0A59F7')
            .position({ top: 0, left: 0 })
          Text('Text2')
            .width(100)
            .height(100)
            .backgroundColor('#F1F3F5')
            .position({ right: 0, bottom: 0 })
        }
        .width(300)
        .height(300)
        .border({ width: 2, color: '#6699FF' })
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .alignItems(HorizontalAlign.Center)
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/i_R6sR9HQ429qn2bYXnPDA/zh-cn_image_0000002628394276.png "点击放大")

## 总结

上述各方法的适用场景如下：

| 方法 | 适用场景 |
| --- | --- |
| 使用相对布局 | 复杂布局或需要复用布局逻辑的场景。 |
| 使用Stack组件 | 布局轻量，且需要层叠或非对称排列的场景。 |
| 设置position属性 | 需要设置子组件相对父组件内容区的位置的场景。 |
