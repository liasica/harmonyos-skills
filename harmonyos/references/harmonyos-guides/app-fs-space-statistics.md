---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-fs-space-statistics
title: 应用及文件系统空间统计
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用文件访问与管理 > 应用及文件系统空间统计
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2a9651ace843ff5eb67654709b688cfaada72b929206bd87b63e3d96c0651f98
---

在系统中，可能出现系统空间不够或者cacheDir等目录受系统配额限制等情况，需要应用开发者关注系统剩余空间，同时控制应用自身占用的空间大小。

## 接口说明

API的详细介绍请参见[ohos.file.statvfs](../harmonyos-references/js-apis-file-statvfs.md)、[ohos.file.storageStatistics](../harmonyos-references/js-apis-file-storage-statistics.md)。

**表1** 文件系统空间和应用空间统计

| 模块 | 接口名 | 功能 |
| --- | --- | --- |
| @ohos.file.storageStatistics | getCurrentBundleStats | 获取当前应用的存储空间大小（单位为Byte）。 |
| @ohos.file.storageStatistics | getFreeSize | 异步获取内置存储的可用空间大小（单位为Byte）。  **说明**：从API version 15开始，支持该接口。 |
| @ohos.file.storageStatistics | getFreeSizeSync | 同步获取内置存储的可用空间大小（单位为Byte）。  **说明**：从API version 15开始，支持该接口。 |
| @ohos.file.storageStatistics | getTotalSize | 异步获取内置存储的总空间大小（单位为Byte）。  **说明**：从API version 15开始，支持该接口。 |
| @ohos.file.storageStatistics | getTotalSizeSync | 同步获取内置存储的总空间大小（单位为Byte）。  **说明**：从API version 15开始，支持该接口。 |
| @ohos.file.statvfs | getFreeSize | 获取指定文件系统的剩余空间大小（单位为Byte）。  **说明**：从API version 20开始，支持该接口。 |
| @ohos.file.statvfs | getTotalSize | 获取指定文件系统的总空间大小（单位为Byte）。  **说明**：从API version 20开始，支持该接口。 |

**表2** 应用空间统计

注意

表格中统计路径列涉及的目录均指应用的沙箱路径，查看路径前需要先进入对应的应用沙箱空间。进入沙箱空间需要执行以下命令：

1. hdc shell。
2. nsenter -t {pid} -m sh。

| BundleStats属性 | 含义 | 统计路径 |
| --- | --- | --- |
| appSize | 应用安装文件大小（单位为Byte） | 应用安装文件保存在以下目录：  /data/storage/el1/bundle |
| cacheSize | 应用缓存文件大小（单位为Byte） | 应用的缓存文件保存在以下目录：  /data/storage/${el1-el5}/base/cache  /data/storage/${el1-el5}/base/haps/${moduleName}/cache  **说明**：${el1-el5}指的是[el1，el2，el3，el4，el5目录](app-sandbox-directory.md#应用文件目录与应用文件路径)。${moduleName}是模块名。 |
| dataSize | 应用文件存储大小（除应用安装文件）（单位为Byte） | 应用文件通常由本地文件、分布式文件、数据库文件等部分组成。  本地文件保存在以下目录（注意缓存文件目录为以下目录的子目录）：  /data/storage/${el1-el5}/base  分布式文件保存在以下目录：  /data/storage/el2/distributedfiles  数据库文件保存在以下目录：  /data/storage/${el1-el5}/database  **说明**：${el1-el5}指的是[el1，el2，el3，el4，el5目录](app-sandbox-directory.md#应用文件目录与应用文件路径)。 |

## 开发示例

* 获取文件系统数据分区剩余空间大小。

  ```
  1. import { statfs } from '@kit.CoreFileKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { common } from '@kit.AbilityKit';
  ```

  ```
  1. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  2. let path = context.filesDir;
  3. statfs.getFreeSize(path, (err: BusinessError, number: number) => {
  4. if (err) {
  5. console.error(`Invoke getFreeSize failed, code is ${err.code}, message is ${err.message}`);
  6. } else {
  7. console.info(`Invoke getFreeSize succeeded, size is ${number}`);
  8. }
  9. });
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/AppFsSpcaeStatisticsSample/entry/src/main/ets/pages/Index.ets#L171-L181)
* 获取当前应用的存储空间大小。

  ```
  1. import { storageStatistics } from '@kit.CoreFileKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  ```

  ```
  1. storageStatistics.getCurrentBundleStats((err: BusinessError, bundleStats: storageStatistics.BundleStats) => {
  2. if (err) {
  3. console.error(`Invoke getCurrentBundleStats failed, code is ${err.code}, message is ${err.message}`);
  4. } else {
  5. console.info(`Invoke getCurrentBundleStats succeeded, appsize is ${bundleStats.appSize}`);
  6. }
  7. });
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/AppFsSpcaeStatisticsSample/entry/src/main/ets/pages/Index.ets#L152-L160)
* 异步获取内置存储的总空间大小。

  ```
  1. import { storageStatistics } from '@kit.CoreFileKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  ```

  ```
  1. storageStatistics.getTotalSize().then((number: number) => {
  2. console.info(`getTotalSize successfully, number is ${number}`);
  3. }).catch((err: BusinessError) => {
  4. console.error(`getTotalSize failed with error, code is ${err.code}, message is ${err.message}`);
  5. });
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/AppFsSpcaeStatisticsSample/entry/src/main/ets/pages/Index.ets#L191-L197)
* 同步获取内置存储的总空间大小。

  ```
  1. import { storageStatistics } from '@kit.CoreFileKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  ```

  ```
  1. try {
  2. let number = storageStatistics.getTotalSizeSync();
  3. console.info(`getTotalSizeSync successfully, number is ${number}`);
  4. } catch (err) {
  5. let error: BusinessError = err as BusinessError;
  6. console.error(`getTotalSizeSync failed with error, code is ${error.code}, message is ${error.message}`);
  7. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/AppFsSpcaeStatisticsSample/entry/src/main/ets/pages/Index.ets#L206-L214)
* 异步获取内置存储的可用空间大小。

  ```
  1. import { storageStatistics } from '@kit.CoreFileKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  ```

  ```
  1. storageStatistics.getFreeSize().then((number: number) => {
  2. console.info(`getFreeSize successfully, number is ${number}`);
  3. }).catch((err: BusinessError) => {
  4. console.error(`getFreeSize failed with error, code is ${err.code}, message is ${err.message}`);
  5. });
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/AppFsSpcaeStatisticsSample/entry/src/main/ets/pages/Index.ets#L220-L226)
* 同步获取内置存储的可用空间大小。

  ```
  1. import { storageStatistics } from '@kit.CoreFileKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';
  ```

  ```
  1. try {
  2. let number = storageStatistics.getFreeSizeSync();
  3. console.info(`getFreeSizeSync successfully, number is ${number}`);
  4. } catch (err) {
  5. let error: BusinessError = err as BusinessError;
  6. console.error(`getFreeSizeSync failed with error, code is ${error.code}, message is ${error.message}`);
  7. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/CoreFile/AppFsSpcaeStatisticsSample/entry/src/main/ets/pages/Index.ets#L235-L243)
