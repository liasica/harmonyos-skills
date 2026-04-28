---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-expanding-context
title: 插件上下文
breadcrumb: 指南 > 构建应用 > 扩展构建能力 > 扩展构建API > 插件上下文
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:24+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:42b22cdea2743426ec60a598c5071d2972fd1176e76752418e2c0763570634c1
---

## OhosPluginId

本组件是hvigor-ohos-plugin插件id常量类。

### 导入模块

```
1. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';
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

```
1. import { OhosAppContext } from '@ohos/hvigor-ohos-plugin';
```

### getProjectName

getProjectName: () => string

获取工程名称。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 工程名称 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. const projectName = appContext.getProjectName();
8. console.log(`Project Name: ${projectName}`);
9. });

11. export default {
12. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
13. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
14. }
```

### getProjectPath

getProjectPath: () => string

获取工程路径。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 工程路径 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. const projectPath = appContext.getProjectPath();
8. console.log(`Project Path: ${projectPath}`);
9. });

11. export default {
12. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
13. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
14. }
```

### getBuildRootPath

getBuildRootPath: () => string

获取构建目录根路径。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 构建根路径 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. const buildRootPath = appContext.getBuildRootPath();
8. console.log(`Build Root Path: ${buildRootPath}`);
9. });

11. export default {
12. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
13. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
14. }
```

### getBuildProductOutputPath

getBuildProductOutputPath: () => string

获取当前product构建的打包输出路径。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 当前product构建的打包输出路径 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. const buildProductOutputPath =  appContext.getBuildProductOutputPath();
8. console.log(`Build Product Output Path: ${buildProductOutputPath}`);
9. });

11. export default {
12. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
13. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
14. }
```

### getCurrentProduct

getCurrentProduct: () => Product

获取当前构建指定的product对象。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| [Product](ide-hvigor-api.md#section1553414254713) | 当前构建指定的product对象 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. const currentProduct = appContext.getCurrentProduct();
8. });

10. export default {
11. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
12. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
13. }
```

### getBuildMode

getBuildMode: () => string

获取当前构建指定的BuildMode。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 当前构建指定的BuildMode |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. const buildMode = appContext.getBuildMode();
8. console.log(`Build Mode: ${buildMode}`);
9. });

11. export default {
12. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
13. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
14. }
```

### getAppJsonOpt

getAppJsonOpt: () => any

获取当前构建的app.json5文件中内容的obj对象。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| any | 当前构建的app.json5文件中内容的obj对象 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. const appJsonOpt =  appContext.getAppJsonOpt();
8. console.log(`bundleName: ${appJsonOpt.app.bundleName}`);
9. });

11. export default {
12. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
13. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
14. }
```

### setAppJsonOpt

setAppJsonOpt: (appJsonOpt: any) => void

修改当前构建的app.json5文件中内容的obj对象。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appJsonOpt | any | 是 | 设置当前构建的app.json5文件解析出来的obj对象 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosPluginId, OhosAppContext, AppJson } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, getNode, HvigorNode  } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const node: HvigorNode = getNode(__filename);
7. const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
8. console.log('projectName:', appContext.getProjectName());
9. const appJson5: AppJson.AppOptObj = appContext.getAppJsonOpt();
10. if (appContext.getBuildMode() === 'debug') {
11. appJson5.app.versionName = '1.0.0-debug';
12. } else {
13. appJson5.app.versionName = '1.0.0-release';
14. }
15. appContext.setAppJsonOpt(appJson5);
16. });
17. export default {
18. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
19. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
20. }
```

说明

setAppJsonOpt会进行schema校验，如果传入的对象不符合校验规则则会抛出异常。

### getBuildProfileOpt

getBuildProfileOpt: () => any

获取当前构建的根目录下build-profile.json5文件中内容的obj对象。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| any | 当前构建的根目录下build-profile.json5文件中内容的obj对象 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. const buildProfileOpt = appContext.getBuildProfileOpt();
8. });

10. export default {
11. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
12. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
13. }
```

### setBuildProfileOpt

setBuildProfileOpt: (buildProfileOpt: any) => void

设置当前构建的build-profile.json5文件中内容的obj对象。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buildProfileOpt | any | 是 | 设置当前构建的根目录下build-profile.json5文件中内容的obj对象 |

