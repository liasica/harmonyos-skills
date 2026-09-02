---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/driverextensionability
title: 开发无UI界面基础驱动
breadcrumb: 指南 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > 扩展外设基础驱动开发 > 开发无UI界面基础驱动
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bf1ba7980757f4711befa9ba57098cdad0d07dd6217d2b00ab54f60cdf205951
---

## 场景介绍

无UI界面的基础驱动，适用于不需要通过UI界面设置驱动能力的简单设备，例如鼠标、键盘等，保证设备的即插即用功能即可。开发者可以通过DriverExtensionAbility实现此类应用的开发。

## 基本概念

* DriverExtensionAbility

  [DriverExtensionAbility](../harmonyos-references/js-apis-app-ability-driverextensionability.md)是Driver类型的ExtensionAbility组件，提供驱动相关扩展框架能力。对于部分设备，支持插入外接的硬件模块来扩展设备能力， 此时可以以应用方式安装该硬件模块的驱动程序。[DriverExtensionAbility](../harmonyos-references/js-apis-app-ability-driverextensionability.md)可以通过[@ohos.driver.deviceManager (外设管理)](../harmonyos-references/js-apis-driver-devicemanager.md)提供的接口被应用绑定，并根据应用的请求信息在后台处理相关事务。

  每个类型的ExtensionAbility都有自己的Context，DriverExtensionAbility通过[DriverExtensionContext](../harmonyos-references/js-apis-inner-application-driverextensioncontext.md)提供相关能力。

## 环境搭建

请参考[环境准备](environmental-preparation.md)完成开发前的准备工作。

## 开发步骤

开发者在实现一个驱动时，需要在DevEco Studio工程中手动新建一个DriverExtensionAbility，具体步骤如下：

1. 创建新工程，请参考[创建一个新的工程](ide-create-new-project.md)，创建一个HarmonyOS工程。（如果在[开发带UI界面基础驱动](externaldevice-guidelines.md)已经创建，则此处不需要创建。）
2. 在新创建的工程对应的ets目录下，右键选择“New > Directory”，新建一个目录并命名为driverextability。
3. 在driverextability目录，右键选择“New > ArkTS File”，新建一个文件并命名为DriverExtAbility.ets。
4. 在文件中导入相关Kit，并定义请求Code。

   ```typescript
   import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
   import { Want } from '@kit.AbilityKit';
   import { rpc } from '@kit.IPCKit';

   const REQUEST_CODE = 99; // 与扩展外设客户端约定请求码。
   ```
5. 打开DriverExtAbility.ets文件，导入[@ohos.rpc (RPC通信)](../harmonyos-references/js-apis-rpc.md)，重载onRemoteMessageRequest()方法，接收应用传递过来的消息，并将处理的结果返回给应用。REQUEST\_CODE用于校验应用发送的服务请求码。

   ```typescript
   class StubTest extends rpc.RemoteObject {
     // 接收应用传递过来的消息处理，以及将处理的结果返回给客户端。
     onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
       option: rpc.MessageOption) {
       if (code === REQUEST_CODE) {
         // 接收应用传递过来的数据。
         // 应用使用多次调用data.writeString()写入多个数据时，驱动可以通过多次调用data.readString()方法接收对应的数据。
         let optFir: string = data.readString();
         // 驱动将数据的处理结果返回给应用。
         // 示例中为接收了"Hello"，并将"Hello World"返回给应用。
         reply.writeString(optFir + ` World`);
       }
       return true;
     }
   }
   ```
