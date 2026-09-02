---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-cloud-sync-filesync
title: 端云文件协同适配指导
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 端云文件协同 > 端云文件协同适配指导
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:24+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:a702ff58c74ecc3b842bce6f2bf8e5eb69ad8e3df6528a6ace7f3efcc88282ef
---

为方便开发者使用端云文件协同的文件缓存、同步等能力，此篇指南介绍了环境准备、文件同步和文件缓存，并且在指南的最后提供了完整的应用工程示例。

## 文件同步

开发者可以使用基本的[文件操作接口](app-file-access.md)，在沙箱路径/data/storage/el2/cloud下进行文件的读写、重命名、拷贝、创建目录等操作，在文件完成写入或文件夹创建成功后，端云协同服务会自动触发同步流程，将新建的文件或文件夹同步上云。

针对一些设备的网络异常、温度过高、电量过低异常场景，受功耗管控，端云协同服务**无法及时**将文件修改同步到云服务器，此时开发者可以通过cloudSync.FileSync对象来订阅同步状态，并根据状态完成对同步的管理。

同时开发者可以在另外一部设备的沙箱路径/data/storage/el2/cloud下，查看到新增的文件或已有文件的修改，另外一部设备主要用于验证多端同步功能。

### 环境准备

* 调试设备：两部鸿蒙设备，系统版本在HarmonyOS 6.0.0.115及以上，云空间版本在6.0.0.300及以上。
* 开发环境：受云空间版本限制，IDE为DevEco Studio 6.0.1 Release或更新版本，构建版本为6.0.1.251，SDK 版本为 API Version 21 Release及以上。
* 配置应用：在项目路径AppScope/app.json5中添加cloudFileSyncEnabled字段为true。

  ```json
  {
    "app": {
      "cloudFileSyncEnabled": true
    }
  }
  ```
* 安装应用：两部设备应用安装后，登录账号，在设置->云空间中找到开发应用同步开关，如下图中的端云协同demo，打开同步开关，可以借助IDE的[Device File Browser](ide-device-file-explorer.md)浏览/data/storage/el2/cloud目录。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/E23A9aMSTiC2SspDvv7usA/zh-cn_image_0000002706834132.png)

### 接口说明

