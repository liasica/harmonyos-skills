---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-plugin
title: 开发Hvigor插件
breadcrumb: 指南 > 构建应用 > 扩展构建能力 > 开发Hvigor插件
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8b8581442c8c9829d92bbd37ec76080095c1d91bd2ef71f408b8889e0fd87be0
---

Hvigor允许开发者实现自己的插件，开发者可以定义自己的构建逻辑，并与他人共享。

Hvigor主要提供了两种方式来实现插件：基于hvigorfile脚本开发插件、基于typescript项目开发。

关于插件开发的具体实践请参考[定制hvigor插件开发实践](../best-practices/bpta-custom-hvigor-plugin.md)。

## 基于hvigorfile脚本开发

基于hvigorfile.ts脚本开发的方式，其优点是可实现快速开发，直接编辑工程或模块下hvigorfile.ts即可编写插件代码，不足之处是在多个项目中，无法方便地进行插件代码的复用和共享分发。

从DevEco Studio 6.0.2 Beta1版本开始，在构建脚本中编写代码时，支持代码补全、代码生成、代码重构等代码编辑能力，具体使用方式请参考[代码阅读](ide-editer-overview.md)、[代码生成/补全](ide-code-completion.md)、[代码重构](ide-code-refactoring.md)。

若开发者需要创建新的构建脚本，推荐将这些脚本统一放在工程或模块的scripts目录下，以便与应用代码进行隔离，示例如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/-g-Bzp7cQNWkVYxZRe5Cog/zh-cn_image_0000002561832859.png?HW-CC-KV=V1&HW-CC-Date=20260429T054331Z&HW-CC-Expire=86400&HW-CC-Sign=F0CCDAEA8B4611E5051F354B4DEF39AA603DC77107A1E8B040C2DFDFC7F9AAEC)

以工程级hvigorfile.ts脚本为例，开发步骤如下。

1. 导入模块依赖，更多接口请参考[扩展构建API](ide-hvigor-apis.md)。

   ```
   1. // 工程级hvigorfile.ts
   2. import { appTasks } from '@ohos/hvigor-ohos-plugin';
   3. import { HvigorPlugin, HvigorNode } from '@ohos/hvigor';
   ```
2. 编写插件代码，实现HvigorPlugin接口。

   ```
   1. // 工程级hvigorfile.ts
   2. function customPlugin(): HvigorPlugin {
   3. return {
   4. pluginId: 'customPlugin',
   5. apply(node: HvigorNode) {
   6. // 插件主体
   7. console.log('hello customPlugin!');
   8. }
   9. }
   10. }
   ```
3. 在导出声明中使用插件。

   ```
   1. // 工程级hvigorfile.ts
   2. export default {
   3. system: appTasks,
   4. plugins:[
   5. customPlugin()  // 应用自定义Plugin
   6. ]
   7. }
   ```
4. 执行Hvigor命令。

   执行Hvigor命令时，在Hvigor生命周期配置阶段执行插件中的apply方法。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/PzRekmEvQp-IAzNL99jL6A/zh-cn_image_0000002530912940.png?HW-CC-KV=V1&HW-CC-Date=20260429T054331Z&HW-CC-Expire=86400&HW-CC-Sign=7DDB0A326B93B774AF963A64458432852410223804D45AB9446AE26D282BCCCF)

## 基于typescript项目开发

基于typescript项目开发较好地弥补了上一小节中使用hvigorfile脚本方式编写插件代码不易复用和共享分发的问题。因此通常情况下推荐此方式开发。

### 初始化typescript项目

1. 创建一个空目录。

   在命令行工具中使用cd命令进入空目录下。
2. 安装typescript模块。

   ```
   1. // 全局安装TypeScript
   2. npm install typescript -g
   ```
3. 初始化npm项目。

   执行如下命令，根据命令行指示配置项目。初始化完成后会生成package.json文件。

   ```
   1. // 初始化一个npm项目
   2. npm init
   ```
