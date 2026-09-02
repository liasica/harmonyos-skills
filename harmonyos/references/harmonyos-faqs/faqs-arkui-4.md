---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-4
title: 如何在长按手势回调方法里获取手指触摸点的坐标
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何在长按手势回调方法里获取手指触摸点的坐标
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2f73b63c3218789a370701a18cbcefbe389fcb340ea98fccd529be03a11f4e2c
---

使用[组合手势](../harmonyos-guides/arkts-gesture-events-combined-gestures.md)的顺序识别，当长按手势事件结束后触发拖动手势事件。在手势回调方法里获取event（[GestureEvent](../harmonyos-references/ts-gesture-common.md#gestureevent对象说明)类型）的fingerList（[FingerInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-common#fingerinfo8对象说明)类型），获取到localX和localY数值，表示相对于当前组件元素原始区域左上角的坐标位置。可参考如下代码：

```typescript
@Component
struct CoordinatesOfTheFingerTouchPoint {
  @State count: number = 0;
  private touchAreaRight: number = 0;
  private touchAreaBottom: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  @State gestureEventInfo: string = '';

  build() {
    Column() {
      Row() {
        Column() {
          Text('+')
            .fontSize(28)
            .position({ x: this.positionX, y: this.positionY })
        }
        .height(200)
        .width('100%')
        .backgroundColor('#F1F3F5')
        .onAreaChange((oldValue: Area, newValue: Area) => {
          this.touchAreaRight = newValue.width as number;
          this.touchAreaBottom = newValue.height as number;
        })
        .gesture(
          // The following combined gestures are recognized sequentially. If the long press gesture event is not triggered normally, the drag gesture event will not be triggered.
          GestureGroup(GestureMode.Sequence,
            LongPressGesture({ repeat: true })
              .onAction((event: GestureEvent) => {
                if (event.repeat) {
                  this.count++;
                }
              }),
            PanGesture()
              .onActionStart(() => {
                this.getUIContext().getPromptAction().showToast({ message: 'Pan start', duration: 1000 });
              })
              .onActionUpdate((event: GestureEvent) => {
                for (let i = 0; i < event.fingerList.length; i++) {
                  if (event.fingerList[i] == undefined
                    || event.fingerList[i].localX < 0
                    || event.fingerList[i].localY < 0
                    || event.fingerList[i].localX > this.touchAreaRight
                    || event.fingerList[i].localY > this.touchAreaBottom) {
                    return;
                  }
                  this.positionX = event.fingerList[i].localX;
                  this.positionY = event.fingerList[i].localY;
                }
                this.gestureEventInfo = 'sequence gesture\n' + 'LongPress onAction' + this.count
                  + '\nX:' + this.positionX + '\nY:' + this.positionY;
              })
              .onActionEnd(() => {
                this.getUIContext().getPromptAction().showToast({ message: 'Pan end', duration: 1000 });
              })
          )
            .onCancel(() => {
              this.getUIContext().getPromptAction().showToast({ message: 'Cancel', duration: 1000 });
            })
        )
      }
      .padding(12)
      .borderRadius(24)
      .backgroundColor(Color.White)

      Text(this.gestureEventInfo)
        .fontSize(18)
        .width('100%')
        .textAlign(TextAlign.Start)
        .padding({ left: 18, top: 30 })
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#F1F3F5')
  }
}
```
