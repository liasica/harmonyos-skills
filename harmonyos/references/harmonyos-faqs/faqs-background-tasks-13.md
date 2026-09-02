---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-13
title: 后台位置上报类型长时任务开发指导
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 后台任务开发（Background Tasks） > 后台位置上报类型长时任务开发指导
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-08-05
content_hash: sha256:b761beac324945305b1ed3e3100baea1166311700c66f493363662f7fb01d58c
---

## 问题现象

员工外出工作，需要每隔一定时间上报一次位置，应用处于后台运行的案例。

## 背景知识

* [长时任务](../harmonyos-guides/continuous-task.md)：应用退至后台后，在后台需要长时间运行用户可感知的任务，如导航等。为防止应用进程被挂起，导致对应功能异常，可以申请长时任务，使应用在后台长时间运行。
* [Location Kit（位置服务）](../harmonyos-guides/location-kit-intro.md)：位置子系统使用多种定位技术提供服务，通过这些定位技术，无论用户设备在室内或是户外，都可以准确地确定设备位置。通过[on('locationChange')](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanageronlocationchange)开启位置变化监听，可实时获取当前位置信息。

## 解决方案

1. 申请ohos.permission.KEEP\_BACKGROUND\_RUNNING、ohos.permission.LOCATION、ohos.permission.APPROXIMATELY\_LOCATION权限，配置方式请参见[声明权限](../harmonyos-guides/declare-permissions.md)。
2. 声明后台模式类型：

   在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中abilities下的backgroundModes字段里，为需要使用长时任务的UIAbility声明相应的长时任务类型，配置文件中填写长时任务类型的[配置项](../harmonyos-guides/continuous-task.md#使用场景)。

   ```json
   "backgroundModes": [
             "location"
           ],
   ```
3. 定位能力先申请定位权限，然后在定位功能启动时可同步启动后台定位长时任务，在取消定位时同时取消长时任务，完整代码如下：

   ```ts
   import { geoLocationManager } from '@kit.LocationKit';
   import { abilityAccessCtrl, common, PermissionRequestResult, Permissions, WantAgent, wantAgent } from '@kit.AbilityKit';
   import { backgroundTaskManager } from '@kit.BackgroundTasksKit';

   @Entry
   @Component
   struct Index {
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     @State workingState: boolean = false;
     @State locationInfos: Array<LocationInfo> = [];

     // Start solution1
     aboutToAppear() {
       // 申请定位权限
       let permissions: Array<Permissions> = ['ohos.permission.LOCATION', 'ohos.permission.APPROXIMATELY_LOCATION'];
       this.reqPermissionsFromUser(permissions);
     }

     reqPermissionsFromUser(permissions: Array<Permissions>): void {
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       // requestPermissionsFromUser会判断权限的授权状态来决定是否唤起弹窗
       atManager.requestPermissionsFromUser(this.context, permissions).then((data: PermissionRequestResult) => {
         console.info(`requestPermissionsFromUser success, result: ${JSON.stringify(data)}`);
       }).catch((err: BusinessError) => {
         console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
       });
     }
     // End solution1

     build() {
       Column({ space: 16 }) {
         Row() {
           Column({ space: 20 }) {
             Row({ space: 15 }) {
               Image($r('sys.media.person_shield'))
                 .width(30)
                 .height(30)

               Text('张三')
             }

             Text('外出场所：大运广场')
           }
           .alignItems(HorizontalAlign.Start)
           .width('70%')

           Blank().width(2).backgroundColor(Color.Gray)

           Column() {
             Column() {
               if (this.workingState) {
                 Text('结束')
               } else {
                 Text('开始')
               }
               Text('工作')
             }
             .padding(5)
             .backgroundColor(this.workingState ? '#E84026' : '#64BB5C')
             .borderRadius($r('sys.float.corner_radius_level4'))
             .onClick(() => {
               if (this.workingState) {
                 this.offLocationListen();
                 this.stopContinuousTask();
               } else {
                 this.getLocation();
                 this.startContinuousTask();
               }
             });
           }
           .width('29%')
         }
         .width('100%')
         .padding(14)
         .borderRadius(8)
         .backgroundColor(Color.White)

         Column() {
           Row() {
             Text('位置信息列表')

             Text(`Total: ${this.locationInfos.length}`)
           }
           .width('100%')
           .justifyContent(FlexAlign.SpaceBetween)

           Scroll() {
             List({ space: 5 }) {
               ForEach(this.locationInfos, (item: LocationInfo) => {
                 ListItem() {
                   Column() {
                     Text(`时间：${item.time}`)

                     Text(`坐标：[${item.latitude}, ${item.longitude}]`)

                     Text(`地址：${item.address}`)
                   }
                   .width('100%')
                   .padding(5)
                   .borderRadius(5)
                   .alignItems(HorizontalAlign.Start)
                   .backgroundColor('#0C0A59F7')
                 }
               })
             }
           }
           .scrollBar(BarState.Off)
           .padding({ top: 5, bottom: 10 })
         }
         .width('100%')
         .height('100%')
         .padding(14)
         .borderRadius(8)
         .flexShrink(999)
         .backgroundColor(Color.White)
       }
       .height('100%')
       .width('100%')
       .padding(12)
       .backgroundColor('#f1f3f5')
     }

     locationChange = async (location: geoLocationManager.Location) => {
       if (location) {
         this.workingState = true;
         if (this.locationInfos.length >= 50) {
           this.locationInfos.pop();
         }

         let info = new LocationInfo();
         info.location = location;
         info.latitude = location?.latitude.toFixed(5);
         info.longitude = location?.longitude.toFixed(5);
         info.time = new Date(location?.timeStamp).toLocaleString('zh-CN', { hour12: false });
         let address = await this.getAddressFromLocation(location.latitude, location.longitude);
         info.address = address;
         this.locationInfos.push(info);
       }
     };

     /**
      * 每隔2秒上报一次位置
      */
     getLocation() {
       let requestInfo: geoLocationManager.LocationRequest = {
         'priority': geoLocationManager.LocationRequestPriority.FIRST_FIX,
         'scenario': geoLocationManager.LocationRequestScenario.UNSET,
         'timeInterval': 2,
         'distanceInterval': 0,
         'maxAccuracy': 0
       };

       try {
         geoLocationManager.on('locationChange', requestInfo, this.locationChange);
       } catch (err) {
         console.error(`getLocation errCode: ${err?.code},errMessage: ${err?.message}`);
       }
     }

     /**
      * 坐标转化为地址
      */
     async getAddressFromLocation(lati: number, long: number): Promise<string> {
       let address: string | undefined = '';
       let reverseGeocodeRequest: geoLocationManager.ReverseGeoCodeRequest = {
         'latitude': lati,
         'longitude': long,
         'maxItems': 1
       };
       let locationResult = await geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest);
       console.log(`locationResult => ${JSON.stringify(locationResult)}`);
       if (locationResult && locationResult.length > 0) {
         address = locationResult[0].placeName;
       }
       return address ? address : '';
     }

     /**
      * 关闭位置上报
      */
     offLocationListen() {
       try {
         // 需要取消订阅的回调函数。该回调函数需要与on接口传入的回调函数保持一致。若无此参数，则取消当前类型的所有订阅。
         geoLocationManager.off('locationChange', this.locationChange);
         this.workingState = false;
         this.locationInfos = [];
       } catch (err) {
         console.error(`offLocationListen errCode: ${err?.code},errMessage: ${err?.message}`);
       }
     }

     startContinuousTask() {
       let wantAgentInfo: wantAgent.WantAgentInfo = {
         // 点击通知后，将要执行的动作列表
         // 添加需要被拉起应用的bundleName和abilityName
         wants: [
           {
             bundleName: this.context.abilityInfo.bundleName,
             abilityName: 'EntryAbility'
           }
         ],
         // 指定点击通知栏消息后的动作是拉起ability
         actionType: wantAgent.OperationType.START_ABILITY,
         // 使用者自定义的一个私有值
         requestCode: 0,
         // 点击通知后，动作执行属性
         actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
       };

       // 通过wantAgent模块下getWantAgent方法获取WantAgent对象
       wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj: WantAgent) => {
         backgroundTaskManager.startBackgroundRunning(this.context,
           backgroundTaskManager.BackgroundMode.LOCATION, wantAgentObj).then(() => {
           console.info(`Succeeded in operating startBackgroundRunning.`);
         }).catch((err: BusinessError) => {
           console.error(`Failed to operation startBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
         });
       });
     }

     stopContinuousTask() {
       backgroundTaskManager.stopBackgroundRunning(this.context).then(() => {
         console.info(`Succeeded in operating stopBackgroundRunning.`);
       }).catch((err: BusinessError) => {
         console.error(`Failed to operation stopBackgroundRunning. Code is ${err.code}, message is ${err.message}`);
       });
     }
   }

   class LocationInfo {
     public location: geoLocationManager.Location | undefined;
     public latitude: string = '';
     public longitude: string = '';
     public address: string = '';
     public time: string = '';
   }
   ```

## 常见FAQ

Q：应用置于后台一段时间后会被冻结，报FROZEN\_BY\_DEVICE\_STILL\_ENTER。

A：FROZEN\_BY\_DEVICE\_STILL\_ENTER表示应用基于定位的长时任务，在应用退至后台进入静止状态超过3分钟或者应用退后台前已进入静止超过30秒，系统会主动进行冻结。

Q：应用在后台长时间进行定位采集时，进程被反复kill并重启，日志显示kill reason=GnssWorkTimeAbnormal。

A：应用长时间进行定位采集但未申请后台持续定位长时任务时，系统会对进程进行管控。需要申请后台持续定位长时任务，具体操作请参见【解决方案】章节。
