---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/plugin-package
title: 开发与使用应用插件（PC/2in1）
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > 开发与使用应用插件（PC/2in1）
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:58b324d8e5bcd05ef8b1b28da0ef15b44c58266f3b3632a9b119bde26af6f2d7
---

插件包是基于[HSP](in-app-hsp.md)的共享包组件，用于扩展宿主应用（加载并运行插件的应用程序）的功能。插件通常由第三方开发者或宿主应用开发者创建，旨在为宿主应用提供额外的特性或服务，例如专业设计软件通过插件为不同行业提供定制能力。插件运行依赖系统能力，例如调用ArkTS接口、使用Ability组件等。若插件自身不依赖系统能力，则可沿用应用原有的插件打包方式，无需采用HSP形式。插件不能独立运行，必须依赖宿主应用提供的运行环境和功能支持。

## 需要权限

宿主应用使用插件需申请ohos.permission.kernel.SUPPORT\_LOCAL\_PLUGIN权限，具体申请方式请参考[声明权限](declare-permissions-in-acl.md)。

```json5
"requestPermissions": [
  {
    "name": "ohos.permission.kernel.SUPPORT_LOCAL_PLUGIN"
  }
]
```

## 开发应用插件

本章节介绍如何在DevEco Studio中完成应用插件包的工程配置、签名设置与编译打包，帮助开发者快速构建可被宿主应用集成的HSP插件包。

### 工程配置

1. 插件包本质上是动态共享包HSP，参考[创建HSP模块](ide-hsp.md#section79378499185)在工程中创建插件模块plugin。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/aOdi-vaYR1yZu2-uqWlb8g/zh-cn_image_0000002815397885.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=391EA722A8C986BF0AF1C1473FECE4A19FE45C24EE7A7F13716AF96FD16A5E8D)
2. 在[app.json5](app-configuration-file.md)中配置bundleType字段为appPlugin，该字段表示当前包为应用的插件包，bundleName为插件的包名。

   ```json5
   {
     "app": {
       "bundleName": "com.example.plugin",
       "vendor": "example",
       "versionCode": 1000000,
       "versionName": "1.0.0",
       "buildVersion": "1",
       "icon": "$media:layered_image",
       "label": "$string:app_name",
       "bundleType": "appPlugin"
     }
   }
   ```
3. 选择DevEco Studio菜单栏中的File > Project Structure，在Signing Configs页面勾选Automatically generate signature。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/OR30sxVuSsGbTaBbi9Kr1Q/zh-cn_image_0000002786518310.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=52CDF68C9EBAB2F40CCDC9AAE8A6C72EC79CF43FE8E5E1E007D05803F0947580)

### 编译打包

1. 选中工程目录中插件模块的文件目录，通过DevEco Studio菜单栏的Build > Make Module ${libraryName}进行编译构建。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/oBB4AZbTT6ySRG5aiIoPUA/zh-cn_image_0000002786358382.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=3295C5B636DA807769E2F15906023D7ECBB6714CA4A4CACA43742698164E5B71)
2. 编译完成后，会在工程目录中生成对应的产物。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/4VLZ0K9tSzmK3L1jzuxQig/zh-cn_image_0000002815557803.png?HW-CC-KV=V1&HW-CC-Date=20261112T233235Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9B5295F7FAA93F72CE267AB78717E9B3325082BA4963D0B8EFDAE7D2E6D6813)

## 使用应用插件

本章节介绍宿主应用如何安装、更新和卸载应用插件，以及如何通过调用插件接口将插件能力集成到宿主应用中。

### 安装或更新插件

1. 将插件包HSP放在宿主应用可访问的目录下，例如/storage/Users/currentUser或者宿主应用自身的沙箱目录。
2. 在宿主应用的[module.json5](module-configuration-file.md)配置文件的requestPermissions字段中申请ohos.permission.kernel.SUPPORT\_LOCAL\_PLUGIN权限。
3. 参考以下示例代码，在宿主应用中调用[installLocalPlugin](../harmonyos-references/js-apis-pluginbundlemanager.md#pluginbundlemanagerinstalllocalplugin)接口安装插件。

   ```typescript
   import { pluginBundleManager } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   // ...
   let pluginPaths: string[] = ['/storage/Users/currentUser/plugin.hsp'];

   pluginBundleManager.installLocalPlugin(pluginPaths)
     .then(() => {
       console.info('installLocalPlugin success');
     }).catch((err: BusinessError) => {
     console.error(`installLocalPlugin errData is errCode:${err.code}  message:${err.message}`);
   });
   // ...
   ```

**说明** 

* 更新插件后，依赖宿主应用重新加载或重启宿主应用生效。
* 如果插件包HSP放置在/storage/Users/currentUser目录下，宿主应用还需要额外申请ohos.permission.READ\_WRITE\_USER\_FILE权限。

### 查询插件

在宿主应用中调用[getAllLocalPluginInfoForSelf](../harmonyos-references/js-apis-pluginbundlemanager.md#pluginbundlemanagergetalllocalplugininfoforself)接口查询插件的信息。

```typescript
import { pluginBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// ...
pluginBundleManager.getAllLocalPluginInfoForSelf().then((data): void => {
  console.info('getAllLocalPluginInfoForSelf plugin data is' + JSON.stringify(data));
}).catch((err: Error): void => {
  const businessErr = err as BusinessError;
  console.error(`getAllLocalPluginInfoForSelf errData is errCode:${businessErr.code}  message:${businessErr.message}`);
});
// ...
```

### 卸载插件

在宿主应用中调用[uninstallLocalPlugin](../harmonyos-references/js-apis-pluginbundlemanager.md#pluginbundlemanageruninstalllocalplugin)接口卸载插件。

```typescript
import { pluginBundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// ...
let pluginBundleName: string = 'com.example.plugin';

pluginBundleManager.uninstallLocalPlugin(pluginBundleName)
  .then(() => {
    console.info('uninstallLocalPlugin success');
  }).catch((err: BusinessError) => {
  console.error(`uninstallLocalPlugin errData is errCode:${err.code}  message:${err.message}`);
});
// ...
```

## 调用插件能力

本章节介绍如何使用插件中提供的功能。应用可以通过import的方式引用插件。

```ts
import native from 'plugin';

export function nativeMulti(a: number, b: number): number {
  let result: number = native.multi(a, b);
  return result;
}
```

该场景下，开发者可以使用插件包的上下文获取插件资源。通过[createPluginModuleContext](../harmonyos-references/js-apis-app-ability-application.md#applicationcreatepluginmodulecontext19)接口创建context，然后从context中获取相关信息。

```ts
import { AbilityConstant, UIAbility, application, common, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    let moduleContext: common.Context;
    try {
      application.createPluginModuleContext(this.context, 'com.example.pluginBundleName', 'pluginModuleName')
        .then((data: common.Context) => {
          moduleContext = data;
          console.info('createPluginModuleContext success!');
        })
        .catch((error: BusinessError) => {
          let code: number = (error as BusinessError).code;
          let message: string = (error as BusinessError).message;
          console.error(`createPluginModuleContext failed, error.code: ${code}, error.message: ${message}`);
        });
    } catch (error) {
      let code: number = (error as BusinessError).code;
      let message: string = (error as BusinessError).message;
      console.error(`createPluginModuleContext failed, error.code: ${code}, error.message: ${message}`);
    }
  }
}
```
