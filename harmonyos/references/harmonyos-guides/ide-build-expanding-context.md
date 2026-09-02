---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-expanding-context
title: 插件上下文
breadcrumb: 指南 > 构建应用 > 扩展构建能力 > 扩展构建API > 插件上下文
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9623b1b672a7d9261b657f52d126b0b0360bade4e7ee871f30c2351883b1581c
---

## OhosPluginId

本组件是hvigor-ohos-plugin插件id常量类。

### 导入模块

```ts
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';
```

| 常量名 | 类型 | 描述 |
| --- | --- | --- |
| OHOS\_APP\_PLUGIN | string | AppPlugin插件ID |
| OHOS\_HAP\_PLUGIN | string | HapPlugin插件ID |
| OHOS\_HSP\_PLUGIN | string | HspPlugin插件ID |
| OHOS\_HAR\_PLUGIN | string | HarPlugin插件ID |

## OhosAppContext

本组件是appTasks插件对外提供的上下文扩展接口，包括工程信息、product信息等。

### 导入模块

```ts
import { OhosAppContext } from '@ohos/hvigor-ohos-plugin';
```

### getProjectName

getProjectName: () => string

获取工程名称。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 工程名称 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const projectName = appContext.getProjectName();
  console.log(`Project Name: ${projectName}`);
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getProjectPath

getProjectPath: () => string

获取工程路径。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 工程路径 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const projectPath = appContext.getProjectPath();
  console.log(`Project Path: ${projectPath}`);
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getBuildRootPath

getBuildRootPath: () => string

获取构建目录根路径。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 构建根路径 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const buildRootPath = appContext.getBuildRootPath();
  console.log(`Build Root Path: ${buildRootPath}`);
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getBuildProductOutputPath

getBuildProductOutputPath: () => string

获取当前product构建的打包输出路径。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前product构建的打包输出路径 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const buildProductOutputPath =  appContext.getBuildProductOutputPath();
  console.log(`Build Product Output Path: ${buildProductOutputPath}`);
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getCurrentProduct

getCurrentProduct: () => Product

获取当前构建指定的product对象。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Product](ide-hvigor-api.md#section1553414254713) | 当前构建指定的product对象 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const currentProduct = appContext.getCurrentProduct();
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getBuildMode

getBuildMode: () => string

获取当前构建指定的BuildMode。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前构建指定的BuildMode |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const buildMode = appContext.getBuildMode();
  console.log(`Build Mode: ${buildMode}`);
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getAppJsonOpt

getAppJsonOpt: () => AppJson.AppOptObj

获取当前构建的app.json5文件中内容的obj对象。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AppJson.AppOptObj](app-configuration-file.md) | 当前构建的app.json5文件中内容的obj对象 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const appJsonOpt =  appContext.getAppJsonOpt();
  console.log(`bundleName: ${appJsonOpt.app.bundleName}`);
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### setAppJsonOpt

setAppJsonOpt: (appJsonOpt: AppJson.AppOptObj) => void

修改当前构建的app.json5文件中内容的obj对象。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appJsonOpt | [AppJson.AppOptObj](app-configuration-file.md) | 是 | 设置当前构建的app.json5文件解析出来的obj对象 |

**说明** 

setAppJsonOpt会进行schema校验，如果传入的对象不符合校验规则则会抛出异常。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext, AppJson } from '@ohos/hvigor-ohos-plugin';
import { hvigor, getNode, HvigorNode  } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const node: HvigorNode = getNode(__filename);
  const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  console.log('projectName:', appContext.getProjectName());
  const appJson5: AppJson.AppOptObj = appContext.getAppJsonOpt();
  if (appContext.getBuildMode() === 'debug') {
    appJson5.app.versionName = '1.0.0-debug';
  } else {
    appJson5.app.versionName = '1.0.0-release';
  }
  appContext.setAppJsonOpt(appJson5);
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getBuildProfileOpt

getBuildProfileOpt: () => ProjectBuildProfile.ProjectProfileOpt

获取当前构建的根目录下build-profile.json5文件中内容的obj对象。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProjectBuildProfile.ProjectProfileOpt](ide-hvigor-build-profile-app.md) | 当前构建的根目录下build-profile.json5文件中内容的obj对象 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const buildProfileOpt = appContext.getBuildProfileOpt();
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### setBuildProfileOpt

setBuildProfileOpt: (buildProfileOpt: ProjectBuildProfile.ProjectProfileOpt) => void

