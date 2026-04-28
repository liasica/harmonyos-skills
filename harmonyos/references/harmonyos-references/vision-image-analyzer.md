---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vision-image-analyzer
title: visionImageAnalyzer（AI识图控件）
breadcrumb: API参考 > AI > Vision Kit（场景化视觉服务） > ArkTS API > visionImageAnalyzer（AI识图控件）
category: harmonyos-references
scraped_at: 2026-04-28T08:19:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dd913baa54bed646ad1bd4fb7b40f41e856d9c2045a84455c6f40a94dcefb0ed
---

AI识图是通过聚合OCR（Optical Character Recognition）、主体分割、实体识别、多目标识别等AI能力，提供场景化的文本识别、主体分割、识图搜索功能。

说明

调用接口需捕获异常。

**起始版本：** 5.0.0(12)

## 导入模块

PhonePC/2in1Tablet

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';
```

## Menu

PhonePC/2in1Tablet

AI识图菜单。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 菜单内容。 |
| action | [Callback](js-apis-base.md#callback)<string | [Subject](vision-image-analyzer.md#subject)[]> | 否 | 否 | 菜单结果回调，包含文字选中结果和抠图结果。 |

## Rect

PhonePC/2in1Tablet

矩形数据结构。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 是 | 矩形的左方位置。取值范围在图片的左边界到右边界之间。单位：vp。 |
| top | number | 否 | 是 | 矩形的上方位置。取值范围在图片的上边界到下边界之间。单位：vp。 |
| right | number | 否 | 是 | 矩形的右方位置。取值范围在图片的左边界到右边界之间。单位：vp。 |
| bottom | number | 否 | 是 | 矩形的下方位置。取值范围在图片的上边界到下边界之间。单位：vp。 |

## Subject

PhonePC/2in1Tablet

主体识别结果。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 否 | 否 | 主体id。取值范围：[0，6]。 |
| image | [PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 主体识别的图片。 |
| boundingBox | [Rect](vision-image-analyzer.md#rect) | 否 | 否 | 主体识别图片结果的外接矩形框。 |
| maskData | Int32Array | 否 | 是 | 基于原图大小的一维数组，表示主体掩码。0-255取值范围。0代表背景，255代表主体，中间值代表是否是显著性主体的概率。  **起始版本**：5.1.0(18)。  **说明：**  maskData参数数据可能较大，通过JSON.stringify()方法解析打印日志会比较耗时，可能会影响接口性能，请按需打印。 |

## SelectedStatus

PhonePC/2in1Tablet

识图对象选中状态的枚举值。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECTED | 0 | 选中状态。 |
| UNSELECTED | 1 | 未选中状态。 |

## ImageAnalyzerVisibility

PhonePC/2in1Tablet

AI识图控件可见状态的枚举值。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOWN | 0 | AI识图控件的可见状态。 |
| HIDDEN | 1 | AI识图控件的不可见状态。 |

## AIButtonStatus

PhonePC/2in1Tablet

AIButton状态的枚举值。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECTED | 0 | AIButton选中状态。 |
| UNSELECTED | 1 | AIButton未选中状态。 |
| HIDDEN | 2 | AIButton隐藏状态。 |

## ObjectSearchPanelVisibility

PhonePC/2in1Tablet

图片搜索界面可见状态的枚举值。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SHOW | 0 | 图片搜索界面的可见状态。 |
| HIDE | 1 | 图片搜索界面的不可见状态。 |

## ImageAnalyzerUIStatus

PhonePC/2in1Tablet

图片分析界面状态的枚举值。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.2(14)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INITIAL | 0 | 初始化状态。 |
| AI\_BUTTON\_SELECTED | 1 | AIButton选中状态。 |
| TEXT\_SELECTED | 2 | 文字选中状态。 |
| SUBJECT\_SELECTED | 3 | 主体选中状态。 |
| OBJECT\_SEARCH | 4 | 视觉搜索状态。 |

## VisionImageAnalyzerController

PhonePC/2in1Tablet

这是视觉图像控制器，用于控制交互。继承自[ImageAnalyzerController](ts-image-common.md#imageanalyzercontroller12)类。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

### setImageAnalyzerVisibility

PhonePC/2in1Tablet

setImageAnalyzerVisibility(visibility: ImageAnalyzerVisibility): void

设置AI识图控件的可见性。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visibility | [ImageAnalyzerVisibility](vision-image-analyzer.md#imageanalyzervisibility) | 是 | AI识图控件的可见性。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear() {
9. this.visionImageAnalyzerController.setImageAnalyzerVisibility(visionImageAnalyzer.ImageAnalyzerVisibility.HIDDEN)
10. }
11. build() {
12. Stack() {
13. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
14. Image($r('app.media.img'), {
15. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
16. aiController: this.visionImageAnalyzerController
17. })
18. .width('100%')
19. .height('100%')
20. .enableAnalyzer(true)
21. .objectFit(ImageFit.Contain)
22. }.width('100%').height('100%')
23. }
24. }
```

