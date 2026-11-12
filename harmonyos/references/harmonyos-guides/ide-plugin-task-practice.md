---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-plugin-task-practice
title: 性能优化：自定义插件和任务优化实践
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 提升构建效率 > 实践说明 > 性能优化：自定义插件和任务优化实践
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:0b2dc03577fa3c0a97a302e254b937576b17f10d36fce03a24c0d78c0b862271
---

## 概述

开发者可通过自定义插件和任务扩展构建能力，实现自动化构建步骤、定制化资源处理等需求。本文主要内容如下：

1. 通过自定义插件示例分析可能的性能问题并给出优化方案。
2. 通过自定义任务示例分析可能的性能问题并给出优化方案。

## 优化自定义插件

### 示例

开发者可以通过实现[HvigorPlugin接口](ide-hvigor-api.md#section182865194515)的方式开发[自定义插件](ide-hvigor-plugin.md)。下面示例在entry/hvigorfile.ts中定义一个插件，模拟开发者在构建Hap开始阶段下载必要资源的场景。

```ts
// entry/hvigorfile.ts
import { hapTasks } from '@ohos/hvigor-ohos-plugin';
import { HvigorPlugin, HvigorNode } from '@ohos/hvigor';

class MyCustomPlugin implements HvigorPlugin {
  pluginId = 'customPlugin';

  async apply(node: HvigorNode): Promise<void> {
    console.log('download start at', new Date());
    await new Promise<void>((resolve) => {
      setTimeout(() => {
        // 使用延时模拟耗时操作
        console.log('download end at', new Date());
        resolve();
      }, 5000);
    });
  }
}

export default {
  system: hapTasks,
  plugins: [new MyCustomPlugin()]
}
```

点击ReBuild Project构建工程，构建窗口输出日志如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/rYrWTMyhSYmnbUE1H8tsyA/zh-cn_image_0000002808886469.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=988F8F75B63B8DA39185605D99049D09149A9C1D3DB7A4B2692E0DBB7E0D617E)

执行Sync时，也会触发下载操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/i2D3hDYJShGdA1lGWfkBow/zh-cn_image_0000002779566802.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2ACA792B718D33EC7F95756D8CE60A9BB3ACD4251E6AB22BF3327481724ECD8)

### 问题分析

HvigorPlugin的apply方法运行在构建[生命周期](ide-hvigor-life-cycle.md#section746253616316)的配置阶段（内部生命周期函数，开发者无法使用）。上述示例中，耗时的业务下载逻辑直接在apply方法中执行，apply方法无增量跳过机制，导致每次构建都必须执行，并且耗时的操作会阻塞主线程逻辑，影响开发效率。

### 优化方案

业务耗时的逻辑应避免直接在apply方法中执行，建议：

* 将业务逻辑放在明确的生命周期钩子函数中，如[hvigor.nodesEvaluated()](ide-hvigor-api.md#section104511551152118)，确保业务在明确的阶段执行。
* 将业务逻辑注册为HvigorTask任务，使得业务在构建生命周期的执行阶段执行，并且可以选择使用任务的增量机制避免重复执行。

下面示例对上面实现进行改造，使用HvigorTask任务承载业务逻辑：

```ts
// entry/hvigorfile.ts
import { hapTasks, OhosPluginId, OhosHapContext, Target } from '@ohos/hvigor-ohos-plugin';
import { HvigorPlugin, HvigorNode, hvigor } from '@ohos/hvigor';

class MyCustomPlugin implements HvigorPlugin {
  pluginId = 'customPlugin';

  async apply(node: HvigorNode): Promise<void> {
    const hapContext = node?.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    hapContext?.targets((target: Target) => {
      const targetName = target.getTargetName();
      // 把业务逻辑封装到任务里面，apply方法中不再执行下载操作，下载操作推迟到任务执行阶段
      node?.registerTask({
        name: `${targetName}@DownloadTask`,
        async run() {
          console.log('download start at', new Date());
          await new Promise<void>((resolve) => {
            setTimeout(() => {
              // 使用延时模拟耗时操作
              console.log('download end at', new Date());
              resolve();
            }, 5000);
          });
        },
        // 设置前置依赖任务，PreBuild任务会先于本任务执行
        dependencies: [`${targetName}@PreBuild`],
        // 设置后置依赖任务，本任务会先于CreateModuleInfo任务执行
        postDependencies: [`${targetName}@CreateModuleInfo`]
      });
    });
  }
}

export default {
  system: hapTasks,
  plugins: [new MyCustomPlugin()]
}
```

改造之后，Sync流程不会触发下载操作：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/_whPbL_0RRCC-rV9WTAWXA/zh-cn_image_0000002779406818.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=58A6DA8F93AA882ACEDE6EE4286E27064B9F9029B4442BF76761F6BC29D09DF2)

用户的业务逻辑在任务执行阶段执行：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/4qpkkCzXTbCQrD3R2-TfOA/zh-cn_image_0000002779406824.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C1F53F8C41E70FA08160C7D263512AA921FE35105EEE0D15887EF23CAF5AA284)