设置当前构建的根目录下build-profile.json5文件中内容的obj对象。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buildProfileOpt | [ProjectBuildProfile.ProjectProfileOpt](ide-hvigor-build-profile-app.md) | 是 | 当前构建的根目录下build-profile.json5文件中内容的obj对象 |

**说明** 

* setBuildProfileOpt会进行schema校验，如果传入的对象不符合校验规则则会抛出异常。
* 不支持通过setBuildProfileOpt方法设置maxFlowDepth字段。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const buildProfileOpt = appContext.getBuildProfileOpt();
  // 添加一个工程外的模块
  const newModule = {
    "name": "har",
    "srcPath": "./../MyApplication40/har",// 确保该源码模块存在
  }
  buildProfileOpt.modules.push(newModule);
  appContext.setBuildProfileOpt(buildProfileOpt);
  console.log(buildProfileOpt.modules.map(module => {
    return module.name;
  }));
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getOhpmDependencyInfo

getOhpmDependencyInfo: () => Record<string, OhpmDependencyInfo> | object

获取工程下的依赖信息，包括dependencies和dynamicDependencies中的har和hsp。

**说明** 

在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)之前调用该接口获取的依赖信息不准确，后续使用依赖信息时可能会报错，建议使用[getOhpmDependencyInfoV2](ide-build-expanding-context.md#section1897251184819)接口替代。

**起始版本：**Hvigor 5.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [OhpmDependencyInfo](ide-build-expanding-context.md#section5282354105510)> | object | 工程下的依赖信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 自定义插件代码
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
      if (!rootNodeContext) {
        return;
      }
      const ohpmInfo = rootNodeContext.getOhpmDependencyInfo();
      console.log(ohpmInfo)
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getOhpmDependencyInfoV2

getOhpmDependencyInfoV2: () => Record<string, OhpmDependencyInfo>

获取工程下的依赖信息，包括dependencies和dynamicDependencies中的har和hsp。

**起始版本：**Hvigor 6.26.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [OhpmDependencyInfo](ide-build-expanding-context.md#section5282354105510)> | 工程下的依赖信息 |

**说明** 

通过该接口获取依赖信息，需要在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)完成之后执行，在此之前调用会报错。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';
// 自定义插件代码
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.taskGraphResolved(() => {
        const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
        if (!rootNodeContext) {
          return;
        }
        const ohpmInfo = rootNodeContext.getOhpmDependencyInfoV2();
        console.log(ohpmInfo)
      })
    }
  };
}
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getAllDependencyInfo

getAllDependencyInfo: () => Record<string, OhpmDependencyInfo>

获取工程下所有的依赖信息，包括dependencies和dynamicDependencies中的har、hsp、so、npm等。

**起始版本：**Hvigor 6.26.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [OhpmDependencyInfo](ide-build-expanding-context.md#section5282354105510)> | 工程下所有的依赖信息 |

**说明** 

通过该接口获取完整的依赖信息，需要在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)完成之后执行，在此之前调用会报错。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.taskGraphResolved(async () => {
        const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
        if (!rootNodeContext) {
          return;
        }
        const allDependencyInfo = rootNodeContext.getAllDependencyInfo();
        console.log(allDependencyInfo);
      })
    }
  };
}

