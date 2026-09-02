---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-location-28
title: 如何配置后台持续定位长时任务
breadcrumb: FAQ > 应用服务开发 > 位置服务（Location Kit） > 如何配置后台持续定位长时任务
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6ab32fd57a661d643871fc702622c2244038294cc31b0b9a389f6bbde56ec3ac
---

## 问题现象

实时导航等场景下，应用可能需要退至后台并持续更新位置信息，如何实现后台持续定位长时任务？

## 背景知识

* [长时任务(ArkTS)](../harmonyos-guides/continuous-task.md)：应用退至后台后，在后台需要长时间运行用户可感知的任务，如播放音乐、导航等。为防止应用进程被挂起，导致对应功能异常，可以申请长时任务，使应用在后台长时间运行。
* [Location Kit（位置服务）](../harmonyos-guides/location-kit.md)：位置子系统使用多种定位技术提供服务，如GNSS定位、基站定位、WLAN/蓝牙定位（基站定位、WLAN/蓝牙定位后续统称“网络定位技术”）；通过这些定位技术，无论用户设备在室内或是户外，都可以准确地确定设备位置。
* [geoLocationManager.on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange)：获取实时位置的接口，开启位置变化订阅，并发起定位请求。

## 解决方案

1. 在module.json5文件的requestPermissions中声明位置权限和后台运行位置权限。

   ```json
   {
     "name" : "ohos.permission.LOCATION",
     "usedScene": {
       "abilities": [
         "EntryAbility"
       ],
       "when": "inuse"
     },
     "reason": "$string:location_use"
   },
   {
     "name" : "ohos.permission.APPROXIMATELY_LOCATION",
     "usedScene": {
       "abilities": [
         "EntryAbility"
       ],
       "when": "inuse"
     },
     "reason": "$string:location_use"
   },
   {
     "name" : "ohos.permission.LOCATION_IN_BACKGROUND",
     "usedScene": {
       "abilities": [
         "EntryAbility"
       ],
       "when": "inuse"
     },
     "reason": "$string:location_use"
   },
   {
     "name" : "ohos.permission.KEEP_BACKGROUND_RUNNING",
     "usedScene": {
       "abilities": [
         "EntryAbility"
       ],
       "when": "inuse"
     },
     "reason": "$string:location_use"
   }
   ```
2. 在module.json5文件中为需要使用长时任务的UIAbility声明长时任务类型backgroundModes为location。

   ```json
   "abilities": [
     {
       "name": "EntryAbility",
       "srcEntry": "./ets/entryability/EntryAbility.ets",
       "description": "$string:EntryAbility_desc",
       "icon": "$media:layered_image",
       "label": "$string:EntryAbility_label",
       "startWindowIcon": "$media:startIcon",
       "startWindowBackground": "$color:start_window_background",
       "exported": true,
       "backgroundModes": ["location"],// 声明支持定位后台模式
       "skills": [
         {
           "entities": [
             "entity.system.home"
           ],
           "actions": [
             "ohos.want.action.home"
           ]
         }
       ]
     }
   ],
   ```
3. 添加后台应用的相关信息。

   ```ts
   let wantAgentInfo: wantAgent.WantAgentInfo = {
     // 添加需要被拉起应用的bundleName和abilityName
     wants: [
       {
         bundleName: 'com.example.backgroundtask',
         abilityName: 'EntryAbility'
       }
     ],
     // 指定点击通知栏消息后的动作是拉起ability
     actionType: wantAgent.OperationType.START_ABILITY,
     // 使用者自定义的一个私有值
     requestCode: 0,
     // 点击通知后，动作执行属性
     actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
   };
   ```
4. 向用户申请位置权限。

   ```ts
   // 启动定位之前先申请位置权限
   await reqPermissionsFromUser(['ohos.permission.APPROXIMATELY_LOCATION', 'ohos.permission.LOCATION'],
     this.getUIContext().getHostContext() as common.UIAbilityContext);
   ```
