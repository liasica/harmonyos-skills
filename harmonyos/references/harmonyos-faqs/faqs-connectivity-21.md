---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-connectivity-21
title: App点击蓝牙设备列表不显示设备
breadcrumb: FAQ > 系统开发 > 网络 > 短距通信（Connectivity） > App点击蓝牙设备列表不显示设备
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:38+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:09f0d88f01d0966bbf6d3e4f5d692f71299dd98f31b3c5107f35eb4f111f2e99
---

## 问题现象

进入App内蓝牙设备列表，不显示设备，是什么原因导致的？

## 背景知识

* [蓝牙connection模块](../harmonyos-references/js-apis-bluetooth-connection.md)：connection模块提供了蓝牙设备的配对、连接及状态查询等能力。
* [connection.on('bluetoothDeviceFind')](../harmonyos-references/js-apis-bluetooth-connection.md#connectiononbluetoothdevicefind)：订阅蓝牙设备扫描结果上报事件。使用Callback异步回调。可扫描到的设备类型包括传统蓝牙设备和低功耗蓝牙设备。该上报方式只支持获取设备地址信息。
* [connection.getRemoteDeviceName](../harmonyos-references/js-apis-bluetooth-connection.md#connectiongetremotedevicename)：获取对端蓝牙设备的名称。
* [ForEach](../harmonyos-references/ts-rendering-control-foreach.md)：ForEach接口基于数组类型数据来进行循环渲染。
* [List](../harmonyos-references/js-service-widget-container-list.md)：列表包含一系列相同宽度的列表项。适合连续、多行呈现同类数据，例如图片和文本。
* 使用蓝牙功能前，需要申请权限ohos.permission.ACCESS\_BLUETOOTH。如何申请蓝牙权限，具体操作请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 问题定位

1. 检查从系统设置里是否能蓝牙搜索到附近设备：系统设置中可搜到附近设备，排除硬件问题。
2. 检查是否配置权限接入了ohos.permission.ACCESS\_BLUETOOTH：观察hilog日志，触发蓝牙扫描时未触发permission相关报错，并且返回了相关地址信息，说明蓝牙功能是可用的。
3. 检查触发蓝牙扫描时的hilog信息，蓝牙扫描时的hilog结果（截取部分）：

   (operator():81)device: D0:1E:\*\*:\*\*:\*\*:8D, len: 31

   可见进入App蓝牙设备列表后有获取到附近设备的地址信息，但并未有相关设备名。

## 分析结论

根据问题定位现象可知，App能正常获取到地址信息。未能在App蓝牙设备页面显示应用信息，可能原因有：

1. 缺少了通过设备地址获取设备名称的步骤。
2. UI设计上缺少了列表显示设备信息的组件。

## 修改建议

1. 在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)的requestPermissions标签中声明权限ohos.permission.ACCESS\_BLUETOOTH。
2. 在使用connection.on('bluetoothDeviceFind')获取蓝牙设备相关信息后，通过connection.getRemoteDeviceName获取蓝牙设备的名称。示例代码如下：

   ```ts
   connection.on('bluetoothDeviceFind', (data: string[]) => {
     console.info(`data: ${JSON.stringify(data)} ${connection.getRemoteDeviceName(data[0])}`);
     if (!this.findList.find((item: Device) => item.deviceId === data[0])) {
       this.findList.push({
         name: connection.getRemoteDeviceName(data[0]),
         deviceId: data[0]
       });
     };
   });
   ```
3. 使用ForEach结合List实现列表显示设备信息的组件。示例代码如下：

   ```ts
   List() {
     ForEach(this.findList, (item: Device) => {
       ListItem() {
         Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
           Column() {
             Text(`设备名称：${item?.name}`);
             Text(`设备id：${item?.deviceId}`).fontColor('#ffcbcbcb').fontSize(12);
           }
           .alignItems(HorizontalAlign.Start);

           Row({ space: 5 }) {
             Button('链接').width(60).height(20).fontSize(12).onClick(() => {
               try {
                 // 实际的地址可由扫描流程获取
                 connection.pairDevice(item.deviceId, () => {
                   this.getUIContext().getPromptAction().showToast({
                     message: '配对成功'
                   });
                 });
               } catch (err) {
                 console.error(`errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
               };
             });
           };
         }
         .height(50)
         .backgroundColor('#fff')
         .width('100%')
         .borderRadius(10)
         .padding(6);
       }.padding(4);
     });
   }
   .height(200)
   .width('100%')
   .flexGrow(1)
   .flexShrink(1)
   .flexBasis(1);
   ```
4. 完整示例代码如下：

   ```ts
   import connection from '@ohos.bluetooth.connection';
   import { BusinessError } from '@ohos.base';
   import { PromptAction } from '@kit.ArkUI';
   import abilityAccessCtrl, { Permissions } from '@ohos.abilityAccessCtrl';
   import common from '@ohos.app.ability.common';

   interface Device {
     name?: string
     deviceId?: string
   };

   @Entry
   @Component
   struct Index {
     // 正确写法（Stage模型）
     private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     promptAction: PromptAction = this.getUIContext().getPromptAction();

     @State findList: Device[] = [];

     aboutToAppear(): void {
       const permissions: Array<Permissions> = ['ohos.permission.ACCESS_BLUETOOTH'];
       let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
       atManager.requestPermissionsFromUser(this.context, permissions).then(() => {
         // 授权成功
       }).catch((err: BusinessError) => {
         console.error(`Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
       });
     };

     build() {
       Flex({ direction: FlexDirection.Column }) {
         Row() {
           Button('扫描蓝牙').onClick(() => {
             // 开启扫描
             try {
               connection.startBluetoothDiscovery();
               console.info('startBleScan success');
               this.getUIContext().getPromptAction().showToast({
                 message: '已打开'
               });
             } catch (err) {
               this.getUIContext().getPromptAction().showToast({
                 message: '蓝牙开关未打开'
               });
             };

             // 接收扫描结果
             connection.on('bluetoothDeviceFind', (data: string[]) => {
               console.info(`data: ${JSON.stringify(data)} ${connection.getRemoteDeviceName(data[0])}`);
               if (!this.findList.find((item: Device) => item.deviceId === data[0])) {
                 this.findList.push({
                   name: connection.getRemoteDeviceName(data[0]),
                   deviceId: data[0]
                 });
               };
             });
           });

           Button('停止扫描').onClick(() => {
             try {
               // 关闭扫描
               connection.stopBluetoothDiscovery();
               console.info('stopBleScan success');
               this.getUIContext().getPromptAction().showToast({
                 message: '停止扫描'
               });
             } catch (err) {
               this.getUIContext().getPromptAction().showToast({
                 message: '蓝牙已关闭'
               });
             };
           });

           Button('清空').onClick(() => {
             this.findList = [];
           });
         };
         List() {
           ForEach(this.findList, (item: Device) => {
             ListItem() {
               Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
                 Column() {
                   Text(`设备名称：${item?.name}`);
                   Text(`设备id：${item?.deviceId}`).fontColor('#ffcbcbcb').fontSize(12);
                 }
                 .alignItems(HorizontalAlign.Start);

                 Row({ space: 5 }) {
                   Button('链接').width(60).height(20).fontSize(12).onClick(() => {
                     try {
                       // 实际的地址可由扫描流程获取
                       connection.pairDevice(item.deviceId, () => {
                         this.getUIContext().getPromptAction().showToast({
                           message: '配对成功'
                         });
                       });
                     } catch (err) {
                       console.error(`errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
                     };
                   });
                 };
               }
               .height(50)
               .backgroundColor('#fff')
               .width('100%')
               .borderRadius(10)
               .padding(6);
             }.padding(4);
           });
         }
         .height(200)
         .width('100%')
         .flexGrow(1)
         .flexShrink(1)
         .flexBasis(1);
       }.padding(10).width('100%').height('100%').backgroundColor('#ffcdcdcd');
     };
   };
   ```
