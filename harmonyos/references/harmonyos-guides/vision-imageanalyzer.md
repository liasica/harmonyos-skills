---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-imageanalyzer
title: AI识图
breadcrumb: 指南 > AI > Vision Kit（场景化视觉服务） > AI识图
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:44+08:00
doc_updated_at: 2026-04-29
content_hash: sha256:a8cff443f5aa1dc90a6ac5ad142d2efc67f2c67574386874830d962dfd62984b
---

## 场景介绍

AI识图是通过聚合OCR（Optical Character Recognition）、主体分割、实体识别、多目标识别等AI能力，提供场景化的文本识别、主体分割、识图搜索功能。AI识图功能主开关入口在基础控件API列表中，如果您接受AI识图默认的交互和功能，仅需使用基础控件提供的相关使能接口打开功能开关即可。该文档配套的API配合基础控件使用，主要满足您的定制诉求，帮助您完成AI识图功能交互上的细粒度控制，获取文本识别、图像分割等分析结果以便您进行扩展业务的开发，目前支持的基础控件范围包括[Image](../harmonyos-references/ts-basic-components-image.md#enableanalyzer11)、[Video](../harmonyos-references/ts-media-components-video.md#enableanalyzer12)、[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md#enableanalyzer12)。其中，配合Image控件可完成静态图片上的识图功能，配合Video控件可完成视频播放暂停帧的识图功能，配合XComponent可完成自定义渲染等场景下的图像的识图功能。

识图功能提供如下能力：

* 识别文字。

  用户长按文本选取文字或持续长按文本中的电话号码、邮箱、网址、地址、时间等实体，可触发对应实体的快捷操作，如持续长按文本中的时间，可触发"新建日程"快捷操作入口。
* 识图搜索。

  用户抠图后可基于抠出的主体进行识图搜索，开发者也可以主动触发目标标识，触发后会识别图中的动物、植物、建筑物等目标并用相应的ICON标识，用户点击ICON也可以进行识图搜索，搜索结果会以模态窗的方式为用户呈现。
* 主体分割。

  用户长按主体分割，分割后用户可以完成复制，分享，全选，识图搜索等功能。
* AIButton。

  AIButton承载了电话号码、邮箱、网址、地址、时间等实体的显性下划线标识（点击后出现快捷操作菜单），原图翻译（系统设置语种与图片上文本语种不一致且能将图中文本翻译为系统当前设置的语种时出现），表格提取（图片中存在表格时出现）等功能特性。配置AIButton属性可见后，会对图片进行预分析，当图片中存在文本且文本区域大于图片区域的5%时AIButton才会显示。

识图功能提供如下建议：

* AI识图特性可帮助消费者从图片上获取更多的信息（长按抠图，长按选取文本，长按实体识别等）。建议在大图预览场景都打开此能力，大图预览场景下用户对图片中的内容会更感兴趣，此时适时的提供识图服务契合用户体验场景，同时为用户提供最佳的识图交互体验。
* AI识图特性中的AIButton与图片中是否有文本存在关联，显性的提醒用户操作文本。开启AIButton会触发图片的预分析从而导致一定的功耗开销，建议开发者充分理解自身业务场景，预估目标用户图片内容分布，兼顾用户图片浏览体验和提供更高阶AI识图功能体验的情况下按需提供AIButton露出。例如，业务本身是辅助用户高效提取图片中的文本内容，开启AIButton将会提升用户文本提取的体验。业务本身更偏向于图片编辑，也可隐藏AIButton。

**图1** AI识图示意图

![](https://media:401788444059537563)

## 约束与限制

* 支持的文本语种类型：简体中文、繁体中文、英文、维吾尔文、藏文。
* 支持图片最小规格100\*100分辨率。
* 分析图像要求是静态非矢量图，即svg、gif等图像类型不支持分析，支持传入[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)进行分析，目前仅支持[RGBA\_8888](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7)类型。
* 支持翻译的图片宽高最小比例为1:3（高度小于宽度的3倍），支持文本识别的图片宽高最小比例为1:7（高度小于宽度的7倍）。
* 当前设备支持本能力可以通过[getImageAnalyzerSupportTypes](../harmonyos-references/ts-image-common.md#getimageanalyzersupporttypes12)进行判断。

  返回格式为“SupportTypes: [主体识别功能枚举值,文字识别功能枚举值,对象查找功能枚举值]”，具体枚举值可参见[ImageAnalyzerType](../harmonyos-references/ts-image-common.md#imageanalyzertype12)。

  若返回“SupportTypes: []”，则说明当前设备不支持AI识图能力；若返回其他值，则说明当前设备支持AI识图能力。

  ```typescript
  import { visionImageAnalyzer } from '@kit.VisionKit';

  @Entry
  @Component
  struct Index {
    private aiController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController();

    build() {
      Row() {
        Button('getTypes')
          .onClick(() => {
            let supportTypes = this.aiController.getImageAnalyzerSupportTypes();
            console.info(`supportTypes: ${JSON.stringify(supportTypes)}`);
          })
      }
    }
  }
  ```

## 开发步骤

1. 将AI识图控件相关的类添加。

   ```typescript
   import { visionImageAnalyzer } from '@kit.VisionKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[VisionImageAnalyzerController](../harmonyos-references/vision-image-analyzer.md#visionimageanalyzercontroller)对象。

   ```typescript
   private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController();
   private isSupportImageAnalyzer: boolean = false;
   ```
3. 判断设备是否支持AI识图相关功能，若支持，添加订阅事件和取消事件监听方法。

   ```typescript
   aboutToAppear(): void {
     let supportTypes = this.visionImageAnalyzerController.getImageAnalyzerSupportTypes();
     if (supportTypes.length > 0) {
       this.isSupportImageAnalyzer = true;
       this.registerListener();
     }
   }

   registerListener(){
     this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
       console.info('DEMO_TAG', `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`)
     });
     this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
       console.info('DEMO_TAG', `textAnalysis result: ${JSON.stringify(text)}`);
     });
     this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
       console.info('DEMO_TAG', `selectedTextChange result: ${JSON.stringify(selectedText)}`);
     });
     this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
       console.info('DEMO_TAG', `subjectAnalysis result: ${JSON.stringify(subjects)}`);
     });
     this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
       console.info('DEMO_TAG', `selectedSubjectsChange result: ${JSON.stringify(subjects)}`);
     });
     this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
       console.error('DEMO_TAG', `analyzerFailed result: ${JSON.stringify(error)}`);
     });
   }

   aboutToDisappear(): void {
     this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange');
     this.visionImageAnalyzerController.off('textAnalysis');
     this.visionImageAnalyzerController.off('selectedTextChange');
     this.visionImageAnalyzerController.off('subjectAnalysis');
     this.visionImageAnalyzerController.off('selectedSubjectsChange');
     this.visionImageAnalyzerController.off('analyzerFailed');
   }
   ```
4. 绑定[VisionImageAnalyzerController](../harmonyos-references/vision-image-analyzer.md#visionimageanalyzercontroller)对象，可以控制识图相关的交互。

   ```typescript
   build() {
     Stack() {
       // 需要替换您自己的资源图片，存放在resources/base/media目录下，设置的types参数必须是上一步supportTypes里包含的。
       Image($r('app.media.img'), {
         types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
         aiController: this.visionImageAnalyzerController
       })
         .width('100%')
         .height('100%')
         .enableAnalyzer(this.isSupportImageAnalyzer ? true: false)
         .objectFit(ImageFit.Contain)
     }.width('100%').height('100%')
   }
   ```

## 开发实例

### Index.ets

```typescript
import { visionImageAnalyzer } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
@Entry
@Component
struct ImageDemo {
  private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController();
  private isSupportImageAnalyzer: boolean = false;
  aboutToAppear(): void {
    let supportTypes = this.visionImageAnalyzerController.getImageAnalyzerSupportTypes();
    if (supportTypes.length > 0) {
      this.isSupportImageAnalyzer = true;
      this.registerListener();
    }
  }