说明

* setBuildProfileOpt会进行schema校验，如果传入的对象不符合校验规则则会抛出异常。
* 不支持通过setBuildProfileOpt方法设置maxFlowDepth字段。

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. const buildProfileOpt = appContext.getBuildProfileOpt();
8. // 添加一个工程外的模块
9. const newModule = {
10. "name": "har",
11. "srcPath": "./../MyApplication40/har",// 确保该源码模块存在
12. }
13. buildProfileOpt.modules.push(newModule);
14. appContext.setBuildProfileOpt(buildProfileOpt);
15. console.log(buildProfileOpt.modules.map(module => {
16. return module.name;
17. }));
18. });

20. export default {
21. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
22. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
23. }
```

### getOhpmDependencyInfo

getOhpmDependencyInfo: () => Record<string, OhpmDependencyInfo> | object

获取工程下oh-package.json5中配置的依赖信息。

**起始版本：**Hvigor 5.0.0

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Record<string, OhpmDependencyInfo> | object | oh-package.json5中配置的依赖信息 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
3. import { appTasks } from '@ohos/hvigor-ohos-plugin';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

6. // 自定义插件代码
7. export function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. async apply(currentNode: HvigorNode): Promise<void> {
11. const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
12. if (!rootNodeContext) {
13. return;
14. }
15. const ohpmInfo = rootNodeContext.getOhpmDependencyInfo();
16. console.log(ohpmInfo)
17. }
18. };
19. }

21. export default {
22. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
23. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
24. }
```

### getOhpmRemoteHspDependencyInfo

getOhpmRemoteHspDependencyInfo: (isSigned: boolean) => Record<string, OhpmDependencyInfo> | object

获取工程下oh-package.json5中配置的hsp包依赖信息。

**起始版本：**Hvigor 5.6.2

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| signed | boolean | 否 | 是否获取签名的hsp包路径，默认为false |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Record<string, OhpmDependencyInfo> | object | 工程下oh-package.json5中配置的hsp包依赖信息 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
3. import { appTasks, OhosHapContext, OhosAppContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
4. // 实现自定义插件
5. export function customPlugin(): HvigorPlugin {
6. return {
7. pluginId: 'customPlugin',
8. context() {
9. return {
10. data: 'customPlugin xxx'
11. };
12. },
13. async apply(currentNode: HvigorNode): Promise<void> {
14. hvigor.nodesEvaluated(async () => {
15. // 注册模块级任务
16. hapTask(currentNode);
17. });
18. }
19. };
20. }
21. function hapTask(currentNode: HvigorNode) {
22. // 等待全部节点加载完成之后获取子节点信息
23. currentNode.subNodes((node: HvigorNode) => {
24. // 获取hap模块上下文信息
25. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
26. const moduleName = hapContext?.getModuleName();
27. hapContext?.targets((target: Target) => {
28. const targetName = target.getTargetName();
29. node.registerTask({
30. // 任务名称
31. name: `${targetName}@getRemoteHspInfo`,
32. // 任务执行逻辑主体函数
33. run() {
34. const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
35. if (!rootNodeContext) {
36. return;
37. }
38. // 获取未签名的远程hsp相关信息
39. const remoteHspInfo = rootNodeContext.getOhpmRemoteHspDependencyInfo(false);
40. console.log(remoteHspInfo)
41. // 获取已签名的远程hsp相关信息
42. const signedRemoteHspInfo = rootNodeContext.getOhpmRemoteHspDependencyInfo(true);
43. console.log(signedRemoteHspInfo)
44. },
45. // 配置前置任务依赖
46. dependencies: [`${targetName}@PackageHap`],
47. // 配置任务的后置任务依赖
48. postDependencies: ['assembleHap']
49. });
50. });
51. });
52. }
53. export default {
54. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
55. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
56. };
```

### getDependenciesOpt

getDependenciesOpt: () => any

获取工程下oh-package.json5中配置的dependencies依赖。

**起始版本：**Hvigor 5.0.10

**返回值:**

| 类型 | 说明 |
| --- | --- |
| any | 工程级别下oh-package.json5中的dependencies信息 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
3. import { appTasks } from '@ohos/hvigor-ohos-plugin';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

6. // 自定义插件代码
7. export function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. async apply(currentNode: HvigorNode): Promise<void> {
11. const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
12. if (!rootNodeContext) {
13. return;
14. }
15. const DependenciesInfo = rootNodeContext.getDependenciesOpt();
16. console.log(DependenciesInfo)
17. }
18. };
19. }

21. export default {
22. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
23. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
24. }
```

### setDependenciesOpt

setDependenciesOpt: (dependencies: any) => void

设置工程下oh-package.json5中的dependencies依赖。需要确保oh-package.json5中dependencies字段存在。

**起始版本：**Hvigor 5.0.10

**参数值:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dependencies | any | 是 | 设置当前工程下oh-package.json5中dependencies依赖 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
3. import { appTasks } from '@ohos/hvigor-ohos-plugin';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

6. // 自定义插件代码
7. export function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. async apply(currentNode: HvigorNode): Promise<void> {
11. const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
12. if (!rootNodeContext) {
13. return;
14. }
15. const dependenciesInfo = rootNodeContext.getDependenciesOpt()
16. dependenciesInfo["har"] = "./har";  // 确保依赖存在
17. rootNodeContext.setDependenciesOpt(dependenciesInfo);
18. }
19. };
20. }

