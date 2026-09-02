---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-165
title: 如何获取Stage模型应用配置信息？
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取Stage模型应用配置信息？
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:be93e48b49d944c733c9160baf2d93effb987a82dffcc938ff6faafdb33b9c23
---

## 问题现象

如何获取Stage模型应用配置信息？包括全局应用配置文件app.json5以及模块配置文件module.json5。

## 背景知识

[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)：根据给定的bundleFlags获取当前应用的BundleInfo。使用Promise异步回调。

[BundleFlag](../harmonyos-references/js-apis-bundlemanager.md#bundleflag)：包信息标志，指示需要获取的包信息的内容。

[应用配置文件概述（Stage模型）](../harmonyos-guides/application-configuration-file-overview-stage.md)：在基于Stage模型开发的应用项目代码下，都存在一个app.json5配置文件、以及一个或多个module.json5配置文件。

## 解决方案

Stage模型下应用配置主要是app.json5和module.json5两个文件，其中app.json5包含应用全局的配置信息（例如Bundle名称、开发厂商、版本号等基本信息）以及特定设备类型的配置信息，module.json5包含Module的基本配置信息（Module名称、类型、描述、支持的设备类型等基本信息）、应用组件配置信息（UIAbility、ExtensionAbility）、应用运行过程当中所需的权限信息。可以通过包管理工具类当中提供的方法bundleManager.getBundleInfoForSelf在应用代码当中获取这些值。

| 字段 | 所属配置文件 | 查询接口 | 参数bundleFlag | 接口返回值说明 |
| --- | --- | --- | --- | --- |
| bundleName | app.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_DEFAULT | 应用bundleName，bundleInfo.name |
| vendor | app.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_DEFAULT | 应用包的供应商，bundleInfo.vendor |
| versionCode | app.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_DEFAULT | 应用包的版本号，bundleInfo.versionCode |
| versionName | app.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_DEFAULT | 应用包的版本文本描述信息，bundleInfo.versionName |
| minCompatibleVersionCode | app.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_DEFAULT | 分布式场景下的应用包兼容的最低版本，bundleInfo.minCompatibleVersionCode |
| targetAPIVersion | app.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_DEFAULT | 应用运行目标版本，bundleInfo.targetVersion |
| bundleName | app.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_WITH\_APPLICATION | 应用bundleName，bundleInfo.appInfo.name |
| description | app.json5、module.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_WITH\_APPLICATION | 应用的描述信息，返回的是资源描述符，bundleInfo.appInfo.description。可以通过bundleInfo.appInfo.descriptionId资源id获取具体文本。  注：如果app.json5和module.json5配置的入口UIAbility都配置了这个属性，取入口UIAbility配置的值 |
| label | app.json5、module.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_WITH\_APPLICATION | 应用的名称，返回的是资源描述符，bundleInfo.appInfo.label。可以通过bundleInfo.appInfo.labelId资源id获取具体文本。  注：如果app.json5和module.json5配置的入口UIAbility都配置了这个属性，取入口UIAbility配置的值 |
| icon | app.json5、module.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_WITH\_APPLICATION | 应用程序图标，返回的是资源描述符，bundleInfo.appInfo.icon。可以通过bundleInfo.appInfo.iconId资源id获取完整资源。  注：如果app.json5和module.json5配置的入口UIAbility都配置了这个属性，取入口UIAbility配置的值 |
| requestPermissions | module.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_WITH\_REQUESTED\_PERMISSION | 访问应用程序所需的权限，bundleInfo.reqPermissionDetails |
| deviceTypes | module.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE | 当前模块支持安装运行的设备类型的集合, bundleInfo.hapModulesInfo[0].deviceTypes |
| abilities | module.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE  GET\_BUNDLE\_INFO\_WITH\_ABILITY | 当前模块所有Ability的信息，bundleInfo.hapModulesInfo[0].abilitiesInfo |
| extensionAbilitiesInfo | module.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE  GET\_BUNDLE\_INFO\_WITH\_EXTENSION\_ABILITY | 当前模块所有ExtensionAbility的信息，bundleInfo.hapModulesInfo[0].extensionAbilitiesInfo |
| metadata | module.json5 | bundleManager.getBundleInfoForSelf | GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE  GET\_BUNDLE\_INFO\_WITH\_METADATA | 当前模块的元数据，bundleInfo.hapModulesInfo[0].metadata |

代码实例参考如下：

```ts
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';

@Entry
@Component
struct GetStageConfigData {

  build() {
    RelativeContainer() {
      Text('查询应用配置信息')
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT |
            bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION |
            bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
            bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_HAP_MODULE |
            bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_ABILITY |
            bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY |
            bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_METADATA;
          bundleManager.getBundleInfoForSelf(bundleFlags).then((bundleInfo : bundleManager.BundleInfo) => {
            console.info(`bundleName：${bundleInfo.name}`);
            console.info(`供应商：${bundleInfo.vendor}`);
            console.info(`版本号：${bundleInfo.versionCode}`);
            console.info(`版本描述：${bundleInfo.versionName}`);
            console.info(`分布式场景下应用兼容的最低版本：${bundleInfo.minCompatibleVersionCode}`);
            console.info(`应用运行目标版本：${bundleInfo.targetVersion}`);
            // 权限信息：bundleFlags需要包含GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION
            let permissions = bundleInfo.reqPermissionDetails;
            console.info(`应用运行时需向系统申请的权限集合的详细信息：${JSON.stringify(permissions)}`);

            // 应用程序的配置信息，GET_BUNDLE_INFO_WITH_APPLICATION
            let applicationInfo = bundleInfo.appInfo;
            console.info(`bundleName：${applicationInfo.name}`);
            let descriptionId = applicationInfo.descriptionId;
            if (descriptionId) {
              console.info(`应用描述详细信息: ${this.getUIContext().getHostContext()!.resourceManager.getStringSync(descriptionId)}`);
            }
            let labelId = applicationInfo.labelId;
            if (labelId) {
              console.info(`label: ${this.getUIContext().getHostContext()!.resourceManager.getStringSync(labelId)}`);
            }
            let iconId = applicationInfo.iconId;
            if (iconId) {
              let icon = this.getUIContext().getHostContext()!.resourceManager.getMediaContentSync(iconId);
              console.info(`icon: ${buffer.from(icon.buffer).toString()}`);
            }

            // 获取模块配置信息, GET_BUNDLE_INFO_WITH_HAP_MODULE
            let hapInfos = bundleInfo.hapModulesInfo;
            for (let hapInfo of hapInfos) {
              console.info(`模块名称：${hapInfo.name}`);
              console.info(`当前模块的入口UIAbility名称：${hapInfo.mainElementName}`);
              console.info(`模块支持安装运行的设备类型的集合：${JSON.stringify(hapInfo.deviceTypes)}`);
              let abilitiesInfo = hapInfo.abilitiesInfo;
              for (let ability of abilitiesInfo) {
                console.info(`ability信息: ${JSON.stringify(ability)}`);
              }
              // 获取当前模块所有ExtensionAbility的信息,需要额外的GET_BUNDLE_INFO_WITH_EXTENSION_ABILITY
              let extensionAbilitiesInfo = hapInfo.extensionAbilitiesInfo;
              for (let extensionAbilityInfo of extensionAbilitiesInfo) {
                console.info(`extensionAbility信息: ${JSON.stringify(extensionAbilityInfo)}`);
              }
              // 获取模块元信息, 需要额外的GET_BUNDLE_INFO_WITH_METADATA
              let metaData = hapInfo.metadata;
              console.info(`当前模块的元数据: ${JSON.stringify(metaData)}`);
            }

          }).catch((err: BusinessError) => {
            console.info(`查询应用包基础信息失败。code: ${err.code}; message: ${err.message}`);
          });
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