6. 在DriverExtAbility.ets文件中，增加导入[DriverExtensionAbility](../harmonyos-references/js-apis-app-ability-driverextensionability.md)的依赖包，该包提供了onInit()、onRelease()、onConnect()和onDisconnect()生命周期回调，自定义类继承[DriverExtensionAbility](../harmonyos-references/js-apis-app-ability-driverextensionability.md)并根据需要重写生命周期回调。

   ```typescript
   export default class DriverExtAbility extends DriverExtensionAbility {
     onInit(want: Want) {
       console.info('testTag', `onInit, want: ${want.abilityName}`);
     }

     onRelease() {
       console.info('testTag', `onRelease`);
     }

     onConnect(want: Want) {
       console.info('testTag', `onConnect, want: ${want.abilityName}`);
       return new StubTest('test');
     }

     onDisconnect(want: Want) {
       console.info('testTag', `onDisconnect, want: ${want.abilityName}`);
     }

     onDump(params: Array<string>) {
       console.info('testTag', `onDump, params:` + JSON.stringify(params));
       return ['params'];
     }
   }
   ```
7. 在工程Module对应的[module.json5配置文件](module-configuration-file.md)中注册DriverExtensionAbility，type标签需要设置为“driver”，srcEntry标签表示当前ExtensionAbility组件所对应的代码路径。

   ```json5
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "default"
       ],
       "requestPermissions": [
         {
           "name": "ohos.permission.ACCESS_EXTENSIONAL_DEVICE_DRIVER" // 此处为扩展外设相关权限，必须配置。
         }
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:main_pages",
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
       "extensionAbilities": [
         {
           "name": "DriverExtAbility",
           "icon": "$media:startIcon",
           "description": "driver",
           "type": "driver",
           "exported": true,
           "srcEntry": "./ets/driverextability/DriverExtAbility.ets",
           "metadata": [
             {
               "name": "bus", // 必填项，所属总线。
               "value": "USB"
             },
             {
               "name": "desc", // 选填项，必要的驱动描述。
               "value": "the sample of driverExtensionAbility"
             },
             {
               "name": "vendor", // 选填项，驱动厂商名称。
               "value": "string"
             },
             {
               "name": "vid", // 支持 USB vendor id 列表，填写16进制，此处为4817的16进制。
               "value": "0x12D1"
             },
             {
               "name": "pid", // 支持的 USB product id 列表，填写16进制，此处为4258的16进制。
               "value": "0x10A2"
             },
             {
               "name": "launchOnBind", // 选填项，延迟拉起驱动。此处“true”表示延迟拉起，“false”表示即时拉起，配置错误或不配置，默认为“false”。
               "value": "true"
             },
             {
               "name": "ohos.permission.ACCESS_DDK_ALLOWED", // 选填项，允许应用访问。此处“true”表示允许访问，“false”表示不允许访问，配置错误或不配置，默认为“false”。
               "value": "true"
             }
           ]
         }
       ]
     }
   }
   ```
8. 完成客户端和驱动示例代码开发后，请参考[使用本地真机运行应用/元服务](ide-run-device.md)，将Hap导入设备中，并点击hap中的Hello，查看是否会转变为Hello world，即实现ipc通信功能。

## 扩展设备能力

扩展外设管理目前提供了HidDdk、UsbDdk、USBSerialDDK和ScsiPeripheralDDK四种能力，用于扩展外设专项驱动的开发。具体使用方法，请参考：

* [开发适用HID协议的设备驱动](hid-ddk-guidelines.md)
* [开发适用USB协议的设备驱动](usb-ddk-guidelines.md)
* [开发适用串口协议的设备驱动](usb-serial-ddk-guidelines.md)
* [开发使用SCSI协议的设备驱动](scsi-peripheral-ddk-guidelines.md)

## 应用签名

**注意** 

先配置权限，再自动签名。

应用需要配置签名文件才能在设备上运行，并且扩展外设管理客户端开发，需要配置扩展外设的权限：ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER。

* ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

  在module.json5配置文件的requestPermissions标签中[声明权限](declare-permissions.md)后，即可获得授权。
* ohos.permission.ACCESS\_DDK\_DRIVERS

  1. 在module.json5配置文件的requestPermissions标签中[声明权限](declare-permissions.md)。
  2. HarmonyAppProvision配置文件中，修改acls字段，跨级别申请权限，可参考[申请使用受限权限](declare-permissions-in-acl.md)。

完成权限配置后，可参考[自动签名](ide-signing-auto.md)对应用进行签名。
