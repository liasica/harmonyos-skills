---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-207
title: 能否在编译打包时自定义版本号
breadcrumb: FAQ > DevEco Studio > 编译构建 > 能否在编译打包时自定义版本号
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fb0848273cf647d0c1b514d727cc0df1f01d24a2133979fb907696a6087f0cd0
---

## 问题现象

如何在编译打包时自定义版本号，将设置的版本号打入包中？

## 背景知识

hvigorfile.ts的作用：

1. 配置构建任务：该文件用于定义和配置项目的构建任务。这些任务可能包括编译、打包、混淆、测试等各个阶段。
2. 集成插件：通过引入和配置插件，hvigorfile.ts可以扩展构建系统的功能。比如引入@ohos/hvigor-ohos-plugin，这是一个专门用于HarmonyOS应用构建的插件。

## 解决方案

修改app.json5中的"versionName"可以自定义版本号。通过在插件代码中使用[setAppJsonOpt](../harmonyos-guides/ide-build-expanding-context.md#section14633161122119)方法，修改当前构建的app.json5文件中内容的obj对象，达到编译打包时自定义版本号的效果。

具体实现可在工程级hvigorfile.ts中：

```ts
import { appTasks, OhosPluginId, OhosAppContext, AppJson } from '@ohos/hvigor-ohos-plugin';
import { hvigor, getNode, HvigorNode  } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const node: HvigorNode = getNode(__filename);
  const appContext = node.getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
  console.log('projectName:', appContext.getProjectName());
  const appJson5: AppJson.AppOptObj = appContext.getAppJsonOpt();
  if (appContext.getBuildMode() === 'debug') {
    appJson5.app.versionName = '1.0.0-debug-' + new Date().toLocaleDateString(); // 自定义版本号示例
  } else {
    appJson5.app.versionName = '1.0.0-release-' + new Date().toLocaleDateString(); // 自定义版本号示例
  }
  appContext.setAppJsonOpt(appJson5);
});
export default {
  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: []       /* Custom plugin to extend the functionality of Hvigor. */
}
```
