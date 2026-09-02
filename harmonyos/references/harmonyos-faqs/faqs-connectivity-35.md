---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-35
title: 如何解决蓝牙订阅事件异常问题
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 如何解决蓝牙订阅事件异常问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:5e9266bea89d7509cc7e0925a42245036c36855204235b2a72ea4a199b8bee42
---

## 问题现象

如何解决蓝牙订阅事件异常，如出现订阅无法取消、订阅不生效和订阅后多次回调等问题？

## 背景知识

每个订阅事件会创建一个独立的监听器实例。当订阅蓝牙开关状态事件[access.on('stateChange')](../harmonyos-references/js-apis-bluetooth-access.md#accessonstatechange)后，使用[access.off('stateChange')](../harmonyos-references/js-apis-bluetooth-access.md#accessoffstatechange)取消订阅：

* 若传入参数callback，需要传入相同的回调函数，才能识别要移除具体的监听器。
* 若不传参，则取消订阅该事件对应的所有回调函数通知。

## 问题定位

蓝牙订阅事件异常，主要分为以下三类场景：

1. 订阅事件后无法取消：

   例如，使用access.on('stateChange', this.onReceiveEvent)订阅蓝牙设备开关状态事件后，使用方式一可以正常取消订阅，而使用方式二却无法取消订阅。

   ```ts
   function onReceiveEvent(data: access.BluetoothState) {
     console.info(`bluetooth state = ${data}`);
   }
   // 订阅蓝牙设备开关状态事件
   access.on('stateChange', this.onReceiveEvent)

   // 方式一，取消订阅正常
   access.off('stateChange');
   // 方式二，无法取消订阅
   access.off('stateChange', (callback: access.BluetoothState) => {
     console.info('蓝牙开关取消订阅')
   });
   ```
2. 订阅事件不生效：
   * 排查是否在后台运行，应用线程是否被冻结。如果需要应用可以在后台稳定运行，需要开启蓝牙[长时任务](../harmonyos-guides/continuous-task.md)。
   * 排查事件是否已成功触发。
   * 排查应用订阅事件的时间，是否晚于触发事件的时间。
   * 排查订阅BLE特征值变更事件时，是否已调用[setCharacteristicChangeNotification](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangenotification)或[setCharacteristicChangeIndication](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangeindication)启用通知或指示能力。只有启用通知或指示能力后，才能接收到server端的特征值内容变更通知或指示。

   例如，订阅[on('BLECharacteristicChange')](../harmonyos-references/js-apis-bluetooth-ble.md#onblecharacteristicchange)后，server端特征值内容变更通知client端，但未触发回调。
3. 订阅事件后多次回调：
   * 排查是否多次订阅事件，未及时取消监听，导致重复调用。
   * 部分事件本身会触发多次回调。

   例如，使用access.on('stateChange')订阅蓝牙设备开关状态事件后关闭蓝牙，会接收到多次蓝牙已关闭的状态。

## 分析结论

1. 取消订阅蓝牙设备开关状态事件access.off('stateChange')传入的回调，需要和当时订阅on的回调函数是同一个，上述问题中，方式二的回调函数传的是匿名函数，与订阅事件注册的回调函数不一致，因此无法取消监听。正确写法为：

   ```ts
   // 方式二正确写法
   access.off('stateChange', this.onReceiveEvent);
   ```
2. 分析hilog日志，发现应用的订阅时间为14:16:50.545，对端设备回复消息的时间为14:16:50.543，对端设备已经回复过消息了，应用才订阅通知，因此订阅事件未能触发。若订阅BLE特征值变更事件后回调未触发，还需检查是否已调用setCharacteristicChangeNotification或setCharacteristicChangeIndication启用通知或指示能力，未启用则无法接收server端的特征值变更通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/pHrETneWR9S1Eca02fQPPg/zh-cn_image_0000002682922530.png "点击放大")
3. 订阅stateChange事件会监听所有[BluetoothState](../harmonyos-references/js-apis-bluetooth-access.md#bluetoothstate)状态变化，而不仅仅是最终的开启或关闭状态。关闭蓝牙时会经历STATE\_BLE\_TURNING\_OFF中间态，最终到达STATE\_OFF状态，每个状态变化都会触发回调。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/bUK2L1l0QWiRH3DlhQ4E7w/zh-cn_image_0000002712522461.png "点击放大")

## 修改建议

1. 取消订阅时，确保传入与订阅时相同的回调函数，才能识别要移除具体的监听器。
2. 修改代码逻辑，确保在对端设备回复消息之前完成事件订阅。若订阅BLE特征值变更事件，需先调用[setCharacteristicChangeNotification](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangenotification)或[setCharacteristicChangeIndication](../harmonyos-references/js-apis-bluetooth-ble.md#setcharacteristicchangeindication)启用通知或指示能力，才能接收到server端的特征值内容变更通知或指示。
3. 蓝牙关闭时出现的多次STATE\_OFF事件不用过多关注，出现一次就可以表明蓝牙已关闭，如果应用需要对蓝牙关闭时做一些特定的操作，仅执行一次即可。
