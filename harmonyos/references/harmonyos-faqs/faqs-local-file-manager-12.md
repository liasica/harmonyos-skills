---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-12
title: 怎么获取应用已使用的缓存大小，如何使用API清理缓存
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 怎么获取应用已使用的缓存大小，如何使用API清理缓存
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:574a974e489bc063f520fd667d8ca357d3fc47150bb8eeb94d4d0b45efc6154d
---

**解决措施**

获取应用已使用缓存大小可以通过[storageStatistics.getCurrentBundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgetcurrentbundlestats9)来获取。清理缓存需要调用context的cacheDir获取缓存，然后调用系统[@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md) 接口，判断是文件或者文件夹，再分别删除缓存。

如果需要删除整个应用的缓存，必须使用以下代码对所有模块级和应用级的Context进行操作。

**参考代码**

```ts
import { fileIo, storageStatistics } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct ClearCache {
  // Create a file in the cache
  writeFile() {
    let filePath = this.getUIContext().getHostContext()!.cacheDir + '/test.txt';
    let fileStream = fileIo.createStreamSync(filePath, 'w+');
    fileStream.writeSync('1145141919810');
    fileStream.close();
  }

  // Obtain the size of the application data space
  getCache() {
    storageStatistics.getCurrentBundleStats((error: BusinessError, bundleStats: storageStatistics.BundleStats) => {
      if (error) {
        console.error('getCurrentBundleStats failed with error:' + JSON.stringify(error));
      } else {
        console.info('getCurrentBundleStats successfully:' + JSON.stringify(bundleStats));
        console.info('appsize :' + bundleStats.appSize);
        console.info('cacheSize :' + bundleStats.cacheSize);
        console.info('dataSize :' + bundleStats.dataSize);
      }
    });
  }

  // Clear cache
  clearCache() {
    let cacheDir = this.getUIContext().getHostContext()!.cacheDir;
    console.info(cacheDir);

    fileIo.listFile(cacheDir).then((filenames) => {
      for (let i = 0; i < filenames.length; i++) {
        let dirPath = cacheDir + '/' + filenames[i];
        console.log(dirPath);
        // Determine whether it is a folder
        let isDirectory: boolean = false;
        try {
          isDirectory = fileIo.statSync(dirPath).isDirectory();
        } catch (e) {
          console.error(JSON.stringify(e));
        }

        if (isDirectory) {
          fileIo.rmdirSync(dirPath);
        } else {
          fileIo.unlink(dirPath).then(() => {
            console.info('remove file succeed');
          }).catch((err: Error) => {
            console.error('remove file failed with error message: ' + err.message);
          });
        }
      }

    })
  }

  build() {
    Column() {
      Button('Write data to cache')
        .onClick(() => {
          this.writeFile();
        })
      Button('Get the system cache size')
        .onClick(() => {
          this.getCache();
        })
      Button('Click to clear cache')
        .onClick(() => {
          this.clearCache();
        })
    }
  }
}
```