### setAIButtonPosition

PhonePC/2in1Tablet

setAIButtonPosition(position: Rect): void

设置AIButton的位置。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Rect](vision-image-analyzer.md#rect) | 是 | AIButton区域距离AI识图控件四边的位置（vp）。默认展示在右下角 。  当传入部分参数时，优先按照传入的参数匹配，如果位置参数异常，使用默认位置展示。  同时设置top及bottom参数，调setAIButtonPosition接口仅top参数生效。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear() {
9. let position: visionImageAnalyzer.Rect = {
10. bottom: 300
11. }
12. this.visionImageAnalyzerController.setAIButtonPosition(position)
13. this.visionImageAnalyzerController.setAIButtonVisibility(true)
14. }
15. build() {
16. Stack() {
17. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
18. Image($r('app.media.6'), {
19. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
20. aiController: this.visionImageAnalyzerController
21. })
22. .width('100%')
23. .height('100%')
24. .enableAnalyzer(true)
25. .objectFit(ImageFit.Contain)
26. }.width('100%').height('100%')
27. }
28. }
```

### setAIButtonVisibility

PhonePC/2in1Tablet

setAIButtonVisibility(visible: boolean): void

设置AIButton的可见性。配置AIButton属性可见后，会对图片进行预分析，当图片中存在文本且文本区域大于图片区域的5%时AIButton才会显示。开启AIButton会触发图片的预分析从而导致一定的功耗开销，建议评估场景，对图片中文本内容较为关注的场景下按需开启，带给消费者良好的图片浏览体验的同时降低不必要的功耗开销。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | AIButton的可见性。true表示可见，false表示不可见。  默认为false，隐藏AIButton。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear() {
9. this.visionImageAnalyzerController.setAIButtonVisibility(true)
10. }
11. build() {
12. Stack() {
13. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
14. Image($r('app.media.img'), {
15. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
16. aiController: this.visionImageAnalyzerController
17. })
18. .width('100%')
19. .height('100%')
20. .enableAnalyzer(true)
21. .objectFit(ImageFit.Contain)
22. }.width('100%').height('100%')
23. }
24. }
```

### setCustomTextMenuItems

PhonePC/2in1Tablet

setCustomTextMenuItems(menus: Menu[]): void

设置自定义的文字分析菜单项。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| menus | [Menu](vision-image-analyzer.md#menu)[] | 是 | 选中文字时，支持在文字菜单上增加自定义菜单项，回调中包含当前选中的文字结果。  最多只展示三个，超过三个时取前三个。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear() {
9. this.visionImageAnalyzerController.setAIButtonVisibility(true)
10. this.visionImageAnalyzerController.setCustomTextMenuItems([
11. {
12. value: "menu2",
13. action: (param: string | visionImageAnalyzer.Subject[]) => {
14. console.info("DEMO_TAG", "text menu clicked")
15. }
16. }
17. ]
18. )
19. }
20. build() {
21. Stack() {
22. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
23. Image($r('app.media.img'), {
24. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
25. aiController: this.visionImageAnalyzerController
26. })
27. .width('100%')
28. .height('100%')
29. .enableAnalyzer(true)
30. .objectFit(ImageFit.Contain)
31. }.width('100%').height('100%')
32. }
33. }
```

### startSubjectAnalyzer

PhonePC/2in1Tablet

startSubjectAnalyzer(): void

开启主体识别，前提需确保当前设备支持主体识别功能。可通过监听 “subjectAnalysis”事件回调获取主体, 注意在等待返回主体时增加超时处理，避免因未识别到主体而一直处于等待状态。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear() {
9. let supportTypes = this.visionImageAnalyzerController.getImageAnalyzerSupportTypes();
10. if (supportTypes.includes(ImageAnalyzerType.SUBJECT)) {
11. this.visionImageAnalyzerController.startSubjectAnalyzer()
12. }
13. }
14. build() {
15. Stack() {
16. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
17. Image($r('app.media.img'), {
18. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
19. aiController: this.visionImageAnalyzerController
20. })
21. .width('100%')
22. .height('100%')
23. .enableAnalyzer(true)
24. .objectFit(ImageFit.Contain)
25. }.width('100%').height('100%')
26. }
27. }
```

