---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1360
title: 拖拽模块到指定位置
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 拖拽模块到指定位置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:24ac9a15db96e61ce019603d109e20d15d08e1c167de861bd174c89c3da5fa41
---

## 问题现象

如何实现拖动一个模块到指定位置的功能？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/zpTwdz-lQXSaOGEA7UWBRA/zh-cn_image_0000002628761882.png "点击放大")

## 背景知识

[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)为滑动手势事件，当滑动的最小距离达到设定的最小值时触发滑动手势事件。

## 解决方案

可通过@State跟踪位置偏移与最终坐标，结合PanGesture手势事件实时更新坐标并触发[translate](../harmonyos-references/ts-page-transition-animation.md#translate)方法动态调整组件位置，实现拖动后停留的效果，具体步骤如下：

1. 使用@State跟踪位置状态，区分临时偏移和最终位置。
2. 通过PanGesture监听拖动事件，实时更新偏移并在结束时保存最终位置。
3. 用translate方法根据状态值动态调整组件位置，实现拖动效果。

完整示例参考如下：

```screen
@Entry
@Component
struct GestureDemo {
  build() {
    Column({ space: 16 }) {
      TextInput()
        .width(350)
        .height(400);

      Row({ space: 5 }) {
        Repeat(new Array(5).fill('0').map((item: string, index) => item + index))
          .each((repeat) => {
            GestureItem({ text: repeat.item });
          });
      }
      .width(350)
      .height(80)
      .border({ color: Color.Blue, width: 1, radius: 16 })
      .padding(10);
    }
    .padding(24)
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%');
  }
}

@Component
export struct GestureItem {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  text: string = '';

  build() {
    Button() {
      Text(this.text);
    }
    .backgroundColor('#0a59f7')
    .width(60)
    .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
    .gesture(
      PanGesture() // 当触发滑动手势时，根据回调函数修改组件的布局位置信息
        .onActionUpdate((event: GestureEvent | undefined) => {
          if (event) {
            this.offsetX = this.positionX + event.offsetX;
            this.offsetY = this.positionY + event.offsetY;
          }
        })
        .onActionEnd(() => {
          this.positionX = this.offsetX;
          this.positionY = this.offsetY;
        })
    );
  }
}
```
