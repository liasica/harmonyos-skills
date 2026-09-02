---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-14
title: 蓝牙相关业务开发中长时任务的使用流程以及注意事项
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > 蓝牙相关业务开发中长时任务的使用流程以及注意事项
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:56daae5d61e76adfbbcee47f66df2803cf4c974e5c97a3ac1b8ecbf03ae2e69a
---

## 问题现象

蓝牙相关业务开发中如何使用长时任务？有哪些注意事项？

## 背景知识

* [BLUETOOTH\_INTERACTION](../harmonyos-guides/continuous-task.md#使用场景)：应用退至后台后，在后台需要长时间运行用户可感知的任务，如录制。为防止应用进程被挂起，导致对应功能异常，可以申请长时任务，使应用在后台长时间运行。
* [蓝牙低功耗连接和传输数据](../harmonyos-guides/gatt-development-guide.md)：基于通用属性协议（Generic Attribute Profile，GATT）实现BLE设备间连接和传输数据的开发。当两个设备间进行GATT通信交互时，依据设备功能的不同，可区分为GATT客户端和GATT服务端。

## 解决方案

蓝牙低功耗场景长时任务开发步骤：

1. 申请ohos.permission.KEEP\_BACKGROUND\_RUNNING权限，配置方式请参见[声明权限](../harmonyos-guides/declare-permissions.md)。
2. 声明后台模式类型：

   在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中abilities下的backgroundModes字段里，为需要使用长时任务的UIAbility声明相应的长时任务类型，配置文件中填写长时任务类型的[配置项](../harmonyos-guides/continuous-task.md#使用场景)。

   ```json
   "backgroundModes": [
     // 蓝牙传输类型长时任务
     "bluetoothInteraction"
   ],
   ```
3. 申请和取消长时任务。

   ```js
   import { bundleManager, WantAgent, wantAgent } from '@kit.AbilityKit';
   import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   class BackgroundRunningManager {
     // 申请长时任务
     public static async startBackgroundRunning(context?: Context) {
       // 获取bundle应用信息
       let bundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
       // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
       let wantAgentInfo: wantAgent.WantAgentInfo = {
         // 点击通知后，将要执行的动作列表
         // 添加需要被拉起应用的bundleName和abilityName
         wants: [
           {
             bundleName: bundleInfo.name,
             abilityName: 'MainAbility'
           }
         ],
         // 指定点击通知栏消息后的动作是拉起ability
         actionType: wantAgent.OperationType.START_ABILITY,
         // 使用者自定义的一个私有值
         requestCode: 0,
         // 点击通知后，动作执行属性
         actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
         // 车钥匙长时任务子类型，从API version 16开始支持。只有申请bluetoothInteraction类型的长时任务，车钥匙子类型才能生效。
         // 确保extraInfo参数中的Key值为backgroundTaskManager.BackgroundModeType.SUB_MODE，否则子类型不生效。
         // extraInfo: { [backgroundTaskManager.BackgroundModeType.SUB_MODE] : backgroundTaskManager.BackgroundSubMode.CAR_KEY }
       };

       try {
         // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
         wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
           try {
             backgroundTaskManager.startBackgroundRunning(context,
               backgroundTaskManager.BackgroundMode.BLUETOOTH_INTERACTION, wantAgentObj).then(() => {
               console.info('Operation startBackgroundRunning succeeded');
             }).catch((error: BusinessError) => {
               console.error(`Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}`);
             });
           } catch (error) {
             console.error(`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
           }
         });
       } catch (error) {
         console.error(`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
       }
     }

     // 停止后台任务
     public static async stopBackgroundRunning(context?: Context) {
       backgroundTaskManager.stopBackgroundRunning(context).then(() => {
         console.info(`Succeeded in operationing stopBackgroundRunning.`);
       }).catch((err: BusinessError) => {
         console.error(`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
       });
     }
   }
   ```
4. 调用方式。

   ```js
   @Entry
   @Component
   struct Index {
     private context: Context = this.getUIContext().getHostContext() as Context;

     build() {
       Column({ space: 20 }) {
         Button() {
           Text('申请蓝牙长时任务').fontSize(25).fontWeight(FontWeight.Bold);
         }
         .type(ButtonType.Capsule)
         .margin({ top: 10 })
         .backgroundColor('#0D9FFB')
         .width(300)
         .height(40)
         .onClick(() => {
           // 通过按钮申请长时任务
           BackgroundRunningManager.startBackgroundRunning(this.context);
           // 下方执行开发者自己的蓝牙相关任务
         });

         Button() {
           Text('停止蓝牙长时任务').fontSize(25).fontWeight(FontWeight.Bold);
         }
         .type(ButtonType.Capsule)
         .margin({ top: 10 })
         .backgroundColor('#0D9FFB')
         .width(300)
         .height(40)
         .onClick(() => {
           // 通过按钮停止长时任务
           BackgroundRunningManager.stopBackgroundRunning(this.context);
         });
       }
       .height('100%')
       .width('100%')
       .justifyContent(FlexAlign.Center);
     }
   }
   ```

完整代码：

```ts
/*
 *
 *  * Copyright (c) 2025 Huawei Device Co., Ltd.
 *  * Licensed under the Apache License, Version 2.0 (the ""License"");
 *  * you may not use this file except in compliance with the License.
 *  * You may obtain a copy of the License at
 *  *
 *  *     http://www.apache.org/licenses/LICENSE-2.0
 *  *
 *  * Unless required by applicable law or agreed to in writing, software
 *  * distributed under the License is distributed on an ""AS IS"" BASIS,
 *  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  * See the License for the specific language governing permissions and
 *  * limitations under the License.
 *
 */

