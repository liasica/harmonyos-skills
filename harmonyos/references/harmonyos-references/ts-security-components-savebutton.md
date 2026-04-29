---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-security-components-savebutton
title: SaveButton
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 安全 > SaveButton
category: harmonyos-references
scraped_at: 2026-04-29T13:52:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c3ecd4ebd2bbfd80e70b111f1e1cb423e15551e196cbba2a86ed7981e1f9ec9f
---

安全控件的保存控件。应用集成保存控件后，用户首次使用保存控件展示弹窗，在点击允许后自动授权，应用会在短时间内获取访问媒体库特权接口的授权。后续使用无需弹窗授权。在API version 19及之前的版本中，授权持续时间为10秒；在API version 20及之后的版本中，授权持续时间为1分钟。

说明

该组件从API version 10开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 接口

PhonePC/2in1TabletTVWearable

### SaveButton

PhonePC/2in1TabletTVWearable

SaveButton()

默认创建带有图标、文本、背景的保存控件。

为避免控件样式不合法导致授权失败，请开发者先了解安全控件样式的[约束与限制](../harmonyos-guides/security-component-overview.md#约束与限制)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### SaveButton

PhonePC/2in1TabletTVWearable

SaveButton(options: SaveButtonOptions)

创建包含指定元素的保存控件。

为避免控件样式不合法导致授权失败，请开发者先了解安全控件样式的[约束与限制](../harmonyos-guides/security-component-overview.md#约束与限制)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SaveButtonOptions](ts-security-components-savebutton.md#savebuttonoptions) | 是 | 创建包含指定元素的保存控件。 |

## SaveButtonOptions

PhonePC/2in1TabletTVWearable

用于指定保存控件的图标、文本等指定元素。

说明

* icon或text需至少传入一个。
* 如果icon、text都不传入，SaveButton中的options参数不生效，创建的SaveButton为默认样式，默认样式：

  SaveIconStyle默认样式为FULL\_FILLED；

  SaveDescription默认样式为DOWNLOAD；

  ButtonType默认样式为Capsule。
* icon、text、buttonType不支持动态修改。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [SaveIconStyle](ts-security-components-savebutton.md#saveiconstyle枚举说明) | 否 | 是 | 设置保存控件的图标风格。  不传入该参数表示没有图标。 |
| text | [SaveDescription](ts-security-components-savebutton.md#savedescription枚举说明) | 否 | 是 | 设置保存控件的文本描述。  不传入该参数表示没有文字描述。 |
| buttonType | [ButtonType](ts-securitycomponent-attributes.md#buttontype枚举说明) | 否 | 是 | 设置保存控件的背景样式。  不传入该参数，系统默认提供Capsule类型按钮。 |

## SaveIconStyle枚举说明

PhonePC/2in1TabletTVWearable

保存控件的图标风格。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FULL\_FILLED | 0 | 保存控件展示填充样式图标。 |
| LINES | 1 | 保存控件展示线条样式图标。 |

## SaveDescription枚举说明

PhonePC/2in1TabletTVWearable

保存控件的文本描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOWNLOAD | 0 | 保存控件的文字描述为“下载”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| DOWNLOAD\_FILE | 1 | 保存控件的文字描述为“下载文件”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| SAVE | 2 | 保存控件的文字描述为“保存”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| SAVE\_IMAGE | 3 | 保存控件的文字描述为“保存图片”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| SAVE\_FILE | 4 | 保存控件的文字描述为“保存文件”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| DOWNLOAD\_AND\_SHARE | 5 | 保存控件的文字描述为“下载分享”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| RECEIVE | 6 | 保存控件的文字描述为“接收”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| CONTINUE\_TO\_RECEIVE | 7 | 保存控件的文字描述为“继续接收”。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| SAVE\_TO\_GALLERY12+ | 8 | 保存控件的文字描述为“保存至图库”。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| EXPORT\_TO\_GALLERY12+ | 9 | 保存控件的文字描述为“导出”。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| QUICK\_SAVE\_TO\_GALLERY12+ | 10 | 保存控件的文字描述为“快速保存图片”。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| RESAVE\_TO\_GALLERY12+ | 11 | 保存控件的文字描述为“重新保存”。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SAVE\_ALL18+ | 12 | 保存控件的文字描述为“全部保存”。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## SaveButtonOnClickResult枚举说明

PhonePC/2in1TabletTVWearable

保存控件点击后的授权结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 保存控件点击后权限授权成功。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| TEMPORARY\_AUTHORIZATION\_FAILED | 1 | 保存控件点击后权限授权失败。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| CANCELED\_BY\_USER21+ | 2 | 保存控件点击后弹窗用户取消授权。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |

## SaveButtonCallback18+

PhonePC/2in1TabletTVWearable

type SaveButtonCallback = (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError<void>) => void

点击保存控件触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [ClickEvent](ts-universal-events-click.md#clickevent) | 是 | 见ClickEvent对象说明。 |
| result | [SaveButtonOnClickResult](ts-security-components-savebutton.md#savebuttononclickresult枚举说明) | 是 | 授权的结果。 |
| error | [BusinessError<void>](js-apis-base.md#businesserror) | 否 | 点击按钮时的错误码和错误信息。  错误码0表示点击保存控件授权成功或用户取消授权。  错误码1表示系统内部错误，包括但不限于：  1. ipc通信失败。  2. 安全控件弹窗失败。  错误码2表示属性设置错误，包括但不限于：  1. 字体或图标设置过小。  2. 字体或图标与背托颜色相近。  3. 字体或图标颜色过于透明。  4. padding为负值。  5. 按钮被其他组件或窗口遮挡。  6. 文本超出背托范围。  7. 按钮超出窗口或屏幕。  8. 按钮整体尺寸过大。  9. 按钮文本被截断，显示不全。  10. 相关属性设置影响安全控件显示。 |

## SaveButtonAttribute

PhonePC/2in1TabletTVWearable

SaveButtonAttribute提供自定义图标（setIcon）、自定义文本（setText）、图标尺寸（iconSize）、图标圆角（iconBorderRadius），以及按压态效果（stateEffect）等属性设置的方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

### setIcon20+

PhonePC/2in1TabletTVWearable

setIcon(icon: Resource)

设置保存控件的图标。

**需要权限**：ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| icon | [Resource](ts-types.md#resource) | 是 | 自定义图标资源信息，仅支持Resource类型的数据源。  可支持的图片格式：png、jpg、jpeg、bmp、svg、webp、gif和heif等，支持的图片格式范围见[Image](ts-basic-components-image.md)。当资源为非图片资源或不支持的格式时，图标显示为空白。  如果应用无ohos.permission.CUSTOMIZE\_SAVE\_BUTTON权限，则自定义图标设置不生效，保存控件保持默认样式。详见[SaveButtonOptions](ts-security-components-savebutton.md#savebuttonoptions)说明。 |

### setText20+

PhonePC/2in1TabletTVWearable

setText(text: string | Resource)

设置保存控件的文本。

**需要权限**：ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | [Resource](ts-types.md#resource) | 是 | 自定义文本信息。  如果应用无ohos.permission.CUSTOMIZE\_SAVE\_BUTTON权限，则自定义文本设置不生效，保存控件保持默认样式。详见[SaveButtonOptions](ts-security-components-savebutton.md#savebuttonoptions)说明。 |

### iconSize20+

PhonePC/2in1TabletTVWearable

iconSize(size: Dimension | SizeOptions)

设置保存控件的图标尺寸。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Dimension](ts-types.md#dimension10) | [SizeOptions](ts-types.md#sizeoptions) | 是 | 图标尺寸。宽高默认值均为16vp。  不支持设置百分比字符串。若设置Dimension类型入参的百分比字符串，则图标尺寸显示为默认值；若设置SizeOptions类型入参的width或height属性为百分比字符串，则图标尺寸显示为0。  对于保存控件提供的系统图标：  - 使用Dimension类型入参时，宽、高相等，均为设定值。  - 使用SizeOptions类型入参时，若宽、高设定值不一致，则宽、高相等取两者较小值；若仅设定其中一个值，则取该值作为宽、高值。  对于自定义图标：  - 使用Dimension类型入参时，宽、高相等，均为设定值。  - 使用SizeOptions类型入参时，建议同时设定宽和高，此时按照指定宽、高生效；若仅设定其中一个值，则宽高均显示为该设定值。  - 当设定的宽高与自定义图标的宽高比例不一致时，图片按[ImageFit.Cover](ts-appendix-enums.md#imagefit)的方式填充显示区域。 |

### iconBorderRadius20+

PhonePC/2in1TabletTVWearable

iconBorderRadius(radius: Dimension | BorderRadiuses)

设置保存控件图标的边框圆角半径。

**需要权限**：ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | 是 | 保存控件图标的圆角半径，支持设置四个圆角。四个圆角默认值均为0vp。  如果应用无ohos.permission.CUSTOMIZE\_SAVE\_BUTTON权限，则图标的圆角半径设置不生效。 |

### stateEffect20+

PhonePC/2in1TabletTVWearable

stateEffect(enabled: boolean)

设置保存控件的按压效果。

**需要权限**：ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 表示是否开启按压效果，true表示保存控件按压时显示按压效果，false表示保存控件按压时不显示按压效果。  默认值：true。  如果应用无ohos.permission.CUSTOMIZE\_SAVE\_BUTTON权限，按压效果设置不生效。 |

### userCancelEvent21+

PhonePC/2in1TabletTVWearable

userCancelEvent(enabled: boolean)

设置接收保存控件的用户取消授权事件。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 表示是否接收保存控件的用户取消授权事件，true表示接收保存控件的用户取消授权事件，false表示不接收保存控件的用户取消授权事件。  默认值：false。 |

## 属性

PhonePC/2in1TabletTVWearable

不支持通用属性，仅继承[安全控件通用属性](ts-securitycomponent-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

不支持通用事件，仅支持以下事件：

### onClick

PhonePC/2in1TabletTVWearable

onClick(event: SaveButtonCallback)

点击动作触发该回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [SaveButtonCallback](ts-security-components-savebutton.md#savebuttoncallback18) | 是 | 见SaveButtonCallback。  在API10-17时，参数类型为：(event: [ClickEvent](ts-universal-events-click.md#clickevent), result: [SaveButtonOnClickResult](ts-security-components-savebutton.md#savebuttononclickresult枚举说明)) => void。  从API18开始，变更为SaveButtonCallback。 |

## 示例1

PhonePC/2in1TabletTVWearable

```
1. // xxx.ets
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';
3. import { fileIo } from '@kit.CoreFileKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Index {
9. handleSaveButtonClick: SaveButtonCallback =
10. async (event: ClickEvent, result: SaveButtonOnClickResult, error?: BusinessError) => {
11. if (result === SaveButtonOnClickResult.SUCCESS) {
12. try {
13. const context = this.getUIContext().getHostContext();
14. let helper = photoAccessHelper.getPhotoAccessHelper(context);
15. let uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
16. // 使用uri打开文件，可以持续写入内容，写入过程不受时间限制。
17. let file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
18. // 写入文件
19. await fileIo.write(file.fd, "context");
20. // 关闭文件
21. await fileIo.close(file.fd);
22. } catch (error) {
23. console.error(`errCode: ${error.code}, errMessage: ${error.message}`);
24. }
25. } else if (result === SaveButtonOnClickResult.CANCELED_BY_USER) {
26. console.info("errCode: " + error?.code);
27. console.info("errMessage: " + error?.message);
28. } else {
29. console.error("errCode: " + error?.code);
30. console.error("errMessage: " + error?.message);
31. }
32. };

34. build() {
35. Row() {
36. Column({ space: 10 }) {
37. // 默认参数下，图标、文字、背景都存在。
38. SaveButton().onClick((this.handleSaveButtonClick))
39. // 传入参数即表示元素存在，不传入的参数表示元素不存在，如果不传入buttonType，会默认添加ButtonType.Capsule配置，显示图标+背景。
40. SaveButton({ icon: SaveIconStyle.FULL_FILLED })
41. // 只显示图标+背景，如果设置背景色高八位的α值低于0x1a，则会被系统强制调整为0xff。
42. SaveButton({ icon: SaveIconStyle.FULL_FILLED, buttonType: ButtonType.Capsule })
43. .backgroundColor(0x10007dff)
44. // 图标、文字、背景都存在，如果设置背景色高八位的α值低于0x1a，则会被系统强制调整为0xff。
45. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Capsule })
46. // 图标、文字、背景都存在，如果设置宽度小于当前属性组合下允许的最小宽度时，宽度仍为设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。
47. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Capsule })
48. .fontSize(16)
49. .width(30)
50. // 图标、文字、背景都存在，如果设置宽度小于当前属性组合下允许的最小宽度时，宽度仍为设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。
51. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Capsule })
52. .fontSize(16)
53. .size({ width: 30, height: 30 })
54. // 图标、文字、背景都存在，如果设置宽度小于当前属性组合下允许的最小宽度时，宽度仍为设置值，此时按钮文本信息会自动换行，以保证安全控件显示的完整性。
55. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD, buttonType: ButtonType.Capsule })
56. .fontSize(16)
57. .constraintSize({
58. minWidth: 0,
59. maxWidth: 30,
60. minHeight: 0,
61. maxHeight: 30
62. })
63. // 设置保存控件接收用户取消授权事件。
64. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
65. .onClick((this.handleSaveButtonClick))
66. .userCancelEvent(true)
67. }.width('100%')
68. }.height('100%')
69. }
70. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/dcXvQvX5QpKp6hdTM7nUOA/zh-cn_image_0000002558766602.png?HW-CC-KV=V1&HW-CC-Date=20260429T055250Z&HW-CC-Expire=86400&HW-CC-Sign=9BFC6D41D1ADE340B9DE2225EC2F816FDE3F21BCCE4EB0958BE48D2553C60B70)

## 示例2

PhonePC/2in1TabletTVWearable

应用需要申请权限：ohos.permission.CUSTOMIZE\_SAVE\_BUTTON

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SetIcon {
5. build() {
6. Row() {
7. Column({ space: 10 }) {
8. // 设置图标为resource类型，有权限时显示设置的图标。
9. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
10. .setIcon($r('app.media.startIcon'))
11. // 设置文本为string类型，有权限时显示设置的文本。
12. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
13. .setText("保存控件设置文本")
14. // 设置文本为resource类型，有权限时显示设置的资源文本。
15. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
16. .setText($r('app.string.app_name'))
17. // 设置保存控件图标大小，入参为Dimension类型。
18. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
19. .iconSize(28)
20. // 设置保存控件的默认图标大小，入参为SizeOptions类型。将默认图标设置为宽高中的较小值。
21. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
22. .iconSize({ width: 20, height: 40 })
23. // 设置保存控件的自定义图标大小，入参为SizeOptions类型。图片按设置的宽高显示。
24. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
25. .setIcon($r('app.media.startIcon'))
26. .iconSize({ width: 30, height: 40 })
27. // 设置保存控件的自定义图标大小，入参为SizeOptions类型且只设置一个值。图片宽高均显示为设置值。
28. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
29. .setIcon($r('app.media.startIcon'))
30. .iconSize({ width: 40 })
31. // 设置保存控件的图标圆角，入参为Dimension类型。图片四个圆角的半径均为入参大小。
32. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
33. .backgroundColor(Color.Orange)
34. .setIcon($r('app.media.background'))
35. .iconSize(30)
36. .iconBorderRadius(6)
37. // 设置正方形图标圆角大于边长一半时图标显示为圆形。
38. SaveButton({ icon: SaveIconStyle.FULL_FILLED, buttonType: ButtonType.Circle })
39. .backgroundColor(Color.Orange)
40. .setIcon($r('app.media.foreground'))
41. .iconSize(30)
42. .iconBorderRadius(30)
43. .padding(0)
44. // 自定义图标通过iconBorderRadius设置为圆形，背托设置为透明色并设置边框。
45. SaveButton({ icon: SaveIconStyle.FULL_FILLED, buttonType:ButtonType.Circle })
46. .setIcon($r('app.media.background'))
47. .backgroundColor(Color.Transparent)
48. .iconSize(40)
49. .iconBorderRadius(30)
50. .borderWidth(1)
51. .borderColor(Color.Black)
52. .borderStyle(BorderStyle.Solid)
53. .padding(10)
54. // 设置保存控件的图标圆角，入参为BorderRadiuses类型。图片四个圆角的半径分别为对应入参大小，未设置的无圆角。
55. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
56. .backgroundColor(Color.Orange)
57. .setIcon($r('app.media.background'))
58. .iconSize(30)
59. .iconBorderRadius({ topLeft: 10, topRight: 16, bottomRight: 20 })
60. // 设置保存控件的按压特效为无按压特效。
61. SaveButton({ icon: SaveIconStyle.FULL_FILLED, text: SaveDescription.DOWNLOAD })
62. .stateEffect(false)
63. }.width('100%')
64. }.height('100%')
65. }
66. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/mYqA1e0cS_2yo5_iGfoIDg/zh-cn_image_0000002558606942.png?HW-CC-KV=V1&HW-CC-Date=20260429T055250Z&HW-CC-Expire=86400&HW-CC-Sign=4ADD296591FBAE88A1D56D57A43992E69D0B982C7F87B2CAE307EB9C215C504D)
