---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-8
title: HID蓝牙配对后如何实现自动连接
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > HID蓝牙配对后如何实现自动连接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:262e07e0daef85e43477bc33e239b39aeb8e95fa6e2bbfc6cb5ce5514ee8fd0a
---

## 问题现象

在与HID设备完成配对后，如何实现自动连接？如果在系统蓝牙界面手动点击连接之后，后续断开是否会稳定回连？

## 背景知识

* 从API16版本开始，@ohos.bluetooth.connection模块提供了[connectAllowedProfiles](../harmonyos-references/js-apis-bluetooth-connection.md#connectionconnectallowedprofiles16-1)接口，支持对HFP、HID、A2DP设备主动发起连接。
* 从API12版本开始，@ohos.bluetooth.connection模块提供了[getRemoteProfileUuids](../harmonyos-references/js-apis-bluetooth-connection.md#connectiongetremoteprofileuuids12)接口，可用于查询对端蓝牙设备的profile协议能力，建议仅对已配对的设备调用该方法。

## 解决方案

* 当与HID设备完成配对，调用connectAllowedProfiles接口成功建立连接后，后续每次重新打开蓝牙开关，系统都可以自动与HID设备建立连接。

  ```screen
  import { connection } from '@kit.ConnectivityKit';
  import { BusinessError } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct connectAllowedProfiles {
    connectAllowedProfiles() {
      // 发起蓝牙配对请求，此处的mac需要提前获取
      connection.pairDevice('xx.xx.xx.xx', (err: BusinessError) => {
        console.info(`pairDevice, device name err:${err}`);
      });

      // 订阅蓝牙配对状态变化事件
      connection.on('bondStateChange', (data: connection.BondStateParam) => {
        // 蓝牙已配对
        if (data.state === connection.BondState.BOND_STATE_BONDED) {
          // 调用getRemoteProfileUuids接口获取对端蓝牙支持的Profile类型
          connection.getRemoteProfileUuids(data.deviceId,
            (err: BusinessError, dataArray: Array<connection.ProfileUuids>) => {
              console.error(`getRemoteProfileUuids errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}, dataArray: ${dataArray}`);
              // 当dataArray中支持类型包含A2DP、HFP和HID其中的一种，可调用connectAllowedProfiles接口发起连接
              connection.connectAllowedProfiles(data.deviceId, (err: BusinessError) => {
                if (err) {
                  console.error(`connectAllowedProfiles errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
                  return;
                }
                console.info('connectAllowedProfiles');
              });
            });
        }
      });
    }

    build() {
      Column() {
        Button('connect Allowed Profiles')
          .onClick(() => {
            // 创建蓝牙配对状态变化监听，发起蓝牙配对，连接蓝牙
            this.connectAllowedProfiles();
          });
      };
    }
  }
  ```
* 如果在系统蓝牙界面使用手动点击的方式与HID设备建立连接，需要在已配对的设备配置信息中打开‘输入设备’开关，才能实现稳定回连。

## 常见FAQ

Q：在HarmonyOS中，connection.connectAllowedProfiles接口用于连接支持特定配置文件的蓝牙设备。请问该接口支持哪些profile类型？

A：connection.connectAllowedProfiles接口支持的profile类型理论上只包括A2DP、HFP和HID这三种，但是有个特殊的profile类型HOGP。HOGP实际上为HID Over GATT Protocol的缩写，HID以前是只有BR设备有的，后来HID profile为了适配BLE设备才有了HOGP profile这个类型，属于HID profile的一种。
