---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-special-text-recognition
title: 特殊文本识别跳转
breadcrumb: 最佳实践 > 应用框架 > 程序框架 > 特殊文本识别跳转
category: best-practices
scraped_at: 2026-04-28T08:20:11+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:12f689cf7c986e74e0eec16e3627e3e53e3e389c0a605b20b0a2b9a45767f587
---

## 概述

特殊文本识别，是指自动检测文本内容中具备特定格式或语义的信息（如链接、日期、电话号码等），并将其赋予交互功能，实现一键跳转或快捷操作。这一能力让用户在阅读、聊天、办公等场景下，无需复制粘贴即可高效完成访问网页、添加日程、拨打电话等任务。

以社交应用场景为例，当用户在聊天过程中收到包含特殊文本的消息时，系统会自动识别这些内容并渲染为可点击的链接。用户点击后，即可快速完成如打开网页、跳转应用详情、拨打电话、写邮件等操作，极大提升了用户体验和操作效率。

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/13/v3/b8mRey7YSO63BxFusfW-lg/zh-cn_media_0000002284820694.mp4?HW-CC-KV=V1&HW-CC-Date=20260428T002008Z&HW-CC-Expire=86400&HW-CC-Sign=5A09E9C54619E9CA7CB7F9C7228D06527E3200D28A90A85D5DFF7E78F9B675A2)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 2.75%

0:00

Duration 0:16

Mute

1x

Playback Rate

* 2x
* 1.8x
* 1.5x
* 1.2x
* 1x, selected

Fullscreen

This is a modal window.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

Reset restore all settings to the default valuesDone

Close Modal Dialog

End of dialog window.

本文主要是为了帮助开发者了解在社交应用中，如何识别出一段文字中的特殊文本，并将其标记为链接的格式，赋予其交互能力。常见的特殊文本类型包括：

* HTTP/HTTPS链接：点击后直接在系统浏览器中打开网址。
* App Linking链接：点击后，如目标应用已安装则直达详情页；未安装可跳转Web页面或应用市场。
* 日期：点击后，可发起新建日程操作。
* 电话号码：点击后，可选择拨打、发短信或保存联系人。
* 地址：点击后，可拉起已安装的地图应用导航。
* 邮箱：点击后，拉起邮件应用编写邮件。

用户点击这些特殊文本后，系统自动弹出操作面板，根据具体类别执行对应动作。

## 典型场景

以社交应用中好友之间相互发送聊天信息为例，这些信息中可能会包含标准HTTP/HTTPS链接、App Linking链接、日期、电话号码、地址、邮箱等。这些特殊的文本，通常会被识别为可点击的链接格式。

用户点击这些经过系统底层处理过的文本后，会拉起相应的操作菜单，点击操作菜单中的可选项后，则会进行相应的跳转处理。各种链接点击后效果如下图所示。

|  |  |  |  |
| --- | --- | --- | --- |
| 类型 | 标准HTTP/HTTPS链接 | App Linking链接 | 日期 |
| 效果图 |  |  |  |
| 类型 | 电话号码 | 地址 | 邮箱 |
| 效果图 |  |  |  |

说明

本文中所有电话号码均为示例用途，非真实可用号码。

## 实现原理

### 关键技术

Text组件提供了[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)属性，通过将该属性设置为true，即可进行文本特殊实体识别。一段文字中若包含标准HTTP/HTTPS链接、App Linking链接、日期、电话号码、地址、邮箱等，则这些特殊文本会被自动识别为可点击的链接格式。手势点击和鼠标右键点击实体，会根据实体类型弹出对应的实体操作菜单，鼠标左键点击实体会直接响应菜单的第一个选项。

常用的文本与输入组件是否支持设置[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)属性如下表所示。

| 组件 | 是否支持enableDataDetector属性 |
| --- | --- |
| Text | 是 |
| TextArea | 否 |
| TextInput | 否 |
| RichEditor | 是 |
| RichText | 否 |

### 开发流程

1. 自定义带头像和文本信息的组件。

   封装如TextLink组件，参数包含头像资源（img）和文本内容（text）。

   ```
   1. @Component
   2. export default struct TextLink {
   3. @State enableDataDetector: boolean = true;
   4. public img: string | PixelMap | Resource = $r('app.media.Public_avatar');
   5. public text: ResourceStr = '';

   7. // ...
   8. }
   ```

   [TextLink.ets](https://gitcode.com/HarmonyOS_Samples/CommonLinksSkip/blob/master/entry/src/main/ets/uiComponent/TextLink.ets#L17-L63)
2. 组件样式设置。

   为头像、文本等元素分配合适UI样式，提升聊天或内容流的展示效果。

   ```
   1. Row() {
   2. Image(this.img)
   3. .width(36)
   4. .height(36)
   5. Row() {
   6. Text(this.text)
   7. .enableDataDetector(this.enableDataDetector)
   8. }
   9. .borderRadius({
   10. topLeft: 2,
   11. topRight: 16,
   12. bottomLeft: 16,
   13. bottomRight: 16
   14. })
   15. .margin({ left: 8 })
   16. .padding({
   17. left: 12,
   18. right: 12,
   19. top: 12,
   20. bottom: 12
   21. })
   22. .backgroundColor(Color.White)
   23. .constraintSize({ maxWidth: 300 })
   24. .width('100%')
   25. }
   26. .alignItems(VerticalAlign.Top)
   27. .margin({
   28. left: 16,
   29. right: 16,
   30. bottom: 12
   31. })
   32. .width('100%')
   ```

   [TextLink.ets](https://gitcode.com/HarmonyOS_Samples/CommonLinksSkip/blob/master/entry/src/main/ets/uiComponent/TextLink.ets#L26-L59)

   实现效果如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/XwIcsGVMR3Ctdz0VVlPM8Q/zh-cn_image_0000002319470057.png?HW-CC-KV=V1&HW-CC-Date=20260428T002008Z&HW-CC-Expire=86400&HW-CC-Sign=AE75C06AF7DBC3C298FDD5DF76FCD3F09C4DC49E988BBC5FE82B8F303B2D3A12 "点击放大")
3. 启用特殊文本识别。

   在Text组件上启用[enableDataDetector](../harmonyos-references/ts-basic-components-text.md#enabledatadetector11)属性，即可实现对一段文字中的链接、日期、电话号码、地址、邮箱等特殊文本进行自动识别并标记。

   ```
   1. Text(this.text)
   2. .enableDataDetector(this.enableDataDetector)
   ```

   [TextLink.ets](https://gitcode.com/HarmonyOS_Samples/CommonLinksSkip/blob/master/entry/src/main/ets/uiComponent/TextLink.ets#L32-L33)
4. 识别效果验证。

   分别传入包含标准HTTP/HTTPS链接、App Linking链接、日期、电话号码、地址、邮箱等文字内容到TextLink组件中，均以可交互形式显示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/u80X7QNgRRinfl7zoIhkrg/zh-cn_image_0000002284820702.png?HW-CC-KV=V1&HW-CC-Date=20260428T002008Z&HW-CC-Expire=86400&HW-CC-Sign=D1B65D1CB160C912A4BBEBB20AB4E9707655E407557421B34ECE2E634E19B69E "点击放大")

## 示例代码

* [基于enableDataDetector属性实现特殊文本识别的能力](https://gitcode.com/harmonyos_samples/CommonLinksSkip)