### setCustomSubjectMenuItems

PhonePC/2in1Tablet

setCustomSubjectMenuItems(menus: Menu[]): void

设置自定义的主体分析菜单项。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| menus | [Menu](vision-image-analyzer.md#menu)[] | 是 | 选中主体时，支持在主体菜单上增加自定义菜单项，回调中包含当前选中的主体结果。  最多只展示三个，超过部分取前三个。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear() {
9. this.visionImageAnalyzerController.setCustomSubjectMenuItems([
10. {
11. value: "menu2",
12. action: (param: string | visionImageAnalyzer.Subject[]) => {
13. console.info("DEMO_TAG", "subject menu clicked")
14. }
15. }
16. ]
17. )
18. }
19. build() {
20. Stack() {
21. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
22. Image($r('app.media.img'), {
23. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
24. aiController: this.visionImageAnalyzerController
25. })
26. .width('100%')
27. .height('100%')
28. .enableAnalyzer(true)
29. .objectFit(ImageFit.Contain)
30. }.width('100%').height('100%')
31. }
32. }
```

### setSelectedSubjects

PhonePC/2in1Tablet

setSelectedSubjects(subjectIds: number[]): void

根据主体id列表设置选中的主体。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subjectIds | number[] | 是 | 要选中的主体id列表。通过[getSubject](vision-image-analyzer.md#getsubject)获取，只有图片识别结果中包含的主体id才有效。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct SingleImageTest2 {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear() {
9. this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
10. console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
11. if(subjects.length > 0) {
12. this.visionImageAnalyzerController.setSelectedSubjects([subjects[0].id])
13. }
14. })
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### getSelectedSubjects

PhonePC/2in1Tablet

getSelectedSubjects(): Promise<Subject[] | null>

获取当前选中的主体。使用Promise异步回调。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Subject](vision-image-analyzer.md#subject)[] | null> | Promise对象，返回当前选中的主体。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. getSelectedSubjects() {
9. void this.visionImageAnalyzerController.getSelectedSubjects().then((subjects: visionImageAnalyzer.Subject[] | null) => {
10. console.info("DEMO_TAG", `getSelectedSubjects result: ${JSON.stringify(subjects)}`)
11. })
12. }
13. build() {
14. Stack() {
15. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
16. Image($r('app.media.img'), {
17. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
18. aiController: this.visionImageAnalyzerController
19. })
20. .width('100%')
21. .height('100%')
22. .enableAnalyzer(true)
23. .objectFit(ImageFit.Contain)
24. }.width('100%').height('100%')
25. }
26. }
```

### getSubject

PhonePC/2in1Tablet

getSubject(point: visionBase.Point): Promise<Subject | null>

