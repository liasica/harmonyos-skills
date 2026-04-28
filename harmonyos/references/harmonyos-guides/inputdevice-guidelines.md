---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/inputdevice-guidelines
title: 输入设备开发指导
breadcrumb: 指南 > 系统 > 基础功能 > Input Kit（多模输入服务） > 输入设备开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:35c1835d7cb8f253fa4a10dcba9c452bb3270d5f6c93eba82bd4926750feb803
---

## 场景介绍

输入设备管理提供设备热插拔监听、查询指定设备的键盘类型等能力。使用场景例如：当用户需要输入文本时，输入法会根据当前是否插入了物理键盘来决定是否弹出虚拟键盘，开发者可以通过监听设备热插拔判断是否有物理键盘插入。

## 导入模块

```
1. import { inputDevice } from '@kit.InputKit';
```

## 接口说明

输入设备管理常用接口如下表所示，接口详细介绍请参考[@ohos.multimodalInput.inputDevice](../harmonyos-references/js-apis-inputdevice.md)。

| 接口名称 | 描述 |
| --- | --- |
| getDeviceList(): Promise<Array<number>> | 获取输入设备列表。 |
| getKeyboardType(deviceId: number): Promise<KeyboardType> | 获取输入设备的键盘类型。 |
| on(type: "change", listener: Callback<DeviceListener>): void | 监听输入设备的热插拔事件。 |
| off(type: "change", listener?: Callback<DeviceListener>): void | 取消监听输入设备的热插拔事件。 |

## 虚拟键盘弹出检测

当用户需要输入文本时，输入法会根据当前是否插入了物理键盘来决定是否弹出虚拟键盘，开发者可以通过监听设备热插拔，判断是否有物理键盘插入。

### 开发步骤

1. 调用[getDeviceList](../harmonyos-references/js-apis-inputdevice.md#inputdevicegetdevicelist9)方法查询所有连接的输入设备，调用[getKeyboardType](../harmonyos-references/js-apis-inputdevice.md#inputdevicegetkeyboardtype9)方法遍历所有连接的设备，判断是否有物理键盘，若有则标记已有物理键盘连接，该步骤确保监听设备热插拔之前，检测所有插入的输入设备。
2. 调用[on](../harmonyos-references/js-apis-inputdevice.md#inputdeviceonchange9)接口监听输入设备热插拔事件，若监听到有物理键盘插入，则标记已有物理键盘连接；若监听到有物理键盘拔掉，则标记没有物理键盘连接。

```
1. import { inputDevice } from '@kit.InputKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;

6. @Entry
7. @Component
8. struct Index {
9. @State isPhysicalKeyboardExist: boolean = false;
10. @State message: string = "Click to obtain the device list and monitor device hot-plug events";
11. keyBoards: Map<number, inputDevice.KeyboardType> = new Map();

13. // ...

15. build() {
16. RelativeContainer() {
17. Column() {
18. // ...

20. Text(this.message)
21. .onClick(() => {
22. try {
23. // 1.获取设备列表，判断是否有物理键盘连接
24. inputDevice.getDeviceList().then(data => {
25. for (let i = 0; i < data.length; ++i) {
26. inputDevice.getKeyboardType(data[i]).then(type => {
27. if (type === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD) {
28. // 物理键盘已连接
29. this.isPhysicalKeyboardExist = true;
30. this.keyBoards.set(data[i], type);
31. }
32. });
33. }
34. });
35. // 2.监听设备热插拔
36. inputDevice.on("change", (data) => {
37. hilog.info(DOMAIN, 'InputDevice', `Device event info: %{public}s`, JSON.stringify(data));
38. inputDevice.getKeyboardType(data.deviceId).then((type) => {
39. hilog.info(DOMAIN, 'InputDevice', 'The keyboard type is: %{public}d', type);
40. if (type === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD && data.type === 'add') {
41. // 物理键盘已插入
42. this.isPhysicalKeyboardExist = true;
43. this.keyBoards.set(data.deviceId, type);
44. }
45. });
46. if (this.keyBoards.get(data.deviceId) === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD &&
47. data.type === 'remove') {
48. // 物理键盘已拔掉
49. this.isPhysicalKeyboardExist = false;
50. this.keyBoards.delete(data.deviceId);
51. }
52. });
53. this.message = "Device monitoring enabled successfully"
54. } catch (error) {
55. hilog.error(DOMAIN, 'InputDevice', `Execute failed, error: %{public}s`,
56. JSON.stringify(error, ["code", "message"]));
57. this.message = `Failed to enable device monitoring. Click to retry. Error message:${JSON.stringify(error,
58. ["code", "message"])}`
59. }
60. })
61. // ...
62. }
63. // ...
64. }
65. }
66. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputKit/ArkTSInputDevice/entry/src/main/ets/pages/Index.ets#L16-L131)
