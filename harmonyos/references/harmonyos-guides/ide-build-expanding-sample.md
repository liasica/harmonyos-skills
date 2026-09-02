---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-expanding-sample
title: API使用示例
breadcrumb: 指南 > 构建应用 > 扩展构建能力 > 扩展构建API > API使用示例
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6671c4ef5681c0c41fe99155dcc6b3bed15e6b121809548b04626340f5694326
---

示例：在工程级hvigorfile.ts文件中分别注册工程级与模块级任务。

```ts
// 工程级hvigorfile.ts文件
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';

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
      const outputPath = target.getBuildTargetOutputPath();
      // 禁用任务
      node.getTaskByName(`${target.getTargetName()}@SignHap`)?.setEnable(false);
      node.registerTask({
        // 任务名称
        name: `${targetName}@onlineSignHap`,
        // 任务执行逻辑主体函数
        run() {
          console.log('module Task');
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
