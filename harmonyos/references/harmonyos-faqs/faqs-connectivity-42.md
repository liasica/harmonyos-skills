---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-42
title: BLE蓝牙广播startAdvertising报错401问题
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > BLE蓝牙广播startAdvertising报错401问题
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:91336de88da4ae55eb2284668890826c9d749dad85f7f16444de8a07cd246593
---

## 问题现象

使用BLE蓝牙广播[startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising11)出现如下报错：

```txt
Error: BusinessError 401: Invalid parameter.
```

数据结构如下：

```ts
import ble from '@ohos.bluetooth.ble';

export class BleAdvertiser {
  static startAdvertising(sendBytes: Uint8Array, timerCount: number) {
    const advertiseSettings = BleAdvertiser.buildAdvertiseSettings(timerCount);
    const advertiseData = BleAdvertiser.buildAdvertiseData(sendBytes);
    try {
      ble.startAdvertising(advertiseSettings, advertiseData);
    }catch (err) {
      console.info(`发送异常：${err}`)
    }
  }

  static buildAdvertiseData(sendByte: Uint8Array): ble.AdvertiseData {
    const advertiseData: ble.AdvertiseData = {
      includeDeviceName: false,
      manufactureData: [
        {
          manufactureId: 0xfff0,
          manufactureValue: BleAdvertiser.prepareManufacturerData(sendByte)
        }
      ],
      // 使用数组而非Map
      serviceData: [],
      serviceUuids: []
    };
    return advertiseData;
  }

  static prepareManufacturerData(input: Uint8Array): Uint8Array {
    const bufferSize = 24;
    const result = new Uint8Array(bufferSize);
    // 填充默认数据（示例：i+1）
    for (let i = 0; i < bufferSize; i++) {
      result[i] = i + 1;
    }
    // 复制输入数据到缓冲区开头
    const copyLength = Math.min(input.length, bufferSize);
    for (let i = 0; i < copyLength; i++) {
      result[i] = input[i];
    }
    return result;
  }

  static buildAdvertiseSettings(timerCount: number): ble.AdvertiseSetting {
    return {
      connectable: false,
      interval: 160,
      txPower: 0,
    };
  }
}
```

## 背景知识

