---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-12
title: 如何屏蔽卡证识别CardRecognition图库选择入口
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 如何屏蔽卡证识别CardRecognition图库选择入口
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:3e300b802f3fc5cc56fb6fcaf2dfe6785ee629a9d12537e1ce5f6b902361cb4f
---

## 问题现象

高端理财身份证OCR识别，不能使用照片，只能拍照或者扫描有没有办法把图库选择的入口屏蔽？

## 背景知识

[卡证识别](../harmonyos-guides/vision-cardrecognition.md)控件提供身份证（目前仅支持中国大陆二代身份证，且不包含民汉双文身份证）、行驶证、驾驶证、护照、银行卡的结构化识别服务，满足卡证的自动分类功能，系统可自动判断所属卡证类型并返回结构化信息和卡证图片信息。

对于需要填充卡证信息的场景，如身份证、银行卡信息等，可使用卡证识别控件读取OCR（Optical Character Recognition）信息，将结果信息返回后进行填充。支持单独识别正面、反面，或同时进行双面识别。

## 解决方案

在卡证识别控件的参数配置对象[CardRecognitionConfig](../harmonyos-references/vision-card-recognition.md#cardrecognitionconfig)中有一个isPhotoSelectionSupported参数，可以控制在卡证识别时是否支持从图库中选取图片进行识别。参数说明如下：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isPhotoSelectionSupported | boolean | 否 | 是 | 是否支持从图库选图。   * true为显示图库按钮并支持从图库选图。 * false为不显示图库按钮且不支持从图库选图。 * 默认值：true。   元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |

只需要在CardRecognitionConfig对象配置时将isPhotoSelectionSupported设置为false即可。

完整示例参考如下：

CardDemoPage.ets：

```ts
import { CardRecognition, CardRecognitionResult, CardType, CardSide, ShootingMode } from '@kit.VisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'CardRecognitionPage';

@Component
export struct CardDemoPage {
  @State cardDataSource: Record<string, string>[] = [];
  @Consume('pathStack') pathStack: NavPathStack;

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Top }) {
        Stack() {
          this.cardDataShowBuilder();
        }
        .width('80%')
        .height('80%')

        CardRecognition({
          supportType: CardType.CARD_ID,
          cardSide: CardSide.DEFAULT,
          cardRecognitionConfig: {
            defaultShootingMode: ShootingMode.MANUAL,
            isPhotoSelectionSupported: false,
            setCardMargins:100
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

Index.ets：

```ts
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
    }
    .title('卡证识别控件demo')
    .navDestination(this.PageMap)
    .mode(NavigationMode.Stack)
  }
}
```
