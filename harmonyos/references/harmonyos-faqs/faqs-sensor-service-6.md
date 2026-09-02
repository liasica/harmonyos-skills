---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-6
title: 权限申请和使用的顺序不合理
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 权限申请和使用的顺序不合理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1394f581c21895e195ba8f559895de90542f52050a45c86ef5dc1720bea037d6
---

## 问题现象

应用配置权限ohos.permission.ACCELEROMETER，并动态向用户申请授权。订阅计步器传感器数据，获取用户的行走步数。然而，首次启动应用并同意授权后页面中展示行走步数为0，第二次启动应用方可正常展示。

## 背景知识

* 为了应用发挥完整功能，需要访问系统特定资源，这些资源的访问需要获得相应权限许可。在应用进行权限申请时，选择合适的[权限申请时机](../best-practices/bpta-permission-application.md#section44096197551)是提升用户体验和保护用户隐私安全的关键。具体来说，权限请求与应用内的具体功能场景紧密结合。
* 获取步数时，使用[Sensor Service Kit（传感器服务）](../harmonyos-guides/sensor-service-kit.md)能力。订阅计步器传感器数据，需要配置权限[ohos.permission.ACTIVITY\_MOTION](../harmonyos-guides/permissions-for-all-user.md#ohospermissionactivity_motion)。

## 问题定位

1. 检查module.json5中是否配置ohos.permission.ACTIVITY\_MOTION。
2. 检查应用内调用requestPermissionsFromUser动态向用户申请权限，并在成功获取授权后执行订阅操作。requestPermissionsFromUser用于拉起弹框请求用户授权，使用异步回调。当用户还未授权时，直接调用sensor.on()方法会执行失败。

## 分析结论

由于requestPermissionsFromUser是需要等用户反馈（授权/拒绝）后，才能执行后续订阅计步器传感器数据的操作。本案例在首次安装应用后，应用还未申请权限，执行计步器订阅操作会执行失败，因此页面中的数据无法刷新。当第二次启动应用时，因为用户已经在第一次授予了权限，所以执行订阅操作成功，可以正常展示步数数据。

## 修改建议

首次打开应用时，需要在atManager.requestPermissionsFromUser回调中，判断用户是否授予了权限，如果授予了权限，再执行订阅计步器传感器数据的操作。

```ts
import { abilityAccessCtrl, common, PermissionRequestResult, Permissions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { sensor } from '@kit.SensorServiceKit';

@Entry
@Component
struct Index {
  @State stepNum: number = 0;

  aboutToAppear(): void {
    this.check();
  }

  // 申请权限
  check() {
    const permissions: Permissions[] = ['ohos.permission.ACTIVITY_MOTION'];
    let atManager = abilityAccessCtrl.createAtManager();
    let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, permissions).then((result: PermissionRequestResult) => {
      console.info(`get Permission success, result: ${result}`);
      // 用户授权后再执行订阅操作
      if (result.authResults[0] == 0) {
        this.getPedometerData();
      }
    }).catch((error: BusinessError) => {
      console.error(`get Permission error, error. Code: ${error.code}, message: ${error.message}`);
    });
  }

  // 订阅
  getPedometerData() {
    let sensorCallback: (data: sensor.PedometerResponse) => void = (data: sensor.PedometerResponse) => {
      this.stepNum = data.steps ? data.steps : 0;
    };
    try {
      sensor.on(sensor.SensorId.PEDOMETER, sensorCallback, { interval: 100 });
    } catch (err) {
      console.log(`error ${err}`);
    }
  }

  build() {
    Column() {
      Text(this.stepNum.toString())
        .fontSize(36);
    }
    .height('100%')
    .width('100%');
  }
}
```