export default {
  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getOhpmRemoteHspDependencyInfo

getOhpmRemoteHspDependencyInfo: (isSigned: boolean | undefined) => Record<string, OhpmDependencyInfo>

获取工程下的hsp包依赖信息，包括dependencies和dynamicDependencies中的hsp包依赖。

**说明** 

在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)之前调用该接口获取的依赖信息不准确，后续使用依赖信息时可能会报错，建议使用[getOhpmRemoteHspDependencyInfoV2](ide-build-expanding-context.md#section1697717782918)接口替代。

**起始版本：**Hvigor 5.6.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSigned | boolean | undefined | 否 | 是否获取签名的hsp包路径，默认为false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [OhpmDependencyInfo](ide-build-expanding-context.md#section5282354105510)> | 工程下的hsp包依赖信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosHapContext, OhosAppContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';

// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        // 注册模块级任务
        hapTask(currentNode);
      });
    }
  };
}
function hapTask(currentNode: HvigorNode) {
  // 等待全部节点加载完成之后获取子节点信息
  currentNode.subNodes((node: HvigorNode) => {
    // 获取hap模块上下文信息
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    const moduleName = hapContext?.getModuleName();
    hapContext?.targets((target: Target) => {
      const targetName = target.getTargetName();
      node.registerTask({
        // 任务名称
        name: `${targetName}@getRemoteHspInfo`,
        // 任务执行逻辑主体函数
        run() {
          const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
          if (!rootNodeContext) {
            return;
          }
          // 获取未签名的远程hsp相关信息
          const remoteHspInfo = rootNodeContext.getOhpmRemoteHspDependencyInfo(false);
          console.log(remoteHspInfo)
          // 获取已签名的远程hsp相关信息
          const signedRemoteHspInfo = rootNodeContext.getOhpmRemoteHspDependencyInfo(true);
          console.log(signedRemoteHspInfo)
        },
        // 配置前置任务依赖
        dependencies: [`${targetName}@PackageHap`],
        // 配置任务的后置任务依赖
        postDependencies: ['assembleHap']
      });
    });
  });
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
};
```

### getOhpmRemoteHspDependencyInfoV2

getOhpmRemoteHspDependencyInfoV2: (isSigned: boolean | undefined) => Record<string, OhpmDependencyInfo>

获取工程下的hsp包依赖信息，包括dependencies和dynamicDependencies中的hsp包依赖。

**起始版本：**Hvigor 6.26.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSigned | boolean | undefined | 否 | 是否获取签名的hsp包路径，默认为false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [OhpmDependencyInfo](ide-build-expanding-context.md#section5282354105510)> | 工程下的hsp包依赖信息 |

**说明** 

通过该接口获取依赖信息，需要在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)完成之后执行，在此之前调用会报错。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';
// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.taskGraphResolved(async () => {
        currentNode.subNodes((node: HvigorNode) => {
          // 获取hap模块上下文信息
          const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
          if (!hapNodeContext) {
            return
          }
          // 获取未签名的远程hsp相关信息
          const remoteHspInfo = hapNodeContext.getOhpmRemoteHspDependencyInfoV2(false);
          console.log(remoteHspInfo);
          // 获取已签名的远程hsp相关信息
          const signedRemoteHspInfo = hapNodeContext.getOhpmRemoteHspDependencyInfoV2(true);
          console.log(signedRemoteHspInfo);
        });
      });
    }
  };
}
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getDependenciesOpt

getDependenciesOpt: () => any

获取工程下oh-package.json5中配置的dependencies依赖。

**起始版本：**Hvigor 5.0.10

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any | 工程级别下oh-package.json5中的dependencies信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 自定义插件代码
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
      if (!rootNodeContext) {
        return;
      }
      const DependenciesInfo = rootNodeContext.getDependenciesOpt();
      console.log(DependenciesInfo)
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### setDependenciesOpt

setDependenciesOpt: (dependencies: any) => void

设置工程下oh-package.json5中的dependencies依赖。需要确保oh-package.json5中dependencies字段存在。

**起始版本：**Hvigor 5.0.10

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dependencies | any | 是 | 设置当前工程下oh-package.json5中dependencies依赖 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 自定义插件代码
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
      if (!rootNodeContext) {
        return;
      }
      const dependenciesInfo = rootNodeContext.getDependenciesOpt()
      dependenciesInfo["har"] = "./har";  // 确保依赖存在
      rootNodeContext.setDependenciesOpt(dependenciesInfo);
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getDevDependenciesOpt

getDevDependenciesOpt: () => any

获取工程下oh-package.json5中配置的devDependencies依赖。

**起始版本：**Hvigor 5.0.10

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any | 获取工程级别下oh-package.json5中devDependencies信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 自定义插件代码
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
      if (!rootNodeContext) {
        return;
      }
      const devDependenciesInfo = rootNodeContext.getDevDependenciesOpt();
      console.log(devDependenciesInfo)
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### setDevDependenciesOpt

setDevDependenciesOpt: (devDependencies: any) => void

设置工程下oh-package.json5中的devDependencies依赖。需要确保oh-package.json5中devDependencies字段存在。

**起始版本：**Hvigor 5.0.10

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| devDependencies | any | 是 | 设置当前工程下oh-package.json5中的devDependencies依赖 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 自定义插件代码
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
      if (!rootNodeContext) {
        return;
      }
      const devDependenciesInfo = rootNodeContext.getDevDependenciesOpt()
      devDependenciesInfo["har"] = "./har";  // 确保依赖存在
      rootNodeContext.setDevDependenciesOpt(devDependenciesInfo);
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getDynamicDependenciesOpt

getDynamicDependenciesOpt: () => any

获取工程下oh-package.json5中配置的dynamicDependencies依赖。

**起始版本：**Hvigor 5.0.10

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any | 获取工程级别下oh-package.json5中DynamicDependencies信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 自定义插件代码
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
      if (!rootNodeContext) {
        return;
      }
      const dynamicDependenciesInfo = rootNodeContext.getDynamicDependenciesOpt();
      console.log(dynamicDependenciesInfo)
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### setDynamicDependenciesOpt

setDynamicDependenciesOpt: (dynamicDependencies: any) => void

设置工程下oh-package.json5中的dynamicDependencies依赖。需要确保oh-package.json5中dynamicDependencies字段存在。

**起始版本：**Hvigor 5.0.10

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dynamicDependencies | any | 是 | 设置当前工程下oh-package.json5中dynamicDependencies依赖 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 自定义插件代码
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
      if (!rootNodeContext) {
        return;
      }
      const dynamicDependenciesInfo = rootNodeContext.getDynamicDependenciesOpt()
      dynamicDependenciesInfo["har"] = "./har";  // 确保依赖存在
      rootNodeContext.setDynamicDependenciesOpt(dynamicDependenciesInfo);
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getOverrides

getOverrides: () => any

获取工程下oh-package.json5中配置的overrides字段。

**起始版本：**Hvigor 5.10.3

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any | 获取工程下oh-package.json5中配置的overrides字段 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import {OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';
hvigor.afterNodeEvaluate(node => {
  const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  if (appContext) {
    let dependency = appContext.getOverrides() ?? {};
    console.log(dependency)
  }
});
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### setOverrides

setOverrides: (overrides: any) => void

设置工程下oh-package.json5中的overrides字段。

**起始版本：**Hvigor 5.10.3

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| overrides | any | 是 | 设置工程下oh-package.json5中的overrides字段 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import {OhosAppContext, OhosHapContext, OhosPluginId} from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';
hvigor.afterNodeEvaluate(node => {
  const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  if (appContext) {
    let dependency = appContext.getOverrides() ?? {};
    dependency['library'] = 'file:./library.har'; //在工程级oh-package.json5中动态添加工程内HAR包依赖
    appContext.setOverrides(dependency);
    return;
  }
  const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
  if (hapContext) {
    const dependency = hapContext.getDependenciesOpt();
    dependency['library'] = 'file:./../library';    //在entry上动态添加工程内模块依赖
    hapContext.setDependenciesOpt(dependency);
  }
});
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getSdkDetails

getSdkDetails: () => SdkDetails

获取SDK相关的信息。

**起始版本：**Hvigor 6.0.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SdkDetails](ide-hvigor-api.md#section1463642114714) | SDK相关的信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.afterNodeEvaluate(node => {
        const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
        if (appContext) {
          let sdk = appContext.getSdkDetails();
          console.log(sdk?.getSdkDir())
          console.log(sdk?.isOhos())
          console.log(sdk?.getSdkVersion())
          console.log(sdk?.getEtsComponentVersion())
          console.log(sdk?.getEtsComponentReleaseType())
        }
      });
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### isDebugLineEnable

isDebugLineEnable: () => Boolean

是否[启用debugLine](ide-run-debug-configurations.md#section21619254511)。

**起始版本**：Hvigor 6.22.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Boolean | 是否启用debugLine |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor } from '@ohos/hvigor';
import { appTasks, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  if (appContext) {
    const isDebugLineEnable = appContext.isDebugLineEnable();
    console.log(isDebugLineEnable)
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getAllModuleNameHash

getAllModuleNameHash: () => string

对工程名与所有模块名进行拼接，并计算哈希值。

**起始版本**：Hvigor 6.22.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 工程名和所有模块名拼接结果的哈希值 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor } from '@ohos/hvigor';
import { appTasks, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  if (appContext) {
    const allModuleNameHash = appContext.getAllModuleNameHash();
    console.log(allModuleNameHash)
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getFastBuildApp

getFastBuildApp: () => boolean

获取工程级build-profile.json5中fastBuildApp字段的值。

**起始版本**：Hvigor 6.22.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 工程级build-profile.json5中fastBuildApp字段的值 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor } from '@ohos/hvigor';
import { appTasks, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  if (appContext) {
    const fastBuildApp = appContext.getFastBuildApp();
    console.log(fastBuildApp)
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getAppWithSignedPkg

getAppWithSignedPkg: () => boolean

获取工程级build-profile.json5中appWithSignedPkg字段的值。

**起始版本**：Hvigor 6.22.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 工程级build-profile.json5中appWithSignedPkg字段的值 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor } from '@ohos/hvigor';
import { appTasks, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

hvigor.nodesEvaluated(() => {
  const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  if (appContext) {
    const appWithSignedPkg = appContext.getAppWithSignedPkg();
    console.log(appWithSignedPkg)
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

## OhosHapContext

hap模块Plugin提供的上下文接口，在hap模块的hvigor节点中可通过getContext方法传入OhosPluginId.OHOS\_HAP\_PLUGIN\_ID获取该接口，接口中主要包含了hap模块中module、target信息。

### 导入模块

```ts
import { OhosHapContext } from '@ohos/hvigor-ohos-plugin';
```

### getModuleName

getModuleName: () => string

获取模块名称。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 模块名称 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    const moduleName = hapContext?.getModuleName();
    console.log(`Module Name: ${moduleName}`);
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getModulePath

getModulePath: () => string

获取模块路径。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 模块路径 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    const modulePath = hapContext?.getModulePath();
    console.log(`Module Path: ${modulePath}`);
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getModuleType

getModuleType: () => string

获取模块类型，取值来自模块配置文件module.json5的type字段。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 模块类型 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    const moduleType = hapContext?.getModuleType();
    console.log(`Module Type: ${moduleType}`);
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getBuildProductRootPath

getBuildProductRootPath: () => string

获取模块基于product构建根路径。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 模块基于product构建根路径 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    const buildProductRootPath = hapContext?.getBuildProductRootPath();
    console.log(`Build Product Root Path: ${buildProductRootPath}`);
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### targets

targets: (callbackfn: (target: Target) => void) => void

当前需构建的target对象回调方法。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (target: [Target](ide-hvigor-api.md#section12392182963714)) => void | 是 | 入参类型为Target，返回类型为void的函数 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    hapContext?.targets((target: Target) => {
      // 这里可以写入对每个target的处理逻辑
      const targetName = target.getTargetName();
      console.log(`Target Name: ${targetName}`);
    });
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getBuildMode

getBuildMode: () => string

获取当前构建指定的BuildMode。

**起始版本：**Hvigor 5.18.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前构建指定的BuildMode |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    const buildMode = hapContext?.getBuildMode();
    console.log(`Build Mode: ${buildMode}`);
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getModuleJsonOpt

getModuleJsonOpt: () => ModuleJson.ModuleOptObj

获取当前模块的module.json5文件中内容的obj对象。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ModuleJson.ModuleOptObj](module-configuration-file.md) | 当前模块的module.json5文件中内容的obj对象 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    const moduleJsonOpt = hapContext?.getModuleJsonOpt();
    console.log(`Module Json Opt: ${JSON.stringify(moduleJsonOpt)}`);
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### setModuleJsonOpt

setModuleJsonOpt: (moduleJsonOpt: ModuleJson.ModuleOptObj) => void

修改当前构建的module.json5文件中的obj对象。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleJsonOpt | [ModuleJson.ModuleOptObj](module-configuration-file.md) | 是 | 设置当前模块的module.json5文件解析出来的obj对象 |

**说明** 

setModuleJsonOpt会进行schema校验，如果传入的对象不符合校验规则会抛出异常。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext; // 仅对hap模块生效，hsp和har需要使用模块对应接口
    const moduleJsonOpt = hapContext?.getModuleJsonOpt();
    moduleJsonOpt.module.deviceTypes = ["phone", "tablet"]; // 修改module.json5中的deviceTypes字段
    hapContext?.setModuleJsonOpt(moduleJsonOpt); // 更新module.json5
    console.log(`Module Json Opt: ${JSON.stringify(moduleJsonOpt)}`);
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getBuildProfileOpt

getBuildProfileOpt: () => ModuleBuildProfile.ModuleBuildOpt

获取当前模块的build-profile.json5文件中内容的obj对象。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ModuleBuildProfile.ModuleBuildOpt](ide-hvigor-build-profile.md) | 当前模块的build-profile.json5文件中内容的obj对象 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    const buildProfileOpt = hapContext?.getBuildProfileOpt();
    console.log(`Build Profile Opt: ${JSON.stringify(buildProfileOpt)}`);
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### setBuildProfileOpt

setBuildProfileOpt: (buildProfileOpt: ModuleBuildProfile.ModuleBuildOpt) => void

设置当前模块的build-profile.json5文件中内容的obj对象。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buildProfileOpt | [ModuleBuildProfile.ModuleBuildOpt](ide-hvigor-build-profile.md) | 是 | 当前模块的build-profile.json5文件中内容的obj对象 |

**说明** 

setBuildProfileOpt会进行schema校验，如果传入的对象不符合校验规则会抛出异常。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    const buildProfileOpt = hapContext?.getBuildProfileOpt();
    // 可以对buildProfileOpt进行修改
    buildProfileOpt?.targets?.push({
      "name": "default1",
    })
    hapContext?.setBuildProfileOpt(buildProfileOpt); // 更新buildProfileOpt
    console.log(`Build Profile Opt: ${JSON.stringify(buildProfileOpt)}`);
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getVersion

getVersion: () => string

获取模块oh-package.json5中配置的版本号。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 模块oh-package.json5中配置的版本号 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        currentNode.subNodes((node: HvigorNode) => {
          // 获取hap模块上下文信息
          // 如果是HAR或HSP，使用OHOS_HAR_PLUGIN/OHOS_HSP_PLUGIN
          const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
          if (!hapNodeContext) {
            return;
          }
          const moduleVersion = hapNodeContext.getVersion();
          console.log(moduleVersion);
        });
      });
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### setVersion

setVersion: (version: string) => void

修改模块oh-package.json5中的版本号。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | string | 是 | 修改模块oh-package.json5中的版本号 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        currentNode.subNodes((node: HvigorNode) => {
          // 获取hap模块上下文信息
          // 如果是HAR或HSP，使用OHOS_HAR_PLUGIN/OHOS_HSP_PLUGIN
          const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
          if (!hapNodeContext) {
            return;
          }
          hapNodeContext.setVersion('2.0.0');
          const moduleVersion = hapNodeContext.getVersion();
          console.log(moduleVersion);
        });
      });
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getOhpmDependencyInfo

getOhpmDependencyInfo: () => Record<string, OhpmDependencyInfo>

获取模块的依赖信息，包括dependencies和dynamicDependencies中的har和hsp。

**说明** 

在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)之前调用该接口获取的依赖信息不准确，后续使用依赖信息时可能会报错，建议使用[getOhpmDependencyInfoV2](ide-build-expanding-context.md#section1135681818322)接口替代。

**起始版本：**Hvigor 5.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [OhpmDependencyInfo](ide-build-expanding-context.md#section5282354105510)> | 模块的依赖信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        currentNode.subNodes((node: HvigorNode) => {
          // 获取hap模块上下文信息
          const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
          if (!hapNodeContext) {
            return;
          }
          const ohpmInfo = hapNodeContext.getOhpmDependencyInfo();
          console.log(ohpmInfo)
        });
      });
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getOhpmDependencyInfoV2

getOhpmDependencyInfoV2: () => Record<string, OhpmDependencyInfo>

获取模块的依赖信息，包括dependencies和dynamicDependencies中的har和hsp。

**起始版本：**Hvigor 6.26.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [OhpmDependencyInfo](ide-build-expanding-context.md#section5282354105510)> | 模块的依赖信息 |

**说明** 

通过该接口获取依赖信息，需要在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)完成之后执行，在此之前调用会报错。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.taskGraphResolved(async () => {
        currentNode.subNodes((node: HvigorNode) => {
          // 获取hap模块上下文信息
          const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
          if (!hapNodeContext) {
            return;
          }
          const ohpmInfo = hapNodeContext.getOhpmDependencyInfoV2();
          console.log(ohpmInfo)
        });
      });
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getAllDependencyInfo

getAllDependencyInfo: () => Record<string, OhpmDependencyInfo>

获取模块所有的依赖信息，包括dependencies和dynamicDependencies中的har、hsp、so、npm等。

**起始版本：**Hvigor 6.26.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [OhpmDependencyInfo](ide-build-expanding-context.md#section5282354105510)> | 模块所有的依赖信息 |

**说明** 

通过该接口获取完整的依赖信息，需要在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)完成之后执行，在此之前调用会报错。

**示例：**

```screen
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.taskGraphResolved(async () => {
        currentNode.subNodes((node) => {
            // 获取hap模块上下文信息
            const nodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN);
            if (!nodeContext) {
              return;
            }
            const allDependencyInfo = nodeContext.getAllDependencyInfo();
            console.log(allDependencyInfo);
          })
        }
      )
    }
  };
}

