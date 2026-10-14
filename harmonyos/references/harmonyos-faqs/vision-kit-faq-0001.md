---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/vision-kit-faq-0001
title: 卡证识别PixelMap转换问题排查
breadcrumb: FAQ > AI功能开发 > 机器学习 > 场景化视觉（Vision） > 常见问题 > 卡证识别PixelMap转换问题排查
category: harmonyos-faqs
scraped_at: 2026-10-15T07:16:21+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:816386e02f3d3dadb840e78547c2208df52cbf8463e200f7474760aa26ca857d
---

**Q：对于CardRecognition识别身份证返回的结果photoUri，希望将其转换成图片和另一张图片进行相似度对比，但将获取的photoUri转换成PixelMap时报错，image.createImageSource(photoUri)返回为undefined。**

**A**：获取到uri路径后，可以使用image提供的createImageSource()方法，为uri创建ImageSource图片源实例，并使用createPixelMap()方法，解码参数创建PixelMap对象。以下提供一个将卡证识别uri转换成image.PixelMap的示例：

```ts
import { CardRecognition, CardRecognitionResult, CardType, CardSide } from '@kit.VisionKit';
import { image } from '@kit.ImageKit';
import fs from '@ohos.file.fs';

@Entry
@Component
struct Index {
  @State showOCR: boolean = false;
  @State src?: image.PixelMap = undefined;

  build() {
    Stack() {
      Column() {
        Button('click me')
          .onClick(() => {
            this.showOCR = true;
          })
        Image(this.src)
      }

      if (this.showOCR) {
        this.CardOCRPage();
      }
    }
    .width('100%')
    .height('100%')
  }

  @Builder
  CardOCRPage() {
    CardRecognition({
      // 此处选择身份证类型作为示例
      supportType: CardType.CARD_ID,
      cardSide: CardSide.FRONT,
      cardRecognitionConfig: {
        isPhotoSelectionSupported: true,
        cardContentConfig: { idCard: { isPhotoNeeded: true } }
      },
      onResult: async (params: CardRecognitionResult) => {
        try {
          this.showOCR = false;
          if (params.cardInfo) {
            let photoUri = params.cardInfo.front.photoUri;
            let file = fs.openSync(photoUri, fs.OpenMode.READ_ONLY);
            const imageSource: image.ImageSource = image.createImageSource(file.fd);
            let decodingOptions: image.DecodingOptions = {
              editable: true,
              desiredPixelFormat: 3,
            };
            this.src = await imageSource.createPixelMap(decodingOptions);
            if (file) {
              fs.closeSync(file);
            }
          }
        } catch (error) {
          console.error('Card recognition error:', error);
        }
      }
    })
      .width('100%')
      .height('100%')
  }
}
```

**Q：卡证识别是纯SDK本地功能吗，数据会回传后端，后端配合识别吗？**

**A**：卡证识别是本地SDK功能，使用卡证识别控件读取OCR（Optical Character Recognition）信息，将结果信息返回后进行填充。卡证识别返回的uri没有有效期，可以通过OpenMode.READ\_ONLY方式将图片内容复制出来。

**Q：通过photoAccessHelper获取卡证识别结果的uri失败？**

**A**：可以通过拷贝进应用沙箱的方式解决。

**Q：卡证识别能否对身份证和银行卡在提取文字的同时，返回给开发者卡证四个边范围内的图片？**

**A**：Vision Kit目前已提供该能力，以身份证为例，可以通过cardImageUri或originalImageUri获取不含背景/含背景的人像面图片，可以参考[开发实例](../harmonyos-guides/vision-cardrecognition.md#section12918203941611)。

**Q：卡证识别能否判断所识别身份证的真伪？**

**A**：卡证识别控件可以用于识别身份证，并返回结构化信息和身份证图片信息，并不能判断身份证的真伪。

**Q：证件扫描如何自动判断证件正反面？**

**A**：卡证识别在扫描身份证完成后，会自动识别正反面，并通过params.cardInfo传递front或back来区分正反面。

**Q：卡证识别后的结果边角有裁剪，如何解决？**

**A**：在卡证识别控件[CardRecognition](../harmonyos-references/vision-card-recognition.md#section143611912403)中，可以通过cardRecognitionConfig的[setCardMargins](../harmonyos-references/vision-card-recognition.md#section14439151274411)参数设置经裁剪的卡证图片预留边距，范围[10,10000]，默认值为10，单位为px。

**Q：卡证识别CardRecognition接口，识别的身份证信息有时出现错误，如何解决？**

**A**：可以尝试换下光线和角度，光线不好也会影响识别。

**Q：卡证识别是否支持少数民族身份证识别？**

**A**：当前仅支持纯汉字的身份证识别，若少数民族身份证仅有汉字，则可以进行识别。

**Q：卡证识别是否提供纯API形式调用？**

**A**：卡证识别能力集成在系统底层，仅支持通过调用系统API拉起。基于安全考虑，卡证识别不允许被其他组件或窗口阻挡。

**Q：卡证识别是否支持横屏检测？**

**A**：当前仅平板和三折叠全展开态支持横屏检测。
