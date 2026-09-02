---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-10
title: BLE连接成功后状态监听会回调2次
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > BLE连接成功后状态监听会回调2次
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f60f4aea1eb6d6bcfd5c23fe3d9d126436c91c32b4b972ebc1e2657bdcf7f225
---

## 问题现象

BLE连接状态监听会触发两次回调。

问题代码示例参考如下：

```ts
bleConnect(deviceId: string): void {
  try {
    this.gattClient = ble.createGattClientDevice(deviceId);
    this.gattClient.connect();
    this.gattClient.on('BLEConnectionStateChange', (state: ble.BLEConnectionChangeState) => {
      if (state) {
        console.info('连接成功了');
        this.getUIContext().getPromptAction().showToast({ message: '连接成功了！' });
        this.getServices();
      }
    });
  } catch (err) {
    console.error(`errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
  }
}
```

## 背景知识

* [on('BLEConnectionStateChange')](../harmonyos-references/js-apis-bluetooth-ble.md#onbleconnectionstatechange)：client端订阅GATT profile协议的连接状态变化事件。当client和server端之间的连接状态发生变化时，触发该事件。
* [ProfileConnectionState](../harmonyos-references/js-apis-bluetooth-constant.md#profileconnectionstate)：枚举，本端和对端蓝牙设备间的Profile连接状态。

## 问题定位

状态监听API的回调场景如下：

1. 打开蓝牙连接。

   当回调状态为1时表示正在连接，当状态返回2时表明已连接，所以是两次回调。

   打印示例：

   ```txt
   04-25 16:18:56.483   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage bluetooth connect state changed
   04-25 16:18:56.483   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage deviceId connectState 98:92:1A:03:BF:4B
   04-25 16:18:56.483   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage bluetooth connectState 1
   04-25 16:18:59.117   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage bluetooth connect state changed
   04-25 16:18:59.117   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage deviceId connectState 98:92:1A:03:BF:4B
   04-25 16:18:59.118   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage bluetooth connectState 2
   ```
2. 关闭蓝牙连接。

   当回调状态为3时表示正在断连，当状态返回0时表明已断开，所以是两次回调。

   打印示例：

   ```txt
   04-25 16:18:03.065   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage bluetooth connect state changed
   04-25 16:18:03.065   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage deviceId connectState 98:92:1A:03:BF:4B
   04-25 16:18:03.065   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage bluetooth connectState 3
   04-25 16:18:03.078   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage bluetooth connect state changed
   04-25 16:18:03.078   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage deviceId connectState 98:92:1A:03:BF:4B
   04-25 16:18:03.078   41735-41735   A03D00/com.example.ble/JSAPP    com.example.ble       I     BluetoothPage bluetooth connectState 0
   ```

以上两种场景每次回调代表1种状态的返回。开发者可以根据不同的状态触发对应的业务。

## 分析结论

依据业务需要添加状态判断再触发别的业务。

## 修改建议

依据ProfileConnectionState在对应的状态下再执行自己的业务。

完整性案例参考官方示例[低功耗设备蓝牙扫描与连接](../architecture-guides/search_and_connect_ble-0000002293947117.md)，依据真实设备可查看on('BLEConnectionStateChange')具体状态变化。
