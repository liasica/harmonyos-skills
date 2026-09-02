---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-203
title: 动态生成编译构建产物Hap和App的名称
breadcrumb: FAQ > DevEco Studio > 编译构建 > 动态生成编译构建产物Hap和App的名称
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6c7221519c14daa6dd0c8a3898537453d780c3b7f76e12b91c7e5d16f1523877
---

## 问题现象

在编译构建时，能够动态生成编译产物的名称，名称包含：编译构建时间、版本号、编译模式（debug或者release）。

## 背景知识

hvigor支持在hvigorfile.ts里接收部分编译配置，实现动态配置构建配置，并使能到构建的过程与结果中。

自定义hvigor插件，实现编译产物名称的动态配置，参考文档：[通过hook以及插件上下文动态配置构建配置](../harmonyos-guides/ide-hvigor-config-ohos-sample.md)。

## 解决方案

* **动态生成app名称实现方案：**
  1. 在工程级build-profile.json5中定义编译构建产物app名称。

     ```json
     "products": [
       {
         "name": "default",
         "signingConfig": "default",
         "targetSdkVersion": "6.0.0(20)",
         "compatibleSdkVersion": "6.0.0(20)",
         "runtimeOS": "HarmonyOS",
         "buildOption": {
           "strictMode": {
             "caseSensitiveCheck": true,
             "useNormalizedOHMUrl": true
           }
         },
         "output": {
           "artifactName": "testAppName"
           // app产物名称
         }
       }
     ],
     ```
  2. 在模块级build-profile.json5中定义编译构建产物hap名称。

     ```json
     "targets": [
       {
         "name": "default",
         "output": {
           "artifactName": "testHapName" // hap产物名称
         }
       },
       {
         "name": "ohosTest",
       }
     ],
     ```
  3. 在工程根目录下的hvigorfile.ts中自定义hvigor插件，动态生成app和hap的名称。

     ```ts
     import { appTasks, OhosAppContext, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
     import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor'

     export function customPlugin(): HvigorPlugin {
       return {
         pluginId: "customPlugin",
         context():object {
           return {
             data: "modify output name"
           };
         },
         async apply(currentNode: HvigorNode): Promise<void> {
           // 获取app插件的上下文对象
           const appContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
           // 通过上下文对象获取从根目录build-profile.json5文件中读出来的obj对象
           const buildProfileOpt = appContext.getBuildProfileOpt();
           const appJsonOpt = appContext.getAppJsonOpt();
           // 修改obj对象为想要的，此处举例修改app中的signingConfigs
           const products = buildProfileOpt.app.products;
           let date = new Date();
           let formatDate = date.getFullYear().toString() + (date.getMonth() + 1).toString().padStart(2, '0') +
           date.getDate().toString().padStart(2, '0') + "_" + date.getHours().toString().padStart(2, '0') +
           date.getMinutes().toString().padStart(2, '0') + date.getSeconds().toString().padStart(2, '0');
           for (const product of products) {
             if (product.name === 'default') {
               product.output.artifactName = formatDate + '_' + appJsonOpt.app.versionName + '_'  +
               product.output.artifactName + '_' + appContext.getBuildMode();
               console.info(`output app name: ${product.output.artifactName}`);
             }
           }
           // 将obj对象设置回上下文对象以使能到构建的过程与结果中
           appContext.setBuildProfileOpt(buildProfileOpt);
           hvigor.nodesEvaluated(async() => {
             currentNode.subNodes((node: HvigorNode) => {
               // 获取hap插件的上下文对象
               const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
               // 通过上下文对象获取从根目录build-profile.json5文件中读出来的obj对象
               const hapBuildProfileOpt = hapContext?.getBuildProfileOpt();
               if (hapBuildProfileOpt !== undefined) {
                 const targets = hapBuildProfileOpt.targets;
                 for (const target of targets) {
                   if (target.name === 'default' && target.output?.artifactName !== undefined) {
                     target.output.artifactName = formatDate + '_' + appJsonOpt.app.versionName +'_'  +
                     target.output.artifactName + '_' + appContext.getBuildMode();
                     console.info(`output hap name: ${target.output?.artifactName}`);
                   }
                 }
                 hapContext.setBuildProfileOpt(hapBuildProfileOpt);
               }
             })
           })
         }
       }
     }

     export default {
       system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
       plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
     }
     ```
* **直接修改app名称实现方案：**

  通过afterNodeEvaluate hook获取插件向node中注册的context，通过context修改buildOption或者操作一些任务。
  + OhosPluginId：本组件是hvigor-ohos-plugin插件id常量类；
  + OhosAppContext：本组件是appTasks插件对外提供的上下文扩展接口，包括工程信息、product信息等；
  + afterNodeEvaluate：为所有的node添加一个node评估后的回调函数；
  + getBuildProfileOpt：获取当前构建的根目录下build-profile.json5文件中内容的obj对象；
  + setBuildProfileOpt：设置当前构建的根目录下build-profile.json5文件中内容的obj对象。

    ```ts
    // 动态修改App包名加版本号，工程级hvigorfile.ts
    import { appTasks , OhosPluginId} from '@ohos/hvigor-ohos-plugin';
    import { hvigor } from '@ohos/hvigor'

    hvigor.afterNodeEvaluate((hvigorNode)=>{
      const context = hvigorNode.getContext(OhosPluginId.OHOS_APP_PLUGIN)
      if (context && context.getBuildProfileOpt) {
        const buildProfile = context.getBuildProfileOpt();
        const products = buildProfile.app.products;
        for (const product of products) {
          if (product.name === context.getCurrentProduct().productBuildOpt.name) {
            product.output = {
              "artifactName": "app-v1.0.3"
            }
          }
        }
        context.setBuildProfileOpt(buildProfile);
      }
    })

    export default {
      system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
      plugins:[] /* Custom plugin to extend the functionality of Hvigor. */
    }
    ```
* **动态生成har包名称实现方案：**

  ```ts
  import { harTasks,OhosPluginId  } from '@ohos/hvigor-ohos-plugin';
  import { hvigor } from '@ohos/hvigor'

  hvigor.afterNodeEvaluate((hvigorNode)=>{
    const context = hvigorNode.getContext(OhosPluginId.OHOS_HAR_PLUGIN)
    if (context && context.getBuildProfileOpt) {
      const buildProfile = context.getBuildProfileOpt();
      const targets = buildProfile.targets
      for (const target of targets) {
        if (target.name === 'default') {
          target.output={
            "artifactName": 'myTestHar'
          }
        }
      }
      context.setBuildProfileOpt(buildProfile);
    }
  })

  export default {
    system: harTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
  }
  ```

## 常见FAQ

Q：如何在hvigor自定义任务中使用npm包？

A：在hvigor/hvigor-config.json5的dependencies中指定依赖，然后在自定义任务中使用。

Q：如何查看编译的详细过程？

A：取消hvigor->hvigor-config.json5中"logging": { //"level": "info" }的注释，改为debug，改完后的结果为"logging": { "level": "debug" }，在编译时就可以看到编译的详细过程。
