---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-169
title: 如何快速关闭工程中所有字节码HAR配置
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何快速关闭工程中所有字节码HAR配置
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7ccbcedbd01fec98fe5e3415dd2daacdc51f15112c7205ef23410d523cc2ab36
---

**解决措施**

方案一：适用于HAR文件较少的场景，直接修改字段byteCodeHar为false，详细字段可在以下链接中查询：[模块级build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile.md)

方案二：适用于HAR文件数量较多的场景。单独为每个HAR包配置较为繁琐，可以通过自定义插件直接修改所有HAR包的byteCodeHar字段值。该方法在编译时生效，但不会修改build-profile.json5文件中的字段值。

```typescript
// Engineering-level hvigorfile.ts file
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosHarContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
// Implement custom plugins
export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.afterNodeEvaluate(async () => {
        // Register module-level tasks
        harTask(currentNode);
      });
    }
  };
}
function harTask(currentNode: HvigorNode) {
  currentNode.subNodes((node: HvigorNode) => {
    const context = node.getContext(OhosPluginId.OHOS_HAR_PLUGIN)
    context?.targets((target: Target) => {
      const targetName = target.getTargetName();
      node.registerTask({
        // Task name
        name: `HarTask`,
        // Main function of task execution logic
        run() {
          if (context.getBuildProfileOpt) {
            const buildProfile = context.getBuildProfileOpt();
            console.log(buildProfile)
            // Set the bytecode har config to false
            buildProfile["buildOption"] = { arkOptions: { byteCodeHar: false } };
            console.log(buildProfile)
            context.setBuildProfileOpt(buildProfile);
          }
        },
        // Configure the dependency of the pre-task
        dependencies: [`${targetName}@PackageHar`],
        // Post-task dependency for configuring tasks
        postDependencies: ['assembleHar']
      });
    });
  });
}
export default {
  system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins:[customPlugin()]  /* Custom plugin to extend the functionality of Hvigor. */
}
```
