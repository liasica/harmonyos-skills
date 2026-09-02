---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-cardrecognition
title: 卡证识别
breadcrumb: 指南 > AI > Vision Kit（场景化视觉服务） > 卡证识别
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:15+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:00b36a59117e9e71fc8bd94ca036d1a64b52ce7aaa49a2745cf7b94be1113435
---

从6.1.1(24)开始，新增支持对港澳居民来往内地通行证、台湾居民来往大陆通行证的识别。

## 场景介绍

卡证识别控件提供身份证（目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）二代身份证，且不包含民汉双语身份证）、行驶证、驾驶证、护照、银行卡、港澳居民来往内地通行证、台湾居民来往大陆通行证的结构化识别服务，并支持自动分类功能，系统可自动判断所属卡证类型并返回结构化信息和卡证图片信息。

对于需要填充卡证信息的场景，如身份证、银行卡信息等，可使用卡证识别控件读取OCR（Optical Character Recognition）信息，将结果信息返回后进行填充。支持单独识别正面、反面，或同时进行双面识别。

**图1** 银行卡识别示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/NVF-8Wj-SYezcTuIuM6Wzw/zh-cn_image_0000002706835432.png)

## 约束与限制

* 支持的语种类型：简体中文、英文。
* 卡证识别暂时只支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）相关卡证，具体包括身份证、银行卡、护照、驾驶证、行驶证、港澳居民来往内地通行证、台湾居民来往大陆通行证。
* 卡证需要保持与真实证件一致的长宽比、没有形变、正向拍摄角度小于30度。
* 卡证图像清晰、完整。无摩尔纹、无遮挡、无反光、无卡套。
* 不允许被其他组件或窗口遮挡。

## 接口说明

以下仅列出demo中调用的部分主要接口，具体API说明详见[API参考](../harmonyos-references/vision-card-recognition.md)。