4. 生成typescript配置文件。

   执行如下命令生成tsconfig.json文件。

   ```
   1. // 初始化typeScript配置文件
   2. tsc --init
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/jXQEpDnCQpuuBHVTkMiuMQ/zh-cn_image_0000002561752881.png?HW-CC-KV=V1&HW-CC-Date=20260429T054331Z&HW-CC-Expire=86400&HW-CC-Sign=2F9F9370BE66EF9ECCA61B7A87B8E381FB785838623C43DE7E1DD3C44A8D3DE7)
5. 删除verbatimModuleSyntax字段。

   检查tsconfig.json文件是否存在verbatimModuleSyntax字段，如果存在且配置为true，会导致无法使用ESM语法，编译时会报错，因此需要删除该字段。

### 开发插件

1. 配置npm镜像仓库地址，用于安装@ohos/hvigor插件。

   在工程目录下创建.npmrc文件，配置如下信息：

   ```
   1. registry=https://repo.huaweicloud.com/repository/npm/
   2. @ohos:registry=https://repo.harmonyos.com/npm/
   ```
2. 添加依赖声明。

   打开package.json添加devDependencies配置。

   ```
   1. "devDependencies": {
   2. "@ohos/hvigor": "5.2.2"
   3. }
   ```
3. 安装依赖。

   执行如下命令安装依赖。

   ```
   1. npm install
   ```
4. 编写插件代码。

   在src/plugin目录下创建custom-plugin.ts文件，编写插件代码，更多接口请参考[扩展构建API](ide-hvigor-apis.md)。

   ```
   1. import type { HvigorNode, HvigorPlugin } from '@ohos/hvigor';

   3. export function customPlugin(): HvigorPlugin {
   4. return {
   5. pluginId: 'customPlugin',
   6. apply(node: HvigorNode) {
   7. console.log('hello customPlugin!');
   8. }
   9. }
   10. }
   ```
5. 导出插件。

   创建index.ts文件，并在该文件中声明插件方法的导出。由于.ts最终会编译成.js文件，因此需要导出.js文件。

   ```
   1. export { customPlugin } from './src/plugin/custom-plugin.js';
   ```

### 发布插件

typescript项目本质上是一种npm项目，插件发布流程遵循npm发布规范。详情请查询npm官方资料。

发布npm包流程：

1. 配置registry。

   打开工程目录下的.npmrc文件，配置您需要发布的镜像仓库。

   ```
   1. registry=[npm镜像仓库地址]
   ```
2. 生成AccessToken。

   执行如下命令，注册并登录npm仓库，在工程目录下.npmrc文件中自动生成token信息。

   ```
   1. npm login
   ```
3. 编译npm包。

   ```
   1. tsc
   ```

   如果编译时报以下错误，请检查初始化项目时是否[删除了verbatimModuleSyntax](ide-hvigor-plugin.md#li88369101451)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/uojYOcOWTBmsZFOGVaubvA/zh-cn_image_0000002530752942.png?HW-CC-KV=V1&HW-CC-Date=20260429T054331Z&HW-CC-Expire=86400&HW-CC-Sign=3675E3E2341030D0F53ED8F1DA1BA88F2626F1296D73A919AD66B95E62DBAEB1)
4. 发布npm包。

   执行如下命令，将npm项目打包并发布至镜像仓库。

   ```
   1. npm publish
   ```

### 使用插件

1. 添加依赖。

   在工程下hvigor/hvigor-config.json5中添加自定义插件依赖，依赖项支持离线插件配置。

   ```
   1. "dependencies": {
   2. "custom-plugin": "1.0.0"   // 添加自定义插件依赖
   3. }
   ```
2. 安装依赖。
   * 方式1：执行编辑区右上角**Sync** **Now**或执行菜单**File -> Sync and Refresh Project**进行工程Sync后，DevEco Studio将会根据hvigor-config.json5中的依赖配置自动安装。
   * 方式2：使用hvigorw命令行工具执行任一命令，命令行工具会自动执行安装构建依赖。

     ```
     1. hvigorw --sync
     ```
3. 导入插件。

   根据插件编写时基于的node节点，确定导入的节点所在的hvigorfile.ts文件，在hvigorfile.ts中导入插件。

   ```
   1. import { customPlugin } from 'custom-plugin';
   ```
4. 使用插件。

   将自定义插件添加到export default的plugins中。

   ```
   1. export default {
   2. system: appTasks,  // 以工程级hvigorfile.ts为例
   3. plugins:[
   4. customPlugin()  // 应用自定义插件
   5. ]
   6. }
   ```
