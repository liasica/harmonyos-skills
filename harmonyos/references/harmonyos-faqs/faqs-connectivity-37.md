---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-37
title: 蓝牙配对后如何在系统蓝牙界面显示已连接
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 蓝牙配对后如何在系统蓝牙界面显示已连接
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9a1bc7dfcf93294331a60d9d50b5689279a7261756f6b1a3e1037111b29ea8ec
---

## 问题现象

蓝牙配对后，系统蓝牙界面只显示该设备已配对，如何使系统蓝牙界面已配对的设备显示“已连接”？

## 背景知识

系统蓝牙界面显示“已连接”需要发起配对的应用去连蓝牙的profile，可以使用[connection.connectAllowedProfiles](../harmonyos-references/js-apis-bluetooth-connection.md#connectionconnectallowedprofiles16-1)接口连接对端设备支持的profile（只包括A2DP、HFP和HID）。

* 需先调用[connection.pairDevice](../harmonyos-references/js-apis-bluetooth-connection.md#connectionpairdevice)发起配对，且仅允许在每次发起配对后30s内调用此接口一次。
* 当配对成功后，建议先调用[getRemoteProfileUuids](../harmonyos-references/js-apis-bluetooth-connection.md#connectiongetremoteprofileuuids12)主动查询目标设备支持的profile能力。若存在应用需要的能力，才调用此接口。
* 目标设备支持的profile能力可参考[ProfileUuids](../harmonyos-references/js-apis-bluetooth-constant.md#profileuuids12)通用唯一标识（Universally Unique Identifier，UUID）。

## 解决方案

三方应用在蓝牙配对成功后，需要主动使用[connection.connectAllowedProfiles](../harmonyos-references/js-apis-bluetooth-connection.md#connectionconnectallowedprofiles16-1)接口连接对端设备支持的profile，才能在系统蓝牙界面显示“已连接”。

参考示例如下：

```ts
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
            // 当dataArray中支持类型包含A2DP、HFP和HID其中的一种，可调用connectAllowedProfiles接口发起连接。
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

权限说明：需要在module.json5文件中配置允许应用接入蓝牙并使用蓝牙功能权限[ohos.permission.ACCESS\_BLUETOOTH](../harmonyos-guides/permissions-for-all-user.md#ohospermissionaccess_bluetooth)。
