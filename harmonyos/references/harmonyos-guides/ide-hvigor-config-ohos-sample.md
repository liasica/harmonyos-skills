---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-config-ohos-sample
title: 实践说明
breadcrumb: 指南 > 构建应用 > 定制构建 > 动态修改编译配置 > 实践说明
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:969a82ce760b257dd1bf1bb87ec4f0089a97f1be5c9bac66930f655edd548b1e
---

## 通过hook以及插件上下文动态修改配置(推荐使用)

### 修改每个hvigorNode中的build-profile.json5

以下示例为单个node注册hook并修改build-profile.json5的信息。

例如修改根目录下的build-profile.json5的签名信息，则在项目根目录下的hvigorfile.ts中添加如下内容：

```ts
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor,getNode } from '@ohos/hvigor'

// 获取根节点
const rootNode = getNode(__filename);
// 为根节点添加一个afterNodeEvaluate hook 在hook中修改根目录下的build-profile.json5的内容并使能
rootNode.afterNodeEvaluate(node => {
    // 获取app插件的上下文对象
    const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
    // 通过上下文对象获取从根目录build-profile.json5文件中读出来的obj对象
    const buildProfileOpt = appContext.getBuildProfileOpt();
    // 修改obj对象为想要的，此处举例修改app中的signingConfigs
    buildProfileOpt['app']['signingConfigs'] = [
        {
            "name": "default",
            "type": "HarmonyOS",
            "material": {
                "certpath": "D:\\SigningConfig\\debug_hos.cer",
                "storePassword": "******",
                "keyAlias": "debugKey",
                "keyPassword": "******",
                "profile": "D:\\SigningConfig\\debug_hos.p7b",
                "signAlg": "SHA256withECDSA",
                "storeFile": "D:\\SigningConfig\\debug_hos.p12"
            }
        }
    ];
    // 将obj对象设置回上下文对象以使能到构建的过程与结果中
    appContext.setBuildProfileOpt(buildProfileOpt);
})
export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### 修改module.json5中的配置信息

可通过hvigor对象的hook能力快捷为所有的node创建hook，以下示例为单个node创建一个hook并修改其中的module.json5的配置信息。

例如修改entry下的module.json5配置，则在entry下的hvigorfile.ts中添加如下内容：

```ts
import { hapTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode } from '@ohos/hvigor'

const entryNode = getNode(__filename);
// 为此节点添加一个afterNodeEvaluate hook 在hook中修改module.json5的内容并使能
entryNode.afterNodeEvaluate(node => {
    // 获取此节点使用插件的上下文对象 此时为hap插件 获取hap插件上下文对象
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    // 通过上下文对象获取从module.json5文件中读出来的obj对象
    const moduleJsonOpt = hapContext.getModuleJsonOpt();
    // 修改obj对象为想要的，此处举例修改module中的deviceTypes
    moduleJsonOpt['module']['deviceTypes'] = ["phone", "tablet", "2in1", "car"];
    // 将obj对象设置回上下文对象以使能到构建的过程与结果中
    hapContext.setModuleJsonOpt(moduleJsonOpt);
})
export default {
    system: hapTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### 修改app.json5中的配置信息

在项目的根目录下的hvigorfile.ts中添加如下代码内容：

```ts
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor'

// 为根节点添加一个afterNodeEvaluate hook 在hook中修改app.json5的内容并使能
hvigor.getRootNode().afterNodeEvaluate(rootNode => {
    // 获取app插件的上下文对象
    const appContext = rootNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
    // 通过上下文对象获取从app.json5文件中读出来的obj对象
    const appJsonOpt = appContext.getAppJsonOpt();
    // 修改obj对象为想要的，此处举例修改app中的versionCode
    appJsonOpt['app']['versionCode'] = 1000001;
    // 将obj对象设置回上下文对象以使能到构建的过程与结果中
    appContext.setAppJsonOpt(appJsonOpt);
})
export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### 修改oh-package.json5中的依赖

可通过hvigorfile.ts自定义插件修改工程级、模块级的oh-package.json5的依赖，例如在工程级hvigorfile.ts或模块级hvigorfile.ts分别添加以下内容：

```ts
// 工程级hvigorfile.ts
import { appTasks, OhosAppContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { HvigorNode, HvigorPlugin, TaskInput, TaskOutput } from '@ohos/hvigor';
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const appContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
            const dependency = appContext.getDependenciesOpt();  // 获取dependency依赖
            dependency["library"]="file:library.har"    // 确保har包存在
            console.log(dependency);
            appContext.setDependenciesOpt(dependency );  // 修改dependency依赖，需要确保oh-package.json5中dependencies字段存在
        }
    };
}
export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}

// 模块级hvigorfile.ts
import {hapTasks,OhosHapContext,OhosPluginId,Target} from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin} from '@ohos/hvigor';
import * as fs from 'fs';
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const hapContext = currentNode.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
            const dependency = hapContext.getDependenciesOpt();    // 获取dependency依赖
            dependency["library"]="file:library.har"    // 确保har包存在
            hapContext.setDependenciesOpt(dependency);}   // 需要确保oh-package.json5中dependencies字段存在
        }
    };
export default {
    system: hapTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

## 通过overrides动态配置签名材料和版本信息(不推荐使用)

通过在hvigorfile.ts中使用函数方法，动态配置签名材料和版本号、版本名等信息：

```ts
//工程级别hvigorfile.ts
import { appTasks } from '@ohos/hvigor-ohos-plugin';
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [],       /* Custom plugin to extend the functionality of Hvigor. */
  config: {
    ohos: {
      overrides:{
        signingConfig: getSigningConfig(), //签名配置对象 
        appOpt: {
          versionCode: getVersionCode(),
          versionName: getVersionName(),
        } //app.json中的内容 
      }
    }
  }
}

function getSigningConfig() {
  return {
    type: "HarmonyOS",
    material: {
      certpath: "D:\\SigningConfig\\debug_hos.cer",
      storePassword: "******",
      keyAlias: "debugKey",
      keyPassword: "******",
      profile: "D:\\SigningConfig\\debug_hos.p7b",
      signAlg: "SHA256withECDSA",
      storeFile: "D:\\SigningConfig\\debug_hos.p12"
    }
  }
}

function getVersionCode() {
  return 100000+new Date().getFullYear();
}

function getVersionName() {
  return `1.0.0${new Date().getTime()}`;
}
```
