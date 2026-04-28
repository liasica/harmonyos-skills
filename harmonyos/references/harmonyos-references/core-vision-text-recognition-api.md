---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-vision-text-recognition-api
title: textRecognition（文字识别）
breadcrumb: API参考 > AI > Core Vision Kit（基础视觉服务） > ArkTS API > textRecognition（文字识别）
category: harmonyos-references
scraped_at: 2026-04-28T08:18:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d2587f52533b868afb0e83a9afece4f16593fc9fdae15df595ad062b59ded7a8
---

通用文字识别服务提供图像信息转换为字符信息的能力。通过拍照、扫描等光学输入方式，把各种票据、卡证、表格、报刊、书籍等印刷品文字转化为图像信息，再利用文字识别技术将图像信息转化为计算机等设备可以使用的字符信息，便于用户提取字符内容、屏幕坐标及外框。目前本服务支持识别的语言有：简体中文、英文、日文、韩文、繁体中文五种语言。

**起始版本：** 4.0.0(10)

## 导入模块

PhonePC/2in1Tablet

```
1. import { textRecognition } from '@kit.CoreVisionKit';
```

## TextRecognitionConfiguration

PhonePC/2in1Tablet

通用文本识别的配置项，用于配置是否支持朝向检测。

系统能力：SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isDirectionDetectionSupported | boolean | 否 | 是 | 表示是否支持文字朝向检测。  true：表示支持朝向检测；false：表示不支持朝向检测。  默认是true，支持朝向检测。如果能判断当前图片是正向的，则可考虑将该属性设置为false，以提升性能。 |

## VisionInfo

PhonePC/2in1Tablet

