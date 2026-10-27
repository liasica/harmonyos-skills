---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/connectivity-kit-troubleshooting-0001
title: BLE蓝牙数据传输与广播报错问题排查
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 故障排查 > BLE蓝牙数据传输与广播报错问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:18+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:bfa379a6f83b76a040bed02457fd3f0e4e10b755ad34706024dc66e611df0ab3
---

## BLE蓝牙客户端连接后无法接收服务端广播数据

### 问题现象

BLE蓝牙服务端和客户端连接成功后，客户端收到服务端约30次数据后停止接收。

### 定位过程

定位思路：

先排查服务端是否正常广播数据，以下日志表示服务端广播日志正常打印：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/UENzDqZ1TXq4_eeWTEs2tg/zh-cn_image_0000002795167129.png "点击放大")

再排查客户端是否正常接收数据，发现客户端BLECharacteristicChanges事件回调日志打印到第30次后结束打印。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/KlFcaEIWSs-7x8F1kd0yUQ/zh-cn_image_0000002795167133.png "点击放大")

蓝牙中的Hilog日志显示客户端NotifyCallback同样只执行30次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/er4M-L1JSninU9cBSP-NmQ/zh-cn_image_0000002765608640.png "点击放大")

翻看BLE蓝牙服务端文档发现，当服务端收到写入描述符请求时，根据写入请求[DescriptorWriteRequest](../harmonyos-references/js-apis-bluetooth-ble.md#descriptorwriterequest)的needRsp判断是否需要调用[sendResponse](../harmonyos-references/js-apis-bluetooth-ble.md#sendresponse)进行回复。

根据文档说明可知，服务端需要订阅客户端的描述符写请求事件，即server.on('descriptorWrite')，当客户端发起写入描述符请求事件[descriptorWrite](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)时，可通过在服务端监听descriptorWrite事件，并在回调中回复客户端。

### 分析结论

根据分析以上定位过程可知，造成客户端无法接收服务端广播数据的原因是服务端没有监听客户端发起写入描述符请求事件[descriptorWrite](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)。

### 修改建议

服务端在数据传输阶段[监听descriptorWrite事件](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)。

验证结果可以看出客户端的BLECharacteristicChange回调函数已经持续执行超过30次。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/w1AYjimQTpqbxeYceaGInA/zh-cn_image_0000002765769036.png "点击放大")

## BLE蓝牙调用setCharacteristicChangeNotification接口报错2900007或2900099

### 问题现象

在BLE蓝牙应用开发过程中，调用setCharacteristicChangeNotification接口时出现2900007或2900099报错，该如何排查解决？

### 定位过程

