---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputdevice
title: "@ohos.multimodalInput.inputDevice (输入设备)"
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > ArkTS API > @ohos.multimodalInput.inputDevice (输入设备)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:08+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:284285c79435f724096b7562ad807f977b316b5272cd09f3c2734e9891a8c344
---

本模块提供输入设备管理能力，包括监听输入设备的连接和断开状态，查询设备名称等输入设备信息。

**说明** 

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

## inputDevice.getDeviceList9+

getDeviceList(callback: AsyncCallback<Array<number>>): void

获取所有输入设备的ID列表，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数。当获取成功，err为undefined，data为所有输入设备的ID列表（ID是输入设备的唯一标识）；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 获取输入设备列表
            inputDevice.getDeviceList((error: BusinessError, ids: Array<number>) => {
              if (error) {
                console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in getting device id list: ${JSON.stringify(ids)}.`);
            });
          } catch (error) {
            console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        });
    }
  }
}
```

## inputDevice.getDeviceList9+

getDeviceList(): Promise<Array<number>>

获取所有输入设备的ID列表，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回所有输入设备的ID列表。ID是输入设备的唯一标识。 |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 获取输入设备列表
            inputDevice.getDeviceList().then((ids: Array<number>) => {
              console.info(`Succeeded in getting device id list: ${JSON.stringify(ids)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            });
          } catch (error) {
            console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.getDeviceInfo9+

getDeviceInfo(deviceId: number, callback: AsyncCallback<InputDeviceData>): void

获取指定输入设备的信息，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| callback | AsyncCallback<[InputDeviceData](js-apis-inputdevice.md#inputdevicedata)> | 是 | 回调函数。当获取成功，err为undefined，data为输入设备信息（包括输入设备ID、名称、支持的输入能力等）；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID为1的设备信息。
          try {
            // 获取输入设备信息
            inputDevice.getDeviceInfo(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
              if (error) {
                console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in getting device info: ${JSON.stringify(deviceData)}.`);
            });
          } catch (error) {
            console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.getDeviceInfo9+

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID为1的设备信息。
          try {
            // 获取输入设备信息
            inputDevice.getDeviceInfo(1).then((deviceData: inputDevice.InputDeviceData) => {
              console.info(`Succeeded in getting device info: ${JSON.stringify(deviceData)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            });
          } catch (error) {
            console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.getDeviceInfoSync10+

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID为1的设备信息。
          try {
            let deviceData: inputDevice.InputDeviceData = inputDevice.getDeviceInfoSync(1);
            console.info(`Succeeded in getting device info: ${JSON.stringify(deviceData)}.`);
          } catch (error) {
            console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.on('change')9+

on(type: 'change', listener: Callback<DeviceListener>): void

注册监听输入设备的热插拔事件，使用时需连接鼠标、键盘、触摸屏等外部设备。使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 输入设备的事件类型，固定值为'change'。 |
| listener | Callback<[DeviceListener](js-apis-inputdevice.md#devicelistener9)> | 是 | 回调函数，返回输入设备热插拔事件。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

const DOMAIN = 0x0000;

@Entry
@Component
struct Index {
  @State isPhysicalKeyboardExist: boolean = false;
  @State message: string = 'Click to obtain the device list and monitor device hot-plug events';
  keyboards: Map<number, inputDevice.KeyboardType> = new Map();

  build() {
    RelativeContainer() {
      Column() {
        Text(this.message)
          .onClick(() => {
            try {
              // 1.获取设备列表，判断是否有物理键盘连接
              inputDevice.getDeviceList().then(data => {
                for (let i = 0; i < data.length; ++i) {
                  // 获取键盘类型
                  inputDevice.getKeyboardType(data[i]).then(type => {
                    if (type === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD) {
                      // 物理键盘已连接
                      this.isPhysicalKeyboardExist = true;
                      this.keyboards.set(data[i], type);
                    }
                  }).catch((error: BusinessError) => {
                    console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                  });
                }
              }).catch((error: BusinessError) => {
                console.error(`Failed to get Device List, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              });
              // 2.监听设备热插拔
              inputDevice.on('change', (data) => {
                // 打印日志
                hilog.info(DOMAIN, 'InputDevice', `Device event info: %{public}s`, JSON.stringify(data));
                // 获取键盘类型
                inputDevice.getKeyboardType(data.deviceId).then((type) => {
                  // 打印日志
                  hilog.info(DOMAIN, 'InputDevice', 'The keyboard type is: %{public}d', type);
                  if (type === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD && data.type === 'add') {
                    // 物理键盘已插入
                    this.isPhysicalKeyboardExist = true;
                    this.keyboards.set(data.deviceId, type);
                  }
                }).catch((error: BusinessError) => {
                  console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                });
                if (this.keyboards.get(data.deviceId) === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD &&
                  data.type === 'remove') {
                  // 物理键盘已拔掉
                  this.isPhysicalKeyboardExist = false;
                  this.keyboards.delete(data.deviceId);
                }
              });
              this.message = 'Device monitoring enabled successfully'
            } catch (error) {
              // 打印错误日志
              hilog.error(DOMAIN, 'InputDevice', `Execute failed, error: %{public}s`,
                JSON.stringify(error, ['code', 'message']));
              this.message = `Failed to enable device monitoring. Click to retry. Error message:${JSON.stringify(error,
                ["code", "message"])}`
            }
          })
      }
    }
  }
}
```

## inputDevice.off('change')9+

off(type: 'change', listener?: Callback<DeviceListener>): void

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          let callback = (data: inputDevice.DeviceListener) => {
            console.info(`Succeeded in listening to device change, data: ${JSON.stringify(data, [`type`, `deviceId`])}.`);
          };

          try {
            // 监听设备热插拔事件
            inputDevice.on('change', callback);
          } catch (error) {
            console.error(`Failed to listen to device event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }

          // 取消指定的监听。
          try {
            // 取消监听设备热插拔事件
            inputDevice.off('change', callback);
          } catch (error) {
            console.error(`Failed to cancel listening to device event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }

          // 取消所有监听。
          try {
            // 取消监听设备热插拔事件
            inputDevice.off('change');
          } catch (error) {
            console.error(`Failed to cancel all listening device event, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.getDeviceIds(deprecated)

getDeviceIds(callback: AsyncCallback<Array<number>>): void

获取所有输入设备的ID列表，使用callback异步回调。

**说明** 

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceList](js-apis-inputdevice.md#inputdevicegetdevicelist9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<number>> | 是 | 回调函数。当获取成功，err为undefined，data为所有输入设备的ID列表；否则为错误对象。 |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID列表
          inputDevice.getDeviceIds((error: BusinessError, ids: Array<number>) => {
            if (error) {
              console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              return;
            }
            console.info(`Succeeded in getting device id list: ${JSON.stringify(ids)}.`);
          });
        })
    }
  }
}
```

## inputDevice.getDeviceIds(deprecated)

getDeviceIds(): Promise<Array<number>>

获取所有输入设备的ID列表，使用Promise异步回调。

**说明** 

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceList](js-apis-inputdevice.md#inputdevicegetdevicelist9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回所有输入设备的ID列表。ID是输入设备的唯一标识。 |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID列表
          inputDevice.getDeviceIds().then((ids: Array<number>) => {
            console.info(`Succeeded in getting device id list: ${JSON.stringify(ids)}.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to get device id list, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          })
        })
    }
  }
}
```

## inputDevice.getDevice(deprecated)

getDevice(deviceId: number, callback: AsyncCallback<InputDeviceData>): void

获取指定id的输入设备信息，使用callback异步回调。

**说明** 

从API version 8 开始支持，从API version 9 开始废弃，建议使用[inputDevice.getDeviceInfo](js-apis-inputdevice.md#inputdevicegetdeviceinfo9)替代。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| callback | AsyncCallback<[InputDeviceData](js-apis-inputdevice.md#inputdevicedata)> | 是 | 回调函数。当获取成功，err为undefined，data为输入设备信息；否则为错误对象。 |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID为1的设备信息。
          inputDevice.getDevice(1, (error: BusinessError, deviceData: inputDevice.InputDeviceData) => {
            if (error) {
              console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              return;
            }
            console.info(`Succeeded in getting device info: ${JSON.stringify(deviceData)}.`);
          });
        })
    }
  }
}
```

