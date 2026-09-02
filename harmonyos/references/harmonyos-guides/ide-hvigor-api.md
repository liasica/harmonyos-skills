---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-api
title: 基础构建能力
breadcrumb: 指南 > 构建应用 > 扩展构建能力 > 扩展构建API > 基础构建能力
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:27+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3e42c33c6e244f52d622916b8c252d3bd34ce7847d7e692e3b914ad33be0f443
---

## Hvigor预置对象

"hvigor"对象是一个预定义的Hvigor对象，表示当前正在执行的Hvigor构建引擎的实例，通过"hvigor"对象可以获得有关构建的一些信息和操作。

### 导入模块

```ts
import { hvigor } from '@ohos/hvigor';
```

### getRootNode

getRootNode(): HvigorNode

获取根项目的节点对象。在[nodesInitialized和之后的阶段](ide-hvigor-life-cycle.md#section746253616316)才能使用，否则会报错。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNode](ide-hvigor-api.md#section14832104719474) | hvigor根节点对象 |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const rootNode = hvigor.getRootNode();
```

### getAllNodes

getAllNodes(): HvigorNode[]

获取所有节点对象的数组。在node初始化后才能使用，否则会报错。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNode](ide-hvigor-api.md#section14832104719474)[] | hvigor所有节点对象的数组 |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const allNodes = hvigor.getAllNodes();
```

### getNodeByName

getNodeByName(nodeName: string, classKind?: string): HvigorNode | undefined

根据节点名称获取节点对象。在node初始化后才能使用，否则会报错。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nodeName | string | 是 | 节点的名称，即工程名或模块名。 |
| classKind | string | 否 | 节点的类型。  当工程名和模块名相同时，可通过此参数指定获取工程或模块的节点对象。支持以下三种取值：   * project：当工程名和模块名相同时，返回工程的节点对象。 * module：当工程名和模块名相同时，返回模块的节点对象。 * node（缺省值）：当工程名和模块名相同时，返回模块的节点对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNode](ide-hvigor-api.md#section14832104719474) | undefined | 根据名称找到的节点对象，如果不存在则返回undefined |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const entryNode = hvigor.getNodeByName('entry');
```

### getHvigorConfig

getHvigorConfig(): HvigorConfig

获取HvigorConfig对象。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorConfig](ide-hvigor-api.md#section7253174081515) | HvigorConfig对象 |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const hvigorConfig = hvigor.getHvigorConfig();
```

### getParameter

getParameter(): Parameter

获取Parameter对象。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Parameter](ide-hvigor-api.md#section18886457152915) | Parameter对象 |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const parameter = hvigor.getParameter();
```

### getHvigorVersion

getHvigorVersion(): string

获取Hvigor的版本号。

**起始版本：**Hvigor 6.22.3

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Hvigor的版本号 |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const hvigorVersion = hvigor.getHvigorVersion();
```

### configEvaluated

configEvaluated(fn: (HvigorConfig) => {}): void

添加一个config文件评估完成的回调函数。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | ([HvigorConfig](ide-hvigor-api.md#section7253174081515)) => {} | 是 | 一个入参为空或者为hvigorConfig的方法 |

**说明** 

此API写在[hvigorconfig.ts文件](ide-hvigor-life-cycle.md#section810245135914)中才会生效，在构建生命周期的初始化阶段被执行。

**示例：**注册configEvaluated hook。

```ts
// hvigorconfig.ts文件
import { hvigor } from '@ohos/hvigor'
hvigor.configEvaluated(hvigorConfig => {
    console.log('configEvaluated');
})
```

### beforeNodeEvaluate

beforeNodeEvaluate(fn: (HvigorNode) => {}): void

为所有的node添加一个node评估前的回调函数。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | ([HvigorNode](ide-hvigor-api.md#section14832104719474)) => {} | 是 | 一个入参为空或者为HvigorNode的方法 |

**说明** 

此API写在[hvigorconfig.ts文件](ide-hvigor-life-cycle.md#section810245135914)中才会生效，在构建生命周期的初始化阶段被执行。

**示例：**注册beforeNodeEvaluate hook。

```ts
// hvigorconfig.ts文件
import { hvigor } from '@ohos/hvigor';
hvigor.beforeNodeEvaluate(hvigorNode => {
  console.log('beforeNodeEvaluate');
})
```

### afterNodeEvaluate

afterNodeEvaluate(fn: (HvigorNode) => {}): void

为所有的node添加一个node评估后的回调函数。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | ([HvigorNode](ide-hvigor-api.md#section14832104719474)) => {} | 是 | 一个入参为空或者为HvigorNode的方法 |

**示例：**注册afterNodeEvaluate hook。

```ts
import { hvigor } from '@ohos/hvigor';
hvigor.afterNodeEvaluate(hvigorNode => {
  console.log('afterNodeEvaluate');
})
```

### nodesInitialized

nodesInitialized(fn: (Hvigor) => {}): void

添加一个node初始化完成的回调函数。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | ([Hvigor](ide-hvigor-api.md#section64891890155)) => {} | 是 | 一个入参为空或者为Hvigor对象的方法 |

**说明** 

此API写在[hvigorconfig.ts文件](ide-hvigor-life-cycle.md#section810245135914)中才会生效，在构建生命周期的初始化阶段被执行。

**示例：**注册nodesInitialized hook。

```ts
// hvigorconfig.ts文件
import { hvigor } from '@ohos/hvigor';
hvigor.nodesInitialized(() => {
  console.log('nodesInitialized');
})
```

### nodesEvaluated

nodesEvaluated(fn: (Hvigor) => {}): void

添加hvigor配置阶段完成之后执行的回调函数，此函数在配置阶段结束之前使用方可有效。在配置阶段中接口使用场景例如节点插件上下文信息延迟获取、任务延迟注册等。添加的回调函数是以队列的形式存储，遵循先进先出原则，先添加的回调会先被执行。

**起始版本：**Hvigor 4.0.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | ([Hvigor](ide-hvigor-api.md#section64891890155)) => {} | 是 | 一个入参为空或者为Hvigor对象的方法 |

**示例：**工程节点获取子节点插件上下文信息。

在Hvigor中，工程节点插件加载要优先于模块节点插件加载顺序，若想实现在工程节点查找子节点注册task的上下文信息，则需要使用此接口，等待全部节点加载完成之后去执行。

```ts
import { hvigor } from '@ohos/hvigor';
import { OhosHapContext, OhosPluginId } from "@ohos/hvigor-ohos-plugin";
hvigor.nodesEvaluated(() => {
  // 等待全部节点加载完成之后获取子节点信息
  hvigor.getRootNode().subNodes(subNode => {
    const hapContext = subNode.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
  });
});
```

### taskGraphResolved

taskGraphResolved(fn: (Hvigor) => {}): void

添加一个任务图解析完毕的回调函数。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | ([Hvigor](ide-hvigor-api.md#section64891890155)) => {} | 是 | 一个入参为空或者为Hvigor对象的方法 |

**示例：**添加一个任务图解析完毕的回调函数。

```ts
import { hvigor } from '@ohos/hvigor';
hvigor.taskGraphResolved(() => {
  console.log('taskGraphResolved');
});
```

### buildFinished

buildFinished(fn: (BuildResult) => {}): void

添加一个构建结束的回调函数。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | ([BuildResult](ide-hvigor-api.md#section1476618469121)) => {} | 是 | 一个入参为空或者为BuildResult对象的方法 |

**示例：**获取构建结束的信息，如果是异常结束则打印出信息。

```ts
import { hvigor } from '@ohos/hvigor';
hvigor.buildFinished(buildResult => {
  if (buildResult.getError()) {
    console.log(buildResult.getError().stack);
  }
})
```

### getCommandEntryTask

getCommandEntryTask(): string[] | undefined

获取构建的入口任务名字符串数组。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | undefined | 构建的入口任务名字符串数组，如果不存在返回undefined |

**示例：**获取入口任务并打印出来。

```ts
import { hvigor } from '@ohos/hvigor';
console.log(hvigor.getCommandEntryTask());
```

### isCommandEntryTask

isCommandEntryTask(taskName: string): boolean

判断是否是命令入口任务。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskName | string | 是 | 任务名 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否是入口任务 |

**示例：**判断是否是assembleHap任务并打印出来。

```ts
import { hvigor } from '@ohos/hvigor';
console.log(hvigor.isCommandEntryTask('assembleHap'));
```

## getNode

getNode(scriptPath: string): HvigorNode | undefined

传入hvigorfile.ts脚本文件路径获取当前节点对象，如果入参scriptPath未指向本工程内的hvigorfile.ts则返回undefined。

**起始版本：**Hvigor 4.0.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scriptPath | string | 是 | hvigorfile.ts脚本全路径 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNode](ide-hvigor-api.md#section14832104719474) | undefined | hvigor节点对象，如果入参scriptPath未指向本工程内的hvigorfile.ts则返回undefined |

**示例：**获取当前节点对象。

```ts
import { getNode } from "@ohos/hvigor";
const node = getNode(__filename);
```

## BuildResult

代表构建结果的对象，如果是异常结束则会包含异常的信息。

### getError

getError(): Error | null

获取异常信息。没有异常则返回null。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Error | null | 异常信息。没有异常则为null。 |

**示例：**获取构建结束的信息，如果是异常结束则打印出信息。

```ts
import { hvigor } from '@ohos/hvigor';
hvigor.buildFinished(buildResult => {
  if (buildResult.getError()) {
    console.log(buildResult.getError().stack);
  }
})
```

### getReportJson

getReportJson(): any

获取本次构建的可视化记录report.json结果。

**起始版本：**Hvigor 5.0.10

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any | 本次构建的可视化记录report.json结果。 |

不同类型的构建事件具有不同结构，以下为典型结构示例：

```json5
// report.json
{
  "version": "2.0", // 固定字段
  "ppid": 524, // process.ppid
  "events": [ // 构建事件
    ...
    {
      "head": {
        "id": "61068546-11d9-49d0-baa7-733e167af7d6", // 事件id
        "name": "Finished :entry:default@PreBuild", // 事件name
        "description": "Pre-build in the stage model.",// 描述
        "type": "log" // 类型
      },
      "body": {
        "pid": 3960, // process.pid
        "tid": "Main Thread", // thread id
        "startTime": 1280741873226000, // 开始时间
        "endTime": 1280741896325200, // 结束时间
        "totalTime": 22868300 // 总计时间
      },
      "additional": {
        "logType": "info", // log类型
        "children": [], // 子事件id列表
      }
    }
  ],
  "workLog": []
}
```

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil } from '@ohos/hvigor';

hvigor.buildFinished(buildResult => {
  // 将数据写入指定path的文件中
  const json5FilePath = FileUtil.pathResolve('D:\\', 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFileSync(json5FilePath, JSON.stringify(buildResult.getReportJson(), null, 2));
})

export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

## HvigorConfig

HvigorConfig对象是在node对象被创建之前用来保存每个节点的描述信息的对象。

### getRootNodeDescriptor

getRootNodeDescriptor(): HvigorNodeDescriptor

获取RootNode的描述对象。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNodeDescriptor](ide-hvigor-api.md#section1914012226435) | 根节点的节点描述对象 |

**示例：**获取构建的所有节点描述对象。

```ts
import { hvigor } from '@ohos/hvigor';
const rootNodeDescriptor = hvigor.getHvigorConfig().getRootNodeDescriptor();
```

### getAllNodeDescriptor

getAllNodeDescriptor(): HvigorNodeDescriptor[]

获取所有的node描述对象的数组。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNodeDescriptor](ide-hvigor-api.md#section1914012226435)[] | 所有节点的节点描述对象 |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const allNodeDescriptors = hvigor.getHvigorConfig().getAllNodeDescriptor();
```

### getNodeDescriptorByName

getNodeDescriptorByName(name: string): HvigorNodeDescriptor

根据节点名称获取node描述对象。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 根据此name查找NodeDescriptor |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNodeDescriptor](ide-hvigor-api.md#section1914012226435) | 根据名称获取的节点描述对象 |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const entryNodeDescriptors = hvigor.getHvigorConfig().getNodeDescriptorByName('entry');
```

### includeNode

includeNode(name: string, srcPath: string, extraOptions?: Record<string, any>): void

添加一个node。

**起始版本：**Hvigor 5.4.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要添加的node的name |
| srcPath | string | 是 | 要添加的node的srcPath |
| extraOptions | Record<string, any> | 否 | 可以通过此参数传入额外的配置信息，会被解析成为此node的targets |

**说明** 

此API写在[hvigorconfig.ts文件](ide-hvigor-life-cycle.md#section810245135914)中才会生效，在构建生命周期的初始化阶段被执行。

**示例1：**添加一个名为exampleNodeName且无额外信息的node。

```screen
// hvigorconfig.ts文件
import { hvigor } from '@ohos/hvigor';

const hvigorConfig = hvigor.getHvigorConfig();
hvigorConfig.includeNode('exampleNodeName', './exampleNodeName');
```

**示例2：**添加一个名为exampleNodeName且附带targets信息的node。

```screen
// hvigorconfig.ts文件
import { hvigor } from '@ohos/hvigor';

const hvigorConfig = hvigor.getHvigorConfig();
hvigorConfig.includeNode('exampleNodeName', './exampleNodeName', {
  "targets": [
    {
      "name": "default",
      "applyToProducts": [
        "default"
      ]
    },
    {
      "name": "targetTest1",
      "applyToProducts": [
        "default"
      ]
    }
  ]
});
```

### excludeNodeByName

excludeNodeByName(name: string): void

通过name排除一个Node。

从DevEco Studio 6.0.0 Beta3版本开始，支持排除工程中不存在的模块，具体请参考[通过Hvigor执行ohpm install](ide-hvigor-experimental-properties.md#section11663628141317)。

**起始版本：**Hvigor 5.4.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要排除的node的name |

**说明** 

此API写在[hvigorconfig.ts文件](ide-hvigor-life-cycle.md#section810245135914)中才会生效，在构建生命周期的初始化阶段被执行。

**示例：**排除名为exampleNodeName的Node。

```screen
// hvigorconfig.ts文件
import { hvigor } from '@ohos/hvigor';

const hvigorConfig = hvigor.getHvigorConfig();
hvigorConfig.excludeNodeByName('exampleNodeName');
```

## HvigorNodeDescriptor

此对象为hvigor的节点描述对象，hvigor在构建时会通过此对象来构造出hvigorNode对象。

### 属性

| 成员 | 类型 | 只读 | 说明 | 开始支持的版本 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 节点的名称 | Hvigor 4.3.0 |
| srcPath | string | 否 | 节点的src路径 | Hvigor 4.3.0 |
| extraOptions | Map<string, any> | 否 | 自定义属性，用来保存传递数据 | Hvigor 4.3.0 |

### getChildNode

getChildNode(): HvigorNodeDescriptor[] | undefined

获取所有的子节点描述对象，不存在子节点则返回undefined。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNodeDescriptor](ide-hvigor-api.md#section1914012226435)[] | undefined | 所有的子节点描述对象，不存在子节点则返回undefined |

**示例：**

```ts
// hvigorconfig.ts
import { hvigorConfig } from '@ohos/hvigor';
const rootNodeDescriptors = hvigorConfig.getRootNodeDescriptor();
rootNodeDescriptors.getChildNode()?.forEach(child => {
  console.log(`child: ${child.name}`);
});
```

### getRootNode

getRootNode(): HvigorNodeDescriptor

获取根节点的节点描述对象。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNodeDescriptor](ide-hvigor-api.md#section1914012226435) | 根节点的节点描述对象 |

**示例：**

```screen
// hvigorconfig.ts
import { hvigorConfig } from '@ohos/hvigor';
const entryNodeDescriptor = hvigorConfig.getNodeDescriptorByName('entry');
console.log(`rootNode name: ${entryNodeDescriptor.getRootNode().name}`);
```

## Product

HarmonyOS应用工程级配置中的Product信息接口。在调用Product的接口前，可以先通过OhosAppContext的[getCurrentProduct](ide-build-expanding-context.md#section962214395515)方法来获取本对象。

### 导入模块

```ts
import { Product } from '@ohos/hvigor-ohos-plugin';
```

### getProductName

getProductName: () => string

获取product名称。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | product名称 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosAppContext, OhosPluginId, Product } from '@ohos/hvigor-ohos-plugin';
// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        const context: OhosAppContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
        const currentProduct: Product = context.getCurrentProduct();
        console.log(currentProduct.getProductName());
      });
    }
  };
}
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getBundleType

getBundleType: () => string

获取product使用的bundleType信息。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | bundleType值 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosAppContext, OhosPluginId, Product } from '@ohos/hvigor-ohos-plugin';
// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        const context: OhosAppContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
        const currentProduct: Product = context.getCurrentProduct();
        console.log(currentProduct.getBundleType());
      });
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getBundleName

getBundleName: () => string

获取product使用的bundleName信息。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | bundleName值 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosAppContext, OhosPluginId, Product } from '@ohos/hvigor-ohos-plugin';
// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        const context: OhosAppContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
        const currentProduct: Product = context.getCurrentProduct();
        console.log(currentProduct.getBundleName());
      });
    }
  };
}
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getOutputArtifactName

getOutputArtifactName: () => string | undefined

获取自定义的应用包名称，即工程级build-profile.json5中product下的artifactName值，如果未配置artifactName则返回undefined。

**起始版本：**Hvigor 6.22.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | undefined | 自定义的应用包名称，不存在则返回undefined |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosAppContext, OhosPluginId, Product } from '@ohos/hvigor-ohos-plugin';

// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        const context: OhosAppContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
        const currentProduct: Product = context.getCurrentProduct();
        console.log(currentProduct.getOutputArtifactName());
      });
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

## Target

HarmonyOS应用模块级配置中的Target信息接口。

### 导入模块

```ts
import { Target } from '@ohos/hvigor-ohos-plugin';
```

### getCurrentProduct

getCurrentProduct: () => Product

获取当前Target配置的Product。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Product](ide-hvigor-api.md#section1553414254713) | 当前构建target应用的Product对象 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    hapContext.targets((target: Target) => {
      // 这里可以写入对每个target的处理逻辑
      const currentProduct = target.getCurrentProduct();
      console.log(`Product Name: ${currentProduct.getProductName()}`);
    });
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getBuildTargetOutputPath

getBuildTargetOutputPath: () => string

获取当前target构建产物输出路径。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前target构建产物输出路径 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    hapContext.targets((target: Target) => {
      // 这里可以写入对每个target的处理逻辑
      const buildTargetOutputPath = target.getBuildTargetOutputPath();
      console.log(`Build Target Output Path: ${buildTargetOutputPath}`);
    });
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getTargetName

getTargetName: () => string

获取target名称。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | target名称 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    hapContext.targets((target: Target) => {
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

### getBuildOption

getBuildOption: () => BuildOption

获取模块target在本次构建过程中使用的buildOption信息。

**起始版本：**Hvigor 5.8.9

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BuildOption](ide-hvigor-build-profile.md#section1010733210421) | 模块target在本次构建过程中使用的buildOption信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    hapContext.targets((target: Target) => {
      // 这里可以写入对每个target的处理逻辑
      const buildOption = target.getBuildOption();
      console.log(`Build Option: ${JSON.stringify(buildOption, null, 2)}`);
    });
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getModulePathDetails

getModulePathDetails: () => PathDetails

获取模块级路径信息。

**起始版本：**Hvigor 6.0.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathDetails](ide-hvigor-api.md#section1182334313507) | 模块级路径信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    hapContext.targets((target: Target) => {
      // 这里可以写入对每个target的处理逻辑
      const modulePathDetails = target.getModulePathDetails();
      console.log(`Module Build Path: ${modulePathDetails.getModuleBuildPath()}`);
    });
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

