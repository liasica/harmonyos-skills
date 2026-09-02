---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-934
title: onTouch事件在点击时一直触发Move状态的特性及处理逻辑
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > onTouch事件在点击时一直触发Move状态的特性及处理逻辑
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c72a480edd2b4f40411ad3ab35fb9fc681672120768fe9a107d58464e2eb83ce
---

## 问题现象

onTouch事件在点击时，会持续触发TouchType.Move事件，在按下去的瞬间，Down状态被触发后Move状态也会被触发，即使手指不移动也会一直触发Move状态。在模拟器上，TouchType的表现正常，不移动不触发，但是在真机上只要点击就会触发，这是否为正常现象？

## 背景知识

* [onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)触摸事件，手指触摸动作触发该回调。包含按压、抬起、移动、取消等事件。
* [TouchEvent](../harmonyos-references/ts-universal-events-touch.md#touchevent对象说明)中的changedTouches表示有变化的触摸点，根据onTouch里的事件可以获取到事件的偏移量横向x，纵向y，处理相应的逻辑处理。

## 解决方案

在HarmonyOS应用开发中，onTouch事件在真机上持续触发TouchType.Move属于正常现象，主要源于以下特性与处理逻辑：

1. 事件机制特性：

   触控采样率差异：changedTouches按屏幕刷新率重采样，touches按器件刷新率上报。真机的触摸传感器通常具有高灵敏度，即使手指轻微抖动（用户可能感知不到），传感器仍会捕捉到坐标变化并触发Move事件。
2. 系统级事件处理：

   HarmonyOS框架为优化交互体验，会主动上报细微的触控变化。这在需要高精度触控的场景（如绘图应用）中是有益的，但在点击场景下可能造成多次Move事件触发。

如果不需要无效的移动事件，可通过代码逻辑过滤掉：

```ts
@Entry
@Component
struct OnTouchMove {
  @State startX: number = 0;
  @State startY: number = 0;
  // 设置移动阈值（单位：vp）
  readonly MOVE_THRESHOLD: number = 5;

  build() {
    Column() {
      Button('onTouch')
        .onTouch((event: TouchEvent) => {
          if (!event.touches || event.touches.length === 0) {
            return;
          }

          switch (event.type) {
            case TouchType.Down:
              this.startX = event.touches[0].x;
              this.startY = event.touches[0].y;
              console.info('按下');
              break;

            case TouchType.Move:
              const currentX: number = event.touches[0].x;
              const currentY: number = event.touches[0].y;
              // 计算偏移量
              const deltaX = Math.abs(currentX - this.startX);
              const deltaY = Math.abs(currentY - this.startY);
              // 当移动距离超出阈值时，触发move状态
              if (deltaX > this.MOVE_THRESHOLD || deltaY > this.MOVE_THRESHOLD) {
                console.info('有效移动:', currentX, currentY);
                // 更新起始坐标
                this.startX = currentX;
                this.startY = currentY;
              }
              break;

            case TouchType.Up:
              console.info('抬起');
              break;
          }
        });
    }
    .width('100%')
    .height('100%');
  }
}
```

## 总结

onTouch事件在真机上持续触发TouchType.Move属于正常现象，高频次触发的Move事件会导致性能问题，对点击操作敏感的场景（如按钮），建议优先使用onClick事件，避免onTouch的复杂处理逻辑。