根据点位获取对应位置的主体。使用Promise异步回调。调用此接口前需先调用[startSubjectAnalyzer](vision-image-analyzer.md#startsubjectanalyzer)开启主体识别。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [visionBase.Point](core-vision-vision-base-api.md#section1465431712919) | 是 | 相对于图片左上角位置点位（px）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Subject](vision-image-analyzer.md#subject) | null> | Promise对象，point点位所在的主体。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';
2. import { visionBase } from '@kit.CoreVisionKit';

4. @Entry
5. @Component
6. struct ImageDemo {
7. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController = new visionImageAnalyzer.VisionImageAnalyzerController()
8. getSelectedSubjects() {
9. let searchPoint: visionBase.Point = { x: 100, y: 100 }
10. void this.visionImageAnalyzerController.getSubject(searchPoint).then((subjects: visionImageAnalyzer.Subject | null) => {
11. console.info("DEMO_TAG", `getSubject result: ${JSON.stringify(subjects)}`)
12. })
13. }
14. build() {
15. Stack() {
16. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
17. Image($r('app.media.img'), {
18. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
19. aiController: this.visionImageAnalyzerController
20. })
21. .width('100%')
22. .height('100%')
23. .enableAnalyzer(true)
24. .objectFit(ImageFit.Contain)
25. }.width('100%').height('100%')
26. }
27. }
```

### getSubjectsImage

PhonePC/2in1Tablet

getSubjectsImage(subjectIds: number[]): Promise<PixelMap | null>

根据主体id获取对应主体组装成的图像。使用Promise异步回调。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| subjectIds | number[] | 是 | 主体id列表。通过[getSubject](vision-image-analyzer.md#getsubject)获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PixelMap](arkts-apis-image-pixelmap.md) | null> | Promise对象，对应id列表组装成的图片。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. getSubjectsImage() {
9. this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
10. console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
11. if(subjects.length > 0) {
12. let ids: number[] = [subjects[0].id]
13. this.visionImageAnalyzerController.getSubjectsImage(ids).then((image: PixelMap | null) => {
14. console.info('Image data obtained successfully: ', image);
15. }).catch((error: Error) => {
16. console.error('Failed to obtain image data: ', error);
17. })
18. }
19. })
20. }
21. build() {
22. Stack() {
23. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
24. Image($r('app.media.img'), {
25. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
26. aiController: this.visionImageAnalyzerController
27. })
28. .width('100%')
29. .height('100%')
30. .enableAnalyzer(true)
31. .objectFit(ImageFit.Contain)
32. }.width('100%').height('100%')
33. }
34. }
```

### getImageAnalyzerUIStatus

PhonePC/2in1Tablet

getImageAnalyzerUIStatus(): Promise<ImageAnalyzerUIStatus>

获取当前图片分析UI状态。使用Promise异步回调。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.2(14)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ImageAnalyzerUIStatus](vision-image-analyzer.md#imageanalyzeruistatus)> | Promise对象，当前图片分析UI状态。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear() {
9. this.visionImageAnalyzerController.setAIButtonVisibility(true);
10. this.visionImageAnalyzerController.on('objectSearchPanelVisibilityChange', (objectSearchPanelVisibility: visionImageAnalyzer.ObjectSearchPanelVisibility) => {
11. this.visionImageAnalyzerController.getImageAnalyzerUIStatus().then((status: visionImageAnalyzer.ImageAnalyzerUIStatus) => {
12. console.info('Image data obtained successfully: ', status);
13. }).catch((error: Error) => {
14. console.error('Failed to obtain image data: ', error);
15. })
16. })
17. }
18. build() {
19. Stack() {
20. Image($r('app.media.img'), {
21. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
22. aiController: this.visionImageAnalyzerController
23. })
24. .width('100%')
25. .height('60%')
26. .enableAnalyzer(true)
27. .objectFit(ImageFit.Contain)

29. Button('获取当前图片分析UI状态', { stateEffect: true, type: ButtonType.Capsule })
30. .width('80%')
31. .height(40)
32. .onClick(() => {
33. this.visionImageAnalyzerController.getImageAnalyzerUIStatus()
34. .then((status: visionImageAnalyzer.ImageAnalyzerUIStatus) => {
35. console.info('Image data obtained successfully: ', status);
36. })
37. .catch((error: Error) => {
38. console.error('Failed to obtain image data: ', error);
39. })
40. })
41. .id('getImageAnalyzerUIStatus')
42. .width('40%')
43. }.width('100%').height('100%')
44. }
45. }
```

### startObjectSearch

PhonePC/2in1Tablet

startObjectSearch(): Promise<boolean>

开启视觉搜索。使用Promise异步回调。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**设备行为差异：** 该接口在PC/2in1上无效果，在其他设备类型中可正常调用。

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回是否开启视觉搜索。true表示开启视觉搜索，false表示关闭视觉搜索。在文字选择或主体识别状态时拉起会返回false。  **说明：**  视觉搜索若在[Swiper](ts-container-swiper.md)容器切换图场景下无法生效，则需要在图片切换的[onAnimationStart](ts-container-swiper.md#onanimationstart9)中置空一下当前选中图片的index，再由[onAnimationEnd](ts-container-swiper.md#onanimationend9)时将当前选中index置成当前index，以此实现overlay跟随图片变动而变动。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. startObjectSearch() {
9. this.visionImageAnalyzerController.startObjectSearch()
10. }
11. build() {
12. Stack() {
13. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
14. Image($r('app.media.img'), {
15. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
16. aiController: this.visionImageAnalyzerController
17. })
18. .width('100%')
19. .height('100%')
20. .enableAnalyzer(true)
21. .objectFit(ImageFit.Contain)
22. }.width('100%').height('100%')
23. }
24. }
```

### stopObjectSearch

PhonePC/2in1Tablet

stopObjectSearch(): void