22. export default {
23. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
24. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
25. }
```

### getDevDependenciesOpt

getDevDependenciesOpt: () => any

获取工程下oh-package.json5中配置的devDependencies依赖。

**起始版本：**Hvigor 5.0.10

**返回值:**

| 类型 | 说明 |
| --- | --- |
| any | 获取工程级别下oh-package.json5中devDependencies信息 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
3. import { appTasks } from '@ohos/hvigor-ohos-plugin';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

6. // 自定义插件代码
7. export function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. async apply(currentNode: HvigorNode): Promise<void> {
11. const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
12. if (!rootNodeContext) {
13. return;
14. }
15. const devDependenciesInfo = rootNodeContext.getDevDependenciesOpt();
16. console.log(devDependenciesInfo)
17. }
18. };
19. }

21. export default {
22. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
23. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
24. }
```

### setDevDependenciesOpt

setDevDependenciesOpt: (devDependencies: any) => void

设置工程下oh-package.json5中的devDependencies依赖。需要确保oh-package.json5中devDependencies字段存在。

**起始版本：**Hvigor 5.0.10

**参数值:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| devDependencies | any | 是 | 设置当前工程下oh-package.json5中devdependencies依赖 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
3. import { appTasks } from '@ohos/hvigor-ohos-plugin';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

6. // 自定义插件代码
7. export function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. async apply(currentNode: HvigorNode): Promise<void> {
11. const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
12. if (!rootNodeContext) {
13. return;
14. }
15. const devDependenciesInfo = rootNodeContext.getDevDependenciesOpt()
16. devDependenciesInfo["har"] = "./har";  // 确保依赖存在
17. rootNodeContext.setDevDependenciesOpt(devDependenciesInfo);
18. }
19. };
20. }

22. export default {
23. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
24. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
25. }
```

### getDynamicDependenciesOpt

getDynamicDependenciesOpt: () => any

获取工程下oh-package.json5中配置的dynamicDependencies依赖。

**起始版本：**Hvigor 5.0.10

**返回值:**

| 类型 | 说明 |
| --- | --- |
| any | 获取工程级别下oh-package.json5中DynamicDependencies信息 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
3. import { appTasks } from '@ohos/hvigor-ohos-plugin';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

6. // 自定义插件代码
7. export function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. async apply(currentNode: HvigorNode): Promise<void> {
11. const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
12. if (!rootNodeContext) {
13. return;
14. }
15. const dynamicDependenciesInfo = rootNodeContext.getDynamicDependenciesOpt();
16. console.log(dynamicDependenciesInfo)
17. }
18. };
19. }

21. export default {
22. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
23. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
24. }
```

### setDynamicDependenciesOpt

setDynamicDependenciesOpt: (dynamicDependencies: any) => void

设置工程下oh-package.json5中的dynamicDependencies依赖。需要确保oh-package.json5中dynamicDependencies字段存在。

**起始版本：**Hvigor 5.0.10