## PathDetails

模块级路径信息。在调用PathDetails的接口前，可以先通过[getModulePathDetails](ide-hvigor-api.md#section5902751035)方法来获取本对象。

### getModuleBuildPath(): string

获取模块构建产物build根目录。

**起始版本：**Hvigor 6.0.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 模块构建产物build根目录，如"D:\MyApplication\entry\build"。 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    hapContext.targets((target: Target) => {
      // 这里可以写入对每个target的处理逻辑
      const modulePathDetails = target.getModulePathDetails();
      console.log(`Module Build Path: ${modulePathDetails.getModuleBuildPath()}`);
    });
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getModuleBuildCachePath(): string

获取模块构建中间产物缓存目录。

**起始版本：**Hvigor 6.0.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 模块构建中间产物缓存目录，如"D:\MyApplication\entry\build\default\cache\default"。 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    hapContext.targets((target: Target) => {
      // 这里可以写入对每个target的处理逻辑
      const modulePathDetails = target.getModulePathDetails();
      console.log(`Module Build Cache Path: ${modulePathDetails.getModuleBuildCachePath()}`);
    });
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getIntermediatesRes(): string

获取模块构建后生成的资源缓存目录。

**起始版本：**Hvigor 6.0.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 模块构建后生成的资源缓存目录，如"D:\MyApplication\entry\build\default\intermediates\res\default"。 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    if (!hapContext) {
      return
    }
    hapContext.targets((target: Target) => {
      // 这里可以写入对每个target的处理逻辑
      const modulePathDetails = target.getModulePathDetails();
      console.log(`Intermediates Res Path: ${modulePathDetails.getIntermediatesRes()}`);
    });
  });
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

