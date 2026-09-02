---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-vision-3
title: 如何区分CardRecognition的取消和失败
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 如何区分CardRecognition的取消和失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:b9b158bf22ab3f3814158ad84f7f73725e5e4a67b85fd292dbb24a3ac7b80c56
---

## 问题现象

在卡证识别过程中，如何区分取消和失败？当CardRecognition识别正面成功后，摄像头不会开启，若识别结果图片不符合要求，如何重新调用识别接口？

## 背景知识

1. [卡证识别](../harmonyos-references/vision-card-recognition.md)提供身份证、行驶证、驾驶证、护照、银行卡等证件的结构化识别服务，满足卡证的自动分类功能，系统可自动判断所属卡证类型并返回结构化信息和卡证图片信息。
2. [CardRecognitionResult](../harmonyos-references/vision-card-recognition.md#cardrecognitionresult)可获取卡证识别结果是否成功，其中code表示结果码（200表示识别成功，1008701001表示未识别，1008701002表示识别失败，1008701003表示部分识别失败，1008701004表示未完成识别）。
3. 关于卡证识别功能，可参考相关[CardRecognition控件API](../harmonyos-references/vision-card-recognition.md#cardrecognition)和[卡证识别指南](../harmonyos-guides/vision-cardrecognition.md)，以及[Codelabs](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_Next-VisionKit)提供的示例。

## 解决方案

当CardRecognitionResult中code为1008701001时，表明未识别；当code为200时，通过实际识别到的数据来判断是否识别成功；如果识别数据正确，则进一步处理；如果数据错误，可使用[Class (Router)](../harmonyos-references/arkts-apis-uicontext-router.md)重新跳转到识别页面。示例代码如下：

```ts
import { CardRecognition, CardRecognitionResult, CardType } from '@kit.VisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { PromptAction } from '@kit.ArkUI';

const TAG: string = 'CardRecognitionPage';

@Entry
@Component
struct test {
  @State para: CardRecognitionResult | null = null;
  promptAction: PromptAction = this.getUIContext().getPromptAction();

  build() {
    Stack({ alignContent: Alignment.Top }) {
      CardRecognition({
        // 此处选择身份证类型作为示例
        supportType: CardType.CARD_ID,
        callback: ((params: CardRecognitionResult) => {
          this.para = params;
          hilog.info(0x0001, TAG, `params code: ${params.code}`);
          hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`);
          hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`);
          hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`);
          // params.code是-1说明是关闭，识别到后要退出
          if (params.code === -1) {
            this.promptAction.showToast({
              message: '未进行识别，已返回!',
              duration: 1000
            }); // 伙伴可以根据需求自行更改promptAction类型
            this.getUIContext().getRouter().back(1);
          } else {
            // 可以使用某些条件，判断信息是否全面，如果不全面就说明识别信息不全，识别失败
            if (!params.cardInfo?.front.sex) {
              this.promptAction.showToast({
                message: '识别失败，请重试!',
                duration: 1000
              }); // 可以根据需求自行更改promptAction类型
              this.getUIContext().getRouter().back(1);
            }
            // 接下来假设为未发现问题，可以进行后续操作
            else {
              // 后续处理，可以设计存储数据，
              // 处理完成进行跳转
              this.promptAction.showToast({
                message: '识别完成!',
                duration: 1000
              }); // 可以根据需求自行更改promptAction类型
              this.getUIContext().getRouter().back(1);
            }
          }
        })
      });
    }
    .width('100%')
    .height('100%');
  }
}
```

* 当用户点击右上角取消按钮时，返回的code为1008701001。
* 当识别成功后，如果数据正确，可按照正常的业务流程处理。如果数据错误，比如身份证上的名字被盖住了，虽然识别成功但数据错乱，可使用[Class (Router)](../harmonyos-references/arkts-apis-uicontext-router.md)重新跳转到识别页面。
* 当识别异常时，比如本来需要识别的是银行卡，但用户拿出的是学生卡，则不会进行任何识别操作。

## 常见FAQ

Q：目前OCR识别主要支持一些常见的文档类型，如身份证和名片等。对于一些特定的小票、营业执照、发票和价签等，这些类型不在默认支持范围内。是否可以通过自定义识别插槽来实现这些特定场景的OCR识别？

A：当前提供了[通用文字识别](../harmonyos-guides/core-vision-text-recognition.md)API，可用于识别通用文字。

Q：有无不区分识别身份证正反面的API？

A：现阶段的API都是需要传CardSide的，默认身份证为人像面。

Q：关于Vision Kit的活体识别、身份证识别和银行卡识别，这些功能是否可以在Next系统上使用，以及目前的免费使用期限和后续收费详情。

A：Vision Kit是Next系统下的功能模块，其使用受到相关[约束与限制](../harmonyos-guides/vision-introduction.md#约束与限制)，视觉服务目前实施试用期免费的计费政策，试用期至2026年12月31日，后续有新的收费政策时，会在官网提前通知。

Q：使用[卡证识别控件](../harmonyos-references/vision-card-recognition.md)，在识别银行卡卡号和有效期在背面的主题卡（含异形卡）会出现卡顿、识别错误等情况，且不能识别竖版银行卡片。

A：当前针对银行卡的卡证识别功能已优化，现已支持非标卡、竖版银行卡的识别功能。
