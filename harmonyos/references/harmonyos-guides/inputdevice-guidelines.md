---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/inputdevice-guidelines
title: 输入设备开发指导
breadcrumb: 指南 > 系统 > 基础功能 > Input Kit（多模输入服务） > 输入设备开发指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:46ebc16372a153d64f568a286c7ce924a212e17cf2a9c47c269c114c90af21a9
---

## 场景介绍

输入设备管理提供设备热插拔监听、查询指定设备的键盘类型等能力。使用场景例如：当用户需要输入文本时，输入法会根据当前是否插入了物理键盘来决定是否弹出虚拟键盘，开发者可以通过监听设备热插拔判断是否有物理键盘插入。

## 导入模块

```js
import { inputDevice } from '@kit.InputKit';
```

## 接口说明

输入设备管理常用接口如下表所示，接口详细介绍请参考[@ohos.multimodalInput.inputDevice (输入设备)](../harmonyos-references/js-apis-inputdevice.md)。

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

```typescript
import { inputDevice } from '@kit.InputKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;

@Entry
@Component
struct Index {
  @State isPhysicalKeyboardExist: boolean = false;
  @State message: string = "Click to obtain the device list and monitor device hot-plug events";
  keyboards: Map<number, inputDevice.KeyboardType> = new Map();

  // ...

  build() {
    RelativeContainer() {
      Column() {
        // ...

        Text(this.message)
          .onClick(() => {
            try {
              // 1.获取设备列表，判断是否有物理键盘连接
              inputDevice.getDeviceList().then(data => {
                for (let i = 0; i < data.length; ++i) {
                  inputDevice.getKeyboardType(data[i]).then(type => {
                    if (type === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD) {
                      // 物理键盘已连接
                      this.isPhysicalKeyboardExist = true;
                      this.keyboards.set(data[i], type);
                    }
                  });
                }
              });
              // 2.监听设备热插拔
              inputDevice.on("change", (data) => {
                hilog.info(DOMAIN, 'InputDevice', `Device event info: %{public}s`, JSON.stringify(data));
                inputDevice.getKeyboardType(data.deviceId).then((type) => {
                  hilog.info(DOMAIN, 'InputDevice', 'The keyboard type is: %{public}d', type);
                  if (type === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD && data.type === 'add') {
                    // 物理键盘已插入
                    this.isPhysicalKeyboardExist = true;
                    this.keyboards.set(data.deviceId, type);
                  }
                });
                if (this.keyboards.get(data.deviceId) === inputDevice.KeyboardType.ALPHABETIC_KEYBOARD &&
                  data.type === 'remove') {
                  // 物理键盘已拔出
                  this.isPhysicalKeyboardExist = false;
                  this.keyboards.delete(data.deviceId);
                }
              });
              this.message = "Device monitoring enabled successfully"
            } catch (error) {
              hilog.error(DOMAIN, 'InputDevice', `Execute failed, error: %{public}s`,
                JSON.stringify(error, ["code", "message"]));
              this.message = `Failed to enable device monitoring. Click to retry. Error message:${JSON.stringify(error,
                ["code", "message"])}`
            }
          })
          // ...
      }
      // ...
    }
  }
}
```
