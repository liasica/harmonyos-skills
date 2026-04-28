---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-udmfcomponents
title: @ohos.data.UdmfComponents (内容卡片)
breadcrumb: API参考 > 应用框架 > ArkData（方舟数据管理） > ArkTS 组件 > @ohos.data.UdmfComponents (内容卡片)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:24+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:1522aa725a979c8b9801d52b3a7dcf45403b92ae2a7ec98ce5d0b561b9983c91
---

针对[ContentForm](js-apis-data-uniformdatastruct.md#contentform14)标准数据结构的内容卡片，支持设置标题（必选）、描述、应用图标、应用名称、跳转链接、内容图片。用户点击卡片时，执行传入的回调事件函数，若设置的跳转链接不为空，则跳转到指定的页面。

说明

该组件从API version 20开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { ContentFormCard, FormType } from '@kit.ArkData';
```

## 子组件

PhonePC/2in1TabletTV

无

## ContentFormCard

PhonePC/2in1TabletTV

ContentFormCard({contentFormData: uniformDataStruct.ContentForm, formType: FormType, formWidth?: number, formHeight?: number, handleOnClick?: Function})

内容卡片控件，用于在应用内展示标题、描述、内容图片、应用信息等。

**装饰器类型：**@Component

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| contentFormData | [uniformDataStruct.ContentForm](js-apis-data-uniformdatastruct.md#contentform14) | 是 | - | 内容卡片数据。 |
| formType | [FormType](js-apis-data-udmfcomponents.md#formtype) | 是 | @Prop | 内容卡片类型，影响内容卡片的大小。 |
| formWidth | number | 否 | @Prop | 卡片宽度，其范围在设置的内容卡片类型默认宽度的0.8 ~ 1.2倍之间，当formType为TYPE\_SMALL时，其范围在设置的内容卡片类型默认宽度的0.4 ~ 1.2倍之间。单位为vp。 |
| formHeight | number | 否 | @Prop | 卡片高度，当contentFormData中的title为空字符串时，卡片高度为传入的值，否则其范围在设置的内容卡片类型默认宽度的0.8 ~ 1.2倍之间，当formType为TYPE\_SMALL时，其范围在设置的内容卡片类型默认宽度的0.4 ~ 1.2倍之间。单位为vp。 |
| handleOnClick | Function | 否 | - | 点击事件回调函数。 |

## FormType

PhonePC/2in1TabletTV

内容卡片类型枚举，提供了大、中、小三种尺寸。

**系统能力：** SystemCapability.DistributedDataManager.UDMF.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TYPE\_BIG | 0 | 表示 4 x 4 的尺寸。默认卡片宽度为200，默认高度为200。 |
| TYPE\_MID | 1 | 表示 4 x 2 的尺寸。默认卡片宽度为200，默认高度为100。 |
| TYPE\_SMALL | 2 | 表示 2 x 1 的尺寸。默认卡片宽度为137， 默认高度为83。 |

## 示例

PhonePC/2in1TabletTV

```
1. import { uniformDataStruct } from '@kit.ArkData'

3. @Entry
4. @Component
5. struct Index {
6. @State contentForm: uniformDataStruct.ContentForm = {
7. uniformDataType: 'general.content-form',
8. title: ''
9. };
10. @State startToShow: boolean = false;

12. aboutToAppear(): void {
13. this.initData();
14. }

16. async initData() {
17. let context = this.getUIContext().getHostContext();
18. if (!context) {
19. return;
20. }
21. try {
22. let appIcon = await context.resourceManager.getMediaContent($r('app.media.startIcon').id);
23. let thumbImage = await context.resourceManager.getMediaContent($r('app.media.foreground').id);
24. this.contentForm = {
25. uniformDataType: 'general.content-form',
26. title: "Content form title",
27. thumbData: appIcon,
28. description: "Content form description",
29. appIcon: thumbImage,
30. appName: "com.test.demo"
31. };
32. } catch (err) {
33. console.error("Init data error");
34. }
35. }

37. build() {
38. Column() {
39. Button('show card')
40. .onClick(() => {
41. this.startToShow = true;
42. })
43. if (this.startToShow) {
44. ContentFormCard({
45. contentFormData: this.contentForm,
46. formType: FormType.TYPE_SMALL,
47. formWidth: 110,
48. formHeight: 50,
49. handleOnClick: () => {
50. console.info("Clicked card");
51. }
52. })
53. }
54. }
55. }
56. }
```
