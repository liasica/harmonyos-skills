---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputdevice
title: @ohos.multimodalInput.inputDevice (输入设备)
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > ArkTS API > @ohos.multimodalInput.inputDevice (输入设备)
category: harmonyos-references
scraped_at: 2026-04-28T08:10:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8eb4f03d732f2121a9fcc7ee1a4ef199d582e6bb0dfabb752de4af1a2845240f
---

本模块提供输入设备管理能力，包括监听输入设备的连接和断开状态，查询设备名称等输入设备信息。

说明

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { inputDevice } from '@kit.InputKit';
```

## inputDevice.getDeviceList9+

PhonePC/2in1TabletTVWearable

getDeviceList(callback: AsyncCallback<Array<number>>): void

获取所有输入设备的ID列表，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，返回所有输入设备的ID列表。ID是输入设备的唯一标识。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. try {
12. inputDevice.getDeviceList((error: BusinessError, ids: Array<number>) => {
13. if (error) {
14. console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
15. return;
16. }
17. console.info(`Device id list: ${JSON.stringify(ids)}`);
18. });
19. } catch (error) {
20. console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
21. }
22. })
23. }
24. }
25. }
```

## inputDevice.getDeviceList9+

PhonePC/2in1TabletTVWearable

getDeviceList(): Promise<Array<number>>

获取所有输入设备的ID列表，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回所有输入设备的ID列表。ID是输入设备的唯一标识。 |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. try {
12. inputDevice.getDeviceList().then((ids: Array<number>) => {
13. console.info(`Device id list: ${JSON.stringify(ids)}`);
14. }).catch((error: BusinessError) => {
15. console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
16. });
17. } catch (error) {
18. console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
19. }
20. })
21. }
22. }
23. }
```

## inputDevice.getDeviceInfo9+

PhonePC/2in1TabletTVWearable

getDeviceInfo(deviceId: number, callback: AsyncCallback<InputDeviceData>): void

获取指定输入设备的信息，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| callback | AsyncCallback<[InputDeviceData](js-apis-inputdevice.md#inputdevicedata)> | 是 | 回调函数。返回输入设备信息，包括输入设备ID、名称、支持的输入能力、物理地址、版本信息及产品信息等。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. // 获取输入设备ID为1的设备信息。
12. try {
13. inputDevice.getDeviceInfo(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
14. if (error) {
15. console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
16. return;
17. }
18. console.info(`Device info: ${JSON.stringify(deviceData)}`);
19. });
20. } catch (error) {
21. console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
22. }
23. })
24. }
25. }
26. }
```

## inputDevice.getDeviceInfo9+

PhonePC/2in1TabletTVWearable

getDeviceInfo(deviceId: number): Promise<InputDeviceData>

