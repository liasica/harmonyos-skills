---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-task
title: 开发Hvigor任务
breadcrumb: 指南 > 构建应用 > 扩展构建能力 > 开发Hvigor任务
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e385db04fc20a11fa74bfd87928de0b115aae36aaa835dcddf3290322cb2ce68
---

## 了解任务

任务是Hvigor构建过程中的基本执行单元，通常包含一段可执行代码；一个任务可以依赖其他多个任务。Hvigor任务调度执行时通过解析依赖关系确定任务执行时序。

UP-TO-DATE

任务标识，表示任务未实际执行。Hvigor任务增量跳过机制，在二次执行任务时检测任务输入输出条件未发生变化，则任务跳过执行提高构建效率。

示例：

```
1. > hvigor UP-TO-DATE ::PackageApp...
```

Finished

任务执行完成标识，表示任务已执行完成。

示例：

```
1. > hvigor Finished ::PackageApp... after 310 ms
```

## 注册任务

使用HvigorNode节点对象注册任务。

1. 编辑工程下hvigorfile.ts文件。

   ```
   1. // 导入模块
   2. import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';
   ```
2. 编写任务代码。

   ```
   1. // 获取当前hvigorNode节点对象
   2. const node: HvigorNode = getNode(__filename);

   4. // 注册Task
   5. node.registerTask({
   6. name: 'customTask',
   7. run() {
   8. console.log('this is Task');
   9. }
   10. });
   ```
3. 执行任务。

   使用hvigor命令行工具执行任务：

   ```
   1. hvigorw customTask
   ```
4. 查看任务执行结果。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/KCW0yEfIQWOKTWgj_9PDQw/zh-cn_image_0000002561753201.png?HW-CC-KV=V1&HW-CC-Date=20260429T054719Z&HW-CC-Expire=86400&HW-CC-Sign=3560AE887FE83D9F6BCC765472FE23047D011BB3F148243862017FB1D4B305A7 "点击放大")
