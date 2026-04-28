---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-formmenu
title: FormMenu
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 系统预置UI组件库 > FormMenu
category: harmonyos-references
scraped_at: 2026-04-28T08:02:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b76057fb25693e9d57fceaa464a9cb072342fe7ac517ae5650bf81f6f311c243
---

本组件封装了一个“添加至桌面”菜单，用于实现应用内长按组件生成“添加至桌面”菜单，点击该菜单，触发卡片添加至桌面操作。通过桌面访问该应用快捷卡片，可以直接访问该组件功能。在应用使用过程中，该组件作为留存和复访入口，可吸引用户将功能快捷添加到桌面。

本组件支持应用内长按菜单快捷添加卡片到桌面：

1. 开发者将卡片数据以及应用内功能组件ID传给卡片框架。
2. 点击事件会根据组件ID获取应用内功能组件的快照和位置，用于添加到桌面时的过渡动效。
3. 卡片框架通过将加桌数据通知给桌面，触发卡片添加到桌面操作。

说明

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件不支持在Wearable设备上使用。

卡片具体开发指导请参考[卡片开发指南](../harmonyos-guides/formkit-overview.md)。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AddFormMenuItem } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)。

## AddFormMenuItem

PhonePC/2in1TabletTVWearable

```
1. AddFormMenuItem(
2. want: Want,
3. componentId: string,
4. options?: AddFormOptions
5. ): void
```

**装饰器类型：**@Builder

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md#want) | 是 | 待发布功能组件的want信息。 |
| componentId | string | 是 | 应用内功能组件ID，组件ID对应的界面与待添加的服务卡片界面相似。 |
| options | [AddFormOptions](ohos-arkui-advanced-formmenu.md#addformoptions) | 否 | 添加卡片选项。 |

## AddFormOptions

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| formBindingData | [formBindingData.FormBindingData](js-apis-app-form-formbindingdata.md#formbindingdata) | 否 | 是 | 卡片数据。 |
| callback | AsyncCallback<string> | 否 | 是 | 返回添加卡片是否成功的结果回调。返回为0表示卡片添加成功，非0表示卡片添加失败，失败时请参考[卡片错误码信息](errorcode-form.md)进行排查。 |
| style | [FormMenuItemStyle](ohos-arkui-advanced-formmenu.md#formmenuitemstyle) | 否 | 是 | 菜单自定义样式信息。 |

## FormMenuItemStyle

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| options | [MenuItemOptions](ts-basic-components-menuitem.md#menuitemoptions对象说明) | 否 | 是 | 包含设置MenuItem的各项信息。 |

说明

仅在 style配置为空或不配置时，使用默认的图标和menu文字。

## 事件

PhonePC/2in1TabletTVWearable

支持菜单点击事件。

## 示例

PhonePC/2in1TabletTVWearable

```
1. // index.ets
2. import { AddFormMenuItem } from '@kit.ArkUI';
3. import { formBindingData } from '@kit.FormKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const tag = 'AddFormMenuItem';

8. @Entry
9. @Component
10. struct Index {
11. @State message: string = 'Long press show menu';
12. private compId: string = 'addforms@d46313145';

14. @Builder
15. MyMenu() {
16. Menu() {
17. AddFormMenuItem(
18. {
19. bundleName: 'com.example.myapplication', // 包名
20. abilityName: 'EntryFormAbility', // 模块ability名称
21. parameters: {
22. 'ohos.extra.param.key.form_dimension': 2, // 卡片尺寸，1代表1*2卡片，2代表2*2卡片，3代表2*4卡片，4代表4*4卡片，7代表6*4卡片
23. 'ohos.extra.param.key.form_name': 'widget', // 卡片名称
24. 'ohos.extra.param.key.module_name': 'entry' // 卡片所属的模块名称
25. },
26. },
27. this.compId,
28. {
29. formBindingData: formBindingData.createFormBindingData({}),
30. // formBindingData: formBindingData.createFormBindingData({ data: 'share' }),
31. callback: (error, formId) => {
32. hilog.info(0x3900, tag, `callback info：formId = ${formId}`);
33. if (error?.code === 0) {
34. hilog.info(0x3900, tag, "添加至桌面成功")
35. } else {
36. hilog.error(0x3900, tag, `添加至桌面失败，请尝试其它添加方式, error code: ${error?.code}, error message: ${error?.message}`)
37. }
38. },
39. style: {
40. // options: {
41. //   startIcon: $r("app.media.icon"), // 菜单图标,可以自己提供。系统默认采用"sys.media.ic_public_add"
42. //   content: "添加到桌面",  // 菜单内容，可以自己提供。默认使用"sys.string.ohos_add_form_to_desktop"
43. //   endIcon: $r("app.media.icon") // 菜单图标，可以自己提供
44. // }
45. }
46. }
47. )
48. }
49. }

51. build() {
52. Row() {
53. Column() {
54. Image($r("app.media.startIcon"))   // 自定义图片
55. .id(this.compId)
56. .width(200)
57. .height(200)
58. .bindContextMenu(this.MyMenu, ResponseType.LongPress, {
59. placement: Placement.TopLeft
60. })
61. }
62. .width('100%')
63. }
64. .height('100%')
65. }
66. }
```

```
1. // WidgetCard.ets
2. const local = new LocalStorage()

4. @Entry(local)
5. @Component
6. struct WidgetCard {
7. @LocalStorageProp('data') data: string = 'defaultdata'; // 定义需要刷新的卡片数据
8. /*
9. * The action type.
10. */
11. readonly ACTION_TYPE: string = 'router';
12. /*
13. * The ability name.
14. */
15. readonly ABILITY_NAME: string = 'EntryAbility';
16. /*
17. * The message.
18. */
19. readonly MESSAGE: string = 'add detail';
20. /*
21. * The width percentage setting.
22. */
23. readonly FULL_WIDTH_PERCENT: string = '100%';
24. /*
25. * The height percentage setting.
26. */
27. readonly FULL_HEIGHT_PERCENT: string = '100%';

29. build() {
30. Row() {
31. Column() {
32. Text(this.data)
33. .fontSize($r('app.float.font_size'))
34. .fontWeight(FontWeight.Medium)
35. .fontColor($r('app.color.item_title_font'))
36. }
37. .width(this.FULL_WIDTH_PERCENT)
38. }
39. .height(this.FULL_HEIGHT_PERCENT)
40. .backgroundImage($r('app.media.startIcon'))
41. .backgroundImageSize({ width: '100%', height: '100%' })
42. .onClick(() => {
43. postCardAction(this, {
44. action: this.ACTION_TYPE,
45. abilityName: this.ABILITY_NAME,
46. params: {
47. message: this.MESSAGE
48. }
49. });
50. })
51. }
52. }
```

**高级自定义控件界面**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/LH3t72w0RYiSJeav-daNkA/zh-cn_image_0000002583440163.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000236Z&HW-CC-Expire=86400&HW-CC-Sign=B1154FC2B620B5576A6EC700527F1261CC411ECE32F3CF9AB04A792200A86D79)

**调用高级自定义控件桌面加桌结果**

左侧是formbindingdata为空加桌结果，右侧是formbindingdata为{ data: 'share' }的加桌结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/53Jm_jtETFifLomgQifGhg/zh-cn_image_0000002552960118.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000236Z&HW-CC-Expire=86400&HW-CC-Sign=77CD0A5C2643841F7D1BBAE68CA3C5771518C7FF59C58896488F11A31BAA4FA9)
