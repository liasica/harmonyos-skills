---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-78
title: 如何解决应用缓存无法彻底清除问题
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 如何解决应用缓存无法彻底清除问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:104bdada6207a146256639adeb035f562876c9e6ab52c7a81976ff3881508b53
---

## 问题现象

调用context的cacheDir获取并清理缓存时，无法彻底清除，导致通过[storageStatistics.getCurrentBundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgetcurrentbundlestats9)接口获取清理后应用缓存的大小，依旧不为0。

## 背景知识

应用缓存是指应用程序在运行过程中产生的临时数据，如照片、视频、文档等。这些缓存数据可以加快应用程序的响应速度，并提供离线使用的功能。但是当应用缓存的数据过多，会导致应用占用较大的内存空间。[@ohos.file.storageStatistics (应用空间统计)模块](../harmonyos-references/js-apis-file-storage-statistics.md)提供空间查询相关的常用功能：包括对内外卡的空间查询、对应用分类数据统计的查询、对应用数据的查询等。

## 问题定位

如果使用缓存清理接口后，调用缓存查询出的缓存数据依旧不为0，这表明清理的方法没有彻底清除缓存数据。实际上，应用的缓存文件保存在以下目录：

* /data/storage/${el1-el5}/base/cache。
* /data/storage/${el1-el5}/base/haps/${moduleName}/cache。

${el1-el5}指的是[el1，el2，el3，el4，el5目录](../harmonyos-guides/app-sandbox-directory.md#应用文件目录与应用文件路径)。${moduleName}是模块名。日常业务中，用户的缓存主要在el1，el2目录下，如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Z2aPN8LKRcm7BXL2v5-qRA/zh-cn_image_0000002628899112.png "点击放大")

实际情况还是以应用业务为准，应用可以通过[切换应用文件加密分区](../harmonyos-guides/application-context-stage.md#获取和修改加密分区)，获取所有的包含缓存文件的目录。

## 分析结论

由于缓存主要存在四个文件夹中，因此需要分别获取每个文件夹的路径，彻底删除每个文件夹下的缓存数据。

## 修改建议

1. 分别获取四个文件夹的路径，将缓存目录统计至paths数组中。

   ```screen
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
2. 遍历paths数组，彻底删除每个文件夹下的缓存数据。

   ```screen
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

完整示例参考如下：

```screen
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

## 常见FAQ

Q：ArkTS如何获取应用缓存大小？

A：[@ohos.file.storageStatistics](../harmonyos-references/js-apis-file-storage-statistics.md)提供了应用空间统计能力，可使用[storageStatistics.getCurrentBundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgetcurrentbundlestats9)获取应用缓存大小。

Q：应用的缓存数据哪些放在el1下，哪些放在el2下？

A：el1和el2的密级不同，建议应用根据所要缓存数据的密级选择。

* el1（设备级加密区）：设备开机后可访问的数据区。
* el2（用户级加密区）：设备开机后，需解锁对应用户的锁屏界面（密码、指纹、人脸等方式或无密码状态）至少一次，才能访问的数据区。应用若无特殊需求，应将数据存放在el2加密目录下，以保障数据安全。对于需要在用户解锁前访问的文件，如时钟、闹铃、壁纸等，应将这些文件存放在el1下。

Q：如何获取应用打包后体积大小？

A：[storageStatistics.getCurrentBundleStats()](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgetcurrentbundlestats9)接口提供了获取当前应用存储空间大小的能力，其中返回值appSize字段可以获取到应用安装文件大小（单位为Byte）。

Q：如何快速清理应用的缓存？

A：从API version 21开始，推出[bundleManager.cleanBundleCacheFilesForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagercleanbundlecachefilesforself21)接口，用于清理应用自身的缓存。

Q：如何快速清理当前应用的应用文件路径下的所有数据？

A：可以使用[ApplicationContext.clearUpApplicationData](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextclearupapplicationdata11)清理当前应用的应用文件路径下的所有数据，同时撤销应用向用户申请的权限。但是仅支持主线程调用，并且该接口会停止应用进程，应用进程停止后，后续的所有回调都不会再触发。

## 总结

在清理缓存时，需要根据使用场景来决定删除缓存要到什么程度，由应用自己本身控制。常见缓存会存在data/storage/el1/base/cache、data/storage/el1/base/haps/entry/cache、data/storage/el2/base/cache、data/storage/el2/base/haps/entry/cache四个目录下面，当需要彻底删除时，需要遍历每一个目录进行删除。
