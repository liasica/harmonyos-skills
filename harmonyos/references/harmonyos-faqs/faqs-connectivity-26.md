---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-26
title: 如何解决BLE蓝牙广播报文长度超出31字节
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何解决BLE蓝牙广播报文长度超出31字节
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a898ed38f22075f5338a73c15b5be9da8a8cacd4ab761c9c75785f18071a7178
---

## 问题现象

BLE蓝牙广播，如果设置携带设备名就发不了13条serviceUuids数据，应该怎么在携带设备名称和发送13条serviceUuids数据之间做取舍？

问题代码示例参考如下：

```ts
import { ble } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const TAG: string = 'BleAdvertisingManager';

export class BleAdvertisingManager {
  private advHandle: number = 0xFF;

  // 1.定义广播状态上报事件
  onReceiveEvent = (data: ble.AdvertisingStateChangeInfo) => {
    AppStorage.setOrCreate('advertiserState', data.state);
  };

  // 2.首次启动广播
  public async startAdvertising() {
    // 2.1设置广播发送的参数
    let setting: ble.AdvertiseSetting = {
      interval: 160,
      txPower: 0,
      connectable: true,
    };
    // 2.2构造广播数据
    let manufactureValueBuffer = new Uint8Array();
    manufactureValueBuffer[0] = 1;
    manufactureValueBuffer[1] = 2;
    manufactureValueBuffer[2] = 3;
    manufactureValueBuffer[3] = 4;

    let serviceValueBuffer = new Uint8Array(4);
    serviceValueBuffer[0] = 5;
    serviceValueBuffer[1] = 6;
    serviceValueBuffer[2] = 7;
    serviceValueBuffer[3] = 8;
    let manufactureDataUnit: ble.ManufactureData = {
      manufactureId: 4567,
      manufactureValue: manufactureValueBuffer.buffer
    };
    let serviceDataUnit1: ble.ServiceData = {
      serviceUuid: "0000181A-0000-1000-8000-00805F9B34FB",
      serviceValue: serviceValueBuffer.buffer
    };
    let serviceDataUnit2: ble.ServiceData = {
      serviceUuid: "19991999-0000-1000-8000-00805f9b34fb",
      serviceValue: serviceValueBuffer.buffer
    };
    let advData: ble.AdvertiseData = {
      serviceUuids: [
        "000008F0-0000-1000-8000-00805F9B34FB",
        "00000810-0000-1000-8000-00805F9B34FB",
        "00009D13-0000-1000-8000-00805F9B34FB",
        "0000950E-0000-1000-8000-00805F9B34FB",
        "00004E2D-0000-1000-8000-00805F9B34FB",
        "000041F0-0000-1000-8000-00805F9B34FB",
        "00001DE1-0000-1000-8000-00805F9B34FB",
        "00007EB9-0000-1000-8000-00805F9B34FB",
        "0000F59C-0000-1000-8000-00805F9B34FB",
        "00002D98-0000-1000-8000-00805F9B34FB",
        "0000343D-0000-1000-8000-00805F9B34FB",
        "00002B0B-0000-1000-8000-00805F9B34FB",
        "00002D89-0000-1000-8000-00805F9B34FB"
      ],
      manufactureData: [],
      serviceData: [],
    };

    // 2.3构造广播启动完整参数AdvertisingParams
    let advertisingParams: ble.AdvertisingParams = {
      advertisingSettings: setting,
      advertisingData: advData, // 注意:广播报文长度不能超过31个字节
      advertisingResponse: advData, // 注意:广播报文长度不能超过31个字节
      duration: 0 // 可选参数，若参数大于0，则广播发送一段时间后会停止，但分配的广播资源还在，可重新启动发送
    }

    // 2.4首次启动广播，蓝牙子系统会分配相关资源，包括应用获取到的广播标识ID
    try {
      ble.on('advertisingStateChange', this.onReceiveEvent);
      this.advHandle = await ble.startAdvertising(advertisingParams);
    } catch (err) {
      console.error(TAG, 'err');
    }
  }
```

## 背景知识

* 启动发送BLE广播报文[ble.startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising11)方法中，[AdvertisingParams](../harmonyos-references/js-apis-bluetooth-ble.md#advertisingparams11)参数中的[AdvertiseData](../harmonyos-references/js-apis-bluetooth-ble.md#advertisedata)是描述BLE广播报文数据内容，也可以用作回复扫描请求的广播报文数据内容。当前只支持传统广播，因此报文最大长度为31个字节。若超出最大长度（31个字节）限制，会导致启动广播失败。若携带了所有参数，尤其是携带了蓝牙设备名称，需要注意广播报文长度。
* UUID类型有16字节、4字节、2字节三种：

  0000xxxx-0000-1000-8000-00805f9b34fb：2字节。

  xxxxxxxx-0000-1000-8000-00805f9b34fb：4字节。

  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx：16字节。

## 问题定位

根据问题代码中的serviceUuids可以发现，1条serviceUuid是2字节，13条就是26字节。如果广播要携带设备名，占用的字节数取决于设置界面的蓝牙名称的总长度，问题中的设备名"XXXX XXPro"占用10个字节，因此会超出最大长度（31个字节）限制，会导致启动广播失败。

## 分析结论

启动广播失败是因为超出了报文最大长度，serviceUuid可以在连接之后服务发现的时候获取，不一定要在广播的时候全都带上。

服务发现流程：[getServices](../harmonyos-references/js-apis-bluetooth-ble.md#getservices-1)，client获取server端支持的所有服务能力。获取返回的结构体[GattService](../harmonyos-references/js-apis-bluetooth-ble.md#gattservice)中会有所有的serviceUuid。

## 修改建议

如果一定要在广播时设置携带设备名，建议减少serviceUuid的条数，后续在服务发现流程获取serviceUuid。
