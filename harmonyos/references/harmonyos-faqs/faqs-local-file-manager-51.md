---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-51
title: 清理用户缓存后仍然显示有缓存数据存在
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 清理用户缓存后仍然显示有缓存数据存在
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:20688db3dae5dc3d2582b7d8270307476a0e448fc0f9f3d67d2d451780182db2
---

## 问题现象

用户在应用中点击清理缓存功能，应用执行清理缓存动作后，界面上仍然显示有缓存数据。多次执行后，显示缓存数据清零。

## 背景知识

* [应用文件概述](../harmonyos-guides/app-file-overview.md)：应用文件包括应用安装文件、应用资源文件和应用缓存文件，文件所有者是应用。
* [应用文件访问(ArkTS)](../harmonyos-guides/app-file-access.md)：应用需要对应用文件目录下的应用文件进行查看、创建、读写、删除、移动、复制、获取属性等访问操作。
* [应用及文件系统空间统计](../harmonyos-guides/app-fs-space-statistics.md)：在系统中，可能出现系统空间不够或者cacheDir等目录受系统配额限制等情况，需要应用开发者关注系统剩余空间，同时控制应用自身占用的空间大小。
* [storageStatistics.getCurrentBundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgetcurrentbundlestats9)：应用异步获取当前应用存储空间大小（单位为Byte），以Promise方式返回。
* [storageStatistics.getCurrentBundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgetcurrentbundlestats9-1)：应用异步获取当前应用存储空间大小（单位为Byte），以callback方式返回。
* [BundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#bundlestats9)：

  | 名称 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | appSize | number | 是 | 应用安装文件大小（单位为Byte）。 |
  | cacheSize | number | 是 | 应用缓存文件大小（单位为Byte）。 |
  | dataSize | number | 是 | 应用文件存储大小（除应用安装文件和缓存文件）（单位为Byte）。 |

## 问题定位

根据HiLog日志进行分析：

根据关键字storage\_manager在日志中进行检索，发现有以下信息：

```txt
07-04 11:01:25.512   639-656       C04300/storage...torageManager  storage_manager       E     [GetBundleStats:310] StorageStatusService::GetBundleStats success for pkgName=com.hm.example, userId=100, appIndex=0, appSize=46121544, cacheSize=35758401, dataSize=37560320
07-04 11:01:28.753   639-656       C04300/storage...torageManager  storage_manager       I     [GetCurrentBundleStats:271] StorageManager::GetCurrentBundleStats start
07-04 11:01:28.754   639-656       C01120/storage_manager/BMS      storage_manager       I     [bundle_mgr_proxy.cpp(GetBundleStats:3115)]begin com.hm.example
07-04 11:01:28.773   22461-22461   C04500/com.hua.exam.l/chromium  com.cnnb....i.huawei  I     [nodict][nweb_delegate.cc:455] DrapDrop InitAppTempDir --ohos-temp-dir=/data/storage/el2/base/haps/entry/temp
07-04 11:01:28.774   639-656       C01120/storage_manager/BMS      storage_manager       I     [bundle_mgr_proxy.cpp(GetBundleStats:3152)]end com.hm.example
07-04 11:01:28.774   639-656       C04300/storage...torageManager  storage_manager       E     [GetBundleStats:310] StorageStatusService::GetBundleStats success for pkgName=com.hm.example, userId=100, appIndex=0, appSize=46121544, cacheSize=1246634, dataSize=39616512
07-04 11:01:30.597   639-742       C04300/storage...torageManager  storage_manager       I     [GetSizeOfPath:117] StorageStatusService::GetSizeOfPath path is /data, type is total space, size is 499365445632.
07-04 11:01:30.597   639-742       C04300/storage...torageManager  storage_manager       I     [GetSizeOfPath:117] StorageStatusService::GetSizeOfPath path is /, type is total space, size is 3012784128.
07-04 11:01:30.597   639-742       C04300/storage...torageManager  storage_manager       E     [GetTotalSize:82] StorageTotalStatusService::GetTotalSize success, roundSize=512000000000, (/data)totalDataSize=499365445632, (/)totalRootSize=3012784128
07-04 11:01:30.598   639-742       C04300/storage...torageManager  storage_manager       I     [GetSizeOfPath:117] StorageStatusService::GetSizeOfPath path is /data, type is free space, size is 408922464256.
07-04 11:01:30.598   639-742       C04300/storage...torageManager  storage_manager       E     [GetFreeSize:94] StorageTotalStatusService::GetFreeSize success, (/data)freeSize=408922464256
```

以上日志信息可以看到，应用分别获取了两次GetBundleStats信息。分别对应当为用户进入清理页面时，应用第一次调用来查询当前应用的缓存数据。当用户点击清理后，应用第二次调用查询应用的缓存数据。而在第二次调用前，应用仍然有缓存数据在写入，因此这里可以看到缓存数据不为零。因此，在界面上就可以看到仍然有缓存数据。

## 分析结论

storageStatistics.getCurrentBundleStats为异步调用，当清理结束时，仍然有新的缓存数据正在产生。此时，再调用该接口仍然可以获取到缓存数据。

## 修改建议

* 在清理时调用getCurrentBundleStats接口获取缓存数据，用于展示。清理结束后，不用再调用该接口。
* 清理时，通过getCurrentBundleStats判断当前缓存是否为空，不为空时，继续执行。

清理缓存的示例代码：

```ts
import { fileIo, storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { application, common, contextConstant } from '@kit.AbilityKit';

@Entry
@Component
struct CacheStorageDemo {
  @State message: string = '点击开始清理应用缓存';
  @State cacheSize: number = 0;
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    // 获取应用缓存大小
    this.getCacheSize();
  }

  getCacheSize() {
    storageStatistics.getCurrentBundleStats().then((bundleStats: storageStatistics.BundleStats) => {
      console.info(`getCurrentBundleStats successfully:${JSON.stringify(bundleStats)}`);
      this.cacheSize = bundleStats.cacheSize;
    }).catch((err: BusinessError) => {
      console.error(`getCurrentBundleStats failed with error:${JSON.stringify(err)}`);
    });
  }

  build() {
    Column({ space: 20 }) {
      Text(`应用缓存大小：${this.cacheSize}B`)
      Button(this.message)
        .onClick(async () => {
          let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
          let paths: Array<string> = [];
          let moduleContext: common.Context;
          moduleContext = await application.createModuleContext(context, 'entry');
          // 缓存路径/data/storage/el2/base/cache
          paths.push(moduleContext.cacheDir);
          // 缓存路径/data/storage/el2/base/haps/entry/cache
          paths.push(context.cacheDir);
          // 缓存路径/data/storage/el1/base/cache
          moduleContext.area = contextConstant.AreaMode.EL1;
          paths.push(moduleContext.cacheDir);
          // 缓存路径/data/storage/el1/base/haps/entry/cache
          context.area = contextConstant.AreaMode.EL1;
          paths.push(context.cacheDir);
          // 遍历paths数组，彻底删除每个文件夹下的缓存数据
          for (let i = 0; i < paths.length; i++) {
            let path = paths[i];
            let filenames: string[] = [];
            try {
              filenames = fileIo.listFileSync(path);
            } catch (err) {
              console.error(`list file failed with error message: ${err.message}`);
            }
            for (let i = 0; i < filenames.length; i++) {
              let dirPath = path + '/' + filenames[i];
              console.info(dirPath);
              // 判断是否为文件夹
              let isDirectory: boolean = false;
              try {
                isDirectory = fileIo.statSync(dirPath).isDirectory();
              } catch (err) {
                console.error(`stat file failed with error message: ${err.message}`);
              }

              if (isDirectory) {
                fileIo.rmdir(dirPath).then(() => {
                  console.info('rmdir succeed');
                }).catch((err: Error) => {
                  console.error(`rmdir failed with error message: ${err.message}`);
                });
              } else {
                fileIo.unlink(dirPath).then(() => {
                  console.info('unlink file succeed');
                }).catch((err: Error) => {
                  console.error(`unlink file failed with error message: ${err.message}`);
                });
              }
            }
          }
          // 缓存清理完成后，切换到应用原本的加密分区，此处以EL2为例。
          if (moduleContext.area === contextConstant.AreaMode.EL1) {
            moduleContext.area = contextConstant.AreaMode.EL2;
          }
          this.message = '缓存清理完成';
          // 重新获取应用缓存大小
          this.getCacheSize();
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
