---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-15
title: 如何通过已连接的BLE蓝牙设备的虚拟MAC地址建立经典蓝牙连接
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何通过已连接的BLE蓝牙设备的虚拟MAC地址建立经典蓝牙连接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:18597a8ab4f52d163e1f20aa4395477c5ff018245e001ca18af7ae97915cea08
---

## 问题现象

当周围存在多个名称相同的蓝牙设备时，如何在经典蓝牙的扫描列表中准确识别出当前已通过BLE连接的设备，并进一步建立经典蓝牙连接？

## 背景知识

* 蓝牙技术是一种无线通信技术，可以在短距离内传输数据，目前蓝牙有两种常见的技术分类：传统蓝牙（BR/EDR）和低功耗蓝牙（BLE）。两种类型的蓝牙区分可以参考：[蓝牙服务开发概述](../harmonyos-guides/bluetooth-overview.md)。
* 在BLE蓝牙中，可以通过[ScanFilter](../harmonyos-references/js-apis-bluetooth-ble.md#scanfilter)过滤参数精确找到需要连接的BLE蓝牙设备。
* [经典蓝牙扫描](../harmonyos-references/js-apis-bluetooth-connection.md#connectionstartbluetoothdiscovery)无法配置过滤参数，通常只能通过扫描到的虚拟MAC地址，调用[getRemoteDeviceName](../harmonyos-references/js-apis-bluetooth-connection.md#connectiongetremotedevicename16)接口获取设备名称来确定目标设备。
* 若对端设备同时支持经典蓝牙和BLE蓝牙，通过BLE蓝牙虚拟MAC地址建立蓝牙配对的同时，也会完成经典蓝牙的配对。

## 解决方案

使用已连接的BLE蓝牙设备的虚拟MAC地址调用[pairDevice](../harmonyos-references/js-apis-bluetooth-connection.md#connectionpairdevice)接口发起配对。配对完成后，配对列表中不仅会包含BLE蓝牙的配对信息，还会包含经典蓝牙的配对信息。通过调用[getPairedDevices](../harmonyos-references/js-apis-bluetooth-connection.md#connectiongetpaireddevices)接口，可以直接获取到经典蓝牙的虚拟MAC地址，然后使用这个MAC地址建立经典蓝牙连接。

参考样例代码：

```ts
import socket from '@ohos.bluetooth.socket';
import connection from '@ohos.bluetooth.connection';
import { ble } from '@kit.ConnectivityKit';
import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State bleAddress: string = '';
  name: string = '过滤的设备名称';
  uiContext = this.getUIContext();

  aboutToAppear(): void {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.uiContext?.getHostContext() as common.UIAbilityContext,
      ['ohos.permission.ACCESS_BLUETOOTH'], (err: BusinessError, data: PermissionRequestResult) => {
        if (err) {
          console.error(`requestPermissionsFromUser fail, err->${JSON.stringify(err)}`);
        } else {
          console.info(`data:${JSON.stringify(data)}`);
        }
      });
  }

  connect(deviceId: string) {
    let sppOption: socket.SppOptions = {
      // 这里的uuid地址为socket服务端创建时定义的uuid
      uuid: '0000xxxx-0000-1000-8000-00805f9b34fb',
      secure: true,
      type: 0
    };
    console.info(`准备连接经典蓝牙：${deviceId}`);
    setTimeout(() => {
      socket.sppConnect(deviceId, sppOption, (code, socketID) => {
        console.error(`ConnectSPP: ${code} socketID: ${socketID}`);
      });
    }, 1000);
  }

  pinRequired() {
    connection.on('pinRequired', () => {
      connection.on('bondStateChange', (data: connection.BondStateParam) => {
        console.info(`pair state = ${data}`);
        if (data.state === 2) {
          // 3.配对完成后，重新获取配对列表信息。此刻，配对列表中存在该设备的ble配对信息和经典蓝牙配对信息。
          let devices: Array<string> = connection.getPairedDevices();
          for (let i = 0; i < devices.length; i++) {
            console.info(`已配对mac： ${devices[i]}`);
            let dev: string = devices[i];
            // 4.通过ble蓝牙的mac地址，找出经典蓝牙的mac地址。
            if (dev !== this.bleAddress) {
              let n: string = connection.getRemoteDeviceName(devices[i]);
              console.info(`已配对后开始连接 n: ${n} mac: ${devices[i]}`);
              // 5.通过经典蓝牙mac地址获取设备名称，然后通过这个名称二次匹配，确定设备。
              if (n === this.name) {
                connection.off('bondStateChange');
                // 6.确定设备后，发起经典蓝牙连接。
                this.connect(devices[i]);
              }
            }
          }
        }
      });
    });
    ble.on('BLEDeviceFind', (data) => {
      for (let i = 0; i < data.length; i++) {
        let name: string = data[i].deviceName;
        console.info(`发现设备 ： ${name}，地址为 ： ${data[i].deviceId}`);
        ble.stopBLEScan();
        ble.off('BLEDeviceFind');
        // 发现设备后，先保存设备名称
        this.bleAddress = data[i].deviceId;
        let devices: Array<string> = connection.getPairedDevices();
        let index = devices.indexOf(data[i].deviceId);
        // 2.1查询配对列表，如果该设备未配对，先发起配对。
        if (index < 0) {
          console.info(`准备配对: ${name}`);
          connection.pairDevice(data[i].deviceId).then(() => {
            console.info(`进入配对: ${name}`);
          });
        } else {
          console.info(`已配对: ${name}`);
          // 2.2如果设备已经配对，直接在配对列表中找出设备对端设备的经典蓝牙mac地址，发起连接即可。
          for (let i = 0; i < devices.length; i++) {
            console.info(`已配对mac ${devices[i]} 设备名称： ${name}`);
            let dev: string = devices[i];
            if (dev !== this.bleAddress) {
              let n: string = connection.getRemoteDeviceName(devices[i]);
              console.info(`已配对后开始连接 n: ${n} mac: ${devices[i]}`);
              if (n === name) {
                connection.off('pinRequired');
                this.connect(devices[i]);
              }
            }
          }
        }
      }
    });
    // 1.以设备名称为过滤参数，发起ble扫描，获取对端ble蓝牙mac地址。
    ble.startBLEScan([{
      name: this.name
    }], {
      interval: 500,
      dutyMode: ble.ScanDuty.SCAN_MODE_LOW_POWER,
      matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE,
    });
  }

  build() {
    Column() {
      Button('扫描BLE发起配对-连接经典蓝牙')
        .onClick(() => {
          this.pinRequired();
        });
    }
    .width('100%')
    .height('100%');
  }
}
```

## 常见FAQ

Q：使用connection.pairDevice发起设备配对并成功后，如何通过代码调用取消配对？

A：系统暂时还未对外提供取消蓝牙配对的接口。可以尝试通过进入蓝牙设置页面手动取消配对。

Q：扫描结果中的data:{"0":30,"1":255,"2":34...}如何解析成xxxx-xxxx-xxxx-xxxx的形式？

A：可参考API12[开启、关闭扫描](../harmonyos-guides/ble-development-guide.md#ble扫描流程-1)中parseScanResult函数提供的解析方式。

Q：HarmonyOS中的uuid可以给到其它平台连接用吗？

A：uuid是厂商定义的一个参数，可以给到其它平台连接用。

Q：如何实现长时间监听设备发的消息？

A：可以通过[on('BLECharacteristicChange')](../harmonyos-references/js-apis-bluetooth-ble.md#onblecharacteristicchange)订阅蓝牙低功耗设备的特征值变化事件实现。

Q：应用长期在后台，还在连接设备，进程会不会被系统杀掉？有没有保活的措施？

A：会，可以申请[长时任务](../harmonyos-guides/continuous-task.md)保活蓝牙相关业务。

Q：解决方案中是先通过BLE连接的设备，再进一步建立经典蓝牙连接，是否支持先通过经典蓝牙连接，再建立BLE连接的方式？

A：目前不支持通过先建立经典蓝牙连接，再建立BLE连接的方式。

Q：使用ble.startBLEScan扫描出来的地址可以放到socket.sppConnect中调用吗？

A：不可以，经典蓝牙和BLE蓝牙使用的是不同的扫描方式，扫描出来的地址是不一样的。

Q：socket.sppWrite方法，可以支持的arraybuffer大小长度在什么范围内？

A：最好控制在600字节以下，不建议超过1024字节。

Q：SPP还是GATT两种协议有什么差别，传输大量数据选哪一种？

A：关于SPP和GATT的选择，SPP必须要双端交互才能实现，SPP通常用于传输较大的数据量，因为它支持更高的数据传输速率和更大的数据传输量。GATT则常用于需要低功耗和高频率数据更新的场景，如健康监测设备。因此，如果需要传输大量数据，SPP可能是更合适的选择。

Q：应用已存储真实MAC地址，系统双升单后配对仍存在，设备在已配对情况下不会BLE广播，造成扫描不到广播，如何解决？

A：API 21以下系统可通过手动取消配对；API 21后可支持接口直接传入真实MAC地址操作。

Q：[connection.pairDevice](../harmonyos-references/js-apis-bluetooth-connection.md#connectionpairdevice21)接口在API21支持使用真实地址配对，[connection.connectAllowedProfiles](../harmonyos-references/js-apis-bluetooth-connection.md#connectionconnectallowedprofiles16-1)会同步支持使用真实地址连接设备profile吗？

A：支持，升级API21后可支持接口直接传入真实地址操作。

Q：HarmonyOS是一直支持SPP使用蓝牙设备真实Mac地址连接吗？

A：支持SPP使用蓝牙设备真实Mac地址连接，5.1开始支持的。

Q：ble.startBLEScan()怎么样才能扫描到已配对的蓝牙吗？有什么限制条件吗？

A：ble.startBLEScan()方法扫描到的设备和配不配对没有具体的关系，依赖于对端设备是否发送广播，只要对端配对场景下依然会发广播的话，ble.startBLEScan()就能扫到。例如耳机之类的蓝牙设备，配对之后一般是不再发广播的。

Q：API20及以下的[connection.getPairState()](../harmonyos-references/js-apis-bluetooth-connection.md#connectiongetpairstate11)是否支持传入真实的物理地址?

A：从API21开始支持[connection.getPairState()](../harmonyos-references/js-apis-bluetooth-connection.md#connectiongetpairstate11)传入真实物理地址。