* 排查server端（server端以HarmonyOS NEXT设备为例）是否创建了[on('descriptorWrite')](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)监听。若server端没有创建此监听，将无法接收到client端发来的描述符请求，client端setCharacteristicChangeNotification接口将会处于持续请求的阻塞状态。
* 排查server端接收到client端发来的描述符请求后，是否及时应答（检查日志是否返回OnSetNotifyCharacteristic关键字）。若server端在接收到client端发来的描述符请求后没有及时调用sendResponse接口应答，client端setCharacteristicChangeNotification接口同样会处于持续请求的阻塞状态。参考错误日志如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/sGBJ_iEBRT-2NFDddK_Mww/zh-cn_image_0000002795048421.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/4t3jBDahS9ujb-qNZamw2g/zh-cn_image_0000002795048477.png "点击放大")
* 检查client端调用setCharacteristicChangeNotification接口时，是否有其它异步接口调用未完成，导致setCharacteristicChangeNotification接口调用被阻塞。排查方式如下：
  + 通过在接口回调中设置日志打印，查看接口调用的完整顺序流程。从创建对象实例到数据传输，BLE蓝牙client端接口调用顺序参考如下：
    1. 调用[createGattClientDevice](../harmonyos-references/js-apis-bluetooth-ble.md#blecreategattclientdevice)接口创建client实例。
    2. 创建BLE蓝牙连接状态监听、MTU变化监听、特征值变化监听等接口。
    3. 调用[connect](../harmonyos-references/js-apis-bluetooth-ble.md#connect)接口连接BLE蓝牙。
    4. 调用[setBLEMtuSize](../harmonyos-references/js-apis-bluetooth-ble.md#setblemtusize)接口协商MTU。
    5. 调用[getServices](../harmonyos-references/js-apis-bluetooth-ble.md#getservices-1)接口获取server端支持的所有服务能力。
    6. 调用[setCharacteristicChangeNotification](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangenotification)接口设置server端特征值内容变更通知的能力。
    7. 调用[writeCharacteristicValue](../harmonyos-references/js-apis-bluetooth-ble.md#writecharacteristicvalue)接口向server端写入特征值数据。
  + 排查系统日志输出。可在问题复现后[生成hilog日志](../harmonyos-guides/hilog.md#hilog日志生成)，查看日志中各接口调用开始/完成时，系统日志输出的时间点，从而判断是否出现了接口调用阻塞情况。

    如：setCharacteristicChangeNotification接口调用开始时，系统日志中会打印出关键字setCharacteristicChangeNotification。接口调用完成时，可通过setCharacteristicChangeNotification接口Callback回调中自定义的日志进行判断。参考问题日志如下：![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/2bxd_5EfS8GRQDEdysohEw/zh-cn_image_0000002765769698.png "点击放大")

### 分析结论

* server端没有创建on('descriptorWrite')监听，或接收到client端发来的描述符请求后，没有及时应答。
* 在调用setCharacteristicChangeNotification接口前一般会先调用[setBLEMtuSize](../harmonyos-references/js-apis-bluetooth-ble.md#setblemtusize)异步接口，与server端协商MTU数据传输大小。然后再调用getServices接口，获取server端的特征值服务列表。因此，需要在setBLEMtuSize和getServices接口依次调用成功后，才可以调用setCharacteristicChangeNotification接口，设置接收server端特征值内容变更通知的能力。

### 修改建议

* client端调用setCharacteristicChangeNotification接口前，需开启server端订阅client的描述符写请求事件监听，同时在接收到描述符请求后，及时做出消息回复。
* 可对setBLEMtuSize、getServices和setCharacteristicChangeNotification接口调用顺序进行修改，并添加MTU变更事件监听，同时通过一一赋值的方式创建characteristic对象，参考代码如下：

  ```ts
  import { ble, constant } from '@kit.ConnectivityKit';
  import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct setCharacteristicChangeNotification {
    @State gattClient: ble.GattClientDevice | undefined = undefined;

    aboutToAppear(): void {
      let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
      atManager.requestPermissionsFromUser(this.getUIContext()?.getHostContext() as common.UIAbilityContext,
        ['ohos.permission.ACCESS_BLUETOOTH'], (err: BusinessError, data: PermissionRequestResult) => {
          if (err) {
            console.error(`requestPermissionsFromUser fail, err->${JSON.stringify(err)}`);
          } else {
            console.info(`data:${JSON.stringify(data)}`);
          }
        });
    }

    connect() {
      // 创建client端实例，server端虚拟mac地址,使用时,需要根据实际进行修改
      try {
        this.gattClient = ble.createGattClientDevice('deviceMAC');
      } catch (error) {
        console.error(`createGattClientDevice error:${error}`);
      }
      // 订阅ble蓝牙连接状态监听事件
      this.onBLEConnectionStateChange();
      // 订阅MTU监听事件
      this.BLEMtuChange();
      // 连接server端ble蓝牙
      try {
        this.gattClient?.connect();
      } catch (error) {
        console.error(`connect error:${error}`);
      }
    }

    onBLEConnectionStateChange() {
      try {
        this.gattClient?.on('BLEConnectionStateChange', (state: ble.BLEConnectionChangeState) => {
          if (state.state === constant.ProfileConnectionState.STATE_CONNECTED) {
            // 连接成功，先与server协商MTU，参数范围23~517
            try {
              this.gattClient?.setBLEMtuSize(128);
            } catch (error) {
              console.error(`error:${JSON.stringify(error)}`);
            }
          }
        });
      } catch (error) {
        console.error(`on BLEConnectionStateChange error:${error}`);
      }
    }

    BLEMtuChange() {
      try {
        this.gattClient?.on('BLEMtuChange', (mtu: number) => {
          // MTU协商成功,调用getServices接口获取server服务。
          console.info(`协商成功,mtu参数为:${mtu}`);
          this.getServices();
        });
      } catch (error) {
        console.error(`on BLEMtuChange error:${error}`);
      }
    }

    getServices() {
      this.gattClient?.getServices().then((result: Array<ble.GattService>) => {
        result.filter(item => {
          // 筛选出指定特征值服务，并设置通知变更能力。
          // server端指定服务uuid,使用时,需要根据实际进行修改
          if (item.serviceUuid === 'uuid') {
            let descriptors: Array<ble.BLEDescriptor> = [];
            let arrayBuffer = new ArrayBuffer(8);
            let descV = new Uint8Array(arrayBuffer);
            descV[0] = 11;
            let arrayBufferC = new ArrayBuffer(8);
            // 通过一一赋值的方式创建characteristic对象
            let characteristic: ble.BLECharacteristic = {
              serviceUuid: item.serviceUuid,
              characteristicUuid: item.characteristics[0].characteristicUuid,
              characteristicValue: arrayBufferC,
              descriptors: descriptors
            };
            this.gattClient?.setCharacteristicChangeNotification(characteristic, true, (err: BusinessError) => {
              if (err) {
                console.error('notifyCharacteristicChanged callback failed');
              } else {
                console.info('notifyCharacteristicChanged callback successful');
              }
            });
          }
        });
      }).catch((error: BusinessError) => {
        console.error(`getServices error:${error}`);
      });
    }

    build() {
      Column() {
        Button('连接BLE蓝牙，并发起请求')
          .onClick(() => {
            // 连接BLE蓝牙，并发起setCharacteristicChangeNotification请求
            this.connect();
          });
      }.height('100%')
      .width('100%')
      .justifyContent(FlexAlign.SpaceAround);
    }
  }
  ```

  **说明** 

  使用蓝牙能力时，需要在module.json5中添加ohos.permission.ACCESS\_BLUETOOTH权限。

## BLE蓝牙广播startAdvertising报错401问题

### 问题现象

使用BLE蓝牙广播[startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising11)出现如下报错：

```ts
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

### 定位过程

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

### 分析结论

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

### 修改建议

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

**说明** 

权限说明：需要在module.json5文件中配置允许应用接入蓝牙并使用蓝牙功能权限[ohos.permission.ACCESS\_BLUETOOTH](../harmonyos-guides/permissions-for-all-user.md#ohospermissionaccess_bluetooth)。