获取指定id的输入设备信息，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[InputDeviceData](js-apis-inputdevice.md#inputdevicedata)> | Promise对象，返回输入设备信息，包括输入设备ID、名称、支持的输入能力、物理地址、版本信息及产品信息等。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. // 获取输入设备ID为1的设备信息。
12. try {
13. inputDevice.getDeviceInfo(1).then((deviceData: inputDevice.InputDeviceData) => {
14. console.info(`Device info: ${JSON.stringify(deviceData)}`);
15. }).catch((error: BusinessError) => {
16. console.error(`Get device info failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
17. });
18. } catch (error) {
19. console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
20. }
21. })
22. }
23. }
24. }
```

## inputDevice.getDeviceInfoSync10+

PhonePC/2in1TabletTVWearable

getDeviceInfoSync(deviceId: number): InputDeviceData

获取指定输入设备的信息。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [InputDeviceData](js-apis-inputdevice.md#inputdevicedata) | 返回输入设备信息，包括输入设备ID、名称、支持的输入能力、物理地址、版本信息及产品信息等。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. RelativeContainer() {
8. Text()
9. .onClick(() => {
10. // 获取输入设备ID为1的设备信息。
11. try {
12. let deviceData: inputDevice.InputDeviceData = inputDevice.getDeviceInfoSync(1);
13. console.info(`Device info: ${JSON.stringify(deviceData)}`);
14. } catch (error) {
15. console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
16. }
17. })
18. }
19. }
20. }
```

## inputDevice.on('change')9+

PhonePC/2in1TabletTVWearable

on(type: "change", listener: Callback<DeviceListener>): void

注册监听输入设备的热插拔事件，使用时需连接鼠标、键盘、触摸屏等外部设备。使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 输入设备的事件类型，固定值为'change'。 |
| listener | Callback<[DeviceListener](js-apis-inputdevice.md#devicelistener9)> | 是 | 回调函数，异步上报输入设备热插拔事件。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

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

13. build() {
14. RelativeContainer() {
15. Column() {
16. Text(this.message)
17. .onClick(() => {
18. try {
19. // 1.获取设备列表，判断是否有物理键盘连接
20. inputDevice.getDeviceList().then(data => {
21. for (let i = 0; i < data.length; ++i) {
22. inputDevice.getKeyboardType(data[i]).then(type => {
23. if (type === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD) {
24. // 物理键盘已连接
25. this.isPhysicalKeyboardExist = true;
26. this.keyBoards.set(data[i], type);
27. }
28. });
29. }
30. });
31. // 2.监听设备热插拔
32. inputDevice.on("change", (data) => {
33. hilog.info(DOMAIN, 'InputDevice', `Device event info: %{public}s`, JSON.stringify(data));
34. inputDevice.getKeyboardType(data.deviceId).then((type) => {
35. hilog.info(DOMAIN, 'InputDevice', 'The keyboard type is: %{public}d', type);
36. if (type === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD && data.type === 'add') {
37. // 物理键盘已插入
38. this.isPhysicalKeyboardExist = true;
39. this.keyBoards.set(data.deviceId, type);
40. }
41. });
42. if (this.keyBoards.get(data.deviceId) === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD &&
43. data.type === 'remove') {
44. // 物理键盘已拔掉
45. this.isPhysicalKeyboardExist = false;
46. this.keyBoards.delete(data.deviceId);
47. }
48. });
49. this.message = "Device monitoring enabled successfully"
50. } catch (error) {
51. hilog.error(DOMAIN, 'InputDevice', `Execute failed, error: %{public}s`,
52. JSON.stringify(error, ["code", "message"]));
53. this.message = `Failed to enable device monitoring. Click to retry. Error message:${JSON.stringify(error,
54. ["code", "message"])}`
55. }
56. })
57. }
58. }
59. }
60. }
```

## inputDevice.off('change')9+

PhonePC/2in1TabletTVWearable

off(type: "change", listener?: Callback<DeviceListener>): void

取消监听输入设备的热插拔事件。在应用退出前调用，取消监听。使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 输入设备的事件类型，固定值为'change'。 |
| listener | Callback<[DeviceListener](js-apis-inputdevice.md#devicelistener9)> | 否 | 取消监听的回调函数，缺省时取消所有输入设备热插拔事件的监听。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. RelativeContainer() {
8. Text()
9. .onClick(() => {
10. let callback = (data: inputDevice.DeviceListener) => {
11. console.info(`Report device event info: ${JSON.stringify(data, [`type`, `deviceId`])}`);
12. };

14. try {
15. inputDevice.on("change", callback);
16. } catch (error) {
17. console.error(`Listen device event failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
18. }

20. // 取消指定的监听。
21. try {
22. inputDevice.off("change", callback);
23. } catch (error) {
24. console.error(`Cancel listening device event failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
25. }

27. // 取消所有监听。
28. try {
29. inputDevice.off("change");
30. } catch (error) {
31. console.error(`Cancel all listening device event failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
32. }
33. })
34. }
35. }
36. }
```

## inputDevice.getDeviceIds(deprecated)

PhonePC/2in1TabletTVWearable

getDeviceIds(callback: AsyncCallback<Array<number>>): void

获取所有输入设备的ID列表，使用callback异步回调。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceList](js-apis-inputdevice.md#inputdevicegetdevicelist9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数，返回所有输入设备的ID列表。ID是输入设备的唯一标识。 |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. inputDevice.getDeviceIds((error: BusinessError, ids: Array<number>) => {
12. if (error) {
13. console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
14. return;
15. }
16. console.info(`Device id list: ${JSON.stringify(ids)}`);
17. });
18. })
19. }
20. }
21. }
```

## inputDevice.getDeviceIds(deprecated)

PhonePC/2in1TabletTVWearable

getDeviceIds(): Promise<Array<number>>

获取所有输入设备的ID列表，使用Promise异步回调。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceList](js-apis-inputdevice.md#inputdevicegetdevicelist9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回所有输入设备的ID列表。ID是输入设备的唯一标识。 |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. inputDevice.getDeviceIds().then((ids: Array<number>) => {
12. console.info(`Device id list: ${JSON.stringify(ids)}`);
13. }).catch((error: BusinessError) => {
14. console.error(`Failed to get device id list, error: ${JSON.stringify(error, [`code`, `message`])}`);
15. })
16. })
17. }
18. }
19. }
```

## inputDevice.getDevice(deprecated)

PhonePC/2in1TabletTVWearable

getDevice(deviceId: number, callback: AsyncCallback<InputDeviceData>): void

获取指定id的输入设备信息，使用callback异步回调。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceInfo](js-apis-inputdevice.md#inputdevicegetdeviceinfo9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| callback | AsyncCallback<[InputDeviceData](js-apis-inputdevice.md#inputdevicedata)> | 是 | 回调函数，返回输入设备信息，包括输入设备ID、名称、支持的输入能力、物理地址、版本信息及产品信息等。 |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. // 获取输入设备ID为1的设备信息。
12. inputDevice.getDevice(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
13. if (error) {
14. console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
15. return;
16. }
17. console.info(`Device info: ${JSON.stringify(deviceData)}`);
18. });
19. })
20. }
21. }
22. }
```

## inputDevice.getDevice(deprecated)

PhonePC/2in1TabletTVWearable

getDevice(deviceId: number): Promise<InputDeviceData>

获取指定id的输入设备信息，使用Promise异步回调。

说明

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceInfo](js-apis-inputdevice.md#inputdevicegetdeviceinfo9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[InputDeviceData](js-apis-inputdevice.md#inputdevicedata)> | Promise对象，返回输入设备信息，包括输入设备ID、名称、支持的输入能力、物理地址、版本信息及产品信息等。 |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. // 获取输入设备ID为1的设备信息。
12. inputDevice.getDevice(1).then((deviceData: inputDevice.InputDeviceData) => {
13. console.info(`Device info: ${JSON.stringify(deviceData)}`);
14. }).catch((error: BusinessError) => {
15. console.error(`Failed to get device info, error: ${JSON.stringify(error, [`code`, `message`])}`);
16. })
17. })
18. }
19. }
20. }
```

