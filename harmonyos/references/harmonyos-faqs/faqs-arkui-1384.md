---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1384
title: 如何勾勒出类似人脸的轮廓
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何勾勒出类似人脸的轮廓
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:64dac2ac64eec1cc48e09ac5c2733d62bd18bb760ecc7cb49920322a52e454c2
---

## 问题现象

使用四个椭圆，如何绘制出类似人脸的轮廓？可用于人脸识别、手机扫描等场景。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/2VI1FZh_TXu7y_POWdweVw/zh-cn_image_0000002658961875.png "点击放大")

## 背景知识

* [Ellipse](../harmonyos-references/ts-drawing-components-ellipse.md)：椭圆绘制组件。
* [Stack](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。
* [rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate)：设置组件旋转。
* [blendMode](../harmonyos-references/ts-universal-attributes-image-effect.md#blendmode11)：将当前控件的内容（包含子节点内容）与下方画布（可能为离屏画布）已有内容进行混合。

## 解决方案

1. 使用Stack组件，将各个椭圆、圆形进行堆叠嵌套。
2. 通过rotate属性调整Ellipse组件的位置，初步形成人脸形状。
3. 给Ellipse组件设置.blendMode(BlendMode.CLEAR)，将源像素覆盖的目标像素清除为完全透明最终形成人脸轮廓。

示例代码如下：

```ts
@Entry
@Component
struct FacialContour {
  build() {
    Column() {
      Stack() {
        // 相机预览区域
        Column() {
        }
        .width(300)
        .height(300)
        .borderRadius(150);

        Ellipse({ width: '40.96', height: '71.56' })
          .margin({
            top: 112.68,
            left: 29.38,
            right: 171.13,
            bottom: 87.68
          })
          .rotate({
            angle: '-45.05'

          })
          .strokeWidth(3)
          .stroke(Color.Red)
          .strokeDashArray([1, 2])
          .fill(Color.Transparent)
          .blendMode(BlendMode.CLEAR);

        Ellipse({ width: '40.96', height: '71.56' })
          .margin({
            top: 112.68,
            left: 171.13,
            right: 29.38,
            bottom: 87.68
          })
          .rotate({
            angle: '-134.95'
          })
          .strokeWidth(3)
          .stroke(Color.Red)
          .strokeDashArray([1, 2])
          .fill(Color.Transparent)
          .blendMode(BlendMode.CLEAR);

        Ellipse({ width: '143', height: '190' })
          .margin({
            top: 63,
            left: 68,
            right: 69,
            bottom: 27
          })
          .fill(Color.Transparent)
          .strokeWidth(3)
          .stroke(Color.Red)
          .strokeDashArray([1, 2])
          .blendMode(BlendMode.CLEAR);

        Ellipse({ width: '168', height: '174' })
          .margin({
            top: 26,
            left: 56,
            right: 56,
            bottom: 80
          })
          .fill(Color.Transparent)
          .blendMode(BlendMode.CLEAR)
          .strokeWidth(3)
          .stroke(Color.Red)
          .strokeDashArray([1, 2]);

        Circle()
          .width(280)
          .height(280)
          .fill('rgb(0, 0, 0)')
          .opacity(0.2)
          .strokeWidth(3)
          .width(280)
          .height(280);

        Circle()
          .width(300)
          .height(300)
          .fillOpacity(0)
          .strokeWidth(2)
          .stroke('#fc29b2e0');

        Text('请面部正对摄像头')
          .textAlign(TextAlign.Center)
          .width(244)
          .height(20)
          .fontWeight(400)
          .fontSize(20)
          .lineHeight(20)
          .fontColor('rgb(0, 0, 0)')
          .offset({ y: 182 });
      }
      .width(300)
      .height(300)
      .margin({
        top: 106,
        left: 30,
        right: 30,
        bottom: 386
      })
      .alignContent(Alignment.Center);
    }.height('100%').width('100%');
  }
}
```
