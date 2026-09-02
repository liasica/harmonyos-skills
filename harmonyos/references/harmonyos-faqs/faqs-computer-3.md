---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-computer-3
title: PC设备上，页面滚动方向与预期不符
breadcrumb: FAQ > 多设备场景 > 电脑 > 常见问题 > PC设备上，页面滚动方向与预期不符
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:12edcb9fb2fb41f5db7debfbc8c301f0655deb74f0b74ef7176292995e4677a9
---

## 问题现象

PC设备上，触摸屏双指滑动，页面滚动方向与预期不符。

## 背景知识

* [滑动手势事件（PanGesture）](../harmonyos-references/ts-basic-gestures-pangesture.md)：当手势滑动的最小距离达到设定的最小值时触发滑动手势事件。以下场景均可触发滑动手势事件：

  | 触发方式 | 输入源类型 | 输入设备类型 | 备注 |
  | --- | --- | --- | --- |
  | 手指按下滑动。 | SourceTool.Finger | SourceType.TouchScreen | axisVertical和axisHorizontal均为0。 |
  | 鼠标左键按下滑动。 | SourceTool.Mouse | SourceType.Mouse | axisVertical和axisHorizontal均为0。 |
  | 鼠标滚轮滚动。 | SourceTool.Mouse | SourceType.Mouse | axisVertical或axisHorizontal不为0。 |
  | 触摸板按下左键后滑动。 | SourceTool.TouchPad | SourceType.Unknown | axisVertical和axisHorizontal均为0。 |
  | 触摸板双指滑动。 | SourceTool.TouchPad | SourceType.Unknown | axisVertical或axisHorizontal不为0。 |

## 问题定位

1. 在日志中查找关键字“axis-begin”，查到该日志说明用户触发了滑动手势事件。

   ```txt
   07-04 17:20:41.561   3261-3544     C02805/com.example...InputKeyFlow  com.example.test     I     [][OnPointerEvent:216] ac: move, first: 563858-(2025-07-04 17:20:24.881ms), 563928, count: 34, last: ac: axis-begin: 563956
   ```
2. 在日志中查找关键字“yAxis”，其中“point[n]”中的数字n代表了滑动过程中打印日志的顺序，x的值代表从axis-begin的时间到打印日志时间的间隔，y的值代表纵向的偏移量。
   * 在触摸板双指从上往下滑时，y的坐标值变大。

     ```txt
      07-04 17:38:23.640   3261-3261     C03900/com.example.test/Ace    com.example.test     I     [(100000:100000:scope)] yAxis last tracker points[5] x=0.065940 y=-167.929214
      07-04 17:38:23.640   3261-3261     C03900/com.example.test/Ace    com.example.test     I     [(100000:100000:scope)] yAxis last tracker points[4] x=0.061811 y=-152.277924
      07-04 17:38:23.640   3261-3261     C03900/com.example.test/Ace    com.example.test     I     [(100000:100000:scope)] yAxis last tracker points[3] x=0.056301 y=-134.969437
      07-04 17:38:23.640   3261-3261     C03900/com.example.test/Ace    com.example.test     I     [(100000:100000:scope)] yAxis last tracker points[2] x=0.048279 y=-117.292671
      07-04 17:38:23.640   3261-3261     C03900/com.example.test/Ace    com.example.test     I     [(100000:100000:scope)] yAxis last tracker points[1] x=0.042214 y=-99.247643
     ```
   * 在触摸板双指从下往上滑时，y的坐标值变小。

     ```txt
      07-04 17:40:36.572   3261-3261     C03900/com.example.test/Ace    com.example.test     I     [(100000:100000:scope)] yAxis last tracker points[5] x=0.038254 y=138.099686
      07-04 17:40:36.572   3261-3261     C03900/com.example.test/Ace    com.example.test     I     [(100000:100000:scope)] yAxis last tracker points[4] x=0.033880 y=120.607063
      07-04 17:40:36.572   3261-3261     C03900/com.example.test/Ace    com.example.test     I     [(100000:100000:scope)] yAxis last tracker points[3] x=0.027226 y=99.800041
      07-04 17:40:36.572   3261-3261     C03900/com.example.test/Ace    com.example.test     I     [(100000:100000:scope)] yAxis last tracker points[2] x=0.020406 y=77.335823
      07-04 17:40:36.572   3261-3261     C03900/com.example.test/Ace    com.example.test     I     [(100000:100000:scope)] yAxis last tracker points[1] x=0.013854 y=54.871605
     ```
   * 鼠标滚轮向前滚动时，y的坐标值变大。

     ```txt
      [(100000:100000:scope)] yAxis	last tracker points[5] x=0.000000 y=-45.000000
      [(100000:100000:scope)] yAxis	last tracker points[4] x=0.000000 y=0.000000
     ```
   * 鼠标滚轮向后滚动时，y的坐标值变小。

     ```txt
      [(100000:100000:scope)] yAxis Last tracker points[5] x=0.000000 y=45.000000
      [(100000:100000:scope)] yAxis Last tracker points[4] x=0.000000 y=0.000000
     ```
3. 排查监听滑动手势事件的相关代码，确认从手势方向到页面滚动方向的处理逻辑错误。

   示例代码：

   ```ts
    PanGesture(this.panOption)
      .onActionStart((event: GestureEvent) => {
        // PanGesture手势识别成功处理逻辑
        // ...
      })
      .onActionUpdate((event: GestureEvent) => {
        // PanGesture手势移动过程中处理逻辑
        // ...
      })
      .onActionEnd((event: GestureEvent) => {
        // PanGesture手势识别成功，手指抬起后处理逻辑
        // 抬起后页面滚动方向计算错误
      })
   ```

## 分析结论

应用对滑动手势事件处理逻辑错误，导致页面滚动方向与预期不符。

## 修改建议

修改滑动手势事件的处理逻辑，更正计算页面滚动方向的逻辑。

示例代码：

```ts
@Entry
@Component
struct PanGestureExample {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  private panOption: PanGestureOptions = new PanGestureOptions({ fingers: 2, direction: PanDirection.All });

  build() {
    Column() {
      Column() {
        Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
      }
      .height(200)
      .width(300)
      .padding(20)
      .border({ width: 3 })
      .margin(50)
      .translate({ x: this.offsetX, y: this.offsetY, z: 0 }) // 以组件左上角为坐标原点进行移动
      // 双指拖动触发该手势事件
      .gesture(
        PanGesture(this.panOption)
          .onActionStart((event: GestureEvent) => {
            console.info('Pan start');
            console.info('Pan start timeStamp is: ' + event.timestamp);
          })
          .onActionUpdate((event: GestureEvent) => {
            if (event) {
              this.offsetX = this.positionX + event.offsetX;
              this.offsetY = this.positionY + event.offsetY;
            }
          })
          .onActionEnd((event: GestureEvent) => {
            this.positionX = this.offsetX;
            this.positionY = this.offsetY;
            console.info('Pan end');
            console.info('Pan end timeStamp is: ' + event.timestamp);
          })
      )
    }
  }
}
```
