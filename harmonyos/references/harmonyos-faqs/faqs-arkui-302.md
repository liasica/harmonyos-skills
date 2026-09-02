---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-302
title: 如何获取组件渲染完成时间
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何获取组件渲染完成时间
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7de8a4bc30b5c0fd093f71ce93b6487de768adf621d501c56b96d3c63cc26122
---

可以通过@kit.ArkUI.inspector(绘制完成回调) 接口获取绘制完成回调的通知。 创建ComponentObserver实例 ，注册draw事件监听 ，在aboutToAppear中记录开始时间，在listener中监听绘制完成的回调，获取绘制完成的时间。时间差即为组件渲染时间。示例代码如下：

```ts
import { inspector } from '@kit.ArkUI';

@Entry
@Component
struct GetComponentRenderTime {
  @State startTime: number = 0;
  private listener: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('IMAGE_ID');
  // Calculate rendering duration: currentTime - this.startTime
  private onDrawCompleteCallback = () => {
    // 2. Time when the image component finishes drawing
    console.info('onDrawComplete', new Date().getTime());
  };

  aboutToAppear() {
    // 1. Time when rendering starts
    this.startTime = new Date().getTime();
    console.info('aboutToAppear', this.startTime);

    // layout: Component layout completed
    // draw: Component drawing completed
    this.listener.on('draw', this.onDrawCompleteCallback);
  }

  aboutToDisappear() {
    // Unregister callback before destruction
    this.listener.off('draw', this.onDrawCompleteCallback);
  }

  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Image($r('app.media.app_icon'))
            .width(110)
            .height(110)
            .id('IMAGE_ID')
        }
      }
    }
    .height(320)
    .width(360)
    .padding({
      right: 10,
      top: 10
    })
  }
}
```