关闭视觉搜索功能。 如果当前在视觉搜索交互状态，则不支持关闭。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**设备行为差异：** 该接口在PC/2in1上无效果，在其他设备类型中可正常调用。

**起始版本：** 5.0.0(12)

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. stopObjectSearch() {
9. this.visionImageAnalyzerController.stopObjectSearch()
10. }
11. build() {
12. Stack() {
13. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
14. Image($r('app.media.img'), {
15. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
16. aiController: this.visionImageAnalyzerController
17. })
18. .width('100%')
19. .height('100%')
20. .enableAnalyzer(true)
21. .objectFit(ImageFit.Contain)
22. }.width('100%').height('100%')
23. }
24. }
```

### setSubjectMenuVisibility

PhonePC/2in1Tablet

setSubjectMenuVisibility(visible: boolean): void

设置图像分割菜单状态。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 设置图像分割菜单状态。  true：显示图像分割菜单；false：隐藏图像分割菜单。  默认是true。 |

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. setSubjectMenuVisibility(visible: boolean) {
9. this.visionImageAnalyzerController.setSubjectMenuVisibility(visible)
10. }
11. build() {
12. Stack() {
13. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
14. Image($r('app.media.img'), {
15. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
16. aiController: this.visionImageAnalyzerController
17. })
18. .width('100%')
19. .height('100%')
20. .enableAnalyzer(true)
21. .objectFit(ImageFit.Contain)
22. }.width('100%').height('100%')
23. }
24. }
```

### on(type: 'aiButtonStatusChange')

PhonePC/2in1Tablet

on(type: 'aiButtonStatusChange', callback: Callback<AIButtonStatus>): void

监听AIButton展示状态。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"aiButtonStatusChange"。监听AIButton展示状态。 |
| callback | [Callback](js-apis-base.md#callback)<[AIButtonStatus](vision-image-analyzer.md#aibuttonstatus)> | 是 | callback回调函数。接收AIButton展示状态。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController?.setAIButtonVisibility(true)
10. this.visionImageAnalyzerController.on('aiButtonStatusChange', (aiButtonState: visionImageAnalyzer.AIButtonStatus) => {
11. console.info("DEMO_TAG", `aiButtonStatusChange result: ${JSON.stringify(aiButtonState)}`)
12. })
13. }
14. build() {
15. Stack() {
16. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
17. Image($r('app.media.img'), {
18. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
19. aiController: this.visionImageAnalyzerController
20. })
21. .width('100%')
22. .height('100%')
23. .enableAnalyzer(true)
24. .objectFit(ImageFit.Contain)
25. }.width('100%').height('100%')
26. }
27. }
```

### off(type: 'aiButtonStatusChange')

PhonePC/2in1Tablet

off(type: 'aiButtonStatusChange', callback?: Callback<AIButtonStatus>): void

取消监听AIButton展示状态。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"aiButtonStatusChange"。取消监听AIButton展示状态。 |
| callback | [Callback](js-apis-base.md#callback)<[AIButtonStatus](vision-image-analyzer.md#aibuttonstatus)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController?.setAIButtonVisibility(true)
10. this.visionImageAnalyzerController.on('aiButtonStatusChange', (aiButtonState: visionImageAnalyzer.AIButtonStatus) => {
11. console.info("DEMO_TAG", `aiButtonStatusChange result: ${JSON.stringify(aiButtonState)}`)
12. })
13. }
14. aboutToDisappear(): void {
15. this.visionImageAnalyzerController.off('aiButtonStatusChange')
16. }
17. build() {
18. Stack() {
19. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
20. Image($r('app.media.img'), {
21. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
22. aiController: this.visionImageAnalyzerController
23. })
24. .width('100%')
25. .height('100%')
26. .enableAnalyzer(true)
27. .objectFit(ImageFit.Contain)
28. }.width('100%').height('100%')
29. }
30. }
```

### on(type: 'imageAnalyzerVisibilityChange')

PhonePC/2in1Tablet

on(type: 'imageAnalyzerVisibilityChange', callback: Callback<ImageAnalyzerVisibility>): void

