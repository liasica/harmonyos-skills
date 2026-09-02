---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-484
title: 如何实现当长按触发成功后，移出组件取消当前长按手势
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现当长按触发成功后，移出组件取消当前长按手势
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3c20aae9d946d91be51b7ceea61945b65d2c3490633ce294e1b831a5e2608eaa
---

当前长按手势的规格为：触发成功后不会判断移动是否超出组件范围。如需实现该场景，可以结合onTouch判断手指位置是否在组件内自定义长按手势的业务逻辑是否执行。示例如下：

```ts
@Entry
@Component
struct CancelLongPressEventWhenRemovingComponents {
  private recWidth: number = 200;
  private recHeight: number = 100;
  @State isLongPressing: boolean = false;
  @State shouldCancel: boolean = false;
  @State touchInBounds: boolean = true;

  build() {
    Column() {
      // Touchable area.
      Stack() {
        Text(this.isLongPressing ? 'Long Pressing...' : 'Long press me')
          .fontSize(20)
          .fontColor(Color.White)
      }
      .width(this.recWidth)
      .height(this.recHeight)
      .backgroundColor(this.isLongPressing ? Color.Red : Color.Blue)
      .gesture(
        LongPressGesture({ repeat: false })
          .onAction(() => {
            if (!this.shouldCancel && this.touchInBounds) {
              this.handleLongPressStart();
            }
          })
          .onActionEnd(() => {
            this.handleLongPressEnd();
          })
      )
      .onTouch((event: TouchEvent) => {
        this.handleTouchEvent(event);
      })
      .onClick(() => {
        console.info('onClick');
      })
      .width(this.recWidth)
      .height(this.recHeight)

    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }

  // Handling touch events.
  private handleTouchEvent(event: TouchEvent) {
    const touchX = event.touches[0].x;
    const touchY = event.touches[0].y;
    // Calculate whether the touch point is within the component boundary.
    const inBounds = touchX >= 0 && touchX <= this.recWidth && touchY >= 0 && touchY <= this.recHeight;
    switch (event.type) {
      case TouchType.Down:
        this.shouldCancel = false;
        this.touchInBounds = true;
        break;
      case TouchType.Move:
        // Update touch position status.
        this.touchInBounds = inBounds;
        // If moving out of the boundary and long pressing, cancel.
        if (!inBounds && this.isLongPressing) {
          this.shouldCancel = true;
          this.isLongPressing = false;
          console.info('LongPressCancel', 'Slide beyond the boundary, cancel long press.');
        }
        break;
      case TouchType.Up:
        this.shouldCancel = true;
        this.touchInBounds = true;
        break;
    }
  }

  // Long press to start processing.
  private handleLongPressStart() {
    console.info('LongPress', 'Long press to start');
    this.isLongPressing = true;
  }

  // Long press to end processing.
  private handleLongPressEnd() {
    console.info('LongPress', 'Long press to end');
    this.isLongPressing = false;
    this.shouldCancel = false;
  }
}
```
