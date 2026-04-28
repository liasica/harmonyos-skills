---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-169
title: 如何快速关闭工程中所有字节码HAR配置
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何快速关闭工程中所有字节码HAR配置
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9dfa418cec02638acb1a9476a1268e12b7ca4867134f789c38940c6db1973602
---

**解决措施**

方案一：适用于HAR文件较少的场景，直接修改字段byteCodeHar为false，详细字段可在以下链接中查询：[模块级build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile.md)

方案二：适用于HAR文件数量较多的场景。单独为每个HAR包配置较为繁琐，可以通过自定义插件直接修改所有HAR包的byteCodeHar字段值。该方法在编译时生效，但不会修改build-profile.json5文件中的字段值。

```
1. // Engineering-level hvigorfile.ts file
2. import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';
3. import { appTasks, OhosHarContext, OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
4. // Implement custom plugins
5. export function customPlugin(): HvigorPlugin {
6. return {
7. pluginId: 'customPlugin',
8. async apply(currentNode: HvigorNode): Promise<void> {
9. hvigor.afterNodeEvaluate(async () => {
10. // Register module-level tasks
11. harTask(currentNode);
12. });
13. }
14. };
15. }
16. function harTask(currentNode: HvigorNode) {
17. currentNode.subNodes((node: HvigorNode) => {
18. const context = node.getContext(OhosPluginId.OHOS_HAR_PLUGIN)
19. context?.targets((target: Target) => {
20. const targetName = target.getTargetName();
21. node.registerTask({
22. // Task name
23. name: `HarTask`,
24. // Main function of task execution logic
25. run() {
26. if (context.getBuildProfileOpt) {
27. const buildProfile = context.getBuildProfileOpt();
28. console.log(buildProfile)
29. // Set the bytecode har config to false
30. buildProfile["buildOption"] = { arkOptions: { byteCodeHar: false } };
31. console.log(buildProfile)
32. context.setBuildProfileOpt(buildProfile);
33. }
34. },
35. // Configure the dependency of the pre-task
36. dependencies: [`${targetName}@PackageHar`],
37. // Post-task dependency for configuring tasks
38. postDependencies: ['assembleHar']
39. });
40. });
41. });
42. }
43. export default {
44. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
45. plugins:[customPlugin()]  /* Custom plugin to extend the functionality of Hvigor. */
46. }
```

[hvigorfile\_test.ts](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/hvigorfile_test.ts#L4-L49)
