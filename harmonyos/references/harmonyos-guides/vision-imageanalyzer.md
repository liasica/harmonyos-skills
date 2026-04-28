---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-imageanalyzer
title: AI识图
breadcrumb: 指南 > AI > Vision Kit（场景化视觉服务） > AI识图
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:82c401ffecd01055a9745a156527d1aee38e4608e07f2ac5826bfa7b63b1196f
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/9m5bSrtISkCVuRXtLB_B3g/zh-cn_image_0000002583439399.png?HW-CC-KV=V1&HW-CC-Date=20260427T235354Z&HW-CC-Expire=86400&HW-CC-Sign=31587F73ED420EC74636DF9200CCD6AECF3245B6C18F356FE5B961CA246E3588)

## 约束与限制

* 支持的文本语种类型：简体中文、繁体中文、英文、维吾尔文、藏文。
* 支持图片最小规格100\*100分辨率。
* 分析图像要求是静态非矢量图，即svg、gif等图像类型不支持分析，支持传入[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)进行分析，目前仅支持[RGBA\_8888](../harmonyos-references/arkts-apis-image-e.md#pixelmapformat7)类型。
* 支持翻译的图片宽高最小比例为1:3（高度小于宽度的3倍），支持文本识别的图片宽高最小比例为1:7（高度小于宽度的7倍）。
* 当前设备支持本能力可以通过[getImageAnalyzerSupportTypes](../harmonyos-references/ts-image-common.md#getimageanalyzersupporttypes12)进行判断。

  返回格式为“SupportTypes: [主体识别功能枚举值,文字识别功能枚举值,对象查找功能枚举值]”，具体枚举值可参见[ImageAnalyzerType](../harmonyos-references/ts-image-common.md#imageanalyzertype12)。

  若返回“SupportTypes: []”，则说明当前设备不支持AI识图能力；若返回其他值，则说明当前设备支持AI识图能力。

  ```
  1. import { visionImageAnalyzer } from '@kit.VisionKit';

  3. @Entry
  4. @Component
  5. struct Index {
  6. private aiController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController()

  8. build() {
  9. Row() {
  10. Button('getTypes')
  11. .onClick(() => {
  12. let SupportTypes = this.aiController.getImageAnalyzerSupportTypes()
  13. console.info(`SupportTypes: ${JSON.stringify(SupportTypes)}`)
  14. })
  15. }
  16. }
  17. }
  ```

## 开发步骤

1. 将AI识图控件相关的类添加。

   ```
   1. import { visionImageAnalyzer } from '@kit.VisionKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 初始化[VisionImageAnalyzerController](../harmonyos-references/vision-image-analyzer.md#visionimageanalyzercontroller)对象。

   ```
   1. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController();
   2. private isSupportImageAnalyzer: boolean = false;
   ```
3. 判断设备是否支持AI识图相关功能，若支持，添加订阅事件。

   ```
   1. aboutToAppear(): void {
   2. let supportTypes = this.visionImageAnalyzerController.getImageAnalyzerSupportTypes();
   3. if (supportTypes.length > 0) {
   4. this.isSupportImageAnalyzer = true;
   5. this.registerListener();
   6. }
   7. }

   9. registerListener(){
   10. this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
   11. console.info("DEMO_TAG", `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`)
   12. })
   13. this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
   14. console.info("DEMO_TAG", `textAnalysis result: ${JSON.stringify(text)}`)
   15. })
   16. this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
   17. console.info("DEMO_TAG", `selectedTextChange result: ${JSON.stringify(selectedText)}`)
   18. })
   19. this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
   20. console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
   21. })
   22. this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
   23. console.info("DEMO_TAG", `selectedSubjectsChange result: ${JSON.stringify(subjects)}`)
   24. })
   25. this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
   26. console.error("DEMO_TAG", `analyzerFailed result: ${JSON.stringify(error)}`)
   27. })
   28. }
   ```
4. 绑定[VisionImageAnalyzerController](../harmonyos-references/vision-image-analyzer.md#visionimageanalyzercontroller)对象，可以控制识图相关的交互。

   ```
   1. build() {
   2. Stack() {
   3. // 需要替换您自己的资源图片，存放在resources/base/media目录下,设置的types参数必须是上一步supportTypes里包含的
   4. Image($r('app.media.img'), {
   5. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
   6. aiController: this.visionImageAnalyzerController
   7. })
   8. .width('100%')
   9. .height('100%')
   10. .enableAnalyzer(this.isSupportImageAnalyzer ? true: false)
   11. .objectFit(ImageFit.Contain)
   12. }.width('100%').height('100%')
   13. }
   ```
5. 取消订阅事件。

   ```
   1. aboutToDisappear(): void {
   2. this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
   3. this.visionImageAnalyzerController.off('textAnalysis')
   4. this.visionImageAnalyzerController.off('selectedTextChange')
   5. this.visionImageAnalyzerController.off('subjectAnalysis')
   6. this.visionImageAnalyzerController.off('selectedSubjectsChange')
   7. this.visionImageAnalyzerController.off('analyzerFailed')
   8. }
   ```

## 开发实例

### Index.ets

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';
2. import { BusinessError } from '@kit.BasicServicesKit'
3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController()
7. private isSupportImageAnalyzer: boolean = false;
8. aboutToAppear(): void {
9. let supportTypes = this.visionImageAnalyzerController.getImageAnalyzerSupportTypes();
10. if (supportTypes.length > 0) {
11. this.isSupportImageAnalyzer = true;
12. this.registerListener();
13. }
14. }

16. registerListener(){
17. this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
18. console.info("DEMO_TAG", `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`)
19. })
20. this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
21. console.info("DEMO_TAG", `textAnalysis result: ${JSON.stringify(text)}`)
22. })
23. this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
24. console.info("DEMO_TAG", `selectedTextChange result: ${JSON.stringify(selectedText)}`)
25. })
26. this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
27. console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
28. })
29. this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
30. console.info("DEMO_TAG", `selectedSubjectsChange result: ${JSON.stringify(subjects)}`)
31. })
32. this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
33. console.error("DEMO_TAG", `analyzerFailed result: ${JSON.stringify(error)}`)
34. })
35. }
36. build() {
37. Stack() {
38. Image($r('app.media.img'), {
39. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
40. aiController: this.visionImageAnalyzerController
41. })
42. .width('100%')
43. .height('100%')
44. .enableAnalyzer(this.isSupportImageAnalyzer ? true : false)
45. .objectFit(ImageFit.Contain)
46. }.width('100%').height('100%')
47. }
48. aboutToDisappear(): void {
49. this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
50. this.visionImageAnalyzerController.off('textAnalysis')
51. this.visionImageAnalyzerController.off('selectedTextChange')
52. this.visionImageAnalyzerController.off('subjectAnalysis')
53. this.visionImageAnalyzerController.off('selectedSubjectsChange')
54. this.visionImageAnalyzerController.off('analyzerFailed')
55. }
56. }
```
