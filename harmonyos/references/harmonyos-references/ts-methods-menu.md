---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-menu
title: ContextMenu
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 菜单 > ContextMenu
category: harmonyos-references
scraped_at: 2026-04-29T13:52:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8ea24563233040193fed69ce6f21b1659eaf066276bb59364265b9844353335a
---

在页面范围内关闭通过[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu12)属性绑定的菜单。

说明

从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## ContextMenu.close(deprecated)

PhonePC/2in1TabletTVWearable

static close()

可以通过该方法在页面范围内关闭通过[bindContextMenu](ts-universal-attributes-menu.md#bindcontextmenu12)为组件绑定的菜单。

说明

从API version 18开始废弃，建议使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getContextMenuController](arkts-apis-uicontext-uicontext.md#getcontextmenucontroller12)获取[ContextMenuController](arkts-apis-uicontext-contextmenucontroller.md)实例，再通过此实例调用替代方法[close](arkts-apis-uicontext-contextmenucontroller.md#close12)。

从API version 12开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getContextMenuController](arkts-apis-uicontext-uicontext.md#getcontextmenucontroller12)来明确UI的执行上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 示例

PhonePC/2in1TabletTVWearable

该示例为ContextMenu.close关闭通过bindContextMenu属性绑定的菜单。

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getContextMenuController](arkts-apis-uicontext-uicontext.md#getcontextmenucontroller12)来明确UI的执行上下文。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @Builder MenuBuilder() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
7. Button('ContextMenu1')
8. Divider().strokeWidth(2).margin(5).color(Color.Black)
9. Button('ContextMenu2')
10. Divider().strokeWidth(2).margin(5).color(Color.Black)
11. Button('ContextMenu3')
12. }
13. .width(200)
14. .height(160)
15. }

17. build() {
18. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
19. Column() {
20. Text('Long press to show ContextMenu')
21. .fontSize(20)
22. .width('100%')
23. .height(500)
24. .backgroundColor(0xAFEEEE)
25. .textAlign(TextAlign.Center)
26. }
27. .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
28. .onDragStart(()=>{
29. // 拖拽时关闭菜单
30. ContextMenu.close() // 建议使用 this.getUIContext().getContextMenuController().close()
31. })
32. }
33. .width('100%')
34. .height('100%')
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/VNE8ZqLpTXOePSxwzQUUSQ/zh-cn_image_0000002558766548.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055239Z&HW-CC-Expire=86400&HW-CC-Sign=AB83B8095FFC5C0D1E57AE5FA3484EA5F7FBBF34046604A32C6E4C32AA01F918)
