---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-documentscanner
title: 文档扫描
breadcrumb: 指南 > AI > Vision Kit（场景化视觉服务） > 文档扫描
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7d87b184e056a4f550fde761219c1ad7eefd26c426bd2e332205175c65563986
---

## 场景介绍

文档扫描控件提供拍摄文档并转换为高清扫描件的服务。仅需拍摄文档，即可自动裁剪和优化，并支持图片、PDF格式保存和分享；同时支持拍摄或从图库选择图片识别表格，生成表格文档。

可广泛用于教育办公场景，扫描文档、票据、课堂PPT和书籍等输出图片/PDF供用户完成发送、存档等操作。

**图1** 文档扫描示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/usA5giFpRI-alLIxD8JKWQ/zh-cn_image_0000002552799704.png?HW-CC-KV=V1&HW-CC-Date=20260427T235354Z&HW-CC-Expire=86400&HW-CC-Sign=4093353F473F677BB8BE5AF567CB64FABD7330EC8CB362212C4063F4682C1627)

## 约束与限制

* 支持的语种类型：简体中文、英文。
* 文档扫描暂时只支持phone、tablet设备。
* 不允许被其他组件或窗口遮挡。

## 接口说明

以下仅列出demo中调用的部分主要接口，具体API说明详见[API参考](../harmonyos-references/vision-document-scanner.md)。

| 接口名 | 描述 |
| --- | --- |
| [DocumentScanner](../harmonyos-references/vision-document-scanner.md#documentscanner) | 文档扫描控件 |
| [DocumentScannerResultCallback](../harmonyos-references/vision-document-scanner.md#documentscannerresultcallback) | 文档扫描结果 |

## 开发步骤

1. 将文档扫描控件相关的类添加至工程。

   ```
   1. import { DocType, DocumentScanner, DocumentScannerConfig, SaveOption, FilterId, ShootingMode } from "@kit.VisionKit";
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 配置布局，根据业务场景配置文档扫描控件的相关属性，获取返回的文档图片uri列表。

   ```
   1. const TAG = 'DocumentScanner'

   3. @Entry
   4. @Component
   5. struct Index {
   6. private docScanConfig = new DocumentScannerConfig()

   8. aboutToAppear() {
   9. this.docScanConfig.supportType = [DocType.DOC, DocType.SHEET]
   10. this.docScanConfig.isGallerySupported = true
   11. this.docScanConfig.editTabs = []
   12. this.docScanConfig.maxShotCount = 3
   13. this.docScanConfig.defaultFilterId = FilterId.ORIGINAL
   14. this.docScanConfig.defaultShootingMode = ShootingMode.MANUAL
   15. this.docScanConfig.isShareable = true
   16. this.docScanConfig.originalUris = []
   17. }

   19. build() {
   20. Column() {
   21. DocumentScanner({
   22. scannerConfig: this.docScanConfig,
   23. onResult: (code: number, saveType: SaveOption, uris: string[]) => {
   24. hilog.info(0x0001, TAG, `result code: ${code}, save: ${saveType}`)
   25. uris.forEach(uriString => {
   26. hilog.info(0x0001, TAG, `uri: ${uriString}`)
   27. })
   28. }
   29. }).size({ width: '100%', height: '100%' })
   30. }
   31. .height('100%')
   32. .width('100%')
   33. }
   34. }
   ```

## 开发实例

### Index.ets

```
1. // 开发实例分两页实现，一页为文档扫描入口页，一页为文档扫描实现页
2. // 文档扫描入口页，需引入文档扫描实现页，以下文实例为例，实现页文件名为DocDemoPage
3. import { DocDemoPage } from './DocDemoPage'

5. @Entry
6. @Component
7. struct MainPage {
8. @Provide('pathStack') pathStack: NavPathStack = new NavPathStack()

10. @Builder
11. PageMap(name: string) {
12. if (name === 'documentScanner') {
13. DocDemoPage()
14. }
15. }

17. // 文档扫描入口按钮，可替换为业务入口
18. build() {
19. Navigation(this.pathStack) {
20. Button('DocumentScanner', { stateEffect: true, type: ButtonType.Capsule })
21. .width('50%')
22. .height(40)
23. .onClick(() => {
24. this.pathStack.pushPath({ name: 'documentScanner' })
25. })
26. }.title('文档扫描控件demo').navDestination(this.PageMap)
27. .mode(NavigationMode.Stack)
28. }
29. }
```

### DocDemoPage.ets

```
1. // 文档扫描实现页，文件名为DocDemoPage，需被引入至入口页
2. import {
3. DocType,
4. DocumentScanner,
5. DocumentScannerConfig,
6. SaveOption,
7. FilterId,
8. ShootingMode
9. } from "@kit.VisionKit"
10. import { hilog } from '@kit.PerformanceAnalysisKit';

12. const TAG: string = 'DocDemoPage'

14. // 文档扫描页，用于加载UIExtensionAbility
15. @Component
16. export struct DocDemoPage {
17. @State docImageUris: string[] = []
18. @Consume('pathStack') pathStack: NavPathStack
19. private docScanConfig = new DocumentScannerConfig()

21. aboutToAppear() {
22. this.docScanConfig.supportType = [DocType.DOC, DocType.SHEET]
23. this.docScanConfig.isGallerySupported = true
24. this.docScanConfig.editTabs = []
25. this.docScanConfig.maxShotCount = 3
26. this.docScanConfig.defaultFilterId = FilterId.ORIGINAL
27. this.docScanConfig.defaultShootingMode = ShootingMode.MANUAL
28. this.docScanConfig.isShareable = true
29. this.docScanConfig.originalUris = []
30. }

32. build() {
33. NavDestination() {
34. Stack({ alignContent: Alignment.Top }) {
35. // 展示文档扫描结果
36. List() {
37. ForEach(this.docImageUris, (uri: string) => {
38. ListItem() {
39. Image(uri)
40. .objectFit(ImageFit.Contain)
41. .width(100)
42. .height(100)
43. }
44. })
45. }
46. .listDirection(Axis.Vertical)
47. .alignListItem(ListItemAlign.Center)
48. .margin({
49. top: 50
50. })
51. .width('80%')
52. .height('80%')

54. // 文档扫描
55. DocumentScanner({
56. scannerConfig: this.docScanConfig,
57. onResult: (code: number, saveType: SaveOption, uris: string[]) => {
58. hilog.info(0x0001, TAG, `result code: ${code}, save: ${saveType}`)
59. if (code === -1) {
60. this.pathStack.pop()
61. }
62. uris.forEach(uriString => {
63. hilog.info(0x0001, TAG, `uri: ${uriString}`)
64. })
65. this.docImageUris = uris
66. }
67. })
68. .size({ width: '100%', height: '100%' })
69. }
70. .width('100%')
71. .height('100%')
72. }
73. .width('100%')
74. .height('100%')
75. .hideTitleBar(true)
76. }
77. }
```