还可以进一步利用任务的增量机制优化增量构建场景，请参考下文介绍。

## 优化自定义任务

### 示例

开发者可以在hvigorfile.ts中通过[registerTask](ide-hvigor-api.md#section6972141673518)接口注册[HvigorTask](ide-hvigor-api.md#section2386634104512)的方式开发自定义任务。每个模块级hvigorfile.ts可注册多个任务，任务之间通过[dependencies](ide-hvigor-api.md#section16299334294)（前置依赖）和[postDependencies](ide-hvigor-api.md#section25972367914)（后置依赖）声明依赖关系。

下面示例在entry/hvigorfile.ts中注册两个HvigorTask任务，模拟开发者操作编译产物的场景。

```ts
// entry/hvigorfile.ts
// 注册两个自定义任务操作输出目录
import { hapTasks, OhosPluginId, OhosHapContext, Target } from '@ohos/hvigor-ohos-plugin';
import { getNode, hvigor, HvigorNode } from '@ohos/hvigor';

hvigor.nodesEvaluated(() => {
  const node: HvigorNode | undefined = getNode(__filename);
  const hapContext = node?.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
  hapContext?.targets((target: Target) => {
    const targetName = target.getTargetName();
    const buildTargetOutputPath = target.getBuildTargetOutputPath();
    // 注册自定义任务CustomTask0
    node?.registerTask({
      name: `${targetName}@CustomTask0`,
      async run() {
        await new Promise<void>((resolve) => {
          setTimeout(() => {
            // 使用延时模拟耗时操作
            console.log(`${this.name} Processing files in the directory:`, buildTargetOutputPath);
            resolve();
          }, 5000);
        });
      },
      // 设置前置依赖任务，SignHap任务会先于本任务执行
      dependencies: [`${targetName}@SignHap`],
      // 设置后置依赖任务，本任务会先于assembleHap任务执行
      postDependencies: ['assembleHap']
    });
    // 注册自定义任务CustomTask1
    node?.registerTask({
      name: `${targetName}@CustomTask1`,
      async run() {
        await new Promise<void>((resolve) => {
          setTimeout(() => {
            console.log(`${this.name} Processing files in the directory:`, buildTargetOutputPath);
            resolve();
          }, 5000);
        });
      },
      dependencies: [`${targetName}@SignHap`],
      postDependencies: ['assembleHap']
    });
  });
});

export default {
  system: hapTasks,
  plugins: []
}
```

点击ReBuild Project构建工程，构建窗口输出日志如下，端到端全量构建约15s。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/j9GMpaDbSd2cM7QatZ_UdA/zh-cn_image_0000002808886463.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=6098927E6B61F006295922F2E31173EDBD7C020017E01BC04D641B277E59F0C7)

### 问题分析

以上示例代码存在两个问题，重复构建和串行构建。

* **问题一：重复构建**
  + 现象：两个自定义任务每次构建都会重新执行，即使源码未发生变化。表现为连续两次构建耗时基本相同，自定义任务显示为“Finished”状态，表示任务已执行完成。
  + 影响：每次构建都执行自定义任务，影响开发效率。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/Pag9gywiT6244U72KvpFaw/zh-cn_image_0000002779406826.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=B6794D3421417207D178A8915AAD788F1AF8CA9E551653E5B8CC14D409EC109E)
