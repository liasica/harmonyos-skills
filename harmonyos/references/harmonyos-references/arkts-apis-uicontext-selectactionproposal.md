---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-selectactionproposal
title: Class (SelectActionProposal)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (SelectActionProposal)
category: harmonyos-references
scraped_at: 2026-09-05T06:16:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f72000b5bf32f01f7f4415aa91e19925d8ae0446f5ba3313115068ea49d04074
---

智慧手势选中动作处理。当通过[registerMonitor](arkts-apis-uicontext-smartgesturecontroller.md#registermonitor)接口动态自定义智慧手势行为时，设置返回值[Class (GestureHandlingResolution)](arkts-apis-uicontext-gesturehandlingresolution.md)的selectedProposal为该类型对象，会使目标组件被选中。

**起始版本：** 26.0.0

## constructor

constructor(node: FrameNode)

智慧手势选中动作处理的构造函数。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [FrameNode](js-apis-arkui-framenode.md#framenode-1) | 是 | 响应选中动作的目标节点。 |

**示例：**

本示例实现了在智慧手势监听回调中，自定义智慧手势动作处理为智慧手势选中动作处理，完整示例请参考[示例1（启用智慧手势并自定义动作处理）](arkts-apis-uicontext-smartgesturecontroller.md#示例1启用智慧手势并自定义动作处理)。

```ts
import {
  BaseGestureHandlingProposal,
  GestureHandlingResolution,
  SelectActionProposal,
} from '@kit.ArkUI';

@Entry
@Component
struct SmartGestureControllerExample {
  private controller = this.getUIContext().getSmartGestureController();
  private smartGestureMonitor = (proposal: BaseGestureHandlingProposal) => {
    let result = new GestureHandlingResolution(true);
    let node = this.getUIContext().getFrameNodeById('target_text2');
    if (node) {
      let selectProposal = new SelectActionProposal(node);
      result.selectedProposal = selectProposal;
    }
    return result;
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
        Text('文本组件1')
          .id('target_text1')
          .fontSize(18)
          .width('100%')
          .padding(12)
          .borderRadius(10)
          .borderWidth(1)
          .smartGestureShortcut({ action: GestureShortcut.PRIMARY, enabled: true, selectable: true })
          .onClick(() => {
            console.info('smartGesture click is triggered');
          })
        Text('文本组件2')
          .id('target_text2')
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/5_M8J-_ASDWgN2oRWReq1Q/zh-cn_image_0000002712405730.png)
