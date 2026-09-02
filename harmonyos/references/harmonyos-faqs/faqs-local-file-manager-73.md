---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-73
title: 关于系统设置中应用的存储大小
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 关于系统设置中应用的存储大小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:30+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ad91d252e3eed1dc839bbbbfcb5e67e436df136ac8253bb31dc6b7dd286a1f50
---

## 问题现象

系统设置-存储-应用大小页面如下，其中“应用”、“数据”、“缓存”这三个存储数据的值分别表示什么含义？开发者如何查询本应用的这三个存储数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/dVwpSYy3Rz6EgVyAfiS1XA/zh-cn_image_0000002629059028.png "点击放大")

## 解决方案

1. 系统设置-存储-应用大小页面中的“应用”、“数据”、“缓存”这三个存储数据分别对应[BundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#bundlestats9)中的appSize、dataSize、cacheSize。可以参考官网[应用及文件系统空间统计](../harmonyos-guides/app-fs-space-statistics.md)章节的表2应用空间统计。

   | 设置中的存储显示 | BundleStats属性 | 含义 | 统计路径 |
   | --- | --- | --- | --- |
   | 应用 | appSize | 应用安装文件大小（单位为Byte） | 应用安装文件保存在以下目录：/data/storage/el1/bundle |
   | 缓存 | cacheSize | 应用缓存文件大小（单位为Byte） | 应用的缓存文件保存在以下目录：  /data/storage/${el1-el5}/base/cache  /data/storage/${el1-el5}/base/haps/${moduleName}/cache  说明：${el1-el5}指的是[el1，el2，el3，el4，el5目录](../harmonyos-guides/app-sandbox-directory.md#应用文件目录与应用文件路径)。${moduleName}是模块名。 |
   | 数据 | dataSize | 应用文件存储大小（除应用安装文件）（单位为Byte） | 应用文件通常由本地文件、分布式文件、数据库文件等部分组成。  本地文件保存在以下目录（注意缓存文件目录为以下目录的子目录）：  /data/storage/${el1-el5}/base  分布式文件保存在以下目录：  /data/storage/el2/distributedfiles  数据库文件保存在以下目录：  /data/storage/${el1-el5}/database  说明：${el1-el5}指的是[el1，el2，el3，el4，el5目录](../harmonyos-guides/app-sandbox-directory.md#应用文件目录与应用文件路径)。 |
2. 开发者可以通过[storageStatistics.getCurrentBundleStats](../harmonyos-references/js-apis-file-storage-statistics.md#storagestatisticsgetcurrentbundlestats9)查询本应用的“应用”、“数据”、“缓存”这三个存储数据。示例代码如下：

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { storageStatistics } from '@kit.CoreFileKit';

   @Entry
   @Component
   struct QueryAppStorageSize {
     @State appSize: number = 0;
     @State cacheSize: number = 0;
     @State dataSize: number = 0;
     @State totalSize: number = 0;

     aboutToAppear(): void {
       this.getCurrentBundleStats();
     }

     getCurrentBundleStats() {
       storageStatistics.getCurrentBundleStats((err: BusinessError, bundleStats: storageStatistics.BundleStats) => {
         if (err) {
           console.error(`Invoke getCurrentBundleStats failed, code is ${err.code}, message is ${err.message}`);
         } else {
           console.info(`Invoke getCurrentBundleStats succeeded`);
           this.appSize = bundleStats.appSize; // 应用安装文件大小
           this.cacheSize = bundleStats.cacheSize; // 应用缓存文件大小
           this.dataSize = bundleStats.dataSize; // 应用文件存储大小（除应用安装文件）
           this.totalSize = this.appSize + this.dataSize;
         }
       });
     }

     build() {
       Column({ space: 20 }) {
         Text(`应用安装文件大小：${this.appSize} Byte`);
         Text(`应用缓存文件大小：${this.cacheSize} Byte`);
         Text(`应用文件存储大小（除应用安装文件）：${this.dataSize} Byte`);
         Text(`应用总计大小：${this.totalSize} Byte`);
       }
       .width('100%')
       .alignItems(HorizontalAlign.Center);
     }
   }
   ```

   运行效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/p-gWDW93ToGQqugQgAQpQw/zh-cn_image_0000002659258331.png "点击放大")
3. 如果需要继续查询对应存储空间下的文件信息，可以参考[获取文件大小和文件类型](faqs-local-file-manager-63.md)。
