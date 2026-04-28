---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/printextensionabilityguide
title: 打印扩展能力
breadcrumb: 指南 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 打印 > 打印扩展能力
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:48a388d3d3d181b65bad1ff723d9f9acf0a6d3ba1432a1548ae0d264ee6232b3
---

## 概述

打印扩展能力从API version 14开始支持。打印扩展能力是对系统打印功能的扩展，允许开发者以软件的方式模拟打印机行为，实现与上层应用的打印交互。通过该扩展能力，开发者可以实现特殊场景下的定制化打印逻辑，在统一框架下灵活开发差异化功能，提升解决方案的适应性与可维护性。

## 回调说明

| 回调名称 | 回调描述 |
| --- | --- |
| [onCreate(want: Want): void](../harmonyos-references/js-apis-app-ability-printextensionability.md#oncreate) | 初始化打印机能力 |
| [onDestroy(): void](../harmonyos-references/js-apis-app-ability-printextensionability.md#ondestroy) | 结束打印扩展 |
| [onStartDiscoverPrinter(): void](../harmonyos-references/js-apis-app-ability-printextensionability.md#onstartdiscoverprinter) | 开始发现打印机 |
| [onStopDiscoverPrinter(): void](../harmonyos-references/js-apis-app-ability-printextensionability.md#onstopdiscoverprinter) | 停止发现打印机 |
| [onConnectPrinter(printerId: number): void](../harmonyos-references/js-apis-app-ability-printextensionability.md#onconnectprinter) | 连接打印机 |
| [onDisconnectPrinter(printerId: number): void](../harmonyos-references/js-apis-app-ability-printextensionability.md#ondisconnectprinter) | 断开与打印机的连接 |

## 开发步骤

### 实现打印扩展能力

1. 新建工程目录

   在工程entry Module对应的ets目录 (./entry/src/main/ets)下，新建目录及ArkTs文件。例如新建一个目录并命名为PrintExtensionAbility，在PrintExtensionAbility目录下，新建一个ArkTs文件并命名为MyPrintExtension.ets，用以实现打印扩展能力接口。
2. 打开MyPrintExtension.ets文件，导入模块。

   ```
   1. import { PrintExtensionAbility } from '@kit.BasicServicesKit';
   ```
3. 实现PrintExtensionAbility提供的接口。

   ```
   1. import { PrintExtensionAbility } from '@kit.BasicServicesKit';
   2. import { Want } from '@kit.AbilityKit';

   4. // 创建打印扩展能力类，继承PrintExtensionAbility，并实现打印扩展功能。
   5. export default class MyPrintExtension extends PrintExtensionAbility {
   6. // 系统首次连接打印扩展时调用。
   7. onCreate(want: Want): void {
   8. console.info('onCreate');
   9. // 初始化扩展能力，可以在此注册事件。
   10. }

   12. // 结束打印扩展时调用。
   13. onDestroy(): void {
   14. console.info('onDestroy');
   15. // 注销事件。
   16. }

   18. // 开始发现打印机时调用。
   19. onStartDiscoverPrinter(): void {
   20. console.info('onStartDiscoverPrinter enter');
   21. // 实现发现打印机的逻辑。
   22. }

   24. // 停止发现打印机时调用。
   25. onStopDiscoverPrinter(): void {
   26. console.info('onStopDiscoverPrinter enter');
   27. // 实现停止发现打印机的逻辑。
   28. }

   30. // 连接某台打印机时调用。
   31. onConnectPrinter(printerId: number): void {
   32. console.info('onConnectPrinter enter');
   33. // 实现连接打印机逻辑。可以通过打印机ID连接指定的打印机、查询打印机能力等。
   34. }

   36. // 断开与某台打印机的连接时调用。
   37. onDisconnectPrinter(printerId: number): void {
   38. console.info('onDisconnectPrinter enter');
   39. // 实现断开打印机连接逻辑。可以通过打印机ID断开与指定打印机的连接。
   40. }
   41. }
   ```
4. 在工程entry Module目录下的module.json5配置文件中(./entry/src/main/module.json5)注册PrintExtensionAbility并设置如下标签：

   * type标签设置为"print"；
   * srcEntry标签设置为当前ExtensionAbility组件所对应的代码路径。

     示例如下：

   ```
   1. {
   2. "module": {
   3. "extensionAbilities": [
   4. {
   5. "name": "MyPrintExtension",
   6. "srcEntry": "./ets/PrintExtensionAbility/MyPrintExtension.ets",
   7. "type": "print"
   8. }
   9. ]
   10. }
   11. }
   ```

### 功能验证

确认打印扩展能力PrintExtensionAbility中的回调方法实现是否正确、是否可以成功回调。在成功推送HAP包到设备后，可以在设置-打印机和扫描仪-添加打印机和扫描仪，拉起打印扩展能力，执行相应的动作触发回调时机后，通过查找对应接口实现中的日志(由开发者实现的业务逻辑决定)来判断是否成功回调。
