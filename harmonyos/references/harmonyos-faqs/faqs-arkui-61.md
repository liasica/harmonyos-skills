---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-61
title: Image无法使用bindContextMenu
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Image无法使用bindContextMenu
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c2f24e62d8aa8c64ad1ed90f759c251a8df62a79b2bb9376265ae802c09cb034
---

Image组件默认启用长按拖拽功能，会与bindContextMenu的长按弹出菜单冲突，需显式设置draggable(false)来禁用拖拽。参考代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. @Builder
5. menuBuilder() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
7. Button('Test ContextMenu1')
8. Divider().strokeWidth(2).margin(5).color(Color.Black)
9. Button('Test ContextMenu2')
10. Divider().strokeWidth(2).margin(5).color(Color.Black)
11. Button('Test ContextMenu3')
12. }
13. .width(200)
14. .height(160)
15. }

17. build() {
18. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
19. Column() {
20. Image($r('app.media.icon'))
21. .draggable(false)
22. .width('100vp')
23. }
24. .bindContextMenu(this.menuBuilder, ResponseType.LongPress)
25. .onDragStart(() => {
26. // Close menu when dragging
27. this.getUIContext().getContextMenuController().close()
28. })

30. }
31. .width('100%')
32. .height('100%')
33. }
34. }
```

[ImageCanNotUseBindContextMenu.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImageCanNotUseBindContextMenu.ets#L21-L54)

**参考链接**

[菜单控制](../harmonyos-references/ts-universal-attributes-menu.md)，[Image组件](../harmonyos-references/ts-basic-components-image.md)
