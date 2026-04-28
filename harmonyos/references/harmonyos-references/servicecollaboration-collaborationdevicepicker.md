---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-collaborationdevicepicker
title: CollaborationDevicePicker (流转控件)
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > ArkTS 组件 > CollaborationDevicePicker (流转控件)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4329b48a01532a45f16e3a86fe8bbe050c7e513bbdbc1a01a7ebbd5e105f4959
---

该模块提供流转入口组件，点击流转入口组件后，会拉起设备选择面板。

与devicePicker.[createDevicePickerController](servicecollaboration-devicepicker.md#createdevicepickercontroller)配合使用，通过创建的controller可以与设备选择面板进行交互。

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { CollaborationDevicePicker } from '@kit.ServiceCollaborationKit'
```

## CollaborationDevicePicker

PhonePC/2in1TabletTV

**装饰器类型：** @Component

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| controller | devicePicker.[DevicePickerController](servicecollaboration-devicepicker.md#devicepickercontroller) | 否 | 否 | 设备选择控制器，通过该控制器与设备选择界面进行交互。 |
| attribute | devicePicker.[DevicePickerAttribute](servicecollaboration-devicepicker.md#devicepickerattribute) | 否 | 否 | 设备选择属性，指定设备选择界面的应用描述信息，如果不指定，默认使用调用者所属ability配置文件中的信息。 |

### build

PhonePC/2in1TabletTV

build(): void

struct的默认构造函数，开发者无法直接调用此方法。

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

**示例：**

```
1. import { devicePicker, CollaborationDevicePicker } from '@kit.ServiceCollaborationKit'

3. @Entry
4. @Component
5. struct Index {
6. controller: devicePicker.DevicePickerController = devicePicker.createDevicePickerController()

8. build() {
9. Column() {
10. // 流转控件，应用流转的入口
11. CollaborationDevicePicker({
12. controller: this.controller, attribute: {
13. abilityName: '流转测试',
14. abilityDesc: '这是一个流转测试的控件',
15. abilityIcon: $r('sys.media.ohos_app_icon'),
16. businessDesc: '流转到'
17. }
18. })
19. }.width('100%').alignItems(HorizontalAlign.Center)
20. }
21. }
```

| **图1** 设备选择界面的应用描述信息效果图 | **图2** 点击流转入口组件后，拉起设备选择面板效果图 | **图3** 设备流转成功后效果图 | **图4** 流转失败效果图 |
| --- | --- | --- | --- |
| 设备选择界面最上方为应用描述部分，包括应用图标、应用名称、应用描述信息 | 页面右上角为流转图标，点击后会从设备底部弹出设备选择面板 | 流转图标和设备信息会变蓝色 | 流转失败效果图 |
