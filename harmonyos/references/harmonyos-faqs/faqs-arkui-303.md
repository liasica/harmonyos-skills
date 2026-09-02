---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-303
title: Toggle组件设置拖动的同时如何屏蔽其本身的点击手势
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Toggle组件设置拖动的同时如何屏蔽其本身的点击手势
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:11919ab404187256fab5a87567009a5a5a2025f24cb50dacbf4c52815d32c568
---

通过isDragging状态变量区分拖动与点击操作，在拖动过程中屏蔽toggleIsOn的状态变更，示例代码如下：

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct ToggleDrag {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  @State toggleIsOn: boolean = true;
  // Marks whether the current drag state is used to block click events
  private isDragging: boolean = false;

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      Toggle({ type: ToggleType.Button, isOn: this.toggleIsOn }) {
        Text('Toggle')
      }
      .selectedColor(Color.Pink)
      // Onchange callback precedes onActionEnd
      .onChange((isOn: boolean) => {
        hilog.info(0x0000, 'TOGGLE_DRAG', 'xxx %{public}s', `onClick Toggle, isOn: ${isOn}`);
        console.info('isDragging======' + this.isDragging);
        if (isOn === this.toggleIsOn) {
          return;
        } else {
          this.toggleIsOn = isOn;
        }
        if (this.isDragging) {
          this.toggleIsOn = !this.toggleIsOn;
        }
      })
      .translate({ x: this.offsetX, y: this.offsetY })
      .gesture(
        PanGesture()
          .onActionStart(() => {
            this.isDragging = true;
          })
          .onActionUpdate((event: GestureEvent) => {
            this.offsetX = this.positionX + event.offsetX;
            this.offsetY = this.positionY + event.offsetY;
          })
          .onActionEnd(() => {
            this.positionX = this.offsetX;
            this.positionY = this.offsetY;
            this.isDragging = false;
          })
      )
    }
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/YIW6nNZWTwKlZIHj_dhHDQ/zh-cn_image_0000002654835241.png)
