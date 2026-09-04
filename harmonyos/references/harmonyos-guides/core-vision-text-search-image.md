---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-text-search-image
title: 通过文本搜索图片
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 通过文本搜索图片
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:42+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:034b38cb66293b097b99d7243bad50d3f5693319d70243429e9b9456a4ee5e21
---

## 适用场景

文本搜索图片服务提供基于文本语意的图片检索能力。用户可以通过输入文本语意，从图片库中搜索匹配的图像结果。该服务适用于图片检索、相册管理、内容推荐等场景。

效果如下图所示：

![](https://media:401788444060649570 "点击放大")

## 开发步骤

1. 将实现文本搜索图片相关的工具和依赖导入工程。

   ```typescript
   import { textSearchImage } from '@kit.CoreVisionKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 在aboutToAppear中调用[textSearchImage.init()](../harmonyos-references/core-vision-text-search-image-api.md#textsearchimageinit)初始化文本搜索图片分析器服务，在aboutToDisappear中调用[textSearchImage.release()](../harmonyos-references/core-vision-text-search-image-api.md#textsearchimagerelease)释放资源。

   ```typescript
   async aboutToAppear(): Promise<void> {
     const initResult = await textSearchImage.init();
     hilog.info(0x0000, 'textSearchImageSample', `Text search image initialization result:${initResult}`);
   }

   async aboutToDisappear(): Promise<void> {
     await textSearchImage.release();
     hilog.info(0x0000, 'textSearchImageSample', 'Text search image released successfully');
   }
   ```
3. 调用[textSearchImage.insertImage](../harmonyos-references/core-vision-text-search-image-api.md#textsearchimageinsertimage)方法，将图片特征插入数据库。

   ```typescript
   async insertImageToDatabase(imagePath: string, scope: string): Promise<void> {
     try {
       const result = await textSearchImage.insertImage(imagePath, scope);
       hilog.info(0x0000, 'textSearchImageSample', `Insert image result: ${result}`);
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(0x0000, 'textSearchImageSample', `Insert image failed. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```
4. 调用[textSearchImage.search](../harmonyos-references/core-vision-text-search-image-api.md#textsearchimagesearch)方法，获取匹配的图像结果。

   ```typescript
   async searchImages(query: string, scope: string, topKey: number = 100): Promise<void> {
     try {
       const results = await textSearchImage.search(query, scope, topKey);
       hilog.info(0x0000, 'textSearchImageSample', `Search results count: ${results.length}`);
       results.forEach((imageObject, index) => {
         hilog.info(0x0000, 'textSearchImageSample', `Result ${index}: imagePath=${imageObject.imagePath}, similarity=${imageObject.similarity}`);
       });
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(0x0000, 'textSearchImageSample', `Search failed. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```
5. 调用[textSearchImage.deleteImage](../harmonyos-references/core-vision-text-search-image-api.md#textsearchimagedeleteimage)方法，从数据库中删除指定的图片数据。

   ```typescript
   async deleteImageFromDatabase(imagePath: string, scope: string): Promise<void> {
     try {
       const result = await textSearchImage.deleteImage(imagePath, scope);
       hilog.info(0x0000, 'textSearchImageSample', `Delete image result: ${result}`);
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(0x0000, 'textSearchImageSample', `Delete image failed. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```
6. 调用[textSearchImage.clearData](../harmonyos-references/core-vision-text-search-image-api.md#textsearchimagecleardata)方法，清除数据库中的所有数据。

   ```typescript
   async clearAllData(): Promise<void> {
     try {
       const result = await textSearchImage.clearData();
       hilog.info(0x0000, 'textSearchImageSample', `Clear data result: ${result}`);
     } catch (error) {
       const err = error as BusinessError;
       hilog.error(0x0000, 'textSearchImageSample', `Clear data failed. Code: ${err.code}, message: ${err.message}`);
     }
   }
   ```

## 开发实例

### Index.ets

```typescript
import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State searchQuery: string = '';
  @State scope: string = 'default_scope';
  @State resultMessage: string = '';

  async aboutToAppear(): Promise<void> {
    const initResult = await textSearchImage.init();
    hilog.info(0x0000, 'textSearchImageSample', `Text search image initialization result:${initResult}`);
  }

  async aboutToDisappear(): Promise<void> {
    await textSearchImage.release();
    hilog.info(0x0000, 'textSearchImageSample', 'Text search image released successfully');
  }

  build() {
    Column() {
      Text('Text Search Image Sample')
        .fontSize(24)
        .margin(10)

      TextInput({ placeholder: 'Enter image path' })
        .width('80%')
        .margin(10)
        .onChange((value: string) => {
          this.searchQuery = value;
        })

      TextInput({ placeholder: 'Enter scope' })
        .width('80%')
        .margin(10)
        .onChange((value: string) => {
          this.scope = value;
        })

      Button('Insert Image')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.insertImageToDatabase();
        })

      Button('Search Images')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.searchImages();
        })

      Button('Delete Image')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.deleteImageFromDatabase();
        })

      Button('Clear All Data')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.clearAllData();
        })

      Text(this.resultMessage)
        .copyOption(CopyOptions.LocalDevice)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private async insertImageToDatabase(): Promise<void> {
    try {
      const result = await textSearchImage.insertImage(this.searchQuery, this.scope);
      this.resultMessage = `Insert image result: ${result}`;
      hilog.info(0x0000, 'textSearchImageSample', `Insert image result: ${result}`);
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Insert image failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Insert image failed. Code: ${err.code}, message: ${err.message}`);
    }
  }

  private async searchImages(): Promise<void> {
    try {
      const results = await textSearchImage.search(this.searchQuery, this.scope, 100);
      this.resultMessage = `Search results count: ${results.length}`;
      hilog.info(0x0000, 'textSearchImageSample', `Search results count: ${results.length}`);
      results.forEach((imageObject, index) => {
        hilog.info(0x0000, 'textSearchImageSample', `Result ${index}: imagePath=${imageObject.imagePath}, similarity=${imageObject.similarity}`);
      });
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Search failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Search failed. Code: ${err.code}, message: ${err.message}`);
    }
  }

  private async deleteImageFromDatabase(): Promise<void> {
    try {
      const result = await textSearchImage.deleteImage(this.searchQuery, this.scope);
      this.resultMessage = `Delete image result: ${result}`;
      hilog.info(0x0000, 'textSearchImageSample', `Delete image result: ${result}`);
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Delete image failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Delete image failed. Code: ${err.code}, message: ${err.message}`);
    }
  }

  private async clearAllData(): Promise<void> {
    try {
      const result = await textSearchImage.clearData();
      this.resultMessage = `Clear data result: ${result}`;
      hilog.info(0x0000, 'textSearchImageSample', `Clear data result: ${result}`);
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Clear data failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Clear data failed. Code: ${err.code}, message: ${err.message}`);
    }
  }
}
```
