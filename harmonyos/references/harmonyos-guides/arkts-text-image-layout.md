---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-image-layout
title: 图文混排
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用文本 > 图文混排
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:01f7250df8e203346f4903db93f751464f1cc9fa550bbdeeaff99d77b7ee6d17
---

图文混排是指图片与文字混合排列，文字可展示于图片四周。此排列方式能够直观呈现页面信息，增强视觉冲击力，使页面展示效果更加多样化。

## 使用Span和ImageSpan实现图文混排

通过设置[Text](../harmonyos-references/ts-basic-components-text.md)组件[textVerticalAlign](../harmonyos-references/ts-basic-components-text.md#textverticalalign20)属性和设置[ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md)组件[verticalAlign](../harmonyos-references/ts-basic-components-imagespan.md#verticalalign)为ImageSpanAlignment.FOLLOW\_PARAGRAPH，实现商品价格优惠信息展示的应用场景。

```typescript
Text() {
  // 请将$r('app.media.hot_sale')替换为实际资源文件
  ImageSpan($r('app.media.hot_sale'))
    .width(50)
    .height(30)
    .borderRadius(5)
    .verticalAlign(ImageSpanAlignment.FOLLOW_PARAGRAPH)
  // 请将$r('app.string.surprise_price')替换为实际资源文件，在本示例中该资源文件的value值为"惊喜价 ￥1299"
  Span($r('app.string.surprise_price'))
    .fontSize(25)
    .fontColor(Color.Red)
  Span('1599')
    .decoration({
      type: TextDecorationType.LineThrough,
      color: Color.Grey,
      style: TextDecorationStyle.SOLID
    })
    .fontSize(16)
}.textVerticalAlign(TextVerticalAlign.CENTER)
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/GJ9oCMgoSbCVFHHLPiu6Zw/zh-cn_image_0000002706833596.png)

## 使用属性字符串实现图文混排

通过[ImageAttachment](../harmonyos-references/ts-universal-styled-string.md#imageattachment)添加图片，[TextStyle](../harmonyos-references/ts-universal-styled-string.md#textstyle)设置多种文本样式，实现商品详情信息展示的应用场景。

```typescript
// resourceGetString封装工具，从资源中获取字符串
import resourceGetString from '../../common/resource';
import { image } from '@kit.ImageKit';
import { LengthMetrics } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = '[Sample_Textcomponent]';
const DOMAIN = 0xF811;
const BUNDLE = 'Textcomponent_';

@Entry
@Component
struct styled_string_demo {
  imagePixelMap: image.PixelMap | undefined = undefined;
  mutableStr: MutableStyledString = new MutableStyledString('123');
  controller: TextController = new TextController();

  async aboutToAppear() {
    hilog.info(DOMAIN, TAG, BUNDLE + 'aboutToAppear initial imagePixelMap');
    // $r('app.media.sky')需要替换为开发者所需的资源文件。
    this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.sky'));
  }

  private async getPixmapFromMedia(resource: Resource) {
    try {
      let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
      let imageSource = image.createImageSource(unit8Array?.buffer?.slice(0, unit8Array?.buffer?.byteLength));
      let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
        desiredPixelFormat: image.PixelMapFormat.RGBA_8888
      });
      await imageSource.release();
      return createPixelMap;
    } catch (error) {
      hilog.error(DOMAIN, TAG, `Get pixmap failed. error code: ${error.code}, error message: ${error.message}`);
    }
    return undefined;
  }

  leadingMarginValue: ParagraphStyle = new ParagraphStyle({
    leadingMargin: LengthMetrics.vp(5),
    maxLines: 2,
    overflow: TextOverflow.Ellipsis,
    textVerticalAlign: TextVerticalAlign.BASELINE
  });
  // 行高样式对象
  lineHeightStyle1: LineHeightStyle = new LineHeightStyle(new LengthMetrics(24));
  // Bold样式
  boldTextStyle: TextStyle = new TextStyle({ fontWeight: FontWeight.Bold });
  // 创建含段落样式的对象paragraphStyledString1
  paragraphStyledString1: MutableStyledString =
    // 请将$r('app.string.print_photo')替换为实际资源文件，在本示例中该资源文件的value值为"\n高质量冲洗照片，高清冲印3/4/5/6寸包邮塑封，品质保证，"
    new MutableStyledString(resourceGetString.resourceToString($r('app.string.print_photo')), [
      {
        start: 0,
        length: 28,
        styledKey: StyledStringKey.PARAGRAPH_STYLE,
        styledValue: this.leadingMarginValue
      },
      {
        start: 11,
        length: 4,
        styledKey: StyledStringKey.LINE_HEIGHT,
        styledValue: this.lineHeightStyle1
      }
    ]);
  // 请将$r('app.string.limited_time_discount')替换为实际资源文件，在本示例中该资源文件的value值为"\n限时直降5.15元 限量增送"
  paragraphStyledString2: MutableStyledString = new MutableStyledString(resourceGetString.resourceToString($r('app.string.limited_time_discount')), [
    {
      start: 0,
      length: 5,
      styledKey: StyledStringKey.PARAGRAPH_STYLE,
      styledValue: this.leadingMarginValue
    },
    {
      start: 0,
      length: 4,
      styledKey: StyledStringKey.LINE_HEIGHT,
      styledValue: new LineHeightStyle(new LengthMetrics(40))
    },
    {
      start: 0,
      length: 9,
      styledKey: StyledStringKey.FONT,
      styledValue: this.boldTextStyle
    },
    {
      start: 1,
      length: 9,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(20), fontColor: Color.Red })
    },
    {
      start: 11,
      length: 4,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: Color.Grey, fontSize: LengthMetrics.vp(14) })
    }
  ]);
  // 请将$r('app.string.sales_volume')替换为实际资源文件，在本示例中该资源文件的value值为"\n￥22.50 销量400万+"
  paragraphStyledString3: MutableStyledString = new MutableStyledString(resourceGetString.resourceToString($r('app.string.sales_volume')), [
    {
      start: 0,
      length: 15,
      styledKey: StyledStringKey.PARAGRAPH_STYLE,
      styledValue: this.leadingMarginValue
    },
    {
      start: 0,
      length: 7,
      styledKey: StyledStringKey.LINE_HEIGHT,
      styledValue: new LineHeightStyle(new LengthMetrics(40))
    },
    {
      start: 0,
      length: 7,
      styledKey: StyledStringKey.FONT,
      styledValue: this.boldTextStyle
    },
    {
      start: 1,
      length: 1,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(18), fontColor: Color.Red })
    },
    {
      start: 2,
      length: 2,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(36), fontColor: Color.Red })
    },
    {
      start: 4,
      length: 3,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontSize: LengthMetrics.vp(20), fontColor: Color.Red })
    },
    {
      start: 7,
      length: 9,
      styledKey: StyledStringKey.FONT,
      styledValue: new TextStyle({ fontColor: Color.Grey, fontSize: LengthMetrics.vp(14) })
    }
  ]);

  build() {
    Row() {
      Column({ space: 10 }) {
        Text(undefined, { controller: this.controller })
          .copyOption(CopyOptions.InApp)
          .draggable(true)
          .backgroundColor('#FFFFFF')
          .borderRadius(5)
          .width(210)
        // 请将$r('app.string.textImageMixedLayout_content')替换为实际资源文件，在本示例中该资源文件的value值为"点击查看商品详情"
        Button($r('app.string.textImageMixedLayout_content'))
          .onClick(() => {
            if (this.imagePixelMap !== undefined) {
              this.mutableStr = new MutableStyledString(new ImageAttachment({
                value: this.imagePixelMap,
                size: { width: 210, height: 190 },
                verticalAlign: ImageSpanAlignment.BASELINE,
                objectFit: ImageFit.Fill,
                layoutStyle: {
                  borderRadius: LengthMetrics.vp(5)
                }
              }));
              this.paragraphStyledString1.appendStyledString(this.paragraphStyledString2);
              this.paragraphStyledString1.appendStyledString(this.paragraphStyledString3);
              this.mutableStr.appendStyledString(this.paragraphStyledString1);
              this.controller.setStyledString(this.mutableStr);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
    .backgroundColor('#F8F8FF')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/Pxf6-v0vTCSpSttAj7ZUbA/zh-cn_image_0000002736312705.png)