export default {
  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getOhpmRemoteHspDependencyInfo

getOhpmRemoteHspDependencyInfo: (isSigned: boolean | undefined) => Record<string, OhpmDependencyInfo>

获取模块的hsp包依赖信息，包括dependencies和dynamicDependencies中的hsp包依赖。

**说明** 

在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)之前调用该接口获取的依赖信息不准确，后续使用依赖信息时可能会报错，建议使用[getOhpmRemoteHspDependencyInfoV2](ide-build-expanding-context.md#section648452110518)接口替代。

**起始版本：**Hvigor 5.6.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSigned | boolean | undefined | 否 | 是否获取签名的hsp包路径，默认为false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [OhpmDependencyInfo](ide-build-expanding-context.md#section5282354105510)> | 模块下的hsp包依赖信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    context() {
      return {
        data: 'customPlugin xxx'
      };
    },
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        currentNode.subNodes((node: HvigorNode) => {
          // 获取hap模块上下文信息
          const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
          hapNodeContext?.targets((target: Target) => {
            const targetName = target.getTargetName();
            node.registerTask({
              // 任务名称
              name: `${targetName}@getRemoteHspInfo`,
              // 任务执行逻辑主体函数
              run() {
                // 获取未签名的远程hsp相关信息
                const remoteHspInfo = hapNodeContext.getOhpmRemoteHspDependencyInfo(false);
                console.log(remoteHspInfo);
                // 获取已签名的远程hsp相关信息
                const signedRemoteHspInfo = hapNodeContext.getOhpmRemoteHspDependencyInfo(true);
                console.log(signedRemoteHspInfo);
              },
              // 配置前置任务依赖
              dependencies: [`${targetName}@PackageHap`],
              // 配置任务的后置任务依赖
              postDependencies: ['assembleHap']
            });
          });
        });
      });
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getOhpmRemoteHspDependencyInfoV2

