---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-targetedgestureproposal
title: Class (TargetedGestureProposal)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (TargetedGestureProposal)
category: harmonyos-references
scraped_at: 2026-09-02T14:51:19+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2be0352ef00c9763cef2ceb8e056e76530bf8e7f2f4d7af5b24081ca8fbef046
---

带目标节点的智慧手势处理基类。

**起始版本：** 26.0.0

## 属性

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 否 | 否 | 处理当前智慧手势的目标节点。 |

**示例：**

本示例实现了在智慧手势监听回调中，从TargetedGestureProposal获取智慧手势处理信息，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](arkts-apis-uicontext-smartgesturecontroller.md#示例1启用智慧手势并自定义动作处理)。

```ts
import {
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
  TargetedGestureProposal,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    let targetProposal = proposal as TargetedGestureProposal;
    console.info('smartGesture action is', targetProposal.action, ', operateIntention is',
      targetProposal.operateIntention, ', nodeId is', targetProposal.node.getId());
    return new GestureHandlingResolution(true);
  };

  aboutToAppear(): void {
    this.controller.enableSmartTapAndSlideGestures(true);
    this.controller.registerMonitor(this.smartGestureMonitor);
  }

  aboutToDisappear(): void {
    this.controller.clearMonitors();
    this.controller.enableSmartTapAndSlideGestures(false);
  }

  build() {
    Scroll() {
      Column({ space: 12 }) {
        Text('文本组件')
          .id('target_text')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
      }.width('100%')
    }
    .layoutWeight(1)
    .width('100%')
    .height('100%')
    .padding(12)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/WgTATJzVRWywqN3v8D7Ydw/zh-cn_image_0000002736434677.png)