import { bundleManager, WantAgent, wantAgent } from '@kit.AbilityKit';
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { BusinessError } from '@kit.BasicServicesKit';

class BackgroundRunningManager {
  // 申请长时任务
  public static async startBackgroundRunning(context?: Context) {
    // 获取bundle应用信息
    let bundleInfo = bundleManager.getBundleInfoForSelfSync(bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
    // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // 点击通知后，将要执行的动作列表
      // 添加需要被拉起应用的bundleName和abilityName
      wants: [
        {
          bundleName: bundleInfo.name,
          abilityName: 'MainAbility'
        }
      ],
      // 指定点击通知栏消息后的动作是拉起ability
      actionType: wantAgent.OperationType.START_ABILITY,
      // 使用者自定义的一个私有值
      requestCode: 0,
      // 点击通知后，动作执行属性
      actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
      // 车钥匙长时任务子类型，从API version 16开始支持。只有申请bluetoothInteraction类型的长时任务，车钥匙子类型才能生效。
      // 确保extraInfo参数中的Key值为backgroundTaskManager.BackgroundModeType.SUB_MODE，否则子类型不生效。
      // extraInfo: { [backgroundTaskManager.BackgroundModeType.SUB_MODE] : backgroundTaskManager.BackgroundSubMode.CAR_KEY }
    };

    try {
      // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          backgroundTaskManager.startBackgroundRunning(context,
            backgroundTaskManager.BackgroundMode.BLUETOOTH_INTERACTION, wantAgentObj).then(() => {
            console.info('Operation startBackgroundRunning succeeded');
          }).catch((error: BusinessError) => {
            console.error(`Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}`);
          });
        } catch (error) {
          console.error(`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
      });
    } catch (error) {
      console.error(`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
  }

  // 停止后台任务
  public static async stopBackgroundRunning(context?: Context) {
    backgroundTaskManager.stopBackgroundRunning(context).then(() => {
      console.info(`Succeeded in operationing stopBackgroundRunning.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
    });
  }
}

@Entry
@Component
struct Index {
  private context: Context = this.getUIContext().getHostContext() as Context;

  build() {
    Column({ space: 20 }) {
      Button() {
        Text('申请蓝牙长时任务').fontSize(25).fontWeight(FontWeight.Bold);
      }
      .type(ButtonType.Capsule)
      .margin({ top: 10 })
      .backgroundColor('#0D9FFB')
      .width(300)
      .height(40)
      .onClick(() => {
        // 通过按钮申请长时任务
        BackgroundRunningManager.startBackgroundRunning(this.context);
        // 下方执行开发者自己的蓝牙相关任务
      });

      Button() {
        Text('停止蓝牙长时任务').fontSize(25).fontWeight(FontWeight.Bold);
      }
      .type(ButtonType.Capsule)
      .margin({ top: 10 })
      .backgroundColor('#0D9FFB')
      .width(300)
      .height(40)
      .onClick(() => {
        // 通过按钮停止长时任务
        BackgroundRunningManager.stopBackgroundRunning(this.context);
      });
    }
    .height('100%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

**说明** 

* 使用钱包服务中的[数字车钥匙](../harmonyos-guides/wallet-carkey-overview.md)实现保活蓝牙的方案，主要用于车钥匙长时任务子类型。只有申请bluetoothInteraction类型的长时任务，车钥匙子类型才能生效。
* 确保extraInfo参数中的Key值为backgroundTaskManager.BackgroundModeType.SUB\_MODE，否则子类型不生效。
* 如果使用钱包拉起宿主应用长时任务，在执行backgroundTaskManager.startBackgroundRunning时，需要注意参数context是否能获取到。如果获取不到，可以在宿主应用启动时先缓存context。
* 开启蓝牙后台长时任务时，若蓝牙连接断开需在一分钟内重新连接成功，否则长时任务将自动结束。
