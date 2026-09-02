---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-213
title: 使用Hvigor自定义不同产物的配置数据
breadcrumb: FAQ > DevEco Studio > 编译构建 > 使用Hvigor自定义不同产物的配置数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ae8e14cd75edd740b88cba7c4a6b464ac99997f1bbf1d8539a882948154f0701
---

## 问题现象

在HarmonyOS应用开发中，如何根据不同的编译产物，动态配置不同模块中的metadata参数？

## 背景知识

* [扩展构建](../harmonyos-guides/ide-build-expanding.md)允许开发者通过配置任务的形式，在编译过程中对配置参数进行自定义修改。通过扩展构建，开发者可以灵活地调整构建流程和输出结果。
* [插件上下文](../harmonyos-guides/ide-build-expanding-context.md)是扩展构建中的核心概念，它提供了获取当前构建环境信息的接口。通过插件上下文，开发者可以获取当前产物信息（如Debug/Release版本）、遍历模块信息，并对模块配置进行动态调整。

## 解决方案

1. 需要获取产物名称，根据产物配置对应的模块参数，因此应在最外层配置hvigorfile.ts文件。
2. 根据如下代码获取应用配置参数，获取其中配置的产物名称。

   ```ts
   const appNode: HvigorNode = getNode(__filename);
   const appContext = appNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
   const bundleProduct = appContext.getCurrentProduct();
   const productName = bundleProduct.productName;
   ```
3. 使用subNodes接口获取所有模块的环境信息，然后通过getContext接口分别获取hap包配置信息。

   ```ts
   // 获取hap模块上下文信息
   const hapContext = hapNode.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
   ```
4. 根据第2步获取的包名和第三步获取到的环境信息，使用getModuleJsonOpt获取对应模块下的module.json5配置，修改后，使用setModuleJsonOpt将修改后的配置信息写入。

   ```ts
   if (moduleNameExample === moduleName) {
     const moduleJsonOpt = hapContext?.getModuleJsonOpt();
     if (moduleJsonOpt) {
       // 根据产物变更参数值
       moduleJsonOpt.module.metadata = productName === productNameExample ?
         [{ "name": "client_id", "value": "TestIdNo1" }] : [{ "name": "client_id", "value": "TestIdNo2" }];
       // 将obj对象设置回上下文对象以使能到构建的过程与结果中
       hapContext.setModuleJsonOpt(moduleJsonOpt);
     }
   }
   ```
5. 总体配置文件hvigorfile.ts，配置参考如下：

   ```ts
   import { appTasks, OhosHapContext, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
   import { getNode, hvigor, HvigorNode } from '@ohos/hvigor';

   // 待修改的产物名
   const productNameExample = 'default'
   // 待修改的模块名
   const moduleNameExample = 'entry'

   hvigor.nodesEvaluated(() => {
     const appNode: HvigorNode = getNode(__filename);
     const appContext = appNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
     const bundleProduct = appContext.getCurrentProduct();
     const productName = bundleProduct.productName;

     // 遍历子节点
     appNode.subNodes((hapNode: HvigorNode) => {
       // 获取hap模块上下文信息
       const hapContext = hapNode.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
       const moduleName = hapContext?.getModuleName();
       if (moduleNameExample === moduleName) {
         const moduleJsonOpt = hapContext?.getModuleJsonOpt();
         if (moduleJsonOpt) {
           // 根据产物变更参数值
           moduleJsonOpt.module.metadata = productName === productNameExample ?
             [{ "name": "client_id", "value": "TestIdNo1" }] : [{ "name": "client_id", "value": "TestIdNo2" }];
           // 将obj对象设置回上下文对象以使能到构建的过程与结果中
           hapContext.setModuleJsonOpt(moduleJsonOpt);
         }
       }
     });
   });

   export default {
     system: appTasks,
     plugins: []
   }
   ```

## 总结

通过HarmonyOS的扩展构建功能，开发者可以在编译阶段动态配置模块的参数。具体来说：

* 全局配置：若配置信息涉及多个模块或需要跨模块操作（如根据产物名称动态调整参数），建议将配置逻辑放在项目根目录下的hvigorfile.ts文件中。
* 模块级配置：若仅需配置单个模块的metadata参数，且无需跨模块操作，则可以直接在模块目录中进行配置。