待识别的视觉信息，目前仅支持颜色数据格式为RGBA\_8888的[PixelMap](arkts-apis-image-pixelmap.md)类型的视觉信息。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 否 | 待识别的图片。  具体规格请参考[约束与限制](../harmonyos-guides/core-vision-introduction.md#约束与限制)。 |

## PixelPoint

PhonePC/2in1Tablet

指示像素点的位置。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 是 | 否 | 像素点横向x坐标。 |
| y | number | 是 | 否 | 像素点纵向y坐标。 |

## TextWord

PhonePC/2in1Tablet

描述一个单词的信息，包括内容，以及外框的坐标。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | 是 | 否 | 单词的文本内容。 |
| cornerPoints | Array<[PixelPoint](core-vision-text-recognition-api.md#pixelpoint)> | 是 | 否 | 以顺时针返回的单词外框位置点列表。 |

## TextLine

PhonePC/2in1Tablet

描述图像中的一行文本。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | 是 | 否 | 文本行的文本内容。 |
| cornerPoints | Array<[PixelPoint](core-vision-text-recognition-api.md#pixelpoint)> | 是 | 否 | 以顺时针返回该文本行的外框位置点列表。 |
| words | Array<[TextWord](core-vision-text-recognition-api.md#textword)> | 是 | 否 | 该行包含的单词信息。 |

## TextBlock

PhonePC/2in1Tablet

描述图像中的文本块。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | 是 | 否 | 段落的文本内容。 |
| lines | Array<[TextLine](core-vision-text-recognition-api.md#textline)> | 是 | 否 | 该段落包含的文本行内容。 |

## TextRecognitionResult

PhonePC/2in1Tablet

文本识别的结果信息，包括文本内容和坐标信息。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | string | 是 | 否 | 所识别的文本内容。 |
| blocks | Array<[TextBlock](core-vision-text-recognition-api.md#textblock)> | 是 | 否 | 文本内容中的具体段落信息。 |

## textRecognition.init

PhonePC/2in1Tablet

init(): Promise<boolean>

初始化文字识别服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回初始化是否成功。  true：初始化成功；false：初始化失败。 |

**示例：**

```
1. import { textRecognition } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function initAndReleaseOCR() {
5. // 初始化 OCR 服务
6. const initResult = await textRecognition.init();
7. hilog.info(0x0000, 'textRecognitionSample', `OCR service initialization result:${initResult}`);

9. if (initResult) {
10. hilog.info(0x0000, 'textRecognitionSample', 'OCR service initialized successfully');

12. // 这里可以添加使用 OCR 服务的代码
13. // 例如：await textRecognition.recognizeText(...);

15. // 使用完毕后，释放 OCR 服务
16. await textRecognition.release();
17. hilog.info(0x0000, 'textRecognitionSample', 'OCR service released successfully');
18. } else {
19. hilog.error(0x0000, 'textRecognitionSample', 'Failed to initialize OCR service');
20. }
21. }

23. @Entry
24. @Component
25. struct Page {

27. build() {
28. Column(){
29. Button('initAndReleaseOCR').onClick(() => {
30. // 调用函数
31. void initAndReleaseOCR();
32. })
33. }
34. }
35. }
```

## textRecognition.release

PhonePC/2in1Tablet

release(): Promise<void>

释放文字识别服务。使用Promise异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，释放接口无返回值。 |

**示例：**

```
1. import { textRecognition } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. async function initAndReleaseOCR() {
5. // 初始化 OCR 服务
6. const initResult = await textRecognition.init();
7. hilog.info(0x0000, 'textRecognitionSample', `OCR service initialization result:${initResult}`);

9. if (initResult) {
10. hilog.info(0x0000, 'textRecognitionSample', 'OCR service initialized successfully');

12. // 这里可以添加使用 OCR 服务的代码
13. // 例如：await textRecognition.recognizeText(...);

15. // 使用完毕后，释放 OCR 服务
16. await textRecognition.release();
17. hilog.info(0x0000, 'textRecognitionSample', 'OCR service released successfully');
18. } else {
19. hilog.error(0x0000, 'textRecognitionSample', 'Failed to initialize OCR service');
20. }
21. }

23. @Entry
24. @Component
25. struct Page {

27. build() {
28. Column(){
29. Button('initAndReleaseOCR').onClick(() => {
30. // 调用函数
31. void initAndReleaseOCR();
32. })
33. }
34. }
35. }
```

## textRecognition.recognizeText

PhonePC/2in1Tablet

recognizeText(visionInfo: VisionInfo, callback: AsyncCallback<TextRecognitionResult>): void

识别视觉信息内包含的文本。使用Callback异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo | [VisionInfo](core-vision-text-recognition-api.md#visioninfo) | 是 | 待识别的视觉信息。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<[TextRecognitionResult](core-vision-text-recognition-api.md#textrecognitionresult)> | 是 | 回调函数，返回文字识别的对象。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1001400001 | Failed to run, please try again. |
| 1001400002 | The service is abnormal. |

**示例：**

```
1. import { textRecognition } from '@kit.CoreVisionKit'
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. let imageSource: image.ImageSource | undefined = undefined;
9. let chooseImage: PixelMap | undefined = undefined;
10. // 将图片转换为PixelMap，可以通过图库获取
11. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
12. photoPicker.select({
13. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE, maxSelectNumber: 1
14. }).then((res: photoAccessHelper.PhotoSelectResult) => {
15. let uri = res.photoUris[0];
16. if (uri === undefined) {
17. hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
18. return;
19. }
20. setTimeout(async () => {
21. let fileSource = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
22. imageSource = image.createImageSource(fileSource.fd);
23. chooseImage = await imageSource.createPixelMap();
24. if (!chooseImage) {
25. return;
26. }

28. // 调用文本识别接口
29. let visionInfo: textRecognition.VisionInfo = {
30. pixelMap: chooseImage
31. };
32. textRecognition.recognizeText(visionInfo, (error: BusinessError, data: textRecognition.TextRecognitionResult) => {
33. if (error.code !== 0) {
34. hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
35. return;
36. }
37. // 识别成功，获取对应的结果
38. let recognitionString = JSON.stringify(data);
39. hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text: ${recognitionString}`);

41. if(chooseImage && imageSource) {
42. void chooseImage.release();
43. void imageSource.release();
44. }
45. });
46. if (fileSource) {
47. try {
48. await fileIo.close(fileSource);
49. } catch (err) {
50. hilog.error(0x0000, 'OCRDemo', `Failed to close fileSource. Code: ${err.code}, message: ${err.message}`);
51. }
52. }
53. }, 100)
54. }).catch((err: BusinessError) => {
55. hilog.error(0x0000, 'OCRDemo', `Failed to get photo image uri. Code: ${err.code}, message: ${err.message}`);
56. })