**参数值:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dynamicDependencies | any | 是 | 设置当前工程下oh-package.json5中dynamicDependencies依赖 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
3. import { appTasks } from '@ohos/hvigor-ohos-plugin';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

6. // 自定义插件代码
7. export function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. async apply(currentNode: HvigorNode): Promise<void> {
11. const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
12. if (!rootNodeContext) {
13. return;
14. }
15. const dynamicDependenciesInfo = rootNodeContext.getDynamicDependenciesOpt()
16. dynamicDependenciesInfo["har"] = "./har";  // 确保依赖存在
17. rootNodeContext.setDynamicDependenciesOpt(dynamicDependenciesInfo);
18. }
19. };
20. }

22. export default {
23. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
24. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
25. }
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

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks } from '@ohos/hvigor-ohos-plugin';
3. import {OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
4. import { hvigor } from '@ohos/hvigor';
5. hvigor.afterNodeEvaluate(node => {
6. const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. if (appContext) {
8. let dependency = appContext.getOverrides() ?? {};
9. console.log(dependency)
10. }
11. });
12. export default {
13. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
14. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
15. }
```

### setOverrides

setOverrides: (overrides: any) => void

设置工程下oh-package.json5中的overrides字段。

**起始版本：**Hvigor 5.10.3

**参数值：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| overrides | any | 是 | 设置工程下oh-package.json5中的overrides字段 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks } from '@ohos/hvigor-ohos-plugin';
3. import {OhosAppContext, OhosHapContext, OhosPluginId} from '@ohos/hvigor-ohos-plugin';
4. import { hvigor } from '@ohos/hvigor';
5. hvigor.afterNodeEvaluate(node => {
6. const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
7. if (appContext) {
8. let dependency = appContext.getOverrides() ?? {};
9. dependency['library'] = 'file:./library.har'; //在工程级oh-package.json5中动态添加工程内HAR包依赖
10. appContext.setOverrides(dependency);
11. return;
12. }
13. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
14. if (hapContext) {
15. const dependency = hapContext.getDependenciesOpt();
16. dependency['library'] = 'file:./../library';    //在entry上动态添加工程内模块依赖
17. hapContext.setDependenciesOpt(dependency);
18. }
19. });
20. export default {
21. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
22. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
23. }
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

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks } from '@ohos/hvigor-ohos-plugin';
3. import { OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
4. import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';

6. export function customPlugin(): HvigorPlugin {
7. return {
8. pluginId: 'customPlugin',
9. context() {
10. return {
11. data: 'customPlugin xxx'
12. };
13. },
14. async apply(currentNode: HvigorNode): Promise<void> {
15. hvigor.afterNodeEvaluate(node => {
16. const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
17. if (appContext) {
18. let sdk = appContext.getSdkDetails();
19. console.log(sdk?.getSdkDir())
20. console.log(sdk?.isOhos())
21. console.log(sdk?.getSdkVersion())
22. console.log(sdk?.getEtsComponentVersion())
23. console.log(sdk?.getEtsComponentReleaseType())
24. }
25. });
26. }
27. };
28. }

30. export default {
31. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
32. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
33. }
```

## OhosHapContext

hap模块Plugin提供的上下文接口，在hap模块的hvigor节点中可通过getContext方法传入OhosPluginId.OHOS\_HAP\_PLUGIN\_ID获取该接口，接口中主要包含了hap模块中module、target信息。

### 导入模块

```
1. import { OhosHapContext } from '@ohos/hvigor-ohos-plugin';
```

### getModuleName

getModuleName: () => string

获取模块名称。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 模块名称 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const rootNode = hvigor.getRootNode();
7. rootNode.subNodes((node: HvigorNode) => {
8. // 获得所有子节点
9. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
10. const moduleName = hapContext?.getModuleName();
11. console.log(`Module Name: ${moduleName}`);
12. });
13. })

15. export default {
16. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
17. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
18. }
```

### getModulePath

getModulePath: () => string

获取模块路径。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 模块路径 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const rootNode = hvigor.getRootNode();
7. rootNode.subNodes((node: HvigorNode) => {
8. // 获得所有子节点
9. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
10. const modulePath = hapContext?.getModulePath();
11. console.log(`Module Path: ${modulePath}`);
12. });
13. })

15. export default {
16. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
17. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
18. }
```

