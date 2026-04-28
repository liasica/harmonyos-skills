---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-180
title: 构建HSP模块时报错“Ohos BundleTool [Error]: hsp has home ability;Ohos BundleTool [Error]: CompressEntrance::main exit, verify failed.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建HSP模块时报错“Ohos BundleTool [Error]: hsp has home ability;Ohos BundleTool [Error]: CompressEntrance::main exit, verify failed.”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:46+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:ae1a4602b67969ed9456484692859e61ce1f3f57f2cf284d5c0e1ade01b582f1
---

**问题现象**

构建HSP模块时出现以下错误：Ohos BundleTool [Error]: hsp 包含 home 能力；Ohos BundleTool [Error]: CompressEntrance::main 校验失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/gD0K-_BtTvmnqfjvqrNbsg/zh-cn_image_0000002229758781.png?HW-CC-KV=V1&HW-CC-Date=20260428T002944Z&HW-CC-Expire=86400&HW-CC-Sign=5DE6E8EDB073E424FB212B348C83077EFB96A3AFFAEAC93AC64317068EA3C802)

**问题原因**

1. 从DevEco Studio 5.0.2 Beta1版本开始，HSP支持配置UIAbility组件，除入口Ability外。
2. 构建过程中，HSP模块会将依赖的HAR中的Ability与其自身配置合并。因此，HSP不支持依赖带有入口Ability的HAR。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/FXi8Ri0QTkS3NTHPfOzyvQ/zh-cn_image_0000002229604285.png?HW-CC-KV=V1&HW-CC-Date=20260428T002944Z&HW-CC-Expire=86400&HW-CC-Sign=A6DFF25B98BCBEFB6BB35DEAC9022136AEC23862CF6D0FBF313A906116235EDE)

**解决措施**

1. 排查当前构建的HSP模块的module.json5，删除入口Ability中多余的skills配置，然后重新构建。
2. 排查HSP模块依赖的HAR模块的module.json5文件。如果入口Ability配置了HAR，则：
   1. 若为本地源码依赖，删除上述配置后重新构建，或移除HSP中对该模块的依赖。
   2. 若为第三方包依赖，需删除对应配置并重新发布，更新依赖版本后重新构建。
   3. 如果第三方包依赖无法重新发布，可以通过Hvigor自定义插件在HSP模块中增加自定义任务，删除build/${productName}/intermediates/package/${targetName}/module.json中的入口 Ability 相关配置，然后重新构建。

      ```
      1. // HSP module hvigorfile.ts
      2. import { hspTasks,OhosPluginId, Target } from '@ohos/hvigor-ohos-plugin';
      3. import { hvigor, HvigorNode, HvigorPlugin,FileUtil } from '@ohos/hvigor';
      4. export function customPlugin():HvigorPlugin {
      5. return {
      6. pluginId: 'customPlugin',
      7. context() {
      8. return {
      9. data: 'customPlugin xxx'
      10. };
      11. },
      12. apply(currentNode:HvigorNode): Promise<void> {
      13. hvigor.nodesEvaluated(async () => {
      14. hspTask(currentNode);
      15. });
      16. }
      17. }
      18. }
      19. function hspTask(currentNode: HvigorNode) {
      20. // Obtain contextual information of the HSP module
      21. const hspContext = currentNode.getContext(OhosPluginId.OHOS_HSP_PLUGIN) as OhosHspContext;
      22. hspContext?.targets((target: Target) => {
      23. const targetName = target.getTargetName();
      24. const outputPath = target.getBuildTargetOutputPath();
      25. const task = currentNode.getTaskByName(`${targetName}@GeneratePkgModuleJson`);
      26. currentNode.registerTask({
      27. // TASK
      28. name: `${targetName}@changeModuleJson`,
      29. // Task execution logic entity function
      30. run() {
      31. const moduleJson = FileUtil.readJson5(outputPath+"/../../intermediates/package/"+targetName+"/module.json");
      32. const abilities = moduleJson['module']['abilities'];
      33. abilities.forEach((ability)=>{
      34. delete ability['skills'];
      35. })
      36. console.log('begin to rewrite module.json file.');
      37. moduleJson['module']['abilities'] = abilities
      38. FileUtil.writeFileSync(outputPath+"/../../intermediates/package/"+targetName+"/module.json",JSON.stringify(moduleJson));
      39. },
      40. // Configure prerequisite task dependencies
      41. dependencies: [`${targetName}@GeneratePkgModuleJson`],
      42. // Post task dependencies for configuring tasks
      43. postDependencies: [`${targetName}@PackageSharedHar`]
      44. });
      45. });
      46. }
      47. export default {
      48. system: hspTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
      49. plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
      50. }
      ```

      [hvigorfile\_hsp.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/hvigorfile_hsp.ts#L6-L55)