58. @Entry
59. @Component
60. struct Page {

62. build() {
63. Column(){
64. }
65. }
66. }
```

## textRecognition.recognizeText

PhonePC/2in1Tablet

recognizeText(visionInfo: VisionInfo, configuration ?: TextRecognitionConfiguration): Promise<TextRecognitionResult>

识别视觉信息内包含的文本，可以通过自定义配置项进行更详细的设置。使用Promise异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo | [VisionInfo](core-vision-text-recognition-api.md#visioninfo) | 是 | 待识别的视觉信息。 |
| configuration | [TextRecognitionConfiguration](core-vision-text-recognition-api.md#textrecognitionconfiguration) | 否 | 识别的配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[TextRecognitionResult](core-vision-text-recognition-api.md#textrecognitionresult)> | Promise对象，返回文字识别的结果对象。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1001400001 | Failed to run, please try again. |
| 1001400002 | The service is abnormal. |

**示例：**

```
1. import { textRecognition } from '@kit.CoreVisionKit'
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. let imageSource: image.ImageSource | undefined = undefined;
9. let chooseImage: PixelMap | undefined = undefined;
10. // 将图片转换为PixelMap，可以通过图库获取
11. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
12. photoPicker.select({
13. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE, maxSelectNumber: 1
14. }).then((res: photoAccessHelper.PhotoSelectResult) => {
15. let uri = res.photoUris[0];
16. if (uri === undefined) {
17. hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
18. return;
19. }
20. setTimeout(async () => {
21. let fileSource = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
22. imageSource = image.createImageSource(fileSource.fd);
23. chooseImage = await imageSource.createPixelMap();
24. if (!chooseImage) {
25. return;
26. }

28. // 调用文本识别接口
29. let visionInfo: textRecognition.VisionInfo = {
30. pixelMap: chooseImage
31. };
32. let recognitionResult = await textRecognition.recognizeText(visionInfo);

34. // 识别成功，获取对应的结果
35. let recognitionString = JSON.stringify(recognitionResult);
36. hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text: ${recognitionString}`);

38. if(chooseImage && imageSource) {
39. void chooseImage.release();
40. void imageSource.release();
41. }
42. if (fileSource) {
43. try {
44. await fileIo.close(fileSource);
45. } catch (err) {
46. hilog.error(0x0000, 'OCRDemo', `Failed to close fileSource. Code: ${err.code}, message: ${err.message}`);
47. }
48. }
49. }, 100)
50. }).catch((err: BusinessError) => {
51. hilog.error(0x0000, 'OCRDemo', `Failed to get photo image uri. Code: ${err.code}, message: ${err.message}`);
52. })

54. @Entry
55. @Component
56. struct Page {

58. build() {
59. Column(){
60. }
61. }
62. }
```

## textRecognition.recognizeText

PhonePC/2in1Tablet

recognizeText(visionInfo: VisionInfo, configuration: TextRecognitionConfiguration, callback: AsyncCallback<TextRecognitionResult>): void

通过自定义配置项对识别能力进行更详细的设置，识别视觉信息内包含的文本。使用Callback异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visionInfo | [VisionInfo](core-vision-text-recognition-api.md#visioninfo) | 是 | 待识别的视觉信息。 |
| configuration | [TextRecognitionConfiguration](core-vision-text-recognition-api.md#textrecognitionconfiguration) | 是 | 识别的配置项。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<[TextRecognitionResult](core-vision-text-recognition-api.md#textrecognitionresult)> | 是 | 识别结果的回调，可以用于界面显示或交互。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 200 | Run timed out, please try again later. |
| 401 | The parameter check failed. |
| 1001400001 | Failed to run, please try again. |
| 1001400002 | The service is abnormal. |

**示例：**

```
1. import { textRecognition } from '@kit.CoreVisionKit'
2. import { image } from '@kit.ImageKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { photoAccessHelper } from '@kit.MediaLibraryKit';

8. let imageSource: image.ImageSource | undefined = undefined;
9. let chooseImage: PixelMap | undefined = undefined;
10. // 将图片转换为PixelMap，可以通过图库获取
11. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();
12. photoPicker.select({
13. MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE, maxSelectNumber: 1
14. }).then((res: photoAccessHelper.PhotoSelectResult) => {
15. let uri = res.photoUris[0];
16. if (uri === undefined) {
17. hilog.error(0x0000, 'OCRDemo', 'Failed to get uri.');
18. return;
19. }
20. setTimeout(async () => {
21. let fileSource = await fileIo.open(uri, fileIo.OpenMode.READ_ONLY);
22. imageSource = image.createImageSource(fileSource.fd);
23. chooseImage = await imageSource.createPixelMap();
24. if (!chooseImage) {
25. return;
26. }

28. // 调用文本识别接口
29. let visionInfo: textRecognition.VisionInfo = {
30. pixelMap: chooseImage
31. };
32. let textConfiguration: textRecognition.TextRecognitionConfiguration = {
33. isDirectionDetectionSupported: false
34. };
35. textRecognition.recognizeText(visionInfo, textConfiguration, (error: BusinessError, data: textRecognition.TextRecognitionResult) => {
36. if (error.code !== 0) {
37. hilog.error(0x0000, 'OCRDemo', `Failed to recognize text. Code: ${error.code}, message: ${error.message}`);
38. return;
39. }
40. // 识别成功，获取对应的结果
41. let recognitionString = JSON.stringify(data);
42. hilog.info(0x0000, 'OCRDemo', `Succeeded in recognizing text: ${recognitionString}`);

44. if(chooseImage && imageSource) {
45. void chooseImage.release();
46. void imageSource.release();
47. }
48. });
49. if (fileSource) {
50. try {
51. await fileIo.close(fileSource);
52. } catch (err) {
53. hilog.error(0x0000, 'OCRDemo', `Failed to close fileSource. Code: ${err.code}, message: ${err.message}`);
54. }
55. }
56. }, 100)
57. }).catch((err: BusinessError) => {
58. hilog.error(0x0000, 'OCRDemo', `Failed to get photo image uri. Code: ${err.code}, message: ${err.message}`);
59. })

61. @Entry
62. @Component
63. struct Page {

65. build() {
66. Column(){
67. }
68. }
69. }
```

## textRecognition.getSupportedLanguages

PhonePC/2in1Tablet

getSupportedLanguages(): Promise<Array<string>>

获取当前文本识别所支持的语言类型列表。使用Promise异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回所支持的[语言类型列表](core-vision-text-recognition-api.md#语言类型列表)。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1001400001 | Failed to run, please try again. |
| 1001400002 | The service is abnormal. |

**示例：**

```
1. import { textRecognition } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. textRecognition.getSupportedLanguages().then((data: Array<string>) => {
6. let languageString = data.join(', ');
7. hilog.info(0x0000, 'OCRDemo', `Succeeded in obtaining the language: ${languageString}`);
8. }, (err: BusinessError) => {
9. hilog.error(0x0000, 'OCRDemo', `Failed to obtain the language. Code: ${err.code}, message: ${err.message}`);
10. });

12. @Entry
13. @Component
14. struct Page {

16. build() {
17. Column(){
18. }
19. }
20. }
```

## textRecognition.getSupportedLanguages

PhonePC/2in1Tablet

getSupportedLanguages(callback: AsyncCallback<Array<string>>): void

获取当前文本识别所支持的语言类型列表。使用Callback异步回调。

**系统能力：** SystemCapability.AI.OCR.TextRecognition

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<Array<string>> | 是 | 所支持的[语言类型列表](core-vision-text-recognition-api.md#语言类型列表)。 |

**错误码：**

以下错误码的详细介绍请参见[Core Vision Kit错误码](core-vision-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1001400001 | Failed to run, please try again. |
| 1001400002 | The service is abnormal. |

**示例：**

```
1. import { textRecognition } from '@kit.CoreVisionKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. textRecognition.getSupportedLanguages((error: BusinessError, data: Array<string>) => {
6. if (!error) {
7. hilog.info(0x0000, 'OCRDemo', `Succeeded in obtaining the language: ${data}`);
8. } else {
9. hilog.error(0x0000, 'OCRDemo', `Failed to obtain the language. Code: ${error.code}, message: ${error.message}`);
10. }
11. });

13. @Entry
14. @Component
15. struct Page {

17. build() {
18. Column(){
19. }
20. }
21. }
```

## 语言类型列表

PhonePC/2in1Tablet

| 语言（英） | 语言（中） |
| --- | --- |
| zh-CN | 简体中文 |
| en | 英文 |
| ja | 日文 |
| ko | 韩文 |
| zh-TW | 繁体中文 |
