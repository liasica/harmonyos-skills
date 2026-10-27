---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/core-file-kit-troubleshooting-0001
title: 应用缓存无法彻底清除问题排查与解决
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 故障排查 > 应用缓存无法彻底清除问题排查与解决
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:00+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:0f9a7df757aa317e0db358bb0abd3bc55b5dc4dcac924833405118ebd11a3c62
---

## 问题现象

调用context的cacheDir获取并清理缓存时，无法彻底清除，导致通过[storageStatistics.getCurrentBundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgetcurrentbundlestats9)接口获取清理后应用缓存的大小，依旧不为0。

## 定位过程

如果使用缓存清理接口后，调用缓存查询出的缓存数据依旧不为0，这表明清理的方法没有彻底清除缓存数据。实际上，应用的缓存文件保存在以下目录：

* /data/storage/${el1-el5}/base/cache；
* /data/storage/${el1-el5}/base/haps/${moduleName}/cache；

${el1-el5}指的是[el1，el2，el3，el4，el5目录](../harmonyos-guides/app-sandbox-directory.md#应用文件目录与应用文件路径)。${moduleName}是模块名。日常业务中，用户的缓存主要在el1，el2目录下，如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/6UdoKJHGRDed_F1-bmsBNA/zh-cn_image_0000002802039489.png "点击放大")

实际情况还是以应用业务为准，应用可以通过[切换应用文件加密分区](../harmonyos-guides/application-context-stage.md#获取和修改加密分区)，获取所有的包含缓存文件的目录。

## 分析结论

由于缓存主要存在四个文件夹中，因此需要分别获取每个文件夹的路径，彻底删除每个文件夹下的缓存数据。

## 修改建议

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
