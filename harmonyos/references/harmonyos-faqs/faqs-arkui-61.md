---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-61
title: Image无法使用bindContextMenu
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Image无法使用bindContextMenu
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4a8736cfbb12cea39813c2c3ccdce4ffbe1131d4de5e03e5433c128a4fd622ca
---

Image组件默认启用长按拖拽功能，会与bindContextMenu的长按弹出菜单冲突，需显式设置draggable(false)来禁用拖拽。参考代码如下：

```ts
@Entry
@Component
struct Index {
  @Builder
  menuBuilder() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Test ContextMenu1')
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
      Column() {
        Image($r('app.media.icon'))
          .draggable(false)
          .width('100vp')
      }
      .bindContextMenu(this.menuBuilder, ResponseType.LongPress)
      .onDragStart(() => {
        // Close menu when dragging
        this.getUIContext().getContextMenuController().close()
      })

    }
    .width('100%')
    .height('100%')
  }
}
```

**参考链接**

[菜单控制](../harmonyos-references/ts-universal-attributes-menu.md)，[Image组件](../harmonyos-references/ts-basic-components-image.md)
