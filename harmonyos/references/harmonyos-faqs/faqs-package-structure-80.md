---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-80
title: 如何通过定制多目标构建产物实现渠道打包及运行时读取渠道号
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 如何通过定制多目标构建产物实现渠道打包及运行时读取渠道号
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:40b9556461bdc638dd79ab1525182872e36f7ce9fe59daaf1adc2b3dbe7f6996
---

## 问题现象

在HarmonyOS应用开发中，开发者需要实现渠道打包功能，即在编译构建时根据不同的渠道配置生成对应的应用安装包。部分应用在迁移到HarmonyOS前可能依赖原有的渠道打包库（如Walle Library SDK），在HarmonyOS侧需要相应的替代方案来实现运行时读取渠道号或编译时生成多渠道包的能力。

## 背景知识

HarmonyOS提供了定制多目标构建产物的能力，允许开发者在编译时通过不同的配置生成多个APP或HAP。通过定义不同的target和product，可以在构建时同时打包生成不同的安装包，甚至为不同的APP指定不同的页面入口。更多参考请参见[定制多目标构建产物](../harmonyos-guides/ide-customized-multi-targets-and-products-guides.md)和[配置多目标产物-能力说明](../harmonyos-guides/arkts-new-rendering-control-repeat.md#懒加载能力说明)。

Walle Library SDK的核心能力是在运行时从APK中读取渠道号，无需在代码中硬编码。在HarmonyOS中，可通过构建产物定制配合运行时读取BuildProfile或metadata的方式实现等效能力。

## 解决方案

在HarmonyOS中，可以通过定制多目标构建产物来实现渠道打包功能，具体步骤如下：

1. **在build-profile.json5中定义target和product**

   在工程根目录的build-profile.json5中，通过targets和products字段定义多渠道构建配置。每个target对应一个渠道，通过runtimeOS、name等字段区分；product用于定义产物维度的差异。示例配置如下：

   ```json
   {
     "app": {
       "signingConfigs": [],
       "products": [
         {
           "name": "default",
           "signingConfig": "default",
           "compatibleSdkVersion": "5.0.0(12)",
           "runtimeOS": "HarmonyOS"
         }
       ],
       "targets": [
         {
           "name": "default",
           "runtimeOS": "HarmonyOS"
         },
         {
           "name": "huawei",
           "runtimeOS": "HarmonyOS",
           "applyToProducts": ["default"]
         },
         {
           "name": "myapp",
           "runtimeOS": "HarmonyOS",
           "applyToProducts": ["default"]
         }
       ]
     }
   }
   ```

   上述配置定义了default、huawei、myapp三个target，分别对应不同渠道。构建时DevEco Studio会根据选中的target生成对应的HAP/APP产物。
2. **为不同渠道指定不同的源码集或资源**。

   通过在module层级的build-profile.json5中为不同target配置source字段，可以实现不同渠道使用不同的源码集、资源文件或页面入口。示例配置如下：

   ```json
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "deviceTypes": ["default", "tablet"],
       "targets": [
         {
           "name": "default",
           "source": {
             "pages": {
               "$value": "src/main/ets/pages/default_pages"
             },
             "resources": {
               "$value": "src/main/resources/default_resources"
             }
           }
         },
         {
           "name": "huawei",
           "source": {
             "pages": {
               "$value": "src/main/ets/pages/huawei_pages"
             },
             "resources": {
               "$value": "src/main/resources/huawei_resources"
             }
           }
         }
       ]
     }
   }
   ```

   通过上述配置，huawei渠道会使用huawei\_pages目录下的页面和huawei\_resources目录下的资源，实现渠道差异化。更多详情参见[定义产物的source源码集-pages](../harmonyos-guides/ide-customized-multi-targets-and-products-guides.md#section73018336472)。
3. **在运行时读取渠道标识**

   HarmonyOS构建系统会在编译时生成BuildProfile类，其中包含当前构建产物的targetName和productName信息。开发者可在运行时通过BuildProfile获取当前渠道标识，替代Walle Library SDK的运行时读取能力。示例代码如下：

   ```ts
   import { BuildProfile } from 'BuildProfile';

   @Entry
   @Component
   struct Index {
     @State channelName: string = '';

     aboutToAppear(): void {
       // 运行时读取当前构建产物的targetName作为渠道号
       this.channelName = BuildProfile.targetName;
       console.info('当前渠道号:' + this.channelName);
     }

     build() {
       Column() {
         Text('当前渠道: ' + this.channelName)
           .fontSize(24)
           .margin({ top: 50 })
       }
       .width('100%')
       .height('100%')
     }
   }
   ```

   另外，如果需要在module.json5中通过metadata方式传递渠道信息，可在target配置中通过metadata字段注入自定义渠道参数，运行时通过@ohos.bundle.bundleManager读取module的metadata信息。示例代码如下：

   ```screen
   import { bundleManager } from '@kit.AbilityKit';

   // 读取modulemetadata中的渠道信息
   async function getChannelFromMetadata(): Promise<string> {
     const bundleInfo = await bundleManager.getBundleInfoForSelf(
       bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_METADATA
     );
     // 遍历metadata查找渠道标识
     for (const module of bundleInfo.hapModuleInfos) {
       if (module.moduleName === 'entry' && module.metadata) {
         const channelMeta = module.metadata.find(
           (item: Record<string, string>) => item.name === 'channel'
         );
         if (channelMeta) {
           return channelMeta.value;
         }
       }
     }
     return 'unknown';
   }
   ```
4. **构建命令与产物命名**

   在DevEco Studio中，可通过Build菜单选择不同的target进行构建。使用命令行构建时，可通过hvigorw命令指定target和product，示例命令如下：

   ```screen
   # 构建指定target的HAP产物
   hvigorw assembleHap --mode module -p product=default --target huawei

   # 构建指定target的APP产物
   hvigorw assembleApp --mode project -p product=default --target huawei
   ```

   为便于区分不同渠道的产物，建议在build-profile.json5中通过output字段自定义产物命名规则，或在CI/CD流水线中对产物重命名，格式建议为{appName}-{channel}-{version}-{buildTime}.hap，便于后续分发和统计。
5. **多target构建注意事项与CI/CD集成建议**。
   1. 多target构建时，各target共享同一份工程源码，通过source字段差异化配置。需注意避免不同渠道的源码集之间存在命名冲突或依赖循环。
   2. 若渠道差异仅在于资源文件（如应用图标、启动页），可仅配置resources差异化，无需拆分pages目录，降低维护成本。
   3. 在CI/CD流水线中，可遍历所有target依次执行构建命令，将各渠道产物归档至对应分发目录。示例流水线逻辑如下：
      * 读取build-profile.json5中定义的所有target名称列表。
      * 循环执行hvigorw assembleHap --target {targetName}。
      * 将产物按渠道命名归档并上传至分发平台。4.签名配置方面，不同渠道可使用不同的签名证书。在build-profile.json5的signingConfigs中定义多套签名配置，在各target的signingConfig字段中引用对应配置即可。