## inputDevice.getDevice(deprecated)

getDevice(deviceId: number): Promise<InputDeviceData>

获取指定id的输入设备信息，使用Promise异步回调。

**说明** 

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

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 获取输入设备ID为1的设备信息。
          inputDevice.getDevice(1).then((deviceData: inputDevice.InputDeviceData) => {
            console.info(`Succeeded in getting device info: ${JSON.stringify(deviceData)}.`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to get device info, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          })
        })
    }
  }
}
```

## inputDevice.supportKeys9+

supportKeys(deviceId: number, keys: Array<KeyCode>, callback: AsyncCallback <Array<boolean>>): void

查询指定输入设备是否支持指定按键，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| keys | Array<[KeyCode](js-apis-keycode.md#keycode)> | 是 | 需要查询的键值，最多支持5个按键查询。 |
| callback | AsyncCallback<Array<boolean>> | 是 | 回调函数。当查询成功，err为undefined，data为按键支持查询结果（数组元素与keys参数一一对应，true表示支持，false表示不支持）；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 查询ID为1的输入设备对于17、22和2055按键的支持情况。
          try {
            // 查询按键支持情况
            inputDevice.supportKeys(1, [17, 22, 2055], (error: BusinessError, supportResult: Array<Boolean>) => {
              if (error) {
                console.error(`Failed to query support key, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in querying support keys, supportResult: ${JSON.stringify(supportResult)}.`);
            });
          } catch (error) {
            console.error(`Failed to query support key, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.supportKeys9+

supportKeys(deviceId: number, keys: Array<KeyCode>): Promise<Array<boolean>>