### getModuleType

getModuleType: () => string

获取模块类型，取值来自模块配置文件module.json5的type字段。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 模块类型 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const rootNode = hvigor.getRootNode();
7. rootNode.subNodes((node: HvigorNode) => {
8. // 获得所有子节点
9. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
10. const moduleType = hapContext?.getModuleType();
11. console.log(`Module Type: ${moduleType}`);
12. });
13. })

15. export default {
16. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
17. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
18. }
```

### getBuildProductRootPath

getBuildProductRootPath: () => string

获取模块基于product构建根路径。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 模块基于product构建根路径 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const rootNode = hvigor.getRootNode();
7. rootNode.subNodes((node: HvigorNode) => {
8. // 获得所有子节点
9. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
10. const buildProductRootPath = hapContext?.getBuildProductRootPath();
11. console.log(`Build Product Root Path: ${buildProductRootPath}`);
12. });
13. })

15. export default {
16. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
17. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
18. }
```

### targets

targets: (callbackfn: (target: Target) => void) => void

当前需构建的target对象回调方法。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (target: [Target](ide-hvigor-api.md#section12392182963714)) => void | 是 | 入参类型为Target，返回类型为void的函数 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const rootNode = hvigor.getRootNode();
7. rootNode.subNodes((node: HvigorNode) => {
8. // 获得所有子节点
9. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
10. hapContext?.targets((target: Target) => {
11. // 这里可以写入对每个 target 的处理逻辑
12. const targetName = target.getTargetName();
13. console.log(`Target Name: ${targetName}`);
14. });
15. });
16. })

18. export default {
19. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
20. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
21. }
```

### getBuildMode

getBuildMode: () => string

获取当前构建指定的BuildMode。

**起始版本：**Hvigor 5.18.4

**返回值:**

| 类型 | 说明 |
| --- | --- |
| string | 当前构建指定的BuildMode |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const rootNode = hvigor.getRootNode();
7. rootNode.subNodes((node: HvigorNode) => {
8. // 获得所有子节点
9. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
10. const buildMode = hapContext?.getBuildMode();
11. console.log(`Build Mode: ${buildMode}`);
12. });
13. })

15. export default {
16. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
17. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
18. }
```

### getModuleJsonOpt

getModuleJsonOpt: () => any

获取当前模块的module.json5文件中内容的obj对象。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| any | 当前模块的module.json5文件中内容的obj对象 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const rootNode = hvigor.getRootNode();
7. rootNode.subNodes((node: HvigorNode) => {
8. // 获得所有子节点
9. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
10. const moduleJsonOpt = hapContext?.getModuleJsonOpt();
11. console.log(`Module Json Opt: ${JSON.stringify(moduleJsonOpt)}`);
12. });
13. })

15. export default {
16. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
17. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
18. }
```

### setModuleJsonOpt

setModuleJsonOpt: (moduleJsonOpt: any) => void

修改当前构建的module.json5文件中的obj对象。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| moduleJsonOpt | any | 是 | 设置当前模块的module.json5文件解析出来的obj对象 |

说明

setModuleJsonOpt会进行schema校验，如果传入的对象不符合校验规则会抛出异常。

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const rootNode = hvigor.getRootNode();
7. rootNode.subNodes((node: HvigorNode) => {
8. // 获得所有子节点
9. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext; // 仅对hap模块生效，hsp和har需要使用模块对应接口
10. const moduleJsonOpt = hapContext?.getModuleJsonOpt();
11. moduleJsonOpt.module.deviceTypes = ["phone", "tablet"]; // 修改 module.json 中的 deviceTypes 字段
12. hapContext?.setModuleJsonOpt(moduleJsonOpt); // 更新 module.json
13. console.log(`Module Json Opt: ${JSON.stringify(moduleJsonOpt)}`);
14. });
15. })

17. export default {
18. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
19. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
20. }
```

### getBuildProfileOpt

getBuildProfileOpt: () => any

获取当前模块的build-profile.json5文件中内容的obj对象。

**返回值:**

