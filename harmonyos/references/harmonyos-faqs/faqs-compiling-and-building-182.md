---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-182
title: 推包调试报错“Error message:cannot find record '&XXX/src/main/ets/YYY&x.y.z', please check the request path.'ZZZ.abc'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 推包调试报错“Error message:cannot find record '&XXX/src/main/ets/YYY&x.y.z', please check the request path.'ZZZ.abc'.”
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:01+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:2b7c05ac31204334561cc1b25dcf2b46bd6f9149c5e8f1d9432f223484417dac
---

**问题现象**

在使用DevEco Studio推包到设备进行调试时，如果遇到jscrash报错，FaultLog中显示“Error message: cannot find record '&XXX/src/main/ets/YYY&x.y.z'，请检查请求路径 'ZZZ.abc'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/iihUbdnrRS6of-ztdpKFyw/zh-cn_image_0000002251128405.png?HW-CC-KV=V1&HW-CC-Date=20260429T062100Z&HW-CC-Expire=86400&HW-CC-Sign=5C60428B57D1F56AFD87FD671A5A3009EDE119D6B78CF92A7F4661E69DC8953A)

**问题原因**

**场景一**

字节码HAR（H）使用的依赖包XXX未配置在本模块的oh-package.json5的dependencies或dynamicDependencies中（错误地配置在了工程级oh-package.json5中），请参考[字节码HAR约束条件](../harmonyos-guides/ide-hvigor-build-har.md#section38518561610)。

**解决措施**

需要字节码HAR（H）的生产方重新出包，将对XXX包的依赖添加到本模块的oh-package.json5中。

**场景二**

用户在工程级oh-package.json5和模块级oh-package.json5中同时依赖了XXX包的不同版本，请参考[字节码HAR约束条件](../harmonyos-guides/ide-hvigor-build-har.md#section38518561610)。

**解决措施：**

措施1：手工修改工程级或模块级oh-package.json5，将XXX的版本调整一致。

措施2：通过工程级oh-package.json5中的overrides字段，覆盖模块中使用的其他版本。

**场景三**

将HSP包转成HAR包后，未删除"packageType"，导致按字节码进行打包的时候未解析其相关依赖，请参考[HSP转HAR指导](../harmonyos-guides/hsp-to-har.md#hsp转har的操作步骤)。

**解决措施**

参考"HSP转HAR指导"中的第四步，将模块的oh-package.json5文件中"packageType": "InterfaceHar" 配置删除。

**场景四**

使用了不兼容的第三方插件或SDK对代码进行了修改（如混淆、加固类的SDK），导致了代码无法识别。

**解决措施**

联系对应三方插件或SDK进行解决，如升级版本。

**场景****五**

应用依赖了包XXX，该XXX包在构建时使用了[增量构建](../harmonyos-guides/ide-hvigor-incremental-build.md)的方式，且同时修改了模块级oh-package.json5中的version字段，导致了XXX包中部分文件在寻址时还是用老的版本号去寻址，进而导致找不到相关文件。

**解决措施**

措施1：在XXX包对应工程中执行**Build > Clean Project**操作，然后重新构建项目。

措施2：在工程级hvigorfile.ts文件中增加插件来修复。

1）在工程根目录下新增plugin.ts文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/o7415WO_SVSWPKjpkvxQMQ/zh-cn_image_0000002215928680.png?HW-CC-KV=V1&HW-CC-Date=20260429T062100Z&HW-CC-Expire=86400&HW-CC-Sign=388AD73334C0DC1D093C52197CB9C6B25224EA7D5055BF95A97D305D013AD93F)

plugin.ts文件内容：

```
1. import {OhosPluginId, Target} from '@ohos/hvigor-ohos-plugin';
2. import {hvigor, HvigorNode, HvigorPlugin} from '@ohos/hvigor';
3. import path from "path";
4. import fs from "fs";

7. function getLoaderJsonPath(target: Target) {
8. return path.resolve(target.getBuildTargetOutputPath(), `../../intermediates/loader/${target.getTargetName()}/loader.json`);
9. }

12. function getPkgContextInfoPath(target: Target) {
13. return path.resolve(target.getBuildTargetOutputPath(), `../../intermediates/loader/${target.getTargetName()}/pkgContextInfo.json`);
14. }

17. function deleteLoaderJson(target: Target) {
18. const loaderJsonPath = getLoaderJsonPath(target);
19. if (fs.existsSync(loaderJsonPath)) {
20. fs.rmSync(loaderJsonPath);
21. }
22. }

25. function deletePkgContextInfo(target: Target) {
26. const pkgContextInfoPath = getPkgContextInfoPath(target);
27. if (fs.existsSync(pkgContextInfoPath)) {
28. fs.rmSync(pkgContextInfoPath);
29. }
30. }

33. function deleteRollupCache(target: Target, buildMode: string) {
34. const arkTSCompileCachePath = path.resolve(target.getBuildTargetOutputPath(),
35. `../../cache/${target.getTargetName()}/${target.getTargetName()}@HarCompileArkTS/esmodule/${buildMode}/compiler.cache`);
36. if (fs.existsSync(arkTSCompileCachePath)) {
37. fs.rmSync(arkTSCompileCachePath, { recursive: true });
38. }
39. }

42. function updateHapHspAbcVersion(subNode: HvigorNode, target: Target) {
43. const task = subNode.getTaskByName(`${target.getTargetName()}@GenerateLoaderJson`);
44. if (!task) {
45. console.log('GenerateLoaderJson not found.');
46. return;
47. }
48. deleteLoaderJson(target);
49. deletePkgContextInfo(target);
50. task.afterRun(() => {
51. const pkgContextInfoPath = getPkgContextInfoPath(target);
52. if (!fs.existsSync(pkgContextInfoPath)) {
53. console.log('pkgContextInfo not found.');
54. return;
55. }
56. const pkgContextInfoObj = JSON.parse(fs.readFileSync(pkgContextInfoPath).toString());
57. if (!pkgContextInfoObj) {
58. console.log('pkgContextInfo parse failed.');
59. return;
60. }
61. const loaderJsonPath = getLoaderJsonPath(target);
62. if (!fs.existsSync(loaderJsonPath)) {
63. console.log('loaderJson not found.');
64. return;
65. }
66. const loaderJsonObj = JSON.parse(fs.readFileSync(loaderJsonPath).toString());
67. if (!loaderJsonObj) {
68. console.log('loaderJson parse failed.');
69. return;
70. }
71. for (const [key, value] of Object.entries(pkgContextInfoObj)) {
72. if (!value?.version) {
73. continue;
74. }
75. if (!loaderJsonObj.updateVersionInfo[key]) {
76. loaderJsonObj.updateVersionInfo[key] = {};
77. }
78. loaderJsonObj.updateVersionInfo[key][key] = value.version;
79. }
80. fs.writeFileSync(loaderJsonPath, JSON.stringify(loaderJsonObj));
81. });
82. }

85. function updateHarAbcVersion(target: Target) {
86. deleteLoaderJson(target);
87. deleteRollupCache(target, 'debug');
88. deleteRollupCache(target, 'release');
89. }

92. // The user of bytecode har can use this plugin to correctly modify the version number of ohmurl in abc when integrating bytecode har, ensuring no crashes during runtime
93. export function updateAbcVersionPlugin(): HvigorPlugin {
94. return {
95. pluginId: 'updateAbcVersionPlugin',
96. apply(node: HvigorNode) {
97. hvigor.nodesEvaluated(() => {
98. hvigor.getRootNode().subNodes(subNode => {
99. let context = subNode.getContext(OhosPluginId.OHOS_HAP_PLUGIN);
100. if (!context) {
101. context = subNode.getContext(OhosPluginId.OHOS_HSP_PLUGIN);
102. }
103. if (!context) {
104. return;
105. }
106. context.targets(target => {
107. updateHapHspAbcVersion(subNode, target);
108. });
109. });
110. });
111. }
112. };
113. }

116. // The generator of bytecode har uses this plugin to incrementally build ohmurl with the correct bytecode har after modifying the version number
117. export function updateHarAbcVersionPlugin(): HvigorPlugin {
118. return {
119. pluginId: 'updateHarAbcVersionPlugin',
120. apply(node: HvigorNode) {
121. hvigor.nodesEvaluated(() => {
122. hvigor.getRootNode().subNodes(subNode => {
123. const context = subNode.getContext(OhosPluginId.OHOS_HAR_PLUGIN);
124. if (!context) {
125. return;
126. }
127. context.targets(target => {
128. updateHarAbcVersion(target);
129. });
130. });
131. });
132. }
133. };
134. }
```

[plugin.ts](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/plugin.ts#L6-L139)

2）在工程级hvigorfile.ts文件中增加两个插件，并执行Sync。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/KRhx6Pz6Q1OV4rIi7t47MA/zh-cn_image_0000002216088460.png?HW-CC-KV=V1&HW-CC-Date=20260429T062100Z&HW-CC-Expire=86400&HW-CC-Sign=0FA729DA9FEE7747C4F10CD91137EE0749AC70B5BBE32F2513ACAFE3027841FF)

hvigorfile.ts文件内容：

```
1. import { appTasks } from '@ohos/hvigor-ohos-plugin';
2. import { updateAbcVersionPlugin, updateHarAbcVersionPlugin } from './plugin.ts';

5. export default {
6. system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
7. plugins:[updateAbcVersionPlugin(), updateHarAbcVersionPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
8. }
```

[hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/hvigorfile.ts#L6-L13)

3) 在Terminal终端执行以下命令后，重新推包运行。

```
1. hvigorw --stop-daemon
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/k1oo4dLHTyq7TKpMiLe5cA/zh-cn_image_0000002251048357.png?HW-CC-KV=V1&HW-CC-Date=20260429T062100Z&HW-CC-Expire=86400&HW-CC-Sign=6FBBDE5A622B0EE339EF61E55C041B8C50D1036A9CE40F501CD4AE7B4DC6CFF6)