查询指定输入设备是否支持指定按键，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| keys | Array<[KeyCode](js-apis-keycode.md#keycode)> | 是 | 需要查询的键值，最多支持查询5个按键。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<boolean>> | Promise对象，返回查询结果。true表示支持，false表示不支持。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 查询ID为1的输入设备对于17、22和2055按键的支持情况。
          try {
            // 查询按键支持情况
            inputDevice.supportKeys(1, [17, 22, 2055]).then((supportResult: Array<Boolean>) => {
              console.info(`Succeeded in querying support keys, result: ${JSON.stringify(supportResult)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to query support Keys, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            });
          } catch (error) {
            console.error(`Failed to query support key, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.supportKeysSync10+

supportKeysSync(deviceId: number, keys: Array<KeyCode>): Array<boolean>

查询指定id的输入设备对指定键值的支持情况。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| keys | Array<[KeyCode](js-apis-keycode.md#keycode)> | 是 | 需要查询的键值，最多支持查询5个按键。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<boolean> | 返回查询结果。true表示支持，false表示不支持。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 查询ID为1的输入设备对于17、22和2055按键的支持情况。
          try {
            let supportResult: Array<Boolean> = inputDevice.supportKeysSync(1, [17, 22, 2055]);
            console.info(`Succeeded in querying support keys, result: ${JSON.stringify(supportResult)}.`);
          } catch (error) {
            console.error(`Failed to query support key, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.getKeyboardType9+

getKeyboardType(deviceId: number, callback: AsyncCallback<KeyboardType>): void

获取输入设备的键盘类型，如全键盘、小键盘等。输入设备的键盘类型以接口返回结果为准。使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | number | 是 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| callback | AsyncCallback<[KeyboardType](js-apis-inputdevice.md#keyboardtype9)> | 是 | 回调函数。当查询成功，err为undefined，data为输入设备的键盘类型；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 查询ID为1的输入设备的键盘类型。
          try {
            // 获取键盘类型
            inputDevice.getKeyboardType(1, (error: BusinessError, type: inputDevice.KeyboardType) => {
              if (error) {
                console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in getting keyboard type: ${JSON.stringify(type)}.`);
            });
          } catch (error) {
            console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.getKeyboardType9+

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
| Promise<[KeyboardType](js-apis-inputdevice.md#keyboardtype9)> | Promise对象，返回输入设备的键盘类型。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 示例查询设备ID为1的设备键盘类型。
          try {
            // 获取键盘类型
            inputDevice.getKeyboardType(1).then((type: inputDevice.KeyboardType) => {
              console.info(`Succeeded in getting keyboard type: ${JSON.stringify(type)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.getKeyboardTypeSync10+

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          // 示例查询设备ID为1的设备键盘类型。
          try {
            let type: inputDevice.KeyboardType = inputDevice.getKeyboardTypeSync(1);
            console.info(`Succeeded in getting keyboard type: ${JSON.stringify(type)}.`);
          } catch (error) {
            console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.isFunctionKeyEnabled15+

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
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 3900002 | There is currently no keyboard device connected. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 查询功能键是否使能
            inputDevice.isFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK).then((state: boolean) => {
              console.info(`Succeeded in getting capslock state: ${JSON.stringify(state)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get capslock state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get capslock state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.setFunctionKeyEnabled15+

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
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[输入设备错误码](errorcode-inputdevice.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 3900002 | There is currently no keyboard device connected. |
| 3900003 | It is prohibited for non-input applications. |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 设置功能键使能状态
            inputDevice.setFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK, true).then(() => {
              console.info(`Succeeded in setting capslock state.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set capslock state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            });
          } catch (error) {
            console.error(`Failed to set capslock enable, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## inputDevice.getIntervalSinceLastInput14+

getIntervalSinceLastInput(): Promise<number>

获取距离上次系统输入事件的时间间隔（包含设备休眠时间），使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回距离上次系统输入事件的时间间隔，单位为微秒（μs）。 |

**示例**：

```js
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
           try {
            // 获取距上次输入的时间间隔
            inputDevice.getIntervalSinceLastInput().then((timeInterval: number) => {
              console.info(`Succeeded in getting interval since last input: ${JSON.stringify(timeInterval)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get interval since last input, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get interval since last input, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

## DeviceListener9+

描述输入设备热插拔的信息。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [ChangedType](js-apis-inputdevice.md#changedtype9) | 否 | 否 | 输入设备插入或者移除。 |
| deviceId | number | 否 | 否 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

## InputDeviceData

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
| isVirtual23+ | boolean | 否 | 是 | 输入设备是否为虚拟设备。  true表示是虚拟设备，false表示是非虚拟设备。当该字段不存在时，默认值为false。 |
| isLocal23+ | boolean | 否 | 是 | 输入设备是否为本地设备。  true表示是本地设备，false表示是非本地设备。当该字段不存在时，默认值为false。 |

## AxisType9+

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
| 'null' | 无类型。 |

## AxisRange

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

type ChangedType = 'add' | 'remove'

监听设备热插拔事件类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

| 类型 | 说明 |
| --- | --- |
| 'add' | 插入输入设备。 |
| 'remove' | 移除输入设备。 |

## KeyboardType9+

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

功能键的类型。

**系统能力**：SystemCapability.MultimodalInput.Input.InputDevice

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CAPS\_LOCK | 1 | CapsLock键，仅支持对输入键盘扩展的CapsLock键设置使能。 |
