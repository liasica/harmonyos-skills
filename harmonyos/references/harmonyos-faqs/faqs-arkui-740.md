---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-740
title: 如何解决拖动手势时获取屏幕位置为空的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决拖动手势时获取屏幕位置为空的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cf512eb76fe348cb95514140a73690fdaac0f2a98edf86643a7071c893f0c37f
---

## 问题现象

在实现滑动手势PanGesture时，使用双指操作（做缩放捏合动作，没有添加捏合手势），会造成异常闪退。闪退日志：

```screen
Cannot read property displayX of undefined。
```

问题代码示例参考如下：

```ts
@Entry
@Component
struct GetScreen {
  @State touchX: number = 0;
  @State touchY: number = 0;

  build() {
    Column() {
      Column() {
      }
      .width(300)
      .height(500)
      .border({ width: 0.5, color: '#000' })
      .gesture(
        PanGesture()
          .onActionStart((event: GestureEvent | undefined) => {
            if (event && event.fingerList.length > 0) {
              this.touchX = event.fingerList[0].displayX
              this.touchY = event.fingerList[0].displayY
              console.info(`fingerList: ${JSON.stringify(event.fingerList[0])}`)
              // ...
            }
          })
          .onActionUpdate((event?: GestureEvent | undefined) => {
            if (event && event.fingerList.length > 0) {
              this.touchX = event.fingerList[0].displayX
              this.touchY = event.fingerList[0].displayY
              console.info(`fingerList: ${JSON.stringify(event.fingerList[0])}`)
              // ...
            }
          })
      )
    }
    .height('100%')
    .width('100%')
    .padding(24)
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/LF5cY3tiS6Cnbl7m7Cg_Sw/zh-cn_image_0000002658914681.gif "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/uFuJjYKCRlyMnY-cYLtuAQ/zh-cn_image_0000002658794731.gif "点击放大")

## 背景知识

* [滑动手势](../harmonyos-references/ts-basic-gestures-pangesture.md)用于触发拖动手势事件，滑动达到最小滑动距离（默认值为5vp）时拖动手势识别成功。
* 事件参数[GestureEvent](../harmonyos-references/ts-gesture-common.md#gestureevent对象说明)对象中fingerList中会包含触发事件的所有触点信息。

## 问题定位

根据报错信息：

```screen
Cannot read property displayX of undefined
```

可知event.fingerList[0]上没有displayX属性。

## 分析结论

fingerList[0]会存在值为空的情况。比如两个手指操作的场景，第1、2个手指按下，后面第1个手指先抬起，这时fingerList[0]的值为空。

## 修改建议

处理时加一个判断条件，在fingerList[0]有值的情况下获取其属性。

```ts
@Entry
@Component
struct GetScreen {
  @State touchX: number = 0;
  @State touchY: number = 0;

  build() {
    Column() {
      Column() {
      }
      .width(300)
      .height(500)
      .border({ width: 0.5, color: '#000' })
      .gesture(
        PanGesture()
          .onActionStart((event: GestureEvent | undefined) => {
            // 当event.fingerList[0]有值时，再去获取屏幕位置
            if (event && event.fingerList.length > 0 && event.fingerList[0]) {
              this.touchX = event.fingerList[0].displayX;
              this.touchY = event.fingerList[0].displayY;
              console.info(`fingerList: ${event.fingerList[0]}`);
              // ...
            }
          })
          .onActionUpdate((event?: GestureEvent | undefined) => {
            // 当event.fingerList[0]有值时，再去获取屏幕位置
            if (event && event.fingerList.length > 0 && event.fingerList[0]) {
              this.touchX = event.fingerList[0].displayX;
              this.touchY = event.fingerList[0].displayY;
              console.info(`fingerList: ${JSON.stringify(event.fingerList[0])}`);
              // ...
            }
          })
      );
    }
    .height('100%')
    .width('100%')
    .padding(24);
  }
}
```