## Parameter

“Parameter”是hvigor中的命令配置参数对象，可以通过[hvigor.getParameter()](ide-hvigor-api.md#section1349018305379)方法获取。

### getProperty

getProperty(key: string): any | undefined

获取properties配置指定key值的value值，若不存在配置时返回undefined。

**起始版本：**Hvigor 4.1.2

示例：获取properties配置中指定key值的value值。

* 命令行参数：--config properties.{key}={value}， 缩写-c properties.{key}={value}（相同key值时，命令行参数对应的value值优先）。
* hvigor-config.json5配置文件：在"properties"属性中定义的配置项。

  ```json5
  "properties": {
    "key": "value"
  }
  ```

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | properties配置中的key |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any | undefined | properties配置中指定key对应的value值（string，number, boolean类型），若不存在配置时返回undefined |

**示例：**

在hvigorfile.ts中添加代码。

```ts
import { hvigor } from '@ohos/hvigor';
const key = hvigor.getParameter().getProperty('key');
console.log(key);
```

执行命令hvigorw --sync -c properties.key=hello，控制台打印：

```txt
hello
```

### getProperties

getProperties(): Properties

获取properties所有配置的对象。

**起始版本：**Hvigor 4.1.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Properties | Properties配置对象 |

**示例：**

在hvigorfile.ts中添加代码。

```ts
import { hvigor } from '@ohos/hvigor';
const properties = hvigor.getParameter().getProperties();
console.log(properties['key']);
```

执行命令hvigorw --sync -c properties.key=hello，控制台打印：

```txt
hello
```

### setProperty

setProperty(key: string, value: any): void

设置properties对象指定key值的value值。

**起始版本：**Hvigor 5.10.3

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | hvigor-config.json5配置文件中properties字段的key值 |
| value | any | 是 | hvigor-config.json5配置文件中properties字段的key值对应的value值 |

**说明** 

在模块级hvigorfile.ts中调用该API不生效，请在工程级hvigorfile.ts中调用。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import {hvigor, HvigorPlugin} from '@ohos/hvigor';
import {appTasks} from '@ohos/hvigor-ohos-plugin';

export function plugin(): HvigorPlugin{
  console.log('before: ', hvigor.getParameter().getProperty('hvigor.analyzeHtml')); // undefined
  hvigor.getParameter().setProperty('hvigor.analyzeHtml', true);
  return {
    pluginId:'example',
    apply: (node) => {
      console.log('after: ', hvigor.getParameter().getProperty('hvigor.analyzeHtml')); // true
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [plugin()]         /* Custom plugin to extend the functionality of Hvigor. */
};
```

### getExtParam

getExtParam(key: string): string | undefined

获取指定key值的-p扩展参数value值，若不存在配置时返回undefined。

**起始版本：**Hvigor 4.1.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 命令行参数-p配置中的key |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | undefined | 指定key值对应的-p参数对应的value，配置不存在时undefined |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const extParam = hvigor.getParameter().getExtParam('key');
console.log(extParam);
```

执行命令hvigorw --sync -p key=hello，控制台打印：

```txt
hello
```

### getExtParams

getExtParams(): Record<string, string>

获取全部的-p扩展参数对象。

**起始版本：**Hvigor 4.1.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Record<string, string> | 命令行中所有配置的-p参数集合对象 |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const extParams = hvigor.getParameter().getExtParams();
console.log(extParams['key']);
```

执行命令hvigorw --sync -p key=hello，控制台打印：

```txt
hello
```

### getStartParams

getStartParams(): StartParam

获取hvigor启动参数：例如daemon开关，并行功能开关，增量功能开关，日志级别等。

**起始版本：**Hvigor 4.1.2

**返回值：**

| 类型 | 属性 | 说明 |
| --- | --- | --- |
| StartParams | daemon: boolean | 守护进程启用状态，true开启（默认开启）、false关闭 |
| StartParams | parallel: boolean | 并行编译能力启用状态，true开启（默认开启）、false关闭 |
| StartParams | incremental: boolean | 增量编译能力启用状态，true开启（默认开启）、false关闭 |
| StartParams | logLevel: string | 当前日志级别，info、debug、warn、error等 |
| StartParams | typeCheck: boolean | hvigorfile.ts的类型检查，true开启、false关闭（默认关闭） |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const startParams = hvigor.getParameter().getStartParams();
console.log(startParams['daemon']);
console.log(startParams['logLevel']);
```

### getWorkspaceDir

getWorkspaceDir(): string

获取Hvigor工作空间路径。工作空间是指当前工程对应的Hvigor插件安装在磁盘的位置。

**起始版本：**Hvigor 4.1.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Hvigor工作空间路径 |

**示例：**

```ts
import { hvigor } from '@ohos/hvigor';
const workspaceDir = hvigor.getParameter().getWorkspaceDir();
console.log(workspaceDir);
```

## HvigorNode

"HvigorNode"是hvigor中的节点模型接口，Hvigor工程中都有一个根模块对应的节点对象和每个子模块对应的节点对象，节点对象均为HvigorNode接口的实现。节点对象包含了该模块的配置，属性和任务等。

### 导入模块

```ts
import { HvigorNode } from '@ohos/hvigor';
```

### 获取实例

获取hvigorNode实例有多种方法，包括hvigor对象的[getRootNode](ide-hvigor-api.md#section10705432367)和[getAllNodes](ide-hvigor-api.md#section16393827185)方法、[getNode](ide-hvigor-api.md#section208181154171019)方法、HvigorPlugin的[apply](ide-hvigor-api.md#section2027815313120)方法都可以获取到hvigorNode实例。

以HvigorPlugin的apply方法为例，示例如下：

```ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';

// 实现自定义插件
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      // 通过currentNode可以使用hvigorNode的方法
    }
  };
}
```

### registerTask

registerTask: (task: HvigorTask) => void

在当前节点注册任务，在Hvigor生命周期中的配置阶段中执行。注册任务需完成HvigorTask的实现作为入参对象。

**起始版本：**Hvigor 4.0.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task | [HvigorTask](ide-hvigor-api.md#section2386634104512) | 是 | HvigorTask的实现 |

**示例：**

```ts
// node的获取方式请参考获取实例
node.registerTask({
  name: 'customTask',
  run() {
    console.log('this is Task');
  }
});
```

### getTaskByName

getTaskByName: (taskName: string) => Task | undefined

获取当前节点中已注册的Task对象。

**起始版本：**Hvigor 4.0.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskName | string | 是 | 任务名称 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Task](ide-hvigor-api.md#section2055582515349) | undefined | Task对象或undefined。当前节点未找到指定taskName的已注册任务时，返回值为undefined。 |

**示例：**

```screen
// node的获取方式请参考获取实例
node.getTaskByName('assembleApp')
```

### getNodeName

getNodeName: () => string

获取当前节点名称。

**起始版本：**Hvigor 4.0.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 节点名称 |

**示例：**

```ts
// node的获取方式请参考获取实例
const nodeName = node.getNodeName();
```

### getNodePath

getNodePath: () => string

获取当前节点路径。

**起始版本：**Hvigor 4.0.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 节点路径 |

**示例：**

```ts
// node的获取方式请参考获取实例
const nodePath = node.getNodePath();
```

### getParentNode

getParentNode: () => HvigorNode | undefined

获取父级节点对象。

**起始版本：**Hvigor 4.0.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNode](ide-hvigor-api.md#section14832104719474) | undefined | 节点对象或undefined |

**示例：**

```ts
// node的获取方式请参考获取实例
const parentNode = node.getParentNode();
```

### subNodes

subNodes: (callbackfn: (node: HvigorNode) => void) => void

遍历当前节点下的子节点执行回调函数。可通过此接口在工程节点操作节点对象。

补充：工程节点比模块节点优先加载，若需操作子节点，需使用hvigor.nodesEvaluated接口等待全部节点加载完成，才能操作子节点对象。

**起始版本：**Hvigor 4.0.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callbackfn | (node: [HvigorNode](ide-hvigor-api.md#section14832104719474)) => void | 是 | 入参类型为HvigorNode，返回类型为void的函数 |

**示例：**

```ts
// 工程级hvigorfile.ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor'
import { appTasks } from '@ohos/hvigor-ohos-plugin';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      currentNode.subNodes((node: HvigorNode) => {
        // 这里进行子节点相关处理
        // 比如获取子节点的名字
        const subNodeName = node.getNodeName();
      })
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getSubNodeByName

getSubNodeByName: (nodeName: string) => HvigorNode | undefined

根据节点名称获取节点对象。

**起始版本：**Hvigor 4.0.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| nodeName | string | 是 | 节点名称 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HvigorNode](ide-hvigor-api.md#section14832104719474) | undefined | 节点对象或undefined |

**示例：**

```ts
// 工程级hvigorfile.ts
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';

// 在项目根目录下的hvigorfile.ts中，currentNode是指app，子节点中包含entry
// 通过getSubNodeByName可以获取entry的对象
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const subNode = currentNode.getSubNodeByName('entry');
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getContext

getContext: (pluginId: string) => any

根据pluginId获取当前节点上指定插件的上下文接口信息。

**起始版本：**Hvigor 4.0.2

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pluginId | string | 是 | 插件ID |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any | 支持自定义返回值类型 |

**示例：**

```ts
// 工程级hvigorfile.ts
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, getNode, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

// 需要导入OhosPluginId，OhosAppContext来获得上下文信息
// 在生命周期hook中获取
hvigor.nodesEvaluated(() => {
  const node: HvigorNode = getNode(__filename);
  const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  // 这里就可以使用appContext获取以下上下文信息比如项目名
  console.log('projectName:', appContext.getProjectName());
});
// 或者在apply中直接获取
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const appContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
      console.log('projectName:', appContext.getProjectName());
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getAllPluginIds

getAllPluginIds: () => string[]

获取当前节点已加载的pluginId集合。

**起始版本：**Hvigor 4.0.2

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 当前已加载的插件ID集合 |

**示例：**

```ts
// 工程级hvigorfile.ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor'
import { appTasks } from '@ohos/hvigor-ohos-plugin';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const allPluginIds = currentNode.getAllPluginIds();
      allPluginIds.forEach((id) => {
        console.log(id);
      })
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### nodeDir

nodeDir: NormalizedFile

当前节点的根目录的NormalizedFile对象。

**起始版本：**Hvigor 4.3.0

### getNodeDir

getNodeDir: () => NormalizedFile

获取当前节点的根目录的NormalizedFile对象。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NormalizedFile](ide-hvigor-api.md#section281448112713) | 当前节点的根目录的NormalizedFile对象 |

**示例：**

```ts
// 工程级hvigorfile.ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin'

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      const dir = currentNode.getNodeDir();
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### addExtraOption

addExtraOption: (key: string, value: any) => void

为当前的node添加一个自定义属性。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要添加的自定义属性的key |
| value | any | 是 | 要添加的自定义属性的value |

**示例：**

```ts
// 工程级hvigorfile.ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin'

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      currentNode.addExtraOption('key', 'value');
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getExtraOption

getExtraOption: (key: string) => any

获取通过addExtraOption()函数设置在当前node上的自定义属性。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 自定义属性的key |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any | 自定义属性的value |

**示例：**

```ts
// 工程级hvigorfile.ts
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin'

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      currentNode.addExtraOption('key', 'value');
      currentNode.getExtraOption('key');
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### beforeNodeEvaluate

beforeNodeEvaluate(fn: (HvigorNode) => {}): void

为当前的node添加一个node评估前的回调函数。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | ([HvigorNode](ide-hvigor-api.md#section14832104719474)) => {} | 是 | 一个入参为空或者为HvigorNode的方法 |

**示例：**为名称为entry的node注册一个beforeNodeEvaluate hook并打印出node的信息。

```ts
import { hvigor } from '@ohos/hvigor';
hvigor.nodesInitialized(() => {
  hvigor.getRootNode().subNodes(node => {
    if (node.getNodeName() === 'entry') {
      node.beforeNodeEvaluate(hvigorNode => {
        console.log(hvigorNode.getNodeName());
      })
    }
  })
});
```

### afterNodeEvaluate

afterNodeEvaluate(fn: (HvigorNode) => {}): void

为当前的node添加一个node评估后的回调函数。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | ([HvigorNode](ide-hvigor-api.md#section14832104719474)) => {} | 是 | 一个入参为空或者为HvigorNode的方法 |

**示例：**为名称为entry的node注册一个afterNodeEvaluate hook并打印出node的信息。

```ts
import { hvigor } from '@ohos/hvigor';
hvigor.nodesInitialized(() => {
  hvigor.getRootNode().subNodes(node => {
    if (node.getNodeName() === 'entry') {
      node.afterNodeEvaluate(hvigorNode => {
        console.log(hvigorNode.getNodeName());
      })
    }
  })
});
```

## HvigorPlugin

该接口定义了Hvigor开发插件的基本范式。开发Hvigor插件需实现此接口。

### 导入模块

```ts
import { HvigorPlugin } from '@ohos/hvigor';
```

### pluginId

pluginId: string

插件唯一标识属性。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';

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
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: [customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### context

context?: (() => any) | any

插件上下文实现接口，可选实现；实现此函数后，其他插件可通过node.getContext('插件ID'）获取插件中定义的上下文接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (() => any) | any | 自定义返回类型的Function或自定义任一返回类型 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';

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
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### apply

apply: (node: HvigorNode) => void | Promise<void>

插件主体函数，用于定义插件实现逻辑（例如任务注册等）; 在Hvigor的生命周期配置阶段调用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [HvigorNode](ide-hvigor-api.md#section14832104719474) | 是 | hvigor节点对象 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | 无返回值，或返回Promise<void>类型 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';

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
      });
    }
  };
}

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
};
```

## HvigorTask

Hvigor任务实现的接口类型，定义了任务的实现范式，在创建任务时需实现此接口。

### 导入模块

```ts
import { HvigorTask } from '@ohos/hvigor';
```

### name

name: string

定义任务名称。

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// 获取当前hvigorNode节点对象
const node: HvigorNode = getNode(__filename);
// 注册Task
node.registerTask({
  name: 'customTask',
  run() {
    console.log('this is Task');
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### context

context?: (() => any) | any

任务中的局部内数据共享的对象定义。实现此函数中定义的对象将在任务注册时被注入到this.context属性上，在input、output、run函数中可使用直接this.context调用context函数中定义的对象和属性。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (() => any) | any | 自定义返回类型的Function或自定义任一返回类型 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// 获取当前hvigorNode节点对象
const node: HvigorNode = getNode(__filename);
// 注册Task
node.registerTask({
  name: 'customTask',
  context() {
    return {
      data: 'customRegisterTask xxx'
    };
  },
  run() {
    console.log(this.context);
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### input

input?: (input: TaskInput) => void

实现任务增量输入条件定义。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | [TaskInput](ide-hvigor-api.md#section425723621113) | 是 | 控制任务增量的输入条件实现对象 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";

const currentNode = getNode(__filename);

hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const outputFilePath = path.resolve(context.getBuildRootPath(), 'test.txt');
  // 注册一个生成文件的任务并为此任务设置增量
  currentNode.registerTask({
    name: "testTask",
    run(taskContext: HvigorTaskContext): void | Promise<void> {
      fse.writeFileSync(outputFilePath, context.getProjectName());
      return undefined;
    },
    input(input: TaskInput): void {
      input.property('projectName', context.getProjectName());
    },
    async output(output: TaskOutput): Promise<void> {
      try {
        const parentDir = path.dirname(outputFilePath);
        await fse.ensureDir(parentDir); // 确保父目录存在
        await fse.ensureFile(outputFilePath);
        output.file(outputFilePath);
      } catch (error) {
        console.error('File creation failed:', error);
        throw error;
      }
    },
    postDependencies: ['assembleApp']
  })
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

需要在hvigor-config.json5中添加dependencies：

```json5
// hvigor-config.json5
"dependencies": {
  "fs-extra": "11.2.0",
  "@types/fs-extra": "9.0.13"
},
```

### output

output?: (output: TaskOutput) => void

实现任务增量输出条件定义。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| output | [TaskOutput](ide-hvigor-api.md#section135442202125) | 是 | 控制任务增量的输出条件实现对象 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";

const currentNode = getNode(__filename);

hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const outputFilePath = path.resolve(context.getBuildRootPath(), 'test.txt');
  // 注册一个生成文件的任务并为此任务设置增量
  currentNode.registerTask({
    name: "testTask",
    run(taskContext: HvigorTaskContext): void | Promise<void> {
      fse.writeFileSync(outputFilePath, context.getProjectName());
      return undefined;
    },
    input(input: TaskInput): void {
      input.property('projectName', context.getProjectName());
    },
    async output(output: TaskOutput): Promise<void> {
      try {
        const parentDir = path.dirname(outputFilePath);
        await fse.ensureDir(parentDir); // 确保父目录存在
        await fse.ensureFile(outputFilePath);
        output.file(outputFilePath);
      } catch (error) {
        console.error('File creation failed:', error);
        throw error;
      }
    },
    postDependencies: ['assembleApp']
  })
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

需要在hvigor-config.json5里添加dependencies：

```json5
// hvigor-config.json5
"dependencies": {
  "fs-extra": "11.2.0",
  "@types/fs-extra": "9.0.13"
},
```

### run

run: (taskContext: HvigorTaskContext) => void | Promise<void>

任务执行逻辑主体函数。您可以在此函数实现中定义您所需的任务处理逻辑。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskContext | [HvigorTaskContext](ide-hvigor-api.md#section17880854104213) | 否 | 接口中默认注入的公共信息类型 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | 无返回值，或返回Promise<void>类型 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// 获取当前hvigorNode节点对象
const node: HvigorNode = getNode(__filename);
// 注册Task
node.registerTask({
  name: 'customTask',
  run() {
    console.log('this is Task');
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### beforeRun

beforeRun?: (taskContext: HvigorTaskContext) => void | Promise<void>

run函数的前置处理函数。在任务执行阶段，任务中的run函数执行前此函数被调用执行。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskContext | [HvigorTaskContext](ide-hvigor-api.md#section17880854104213) | 否 | 接口中默认注入的公共信息 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | 无返回值，或返回Promise<void>类型 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// 获取当前hvigorNode节点对象
const node: HvigorNode = getNode(__filename);
// 注册Task
node.registerTask({
  name: 'customTask',
  run() {
    console.log('customTask');
  },
  beforeRun() {
    console.log('beforeRun');
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### afterRun

afterRun?: (taskContext: HvigorTaskContext) => void | Promise<void>

run函数的后置处理函数。在任务执行阶段，任务中的run函数执行后此函数被调用执行。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| taskContext | [HvigorTaskContext](ide-hvigor-api.md#section17880854104213) | 否 | 接口中默认注入的公共信息类型 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | 无返回值，或返回Promise<void>类型 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// 获取当前hvigorNode节点对象
const node: HvigorNode = getNode(__filename);
// 注册Task
node.registerTask({
  name: 'customTask',
  run() {
    console.log('customTask');
  },
  afterRun() {
    console.log('afterRun');
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### dependencies

dependencies?: (() => string[]) | string[]

配置前置任务依赖。前置任务依赖是指当前任务依赖另一个任务，执行顺序是前置任务 -> 当前任务 -> 后置任务。

从DevEco Studio 6.0.0 Beta2版本开始，支持依赖其他模块的任务，在任务前加上“模块名:”即可，例如har:assembleHar。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (() => string[]) | string[] | 返回类型为string[]的函数或string[]类型 |

**说明** 

依赖其他模块的任务时，建议将任务注册操作放在[hook-nodesEvaluated](ide-hvigor-life-cycle.md#section746253616316)中，否则注册时其他模块的任务可能还未被初始化，导致当前任务无法注册。

**示例一：**依赖本模块的任务。

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// 获取当前hvigorNode节点对象
const node: HvigorNode = getNode(__filename);
// 注册Task
node.registerTask({
  name: 'customTask',
  run() {
    console.log('customTask');
  },
  dependencies: ['customTask1'],
});
// 注册Task
node.registerTask({
  name: 'customTask1',
  run() {
    console.log('customTask1');
  },
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

**示例二：**依赖其他模块的任务。

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

// 获取当前entry节点对象
const entryNode = hvigor.getNodeByName('entry');

// 逻辑放在hook-nodesEvaluated中
hvigor.nodesEvaluated(async () => {
  // 注册任务
  entryNode.registerTask({
    // 任务名称
    name: `default@CustomTask`,
    run() {
      console.log('customTask1')
    },
    // 配置前置任务依赖
    dependencies: ['har:assembleHar'], // 跨模块依赖har的assembleHar任务，确保har模块存在
    // 配置任务的后置任务依赖
    postDependencies: ['entry:default@PreBuild']  // 支持两种写法 entry:default@PreBuild  default@PreBuild
  });
});

export default {
  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: []       /* Custom plugin to extend the functionality of Hvigor. */
}
```

### postDependencies

postDependencies?: (() => string[]) | string[]

配置任务的后置任务依赖。后置任务依赖是指另一个任务依赖当前任务，执行顺序是前置任务 -> 当前任务 -> 后置任务。

从DevEco Studio 6.0.0 Beta2版本开始，支持依赖其他模块的任务，在任务前加上“模块名:”即可，例如har:default@PreBuild。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| (() => string[]) | string[] | 返回类型为string[]的函数或string[]类型 |

**说明** 

依赖其他模块的任务时，建议将任务注册操作放在[hook-nodesEvaluated](ide-hvigor-life-cycle.md#section746253616316)中，否则注册时其他模块的任务可能还未被初始化，导致当前任务无法注册。

**示例一：**依赖本模块的任务。

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

// 获取当前hvigorNode节点对象
const node: HvigorNode = getNode(__filename);
// 注册Task
node.registerTask({
  name: 'customTask1',
  run() {
    console.log('customTask1');
  },
});
// 注册Task
node.registerTask({
  name: 'customTask',
  run() {
    console.log('customTask');
  },
  postDependencies: ['customTask1'],
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

**示例二：**依赖其他模块的任务。

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

// 获取当前entry节点对象
const entryNode = hvigor.getNodeByName('entry');

// 逻辑放在hook-nodesEvaluated中
hvigor.nodesEvaluated(async () => {
  // 注册任务
  entryNode.registerTask({
    // 任务名称
    name: `default@CustomTask`,
    run() {
      console.log('customTask1')
    },
    // 配置前置任务依赖
    dependencies: ['entry:default@PreBuild'], // 支持两种写法 entry:default@PreBuild  default@PreBuild
    // 配置任务的后置任务依赖
    postDependencies: ['har:default@PreBuild']  // 跨模块依赖har的PreBuild任务，确保har模块存在
  });
});

export default {
  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: []       /* Custom plugin to extend the functionality of Hvigor. */
}
```

## HvigorTaskContext

Hvigor任务上下文对象类型，该类型的对象默认注册了当前任务的上下文信息。

### 属性

| 成员 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| moduleName | string | 是 | 当前任务绑定的模块名称 |
| modulePath | string | 是 | 当前任务绑定的模块路径 |

## TaskInput

任务增量执行判断的输入对象实现类型，提供添加任务输入条件的基本函数。

### 导入模块

```ts
import { TaskInput } from '@ohos/hvigor';
```

### property

property(key: string, value: TaskInputValue): TaskInput

添加键值对作为Task增量输入条件。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 条件名称 |
| value | TaskInputValue | 是 | 支持基本数组类型number、string、boolean及对应的数组类型的参数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TaskInput](ide-hvigor-api.md#section425723621113) | 当前控制任务增量的输入条件对象，用于链式调用 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTask, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const outputFilePath = path.resolve(context.getBuildRootPath(), 'test.txt');
  // 注册一个生成文件的任务并为此任务设置增量
  currentNode.registerTask({
    name: "testTask",
    run(taskContext: HvigorTaskContext): void | Promise<void> {
      fse.writeFileSync(outputFilePath, context.getProjectName());
      return undefined;
    },
    input(input: TaskInput): void {
      input.property('projectName', context.getProjectName());
    },
    async output(output: TaskOutput): Promise<void> {
      try {
        const parentDir = path.dirname(outputFilePath);
        await fse.ensureDir(parentDir); // 确保父目录存在
        await fse.ensureFile(outputFilePath);
        output.file(outputFilePath);
      } catch (error) {
        console.error('File creation failed:', error);
        throw error;
      }
    },
    postDependencies: ['assembleApp']
  })
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

需要在hvigor-config.json5中添加dependencies：

```json5
// hvigor-config.json5
"dependencies": {
  "fs-extra": "11.2.0",
  "@types/fs-extra": "9.0.13"
},
```

### file

file(path: string): TaskInput

添加单个目录或文件路径作为任务增量输入条件。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录或文件路径 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TaskInput](ide-hvigor-api.md#section425723621113) | 当前控制任务增量的输入条件对象，用于链式调用 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTask, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const outputFilePath = path.resolve(context.getBuildRootPath(), 'testOutput.txt');
  // 添加单个文件路径作为任务增量输入条件
  const inputFilePath = path.resolve(context.getProjectPath(), 'testInput.txt');
  // 注册一个生成文件的任务并为此任务设置增量
  currentNode.registerTask({
    name: "testTask",
    run(taskContext: HvigorTaskContext): void | Promise<void> {
      const parentDir = path.dirname(outputFilePath);
      fse.ensureDirSync(parentDir); // 确保父目录存在
      fse.ensureFileSync(outputFilePath);
      fse.writeFileSync(outputFilePath, context.getProjectName());
      return undefined;
    },
    input(input: TaskInput): void {
      input.property('projectName', context.getProjectName());
      if (fse.existsSync(inputFilePath)) {
        input.file(inputFilePath);
      }
    },
    async output(output: TaskOutput): Promise<void> {
      output.file(outputFilePath);
    },
    postDependencies: ['assembleApp']
  })
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

需要在hvigor-config.json5中添加dependencies：

```json5
// hvigor-config.json5
"dependencies": {
  "fs-extra": "11.2.0",
  "@types/fs-extra": "9.0.13"
},
```

### files

files(paths: string[]): TaskInput

添加多个目录或文件路径作为任务增量输入条件。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| paths | string | 是 | 目录或文件路径列表 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TaskInput](ide-hvigor-api.md#section425723621113) | 当前控制任务增量的输入条件对象，用于链式调用 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTask, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const outputFilePath = path.resolve(context.getBuildRootPath(), 'test.txt');
  // 添加单个文件路径作为任务增量输入条件
  const inputFilePath = path.resolve(context.getProjectPath(), 'test.txt');
  // 注册一个生成文件的任务并为此任务设置增量
  currentNode.registerTask({
    name: "testTask",
    run(taskContext: HvigorTaskContext): void | Promise<void> {
      const parentDir = path.dirname(outputFilePath);
      fse.ensureDirSync(parentDir); // 确保父目录存在
      fse.ensureFileSync(outputFilePath);
      fse.writeFileSync(outputFilePath, context.getProjectName());
      return undefined;
    },
    input(input: TaskInput): void {
      input.property('projectName', context.getProjectName());
      if (fse.existsSync(inputFilePath)) {
        input.files([inputFilePath, ]);
      }
    },
    async output(output: TaskOutput): Promise<void> {
      output.files([outputFilePath,]);
    },
    postDependencies: ['assembleApp']
  })
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

需要在hvigor-config.json5中添加dependencies：

```screen
// hvigor-config.json5
"dependencies": {
  "fs-extra": "11.2.0",
  "@types/fs-extra": "9.0.13"
},
```

## TaskOutput

任务增量执行判断的输出对象实现类型，提供添加任务输出条件的基本函数。

### 导入模块

```ts
import { TaskOutput } from '@ohos/hvigor';
```

### file

file(path: string): TaskOutput

添加单个目录或文件路径作为任务的增量输出条件。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 目录或文件路径 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TaskOutput](ide-hvigor-api.md#section135442202125) | 当前控制任务增量的输出条件对象，用于支持链式调用 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const outputFilePath = path.resolve(context.getBuildRootPath(), 'testOutput.txt');
  // 添加单个文件路径作为任务增量输入条件
  const inputFilePath = path.resolve(context.getProjectPath(), 'testInput.txt');
  // 注册一个生成文件的任务并为此任务设置增量
  currentNode.registerTask({
    name: "testTask",
    run(taskContext: HvigorTaskContext): void | Promise<void> {
      const parentDir = path.dirname(outputFilePath);
      fse.ensureDirSync(parentDir); // 确保父目录存在
      fse.ensureFileSync(outputFilePath);
      fse.writeFileSync(outputFilePath, context.getProjectName());
      return undefined;
    },
    input(input: TaskInput): void {
      input.property('projectName', context.getProjectName());
      if (fse.existsSync(inputFilePath)) {
        input.file(inputFilePath);
      }
    },
    async output(output: TaskOutput): Promise<void> {
      output.file(outputFilePath);
    },
    postDependencies: ['assembleApp']
  })
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

需要在hvigor-config.json5中添加dependencies：

```screen
// hvigor-config.json5
"dependencies": {
  "fs-extra": "11.2.0",
  "@types/fs-extra": "9.0.13"
},
```

### files

files(paths: string[]): TaskOutput

添加多个目录或文件路径作为任务的增量输出条件。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| paths | string[] | 是 | 目录或文件路径列表 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TaskOutput](ide-hvigor-api.md#section135442202125) | 控制任务增量的输出条件对象，用于支持链式调用 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorTaskContext, TaskInput, TaskOutput } from "@ohos/hvigor";
import fse from "fs-extra";
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const outputFilePath = path.resolve(context.getBuildRootPath(), 'testOutput.txt');
  // 添加单个文件路径作为任务增量输入条件
  const inputFilePath = path.resolve(context.getProjectPath(), 'testInput.txt');
  // 注册一个生成文件的任务并为此任务设置增量
  currentNode.registerTask({
    name: "testTask",
    run(taskContext: HvigorTaskContext): void | Promise<void> {
      const parentDir = path.dirname(outputFilePath);
      fse.ensureDirSync(parentDir); // 确保父目录存在
      fse.ensureFileSync(outputFilePath);
      fse.writeFileSync(outputFilePath, context.getProjectName());
      return undefined;
    },
    input(input: TaskInput): void {
      input.property('projectName', context.getProjectName());
      if (fse.existsSync(inputFilePath)) {
        input.files([inputFilePath, ]);
      }
    },
    async output(output: TaskOutput): Promise<void> {
      output.files([outputFilePath,]);
    },
    postDependencies: ['assembleApp']
  })
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

需要在hvigor-config.json5中添加dependencies：

```json5
// hvigor-config.json5
"dependencies": {
  "fs-extra": "11.2.0",
  "@types/fs-extra": "9.0.13"
},
```

## Task

HvigorTask的外置对象。您可以使用此对象访问任务的属性、 操作任务提供的接口函数。

### 导入模块

```ts
import { Task } from '@ohos/hvigor';
```

### getName

getName: () => string

获取任务名称。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 任务名称 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
  if (assembleAppTask) {
    const taskName = assembleAppTask.getName();
    console.log(`taskName: ${taskName}`);
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getDependencies

getDependencies: () => string[]

获取当前任务依赖的前置任务名称列表。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] | 当前任务依赖的前置任务名称列表 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
  if (assembleAppTask) {
    const taskDependencies = assembleAppTask.getDependencies();
    console.log(`Task Dependencies: ${taskDependencies}`);
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### setEnable

setEnable: (enable: boolean) => void

设置任务的启用状态，当任务被禁用时，任务仍然在任务依赖图中存在，仅跳过了任务的执行，不会破坏原来设定的任务依赖关系。任务被注册时任务状态默认是启用的。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | true：启用任务， false: 禁用任务 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';
hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  rootNode.subNodes((node: HvigorNode) => {
    // 获取hap模块上下文信息
    const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    const moduleName = hapContext?.getModuleName();
    hapContext?.targets((target: Target) => {
      // 禁用任务
      node.getTaskByName(`${target.getTargetName()}@SignHap`)?.setEnable(false);
    });
  });
});
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### beforeRun

beforeRun: (fn: Function) => void

添加任务执行之前的钩子函数。钩子函数以栈结构存储，遵循先进后出原则，后添加的函数先被执行。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | Function | 是 | 回调函数 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
  if (assembleAppTask) {
    // 任务执行之前的钩子函数
    assembleAppTask.beforeRun(() => {
      console.log('Before Task: assembleApp');
    });
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### afterRun

afterRun: (fn: Function) => void

添加任务执行完成之后的钩子函数。钩子函数以堆结构存储，遵循先进先出原则，先添加的函数先被执行。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | Function | 是 | 回调函数 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
  if (assembleAppTask) {
    // 任务执行之后的钩子函数
    assembleAppTask.afterRun(() => {
      console.log('After Task: assembleApp');
    });
  }
});

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

## SdkDetails

应用工程使用的SDK相关的信息。在调用SdkDetails的接口前，可以先通过OhosAppContext的[getSdkDetails](ide-build-expanding-context.md#section085712212299)方法来获取本对象。

### 导入模块

```ts
import { SdkDetails } from '@ohos/hvigor-ohos-plugin';
```

### getSdkDir

getSdkDir: () => string

获取SDK所在目录。

**起始版本：**Hvigor 6.0.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | SDK所在目录 |

在工程级hvigorfile.ts中编写示例代码：

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosAppContext, OhosPluginId, SdkDetails } from '@ohos/hvigor-ohos-plugin';
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
          let sdk:SdkDetails = appContext.getSdkDetails();
          console.log(sdk?.getSdkDir())
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

### isOhos

isOhos: () => boolean

判断是否为OpenHarmony SDK。

**起始版本：**Hvigor 6.0.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否为OpenHarmony SDK |

在工程级hvigorfile.ts中编写示例代码：

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosAppContext, OhosPluginId, SdkDetails } from '@ohos/hvigor-ohos-plugin';
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
          let sdk:SdkDetails = appContext.getSdkDetails();
          console.log(sdk?.isOhos())
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

### getSdkVersion

getSdkVersion: () => number

获取SDK的版本号。

**起始版本：**Hvigor 6.0.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | SDK版本号 |

在工程级hvigorfile.ts中编写示例代码：

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosAppContext, OhosHapContext, OhosPluginId, SdkDetails } from '@ohos/hvigor-ohos-plugin';
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
          let sdk:SdkDetails = appContext.getSdkDetails();
          console.log(sdk?.getSdkVersion())
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

### getEtsComponentVersion

getEtsComponentVersion: () => string

获取SDK中ets组件（DevEco Studio安装目录/sdk/default/openharmony/ets目录下的组件）的版本号。

**起始版本：**Hvigor 6.0.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 获取SDK中ets组件的版本号 |

在工程级hvigorfile.ts中编写示例代码：

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosAppContext, OhosPluginId, SdkDetails } from '@ohos/hvigor-ohos-plugin';
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
          let sdk:SdkDetails = appContext.getSdkDetails();
          console.log(sdk?.getEtsComponentVersion())
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

### getEtsComponentReleaseType

getEtsComponentReleaseType: () => string

获取SDK中ets组件（DevEco Studio安装目录/sdk/default/openharmony/ets目录下的组件）的发布类型值。

**起始版本：**Hvigor 6.0.4

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 获取SDK中ets组件发布类型值 |

在工程级hvigorfile.ts中编写示例代码：

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosAppContext, OhosPluginId, SdkDetails } from '@ohos/hvigor-ohos-plugin';
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
          let sdk:SdkDetails = appContext.getSdkDetails();
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

## NormalizedFile

hvigor API中的文件类。您可以通过此对象来进行一些基本的文件操作。

### filePath

filePath: string

当前对象的路径信息。

**起始版本：**Hvigor 4.3.0

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  const moduleNormalizedFile = rootNode.nodeDir;
  console.log(`Module Normalized File Path: ${moduleNormalizedFile.filePath}`);
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### getPath

getPath: () => string

获取当前路径信息。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前对象的路径信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  const moduleNormalizedFile = rootNode.nodeDir;
  console.log(`Module Normalized File Path: ${moduleNormalizedFile.getPath()}`);
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### file

file: (\_path: string) => NormalizedFile

在原有的目录路径链式拼接路径，获取它的NormalizedFile对象。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| \_path | string | 是 | 需要拼接路径字符串 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NormalizedFile](ide-hvigor-api.md#section281448112713) | 在原有的NormalizedFile对象的路径链式拼接所得到NormalizedFile对象 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const rootNode = hvigor.getRootNode();
  const moduleNormalizedFile = rootNode.nodeDir;
  const buildProfileNormalizedFile = moduleNormalizedFile.file('build-profile.json5');
  console.log(`buildProfile File Path: ${buildProfileNormalizedFile.getPath()}`);
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### asFileList

asFileList: () => NormalizedFile[]

获取到NormalizedFile对象下深层递归的目录与文件NormalizedFile[]，包含它本身。

**起始版本：**Hvigor 4.3.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NormalizedFile](ide-hvigor-api.md#section281448112713)[] | NormalizedFile对象下深层递归的目录与文件NormalizedFile[]，包含它本身 |

当前只能通过node节点的node.nodeDir或者node.node.getNodeDir() 获取该node节点的根路径的NormalizedFile对象，再通过NormalizedFile.file(\_path: string)方法拼接后续路径来获取到新的NormalizedFile对象，工程级hvigorfile.ts示例：

```ts
import { appTasks } from '@ohos/hvigor-ohos-plugin';
// 导入接口
import { HvigorPlugin, HvigorNode} from '@ohos/hvigor';
// 实现自定义插件
function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    apply(node: HvigorNode) {
      appTask(node);
    }
  }
}
function appTask(currentNode: HvigorNode) {
  // 工程级的node
  currentNode.subNodes((node: HvigorNode) => {
    // 模块级的node 
    // 通过node.nodeDir 或者 node.node.getNodeDir() 获取该node节点的根路径的NormalizedFile文件
    const moduleNormalizedFile = node.nodeDir;
    // 通过NormalizedFile.file() 拼接后续路径，生成新的NormalizedFile对象
    // 生成模块下面build-Profile.json5的NormalizedFile对象
    const buildProfileNormalizedFile = moduleNormalizedFile.file('build-profile.json5');
  })
}
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[
    customPlugin()  // 应用自定义Plugin
  ]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

## FileUtil

文件操作工具类，支持一些基本的文件操作。

### 导入模块

```ts
import { FileUtil } from '@ohos/hvigor';
```

### exist

exist: (filePath: string) => boolean

判断文件路径是否存在。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 文件路径字符串 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 文件路径存在，false: 文件路径不存在 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const testFilePath = path.resolve(context.getProjectPath(), 'test.txt');
  if (FileUtil.exist(testFilePath)) {
    console.log(`File exists: ${testFilePath}`);
  } else {
    console.log(`File doesn't exist: ${testFilePath}`);
  }
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### isDictionary

isDictionary: (file: string | NormalizedFile) => boolean

判断文件路径或NormalizedFile对象是否是目录。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [NormalizedFile](ide-hvigor-api.md#section281448112713) | 是 | 文件路径字符串或者是NormalizedFile对象 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 是目录，false: 不是目录 |

**示例：**

```screen
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const testFilePath = path.resolve(context.getProjectPath(), 'test.txt');
  FileUtil.ensureFileSync(testFilePath);
  if (FileUtil.isDictionary(testFilePath)) {
    console.log(`It is a directory: ${testFilePath}`);
  } else {
    console.log(`It is not a directory: ${testFilePath}`);
  }
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### isFile

isFile: (file: string | NormalizedFile) => boolean

判断文件路径或NormalizedFile对象是否是文件。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [NormalizedFile](ide-hvigor-api.md#section281448112713) | 是 | 文件路径字符串或者是NormalizedFile对象 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 是文件，false: 不是文件 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const testFilePath = path.resolve(context.getProjectPath(), 'test.txt');
  FileUtil.ensureFileSync(testFilePath);
  if (FileUtil.isFile(testFilePath)) {
    console.log(`It is a file: ${testFilePath}`);
  } else {
    console.log(`It is not a file: ${testFilePath}`);
  }
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### ensureDirSync

ensureDirSync: (dirPath: string) => void

确保目录存在，不存在就创建。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dirPath | string | 是 | 目标目录地址 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  FileUtil.ensureDirSync(path.dirname(context.getBuildRootPath()));
})
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### ensureFileSync

ensureFileSync: (filePath: string) => void

确保文件存在，不存在就创建。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filePath | string | 是 | 目标文件地址 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const testFilePath = path.resolve(context.getProjectPath(), 'test.txt');
  FileUtil.ensureFileSync(testFilePath);
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### readJson5

readJson5: (file: string | NormalizedFile) => JSON

同步读取Json5文件。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [NormalizedFile](ide-hvigor-api.md#section281448112713) | 是 | json5文件路径或者NormalizedFile对象 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| JSON | 读取出的JSON格式数据 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const json5FilePath = path.resolve(context.getProjectPath(), 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
  const jsonContent = FileUtil.readJson5(json5FilePath);
  console.log(`Read JSON5 content: ${JSON.stringify(jsonContent, null, 2)}`);
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### readFileSync

readFileSync: (file: string | NormalizedFile) => Buffer

同步读取文件。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [NormalizedFile](ide-hvigor-api.md#section281448112713) | 是 | 文件路径字符串或者是NormalizedFile对象 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Buffer | 读取的Buffer数据 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const json5FilePath = path.resolve(context.getProjectPath(), 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
  const content = FileUtil.readFileSync(json5FilePath);
  console.log(`Content of ${json5FilePath}: ${content}`);
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### readFile

readFile: (file: string | NormalizedFile) => Promise<Buffer>

异步读取文件。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [NormalizedFile](ide-hvigor-api.md#section281448112713) | 是 | 文件路径字符串或者是NormalizedFile对象 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise | Promise<Buffer> |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(async () => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const json5FilePath = path.resolve(context.getProjectPath(), 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
  const content = await FileUtil.readFile(json5FilePath);
  console.log(content.toString());
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### writeFileSync

writeFileSync: (file: string | NormalizedFile, content: any) => void

同步写入文件。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [NormalizedFile](ide-hvigor-api.md#section281448112713) | 是 | 文件路径字符串或者是NormalizedFile对象 |
| content | any | 是 | 需要写入文件的内容 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const json5FilePath = path.resolve(context.getProjectPath(), 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
  const jsonContent = FileUtil.readJson5(json5FilePath);
  console.log(`Read JSON5 content: ${JSON.stringify(jsonContent, null, 2)}`);
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### writeFile

writeFile: (file: string | NormalizedFile, content: any) => Promise<void>

异步写入文件。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [NormalizedFile](ide-hvigor-api.md#section281448112713) | 是 | 文件路径字符串或者是NormalizedFile对象 |
| content | any | 是 | 需要写入文件的内容 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise | Promise<void> |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';
import path from "path";

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const json5FilePath = path.resolve(context.getProjectPath(), 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFile(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### copyFileSync

copyFileSync: (file: string | NormalizedFile, dest: string) => void

同步复制文件。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [NormalizedFile](ide-hvigor-api.md#section281448112713) | 是 | 文件路径字符串或者是NormalizedFile对象 |
| dest | string | 是 | 目标文件路径 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const json5FilePath = FileUtil.pathResolve(context.getProjectPath(), 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
  const copyFilePath = FileUtil.pathResolve(context.getProjectPath(), 'testJson_copy.json5');
  FileUtil.copyFileSync(json5FilePath, copyFilePath);
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### copyFile

copyFile: (file: string | NormalizedFile, dest: string) => Promise<void>

异步复制文件。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | [NormalizedFile](ide-hvigor-api.md#section281448112713) | 是 | 文件路径字符串或者是NormalizedFile对象 |
| dest | string | 是 | 目标文件路径 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise | Promise<void> |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const json5FilePath = FileUtil.pathResolve(context.getProjectPath(), 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFileSync(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
  const copyFilePath = FileUtil.pathResolve(context.getProjectPath(), 'testJson_copy.json5');
  FileUtil.copyFile(json5FilePath, copyFilePath);
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

### pathResolve

pathResolve: (...paths: string[]) => string

拼接路径。

**起始版本：**Hvigor 4.3.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| ...paths | string[] | 是 | 文件路径信息数组 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 拼接后得到的路径信息 |

**示例：**

```ts
// 工程级hvigorfile.ts文件
import { appTasks, OhosPluginId, OhosAppContext } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil, getNode } from '@ohos/hvigor';

const currentNode = getNode(__filename);
hvigor.nodesEvaluated(() => {
  const context = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  const json5FilePath = FileUtil.pathResolve(context.getProjectPath(), 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFile(json5FilePath, JSON.stringify(context.getAppJsonOpt()));
})

export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
```

## submitWorker

submitWorker(node: HvigorNode, taskName: string, workPath: string, workerOption: WorkerOption): TCB

向线程池提交一个worker并执行，worker必须归属于某个任务，表示这个任务并没有结束，但此时主线程可以执行其他任务，依赖该任务的其他任务仍然会排队等待。

**起始版本：**Hvigor 6.0.4

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [HvigorNode](ide-hvigor-api.md#section14832104719474) | 是 | worker归属的任务对应的节点。 |
| taskName | string | 是 | 向线程池提交worker的任务名称。 |
| workPath | string | 是 | 要执行的worker的文件路径，可以拼接函数名称，例如D:/xx/a.js/run是指运行a.js的run方法。 |
| workerOption | [WorkerOption](ide-hvigor-api.md#section2701859185318) | 是 | worker配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TCB](ide-hvigor-api.md#section282818554815) | 提交的worker的状态。 |

**示例：**在hap模块的自定义任务中，向线程池提交一个worker。

```ts
import { hapTasks } from '@ohos/hvigor-ohos-plugin';
import { HvigorNode, HvigorPlugin, submitWorker } from "@ohos/hvigor";
import path from "path";

// 实现自定义插件
function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    apply(node: HvigorNode) {
      // 插件主体
      node.registerTask({
        name: 'customTask',
        run() {
          submitWorker(node, this.name, path.join(__dirname, 'wait-job.js', 'wait'), {callback: () => {
            console.log('submit Worker callback');
          }});
        },
        dependencies: ['default@PreBuild'],
        postDependencies: ['assembleHap'],
      });
    }
  }
}

export default {
  system: hapTasks /* Built-in plugin of Hvigor. It cannot be modified. */,
  plugins: [customPlugin()] /* Custom plugin to extend the functionality of Hvigor. */,  
};
```

wait-job.js内容如下，和hvigorfile.ts在同一个目录下：

```js
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function wait() {
    console.log('开始等待10秒...');
    await sleep(10000);
    console.log('结束，退出程序。');
}

exports.wait = wait;
```

## WorkerOption

设置向线程池提交worker的配置，具体提交方式请参考[submitWorker](ide-hvigor-api.md#section94763341419)。

**起始版本：**Hvigor 6.0.4

| 成员 | 声明 | 说明 |
| --- | --- | --- |
| workInput | workInput?: unknown; | 设置要执行的线程的输入值。 |
| priority | priority?: [Priority](ide-hvigor-api.md#section162915519616); | 设置线程执行的优先级。 |
| targetWorkers | targetWorkers?: number[]; | 指定要在几号线程中执行。 |
| callback | callback?: Function; | 执行完毕的回调函数。 |
| callbackInput | callbackInput?: unknown[]; | 回调函数的入参。 |
| useReturnVal | useReturnVal?: boolean; | 回调函数入参是否使用线程执行结束的返回值，优先级高于callbackInput。 |

## Priority

线程执行的优先级枚举。

**起始版本：**Hvigor 6.0.4

| 成员 | 说明 |
| --- | --- |
| FIRST | 从上到下，优先级依次降低。 |
| HEAVY |
| MEDIUM |
| LIGHT |
| LAST |

## TCB

向线程池提交worker后返回的状态，具体提交方式请参考[submitWorker](ide-hvigor-api.md#section94763341419)。

**起始版本：**Hvigor 6.0.4

| 成员 | 声明 | 说明 |
| --- | --- | --- |
| getId | getId(): string; | 获取TCB自身的id。 |
| getWorkerId | getWorkerId(): number | undefined; | 获取worker的id。 |
| getSubmitTime | getSubmitTime(): number; | 获取提交时间。 |
| getStartTime | getStartTime(): number | undefined; | 获取执行开始时间。 |
| getEndTime | getEndTime(): number | undefined; | 获取执行结束时间。 |
| getState | getState(): TaskState; | 获取worker状态。 |
| getPriority | getPriority(): [Priority](ide-hvigor-api.md#section162915519616); | 获取优先级。 |
| getCallback | getCallback(): Function; | 获取回调函数。 |
| getCallbackInput | getCallbackInput(): unknown[]; | 获取回调函数的输入。 |
| getTaskPath | getTaskPath(): string; | 获取任务路径。 |
| getTaskName | getTaskName(): string; | 获取任务名。 |
| getTaskCompletePath | getTaskCompletePath(): string; | 获取任务完整路径，包含任务路径和任务名。 |
| useReturnVal | useReturnVal(): boolean; | 回调函数是否使用线程执行结束的返回值作为输入。 |