* **问题二：串行构建**
  + 现象：两个自定义任务没有相互依赖关系，但Build Analyzer显示CustomTask0和CustomTask1任务串行执行，并且在主线程中执行，阻塞主线程执行其他任务。
  + 影响：构建总耗时是多个任务耗时总和，构建时间长，且无法充分利用CPU。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/eX-GLpoBQoqNW6_WLwSZ0A/zh-cn_image_0000002808766379.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=F506F574F3273755D3AC193E4C8255BD84C98F1DA6F3347BAE33EA828945274F)

### 优化方案

针对上述问题，建议按照以下方案进行优化。

* **优化一：增量构建**

  使用增量机制，通过配置[input](ide-hvigor-api.md#section2697112881011)或[output](ide-hvigor-api.md#section131451256911)函数，声明任务依赖的文件或目录。Hvigor会记录这些文件/目录的元数据哈希值，仅在文件/目录发生变化时才执行任务。

  以增加input函数为例，优化后的示例代码如下。

  ```ts
  // entry/hvigorfile.ts
  // 注册两个自定义任务操作输出目录
  import fs from 'node:fs';
  import { hapTasks, OhosPluginId, OhosHapContext, Target } from '@ohos/hvigor-ohos-plugin';
  import { getNode, hvigor, HvigorNode, TaskInput } from '@ohos/hvigor';

  hvigor.nodesEvaluated(() => {
    const node: HvigorNode | undefined = getNode(__filename);
    const hapContext = node?.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
    hapContext?.targets((target: Target) => {
      const targetName = target.getTargetName();
      const buildTargetOutputPath = target.getBuildTargetOutputPath();
      // 注册自定义任务CustomTask0
      node?.registerTask({
        name: `${targetName}@CustomTask0`,
        async run() {
          await new Promise<void>((resolve) => {
            setTimeout(() => {
              // 使用延时模拟耗时操作
              console.log(`${this.name} Processing files in the directory:`, buildTargetOutputPath);
              resolve();
            }, 5000);
          });
        },
        // 增加input输入依赖配置
        input(input: TaskInput) {
          if (fs.existsSync(buildTargetOutputPath)) {
            // input.file方法声明任务依赖的文件或者目录，这里把buildTargetOutputPath目录加入增量判断集合中
            // 当buildTargetOutputPath目录内容未变化时，任务会被跳过执行
            input.file(buildTargetOutputPath);
          }
        },
        // 设置前置依赖任务，SignHap任务会先于本任务执行
        dependencies: [`${targetName}@SignHap`],
        // 设置后置依赖任务，本任务会先于assembleHap任务执行
        postDependencies: ['assembleHap']
      });
      // 注册自定义任务CustomTask1
      node?.registerTask({
        name: `${targetName}@CustomTask1`,
        async run() {
          await new Promise<void>((resolve) => {
            setTimeout(() => {
              console.log(`${this.name} Processing files in the directory:`, buildTargetOutputPath);
              resolve();
            }, 5000);
          });
        },
        // 增加input输入依赖配置
        input(input: TaskInput) {
          if (fs.existsSync(buildTargetOutputPath)) {
            input.file(buildTargetOutputPath);
          }
        },
        dependencies: [`${targetName}@SignHap`],
        postDependencies: ['assembleHap']
      });
    });
  });

  export default {
    system: hapTasks,
    plugins: []
  }
  ```

  无代码变更时，重复构建，结果如下，自定义任务显示为“UP-TO-DATE”状态，表示任务被跳过。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/X302RDW3Teq4wbReZz8CEQ/zh-cn_image_0000002779566798.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=5A8724F45C41EACC82D6F091C5C6AF224D2C849CE8614CD53504F8A0EEF48A06)