1. [401参数检查失败](../harmonyos-references/errorcode-universal.md#section401-参数检查失败)错误描述：
   * 必填参数为空。
   * 参数类型不正确。
   * 参数校验失败。无论是同步还是异步接口，此类异常大部分都通过同步的方式抛出。
2. 描述BLE广播报文中制造商数据内容[ManufactureData](../harmonyos-references/js-apis-bluetooth-ble.md#manufacturedata)中，manufactureValue的类型是[ArrayBuffer](../harmonyos-references/arkts-apis-arkts-collections-arraybuffer.md)。
3. [Uint8Array](../harmonyos-references/arkts-apis-arkts-collections-uint8array.md)是一种线性数据结构，底层基于[ArrayBuffer](../harmonyos-references/arkts-apis-arkts-collections-arraybuffer.md)实现。

## 问题定位

prepareManufacturerData函数返回结果为Uint8Array，返回值作为manufactureValue的参数，而manufactureValue的类型是[ArrayBuffer](../harmonyos-references/arkts-apis-arkts-collections-arraybuffer.md)，参数类型不正确导致报错。

```ts
manufactureValue: BleAdvertiser.prepareManufacturerData(sendByte)

static prepareManufacturerData(input: Uint8Array): Uint8Array {
  const bufferSize = 24;
  const result = new Uint8Array(bufferSize);
  // 填充默认数据（示例：i+1）
  for (let i = 0; i < bufferSize; i++) {
    result[i] = i + 1;
  }
  // 复制输入数据到缓冲区开头
  const copyLength = Math.min(input.length, bufferSize);
  for (let i = 0; i < copyLength; i++) {
    result[i] = input[i];
  }
  return result;
}
```

## 分析结论

manufactureValue参数类型填写有误，需要通过Uint8Array.buffer获取ArrayBuffer对象。正确的写法如下：

```ts
let advData: ble.AdvertiseData = {
  serviceUuids: [],
  manufactureData: [
    {
      manufactureId: 0xfff0,
      manufactureValue: manufactureValueBuffer.buffer // 需要通过Uint8Array.buffer获取ArrayBuffer对象
    }
  ],
  serviceData: [],
  includeDeviceName: false // 表示是否携带设备名，可选参数。注意：带上设备名时，容易导致广播报文长度超出31个字节，使得广播启动失败
};
```

## 修改建议

manufactureValue参数需要填写正确，否则会因为参数类型不正确而报错。

完整demo如下：

```ts
import { ble } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, common, Permissions } from '@kit.AbilityKit';

const permissions: Array<Permissions> = ['ohos.permission.ACCESS_BLUETOOTH'];

// 使用UIExtensionAbility：将common.UIAbilityContext替换为common.UIExtensionContext
function reqPermissionsFromUser(permissions: Array<Permissions>, context: common.UIAbilityContext): void {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗。
  atManager.requestPermissionsFromUser(context, permissions).then((data) => {
    let grantStatus: Array<number> = data.authResults;
    let length: number = grantStatus.length;
    for (let i = 0; i < length; i++) {
      if (grantStatus[i] === 0) {
        // 用户授权，可以继续访问目标操作。
      } else {
        // 当用户拒绝授权时，系统应提示用户必须授予相应权限才能使用当前页面的功能，并指导用户前往系统设置开启所需权限。
        return;
      }
    }
    // 授权成功
  }).catch((err: BusinessError) => {
    console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
  });
}

@Entry
@Component
struct Index {
  private message: string = '开启广播';
  private advHandle: number = 0xFF; // 初始的无效值

  // 1.定义广播状态上报事件
  onReceiveEvent = (data: ble.AdvertisingStateChangeInfo) => {
    console.info(`bluetooth advertising state = ${JSON.stringify(data)}`);
    AppStorage.setOrCreate('advertiserState', data.state);
  };

  public async startAdvertising() {
    // 2.1设置广播发送的参数
    let setting: ble.AdvertiseSetting = {
      connectable: false,
      interval: 160,
      txPower: 0,
    };
    // 2.2构造广播数据
    let manufactureValueBuffer = new Uint8Array(4);
    manufactureValueBuffer[0] = 1;
    manufactureValueBuffer[1] = 2;
    manufactureValueBuffer[2] = 3;
    manufactureValueBuffer[3] = 4;
    let serviceValueBuffer = new Uint8Array(4);
    serviceValueBuffer[0] = 5;
    serviceValueBuffer[1] = 6;
    serviceValueBuffer[2] = 7;
    serviceValueBuffer[3] = 8;

    let serviceDataUnit1: ble.ServiceData = {
      serviceUuid: '00001999-0000-1000-8000-00805f9b34fb',
      serviceValue: serviceValueBuffer.buffer
    };
    let serviceDataUnit2: ble.ServiceData = {
      serviceUuid: '19991999-0000-1000-8000-00805f9b34fb',
      serviceValue: serviceValueBuffer.buffer
    };
    let advData: ble.AdvertiseData = {
      serviceUuids: [],
      manufactureData: [
        {
          manufactureId: 0xfff0,
          manufactureValue: manufactureValueBuffer.buffer // 需要通过Uint8Array.buffer获取ArrayBuffer对象
        }
      ],
      serviceData: [],
      includeDeviceName: false // 表示是否携带设备名，可选参数。注意：带上设备名时，容易导致广播报文长度超出31个字节，使得广播启动失败
    };
    let advResponse: ble.AdvertiseData = {
      serviceUuids: [],
      manufactureData: [],
      serviceData: [serviceDataUnit1, serviceDataUnit2]
    };
    // 2.3构造广播启动完整参数AdvertisingParams
    let advertisingParams: ble.AdvertisingParams = {
      advertisingSettings: setting,
      advertisingData: advData, // 注意:广播报文长度不能超过31个字节
      advertisingResponse: advResponse, // 注意:广播报文长度不能超过31个字节
      duration: 0 // 可选参数，若参数大于0，则广播发送一段时间后会停止，但分配的广播资源还在，可重新启动发送
    };

    // 2.4首次启动广播，蓝牙子系统会分配相关资源，包括应用获取到的广播标识ID
    try {
      ble.on('advertisingStateChange', this.onReceiveEvent);
      this.advHandle = await ble.startAdvertising(advertisingParams);
    } catch (err) {
      console.error(`errCode: ${err.code} , errMessage: ${err.message}`);
    };
  }

  aboutToAppear() {
    // 使用UIExtensionAbility：将common.UIAbilityContext替换为common.UIExtensionContext
    const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    reqPermissionsFromUser(permissions, context);
  }

  build() {
    Column() {
      Button(this.message)
        .onClick(() => {
          this.startAdvertising();
        });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```

**须知** 

权限说明：需要在module.json5文件中配置允许应用接入蓝牙并使用蓝牙功能权限[ohos.permission.ACCESS\_BLUETOOTH](../harmonyos-guides/permissions-for-all-user.md#ohospermissionaccess_bluetooth)。

## 常见FAQ

Q：系统蓝牙开关广播接口功能正常，应用数据包未全部发送出去导致后续广播失败。

A：每次开广播都占用一个新通道，没有停的动作，导致所有广播通道达到上限被占满，只需要：

1. 加密数据包按序号分包，以BLE广播包的serviceUuid内容串行发送。
2. 调用startAdvertising发送第一个广播包后，需调用stopAdvertising停掉此通道的广播，再将第二包数据内容通过重新调用startAdvertising接口发送出去，start + stop循环串行调用，完成所有数据包发送。

Q：蓝牙BLE广播报文数据是否有长度限制？

A：[AdvertiseData](../harmonyos-references/js-apis-bluetooth-ble.md#advertisedata)是BLE广播报文数据内容，也可以用作回复扫描请求的广播报文数据内容。当前只支持传统广播，因此报文最大长度为31个字节。注意带上设备名时，容易导致广播报文长度超出31个字节。若携带了所有参数，尤其是携带了蓝牙设备名称，需要注意广播报文长度。
