---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-contextmenucontroller
title: Class (ContextMenuController)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (ContextMenuController)
category: harmonyos-references
scraped_at: 2026-09-02T15:00:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8de0a20d2b73e4c6c01a54b9575b28d941dcc39c02905a7a60601860b05cf5ed
---

提供控制菜单关闭的能力。开发者可以通过此接口在特定场景下（如定时关闭、点击外部区域关闭等）主动关闭菜单。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 本模块接口仅可在Stage模型下使用。
* 以下API需先使用UIContext中的[getContextMenuController()](arkts-apis-uicontext-uicontext.md#getcontextmenucontroller12)方法获取ContextMenuController实例，再通过此实例调用对应方法。

## close12+

close(): void

关闭当前通过bindContextMenu展示的菜单。若当前无菜单展示，调用本方法无效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

通过定时器触发，调用ContextMenuController的close方法关闭菜单。

```ts
import { ContextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  menu: ContextMenuController = this.getUIContext().getContextMenuController();

  @Builder MenuBuilder() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Test ContextMenu1 Close')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('Test ContextMenu2')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('Test ContextMenu3')
    }
    .width(200)
    .height(160)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('启动定时器').onClick(() => {
        // 延时10秒后调用close方法关闭菜单
        setTimeout(() => {
          this.menu.close();
        }, 10000);
      })

      Column() {
        Text('Test ContextMenu close')
          .fontSize(20)
          .width('100%')
          .height(500)
          .backgroundColor(0xAFEEEE)
          .textAlign(TextAlign.Center)
      }
      // 绑定自定义菜单，长按触发
      .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/HrzMQa7TQUq7o8ut2aSU7A/zh-cn_image_0000002736434669.gif)