## inputDevice.supportKeys9+

PhonePC/2in1TabletTVWearable

supportKeys(deviceId: number, keys: Array<KeyCode>, callback: AsyncCallback <Array<boolean>>): void

查询指定输入设备是否支持指定按键，使用Callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| keys | Array[<KeyCode>](js-apis-keycode.md#keycode) | 是 | 需要查询的键值，最多支持5个按键查询。 |
| callback | AsyncCallback<Array<boolean>> | 是 | 回调函数，返回查询结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. // 查询ID为1的输入设备对于17、22和2055按键的支持情况。
12. try {
13. inputDevice.supportKeys(1, [17, 22, 2055], (error: BusinessError, supportResult: Array<Boolean>) => {
14. console.info(`Query result: ${JSON.stringify(supportResult)}`);
15. });
16. } catch (error) {
17. console.error(`Query failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
18. }
19. })
20. }
21. }
22. }
```

## inputDevice.supportKeys9+

PhonePC/2in1TabletTVWearable

supportKeys(deviceId: number, keys: Array<KeyCode>): Promise<Array<boolean>>

查询指定输入设备是否支持指定按键，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| keys | Array[<KeyCode>](js-apis-keycode.md#keycode) | 是 | 需要查询的键值，最多支持查询5个按键。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<boolean>> | Promise对象，返回查询结果。true 表示支持，false表示不支持。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. // 查询ID为1的输入设备对于17、22和2055按键的支持情况。
12. try {
13. inputDevice.supportKeys(1, [17, 22, 2055]).then((supportResult: Array<Boolean>) => {
14. console.info(`Query result: ${JSON.stringify(supportResult)}`);
15. }).catch((error: BusinessError) => {
16. console.error(`Query support Keys failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
17. });
18. } catch (error) {
19. console.error(`Query failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
20. }
21. })
22. }
23. }
24. }
```

## inputDevice.supportKeysSync10+

PhonePC/2in1TabletTVWearable

supportKeysSync(deviceId: number, keys: Array<KeyCode>): Array<boolean>

查询指定id的输入设备对指定键值的支持情况。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| keys | Array[<KeyCode>](js-apis-keycode.md#keycode) | 是 | 需要查询的键值，最多支持查询5个按键。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<boolean> | 返回查询结果。true表示支持，false表示不支持。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. RelativeContainer() {
8. Text()
9. .onClick(() => {
10. // 查询ID为1的输入设备对于17、22和2055按键的支持情况。
11. try {
12. let supportResult: Array<Boolean> = inputDevice.supportKeysSync(1, [17, 22, 2055])
13. console.info(`Query result: ${JSON.stringify(supportResult)}`)
14. } catch (error) {
15. console.error(`Query failed, error: ${JSON.stringify(error, [`code`, `message`])}`)
16. }
17. })
18. }
19. }
20. }
```

## inputDevice.getKeyboardType9+

PhonePC/2in1TabletTVWearable

getKeyboardType(deviceId: number, callback: AsyncCallback<KeyboardType>): void

获取输入设备的键盘类型，如全键盘、小键盘等，使用callback异步回调。输入设备的键盘类型以接口返回结果为准。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| callback | AsyncCallback<[KeyboardType](js-apis-inputdevice.md#keyboardtype9)> | 是 | 回调函数，返回查询结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. // 查询ID为1的输入设备的键盘类型。
12. try {
13. inputDevice.getKeyboardType(1, (error: BusinessError, type: number) => {
14. if (error) {
15. console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`);
16. return;
17. }
18. console.info(`Keyboard type: ${JSON.stringify(type)}`);
19. });
20. } catch (error) {
21. console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`);
22. }
23. })
24. }
25. }
26. }
```

## inputDevice.getKeyboardType9+

PhonePC/2in1TabletTVWearable

getKeyboardType(deviceId: number): Promise<KeyboardType>

获取输入设备的键盘类型，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[KeyboardType](js-apis-inputdevice.md#keyboardtype9)> | Promise对象，返回查询结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. // 示例查询设备ID为1的设备键盘类型。
12. try {
13. inputDevice.getKeyboardType(1).then((type: number) => {
14. console.info(`Keyboard type: ${JSON.stringify(type)}`);
15. }).catch((error: BusinessError) => {
16. console.error(`Get keyboard type failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
17. })
18. } catch (error) {
19. console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`);
20. }
21. })
22. }
23. }
24. }
```

## inputDevice.getKeyboardTypeSync10+

PhonePC/2in1TabletTVWearable

getKeyboardTypeSync(deviceId: number): KeyboardType

获取输入设备的键盘类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [KeyboardType](js-apis-inputdevice.md#keyboardtype9) | 返回查询结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. RelativeContainer() {
8. Text()
9. .onClick(() => {
10. // 示例查询设备ID为1的设备键盘类型。
11. try {
12. let type: number = inputDevice.getKeyboardTypeSync(1)
13. console.info(`Keyboard type: ${JSON.stringify(type)}`)
14. } catch (error) {
15. console.error(`Failed to get keyboard type, error: ${JSON.stringify(error, [`code`, `message`])}`)
16. }
17. })
18. }
19. }
20. }
```

## inputDevice.isFunctionKeyEnabled15+

PhonePC/2in1TabletTVWearable

isFunctionKeyEnabled(functionKey: FunctionKey): Promise<boolean>

检查功能键（如：CapsLock键）是否使能。使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| functionKey | [FunctionKey](js-apis-inputdevice.md#functionkey15) | 是 | 需要设置的功能键类型。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回查询结果，true表示功能键使能，false表示功能键未使能。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[输入设备错误码](errorcode-inputdevice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| 3900002 | There is currently no keyboard device connected. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. try {
12. inputDevice.isFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK).then((state: boolean) => {
13. console.info(`capslock state: ${JSON.stringify(state)}`);
14. }).catch((error: BusinessError) => {
15. console.error(`Get capslock state failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
16. })
17. } catch (error) {
18. console.error(`Failed to get capslock state, error: ${JSON.stringify(error, [`code`, `message`])}`);
19. }
20. })
21. }
22. }
23. }
```

## inputDevice.setFunctionKeyEnabled15+

PhonePC/2in1TabletTVWearable

setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>

设置功能键（如：CapsLock键）使能状态。使用Promise异步回调。

**需要权限**：ohos.permission.INPUT\_KEYBOARD\_CONTROLLER

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| functionKey | [FunctionKey](js-apis-inputdevice.md#functionkey15) | 是 | 需要设置的功能键类型。 |
| enabled | boolean | 是 | 功能键使能状态。取值为true表示使能功能键，取值为false表示不使能功能键。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[输入设备错误码](errorcode-inputdevice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| 3900002 | There is currently no keyboard device connected. |
| 3900003 | It is prohibited for non-input applications. |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. try {
12. inputDevice.setFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK, true).then(() => {
13. console.info(`Set capslock state success`);
14. }).catch((error: BusinessError) => {
15. console.error(`Set capslock state failed, error=${JSON.stringify(error)}`);
16. });
17. } catch (error) {
18. console.error(`Set capslock enable error`);
19. }
20. })
21. }
22. }
23. }
```

