---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-mediaassetprogresshandler
title: Interface (MediaAssetProgressHandler)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS API > @ohos.file.photoAccessHelper (相册管理模块) > Interface (MediaAssetProgressHandler)
category: harmonyos-references
scraped_at: 2026-10-27T07:43:25+08:00
doc_updated_at: 2026-10-26
content_hash: sha256:342c7d4ce71487dbf47692aab6e16218e99569f39cfa996c72a5f053a8554de5
---

媒体资产进度处理器，用于接收媒体资产处理进度的回调。

**说明** 

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Interface首批接口从API version 15开始支持。

## 导入模块

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

## onProgress15+

onProgress(progress: number): void

当所请求的媒体资产返回进度时系统会回调此方法。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progress | number | 是 | 传入的进度百分比，范围为[0, 100]。 |

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { dataSharePredicates } from '@kit.ArkData';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function requestVideoWithProgress(
  phAccessHelper: photoAccessHelper.PhotoAccessHelper,
  context: common.Context
) {
  let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> | null = null;
  try {
    // 查询一个视频资源。
    const predicates = new dataSharePredicates.DataSharePredicates();
    predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_TYPE, photoAccessHelper.PhotoType.VIDEO);
    predicates.limit(1, 0);

    const fetchOptions: photoAccessHelper.FetchOptions = {
      fetchColumns: ['title', 'size', 'subtype'],
      predicates: predicates,
    };

    fetchResult = await phAccessHelper.getAssets(fetchOptions);
    const asset = await fetchResult.getFirstObject();

    // 进度处理器，仅在API版本15及以后有效。
    const progressHandler: photoAccessHelper.MediaAssetProgressHandler = {
      onProgress: (progress: number) => {
        console.info(`视频请求进度: ${progress}%`);
      },
    };

    const requestOptions: photoAccessHelper.RequestOptions = {
      deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
      compatibleMode: photoAccessHelper.CompatibleMode.COMPATIBLE_FORMAT_MODE,
      mediaAssetProgressHandler: progressHandler,
    };

    const destUri = `${context.cacheDir}/output.mp4`;

    const dataHandler: photoAccessHelper.MediaAssetDataHandler<boolean> = {
      onDataPrepared: (data: boolean | undefined) => {
        console.info(`视频数据准备完成: ${data}`);
      },
    };

    const taskId = await photoAccessHelper.MediaAssetManager.requestVideoFile(
      context, asset, requestOptions, destUri, dataHandler
    );
    console.info(`requestVideoFile taskId: ${taskId}`);
  } catch (err) {
    const error = err as BusinessError;
    console.error(`requestVideoFile failed: ${error.code}, ${error.message}`);
  } finally {
    if (fetchResult !== null) {
      fetchResult.close();
    }
  }
}
```
