---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-documentscanner
title: 文档扫描
breadcrumb: 指南 > AI > Vision Kit（场景化视觉服务） > 文档扫描
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:44+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:7714ab9672d51185613d67cb218fcc85d42538b863fabd06d504c73a8517c33c
---

## 场景介绍

文档扫描控件提供拍摄文档并转换为高清扫描件的服务。仅需拍摄文档，即可自动裁剪和优化，并支持图片、PDF格式保存和分享；同时支持拍摄或从图库选择图片识别表格，生成表格文档。

可广泛用于教育办公场景，扫描文档、票据、课堂PPT和书籍等输出图片/PDF供用户完成发送、存档等操作。

**图1** 文档扫描示意图

![](https://media:401788444059173557)

## 约束与限制

* 支持的语种类型：简体中文、英文。
* 文档扫描暂时只支持phone、tablet设备。
* 不允许被其他组件或窗口遮挡。

## 接口说明

以下仅列出demo中调用的部分主要接口，具体API说明详见[API参考](../harmonyos-references/vision-document-scanner.md)。

| 接口名 | 描述 |
| --- | --- |
| [DocumentScanner](../harmonyos-references/vision-document-scanner.md#documentscanner) | 文档扫描控件 |
| [DocumentScannerResultCallback](../harmonyos-references/vision-document-scanner.md#documentscannerresultcallback) | 文档扫描结果回调 |

## 开发步骤

1. 将文档扫描控件相关的类添加至工程。

   ```typescript
   import { DocType, DocumentScanner, DocumentScannerConfig, SaveOption, FilterId, ShootingMode, DocumentScannerController } from '@kit.VisionKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 部分设备不支持文档扫描控件的表格提取功能。在使用该功能前，建议先调用isSheetDetectionSupported接口查询当前设备是否支持。

   ```typescript
   let documentScannerController: DocumentScannerController = new DocumentScannerController();
   let isSheetSupported = documentScannerController.isSheetDetectionSupported();
   hilog.info(0x0001, TAG, `isSheetSupported: ${isSheetSupported}`);
   ```
3. 配置布局，根据业务场景配置文档扫描控件的相关属性，获取返回的文档图片uri列表。

   ```typescript
   const TAG = 'DocumentScanner';

   @Entry
   @Component
   struct Index {
     private docScanConfig = new DocumentScannerConfig();

     aboutToAppear() {
       let documentScannerController: DocumentScannerController = new DocumentScannerController();
       let isSheetSupported = documentScannerController.isSheetDetectionSupported();
       if (isSheetSupported) {
         this.docScanConfig.supportType = [DocType.DOC, DocType.SHEET];
       } else {
         this.docScanConfig.supportType = [DocType.DOC];
       }
       this.docScanConfig.isGallerySupported = true;
       this.docScanConfig.editTabs = [];
       this.docScanConfig.maxShotCount = 3;
       this.docScanConfig.defaultFilterId = FilterId.ORIGINAL;
       this.docScanConfig.defaultShootingMode = ShootingMode.MANUAL;
       this.docScanConfig.isShareable = true;
       this.docScanConfig.originalUris = [];
     }

     build() {
       Column() {
         DocumentScanner({
           scannerConfig: this.docScanConfig,
           onResult: (code: number, saveType: SaveOption, uris: string[]) => {
             hilog.info(0x0001, TAG, `result code: ${code}, save: ${saveType}`);
             uris.forEach(uriString => {
               hilog.info(0x0001, TAG, `uri: ${uriString}`);
             })
           }
         }).size({ width: '100%', height: '100%' })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

## 开发实例

### Index.ets

```typescript
// 开发实例分两页实现，一页为文档扫描入口页，一页为文档扫描实现页
// 文档扫描入口页，需引入文档扫描实现页，以下文实例为例，实现页文件名为DocDemoPage
import { DocDemoPage } from './DocDemoPage';

@Entry
@Component
struct MainPage {
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

  @Builder
  PageMap(name: string) {
    if (name === 'documentScanner') {
      DocDemoPage()
    }
  }

  // 文档扫描入口按钮，可替换为业务入口
  build() {
    Navigation(this.pathStack) {
      Button('DocumentScanner', { stateEffect: true, type: ButtonType.Capsule })
        .width('50%')
        .height(40)
        .onClick(() => {
          this.pathStack.pushPath({ name: 'documentScanner' });
        })
    }.title('文档扫描控件demo').navDestination(this.PageMap)
    .mode(NavigationMode.Stack)
  }
}
```

### DocDemoPage.ets

```typescript
// 文档扫描实现页，文件名为DocDemoPage，需被引入至入口页
import {
  DocType,
  DocumentScanner,
  DocumentScannerConfig,
  SaveOption,
  FilterId,
  ShootingMode,
  DocumentScannerController
} from '@kit.VisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'DocDemoPage';

// 文档扫描页，用于加载UIExtensionAbility
@Component
export struct DocDemoPage {
  @State docImageUris: string[] = [];
  @Consume('pathStack') pathStack: NavPathStack;
  private docScanConfig = new DocumentScannerConfig();

  aboutToAppear() {
    let documentScannerController: DocumentScannerController = new DocumentScannerController();
    let isSheetSupported = documentScannerController.isSheetDetectionSupported();
    if (isSheetSupported) {
      this.docScanConfig.supportType = [DocType.DOC, DocType.SHEET];
    } else {
      this.docScanConfig.supportType = [DocType.DOC];
    }
    this.docScanConfig.isGallerySupported = true;
    this.docScanConfig.editTabs = [];
    this.docScanConfig.maxShotCount = 3;
    this.docScanConfig.defaultFilterId = FilterId.ORIGINAL;
    this.docScanConfig.defaultShootingMode = ShootingMode.MANUAL;
    this.docScanConfig.isShareable = true;
    this.docScanConfig.originalUris = [];
  }

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Top }) {
      // 展示文档扫描结果
        List() {
          ForEach(this.docImageUris, (uri: string) => {
            ListItem() {
              Image(uri)
                .objectFit(ImageFit.Contain)
                .width(100)
                .height(100)
            }
          })
        }
        .listDirection(Axis.Vertical)
        .alignListItem(ListItemAlign.Center)
        .margin({
          top: 50
        })
        .width('80%')
        .height('80%')
        
        // 文档扫描
        DocumentScanner({
          scannerConfig: this.docScanConfig,
          onResult: (code: number, saveType: SaveOption, uris: string[]) => {
            hilog.info(0x0001, TAG, `result code: ${code}, save: ${saveType}`);
            if (code === -1) {
              this.pathStack.pop();
            }
            uris.forEach(uriString => {
              hilog.info(0x0001, TAG, `uri: ${uriString}`);
            })
            this.docImageUris = uris;
          }
        })
          .size({ width: '100%', height: '100%' })
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .hideTitleBar(true)
  }
}
```
