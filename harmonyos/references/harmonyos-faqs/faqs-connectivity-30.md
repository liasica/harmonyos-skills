---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-30
title: 蓝牙发送大数据导致主线程卡死
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 蓝牙发送大数据导致主线程卡死
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:08946e0521968b0e6fbac2fcfd90ff105eac2f82a45ed994b7f40fdb416ae53f
---

## 问题现象

在调用socket.sppWrite接口发送大量数据时，发现有时候会出现THREAD\_BLOCK\_6S主线程卡死的情况，如何解决在蓝牙发送大量数据时，主线程卡死的问题？

## 背景知识

* 蓝牙socket模块提供了[socket.sppWrite](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppwrite)接口，用于经典蓝牙间传输数据。
* ArkTS提供了[taskpool](../harmonyos-references/js-apis-taskpool.md)模块，可以为应用程序提供一个多线程的运行环境。

## 解决方案

常规场景下，socket蓝牙支持蓝牙间大量数据的传输，但是若蓝牙传输业务和应用其它业务同时放入主线程中运行，蓝牙传输大量数据时，有一定几率出现主线程卡死的情况。因此，可以将socket.sppWrite方法添加到taskpool中，另启一个子线程单独处理蓝牙数据传输业务。参考样例如下：

```screen
import { socket } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { taskpool } from '@kit.ArkTS';
import { abilityAccessCtrl, common, PermissionRequestResult } from '@kit.AbilityKit';

// 蓝牙写入方法
@Concurrent
export function sppWrite(clientNumber: number, data: Uint8Array) {
  // 写入数据
  try {
    socket.sppWrite(clientNumber, data.buffer);
    console.info('客户端sppWrite success');
  } catch (err) {
    console.info(`写入失败: Code is ${err.code}, message is ${err.message}`);
  }
}

@Entry
@Component
struct Index {
  // 蓝牙连接成功后获取的客户端socket的id
  @State clientNumber: number = 0;
  uiContext = this.getUIContext();

  aboutToAppear(): void {
    // 蓝牙手动授权
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

  // 开启子线程方法
  taskpool() {
    // 需要蓝牙传输的数据
    let data: Uint8Array = new Uint8Array(1);
    let task: taskpool.Task = new taskpool.Task(sppWrite, this.clientNumber, data);
    taskpool.execute(task).then((res: object) => {
      console.log(`执行成功! ${res}`);
    }).catch((err: BusinessError) => {
      console.info(`执行失败: Code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {
    Row() {
      Column() {
        Text('开启子线程执行蓝牙传输！')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.taskpool();
          });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

**说明** 

上述代码涉及蓝牙API接口，使用前需要在module.json5中配置[ohos.permission.ACCESS\_BLUETOOTH](../harmonyos-guides/permissions-for-all-user.md#ohospermissionaccess_bluetooth)权限，并申请用户授权，然后连接上spp蓝牙，提前获取clientNumber值（该值是调用[socket.sppAccept](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppaccept)或[socket.sppConnect](../harmonyos-references/js-apis-bluetooth-socket.md#socketsppconnect)接口，通过其异步callback获取到的）。
