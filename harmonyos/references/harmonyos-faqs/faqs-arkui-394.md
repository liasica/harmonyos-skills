---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-394
title: 如何对手势事件进行限流？例如500ms内不允许点击事件重复触发
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何对手势事件进行限流？例如500ms内不允许点击事件重复触发
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:24b2b692a4d4a0ed5317fc55810e538da2afce75e2b12fc1b797b865907440a4
---

可以自定义节流函数。

```typescript
// Debouncing: When a function is triggered multiple times within a certain period, debouncing ensures that the function is ultimately executed only once after a specified delay
export function debounce(func: (event: ClickEvent) => void, delay?: number) {
  let timer: number;
  return (event: ClickEvent) => {
    clearTimeout(timer);
    timer = setTimeout(() => {
      func(event);
    }, delay ? delay : 1000);
  };
}

// Throttling: Execute only once within the specified time frame
export function throttle(func: (event: ClickEvent) => void, delay?: number) {
  let inThrottle: boolean;
  return (event: ClickEvent) => {
    if (!inThrottle) {
      func(event);
      inThrottle = true;
      setTimeout(() => inThrottle = false, delay ? delay : 1000);
    }
  };
}

@Entry
@Component
struct Index {
  @State num: number = 0

  build() {
    Row() {
      Column() {
        Text(this.num.toString())
        Button("click")
          .onClick(
            debounce(() => {
              this.num++
            }, 500))
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

如果手势在多处使用，且都需要限流，可以考虑用[GestureModifier](../harmonyos-references/ts-universal-attributes-gesture-modifier.md#gesturemodifier)。

以下示例，演示了TapGesture和LongPressGesture共用一个限流函数，即点击事件、长按事件在2000ms内只能触发一次。

```typescript
class MyGesture implements GestureModifier {
  interval: number = 2000;
  private inThrottle: boolean = false;
  private lastGestureType: string = '';

  // Unified rate limiting processing
  private throttleWrapper(eventType: string, callback: () => void) {
    if (!this.inThrottle) {
      this.inThrottle = true;
      this.lastGestureType = eventType;
      callback();

      setTimeout(() => {
        this.inThrottle = false;
        this.lastGestureType = '';
      }, this.interval);
    }
  }

  applyGesture(event: UIGestureEvent): void {
    // Create a unified gesture processing function
    const handleTap = (gestureEvent: GestureEvent) => {
      this.throttleWrapper('tap', () => {
        console.info('---onTap---');
      });
    };

    const handleLongPress = (gestureEvent: GestureEvent) => {
      this.throttleWrapper('longPress', () => {
        console.info('---onLongPress---');
      });
    };

    // Add two gesture recognizers
    event.addGesture(
      new TapGestureHandler({ count: 1, fingers: 1 })
        .onAction(handleTap)
    );

    event.addGesture(
      new LongPressGestureHandler({ fingers: 1, duration: 600 })
        .onAction(handleLongPress)
    );
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  @State modifier: MyGesture = new MyGesture();

  build() {
    RelativeContainer() {
      Button(this.message)
        .id('click')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: "__container__", align: VerticalAlign.Center },
          middle: { anchor: "__container__", align: HorizontalAlign.Center }
        })
        .gestureModifier(this.modifier)
    }
    .height('100%')
    .width('100%')
  }
}
```
