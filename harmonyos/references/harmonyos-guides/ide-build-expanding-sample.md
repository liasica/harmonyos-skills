---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-expanding-sample
title: API使用示例
breadcrumb: 指南 > 构建应用 > 扩展构建能力 > 扩展构建API > API使用示例
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aafbd7401ec42394bb5dba5c2431df0a6d3b95f93c3326c4aec5f7fcce87974f
---

示例：在工程级hvigorfile.ts文件中分别注册工程级与模块级任务。

```
1. // 工程级hvigorfile.ts文件
2. import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
3. import { appTasks, OhosHapContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';

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
16. // 注册模块级任务
17. hapTask(currentNode);
18. });
19. }
20. };
21. }
22. function hapTask(currentNode: HvigorNode) {
23. // 等待全部节点加载完成之后获取子节点信息
24. currentNode.subNodes((node: HvigorNode) => {
25. // 获取hap模块上下文信息
26. const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
27. const moduleName = hapContext?.getModuleName();
28. hapContext?.targets((target: Target) => {
29. const targetName = target.getTargetName();
30. const outputPath = target.getBuildTargetOutputPath();
31. // 禁用任务
32. node.getTaskByName(`${target.getTargetName()}@SignHap`)?.setEnable(false);
33. node.registerTask({
34. // 任务名称
35. name: `${targetName}@onlineSignHap`,
36. // 任务执行逻辑主体函数
37. run() {
38. console.log('module Task');
39. },
40. // 配置前置任务依赖
41. dependencies: [`${targetName}@PackageHap`],
42. // 配置任务的后置任务依赖
43. postDependencies: ['assembleHap']
44. });
45. });
46. });
47. }
48. export default {
49. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
50. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
51. };
```
