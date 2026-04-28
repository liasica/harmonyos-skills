---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-storage-initialize-context
title: 初始化全局应用上下文
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云存储 > 初始化全局应用上下文
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b2e4dbff3377cee2288bc7c284e15d56244dbb6b0642f3835b4feeee2b0ee23
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 操作步骤

在使用云存储服务进行上传下载时，需要使用应用上下文context。可参考如下代码初始化全局应用上下文。

1. 在“entry/src/main/ets/common”目录下添加GlobalContext.ets文件，开发初始化和获取应用上下文的接口。

   ```
   1. import { common } from '@kit.AbilityKit';

   3. export class GlobalContext {
   4. private static context: common.UIAbilityContext;

   6. public static initContext(context: common.UIAbilityContext): void {
   7. GlobalContext.context = context;
   8. }

   10. public static getContext(): common.UIAbilityContext {
   11. return GlobalContext.context;
   12. }
   13. }
   ```
2. 在“entry/src/main/ets/entryability/EntryAbility.ets”文件中导入GlobalContext，在onCreate方法中使用GlobalContext.initContext(this.context)初始化全局应用上下文。