| 接口名 | 描述 | 注意事项 |
| --- | --- | --- |
| [FileSync.on(event: 'progress', callback: Callback<SyncProgress>): void](../harmonyos-references/js-apis-file-cloudsync.md#onprogress12) | 云盘同步对象添加同步过程事件监听 | 添加监听的对象和触发同步的对象不要混用 |
| [FileSync.off(event: 'progress', callback?: Callback<SyncProgress>): void](../harmonyos-references/js-apis-file-cloudsync.md#offprogress12) | 云盘同步对象移除'progress'类型的指定callback回调 | 移除事件监听前，保证要先添加事件监听 |
| [FileSync.start(): Promise<void>](../harmonyos-references/js-apis-file-cloudsync.md#start12) | 异步方法启动云盘端云同步 | 添加监听的对象和触发同步的对象保持一致。  **使用约束**：该异步接口仅支持有限并发，调用频率过高会导致整机异常。 |
| [FileSync.stop(): Promise<void>](../harmonyos-references/js-apis-file-cloudsync.md#stop12) | 异步方法停止云盘端云同步 | 移除监听的对象和停止同步的对象保持一致 |

### 示例代码

```typescript
// Index.ets
import { cloudSync } from '@kit.CoreFileKit';

@Entry
@Component
struct Index {
  @State errorCode: number = 0;
  @State errorMessage: string = "";
  // 记录此次同步流程的状态，枚举值参考接口说明
  @State state: cloudSync.SyncState = cloudSync.SyncState.STOPPED;
  // 记录同步流程终止时的错误信息，包含温度、电量、网络等错误状态
  @State errCode: cloudSync.ErrorType = cloudSync.ErrorType.NO_ERROR;
  // 声明一个FileSync类的对象
  private fileSync = new cloudSync.FileSync();
  // 声明一个事件监听函数，用于获取同步状态和同步错误码
  private cloudSyncCallback = (pg: cloudSync.SyncProgress) => {
    this.state = pg.state;
    this.errCode = pg.error;
  }

  build() {
    Column({space: 20}) {
      // 为FileSync对象添加事件监听，连续点击会捕获异常
      Button("注册监听").onClick(() => {
        try {
            this.fileSync.on("progress", this.cloudSyncCallback);
        } catch (error) {
            console.error("注册监听失败: ", error);
            this.errorCode = error.code;
            this.errorMessage = error.message;
        }
      });
      // 通过FileSync对象主动触发同步，当端侧和云侧数据不一致时，同步流程会将云上修改同步至端侧，本地修改同步至云上
      Button("触发同步").onClick(() => {
        try {
            this.fileSync.start();
        } catch (error) {
            console.error("触发同步失败: ", error);
            this.errorCode = error.code;
            this.errorMessage = error.message;
        }
      });
      // 通过FileSync对象主动停止同步，端侧不想与云侧保持同步时，停止同步流程可以停止与云上同步
      Button("停止同步").onClick(() => {
        try {
            this.fileSync.stop();
        } catch (error) {
            console.error("停止同步失败: ", error);
            this.errorCode = error.code;
            this.errorMessage = error.message;
        }
      })
      // 将同步事件监听移除，移除后，同步状态发生变化，应用将无法感知同步状态以及同步错误码
      Button("解除监听").onClick(() => {
        try {
            this.fileSync.off("progress");
        } catch (error) {
            console.error("解注册监听: ", error);
            this.errorCode = error.code;
            this.errorMessage = error.message;
        }
      });
      // 用于展示当前同步状态和同步错误码，当网络异常时，错误码为 NETWORK_UNAVAILABLE=1
      Text(`同步状态：${this.state}`).fontSize(12)
      Text(`错误码：${this.errCode}`).fontSize(12)
    }
    .width("100%")
    .height("100%")
  }
}
```

## 文件缓存

开发者将/data/storage/el2/cloud目录下的文件上云后，可以选择将本地空间占用释放，同时也可以缓存云上的文件到本地。调用[fileIo.statSync](../harmonyos-references/js-apis-fileio.md#fileiostatsync)方法可以获取文件的Location信息，根据文件的Location信息，可以有三种状态，分别对应：local=1, cloud=2, local&cloud=3，其中本地新建的文件上云成功后Location为3，此时用户的数据本地一份，云上一份，会同时占用本地空间和云上空间；未上云的文件Location为1，此时用户的数据只有本地一份，只占用本地空间；云上新增的文件，元数据下行到本地时，Location为2，此时用户本地只有元数据信息，文件本身在云上，只占用云上空间。开发者可以通过CloudFileCache对象提供的缓存和释放缓存接口，将Location在2和3之间转换，将本地占用的空间释放或将云上的数据缓存到本地。

### 环境准备

* 调试设备：两部鸿蒙设备，系统版本在HarmonyOS 6.0.0.115及以上，云空间版本在6.0.0.300及以上。
* 开发环境：受云空间版本限制，IDE为DevEco Studio 6.0.1 Release或更新版本，构建版本为6.0.1.251，SDK 版本为 API Version 21 Release及以上。
* 配置应用：在项目路径AppScope/app.json5中添加cloudFileSyncEnabled字段为true。

  ```json
  {
    "app": {
      "cloudFileSyncEnabled": true
    }
  }
  ```
* 安装应用：两部设备应用安装后，登录账号，在设置->云空间中找到开发应用同步开关（见文件同步开发场景中图片），打开同步开关，可以借助IDE的[Device File Browser](ide-device-file-explorer.md)浏览/data/storage/el2/cloud目录。

### 接口说明

| 接口名 | 描述 | 注意事项 |
| --- | --- | --- |
| [CloudFileCache.on(event: 'progress', callback: Callback<DownloadProgress>): void](../harmonyos-references/js-apis-file-cloudsync.md#onprogress11) | 添加云盘文件缓存过程事件监听 | 添加监听的对象和触发缓存的对象不要混用 |
| [CloudFileCache.off(event: 'progress', callback?: Callback<DownloadProgress>): void](../harmonyos-references/js-apis-file-cloudsync.md#offprogress11) | 云盘文件缓存对象移除'progress'类型的指定callback回调 | 移除事件监听前，保证要先添加事件监听 |
| [CloudFileCache.start(uri: string): Promise<void>](../harmonyos-references/js-apis-file-cloudsync.md#start11) | 异步方法启动云盘文件缓存 | 添加监听的对象和触发缓存的对象保持一致。  **使用约束**：该异步接口仅支持有限并发，最大并发数不超过10，调用超过此限制会导致整机异常。如果云盘文件缓存数超过10，建议使用批量下载接口[startbatch](../harmonyos-references/js-apis-file-cloudsync.md#startbatch20) |
| [CloudFileCache.stop(uri: string, needClean?: boolean): Promise<void>](../harmonyos-references/js-apis-file-cloudsync.md#stop11) | 异步方法停止云盘文件缓存 | 移除监听的对象和停止缓存的对象保持一致 |
| [CloudFileCache.cleanFileCache(uri: string): void](../harmonyos-references/js-apis-file-cloudsync.md#cleanfilecache20) | 同步方法删除文件缓存 | 不允许对正在上传的文件进行释放缓存 |

### 示例代码

```typescript
// Index.ets
import { cloudSync, fileIo, fileUri } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State currFilePath: string = "";
  @State errorCode: number = 0;
  @State errorMessage: string = "";
  // 用于记录缓存过程中，单个文件已缓存的大小
  @State process: number = 0;
  // 用于记录缓存过程中遇到的错误码，参考接口说明
  @State downloadErr: cloudSync.DownloadErrorType = cloudSync.DownloadErrorType.NO_ERROR;
  private context = getContext(this) as common.UIAbilityContext;
  // 获取当前应用的 /data/storage/el2/cloud 沙箱路径
  private basePath = this.context.cloudFileDir + "/";
  // 声明一个 CloudFileCache 的对象
  private cloudFileCache = new cloudSync.CloudFileCache();
  // 声明一个缓存过程监听函数，用于监听当前文件的缓存进度
  private downloadProcess = (pg: cloudSync.DownloadProgress) => {
    this.process = pg.processed;
    this.downloadErr = pg.error;
  }

  build() {
    Column({space: 20}) {
      // 添加文件缓存过程的事件监听
      Button("注册监听").onClick(() => {
        try {
            this.cloudFileCache.on("progress", this.downloadProcess);
        } catch (error) {
            console.error("缓存过程注册监听失败: ", error);
            this.errorCode = error.code;
            this.errorMessage = error.message;
        }
      });
      // 当本地只有文件元数据信息，文件实体资源在云上时，文件Location信息为2，此时可通过缓存文件将文件实体从云上缓存至本地
      Button("缓存文件").onClick(() => {
        try {
            let uri = fileUri.getUriFromPath(this.basePath + this.currFilePath);
            let fileStat = fileIo.statSync(this.basePath + this.currFilePath);
            console.info("文件Location信息：", fileStat.location);
            this.cloudFileCache.start(uri);
        } catch (error) {
            console.error("文件缓存失败: ", error);
            this.errorCode = error.code;
            this.errorMessage = error.message;
        }
      });
      // 当文件实体资源在云上和本地都存在时，文件Location信息为3，此时可通过释放缓存将本地占用的空间释放
      Button("释放缓存").onClick(() => {
        try {
            let uri = fileUri.getUriFromPath(this.basePath + this.currFilePath);
            let fileStat = fileIo.statSync(this.basePath + this.currFilePath);
            console.info("文件Location信息：", fileStat.location);
            this.cloudFileCache.cleanFileCache(uri);
        } catch (error) {
            console.error("释放文件缓存失败: ", error);
            this.errorCode = error.code;
            this.errorMessage = error.message;
        }
      });
      // 对缓存进度监听进行解除注册
      Button("解除监听").onClick(() => {
        try {
            this.cloudFileCache.off("progress");
        } catch (error) {
            console.error("解除缓存进度回调失败: ", error);
            this.errorCode = error.code;
            this.errorMessage = error.message;
        }
      });
      Text(`缓存进度：${this.process}`).fontSize(12)
      Text(`错误码：${this.downloadErr}`).fontSize(12)
    }
    .width("100%")
    .height("100%")
  }
}
```

## 文件属性同步

开发者可以设置沙箱内（/data/storage/el2/cloud）文件或目录的自定义扩展属性，设置后该自定义扩展属性可以跟随文件自动上云并同步至多端。

### 环境准备

* 调试设备：两部鸿蒙设备，系统版本在HarmonyOS 6.0.0.115及以上，云空间版本在6.0.0.300及以上。
* 开发环境：受云空间版本限制，IDE为DevEco Studio 6.0.1 Release或更新版本，构建版本为6.0.1.251，SDK 版本为 API Version 21 Release及以上。
* 配置应用：在项目路径AppScope/app.json5中添加cloudFileSyncEnabled字段为true。

  ```json
  {
    "app": {
      "cloudFileSyncEnabled": true
    }
  }
  ```
* 安装应用：两部设备应用安装后，登录账号，在设置->云空间中找到开发应用同步开关（见文件同步开发场景中图片），打开同步开关，可以借助IDE的[Device File Browser](ide-device-file-explorer.md)浏览/data/storage/el2/cloud目录。

### 接口说明

| 接口名 | 描述 | 注意事项 |
| --- | --- | --- |
| [setxattrSync(path: string, key: string, value: string): void](../harmonyos-references/js-apis-file-fs.md#fileiosetxattrsync12) | 设置文件或目录的扩展属性 | path为沙箱内文件或目录，沙箱根路径：/data/storage/el2/cloud，key需要以user.开头，且长度需小于256字节 |
| [getxattrSync(path: string, key: string): string](../harmonyos-references/js-apis-file-fs.md#fileiogetxattrsync12) | 获取文件或目录的扩展属性 | path为沙箱内文件或目录，沙箱根路径：/data/storage/el2/cloud，key需要以user.开头，且长度需小于256字节 |

### 示例代码

```typescript
// Index.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { cloudSync, fileIo, fileUri } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @State fileName: string = "";
  @State attrKey: string = "";
  @State attrVal: string = "";
  private context = getContext(this) as common.UIAbilityContext;
  private basePath = this.context.cloudFileDir + "/";

  build() {
    Column({space: 20}) {
      // 用来展示当前选中的文件路径
      Text(`当前选中的文本路径：${this.basePath + this.fileName}`)
        .fontSize(16).fontWeight(500).margin({top: 10})

      // 文本输入框，用来选中当前文件
      TextInput({
        placeholder: "请输入文件名",
        text: this.fileName
      }).onChange((value: string) => {
        this.fileName = value
      }).width("80%").height(50).backgroundColor("#f0f0f0").borderRadius(10).margin({top: 20})

      // 文本输入框，用来输入当前文件的自定义标签key
      TextInput({
        placeholder: "请输入自定义标签key",
        text: this.attrKey
      }).onChange((value: string) => {
        this.attrKey = value
      }).width("80%").height(50).backgroundColor("#f0f0f0").borderRadius(10).margin({top: 20})

      // 文本输入框，用来输入/输出当前文件的自定义标签value
      TextInput({
        placeholder: "设置时，此处需要输入对应的value。获取时，此处用来展示获取到的value",
        text: this.attrVal
      }).onChange((value: string) => {
        this.attrVal = value
      }).width("80%").height(50).backgroundColor("#f0f0f0").borderRadius(10).margin({top: 20})

      // 设置自定义标签
      Button("设置自定义标签").onClick(() => {
        try {
          fileIo.setxattrSync(this.basePath + this.fileName, this.attrKey, this.attrVal);
          console.info("Set extended attribute successfully.");
        } catch (err) {
          console.error(`Failed to set extended attribute. Code: ${err.code}, message: ${err.message}`);
        }
      });

      // 获取自定义标签
      Button("获取自定义标签").onClick(() => {
        this.attrVal = "";
        try {
          let attrValue = fileIo.getxattrSync(this.basePath + this.fileName, this.attrKey);
          this.attrVal = attrValue;
          console.info("Get extended attribute succeed, the value is: " + attrValue);
        } catch (err) {
          console.error(`Failed to get extended attribute. Code: ${err.code}, message: ${err.message}`);
        }
      });
    }
  }
}
```

## 文件缓存大小查询与清理

接入云盘的应用在大量缓存文件后，单个文件选中清理的操作效率较低，需支持缓存总大小查询和一键批量释放缓存，提高清理易操作性。

支持接入云盘的应用查询已缓存文件总大小（包含本地新增未上云文件、本地新增已上云文件及已下载文件大小），并执行一键清理（未上云文件、写打开文件不会被删除），批量释放本地存储空间。

### 环境准备

* 开发环境：SDK版本为API版本26.0.0 Release及以上。

### 接口说明

| 接口名 | 描述 |
| --- | --- |
| [constructor()](../harmonyos-references/js-apis-file-cloudsync.md#constructor11) | 构造函数 |
| [getCachedTotalSize(): Promise<number>](../harmonyos-references/js-apis-file-cloudsync.md#getcachedtotalsize) | 获取已缓存文件的总大小 |
| [cleanAllFileCache(): Promise<void>](../harmonyos-references/js-apis-file-cloudsync.md#cleanallfilecache) | 删除所有已缓存文件 |

### 示例代码

```typescript
// Index.ets
import { cloudSync } from '@kit.CoreFileKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = 'CloudFileCacheDemo';
@Entry
@Component
struct Index {
  // 用于显示接口调用的返回结果
  @State resultText: string = '';
  // 用于显示详细的日志输出信息
  @State logText: string = '';
  // 声明一个 CloudFileCache 对象，用于管理云文件缓存
  private cloudFileCache: cloudSync.CloudFileCache | null = null;
  aboutToAppear() {
    try {
      // 创建 CloudFileCache 实例
      this.cloudFileCache = new cloudSync.CloudFileCache();
      this.logText += '[INFO] CloudFileCache created\n';
      hilog.info(DOMAIN, TAG, 'CloudFileCache created successfully');
    } catch (err) {
      let errMsg = `Failed to create CloudFileCache: ${JSON.stringify(err)}`;
      this.logText += `[ERROR] ${errMsg}\n`;
      hilog.error(DOMAIN, TAG, errMsg);
    }
  }

  // 获取当前云文件缓存的总大小
  async getCachedTotalSize() {
    this.resultText = 'Calling getCachedTotalSize...';
    this.logText += '[INFO] Calling getCachedTotalSize()\n';
    hilog.info(DOMAIN, TAG, 'Calling getCachedTotalSize()');
    try {
      // 调用 getCachedTotalSize 接口获取缓存文件总大小
      let size: number = await this.cloudFileCache!.getCachedTotalSize();
      let result = `getCachedTotalSize result: ${size} bytes`;
      this.resultText = result;
      this.logText += `[INFO] ${result}\n`;
      hilog.info(DOMAIN, TAG, result);
    } catch (err) {
      let errMsg = `getCachedTotalSize failed: ${JSON.stringify(err)}`;
      this.resultText = errMsg;
      this.logText += `[ERROR] ${errMsg}\n`;
      hilog.error(DOMAIN, TAG, errMsg);
    }
  }

  // 清理当前应用所有的云文件缓存，释放本地存储空间
  async cleanAllFileCache() {
    this.resultText = 'Calling cleanAllFileCache...';
    this.logText += '[INFO] Calling cleanAllFileCache()\n';
    hilog.info(DOMAIN, TAG, 'Calling cleanAllFileCache()');
    try {
      // 调用 cleanAllFileCache 接口清理所有缓存文件
      await this.cloudFileCache!.cleanAllFileCache();
      let result = 'cleanAllFileCache succeeded';
      this.resultText = result;
      this.logText += `[INFO] ${result}\n`;
      hilog.info(DOMAIN, TAG, result);
    } catch (err) {
      let errMsg = `cleanAllFileCache failed: ${JSON.stringify(err)}`;
      this.resultText = errMsg;
      this.logText += `[ERROR] ${errMsg}\n`;
      hilog.error(DOMAIN, TAG, errMsg);
    }
  }
  build() {
    Column() {
      Text('CloudFileCache Demo')
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
        .margin({ top: 30, bottom: 20 })
      Row() {
        Button('getCachedTotalSize')
          .width(180)
          .height(50)
          .fontSize(16)
          // 按钮在 CloudFileCache 实例创建完成之前不可用
          .enabled(this.cloudFileCache !== null)
          .onClick(() => {
            this.getCachedTotalSize();
          })
        Button('cleanAllFileCache')
          .width(180)
          .height(50)
          .fontSize(16)
          .margin({ left: 20 })
          .enabled(this.cloudFileCache !== null)
          .onClick(() => {
            this.cleanAllFileCache();
          })
      }
      .margin({ bottom: 20 })
      Text('接口返回:')
        .fontSize(16)
        .fontWeight(FontWeight.Medium)
        .width('90%')
        .margin({ bottom: 5 })
      Scroll() {
        Text(this.resultText)
          .fontSize(14)
          .width('100%')
          .padding(10)
          .backgroundColor('#F0F0F0')
          .borderRadius(8)
      }
      .width('90%')
      .height(120)
      .margin({ bottom: 15 })
      Text('日志输出:')
        .fontSize(16)
        .fontWeight(FontWeight.Medium)
        .width('90%')
        .margin({ bottom: 5 })
      Scroll() {
        Text(this.logText)
          .fontSize(12)
          .width('100%')
          .padding(10)
          .backgroundColor('#F5F5DC')
          .borderRadius(8)
      }
      .width('90%')
      .height(200)
    }
    .width('100%')
    .height('100%')
    .alignItems(HorizontalAlign.Center)
  }
}
```

## 端云协同应用

为便于开发者快速熟悉接口功能，特提供一套涵盖文件缓存、同步及基本文件操作的示例应用代码。该示例支持在两台调试设备间协同工作：设备 A 可创建和编辑文件，设备 B 则可缓存初始文件并在 A 端修改后自动同步更新。[端云文件协同示例链接](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/CoreFile/AppCloudSync)