5. 启动长时任务时，长时任务类型配置为location。

   ```ts
   let list: Array<string> = ['location']; // 注意长时任务类型
   backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj)
     .then(async () => {
       console.info('Operation startBackgroundRunning succeeded');
       // 此处执行具体的长时任务逻辑，该示例中为获取位置信息
       if (!geoLocationManager.isLocationEnabled()) {
         this.message = 'permission error';
       }
       let request: geoLocationManager.ContinuousLocationRequest = {
         'interval': 1,
         'locationScenario': geoLocationManager.UserActivityScenario.NAVIGATION
       };
       try {
         geoLocationManager.on('locationChange', request, (location: geoLocationManager.Location) => {
           this.latitude = location.latitude;
           this.longitude = location.longitude;
         });
       } catch (err) {
         this.message = JSON.stringify(err);
       }
     })
     .catch((error: BusinessError) => {
       console.error(`Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}`);
     });
   ```

完整代码：

```ts
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { abilityAccessCtrl, common, Permissions, WantAgent, wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { geoLocationManager } from '@kit.LocationKit';

async function reqPermissionsFromUser(permissions: Array<Permissions>,
  context: common.UIAbilityContext): Promise<boolean> {
  let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
  // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
  let data = await atManager.requestPermissionsFromUser(context, permissions);
  let grantStatus: Array<number> = data.authResults;
  let length: number = grantStatus.length;
  for (let i = 0; i < length; i++) {
    if (grantStatus[i] === 0) {
      return true; // 用户授权，可以继续访问目标操作
    }
  }
  return false; // 授权失败
}

@Entry
@Component
struct Index {
  @State message: string = 'ContinuousTask';
  @State latitude: number = 0;
  @State longitude: number = 0;
  // 通过getUIContext().getHostContext()方法，来获取page所在的UIAbility上下文
  private context: Context | undefined = this.getUIContext().getHostContext();

  startContinuousTask() {
    let wantAgentInfo: wantAgent.WantAgentInfo = {
      // 添加需要被拉起应用的bundleName和abilityName
      wants: [
        {
          bundleName: 'com.example.backgroundtask',
          abilityName: 'EntryAbility'
        }
      ],
      // 指定点击通知栏消息后的动作是拉起ability
      actionType: wantAgent.OperationType.START_ABILITY,
      // 使用者自定义的一个私有值
      requestCode: 0,
      // 点击通知后，动作执行属性
      actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG],
    };

    try {
      // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
      wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
        try {
          let list: Array<string> = ['location']; // 注意长时任务类型
          backgroundTaskManager.startBackgroundRunning(this.context, list, wantAgentObj)
            .then(async () => {
              console.info('Operation startBackgroundRunning succeeded');
              // 此处执行具体的长时任务逻辑，该示例中为获取位置信息
              if (!geoLocationManager.isLocationEnabled()) {
                this.message = 'permission error';
              }
              let request: geoLocationManager.ContinuousLocationRequest = {
                'interval': 1,
                'locationScenario': geoLocationManager.UserActivityScenario.NAVIGATION
              };
              try {
                geoLocationManager.on('locationChange', request, (location: geoLocationManager.Location) => {
                  this.latitude = location.latitude;
                  this.longitude = location.longitude;
                });
              } catch (err) {
                this.message = JSON.stringify(err);
              }
            })
            .catch((error: BusinessError) => {
              console.error(`Failed to Operation startBackgroundRunning. code is ${error.code} message is ${error.message}`);
            });
        } catch (error) {
          console.error(`Failed to Operation startBackgroundRunning. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
        }
      });
    } catch (error) {
      console.error(`Failed to Operation getWantAgent. code is ${(error as BusinessError).code} message is ${(error as BusinessError).message}`);
    }
  }

  stopContinuousTask() {
    backgroundTaskManager.stopBackgroundRunning(this.context).then(async () => {
      console.info(`Succeeded in operationing stopBackgroundRunning.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
    });
  }

  build() {
    Row() {
      Column() {
        Button('启动后台定位任务')
          .width(250)
          .height(40)
          .onClick(async () => {
            // 启动定位之前先申请位置权限
            await reqPermissionsFromUser(['ohos.permission.APPROXIMATELY_LOCATION', 'ohos.permission.LOCATION'],
              this.getUIContext().getHostContext() as common.UIAbilityContext);
            this.startContinuousTask();
          });

        Button('取消后台长时任务')
          .margin({ top: 10, bottom: 10 })
          .width(250)
          .height(40)
          .onClick(() => {
            this.stopContinuousTask();
          });

        Text(`latitude: ${this.latitude}`);
        Text(`longitude: ${this.longitude}`);
      }
      .width('100%');
    }
    .height('100%');
  }
}
```