监听AI识图控件可见状态。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"imageAnalyzerVisibilityChange"。监听AI识图控件可见状态。 |
| callback | [Callback](js-apis-base.md#callback)<[ImageAnalyzerVisibility](vision-image-analyzer.md#imageanalyzervisibility)> | 是 | callback回调函数。接收AI识图控件可见状态。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController?.setAIButtonVisibility(true)
10. this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
11. console.info("DEMO_TAG", `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`)
12. })
13. }
14. aboutToDisappear(): void {
15. this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
16. }
17. build() {
18. Stack() {
19. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
20. Image($r('app.media.img'), {
21. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
22. aiController: this.visionImageAnalyzerController
23. })
24. .width('100%')
25. .height('100%')
26. .enableAnalyzer(true)
27. .objectFit(ImageFit.Contain)
28. }.width('100%').height('100%')
29. }
30. }
```

### off(type: 'imageAnalyzerVisibilityChange')

PhonePC/2in1Tablet

off(type: 'imageAnalyzerVisibilityChange', callback?: Callback<ImageAnalyzerVisibility>): void

取消AI识图控件可见状态的监听。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"imageAnalyzerVisibilityChange"。取消AI识图控件可见状态的监听。 |
| callback | [Callback](js-apis-base.md#callback)<[ImageAnalyzerVisibility](vision-image-analyzer.md#imageanalyzervisibility)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController?.setAIButtonVisibility(true)
10. this.visionImageAnalyzerController.on('imageAnalyzerVisibilityChange', (visibility: visionImageAnalyzer.ImageAnalyzerVisibility) => {
11. console.info("DEMO_TAG", `imageAnalyzerVisibilityChange result: ${JSON.stringify(visibility)}`)
12. })
13. }
14. aboutToDisappear(): void {
15. this.visionImageAnalyzerController.off('imageAnalyzerVisibilityChange')
16. }
17. build() {
18. Stack() {
19. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
20. Image($r('app.media.img'), {
21. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
22. aiController: this.visionImageAnalyzerController
23. })
24. .width('100%')
25. .height('100%')
26. .enableAnalyzer(true)
27. .objectFit(ImageFit.Contain)
28. }.width('100%').height('100%')
29. }
30. }
```

### on(type: 'textAnalysis')

PhonePC/2in1Tablet

on(type: 'textAnalysis', callback: Callback<string>): void

