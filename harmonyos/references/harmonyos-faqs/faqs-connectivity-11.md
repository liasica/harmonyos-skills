---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-11
title: BLE蓝牙调用setCharacteristicChangeNotification接口报错2900007或2900099
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > BLE蓝牙调用setCharacteristicChangeNotification接口报错2900007或2900099
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:16+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:d0ff88fa15466938645fb8e395e8fa71f37b2c29fcde2923842b1a065a667a59
---

## 问题现象

在BLE蓝牙应用开发过程中，调用setCharacteristicChangeNotification接口时出现2900007或2900099报错，该如何排查解决？

## 背景知识

* [2900007](../harmonyos-references/errorcode-bluetoothmanager.md#section2900007-异步接口调用超时)表示接口调用超时。当client端向server端发起了请求，在一定时间内（约10s）client端没有收到server端的应答，client端就会返回此错误码。
* [2900099](../harmonyos-references/errorcode-bluetoothmanager.md#section2900099-操作失败)表示接口调用操作失败。一般接口调用阻塞，会返回此错误码。
* [setCharacteristicChangeNotification](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangenotification)接口提供了client端启用或者禁用接收server端特征值内容变更通知的能力，使用前需仔细阅读接口下方说明。
* 调用setCharacteristicChangeNotification接口后，底层会默认通过描述符的形式向server端写入一次数据请求，server端可通过[descriptorWrite](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)接收请求，然后调用[sendResponse](../harmonyos-references/js-apis-bluetooth-ble.md#sendresponse)接口向client返回数据，client成功接收到数据后，即一个完整的setCharacteristicChangeNotification接口请求流程才算完毕。

## 问题定位

* 排查server端（server端以HarmonyOS NEXT设备为例）是否创建了[on('descriptorWrite')](../harmonyos-references/js-apis-bluetooth-ble.md#ondescriptorwrite)监听。若server端没有创建此监听，将无法接收到client端发来的描述符请求，client端setCharacteristicChangeNotification接口将会处于持续请求的阻塞状态。
* 排查server端接收到client端发来的描述符请求后，是否及时应答（检查日志是否返回OnSetNotifyCharacteristic关键字）。若server端在接收到client端发来的描述符请求后没有及时调用sendResponse接口应答，client端setCharacteristicChangeNotification接口同样会处于持续请求的阻塞状态。参考错误日志如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/iNrPk0dCTO6zjXpGymxLtA/zh-cn_image_0000002628772390.png "点击放大")

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/mn8OQM3dR9-lJ5YQzCOTUg/zh-cn_image_0000002658971711.png "点击放大")
* 检查client端调用setCharacteristicChangeNotification接口时，是否有其它异步接口调用未完成，导致setCharacteristicChangeNotification接口调用被阻塞。排查方式如下：
  + 通过在接口回调中设置日志打印，查看接口调用的完整顺序流程。从创建对象实例到数据传输，BLE蓝牙client端接口调用顺序参考如下：
    1. 调用[createGattClientDevice](../harmonyos-references/js-apis-bluetooth-ble.md#blecreategattclientdevice)接口创建client实例。
    2. 创建BLE蓝牙连接状态监听、MTU变化监听、特征值变化监听等接口。
    3. 调用[connect](../harmonyos-references/js-apis-bluetooth-ble.md#connect)接口连接BLE蓝牙。
    4. 调用[setBLEMtuSize](../harmonyos-references/js-apis-bluetooth-ble.md#setblemtusize)接口协商MTU。
    5. 调用[getServices](../harmonyos-references/js-apis-bluetooth-ble.md#getservices-1)接口获取server端支持的所有服务能力。
    6. 调用setCharacteristicChangeNotification接口设置server端特征值内容变更通知的能力。
    7. 调用[writeCharacteristicValue](../harmonyos-references/js-apis-bluetooth-ble.md#writecharacteristicvalue)接口向server端写入特征值数据。
  + 排查系统日志输出。可在问题复现后[生成hilog日志](../harmonyos-guides/hilog.md#hilog日志生成)，查看日志中各接口调用开始/完成时，系统日志输出的时间点，从而判断是否出现了接口调用阻塞情况。

    如：setCharacteristicChangeNotification接口调用开始时，系统日志中会打印出关键字setCharacteristicChangeNotification。接口调用完成时，可通过setCharacteristicChangeNotification接口Callback回调中自定义的日志进行判断。参考问题日志如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/VtNh2PY6SjqQmdUO9aGXwQ/zh-cn_image_0000002628612500.png "点击放大")

## 分析结论

* server端没有创建on('descriptorWrite')监听，或接收到client端发来的描述符请求后，没有及时应答。
* 在调用setCharacteristicChangeNotification接口前一般会先调用setBLEMtuSize异步接口，与server端协商MTU数据传输大小。然后再调用getServices接口，获取server端的特征值服务列表。

  因此，需要在setBLEMtuSize和getServices接口依次调用成功后，才可以调用setCharacteristicChangeNotification接口，设置接收server端特征值内容变更通知的能力。

## 修改建议

* client端调用setCharacteristicChangeNotification接口前，需开启server端订阅client的描述符写请求事件监听，同时在接收到描述符请求后，及时做出消息回复。
* 可对setBLEMtuSize、getServices和setCharacteristicChangeNotification接口调用顺序进行修改，并添加MTU变更事件监听，同时通过一一赋值的方式创建characteristic对象。

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

## 常见FAQ

Q：BLE蓝牙writeCharacteristicValue接口写入数据时，2900099报错是什么原因？

A：关于BLE写入数据报错2900099，有如下原因：

* 当上一个非监听类BLE蓝牙接口（setBLEMtuSize、getServices和setCharacteristicChangeNotification）回调还未返回时写入数据，会出现2900099报错提示，导致写入数据失败。因此，需要保证在其它非监听类BLE接口回调触发完成后，再调用writeCharacteristicValue接口写入数据。
* 每次重连GATT设备时都会重新创建新的gattClient对象，建立一路新的GATT连接。若每次连接关闭后不及时调用[close](../harmonyos-references/js-apis-bluetooth-ble.md#close-1)接口销毁gattClient对象实例，则会导致每次重连时重复多次调用setCharacteristicChangeNotification和getService，出现busy现象，进而导致报错2900099。因此，每次连接关闭后，需及时销毁gattClient对象。
* 参数错误，系统日志会同时打印Invalid parameters，需要排查是否按GATT规范传入了正确的[BLECharacteristic](../harmonyos-references/js-apis-bluetooth-ble.md#blecharacteristic)。

Q：一个setCharacteristicChangeNotification接口能否同时设置多个特征值服务？

A：一个setCharacteristicChangeNotification只能设置一个特征值服务变更通知，如果需要对多个特征值服务进行设置，需要多次调用setCharacteristicChangeNotification接口。

Q：早期存量设备没有描述值不能提供descriptors字段，怎么调用setCharacteristicChangeNotification接口呢？

A：descriptor可以传入[]空列表调用setCharacteristicChangeNotification接口。
