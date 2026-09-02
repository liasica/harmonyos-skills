---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-19
title: 蓝牙监听接口重复触发
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 蓝牙监听接口重复触发
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9d46f9161a6c49ab4108db522d8726dd320558c337b639f8801c5e3b46f7f1c3
---

## 问题现象

在使用蓝牙[access.on('stateChange')](../harmonyos-references/js-apis-bluetooth-access.md#accessonstatechange)类接口订阅事件监听时，有时候会出现发起一次事件请求，监听接口回调重复触发的问题发生。

## 背景知识

同一个access.on('stateChange')接口允许被多次创建，当access.on('stateChange')接口不再需要使用时，可调用相应的[access.off('stateChange')](../harmonyos-references/js-apis-bluetooth-access.md#accessoffstatechange)接口取消监听。

## 问题定位

可通过断点调试，或者在调用access.on('stateChange')接口前添加一条日志输出，排查接口是否被多次调用。

## 分析结论

只有当access.on('stateChange')接口被多次创建时，才会出现接口回调重复触发的问题。

## 解决方案

access.on('stateChange')接口不再需要使用时，请及时调用相配套的access.off('stateChange')接口取消监听，避免下一次调用access.on('stateChange')接口时，之前调用的access.on('stateChange')接口没有被取消监听。以蓝牙开关状态监听接口为例：

```screen
import { access } from '@kit.ConnectivityKit';
import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';

@Entry
@Component
struct StateChangePage {
  // 计数器
  @State number: number = 0;

  aboutToAppear(): void {
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.getUIContext()?.getHostContext() as common.UIAbilityContext,
      ['ohos.permission.ACCESS_BLUETOOTH'], (err, data: PermissionRequestResult) => {
        if (err) {
          console.error(`requestPermissionsFromUser fail, err->${JSON.stringify(err)}`);
        } else {
          console.info(`data:${JSON.stringify(data)}`);
        }
      });
  }

  on() {
    console.info('开启监听');
    // 订阅蓝牙开关状态监听
    try {
      access.on('stateChange', (callback: access.BluetoothState) => {
        console.info(`${this.number} :蓝牙开关状态： ${callback} `);
        this.number++;
      });
    } catch (error) {
      console.info(`开启监听error:${error}`);
    }
  }

  build() {
    Column() {
      Button('开启监听').onClick(() => {
        this.on();
      }).margin(15);
      Button('关闭监听').onClick(() => {
        console.info('关闭监听');
        try {
          access.off('stateChange');
        } catch (error) {
          console.info(`关闭监听error:${error}`);
        }
      }).margin(15);
      Button('开启蓝牙').onClick(() => {
        try {
          if (access.getState() === 0) {
            console.info('开启蓝牙');
            access.enableBluetooth();
          }
        } catch (error) {
          console.info(`开启蓝牙error:${error}`);
        }
      }).margin(15);
      Button('关闭蓝牙').onClick(() => {
        try {
          if (access.getState() === 2) {
            console.info('关闭蓝牙');
            access.disableBluetooth();
          }
        } catch (error) {
          console.info(`关闭蓝牙error:${error}`);
        }
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

Q：BLE蓝牙连接成功之后进行MTU协商，并调用[on('BLEMtuChange')](../harmonyos-references/js-apis-bluetooth-ble.md#onblemtuchange)方法监听MTU变化，但是调用[off('BLEMtuChange')](../harmonyos-references/js-apis-bluetooth-ble.md#offblemtuchange)方法取消监听时回调一直不执行，这是什么原因？

A：取消监听off('BLEMtuChange')方法不会有回调，传入的参数是计划要取消的回调函数。

Q：为什么取消订阅蓝牙设备开关状态事件[access.off('stateChange')](../harmonyos-references/js-apis-bluetooth-access.md#accessoffstatechange)方法可以正常取消监听，而加上第二个参数[Callback<BluetoothState>](../harmonyos-references/js-apis-bluetooth-access.md#bluetoothstate)后无法取消监听？

A：取消订阅蓝牙设备开关状态事件[access.off('stateChange')](../harmonyos-references/js-apis-bluetooth-access.md#accessoffstatechange)传入的回调，需要和订阅on的回调函数是同一个函数。若回调传的是匿名函数，与订阅[access.on('stateChange')](../harmonyos-references/js-apis-bluetooth-access.md#accessonstatechange)的回调函数不一致，将无法取消监听。

Q：access.on('stateChange')能否监听蓝牙权限状态变化？

A：access.on('stateChange')：用于监听“设置-蓝牙”中蓝牙开启/关闭状态变化，不能监听“应用和元服务-应用”下的应用详情中的权限开启/关闭状态变化。
