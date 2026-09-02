---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1179
title: linearGradient渐变色问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > linearGradient渐变色问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9359e7357e61e0ad4dc5a780aab37a13d5fa60834a4d799076939b7c55354741
---

## 问题现象

使用linearGradient设置颜色渐变，当色值设为00时透明度未生效。

问题代码：

```ts
@Entry
@Component
struct Page1 {
  build() {
    Column() {
      Text('HarmonyOS')
        .width('80%')
        .height('50')
        .padding({ left: 15, right: 15 })
        .linearGradient({
          direction: GradientDirection.Bottom,
          colors: [[0x00333333, 0.0], [0x80000000, 1.0]]
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```

## 背景知识

* [linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)设置组件的颜色渐变效果，支持方向控制和多颜色配置。
* colors参数的约束：[ResourceColor](../harmonyos-references/ts-types.md#resourcecolor)表示填充的颜色，number表示指定颜色所处的位置，取值范围为[0,1.0]，0表示需要设置渐变色的容器的开始处，1.0表示容器的结尾处。想要实现多个颜色渐变效果时，多个数组中number参数建议递增设置，如后一个数组number参数比前一个数组number小的话，按照等于前一个数组number的值处理。
* 十六进制颜色表示解析：示例值：0x00333333=完全透明的深灰色（RGB均为0x33，即十进制51）

| 组成部分 | 含义 | 说明 |
| --- | --- | --- |
| 0x | 十六进制标识符 | 声明后续数字是十六进制 |
| 00 | 透明度（Alpha通道） | 00=完全透明，FF=不透明 |
| 33 | 红色分量（Red） | 十六进制值（0-255） |
| 33 | 绿色分量（Green） | 十六进制值（0-255） |
| 33 | 蓝色分量（Blue） | 十六进制值（0-255） |

**完整格式**：0x+AARRGGBB（AA=透明度，RR=红色，GG=绿色，BB=蓝色）

## 解决方案

* 选择适当的颜色纯度和透明度是确保linearGradient渐变效果明显的关键。纯度较高且透明度适中的颜色组合更容易产生明显的渐变效果。
* 透明度为0时，由于数值解析机制导致0x00前缀透明度失效，所以0x00的写法不支持，建议使用#00333333写法。

  ```ts
  @Entry
  @Component
  struct Page2 {
    build() {
      Column() {
        Text('0x00333333写法')
          .fontColor(Color.White)
          .width('80%')
          .height('50')
          .padding({ left: 15, right: 15 })
          .margin({ bottom: 16 })
          .textAlign(TextAlign.Center)
          .borderRadius(5)
          .linearGradient({
            direction: GradientDirection.Bottom,
            colors: [[0x00333333, 0.0], [0x80000000, 1.0]]
          });
        Text('#00333333写法')
          .width('80%')
          .height('50')
          .padding({ left: 15, right: 15 })
          .textAlign(TextAlign.Center)
          .borderRadius(5)
          .linearGradient({
            direction: GradientDirection.Bottom,
            colors: [['#00333333', 0.0], [0x80000000, 1.0]]
          });
      }
      .justifyContent(FlexAlign.Center)
      .height('100%')
      .width('100%');
    }
  }
  ```

  如下图示例：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/rVJIhBqZT7WEHuKC4v_Clw/zh-cn_image_0000002658832207.png "点击放大")

## 常见FAQ

Q：linearGradient如何设置渐变方向和多颜色配置？

A：以下两个案例介绍linearGradient的使用语法：

* 案例一：linearGradient({angle: 0, colors: [[0xff0000, 0.0], [0xffe096, 1.0]]})

  angle表示线性渐变的起始角度，角度为0度时渐变方向为从下往上（即0点方向）；

  colors为指定渐变色颜色和其对应的百分比位置的数组，其中0xff0000表示起始位置颜色，0xffe096为结束的位置颜色，中间即为0xff0000到0xffe096渐变颜色。
* 案例二：linearGradient({direction: GradientDirection.Left, repeating: true, colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 0.5]]})

  direction表示线性渐变的方向，GradientDirection.Left表示线性渐变方向为从右向左；

  repeating设置为true表示渐变的颜色重复着色；

  colors起始位置颜色为0xff0000，0.3即30%位置处的颜色为0x0000ff，0-0.3之间的区域是0xff0000到0x0000ff渐变颜色；

  数组末尾元素百分比位置为0.5，小于1满足重复着色效果，所以0.5-1为重复着色渐变效果。

Q：如何使用linearGradient实现颜色在透明度上的渐变效果？

A：可以使用rgba格式的颜色来设置透明渐变的效果，参考如下：

```ts
@Entry
@Component
struct Page3 {
  build() {
    Column() {
      Text('rgba写法')
        .width('80%')
        .height('50')
        .padding({ left: 15, right: 15 })
        .linearGradient({
          direction: GradientDirection.Bottom,
          colors: [['rgba(128,128,128,0.5)', 0.1], ['rgba(128,128,128,0.3)', 0.6], ['rgba(128,128,128,0.0)', 1]]
        });
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```