  registerListener(){
    this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
      console.info('DEMO_TAG', `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`)
    });
    this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
      console.info('DEMO_TAG', `textAnalysis result: ${JSON.stringify(text)}`);
    });
    this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
      console.info('DEMO_TAG', `selectedTextChange result: ${JSON.stringify(selectedText)}`);
    });
    this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
      console.info('DEMO_TAG', `subjectAnalysis result: ${JSON.stringify(subjects)}`);
    });
    this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
      console.info('DEMO_TAG', `selectedSubjectsChange result: ${JSON.stringify(subjects)}`);
    });
    this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
      console.error('DEMO_TAG', `analyzerFailed result: ${JSON.stringify(error)}`);
    });
  }

  aboutToDisappear(): void {
    this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange');
    this.visionImageAnalyzerController.off('textAnalysis');
    this.visionImageAnalyzerController.off('selectedTextChange');
    this.visionImageAnalyzerController.off('subjectAnalysis');
    this.visionImageAnalyzerController.off('selectedSubjectsChange');
    this.visionImageAnalyzerController.off('analyzerFailed');
  }

  build() {
    Stack() {
      Image($r('app.media.img'), {
        types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
        aiController: this.visionImageAnalyzerController
      })
        .width('100%')
        .height('100%')
        .enableAnalyzer(this.isSupportImageAnalyzer ? true : false)
        .objectFit(ImageFit.Contain)
    }.width('100%').height('100%')
  }
}
```
