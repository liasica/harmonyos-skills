---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-cardrecognition
title: 卡证识别
breadcrumb: 指南 > AI > Vision Kit（场景化视觉服务） > 卡证识别
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2576fa59bfa8bde7fee835e0f7bdc8b51bfda7879829a40d9776deec667c17a9
---

从5.1.1(19)开始，[CardRecognition](../harmonyos-references/vision-card-recognition.md#cardrecognition)接口中的callback参数废弃，请使用onResult代替。

## 场景介绍

卡证识别控件提供身份证（目前仅支持中国大陆二代身份证，且不包含民汉双文身份证）、行驶证、驾驶证、护照、银行卡的结构化识别服务，满足卡证的自动分类功能，系统可自动判断所属卡证类型并返回结构化信息和卡证图片信息。

对于需要填充卡证信息的场景，如身份证、银行卡信息等，可使用卡证识别控件读取OCR（Optical Character Recognition）信息，将结果信息返回后进行填充。支持单独识别正面、反面，或同时进行双面识别。

**图1** 银行卡识别示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/DpShCHJjTr-jymyHJ4zIcQ/zh-cn_image_0000002558606198.png?HW-CC-KV=V1&HW-CC-Date=20260429T054119Z&HW-CC-Expire=86400&HW-CC-Sign=F12274B4A136EB9DD93265B4D26E1B8ED1887573735EC7ABE7BA987732934609)

## 约束与限制

* 支持的语种类型：简体中文、英文。
* 卡证识别暂时只支持中国二代身份证、中国国内银行卡、中国护照、中国驾驶证、中国行驶证（暂不支持中国港澳台地区及海外证件）。
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

   ```
   1. import { CardRecognition, CardRecognitionResult, CardType, CardSide, CardRecognitionConfig, ShootingMode, CardContentConfig, BankCardConfig } from "@kit.VisionKit";
   ```
