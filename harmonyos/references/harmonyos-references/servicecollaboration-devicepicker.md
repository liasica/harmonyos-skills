---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-devicepicker
title: devicePicker (设备选择控制器)
breadcrumb: API参考 > 系统 > 网络 > Service Collaboration Kit（协同服务） > ArkTS 组件 > devicePicker (设备选择控制器)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d4cd01a21e9c12b78e33dbdbd75ad9bfb0792f9454c42dd98355bef0a359c686
---

该模块提供设备选择控制器和设备选择面板的能力。设备选择面板没有对外提供直接显示的接口，需要结合[CollaborationDevicePicker (流转控件)](servicecollaboration-collaborationdevicepicker.md)组件一起使用，点击[CollaborationDevicePicker (流转控件)](servicecollaboration-collaborationdevicepicker.md)组件后该面板会自动显示。通过设备选择控制器可以和设备选择面板进行交互，设备选择面板中包括：应用的描述信息和发现的已组网设备列表（当前设备列表中只支持显示已组网的可信设备）。

用户点击设备后，会触发设备选择控制器对应的接口回调，并返回已选择的设备信息；应用可以通过获取到的设备信息处理分布式业务，比如通过startAbility启动远端UIAbility；待启动远端ability成功后，可以通过[updateState](servicecollaboration-devicepicker.md#updatestate)接口更新业务状态，界面上将会显示指定的状态。

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1TabletTV

```
1. import { devicePicker } from '@kit.ServiceCollaborationKit'
```

## DeviceEvent

PhonePC/2in1TabletTV

type DeviceEvent = 'deviceSelected' | 'deviceUnselected' | 'selectedDeviceOffline'

设备事件类型，支持设备选择事件、设备取消事件、已选择设备的下线事件。

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

| 类型 | 说明 |
| --- | --- |
| 'deviceSelected' | 设备选择事件。  当设备处于空闲状态时，点击设备会触发该事件。 |
| 'deviceUnselected' | 设备取消选择事件。  当设备处于成功状态时，点击该设备会触发该事件；在设备A处于成功状态时，点击设备B也会触发设备A的deviceUnselected事件。 |
| 'selectedDeviceOffline' | 已选择设备的下线事件。  当已经处于成功状态的设备下线后，会触发该事件。 |

## createDevicePickerController

PhonePC/2in1TabletTV

createDevicePickerController(): DevicePickerController

创建设备选择控制器，通过该控制器提供的接口可以与设备选择面板进行交互。

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DevicePickerController](servicecollaboration-devicepicker.md#devicepickercontroller) | 返回设备选择控制器实例，可以与流转控件[CollaborationDevicePicker (流转控件)](servicecollaboration-collaborationdevicepicker.md)配合使用。 |

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

## DevicePickerController

PhonePC/2in1TabletTV

DevicePickerController类提供了与设备选择面板交互的接口。

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

### on('deviceSelected' | 'deviceUnselected' | 'selectedDeviceOffline')

PhonePC/2in1TabletTV

on(event: DeviceEvent, callback: Callback<distributedDeviceManager.DeviceBasicInfo>): void

注册设备相关的事件回调，目前支持：设备选择、设备取消选择、已选择设备的下线事件。

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [DeviceEvent](servicecollaboration-devicepicker.md#deviceevent) | 是 | 设备相关的事件，目前支持：设备选择、设备取消选择、已选择设备的下线事件。 |
| callback | Callback<[distributedDeviceManager.DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)> | 是 | 返回发生对应事件的设备信息，可以在callback中使用返回的设备信息进行跨设备应用ability组件启动。 |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit'
2. import { CollaborationDevicePicker, devicePicker } from '@kit.ServiceCollaborationKit'
3. import { distributedDeviceManager } from '@kit.DistributedServiceKit'
4. import { hilog } from '@kit.PerformanceAnalysisKit'

6. @Entry
7. @Component
8. struct CustomControls {
9. // 创建设备选择控制器
10. controller: devicePicker.DevicePickerController = devicePicker.createDevicePickerController()
11. // 获取所属ability的context
12. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext
13. abilityId: number = 0

15. aboutToAppear() {
16. // 注册设备选择事件
17. this.controller.on('deviceSelected', (device: distributedDeviceManager.DeviceBasicInfo) => {
18. let want: Want = {
19. // 通过device获取设备的id
20. deviceId: device.networkId,
21. // 此处bundleName和abilityName是示例，实际使用必须传递远端设备真实存在的bundleName和abilityName才能拉起指定服务
22. bundleName: 'com.example.myapplication',
23. abilityName: 'ExtensionAbility'
24. }
25. this.getUIContext().getPromptAction().showToast({ message: 'device selected' })
26. this.context.startAbility(want).then(() => {
27. hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in starting Ability')
28. // 更新设备状态
29. this.controller.updateState(device.networkId, devicePicker.BusinessState.SUCCESSFUL)
30. }).catch(() => {
31. hilog.error(0x0000, 'testTag', '%{public}s', 'Failed to startAbility')
32. // 更新设备状态，同时添加失败的原因，这个原因会展示在设备下方
33. this.controller.updateState(device.networkId, devicePicker.BusinessState.FAILED, 'the remote device is busy')
34. })
35. })

37. // 注册设备取消选择事件
38. this.controller.on('deviceUnselected', (device: distributedDeviceManager.DeviceBasicInfo) => {
39. this.getUIContext().getPromptAction().showToast({ message: 'device unselected' })
40. })
41. }

43. build() {
44. Column() {
45. CollaborationDevicePicker({
46. controller: this.controller, attribute: {
47. abilityName: '流转测试',
48. abilityDesc: '这是一个流转测试的控件',
49. abilityIcon: $r('sys.media.ohos_app_icon'),
50. businessDesc: '流转到'
51. }
52. })
53. }.width('100%').alignItems(HorizontalAlign.Center);
54. }
55. }
```

| **图1** 设备空闲状态效果图 | **图2** 设备成功状态效果图 |
| --- | --- |
| 下图中my phone处于空闲状态，点击该设备后会触发deviceSelected事件 | 下图中my phone处于成功状态，点击该设备后会触发deviceUnselected事件 |

### off('deviceSelected' | 'deviceUnselected' | 'selectedDeviceOffline')

PhonePC/2in1TabletTV

off(event: DeviceEvent, callback?: Callback<distributedDeviceManager.DeviceBasicInfo>): void

取消注册设备相关的事件回调，目前支持的事件：设备选择、设备取消选择、已选择设备的下线事件。

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [DeviceEvent](servicecollaboration-devicepicker.md#deviceevent) | 是 | 设备相关的事件，目前支持：设备选择、设备取消选择、已选择设备的下线事件。 |
| callback | Callback<[distributedDeviceManager.DeviceBasicInfo](js-apis-distributeddevicemanager.md#devicebasicinfo)> | 否 | 返回发生指定事件的设备信息，与[on('deviceSelected' | 'deviceUnselected' | 'selectedDeviceOffline')](servicecollaboration-devicepicker.md#ondeviceselected--deviceunselected--selecteddeviceoffline)接口对应，可以在不需要监听设备事件的位置进行取消。比如在组件生命周期的aboutToAppear()调用了on注册接口，则可以在页面aboutToDisappear()调用off取消注册。 |

**示例：**

```
1. import { common } from '@kit.AbilityKit'
2. import { distributedDeviceManager } from '@kit.DistributedServiceKit'
3. import { CollaborationDevicePicker, devicePicker } from '@kit.ServiceCollaborationKit'

5. @Entry
6. @Component
7. struct CustomControls {
8. // 创建设备选择控制器
9. controller: devicePicker.DevicePickerController = devicePicker.createDevicePickerController()
10. // 获取所属ability的context
11. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext

13. aboutToDisappear() {
14. // 取消注册设备选择事件
15. this.controller.off('deviceSelected', (device: distributedDeviceManager.DeviceBasicInfo) => {
16. this.getUIContext().getPromptAction().showToast({ message: 'off device selected' })
17. })

19. // 取消注册设备取消选择事件
20. this.controller.off('deviceUnselected', (device: distributedDeviceManager.DeviceBasicInfo) => {
21. this.getUIContext().getPromptAction().showToast({ message: 'device unselected' })
22. })
23. }

25. build() {
26. Column() {
27. CollaborationDevicePicker({
28. controller: this.controller, attribute: {
29. abilityName: '流转测试',
30. abilityDesc: '这是一个流转测试的控件',
31. abilityIcon: $r('sys.media.ohos_app_icon'),
32. businessDesc: '流转到'
33. }
34. })
35. }.width('100%').alignItems(HorizontalAlign.Center)
36. }
37. }
```

### updateState

PhonePC/2in1TabletTV

updateState(networkId: string, state: BusinessState, desc?: ResourceStr): void

更新设备的业务状态，在设备选择面板上会显示更新后的状态。业务失败情况下，可以传入失败的描述信息，会随着状态一起显示。

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| networkId | string | 是 | 设备的networkId信息。 |
| state | [BusinessState](servicecollaboration-devicepicker.md#businessstate) | 是 | 业务状态，当前支持IDLE、SUCCESSFUL、FAILED三种状态类型。 |
| desc | [ResourceStr](ts-types.md#resourcestr) | 否 | 导致业务失败的具体描述信息。在业务失败情况下，可以传入该参数，会将该信息显示在指定设备名字下方。长度限制1-128。 |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit'
2. import { CollaborationDevicePicker, devicePicker } from '@kit.ServiceCollaborationKit'
3. import { distributedDeviceManager } from '@kit.DistributedServiceKit'
4. import { hilog } from '@kit.PerformanceAnalysisKit'

6. @Entry
7. @Component
8. struct CustomControls {
9. // 创建设备选择控制器
10. controller: devicePicker.DevicePickerController = devicePicker.createDevicePickerController()
11. // 获取所属ability的context
12. context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext
13. abilityId: number = 0

15. aboutToAppear() {
16. // 注册设备选择事件
17. this.controller.on('deviceSelected', (device: distributedDeviceManager.DeviceBasicInfo) => {
18. let want: Want = {
19. // 通过device获取设备的id
20. deviceId: device.networkId,
21. // 此处bundleName和abilityName是示例，实际使用必须传递远端设备真实存在的bundleName和abilityName才能拉起指定服务
22. bundleName: 'com.example.myapplication',
23. abilityName: 'ExtensionAbility'
24. }
25. this.getUIContext().getPromptAction().showToast({ message: 'device selected' })
26. this.context.startAbility(want).then(() => {
27. hilog.info(0x0000, 'testTag', '%{public}s', 'Succeeded in starting Ability')
28. // 更新设备状态
29. this.controller.updateState(device.networkId, devicePicker.BusinessState.SUCCESSFUL)
30. }).catch(() => {
31. hilog.error(0x0000, 'testTag', '%{public}s', 'Failed to startAbility')
32. // 更新设备状态，同时添加失败的原因，这个原因会展示在设备下方
33. this.controller.updateState(device.networkId, devicePicker.BusinessState.FAILED, 'the remote device is busy')
34. })
35. })

37. // 注册设备取消选择事件
38. this.controller.on('deviceUnselected', (device: distributedDeviceManager.DeviceBasicInfo) => {
39. this.getUIContext().getPromptAction().showToast({ message: 'device unselected' })
40. })
41. }

43. build() {
44. Column() {
45. CollaborationDevicePicker({
46. controller: this.controller, attribute: {
47. abilityName: '流转测试',
48. abilityDesc: '这是一个流转测试的控件',
49. abilityIcon: $r('sys.media.ohos_app_icon'),
50. businessDesc: '流转到'
51. }
52. })
53. }.width('100%').alignItems(HorizontalAlign.Center);
54. }
55. }
```

| **图3** 设备流转过程效果图 | **图4** 设备流转成功效果图 | **图5** 设备流转失败效果图 | **图6** 应用描述信息效果图 |
| --- | --- | --- | --- |
| 下图中my phone处于流转中，设备名称右侧会有流转过程动画 | 下图中my phone流转成功 | 下图中my phone流转失败，失败原因是对端设备忙 | 在设备选择面板的最上方显示应用的相关信息，包括应用图标、应用名称、应用描述信息 |

### release

PhonePC/2in1TabletTV

release(): void

释放设备选择控制器，与[createDevicePickerController](servicecollaboration-devicepicker.md#createdevicepickercontroller)方法对应。

在应用不需要设备选择控制器的时候需要调用release()接口进行释放，比如在应用onCreate()生命周期回调中通过[createDevicePickerController](servicecollaboration-devicepicker.md#createdevicepickercontroller)创建了设备选择控制器，可以在onDestroy()生命周期回调中通过release()进行释放。

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit'
2. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit'
3. import { devicePicker } from '@kit.ServiceCollaborationKit'

5. export default class EntryAbility extends UIAbility {
6. // 创建设备选择控制器
7. controller: devicePicker.DevicePickerController = devicePicker.createDevicePickerController()

9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
10. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate')
11. }

13. onDestroy() {
14. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy')
15. // 释放设备选择控制器
16. this.controller.release()
17. }
18. }
```

## DevicePickerAttribute

PhonePC/2in1TabletTV

设备选择器属性类，在设备选择面板的应用描述部分会显示该属性配置的信息；如果未设置则使用调用者对应的ability配置文件中的标签信息。该属性与流转组件接口[CollaborationDevicePicker](servicecollaboration-collaborationdevicepicker.md)配合使用。

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| abilityIcon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | ability对用户显示的图标，在设备选择面板的应用描述部分显示；如果不设置该属性，默认使用module.json5中的icon标签配置。 |
| abilityName | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | ability对用户显示的名称，在设备选择面板的应用描述部分显示；如果不设置该属性，默认使用module.json5中的label标签配置。 |
| abilityDesc | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | ability的描述信息，在设备选择面板的应用描述部分显示；如果不设置该属性，默认使用module.json5中的description标签配置。 |
| businessDesc | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 分布式业务描述信息，比如流转业务：“流转到”，投屏业务：“投屏到”；如果不设置该属性，对于流转业务默认使用“流转到”。 |

## BusinessState

PhonePC/2in1TabletTV

业务状态枚举类。

**系统能力：** SystemCapability.Collaboration.DevicePicker

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IDLE | 0 | 业务空闲状态。 |
| SUCCESSFUL | 1 | 业务成功状态。 |
| FAILED | 2 | 业务失败状态。 |
