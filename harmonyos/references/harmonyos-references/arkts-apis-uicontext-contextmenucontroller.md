---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-contextmenucontroller
title: Class (ContextMenuController)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (ContextMenuController)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f940048e956663a7ffcf5c4937d9f448a9b24ae40a02f865e44c01a183531a47
---

提供控制菜单关闭的能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 以下API需先使用UIContext中的[getContextMenuController()](arkts-apis-uicontext-uicontext.md#getcontextmenucontroller12)方法获取ContextMenuController实例，再通过此实例调用对应方法。

## close12+

PhonePC/2in1TabletTVWearable

close(): void

关闭菜单。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

通过定时器触发，调用ContextMenuController的close方法关闭菜单。

```
1. import { ContextMenuController } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. menu: ContextMenuController = this.getUIContext().getContextMenuController();

8. @Builder MenuBuilder() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Button('Test ContextMenu1 Close')
11. Divider().strokeWidth(2).margin(5).color(Color.Black)
12. Button('Test ContextMenu2')
13. Divider().strokeWidth(2).margin(5).color(Color.Black)
14. Button('Test ContextMenu3')
15. }
16. .width(200)
17. .height(160)
18. }

20. build() {
21. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
22. Button("启动定时器").onClick(()=>
23. {
24. setTimeout(() => {
25. this.menu.close();
26. }, 10000);
27. })

29. Column() {
30. Text("Test ContextMenu close")
31. .fontSize(20)
32. .width('100%')
33. .height(500)
34. .backgroundColor(0xAFEEEE)
35. .textAlign(TextAlign.Center)
36. }
37. .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
38. }
39. .width('100%')
40. .height('100%')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/FNsRo6CxSgiUV5p-6zGm_A/zh-cn_image_0000002552959406.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000019Z&HW-CC-Expire=86400&HW-CC-Sign=500CAC718DD521873EEB439DC88CCAC7CE692AB93F6C454C293FF7AAFA73755C)
