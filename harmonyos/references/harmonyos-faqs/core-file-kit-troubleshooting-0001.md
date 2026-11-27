---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/core-file-kit-troubleshooting-0001
title: 应用缓存无法彻底清除问题排查与解决
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 故障排查 > 应用缓存无法彻底清除问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-11-27T10:51:08+08:00
doc_updated_at: 2026-11-26
content_hash: sha256:fa1fd33cd2ea44bbeed40873a535936b2eaceef57ccc351102668305458d9b05
---

## storageStatistics.getCurrentBundleStats接口获取清理后应用缓存的大小不为0

### 问题现象

调用context的cacheDir获取并清理缓存时，无法彻底清除，导致通过[storageStatistics.getCurrentBundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgetcurrentbundlestats9)接口获取清理后应用缓存的大小，依旧不为0。

### 定位过程

如果使用缓存清理接口后，调用缓存查询出的缓存数据依旧不为0，这表明清理的方法没有彻底清除缓存数据。实际上，应用的缓存文件保存在以下目录：

* /data/storage/${el1-el5}/base/cache；
* /data/storage/${el1-el5}/base/haps/${moduleName}/cache；

${el1-el5}指的是[el1，el2，el3，el4，el5目录](../harmonyos-guides/app-sandbox-directory.md#应用文件目录与应用文件路径)。${moduleName}是模块名。日常业务中，用户的缓存主要在el1，el2目录下，如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/_B41LG_sRzGGJlBbNYfArQ/zh-cn_image_0000002824354753.png?HW-CC-KV=V1&HW-CC-Date=20261127T025108Z&HW-CC-Expire=31536000000&HW-CC-Sign=B59C73D8A975A41CB0C0044017C21B4DDD46CE7DBFC5203DFFC2BD3F2CB96364 "点击放大")

实际情况还是以应用业务为准，应用可以通过[切换应用文件加密分区](../harmonyos-guides/application-context-stage.md#获取和修改加密分区)，获取所有的包含缓存文件的目录。

### 分析结论

由于缓存主要存在四个文件夹中，因此需要分别获取每个文件夹的路径，彻底删除每个文件夹下的缓存数据。

### 修改建议

1. 分别获取四个文件夹的路径，将缓存目录统计至paths数组中。代码示例如下：

   ```ts
   private paths: Array<string> = [];
     private moduleContext: common.Context | undefined = undefined;
     private context: Context | undefined = undefined;

     async aboutToAppear(): Promise<void> {
       this.context = this.getUIContext().getHostContext()!;
       this.moduleContext = await application.createModuleContext(this.context, 'entry');
       console.info(`moduleContext + el2: ${this.moduleContext.cacheDir}`); // data/storage/el2/base/cache
       console.info(`UIAbilityContext + el2: ${this.context.cacheDir}`); // data/storage/el2/base/haps/entry/cache
       this.paths.push(this.moduleContext.cacheDir);
       this.paths.push(this.context.cacheDir);
       this.moduleContext.area = contextConstant.AreaMode.EL1;
       console.info(`moduleContext + el1: ${this.moduleContext.cacheDir}`); // data/storage/el1/base/cache
       this.context.area = contextConstant.AreaMode.EL1;
       console.info(`UIAbilityContext + el1: ${this.context.cacheDir}`); // data/storage/el1/base/haps/entry/cache
       this.paths.push(this.moduleContext.cacheDir);
       this.paths.push(this.context.cacheDir);
     }
   ```
2. 遍历paths数组，彻底删除每个文件夹下的缓存数据。代码示例如下：

   ```ts
   Button('清除缓存').onClick(() => {
           for (let i = 0; i < this.paths.length; i++) {
             let path = this.paths[i];
             fileIo.listFile(path).then((filenames) => {
               for (let i = 0; i < filenames.length; i++) {
                 let dirPath = path + '/' + filenames[i];
                 console.info(dirPath);
                 // 判断是否为文件夹
                 let isDirectory: boolean = false;
                 try {
                   isDirectory = fileIo.statSync(dirPath).isDirectory();
                 } catch (err) {
                   console.error(`remove file failed with error message: ${err.message}`);
                 }

                 if (isDirectory) {
                   fileIo.rmdirSync(dirPath);
                 } else {
                   fileIo.unlink(dirPath).then(() => {
                     console.info('remove file succeed');
                   }).catch((err: Error) => {
                     console.error(`remove file failed with error message: ${err.message}`);
                   });
                 }
               }
             });
           }
         });
   ```

完整示例代码为：

```ts
import { application, common, contextConstant } from '@kit.AbilityKit';
import { fileIo, storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Component
@Entry
struct ClearCache {
  private paths: Array<string> = [];
  private moduleContext: common.Context | undefined = undefined;
  private context: Context | undefined = undefined;

  async aboutToAppear(): Promise<void> {
    this.context = this.getUIContext().getHostContext()!;
    this.moduleContext = await application.createModuleContext(this.context, 'entry');
    console.info(`moduleContext + el2: ${this.moduleContext.cacheDir}`); // data/storage/el2/base/cache
    console.info(`UIAbilityContext + el2: ${this.context.cacheDir}`); // data/storage/el2/base/haps/entry/cache
    this.paths.push(this.moduleContext.cacheDir);
    this.paths.push(this.context.cacheDir);
    this.moduleContext.area = contextConstant.AreaMode.EL1;
    console.info(`moduleContext + el1: ${this.moduleContext.cacheDir}`); // data/storage/el1/base/cache
    this.context.area = contextConstant.AreaMode.EL1;
    console.info(`UIAbilityContext + el1: ${this.context.cacheDir}`); // data/storage/el1/base/haps/entry/cache
    this.paths.push(this.moduleContext.cacheDir);
    this.paths.push(this.context.cacheDir);
  }

  build() {

    Column({ space: 10 }) {
      Button('清除缓存').onClick(() => {
        for (let i = 0; i < this.paths.length; i++) {
          let path = this.paths[i];
          fileIo.listFile(path).then((filenames) => {
            for (let i = 0; i < filenames.length; i++) {
              let dirPath = path + '/' + filenames[i];
              console.info(dirPath);
              // 判断是否为文件夹
              let isDirectory: boolean = false;
              try {
                isDirectory = fileIo.statSync(dirPath).isDirectory();
              } catch (err) {
                console.error(`remove file failed with error message: ${err.message}`);
              }

              if (isDirectory) {
                fileIo.rmdirSync(dirPath);
              } else {
                fileIo.unlink(dirPath).then(() => {
                  console.info('remove file succeed');
                }).catch((err: Error) => {
                  console.error(`remove file failed with error message: ${err.message}`);
                });
              }
            }
          });
        }
      });

      Button('获取应用缓存大小').onClick(() => {
        storageStatistics.getCurrentBundleStats().then((bundleStats: storageStatistics.BundleStats) => {
          console.info(`getCurrentBundleStats successfully:${JSON.stringify(bundleStats)}`);
          console.info(`appsize :${bundleStats.appSize}`);
          console.info(`cacheSize :${bundleStats.cacheSize}`);
          console.info(`dataSize :${bundleStats.dataSize}`);
        }).catch((err: BusinessError) => {
          console.error(`getCurrentBundleStats failed with error:${JSON.stringify(err)}`);
        });
      });

    }
    .width('100%')
    .height('100%');
  }
}
```

## 清理用户缓存后仍然显示有缓存数据存在

### 问题现象

用户在应用中点击清理缓存功能，应用执行清理缓存动作后，界面上仍然显示有缓存数据。多次执行后，显示缓存数据清零。

### 定位过程

根据HiLog日志进行分析：

1. 根据关键字storage\_manager在日志中进行检索，发现有以下信息：

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

### 分析结论

storageStatistics.getCurrentBundleStats为异步调用，当清理结束时，仍然有新的缓存数据正在产生。此时，再调用该接口仍然可以获取到缓存数据。

### 修改建议

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
