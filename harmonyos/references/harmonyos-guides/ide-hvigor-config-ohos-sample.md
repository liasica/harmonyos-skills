---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-config-ohos-sample
title: 实践说明
breadcrumb: 指南 > 构建应用 > 定制构建 > 动态修改编译配置 > 实践说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:918cbe1bd606700e5257bf4c58f794872e501dd2a0867910778d18d6226249bf
---

## 通过hook以及插件上下文动态配置构建配置(推荐使用)

### 修改每个hvigorNode中的build-profile.json5

此处只举例为单个node注册hook并修改build-profile.json5的信息。

例如需要修改根目录下的build-profile.json5的签名信息，则在项目根目录下的hvigorfile.ts中添加如下内容：

```
1. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
2. import { hvigor,getNode } from '@ohos/hvigor'

4. // 获取根节点
5. const rootNode = getNode(__filename);
6. // 为根节点添加一个afterNodeEvaluate hook 在hook中修改根目录下的build-profile.json5的内容并使能
7. rootNode.afterNodeEvaluate(node => {
8. // 获取app插件的上下文对象
9. const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
10. // 通过上下文对象获取从根目录build-profile.json5文件中读出来的obj对象
11. const buildProfileOpt = appContext.getBuildProfileOpt();
12. // 修改obj对象为想要的，此处举例修改app中的signingConfigs
13. buildProfileOpt['app']['signingConfigs'] = [
14. {
15. "name": "default",
16. "type": "HarmonyOS",
17. "material": {
18. "certpath": "D:\\SigningConfig\\debug_hos.cer",
19. "storePassword": "******",
20. "keyAlias": "debugKey",
21. "keyPassword": "******",
22. "profile": "D:\\SigningConfig\\debug_hos.p7b",
23. "signAlg": "SHA256withECDSA",
24. "storeFile": "D:\\SigningConfig\\debug_hos.p12"
25. }
26. }
27. ];
28. // 将obj对象设置回上下文对象以使能到构建的过程与结果中
29. appContext.setBuildProfileOpt(buildProfileOpt);
30. })
31. export default {
32. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
33. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
34. }
```

### 修改module.json5中的配置信息

可以通过hvigor对象的hook能力快捷为所有的node创建hook，此处先举例为单一的node创建一个hook并修改其中的module.json5的配置信息。

例如此处需要修改entry下的module.json5配置，则在entry下的hvigorfile.ts中添加如下内容：

```
1. import { hapTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
2. import { getNode } from '@ohos/hvigor'

4. const entryNode = getNode(__filename);
5. // 为此节点添加一个afterNodeEvaluate hook 在hook中修改module.json5的内容并使能
6. entryNode.afterNodeEvaluate(node => {
7. // 获取此节点使用插件的上下文对象 此时为hap插件 获取hap插件上下文对象
8. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
9. // 通过上下文对象获取从module.json5文件中读出来的obj对象
10. const moduleJsonOpt = hapContext.getModuleJsonOpt();
11. // 修改obj对象为想要的，此处举例修改module中的deviceTypes
12. moduleJsonOpt['module']['deviceTypes'] = ["phone", "tablet", "2in1", "car"];
13. // 将obj对象设置回上下文对象以使能到构建的过程与结果中
14. hapContext.setModuleJsonOpt(moduleJsonOpt);
15. })
16. export default {
17. system: hapTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
18. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
19. }
```

### 修改app.json5中的配置信息

在项目的根目录下的hvigorfile.ts中添加如下代码内容：

```
1. import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
2. import { hvigor } from '@ohos/hvigor'

4. // 为根节点添加一个afterNodeEvaluate hook 在hook中修改app.json5的内容并使能
5. hvigor.getRootNode().afterNodeEvaluate(rootNode => {
6. // 获取app插件的上下文对象
7. const appContext = rootNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
8. // 通过上下文对象获取从app.json5文件中读出来的obj对象
9. const appJsonOpt = appContext.getAppJsonOpt();
10. // 修改obj对象为想要的，此处举例修改app中的versionCode
11. appJsonOpt['app']['versionCode'] = 1000001;
12. // 将obj对象设置回上下文对象以使能到构建的过程与结果中
13. appContext.setAppJsonOpt(appJsonOpt);
14. })
15. export default {
16. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
17. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
18. }
```

### 修改oh-package.json5中的依赖

可以通过hvigorfile.ts自定义插件修改工程级、模块级的oh-package.json5的依赖，例如在工程级hvigorfile.ts或模块级hvigorfile.ts分别添加以下内容：

```
1. // 工程级hvigorfile.ts
2. import { appTasks, OhosAppContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
3. import { HvigorNode, HvigorPlugin, TaskInput, TaskOutput } from '@ohos/hvigor';
4. export function customPlugin(): HvigorPlugin {
5. return {
6. pluginId: 'customPlugin',
7. async apply(currentNode: HvigorNode): Promise<void> {
8. const appContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
9. const dependency = appContext.getDependenciesOpt();  // 获取dependency依赖
10. dependency["library"]="file:library.har"    // 确保har包存在
11. console.log(dependency);
12. appContext.setDependenciesOpt(dependency );  // 修改dependency依赖，需要确保oh-package.json5中dependencies字段存在
13. }
14. };
15. }
16. export default {
17. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
18. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
19. }

21. // 模块级hvigorfile.ts
22. import {hapTasks,OhosHapContext,OhosPluginId,Target} from '@ohos/hvigor-ohos-plugin';
23. import { hvigor, HvigorNode, HvigorPlugin} from '@ohos/hvigor';
24. import * as fs from 'fs';
25. export function customPlugin(): HvigorPlugin {
26. return {
27. pluginId: 'customPlugin',
28. async apply(currentNode: HvigorNode): Promise<void> {
29. const hapContext = currentNode.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
30. const dependency = hapContext.getDependenciesOpt();    // 获取dependency依赖
31. dependency["library"]="file:library.har"    // 确保har包存在
32. hapContext.setDependenciesOpt(dependency);}   // 需要确保oh-package.json5中dependencies字段存在
33. }
34. };
35. export default {
36. system: hapTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
37. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
38. }
```

## 通过overrides动态配置签名材料和版本信息(不推荐使用)

通过在hvigorfile.ts里使用函数方法，动态配置签名材料和版本号、版本名等信息：

```
1. //工程级别hvigorfile.ts
2. import { appTasks } from '@ohos/hvigor-ohos-plugin';
3. export default {
4. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
5. plugins: [],       /* Custom plugin to extend the functionality of Hvigor. */
6. config: {
7. ohos: {
8. overrides:{
9. signingConfig: getSigningConfig(), //签名配置对象
10. appOpt: {
11. versionCode: getVersionCode(),
12. versionName: getVersionName(),
13. } //app.json中的内容
14. }
15. }
16. }
17. }

19. function getSigningConfig() {
20. return {
21. type: "HarmonyOS",
22. material: {
23. certpath: "D:\\SigningConfig\\debug_hos.cer",
24. storePassword: "******",
25. keyAlias: "debugKey",
26. keyPassword: "******",
27. profile: "D:\\SigningConfig\\debug_hos.p7b",
28. signAlg: "SHA256withECDSA",
29. storeFile: "D:\\SigningConfig\\debug_hos.p12"
30. }
31. }
32. }

34. function getVersionCode() {
35. return 100000+new Date().getFullYear();
36. }

38. function getVersionName() {
39. return `1.0.0${new Date().getTime()}`;
40. }
```