| 接口名 | 描述 |
| --- | --- |
| [CardRecognition](../harmonyos-references/vision-card-recognition.md#cardrecognition) | 卡证识别控件 |
| [CardRecognitionResult](../harmonyos-references/vision-card-recognition.md#cardrecognitionresult) | 卡证识别结果 |

## 开发步骤

1. 将卡证识别控件相关的类添加至工程。

   ```typescript
   import { CardRecognition, CardRecognitionResult, CardType, CardSide, CardRecognitionConfig, ShootingMode, CardContentConfig, BankCardConfig } from '@kit.VisionKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 配置页面的布局，选择需要识别的卡证类型和需要识别的卡证页面，配置对应设置项，在回调中获取结果返回值。

   **说明** 

   从5.1.1(19)开始，[CardRecognition](../harmonyos-references/vision-card-recognition.md#cardrecognition)接口中的callback参数废弃，请使用onResult代替。

   以下分别为身份证、银行卡、护照、驾驶证、行驶证、港澳居民来往内地通行证、台湾居民来往大陆通行证的示例代码。

   ```typescript
   const TAG = 'CardRecognition';

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         // 身份证
         CardRecognition({
           supportType: CardType.CARD_ID,
           // 身份证可双面识别
           cardSide: CardSide.DEFAULT,
           cardRecognitionConfig: {
             defaultShootingMode: ShootingMode.MANUAL,
             isPhotoSelectionSupported: true
           },
           onResult: ((params: CardRecognitionResult) => {
             hilog.info(0x0001, TAG, `params code: ${params.code}`);
             hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`);
             hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`);
             hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`);
           })
         })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

   ```typescript
   const TAG = 'CardRecognition';

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         // 银行卡
         CardRecognition({
           supportType: CardType.CARD_BANK,
           // 银行卡为单面识别
           cardSide: CardSide.FRONT,
           cardRecognitionConfig: {
             defaultShootingMode: ShootingMode.MANUAL,
             isPhotoSelectionSupported: true,
             cardContentConfig: { bankCard: { isBankNumberDialogShown: true} }
           },
           onResult: ((params: CardRecognitionResult) => {
             hilog.info(0x0001, TAG, `params code: ${params.code}`);
             hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`);
             hilog.info(0x0001, TAG, `params cardInfo: ${JSON.stringify(params.cardInfo?.main)}`);
           })})
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

   ```typescript
   const TAG = 'CardRecognition';

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         // 护照
         CardRecognition({
           supportType: CardType.CARD_PASSPORT,
           // 护照为单面识别
           cardSide: CardSide.FRONT,
           cardRecognitionConfig: {
             defaultShootingMode: ShootingMode.MANUAL,
             isPhotoSelectionSupported: true
           },
           onResult: ((params: CardRecognitionResult) => {
             hilog.info(0x0001, TAG, `params code: ${params.code}`);
             hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`);
             hilog.info(0x0001, TAG, `params cardInfo: ${JSON.stringify(params.cardInfo?.main)}`);
           })})
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

   ```typescript
   const TAG = 'CardRecognition';

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         // 驾驶证
         CardRecognition({
           supportType: CardType.CARD_DRIVER_LICENSE,
           // 驾驶证可双面识别
           cardSide: CardSide.DEFAULT,
           cardRecognitionConfig: {
             defaultShootingMode: ShootingMode.MANUAL,
             isPhotoSelectionSupported: true
           },
           onResult: ((params: CardRecognitionResult) => {
             hilog.info(0x0001, TAG, `params code: ${params.code}`);
             hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`);
             hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`);
             hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`);
           })
         })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

   ```typescript
   const TAG = 'CardRecognition';

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         // 行驶证
         CardRecognition({
           supportType: CardType.CARD_VEHICLE_LICENSE,
           // 行驶证可双面识别
           cardSide: CardSide.DEFAULT,
           cardRecognitionConfig: {
             defaultShootingMode: ShootingMode.MANUAL,
             isPhotoSelectionSupported: true
           },
           onResult: ((params: CardRecognitionResult) => {
             hilog.info(0x0001, TAG, `params code: ${params.code}`);
             hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`);
             hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`);
             hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`);
           })
         })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

   ```typescript
   const TAG = 'CardRecognition';

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         // 港澳居民来往内地通行证
         CardRecognition({
           supportType: CardType.CARD_MAINLAND_TRAVEL_PERMIT_HK_MO,
           // 港澳居民来往内地通行证可双面识别
           cardSide: CardSide.DEFAULT,
           cardRecognitionConfig: {
             defaultShootingMode: ShootingMode.MANUAL,
             isPhotoSelectionSupported: true
           },
           onResult: ((params: CardRecognitionResult) => {
             hilog.info(0x0001, TAG, `params code: ${params.code}`);
             hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`);
             hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`);
             hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`);
           })
         })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

   ```typescript
   const TAG = 'CardRecognition';

   @Entry
   @Component
   struct Index {
     build() {
       Column() {
         // 台湾居民来往大陆通行证
         CardRecognition({
           supportType: CardType.CARD_MAINLAND_TRAVEL_PERMIT_TW,
           // 台湾居民来往大陆通行证可双面识别
           cardSide: CardSide.DEFAULT,
           cardRecognitionConfig: {
             defaultShootingMode: ShootingMode.MANUAL,
             isPhotoSelectionSupported: true
           },
           onResult: ((params: CardRecognitionResult) => {
             hilog.info(0x0001, TAG, `params code: ${params.code}`);
             hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`);
             hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`);
             hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`);
           })
         })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```

## 开发实例

### Index.ets

```typescript
// 卡证识别开发实例分两页实现，一页为卡证识别入口页，一页为卡证识别实现页
// 卡证识别入口页，需引入卡证识别实现页，以下文实例为例，实现页文件名为CardDemoPage
import { CardDemoPage } from './CardDemoPage';

@Entry
@Component
struct MainPage {
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

  @Builder
  PageMap(name: string) {
    if (name === 'cardRecognition') {
      CardDemoPage()
    }
  }

  // 卡证识别入口按钮
  build() {
    Navigation(this.pathStack) {
      Button('CardRecognition', { stateEffect: true, type: ButtonType.Capsule })
        .width('50%')
        .height(40)
        .onClick(() => {
          this.pathStack.pushPath({ name: 'cardRecognition' });
        })
    }.title('卡证识别控件demo').navDestination(this.PageMap)
    .mode(NavigationMode.Stack)
  }
}
```

### CardDemoPage.ets

```typescript
// 卡证识别实现页，文件名为CardDemoPage，需被引入至入口页
import { CardRecognition, CardRecognitionResult, CardType, CardSide, ShootingMode } from '@kit.VisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'CardRecognitionPage';

// 卡证识别页，用于加载UIExtensionAbility
@Component
export struct CardDemoPage {
  @State cardDataSource: Record<string, string>[] = [];
  @Consume('pathStack') pathStack: NavPathStack;

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Top }) {
        Stack() {
          this.cardDataShowBuilder()
        }
        .width('80%')
        .height('80%')

        CardRecognition({
          // 此处选择身份证类型作为示例
          supportType: CardType.CARD_ID,
          cardSide: CardSide.DEFAULT,
          cardRecognitionConfig: {
            defaultShootingMode: ShootingMode.MANUAL,
            isPhotoSelectionSupported: true
          },
          onResult: ((params: CardRecognitionResult) => {
            hilog.info(0x0001, TAG, `params code: ${params.code}`);
            if (params.code !== 200) {
              this.pathStack.pop();
            }
            hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`);
            if (params.cardInfo?.front !== undefined) {
              this.cardDataSource.push(params.cardInfo?.front);
            }

            if (params.cardInfo?.back !== undefined) {
              this.cardDataSource.push(params.cardInfo?.back);
            }

            if (params.cardInfo?.main !== undefined) {
              this.cardDataSource.push(params.cardInfo?.main);
            }
            hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`);
            hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`);
          })
        })
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
    .hideTitleBar(true)
  }

  @Builder
  cardDataShowBuilder() {
    List() {
      ForEach(this.cardDataSource, (cardData: Record<string, string>) => {
        ListItem() {
          Column() {
            Image(cardData.cardImageUri)
              .objectFit(ImageFit.Contain)
              .width(100)
              .height(100)

            Text(JSON.stringify(cardData))
              .width('100%')
              .fontSize(12)
          }
        }
      })
    }
    .listDirection(Axis.Vertical)
    .alignListItem(ListItemAlign.Center)
    .margin({
      top: 50
    })
    .width('100%')
    .height('100%')
  }
}
```