| 类型 | 说明 |
| --- | --- |
| any | 当前模块的build-profile.json5文件中内容的obj对象 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const rootNode = hvigor.getRootNode();
7. rootNode.subNodes((node: HvigorNode) => {
8. // 获得所有子节点
9. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
10. const buildProfileOpt = hapContext?.getBuildProfileOpt();
11. console.log(`Build Profile Opt: ${JSON.stringify(buildProfileOpt)}`);
12. });
13. })

15. export default {
16. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
17. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
18. }
```

### setBuildProfileOpt

setBuildProfileOpt: (buildProfileOpt: any) => void

设置当前模块的build-profile.json5文件中内容的obj对象。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| buildProfileOpt | any | 是 | 设置当前模块的build-profile.json5文件中内容的obj对象 |

说明

setBuildProfileOpt会进行schema校验，如果传入的对象不符合校验规则会抛出异常。

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode } from '@ohos/hvigor';

5. hvigor.nodesEvaluated(() => {
6. const rootNode = hvigor.getRootNode();
7. rootNode.subNodes((node: HvigorNode) => {
8. // 获得所有子节点
9. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
10. const buildProfileOpt = hapContext?.getBuildProfileOpt();
11. // 可以对buildProfileOpt进行修改
12. buildProfileOpt?.targets?.push({
13. "name": "default1",
14. })
15. hapContext?.setBuildProfileOpt(buildProfileOpt); // 更新 build profile
16. console.log(`Build Profile Opt: ${JSON.stringify(buildProfileOpt)}`);
17. });
18. })

20. export default {
21. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
22. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
23. }
```

### getVersion

getVersion: () => string

获取模块oh-package.json5中配置的版本号。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 模块oh-package.json5中配置的版本号 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

6. // 实现自定义插件
7. export function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. context() {
11. return {
12. data: 'customPlugin xxx'
13. };
14. },
15. async apply(currentNode: HvigorNode): Promise<void> {
16. hvigor.nodesEvaluated(async () => {
17. currentNode.subNodes((node: HvigorNode) => {
18. // 获取hap模块上下文信息
19. // 如果是HAR或HSP，使用OHOS_HAR_PLUGIN/OHOS_HSP_PLUGIN
20. const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
21. if (!hapNodeContext) {
22. return;
23. }
24. const moduleVersion = hapNodeContext.getVersion();
25. console.log(moduleVersion);
26. });
27. });
28. }
29. };
30. }
31. export default {
32. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
33. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
34. }
```

### setVersion

setVersion: (version: string) => void

修改模块oh-package.json5中的版本号。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| version | string | 是 | 修改模块oh-package.json5中的版本号 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

6. // 实现自定义插件
7. export function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. context() {
11. return {
12. data: 'customPlugin xxx'
13. };
14. },
15. async apply(currentNode: HvigorNode): Promise<void> {
16. hvigor.nodesEvaluated(async () => {
17. currentNode.subNodes((node: HvigorNode) => {
18. // 获取hap模块上下文信息
19. // 如果是HAR或HSP，使用OHOS_HAR_PLUGIN/OHOS_HSP_PLUGIN
20. const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
21. if (!hapNodeContext) {
22. return;
23. }
24. hapNodeContext.setVersion('2.0.0');
25. const moduleVersion = hapNodeContext.getVersion();
26. console.log(moduleVersion);
27. });
28. });
29. }
30. };
31. }
32. export default {
33. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
34. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
35. }
```

### getOhpmDependencyInfo

getOhpmDependencyInfo: () => Record<string, OhpmDependencyInfo> | object

获取模块下oh-package.json5中配置的依赖信息。

**起始版本：**Hvigor 5.0.0

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Record<string, OhpmDependencyInfo> | object | oh-package.json5中配置的依赖信息 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';

6. // 实现自定义插件
7. export function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. context() {
11. return {
12. data: 'customPlugin xxx'
13. };
14. },
15. async apply(currentNode: HvigorNode): Promise<void> {
16. hvigor.nodesEvaluated(async () => {
17. currentNode.subNodes((node: HvigorNode) => {
18. // 获取hap模块上下文信息
19. const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
20. if (!hapNodeContext) {
21. return;
22. }
23. const ohpmInfo = hapNodeContext.getOhpmDependencyInfo();
24. console.log(ohpmInfo)

26. });
27. });
28. }
29. };
30. }

