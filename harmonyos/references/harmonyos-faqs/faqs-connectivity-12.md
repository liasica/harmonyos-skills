---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-12
title: 如何实现BLE蓝牙快速回连
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何实现BLE蓝牙快速回连
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:16+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:8c669db2df68c68e243c2a8d363a8b43333c8ea0b7c091b06f2ef5f6b04e3e48
---

## 问题现象

如果应用已经与对端蓝牙设备建立过BLE蓝牙连接，那么如何不通过蓝牙扫描，就能够与之前已连接过的蓝牙设备快速建立连接？

## 背景知识

* 在HarmonyOS中，若设备A与B没有建立配对，则它们的蓝牙虚拟MAC地址会随着开关机等操作发生改变。若设备A与设备B后建立了蓝牙配对，则它们的蓝牙虚拟MAC地址会被固化，即使设备开关机，蓝牙虚拟MAC地址也不会发生改变。
* API16及后续版本，HarmonyOS提供了无需配对就可将蓝牙虚拟MAC地址固化的API接口：[addPersistentDeviceId](../harmonyos-references/js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)。由于应用通过蓝牙扫描获取到未配对或未固化的设备MAC地址是虚拟随机的，若想该虚拟随机地址不发生改变，可以调用addPersistentDeviceId接口持久化存储虚拟随机地址。**注意**：
  1. 使用蓝牙虚拟MAC地址固化API需要使用到[ohos.permission.PERSISTENT\_BLUETOOTH\_PEERS\_MAC](../harmonyos-guides/restricted-permissions.md#ohospermissionpersistent_bluetooth_peers_mac)权限，且需要[ACL](../app/agc-help-apply-acl-0000002394212138.md)权限申请通过后方可使用。
  2. 使用该接口时，开发者应明确该虚拟随机地址对应的对端蓝牙设备真实地址是不变的，若对端设备地址发生变化，持久化保存的地址信息也会失效，无法继续使用。

## 解决方案

* 方案一：与对端设备第一次连接后，发起[蓝牙配对](../harmonyos-references/js-apis-bluetooth-connection.md#connectionpairdevice-1)，配对完成后，蓝牙虚拟MAC地址会被固化。后续无需重复建立蓝牙扫描，调用[getPairedDevices](../harmonyos-references/js-apis-bluetooth-connection.md#connectiongetpaireddevices)接口就可以从已配对列表中获取对端蓝牙的虚拟MAC地址，向对端设备发起连接。
* 方案二：与对端设备第一次连接后，使用[addPersistentDeviceId](../harmonyos-references/js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)接口固化对端设备虚拟MAC地址。后续同样无需重复建立蓝牙扫描，调用[getPersistentDeviceIds](../harmonyos-references/js-apis-bluetooth-access.md#accessgetpersistentdeviceids16)接口就可以从已固化设备列表中获取对端蓝牙的虚拟MAC地址，向对端设备发起连接。

方案一、方案二完整代码如下：

```ts
import { access, ble, connection, constant } from '@kit.ConnectivityKit';

@Entry
@Component
struct Reconnect {
  @State gattClient: ble.GattClientDevice | undefined = undefined;

  // 方案一
  ReconnectOne() {
    // 先查询已配对设备列表，判断需要连接的设备是否在已配对设备列表中存在。
    let devices = connection.getPairedDevices();
    for (let index = 0; index < devices.length; index++) {
      let name = connection.getRemoteDeviceName(devices[index]);
      // 需要连接的设备在已配对设备列表中存在，无需发起扫描，直接创建实例进行连接。
      if (name === 'name') {
        // 创建ble蓝牙client实例
        this.gattClient = ble.createGattClientDevice(devices[index]);
        // 连接前先创建连接状态回调监听
        this.onBLEConnectionStateChangeOne();
        // 连接ble蓝牙
        this.gattClient.connect();
        return;
      }
    }
    // 需要连接的设备在已配对设备列表中不存在，开启常规ble蓝牙连接流程。
    // 订阅BLE设备发现
    this.onBLEDeviceFindOne();
    // 过滤参数可根据实际场景进行设置
    let scanFilter: ble.ScanFilter = {
      name: 'name'
    };
    // 扫描参数可根据实际场景配置
    let scanOptions: ble.ScanOptions = {
      interval: 500,
      dutyMode: ble.ScanDuty.SCAN_MODE_LOW_POWER,
      matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE,
    };
    ble.startBLEScan([scanFilter], scanOptions);
  }

  onBLEDeviceFindOne() {
    ble.on('BLEDeviceFind', (data: Array<ble.ScanResult>) => {
      // 发现设备，创建实例进行连接。
      this.gattClient = ble.createGattClientDevice(data[0].deviceId);
      // 连接前先创建连接状态回调监听
      this.onBLEConnectionStateChangeOne();
      // 连接ble蓝牙
      this.gattClient.connect();
      // 连接成后，将已连接设备加入配对列表。
      // 注意：加入配对列表时机并不固定，可根据实际场景来进行变更。
      connection.pairDevice(data[0].deviceId, () => {
        console.info('pairDevice err');
      });
    });
  }

  onBLEConnectionStateChangeOne() {
    this.gattClient?.on('BLEConnectionStateChange', (state: ble.BLEConnectionChangeState) => {
      if (state.state === constant.ProfileConnectionState.STATE_DISCONNECTED) {
        // 如果蓝牙意外断开了连接，可以在此处重新发起连接，以达到意外断连快速回连能力。
        // 不过需要保证此时this.gattClient实例没有被销毁。
        this.gattClient?.connect();
      }
    });
  }

  // 方案二
  ReconnectTwo() {
    // 先查询已固化设备列表，判断需要连接的设备是否在已固化设备列表中存在。
    let devices = access.getPersistentDeviceIds();
    for (let index = 0; index < devices.length; index++) {
      let name = connection.getRemoteDeviceName(devices[index]);
      let isValid = access.isValidRandomDeviceId(devices[index]);
      // 需要连接的设备在已固化设备列表中存在，同时该地址有效，无需发起扫描，直接创建实例进行连接。
      if (isValid && name === 'name') {
        // 创建ble蓝牙client实例
        this.gattClient = ble.createGattClientDevice(devices[index]);
        // 连接前先创建连接状态回调监听
        this.onBLEConnectionStateChangeTwo();
        // 连接ble蓝牙
        this.gattClient.connect();
        return;
      }
    }
    // 需要连接的设备在已固化设备列表中不存在，开启常规ble蓝牙连接流程。
    // 订阅BLE设备发现
    this.onBLEDeviceFindTwo();
    // 过滤参数可根据实际场景进行设置
    let scanFilter: ble.ScanFilter = {
      name: 'name'
    };
    // 扫描参数可根据实际场景配置
    let scanOptions: ble.ScanOptions = {
      interval: 500,
      dutyMode: ble.ScanDuty.SCAN_MODE_LOW_POWER,
      matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE,
    };
    ble.startBLEScan([scanFilter], scanOptions);
  }

  onBLEDeviceFindTwo() {
    ble.on('BLEDeviceFind', (data: Array<ble.ScanResult>) => {
      // 发现设备，创建实例进行连接。
      this.gattClient = ble.createGattClientDevice(data[0].deviceId);
      // 连接前先创建连接状态回调监听
      this.onBLEConnectionStateChangeTwo();
      // 连接ble蓝牙
      this.gattClient.connect();
      // 连接成后，将已连接设备加入固化列表。
      // 注意：加入固化列表时机并不固定，可根据实际场景来进行变更。
      access.addPersistentDeviceId(data[0].deviceId);
    });
  }

  onBLEConnectionStateChangeTwo() {
    this.gattClient?.on('BLEConnectionStateChange', (state: ble.BLEConnectionChangeState) => {
      if (state.state === constant.ProfileConnectionState.STATE_DISCONNECTED) {
        // 如果蓝牙意外断开了连接，可以在此处重新发起连接，以达到意外断连快速回连能力。
        // 不过需要保证此时this.gattClient实例没有被销毁。
        this.gattClient?.connect();
      }
    });
  }

  build() {
    Column() {
      Button('ble蓝牙连接/支持快速回连(方案1)').onClick(() => {
        // 发起连接
        this.ReconnectOne();
      });
      Button('ble蓝牙连接/支持快速回连(方案2)').onClick(() => {
        // 发起连接
        this.ReconnectTwo();
      });
    }.height('100%')
    .width('100%')
    .justifyContent(FlexAlign.SpaceAround);
  }
}
```

**说明** 

由于方案二需要使用受限开放的ohos.permission.PERSISTENT\_BLUETOOTH\_PEERS\_MAC权限，一般建议使用方案一。若业务中不能包含配对场景，且可以成功申请ohos.permission.PERSISTENT\_BLUETOOTH\_PEERS\_MAC权限，就可以采取方案二。

## 常见FAQ

Q：由于担心蓝牙虚拟MAC地址变化，需要在重新连接前一直扫描，会造成资源消耗，应该如何解决？

A：可以使用[addPersistentDeviceId](../harmonyos-references/js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)持久化蓝牙地址，就不需要在重连前一直扫描。

Q：使用addPersistentDeviceId持久化后，是否即使蓝牙设备关机重启，只要蓝牙物理MAC地址不变，被持久化的虚拟MAC地址也不会发生改变？

A：是的，只要对端蓝牙设备真实地址保持不变，那么被addPersistentDeviceId接口持久化的虚拟MAC地址就不会发生改变。

Q：使用addPersistentDeviceId固化蓝牙虚拟MAC地址后，调用deletePersistentDeviceId删除该地址，再次查询固化列表时发现被删除的地址仍然存在，如何解决？

A：该问题出现在调试阶段，由于应用前后两次签名发生变化，系统未能识别差异，导致固化地址无法正常删除。在正式版本中不会出现此问题。若在调试阶段遇到此问题，可通过"设置>系统>重置>还原网络设置"清除相关数据解决。
