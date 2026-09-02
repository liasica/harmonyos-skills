---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-737
title: GestureEvent手势事件坐标之间的区别
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > GestureEvent手势事件坐标之间的区别
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:ca1e7a3d163e95578c4384e3159277d73d26e2caea0211add5b46b6b3c5fdf30
---

## 问题现象

在使用手势事件时，处理不同的坐标会得到不同的移动效果。GestureEvent手势事件的坐标之间的区别是什么？如何选择正确的坐标？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/evrOQ1vAQtupymKtQUd6hw/zh-cn_image_0000002658914551.gif "点击放大")

## 背景知识

* [添加手势响应](../harmonyos-guides/arkts-interaction-development-guide-support-gesture.md)：当用户的操作符合某个手势的特征时，系统会将其识别为该手势，这一过程称为手势识别。为了响应某一个手势，需在组件上添加对应的手势对象，以便系统可以收集并进行处理。
* [GestureEvent对象](../harmonyos-references/ts-gesture-common.md#gestureevent对象说明)：继承于[BaseEvent对象](../harmonyos-references/ts-gesture-customize-judge.md#baseevent8)，是HarmonyOS中用于表示手势事件的数据类型对象。这个对象包含了处理手势事件所需的信息，例如事件类型、目标信息等。

## 解决方案

GestureEvent手势事件中涉及的坐标之间的区别主要在于参考系的不同。由于参考系的不同，不同的坐标适用于不同的使用场景，具体如下表所示：

| 坐标 | 参考系 | 常见使用场景 |
| --- | --- | --- |
| offsetX / offsetY | 手势起点 | 计算滑动距离和方向 |
| localX / localY | 当前组件元素原始区域左上角 | 组件内部交互，例如Canvas画布绘制 |
| displayX / displayY | 物理屏幕左上角 | 全局手势，例如检测滑动手势是否靠近屏幕边缘 |

**根据使用场景选择适合的坐标：**

* 使用offsetX/offsetY计算滑动距离的示例可参考[PanGesture实现了单指/双指滑动手势](../harmonyos-references/ts-basic-gestures-pangesture.md#示例)。
* 使用displayX/displayY检测滑动手势是否靠近屏幕边缘。关键代码如下：

  ```ts
  @Entry
  @Component
  struct EdgeGestureDemo {
    @State edgeTriggered: boolean = false;

    build() {
      Column() {
        Text(this.edgeTriggered ? '触发返回手势' : '从屏幕左边缘右滑')
          .fontSize(20)
          .margin(50);
      }
      .width('100%')
      .height('100%')
      .gesture(
        PanGesture()
          .onActionUpdate((event: GestureEvent) => {
            // 使用displayX检测屏幕边缘，其中数值30和60仅作示例，根据业务实际需要做出调整
            if (event.fingerList[0].displayX < 60 &&
              event.offsetX > 30) { // 从边缘滑动超过30vp
              this.edgeTriggered = true;
            }
          })
          .onActionEnd(() => {
            this.edgeTriggered = false;
          })
      );
    }
  }
  ```

* 使用localX/localY实现Canvas手签功能。当手指按下时，记录当前位置并开始新的路径。当手指移动时，调用draw()方法绘制线段。当手指抬起时，关闭路径并结束绘制。示例可以参考：[公文审批-画板签名、文件预览下载](../architecture-guides/document_approval-0000002280673593.md)。

## 总结

在实际使用时，可以根据业务场景灵活的选用合适的坐标去实现需要的效果。
