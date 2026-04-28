---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-avcastpicker
title: @ohos.multimedia.avCastPicker (投播组件)
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS组件 > @ohos.multimedia.avCastPicker (投播组件)
category: harmonyos-references
scraped_at: 2026-04-28T08:12:22+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:8d2bc730114af2a7bee5fad34505540cccabcb1ef930d2c2b738369f0f862854
---

本模块提供创建投播组件AVCastPicker的功能，提供设备发现连接的统一入口。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 示例效果请以真机为准，当前DevEco Studio预览器无实际投播功能。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { AVCastPicker } from '@kit.AVSessionKit';
```

## 属性

PhonePC/2in1TabletTV

支持[通用属性](ts-component-general-attributes.md)。

## AVCastPicker

PhonePC/2in1TabletTV

```
1. AVCastPicker({
2. normalColor?: Color | number | string;
3. activeColor?: Color | number | string;
4. pickerStyle?: AVCastPickerStyle;
5. colorMode?: AVCastPickerColorMode;
6. sessionType?: string;
7. customPicker?: CustomBuilder;
8. onStateChange?: (state: AVCastPickerState) => void;
9. })
```

投播组件，可用于将音视频资源投放到其它设备播放。

该组件为自定义组件，开发者在使用前需要先了解[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)。

**装饰器类型：** [@Component](../harmonyos-guides/arkts-create-custom-components.md)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 类型 | 必填 | 装饰器类型 | 说明 |
| --- | --- | --- | --- | --- |
| normalColor11+ | Color | number | string | 否 | @Prop | 指正常状态下投播组件的颜色。  未设置将采用colorMode下的颜色设置。 |
| activeColor11+ | Color | number | string | 否 | @Prop | 指设备切换成功状态下投播组件的颜色。未设置系统将优先根据normalColor的颜色匹配；如果normalColor也未设置，将采用colorMode下的颜色设置。 |
| pickerStyle12+ | [AVCastPickerStyle](js-apis-avcastpickerparam.md#avcastpickerstyle12) | 否 | @Prop | 投播样式。  - 当sessionType是audio或者video时，默认值为STYLE\_PANEL。  - 当sessionType是voice\_call或者video\_call时，默认值为STYLE\_MENU，且不可修改为STYLE\_PANEL。 |
| colorMode12+ | [AVCastPickerColorMode](js-apis-avcastpickerparam.md#avcastpickercolormode12) | 否 | @Prop | 显示模式。默认值为AUTO。  - 当colorMode设置为AUTO时，跟随系统的深浅色模式的默认色值。  - 当colorMode设置为DARK、LIGHT时，使用对应模式的系统预设色值。 |
| sessionType12+ | string | 否 | @Prop | 会话类型，可参考[AVSessionType](arkts-apis-avsession-t.md#avsessiontype10)。默认值为当前应用创建的AVSessionType。 |
| customPicker12+ | [CustomBuilder](ts-types.md#custombuilder8) | 否 | @Prop | 自定义样式。建议应用自定义组件样式，可有效提升组件显示速度。 |
| onStateChange11+ | (state: [AVCastPickerState](js-apis-avcastpickerparam.md#avcastpickerstate)) => void | 否 | - | 投播状态更改回调。 |

## 事件

PhonePC/2in1TabletTV

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTV

投播功能的示例说明参考如下。

体验完整功能请具体参考[播放类开发指南](../harmonyos-guides/distributed-playback-guide.md)和[通话类开发指南](../harmonyos-guides/using-switch-call-devices.md)。

```
1. import { AVCastPickerState, AVCastPicker } from '@kit.AVSessionKit';

3. @Entry
4. @Component
5. struct Index {

7. @State pickerImage: ResourceStr = $r('app.media.castPicker'); // 自定义资源。

9. private onStateChange(state: AVCastPickerState) {
10. if (state == AVCastPickerState.STATE_APPEARING) {
11. console.info('The picker starts showing.');
12. } else if (state == AVCastPickerState.STATE_DISAPPEARING) {
13. console.info('The picker finishes presenting.');
14. }
15. }

17. @Builder
18. customPickerBuilder() {
19. Image(this.pickerImage)
20. .width('100%')
21. .height('100%')
22. .fillColor(Color.Black)
23. }

25. build() {
26. Row() {
27. Column() {
28. AVCastPicker({
29. normalColor: Color.Red,
30. customPicker: () => this.customPickerBuilder(),
31. onStateChange: this.onStateChange
32. })
33. .width('40vp')
34. .height('40vp')
35. .border({ width: 1, color: Color.Red })
36. }.height('50%')
37. }.width('50%')
38. }
39. }
```
