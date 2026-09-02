---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1109
title: 实现卡片投影效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现卡片投影效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9d2c4a126bbe7eefa8b99970e7da0bea9770deed23ff680ab1d9132f686ab498
---

## 问题现象

当给组件设置阴影属性时，可以实现投影效果，使组件具有悬浮和立体感。以下是几种具体的投影效果：

| 场景 | 场景说明 |
| --- | --- |
| 场景一：实现右下角投影效果 | 当阴影仅添加在右下角时，可以模拟光从左上角打过来的视觉效果。 |
| 场景二：实现阴影扩展效果 | 控制阴影区域向外扩展。 |
| 场景三：实现多个阴影样式 | 实现左上角亮色阴影，右下角暗色阴影，增强立体感。 |

## 背景知识

[shadow](../harmonyos-references/ts-universal-attributes-image-effect.md#shadow)为当前组件提供阴影效果，并通过设置偏移量来模拟投影效果。

## 解决方案

* 场景一：实现右下角投影效果。
  1. 使用radius属性给阴影添加圆角效果与卡片圆角对齐。
  2. 阴影颜色设置为灰色可模拟投影效果。

  示例代码如下：

  ```ts
  @Entry
  @Component
  struct Index {
    build() {
      Row() {
        Column() {
          Text('card').fontSize(12);
        }
        .width(100)
        .aspectRatio(1)
        .margin(10)
        .justifyContent(FlexAlign.Center)
        .backgroundColor('#0A59F7')
        .borderRadius(50)
        .shadow({
          radius: 50,
          color: Color.Gray,
          offsetX: 10,
          offsetY: 10
        })
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center);
      }
      .height('100%');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/wWB3CMVlRgudezN5TR5Bjg/zh-cn_image_0000002628407492.png "点击放大")
* 场景二：实现阴影扩展效果。
  1. 使用radius属性给阴影添加圆角效果与卡片圆角对齐。
  2. 给卡片外部增加一层容器，通过padding实现扩展效果，通过position实现扩展方向。

  示例代码如下：

  ```ts
  @Entry
  @Component
  struct Index2 {
    build() {
      Row() {
        Row() {
        }
        .width(300)
        .height(150)
        .borderRadius(20)
        .shadow({
          radius: 20,
          offsetX: 0,
          offsetY: 0,
          fill: true,
          type: ShadowType.COLOR,
          color: Color.White
        });
      }
      .padding(5)
      .borderRadius(20)
      .backgroundColor('#ffc1e6ff')
      .position({ x: 30, y: 100 });
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ZrVKrrzKTva3FjBiTyHQag/zh-cn_image_0000002628567388.png "点击放大")
* 场景三：实现多个阴影样式。

  通过父子组件嵌套实现，设置父子组件的大小，边框等完全一致，仅设置的阴影效果不一致。

  示例代码如下：

  ```ts
  @Entry
  @Component
  struct Index3 {
    build() {
      Column() {
        // 外层：暗色阴影（右下）
        Column() {
          // 内层：亮色阴影（左上）
          Column() {
          }
          .width(200)
          .aspectRatio(1)
          .justifyContent(FlexAlign.Center)
          .backgroundColor('#e0e0e0')
          .borderRadius(100)
          .shadow({
            radius: 20,
            color: '#ffffff',
            offsetX: -10,
            offsetY: -10
          });
        }
        .width(200)
        .aspectRatio(1)
        .justifyContent(FlexAlign.Center)
        .borderRadius(100)
        .shadow({
          radius: 20,
          color: '#a0a0a0',
          offsetX: 10,
          offsetY: 10
        });
      }
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Center)
      .backgroundColor('#e0e0e0');
    }
  }
  ```

  效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/9tMixtb1RVyc9KCsntw3qA/zh-cn_image_0000002658926705.png "点击放大")
