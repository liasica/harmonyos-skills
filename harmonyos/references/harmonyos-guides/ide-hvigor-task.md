---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-task
title: 开发Hvigor任务
breadcrumb: 指南 > 构建应用 > 扩展构建能力 > 开发Hvigor任务
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f2e1f0d4394a2ab1cfe41e044578e6bc642f701b2400251352d962634e535b1f
---

## 了解任务

任务是Hvigor构建过程中的基本执行单元，通常包含一段可执行代码；一个任务可以依赖其他多个任务。Hvigor任务调度执行时通过解析依赖关系确定任务执行时序。

UP-TO-DATE

任务标识，表示任务未实际执行。Hvigor任务增量跳过机制，在二次执行任务时检测任务输入输出条件未发生变化，则任务跳过执行提高构建效率。

示例：

```txt
> hvigor UP-TO-DATE ::PackageApp...
```

Finished

任务执行完成标识，表示任务已执行完成。

示例：

```txt
> hvigor Finished ::PackageApp... after 310 ms
```

## 注册任务

使用HvigorNode节点对象注册任务。

1. 编辑工程下hvigorfile.ts文件。

   ```ts
   // 导入模块
   import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';
   ```
2. 编写任务代码。

   ```screen
   // 获取当前hvigorNode节点对象
   const node: HvigorNode = getNode(__filename);

   // 注册Task
   node.registerTask({
     name: 'customTask',
     run() {
       console.log('this is Task');
     }
   });
   ```
3. 执行任务。

   使用Hvigor命令行工具执行任务：

   ```bash
   hvigorw customTask
   ```
4. 查看任务执行结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/r_Q-HTUfTpyumgGLEFhNwA/zh-cn_image_0000002731542481.png "点击放大")