getOhpmRemoteHspDependencyInfoV2: (isSigned: boolean | undefined) => Record<string, OhpmDependencyInfo>

获取模块的hsp包依赖信息，包括dependencies和dynamicDependencies中的hsp包依赖。

**起始版本：**Hvigor 6.26.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSigned | boolean | undefined | 否 | 是否获取签名的hsp包路径，默认为false |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, [OhpmDependencyInfo](ide-build-expanding-context.md#section5282354105510)> | 模块下的hsp包依赖信息 |

**说明** 

通过该接口获取依赖信息，需要在[taskGraphResolved阶段](ide-hvigor-life-cycle.md#section746253616316)完成之后执行，在此之前调用会报错。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';
// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.taskGraphResolved(async () => {
        currentNode.subNodes((node: HvigorNode) => {
          // 获取hap模块上下文信息
          const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
          if (!hapNodeContext) {
            return
          }
          // 获取未签名的远程hsp相关信息
          const remoteHspInfo = hapNodeContext.getOhpmRemoteHspDependencyInfoV2(false);
          console.log(remoteHspInfo);
          // 获取已签名的远程hsp相关信息
          const signedRemoteHspInfo = hapNodeContext.getOhpmRemoteHspDependencyInfoV2(true);
          console.log(signedRemoteHspInfo);
        });
      });
    }
  };
}
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getDependenciesOpt

