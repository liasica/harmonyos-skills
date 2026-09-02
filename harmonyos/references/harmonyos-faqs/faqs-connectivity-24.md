---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-24
title: 如何解决蓝牙/星闪协商MTU参数失败的问题
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何解决蓝牙/星闪协商MTU参数失败的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:d59faffe3c6c39714af41a167a17657996db2dc0622b3c2cda32128c96d0fcea
---

## 问题现象

在蓝牙/星闪功能开发过程中，协商MTU时，有时会出现[2900099](../harmonyos-references/errorcode-bluetoothmanager.md#section2900099-操作失败)/[1009700099](../harmonyos-references/errorcode-nearlink.md#section1009700099)错误的问题，该如何解决？

## 背景知识

* BLE蓝牙提供了[setBLEMtuSize](../harmonyos-references/js-apis-bluetooth-ble.md#setblemtusize)接口用于client端同server端协商MTU（最大传输单元，取值范围23~517）大小。
* 星闪提供了[requestMtuSize](../harmonyos-references/nearlink-ssap.md#requestmtusize)接口用于client端同server端协商MTU（最大传输单元，取值范围22~512）大小。
* 蓝牙/星闪同server端协商MTU前，需要保证client端同server端处于连接的状态。

## 问题定位

* 排查在协商MTU前，蓝牙/星闪client端同server端是否断开了连接。
* 检查协商的MTU参数范围是否合理。

## 分析结论

* 结论一：setBLEMtuSize/requestMtuSize接口调用时机不对，需要在蓝牙/星闪client端和server端连接成功后，才能调用setBLEMtuSize/requestMtuSize接口协商MTU参数。
* 结论二：协商的MTU参数设置不在取值范围内。

## 修改建议

协商MTU前，需保证client端同server端处于连接的状态，且协商的MTU参数需要设置在取值范围内。蓝牙/星闪端代码参考如下：

```ts
import { ble, constant } from '@kit.ConnectivityKit';
import { ssap } from '@kit.NearLinkKit';

@Entry
@Component
struct BleAndSsapSetMtu {
  @State gattClient: ble.GattClientDevice | undefined = undefined;
  @State ssapClient: ssap.Client | undefined = undefined;

  // 设置ble端mtu
  setBleMtu() {
    // 创建client端实例，bleMac为server端虚拟mac地址，需要提前获取
    this.gattClient = ble.createGattClientDevice('bleMac');
    // 订阅ble蓝牙连接状态监听事件
    this.onBLEConnectionStateChange();
    // 订阅MTU协商结果监听事件
    this.BLEMtuChange();
    // 连接server端ble蓝牙
    this.gattClient.connect();
  }

  onBLEConnectionStateChange() {
    this.gattClient?.on('BLEConnectionStateChange', (state: ble.BLEConnectionChangeState) => {
      // state.state返回结果为2时，表示client端同server端成功建立了连接。
      if (state.state === constant.ProfileConnectionState.STATE_CONNECTED) {
        // 调用setBLEMtuSize接口，同server端协商MTU，参数取值范围23~517。
        this.gattClient?.setBLEMtuSize(128);
      }
    });
  }

  BLEMtuChange() {
    this.gattClient?.on('BLEMtuChange', (mtu: number) => {
      // MTU协商结果监听回调，回调触发，表示协商成功。
      console.info(`BLEMtuChange, mtu: ${mtu}`);
    });
  }

  // 设置星闪端mtu
  setSsapMtu() {
    // 创建client端实例，ssapMac为server端虚拟mac地址，需要提前获取
    this.ssapClient = ssap.createClient('ssapMac');
    // 订阅ble蓝牙连接状态监听事件
    this.onConnectionStateChange();
    // 订阅MTU协商结果监听事件
    this.ssapMtuChange();
    // 连接server端ble蓝牙
    this.ssapClient.connect();
  }

  onConnectionStateChange() {
    this.ssapClient?.on('connectionStateChange', (state: ssap.ConnectionChangeState) => {
      // state.state返回结果为1时，表示client端同server端成功建立了连接。
      if (state.state === 1) {
        // 调用requestMtuSize接口，同server端协商MTU，参数取值范围22~512，默认值为256字节。
        this.ssapClient?.requestMtuSize(128);
      }
    });
  }

  ssapMtuChange() {
    this.ssapClient?.on('mtuChange', (mtu: number) => {
      // MTU协商结果监听回调，回调触发，表示协商成功。
      console.info(`mtuChange, mtu:  ${mtu}`);
    });
  }

  build() {
    Column() {
      Button('连接ble蓝牙，并协商MTU').onClick(() => {
        // 连接ble蓝牙，并协商MTU
        this.setBleMtu();
      }).margin(15);

      Button('连接星闪，并协商MTU').onClick(() => {
        // 连接星闪，并协商MTU
        this.setSsapMtu();
      });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```

## 常见FAQ

Q：在BLE蓝牙开发流程中，setBLEMtuSize()接口在什么时候调用最合适？

A：setBLEMtuSize()方法只能在调用[connect()](../harmonyos-references/js-apis-bluetooth-ble.md#connect)接口成功连接上蓝牙之后调用。建议在调用[getServices()](../harmonyos-references/js-apis-bluetooth-ble.md#getservices)接口获取server端支持的所有服务能力之前调用。