32. export default {
33. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
34. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
35. }
```

### getOhpmRemoteHspDependencyInfo

getOhpmRemoteHspDependencyInfo: (isSigned: boolean) => Record<string, OhpmDependencyInfo> | object

获取模块下oh-package.json5中配置的hsp包依赖信息。

**起始版本：**Hvigor 5.6.2

**参数值:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSigned | boolean | 否 | 是否获取签名的hsp包路径，默认为false |

**返回值:**

| 类型 | 说明 |
| --- | --- |
| Record<string, OhpmDependencyInfo> | object | 模块下oh-package.json5中配置的hsp包依赖信息 |

**示例：**

```
1. // 工程级hvigorfile.ts文件
2. import { appTasks, OhosHapContext, Target } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
4. import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';
5. // 实现自定义插件
6. export function customPlugin(): HvigorPlugin {
7. return {
8. pluginId: 'customPlugin',
9. context() {
10. return {
11. data: 'customPlugin xxx'
12. };
13. },
14. async apply(currentNode: HvigorNode): Promise<void> {
15. hvigor.nodesEvaluated(async () => {
16. currentNode.subNodes((node: HvigorNode) => {
17. // 获取hap模块上下文信息
18. const hapNodeContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
19. hapNodeContext?.targets((target: Target) => {
20. const targetName = target.getTargetName();
21. node.registerTask({
22. // 任务名称
23. name: `${targetName}@getRemoteHspInfo`,
24. // 任务执行逻辑主体函数
25. run() {
26. // 获取未签名的远程hsp相关信息
27. const remoteHspInfo = hapNodeContext.getOhpmRemoteHspDependencyInfo(false);
28. console.log(remoteHspInfo);
29. // 获取已签名的远程hsp相关信息
30. const signedRemoteHspInfo = hapNodeContext.getOhpmRemoteHspDependencyInfo(true);
31. console.log(signedRemoteHspInfo);
32. },
33. // 配置前置任务依赖
34. dependencies: [`${targetName}@PackageHap`],
35. // 配置任务的后置任务依赖
36. postDependencies: ['assembleHap']
37. });
38. });
39. });
40. });
41. }
42. };
43. }
44. export default {
45. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
46. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
47. }
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

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fn | (abcPath: string, config: { isArkGuardEnabled: boolean }) => void | Promise<void> | 是 | 注册在abc文件生成之后执行的回调函数。回调函数的参数说明：  abcPath: abc文件的绝对路径；  config: 模块相关的配置信息，当前仅支持  通过isArkGuardEnabled获取是否开启源码混淆的信息。 |
| targetName | string | 否 | 指定回调函数生效的target，未填写时对所有target生效。 |

**示例：**

```
1. // 模块级hvigorfile.ts文件
2. import { hapTasks } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
4. import { OhosPluginId, OhosHapContext, Target } from "@ohos/hvigor-ohos-plugin";

6. // 自定义hvigor插件
7. function customPlugin(): HvigorPlugin {
8. return {
9. pluginId: 'customPlugin',
10. apply(node: HvigorNode) {
11. hvigor.nodesEvaluated(() => {
12. // 获取模块上下文
13. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
14. if (!hapContext) {
15. return;
16. }

18. // 定义TransformAbc的回调函数
19. const callback = async (abcPath, config) => {
20. console.log("abcPath", abcPath, "config", config);
21. };

23. // 场景一：不指定targetName，对所有target都注册回调函数
24. hapContext.transformAbc(callback);

26. // 场景二：遍历该模块支持的所有target，对指定target进行注册
27. hapContext.targets((target: Target) => {
28. if (target.getTargetName() === 'default') {
29. hapContext.transformAbc(callback, target.getTargetName());
30. }
31. });
32. });
33. }
34. }
35. }

37. export default {
38. system: hapTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
39. plugins: [customPlugin()]       /* Custom plugin to extend the functionality of Hvigor. */
40. }
```

## OhosHspContext

Hsp模块上下文接口信息与OhosHapContext一致，请参考上文中OhosHapContext接口描述。

## OhosHarContext

Har模块上下文接口信息与OhosHapContext一致，请参考上文中OhosHapContext接口描述。
