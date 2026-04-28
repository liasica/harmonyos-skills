---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-to-hsp
title: HAR转HSP指导
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > HAR转HSP指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4c8aab6d6dadbe59854457539ba884a6332c5ac543c978d3d18d0bc9bcc21d81
---

目前HAR的使用存在打包多份，包膨胀的问题，导致整体应用包的体积很大，HSP可以很好地解决该问题，本文介绍如何通过配置项的变更将HAR工程转换为HSP工程。

说明

部分组件和模块在HAP、HSP、HAR中集成使用时存在差异，例如[加载HAR中Worker线程文件相比HSP存在单独的使用约束](worker-introduction.md#文件路径注意事项)，因此按照如下步骤完成HAR转HSP后，请关注对应组件和模块介绍并进行适配。

## HAR转HSP的操作步骤

1. 修改HAR模块下的module.json5文件，将type字段设置为shared，并新增deliveryWithInstall和pages字段。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "type": "shared",
   5. "deliveryWithInstall": true,
   6. "pages": "$profile:main_pages",
   7. // ...
   8. }
   9. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarToHsp/library/src/main/module.json5#L16-L33)
2. 在resources\base下新增profile文件夹，在profile下新增一个main\_pages.json文件，并配置如下内容。

   ```
   1. {
   2. "src": [
   3. "pages/PageIndex"
   4. ]
   5. }
   ```
3. 在ets目录下新增pages目录，并在pages目录下新增PageIndex.ets文件，配置如下内容。

   ```
   1. @Entry
   2. @Component
   3. struct PageIndex {
   4. @State message: string = 'hello world';

   6. build() {
   7. Row() {
   8. Column() {
   9. Text(this.message)
   10. .fontSize(50)
   11. .fontWeight(FontWeight.Bold)
   12. }
   13. .width('100%')
   14. }
   15. .height('100%')
   16. }
   17. }
   ```

   [PageIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarToHsp/library/src/main/ets/pages/PageIndex.ets#L16-L34)
4. 删除HAR模块的build-profile.json5文件中的consumerFiles字段配置。
5. 修改HAR模块的hvigorfile.ts文件，将以下内容替换文件内容。

   ```
   1. // library\hvigorfile.ts
   2. import { hspTasks } from '@ohos/hvigor-ohos-plugin';

   4. export default {
   5. system: hspTasks,  // 编译修改成HSP的任务
   6. plugins:[]
   7. }
   ```

   [hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarToHsp/library/hvigorfile.ts#L16-L24)
6. 修改oh-package.json5文件，新增packageType配置。

   ```
   1. {
   2. // ...
   3. "packageType": "InterfaceHar"
   4. }
   ```

   [oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarToHsp/library/oh-package.json5#L16-L29)
7. 修改项目根目录下的build-profile.json5文件，在modules标签下找到library的配置，新增targets标签。

   ```
   1. "modules": [
   2. // ...
   3. {
   4. "name": "library",
   5. "srcPath": "./library",
   6. "targets": [
   7. {
   8. "name": "default",
   9. "applyToProducts": [
   10. "default"
   11. ]
   12. }
   13. ]
   14. }
   15. ],
   ```

   [build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarToHsp/build-profile.json5#L43-L72)