监听文字分析结果。默认在首次长按图片文本时触发文本分析，PC/2in1是在图片首次加载时触发文本分析。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"textAnalysis"。监听文字分析结果。 |
| callback | [Callback](js-apis-base.md#callback)<string> | 是 | callback回调函数。接收文字分析结果。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
10. console.info("DEMO_TAG", `textAnalysis result: ${JSON.stringify(text)}`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('textAnalysis')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### off(type: 'textAnalysis')

PhonePC/2in1Tablet

off(type: 'textAnalysis', callback?: Callback<string>): void

取消文字分析结果的监听。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"textAnalysis"。取消文字分析结果的监听。 |
| callback | [Callback](js-apis-base.md#callback)<string> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('textAnalysis', (text: string) => {
10. console.info("DEMO_TAG", `textAnalysis result: ${JSON.stringify(text)}`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('textAnalysis')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### on(type: 'selectedTextChange')

PhonePC/2in1Tablet

on(type: 'selectedTextChange', callback: Callback<string>): void

监听文字选中结果。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"selectedTextChange"。监听文字选中结果。 |
| callback | [Callback](js-apis-base.md#callback)<string> | 是 | callback回调函数。接收文字选中结果。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
10. console.info("DEMO_TAG", `selectedTextChange result: ${JSON.stringify(selectedText)}`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('selectedTextChange')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### off(type: 'selectedTextChange')

PhonePC/2in1Tablet

off(type: 'selectedTextChange', callback?: Callback<string>): void

取消文字选中结果的监听。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"selectedTextChange"。取消文字选中结果的监听。 |
| callback | [Callback](js-apis-base.md#callback)<string> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('selectedTextChange', (selectedText: string) => {
10. console.info("DEMO_TAG", `selectedTextChange result: ${JSON.stringify(selectedText)}`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('selectedTextChange')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### on(type: 'subjectAnalysis')

PhonePC/2in1Tablet

on(type: 'subjectAnalysis', callback: Callback<Subject[]>): void

监听主体分析结果，返回所有主体信息。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"subjectAnalysis"。监听主体分析结果， 返回所有主体信息。 |
| callback | [Callback](js-apis-base.md#callback)<[Subject](vision-image-analyzer.md#subject)[]> | 是 | callback回调函数。接收主体分析结果， 返回所有主体信息。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
10. console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('subjectAnalysis')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### off(type: 'subjectAnalysis')

PhonePC/2in1Tablet

off(type: 'subjectAnalysis', callback?: Callback<Subject[]>): void

取消主体分析结果的监听。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"subjectAnalysis"。取消主体分析结果的监听。 |
| callback | [Callback](js-apis-base.md#callback)<[Subject](vision-image-analyzer.md#subject)[]> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('subjectAnalysis', (subjects: visionImageAnalyzer.Subject[]) => {
10. console.info("DEMO_TAG", `subjectAnalysis result: ${JSON.stringify(subjects)}`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('subjectAnalysis')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### on(type: 'selectedSubjectsChange')

PhonePC/2in1Tablet

on(type: 'selectedSubjectsChange', callback: Callback<Subject[]>): void

监听选中的主体。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"selectedSubjectsChange"。监听选中的主体。 |
| callback | [Callback](js-apis-base.md#callback)<[Subject](vision-image-analyzer.md#subject)[]> | 是 | callback回调函数。接收选中的主体信息。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
10. console.info("DEMO_TAG", `selectedSubjectsChange result: ${JSON.stringify(subjects)}`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('selectedSubjectsChange')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### off(type: 'selectedSubjectsChange')

PhonePC/2in1Tablet

off(type: 'selectedSubjectsChange', callback?: Callback<Subject[]>): void

取消对选中主体的监听。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"selectedSubjectsChange"。取消对选中主体的监听。 |
| callback | [Callback](js-apis-base.md#callback)<[Subject](vision-image-analyzer.md#subject)[]> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('selectedSubjectsChange', (subjects: visionImageAnalyzer.Subject[]) => {
10. console.info("DEMO_TAG", `selectedSubjectsChange result: ${JSON.stringify(subjects)}`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('selectedSubjectsChange')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### on(type: 'objectSearchPanelVisibilityChange')

PhonePC/2in1Tablet

on(type: 'objectSearchPanelVisibilityChange', callback: Callback<ObjectSearchPanelVisibility>): void

监听图片搜索事件。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"objectSearchPanelVisibilityChange"。监听图片搜索事件。 |
| callback | [Callback](js-apis-base.md#callback)<[ObjectSearchPanelVisibility](vision-image-analyzer.md#objectsearchpanelvisibility)> | 是 | callback回调函数。接收图片搜索事件信息。 |

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('objectSearchPanelVisibilityChange', (status: visionImageAnalyzer.ObjectSearchPanelVisibility) => {
10. console.info("DEMO_TAG", `objectSearchPanelVisibilityChange result: ${JSON.stringify(status)}`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('objectSearchPanelVisibilityChange')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### off(type: 'objectSearchPanelVisibilityChange')

PhonePC/2in1Tablet

off(type: 'objectSearchPanelVisibilityChange', callback?: Callback<ObjectSearchPanelVisibility>): void

取消图片搜索事件的监听。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"objectSearchPanelVisibilityChange"。取消监听图片搜索事件。 |
| callback | [Callback](js-apis-base.md#callback)<[ObjectSearchPanelVisibility](vision-image-analyzer.md#objectsearchpanelvisibility)> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('objectSearchPanelVisibilityChange', (status: visionImageAnalyzer.ObjectSearchPanelVisibility) => {
10. console.info("DEMO_TAG", `objectSearchPanelVisibilityChange result: ${JSON.stringify(status)}`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('objectSearchPanelVisibilityChange')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### on(type: 'cursorMoveInText')

PhonePC/2in1Tablet

on(type: 'cursorMoveInText', callback: Callback<void>): void

监听光标移入图片内文字区域事件。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"cursorMoveInText"。监听光标移入图片内文字区域事件。 |
| callback | [Callback](js-apis-base.md#callback)<void> | 是 | callback回调函数。接收光标移入图片内文字区域事件信息。 |

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('cursorMoveInText', () => {
10. console.info("DEMO_TAG", `cursorMoveInText on`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('cursorMoveInText')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### off(type: 'cursorMoveInText')

PhonePC/2in1Tablet

off(type: 'cursorMoveInText', callback?: Callback<void>): void

取消光标移入图片内文字区域事件的监听。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"cursorMoveInText"。取消监听光标移入图片内文字区域事件。 |
| callback | [Callback](js-apis-base.md#callback)<void> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('cursorMoveInText', () => {
10. console.info("DEMO_TAG", `cursorMoveInText on`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('cursorMoveInText')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### on(type: 'cursorMoveOutText')

PhonePC/2in1Tablet

on(type: 'cursorMoveOutText', callback: Callback<void>): void

监听光标移出图片内文字区域事件。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"cursorMoveOutText"。监听光标移出图片内文字区域事件。 |
| callback | [Callback](js-apis-base.md#callback)<void> | 是 | callback回调函数。接收光标移出图片内文字区域事件信息。 |

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('cursorMoveOutText', () => {
10. console.info("DEMO_TAG", `cursorMoveOutText on`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('cursorMoveOutText')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### off(type: 'cursorMoveOutText')

PhonePC/2in1Tablet

off(type: 'cursorMoveOutText', callback?: Callback<void>): void

取消光标移出图片内文字区域事件的监听。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"cursorMoveOutText"。取消监听光标移出图片内文字区域事件。 |
| callback | [Callback](js-apis-base.md#callback)<void> | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';

3. @Entry
4. @Component
5. struct ImageDemo {
6. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
7. new visionImageAnalyzer.VisionImageAnalyzerController()
8. aboutToAppear(): void {
9. this.visionImageAnalyzerController.on('cursorMoveOutText', () => {
10. console.info("DEMO_TAG", `cursorMoveOutText on`)
11. })
12. }
13. aboutToDisappear(): void {
14. this.visionImageAnalyzerController.off('cursorMoveOutText')
15. }
16. build() {
17. Stack() {
18. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
19. Image($r('app.media.img'), {
20. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
21. aiController: this.visionImageAnalyzerController
22. })
23. .width('100%')
24. .height('100%')
25. .enableAnalyzer(true)
26. .objectFit(ImageFit.Contain)
27. }.width('100%').height('100%')
28. }
29. }
```

### on(type: 'analyzerFailed')

PhonePC/2in1Tablet

on(type: 'analyzerFailed', callback: ErrorCallback): void

监听AI识图的异常场景。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"analyzerFailed"。监听AI识图异常场景。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 是 | callback回调函数。接收AI识图异常场景信息。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1013700002 | The service is abnormal. |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct ImageDemo {
7. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
8. new visionImageAnalyzer.VisionImageAnalyzerController()
9. aboutToAppear(): void {
10. this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
11. console.error("DEMO_TAG", `analyzerFailed result: ${JSON.stringify(error)}`)
12. })
13. }
14. aboutToDisappear(): void {
15. this.visionImageAnalyzerController.off('analyzerFailed')
16. }
17. build() {
18. Stack() {
19. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
20. Image($r('app.media.img'), {
21. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
22. aiController: this.visionImageAnalyzerController
23. })
24. .width('100%')
25. .height('100%')
26. .enableAnalyzer(true)
27. .objectFit(ImageFit.Contain)
28. }.width('100%').height('100%')
29. }
30. }
```

### off(type: 'analyzerFailed')

PhonePC/2in1Tablet

off(type: 'analyzerFailed', callback?: ErrorCallback): void

取消AI识图异常场景的监听。

**系统能力：** SystemCapability.AI.VisionImageAnalyzer

**起始版本：** 5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 值为"analyzerFailed"。取消AI识图异常场景的监听。 |
| callback | [ErrorCallback](js-apis-base.md#errorcallback) | 否 | 需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 1013700002 | The service is abnormal. |

**示例：**

```
1. import { visionImageAnalyzer } from '@kit.VisionKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct ImageDemo {
7. private visionImageAnalyzerController: visionImageAnalyzer.VisionImageAnalyzerController =
8. new visionImageAnalyzer.VisionImageAnalyzerController()
9. aboutToAppear(): void {
10. this.visionImageAnalyzerController.on('analyzerFailed', (error: BusinessError) => {
11. console.error("DEMO_TAG", `analyzerFailed result: ${JSON.stringify(error)}`)
12. })
13. }
14. aboutToDisappear(): void {
15. this.visionImageAnalyzerController.off('analyzerFailed')
16. }
17. build() {
18. Stack() {
19. // 此处图片需单独配置，添加到src/main/resources/base/media路径下
20. Image($r('app.media.img'), {
21. types: [ImageAnalyzerType.TEXT, ImageAnalyzerType.SUBJECT, ImageAnalyzerType.OBJECT_LOOKUP],
22. aiController: this.visionImageAnalyzerController
23. })
24. .width('100%')
25. .height('100%')
26. .enableAnalyzer(true)
27. .objectFit(ImageFit.Contain)
28. }.width('100%').height('100%')
29. }
30. }
```