与OhosAppContext中的[getDependenciesOpt](ide-build-expanding-context.md#section1085223315215)方法一致，请参考上文中getDependenciesOpt接口描述。

### setDependenciesOpt

与OhosAppContext中的[setDependenciesOpt](ide-build-expanding-context.md#section18789410129)方法一致，请参考上文中getDependenciesOpt接口描述。

### getDevDependenciesOpt

与OhosAppContext中的[getDevDependenciesOpt](ide-build-expanding-context.md#section192992531393)方法一致，请参考上文中getDependenciesOpt接口描述。

### setDevDependenciesOpt

与OhosAppContext中的[setDevDependenciesOpt](ide-build-expanding-context.md#section8534132541914)方法一致，请参考上文中getDependenciesOpt接口描述。

### getDynamicDependenciesOpt

与OhosAppContext中的[getDynamicDependenciesOpt](ide-build-expanding-context.md#section3891011201117)方法一致，请参考上文中getDependenciesOpt接口描述。

### setDynamicDependenciesOpt

与OhosAppContext中的[setDynamicDependenciesOpt](ide-build-expanding-context.md#section2756613192210)方法一致，请参考上文中getDependenciesOpt接口描述。

### transformAbc

transformAbc: (fn: (abcPath: string, config: { isArkGuardEnabled: boolean }) => void | Promise<void>, targetName?: string) => void

注册在abc文件生成之后执行的回调函数。

**起始版本：**Hvigor 6.23.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (abcPath: string, config: { isArkGuardEnabled: boolean }) => void | Promise<void> | 是 | 注册在abc文件生成之后执行的回调函数。回调函数的参数说明：  abcPath: abc文件的绝对路径；  config: 模块相关的配置信息，当前仅支持  通过isArkGuardEnabled获取是否开启源码混淆的信息。 |
| targetName | string | 否 | 指定回调函数生效的target，未填写时对所有target生效。 |

**示例：**

```ts
// 模块级hvigorfile.ts文件
import { hapTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { OhosPluginId, OhosHapContext, Target } from "@ohos/hvigor-ohos-plugin";

// 自定义hvigor插件
function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    apply(node: HvigorNode) {
      hvigor.nodesEvaluated(() => {
        // 获取模块上下文
        const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
        if (!hapContext) {
          return;
        }

        // 定义TransformAbc的回调函数
        const callback = async (abcPath, config) => {
          console.log("abcPath", abcPath, "config", config);
        };

        // 场景一：不指定targetName，对所有target都注册回调函数
        hapContext.transformAbc(callback);

        // 场景二：遍历该模块支持的所有target，对指定target进行注册
        hapContext.targets((target: Target) => {
          if (target.getTargetName() === 'default') {
            hapContext.transformAbc(callback, target.getTargetName());
          }
        });
      });
    }
  }
}

export default {
  system: hapTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [customPlugin()]       /* Custom plugin to extend the functionality of Hvigor. */
}
```

### loadCompilePlugin

loadCompilePlugin: (path: string) => void

加载用户自定义的Rollup插件。

**起始版本：**Hvigor 5.8.9

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | Rollup插件路径 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    // compilePlugin.ts是自定义的Rollup插件，需替换成实际的插件路径
    hapContext?.loadCompilePlugin('../compilePlugin.ts');
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

新建compilePlugin.ts文件，和工程级hvigorfile.ts放在同一目录下。

```ts
// compilePlugin.ts
function customPlugin() {
  return {
    name: 'customPlugin',
    buildStart() {
      console.log('buildStart');
    }
  }
}

export default customPlugin();
```

### getTargetArtifactNames

getTargetArtifactNames: () => Map<string, string>

获取自定义的产物名称，即模块级build-profile.json5中targets下的artifactName值，如果未配置artifactName则返回空。

**起始版本：**Hvigor 6.22.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Map<string, string> | target和对应的artifactName值 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    const targetArtifactNames = hapContext?.getTargetArtifactNames();
    for (const [key, value] of targetArtifactNames) {
      console.log(`${key}: ${value}`);
    }
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getTargetArtifactName

getTargetArtifactName: (targetName: string) => string | undefined

获取指定target的产物名称，即模块级build-profile.json5中targets下的artifactName值，如果未配置artifactName则返回undefined。

**起始版本：**Hvigor 6.22.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| targetName | string | 是 | 模块指定target |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | undefined | 指定target的产物名称，不存在则返回undefined |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获得所有子节点
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    const targetArtifactName = hapContext?.getTargetArtifactName('default');
    console.log(targetArtifactName);
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

## OhosHspContext

Hsp模块上下文接口信息与OhosHapContext一致，请参考上文中OhosHapContext接口描述。

## OhosHarContext

Har模块上下文接口信息与OhosHapContext一致，请参考上文中OhosHapContext接口描述。

## OhpmDependencyInfo

工程中配置的依赖相关的信息，可以通过[getOhpmDependencyInfo](ide-build-expanding-context.md#section19083223370)、[getAllDependencyInfo](ide-build-expanding-context.md#section11559101173916)等方法来获取本对象。

| 成员 | 类型 | 只读 | 说明 | 开始支持的版本 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 依赖的名称。 | Hvigor 5.0.0 |
| version | string | 否 | 依赖的版本。 | Hvigor 5.0.0 |
| dependencies | Record<string, string> | 否 | 子依赖的名称和路径，例如A依赖B，B是A的子依赖。 | Hvigor 5.0.0 |
| packagePath | string | 否 | 依赖的路径。 | Hvigor 5.0.0 |
| remoteHspPath | string | 否 | 未签名的远程hsp路径，如果不存在则不返回该成员。 | Hvigor 5.6.2 |
| signedRemoteHspPath | string | 否 | 签名的远程hsp路径，如果不存在则不返回该成员。 | Hvigor 5.6.2 |
| dependencyType | string | 否 | 依赖的类型，包括har、hsp、so和other。 | Hvigor 6.26.1 |
