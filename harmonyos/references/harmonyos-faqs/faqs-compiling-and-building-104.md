---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-104
title: 如何在构建任务中执行shell脚本
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何在构建任务中执行shell脚本
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:33+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2ac665e28cb14cb1533b664981a9c4245b8622bb97cf199d6be1a02ceeb0f21d
---

## 场景一

只在模块中调用shell脚本，在模块的hvigorfile.ts文件中执行如下示例：

**说明** 

需要特别注意system字段的取值，不同的模块需要使用不同的值：

1. 在har模块的hvigorfile.ts中，需要使用system: harTasks。
2. 在hsp模块的hvigorfile.ts中，需要使用system: hspTasks。
3. 在hap模块的hvigorfile.ts中，需要使用system: hapTasks。

```ts
// 模块级hvigorfile.ts文件
import { harTasks } from '@ohos/hvigor-ohos-plugin';
import { exec } from 'node:child_process';
import util from 'node:util';
const scriptPath = 'xxxx.bat';
// 实现自定义插件
export function customPluginFunction2(str?: string) {
  return {
    pluginId: 'CustomPluginID2',
    apply(pluginContext) {
      pluginContext.registerTask({
       // 在模块上注册任务
        name: 'customTask2',
        run: (taskContext) => {
          console.log('run into: ');
          const execPromise = util.promisify(exec)
          execPromise(scriptPath).then(res => {
            console.log(res, 'res');
          }).catch(err => {
            console.log(err, 'err');
          })
        },
        // 配置前置任务依赖
        dependencies: ['default@BuildJS'],
	// 配置任务的后置任务依赖
        postDependencies: ['default@CompileArkTS']
      })
    }
  }
}
export default {
  // Hvigor插件任务类型，具体请查看最后的说明内容
  system: harTasks,
  // 用于扩展Hvigor功能的自定义插件
  plugins: [customPluginFunction2()]
}
```

## 场景二

如果多个模块的shell脚本是共用的，可以在工程级的hvigorfile.ts中调用：

```ts
// 工程级hvigorfile.ts文件
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { exec } from 'node:child_process';
import util from 'node:util';
const scriptPath = 'xxxx.bat';
// 实现自定义插件
export function customPluginFunction1(): HvigorPlugin {
  return {
    pluginId: 'CustomPluginID1',
    async apply(currentNode: HvigorNode): Promise<void> {
      hvigor.nodesEvaluated(async () => {
        // 注册模块级任务
        hapTask(currentNode);
      });
    }
  };
}
function hapTask(currentNode: HvigorNode) {
  // 遍历所有子模块节点
  currentNode.subNodes((node: HvigorNode) => {
    // 在每个子模块上注册任务
    node.registerTask({
      name: 'customTask1',
      run: (taskContext) => {
        console.log('run into: ', taskContext.moduleName);
        const execPromise = util.promisify(exec);
        execPromise(scriptPath).then(res => {
          console.log(res, 'res');
        }).catch(err => {
          console.log(err, 'err');
        })
      },
	  // 配置前置任务依赖
	  dependencies: ['default@BuildJS'],
	  // 配置任务的后置任务依赖
	  postDependencies: ['default@']
    });
  });
}
export default {
  // 任务类型，不可修改
  system: appTasks,
  // 用于扩展Hvigor功能的自定义插件
  plugins: [customPluginFunction1()]
};
```