* **优化二：并行执行**

  对于耗时较长的任务，可通过[submitWorker](ide-hvigor-api.md#section94763341419)接口将任务分发到worker线程中执行，实现并行处理。

  使用场景：

  + 单个任务处理耗时较长（如大量文件压缩、代码转译）。
  + 多个同类型任务之间无依赖关系。
  + 需要充分利用多核CPU资源。

  优化后的示例代码如下。

  1. worker脚本实现。

     ```js
     // 在entry/scripts目录下创建custom-job.js
     async function runJob(workInput) {
       await new Promise((resolve) => {
         setTimeout(() => {
           console.log(`${workInput.taskName} Processing files in the directory:`, workInput.outputPath);
           resolve();
         }, 5000);
       })
     }

     exports.runJob = runJob;
     ```
  2. 修改run的实现，使用submitWorker加载custom-job.js脚本并提交到worker中执行。

     ```ts
     // entry/hvigorfile.ts
     // 注册两个自定义任务操作输出目录
     import fs from 'node:fs';
     import path from "node:path";
     import { hapTasks, OhosPluginId, OhosHapContext, Target } from '@ohos/hvigor-ohos-plugin';
     import { getNode, hvigor, HvigorNode, TaskInput, submitWorker } from '@ohos/hvigor';

     hvigor.nodesEvaluated(() => {
       const node: HvigorNode | undefined = getNode(__filename);
       const hapContext = node?.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
       hapContext?.targets((target: Target) => {
         const targetName = target.getTargetName();
         const buildTargetOutputPath = target.getBuildTargetOutputPath();
         // 注册自定义任务CustomTask0
         node?.registerTask({
           name: `${targetName}@CustomTask0`,
           async run() {
             // 提交custom-job.js脚本到worker中执行, 请确保该文件来源可信
             submitWorker(node, this.name, path.join(__dirname, 'scripts', 'custom-job.js', 'runJob'), {
               workInput: {
                 taskName: this.name,
                 outputPath: buildTargetOutputPath,
               }
             });
           },
           // 增加input输入依赖配置
           input(input: TaskInput) {
             if (fs.existsSync(buildTargetOutputPath)) {
               input.file(buildTargetOutputPath);
             }
           },
           // 设置前置依赖任务，SignHap任务会先于本任务执行
           dependencies: [`${targetName}@SignHap`],
           // 设置后置依赖任务，本任务会先于assembleHap任务执行
           postDependencies: ['assembleHap']
         });
         // 注册自定义任务CustomTask1
         node?.registerTask({
           name: `${targetName}@CustomTask1`,
           async run() {
             // 提交custom-job.js脚本到worker中执行, 请确保该文件来源可信
             submitWorker(node, this.name, path.join(__dirname, 'scripts', 'custom-job.js', 'runJob'), {
               workInput: {
                 taskName: this.name,
                 outputPath: buildTargetOutputPath,
               }
             });
           },
           // 增加input输入依赖配置
           input(input: TaskInput) {
             if (fs.existsSync(buildTargetOutputPath)) {
               input.file(buildTargetOutputPath);
             }
           },
           dependencies: [`${targetName}@SignHap`],
           postDependencies: ['assembleHap']
         });
       });
     });

     export default {
       system: hapTasks,
       plugins: []
     }
     ```

  并行效果验证：

  1. 通过Build Analyzer观察，CustomTask0和CustomTask1呈并行执行状态。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/uL4DtvCPSfyNS-CATpEsBw/zh-cn_image_0000002808886467.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED60767DD4FB7E8E686A4CAFE52B316176B4700D05183903DE7D240128D07ED8)
  2. 编译构建耗时也得到优化，从一开始的端到端全量构建15s降到10s左右。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/5jdyrmFuS_mAdnPeUGuqvg/zh-cn_image_0000002808766387.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=8BF7226EA17090C1DE010831B292B69156CAB91DCA8732A10C866E7E35E5F578)

## 总结

开发自定义插件和任务时，可从以下几方面实践并验证优化性能问题。

1. 将复杂耗时的业务逻辑封装为独立的HvigorTask，并在插件的apply方法中进行注册。
2. 插件用于组织和管理HvigorTask，不过度参与具体执行。
3. 避免在hvigorfile.ts全局作用域编写同步执行代码，而是使用生命周期钩子函数（如nodesEvaluated）控制执行时机。
4. 自定义任务配置input，声明依赖文件；或者配置output，声明输出文件；连续构建时，确认未变化的任务已被跳过，构建结果显示“UP-TO-DATE”。
5. 耗时任务通过submitWorker分发到worker执行，通过Build Analyzer验证任务并行执行。