## inputDevice.getIntervalSinceLastInput14+

PhonePC/2in1TabletTVWearable

getIntervalSinceLastInput(): Promise<number>

获取距离上次系统输入事件的时间间隔（包含设备休眠时间），使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回距离上次系统输入事件的时间间隔，单位：μs。 |

**示例**：

```
1. import { inputDevice } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. inputDevice.getIntervalSinceLastInput().then((timeInterval: number) => {
12. console.info(`Interval since last input: ${JSON.stringify(timeInterval)}`);
13. }).catch((error: BusinessError) => {
14. console.error(`Get interval since last input failed, error: ${JSON.stringify(error)}`);
15. })
16. })
17. }
18. }
19. }
```

## DeviceListener9+

PhonePC/2in1TabletTVWearable

描述输入设备热插拔的信息。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ChangedType](js-apis-inputdevice.md#changedtype9) | 否 | 否 | 输入设备插入或者移除。 |
| deviceId | number | 否 | 否 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

## InputDeviceData

PhonePC/2in1TabletTVWearable

描述输入设备的信息。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 输入设备的唯一标识，同一个物理设备反复插拔，设备ID可能会发生变化。 |
| name | string | 否 | 否 | 输入设备的名称。 |
| sources | Array<[SourceType](js-apis-inputdevice.md#sourcetype9)> | 否 | 否 | 输入设备的输入能力。包括键盘、鼠标、触摸屏、轨迹球、触控板、操纵杆等。 |
| axisRanges | Array<[AxisRange](js-apis-inputdevice.md#axisrange)> | 否 | 否 | 输入设备的轴信息。 |
| bus9+ | number | 否 | 否 | 输入设备的总线类型，该值以输入设备上报为准。 |
| product9+ | number | 否 | 否 | 输入设备的产品信息。 |
| vendor9+ | number | 否 | 否 | 输入设备的厂商信息。 |
| version9+ | number | 否 | 否 | 输入设备的版本信息。 |
| phys9+ | string | 否 | 否 | 输入设备的物理地址。 |
| uniq9+ | string | 否 | 否 | 输入设备的唯一标识。 |
| isVirtual23+ | boolean | 否 | 是 | 输入设备是否为虚拟设备。  true表示是虚拟设备，false表示是非虚拟设备。 |
| isLocal23+ | boolean | 否 | 是 | 输入设备是否为本地设备。  true表示是本地设备，false表示是非本地设备。 |

## AxisType9+

PhonePC/2in1TabletTVWearable

type AxisType = 'touchmajor' | 'touchminor' | 'orientation' | 'x' | 'y' | 'pressure' | 'toolminor' | 'toolmajor' | 'null'

输入设备的轴类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

| 类型 | 说明 |
| --- | --- |
| 'touchmajor' | 椭圆触摸区域长轴。 |
| 'touchminor' | 椭圆触摸区域短轴。 |
| 'toolminor' | 工具区域短轴。 |
| 'toolmajor' | 工具区域长轴。 |
| 'orientation' | 方向轴。 |
| 'pressure' | 压力轴。 |
| 'x' | 横坐标轴。 |
| 'y' | 纵坐标轴。 |
| 'null' | 无。 |

## AxisRange

PhonePC/2in1TabletTVWearable

输入设备的轴信息。

**系统能力**： SystemCapability.MultimodalInput.Input.InputDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| source | [SourceType](js-apis-inputdevice.md#sourcetype9) | 否 | 否 | 输入设备的输入能力。包括键盘、鼠标、触摸屏、轨迹球、触控板、操纵杆等。 |
| axis | [AxisType](js-apis-inputdevice.md#axistype9) | 否 | 否 | 输入设备的轴类型。 |
| max | number | 否 | 否 | 轴的最大值。 |
| min | number | 否 | 否 | 轴的最小值。 |
| fuzz9+ | number | 否 | 否 | 轴的模糊值。 |
| flat9+ | number | 否 | 否 | 轴的基准值。 |
| resolution9+ | number | 否 | 否 | 轴的分辨率。 |

## SourceType9+

PhonePC/2in1TabletTVWearable

type SourceType = 'keyboard' | 'mouse' | 'touchpad' | 'touchscreen' | 'joystick' | 'trackball'

输入设备的输入能力。包括键盘、鼠标、触摸屏、轨迹球、触控板、操纵杆等。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

| 类型 | 说明 |
| --- | --- |
| 'keyboard' | 表示输入设备是键盘。 |
| 'touchscreen' | 表示输入设备是触摸屏。 |
| 'mouse' | 表示输入设备是鼠标。 |
| 'trackball' | 表示输入设备是轨迹球。 |
| 'touchpad' | 表示输入设备是触控板。 |
| 'joystick' | 表示输入设备是操纵杆。 |

## ChangedType9+

PhonePC/2in1TabletTVWearable

type ChangedType = 'add' | 'remove'

监听设备热插拔事件类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

| 类型 | 说明 |
| --- | --- |
| 'add' | 插入输入设备。 |
| 'remove' | 移除输入设备。 |

## KeyboardType9+

PhonePC/2in1TabletTVWearable

键盘输入设备的类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 表示无按键设备。 |
| UNKNOWN | 1 | 表示未知按键设备。 |
| ALPHABETIC\_KEYBOARD | 2 | 表示全键盘设备。 |
| DIGITAL\_KEYBOARD | 3 | 表示小键盘设备。 |
| HANDWRITING\_PEN | 4 | 表示手写笔设备。 |
| REMOTE\_CONTROL | 5 | 表示遥控器设备。 |

## FunctionKey15+

PhonePC/2in1TabletTVWearable

功能键的类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAPS\_LOCK | 1 | CapsLock键，仅支持对输入键盘扩展的CapsLock键设置使能。 |