2. 配置页面的布局，选择需要识别的卡证类型和需要识别的卡证页面，配置对应设置项，在回调中获取结果返回值。

   以下分别为身份证、银行卡、护照、驾驶证和行驶证的示例代码。

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   3. const TAG = 'CardRecognition'

   5. @Entry
   6. @Component
   7. struct Index {
   8. build() {
   9. Column() {
   10. // 身份证
   11. CardRecognition({
   12. supportType: CardType.CARD_ID,
   13. // 身份证可双面识别
   14. cardSide: CardSide.DEFAULT,
   15. cardRecognitionConfig: {
   16. defaultShootingMode: ShootingMode.MANUAL,
   17. isPhotoSelectionSupported: true
   18. },
   19. onResult: ((params: CardRecognitionResult) => {
   20. hilog.info(0x0001, TAG, `params code: ${params.code}`)
   21. hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`)
   22. hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`)
   23. hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`)
   24. })
   25. })
   26. }
   27. .height('100%')
   28. .width('100%')
   29. }
   30. }
   ```

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   3. const TAG = 'CardRecognition'

   5. @Entry
   6. @Component
   7. struct Index {
   8. build() {
   9. Column() {
   10. // 银行卡
   11. CardRecognition({
   12. supportType: CardType.CARD_BANK,
   13. // 银行卡为单面识别
   14. cardSide: CardSide.FRONT,
   15. cardRecognitionConfig: {
   16. defaultShootingMode: ShootingMode.MANUAL,
   17. isPhotoSelectionSupported: true,
   18. cardContentConfig: { bankCard: { isBankNumberDialogShown: true} }
   19. },
   20. onResult: ((params: CardRecognitionResult) => {
   21. hilog.info(0x0001, TAG, `params code: ${params.code}`)
   22. hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`)
   23. hilog.info(0x0001, TAG, `params cardInfo: ${JSON.stringify(params.cardInfo?.main)}`)
   24. })})
   25. }
   26. .height('100%')
   27. .width('100%')
   28. }
   29. }
   ```

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   3. const TAG = 'CardRecognition'

   5. @Entry
   6. @Component
   7. struct Index {
   8. build() {
   9. Column() {
   10. // 护照
   11. CardRecognition({
   12. supportType: CardType.CARD_PASSPORT,
   13. // 护照为单面识别
   14. cardSide: CardSide.FRONT,
   15. cardRecognitionConfig: {
   16. defaultShootingMode: ShootingMode.MANUAL,
   17. isPhotoSelectionSupported: true
   18. },
   19. onResult: ((params: CardRecognitionResult) => {
   20. hilog.info(0x0001, TAG, `params code: ${params.code}`)
   21. hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`)
   22. hilog.info(0x0001, TAG, `params cardInfo: ${JSON.stringify(params.cardInfo?.main)}`)
   23. })})
   24. }
   25. .height('100%')
   26. .width('100%')
   27. }
   28. }
   ```

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   3. const TAG = 'CardRecognition'

   5. @Entry
   6. @Component
   7. struct Index {
   8. build() {
   9. Column() {
   10. // 驾驶证
   11. CardRecognition({
   12. supportType: CardType.CARD_DRIVER_LICENSE,
   13. // 驾驶证可双面识别
   14. cardSide: CardSide.DEFAULT,
   15. cardRecognitionConfig: {
   16. defaultShootingMode: ShootingMode.MANUAL,
   17. isPhotoSelectionSupported: true
   18. },
   19. onResult: ((params: CardRecognitionResult) => {
   20. hilog.info(0x0001, TAG, `params code: ${params.code}`)
   21. hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`)
   22. hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`)
   23. hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`)
   24. })
   25. })
   26. }
   27. .height('100%')
   28. .width('100%')
   29. }
   30. }
   ```

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';

   3. const TAG = 'CardRecognition'

   5. @Entry
   6. @Component
   7. struct Index {
   8. build() {
   9. Column() {
   10. // 行驶证
   11. CardRecognition({
   12. supportType: CardType.CARD_VEHICLE_LICENSE,
   13. // 行驶证可双面识别
   14. cardSide: CardSide.DEFAULT,
   15. cardRecognitionConfig: {
   16. defaultShootingMode: ShootingMode.MANUAL,
   17. isPhotoSelectionSupported: true
   18. },
   19. onResult: ((params: CardRecognitionResult) => {
   20. hilog.info(0x0001, TAG, `params code: ${params.code}`)
   21. hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`)
   22. hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`)
   23. hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`)
   24. })
   25. })
   26. }
   27. .height('100%')
   28. .width('100%')
   29. }
   30. }
   ```

## 开发实例

### Index.ets

```
1. // 卡证识别开发实例分两页实现，一页为卡证识别入口页，一页为卡证识别实现页
2. // 卡证识别入口页，需引入卡证识别实现页，以下文实例为例，实现页文件名为CardDemoPage
3. import { CardDemoPage } from './CardDemoPage'

5. @Entry
6. @Component
7. struct MainPage {
8. @Provide('pathStack') pathStack: NavPathStack = new NavPathStack()

10. @Builder
11. PageMap(name: string) {
12. if (name === 'cardRecognition') {
13. CardDemoPage()
14. }
15. }

17. // 卡证识别入口按钮
18. build() {
19. Navigation(this.pathStack) {
20. Button('CardRecognition', { stateEffect: true, type: ButtonType.Capsule })
21. .width('50%')
22. .height(40)
23. .onClick(() => {
24. this.pathStack.pushPath({ name: 'cardRecognition' })
25. })
26. }.title('卡证识别控件demo').navDestination(this.PageMap)
27. .mode(NavigationMode.Stack)
28. }
29. }
```

### CardDemoPage.ets

```
1. // 卡证识别实现页，文件名为CardDemoPage，需被引入至入口页
2. import { CardRecognition, CardRecognitionResult, CardType, CardSide, ShootingMode } from "@kit.VisionKit"
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG: string = 'CardRecognitionPage'

7. // 卡证识别页，用于加载UIExtensionAbility
8. @Component
9. export struct CardDemoPage {
10. @State cardDataSource: Record<string, string>[] = []
11. @Consume('pathStack') pathStack: NavPathStack

13. build() {
14. NavDestination() {
15. Stack({ alignContent: Alignment.Top }) {
16. Stack() {
17. this.cardDataShowBuilder()
18. }
19. .width('80%')
20. .height('80%')

22. CardRecognition({
23. // 此处选择身份证类型作为示例
24. supportType: CardType.CARD_ID,
25. cardSide: CardSide.DEFAULT,
26. cardRecognitionConfig: {
27. defaultShootingMode: ShootingMode.MANUAL,
28. isPhotoSelectionSupported: true
29. },
30. onResult: ((params: CardRecognitionResult) => {
31. hilog.info(0x0001, TAG, `params code: ${params.code}`)
32. if (params.code !== 200) {
33. this.pathStack.pop()
34. }
35. hilog.info(0x0001, TAG, `params cardType: ${params.cardType}`)
36. if (params.cardInfo?.front !== undefined) {
37. this.cardDataSource.push(params.cardInfo?.front)
38. }

40. if (params.cardInfo?.back !== undefined) {
41. this.cardDataSource.push(params.cardInfo?.back)
42. }

44. if (params.cardInfo?.main !== undefined) {
45. this.cardDataSource.push(params.cardInfo?.main)
46. }
47. hilog.info(0x0001, TAG, `params cardInfo front: ${JSON.stringify(params.cardInfo?.front)}`)
48. hilog.info(0x0001, TAG, `params cardInfo back: ${JSON.stringify(params.cardInfo?.back)}`)
49. })
50. })
51. }
52. .width('100%')
53. .height('100%')
54. }
55. .width('100%')
56. .height('100%')
57. .hideTitleBar(true)
58. }

60. @Builder
61. cardDataShowBuilder() {
62. List() {
63. ForEach(this.cardDataSource, (cardData: Record<string, string>) => {
64. ListItem() {
65. Column() {
66. Image(cardData.cardImageUri)
67. .objectFit(ImageFit.Contain)
68. .width(100)
69. .height(100)

71. Text(JSON.stringify(cardData))
72. .width('100%')
73. .fontSize(12)
74. }
75. }
76. })
77. }
78. .listDirection(Axis.Vertical)
79. .alignListItem(ListItemAlign.Center)
80. .margin({
81. top: 50
82. })
83. .width('100%')
84. .height('100%')
85. }
86. }
```
