---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-guidelines-based-js
title: 使用MindSpore Lite实现图像分类（ArkTS）
breadcrumb: 指南 > AI > MindSpore Lite Kit（昇思推理框架服务） > 使用MindSpore Lite实现图像分类（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5fd930e4581e18c8ac706f17388cac7678fb1ca775cbcaa6a89031cbfec12798
---

## 场景说明

开发者可以使用[@ohos.ai.mindSporeLite](../harmonyos-references/js-apis-mindsporelite.md)，在UI代码中集成MindSpore Lite能力，快速部署AI算法，进行AI模型推理，实现图像分类的应用。

图像分类可实现对图像中物体的识别，在医学影像分析、自动驾驶、电子商务、人脸识别等领域有广泛的应用。

若需基于本Demo适配自有模型，请优先选择静态Shape模型。由于ArkTS暂不支持动态Shape，如确有相关需求，请参考[使用MindSpore Lite实现图像分类（C/C++）](mindspore-guidelines-based-native.md)，通过Native侧的[OH\_AI\_ModelResize](../harmonyos-references/capi-model-h.md#oh_ai_modelresize)接口对模型inputs进行动态调整。

## 基本概念

在进行开发前，请先了解以下概念。

**张量**：它与数组和矩阵非常相似，是MindSpore Lite网络运算中的基本数据结构。

**Float16推理模式**： Float16又称半精度，它使用16比特表示一个数。Float16推理模式表示推理的时候用半精度进行推理。

## 接口说明

这里给出MindSpore Lite推理的通用开发流程中涉及的一些接口，具体请见下列表格。更多接口及详细内容，请见[@ohos.ai.mindSporeLite (推理能力)](../harmonyos-references/js-apis-mindsporelite.md)。

| 接口名 | 描述 |
| --- | --- |
| loadModelFromFile(model: string, context?: Context): Promise<Model> | 从路径加载模型。 |
| getInputs(): MSTensor[] | 获取模型的输入。 |
| predict(inputs: MSTensor[]): Promise<MSTensor[]> | 推理模型。 |
| getData(): ArrayBuffer | 获取张量的数据。 |
| setData(inputArray: ArrayBuffer): void | 设置张量的数据。 |

## 开发流程

1. 选择图像分类模型。
2. 在端侧使用MindSpore Lite推理模型，实现对选择的图片进行分类。

## 开发步骤

本文以对相册的一张图片进行推理为例，提供使用MindSpore Lite实现图像分类的开发指导。

### 选择模型

本示例程序中使用的图像分类模型文件为[mobilenetv2.ms](https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/1.5/mobilenetv2.ms)，放置在entry/src/main/resources/rawfile工程目录下。

如果开发者有其他图像分类的预训练模型，请参考[MindSpore Lite 模型转换](mindspore-lite-converter-guidelines.md)介绍，将原始模型转换成.ms格式。

### 编写推理代码

1. 工程默认设备定义的能力集可能不包含MindSporeLite。需在DevEco Studio工程的entry/src/main目录下，手动创建syscap.json文件，内容如下：

   ```
   1. {
   2. "devices": {
   3. "general": [
   4. // 需跟module.json5中deviceTypes保持一致。
   5. "default"
   6. ]
   7. },
   8. "development": {
   9. "addedSysCaps": [
   10. "SystemCapability.AI.MindSporeLite"
   11. ]
   12. }
   13. }
   ```
2. 调用[@ohos.ai.mindSporeLite](../harmonyos-references/js-apis-mindsporelite.md)实现端侧推理。具体开发过程及细节如下：

   1. 创建上下文，设置线程数、设备类型等参数。本样例模型，不支持使用NNRt推理。
   2. 加载模型。本文从内存加载模型。
   3. 加载数据。模型执行之前需要先获取输入，再向输入的张量中填充数据。
   4. 执行推理。使用predict接口进行模型推理。

   ```
   1. // model.ets
   2. import { mindSporeLite } from '@kit.MindSporeLiteKit'
   3. import { hilog } from '@kit.PerformanceAnalysisKit';

   5. export default async function modelPredict(
   6. modelBuffer: ArrayBuffer, inputsBuffer: ArrayBuffer[]): Promise<mindSporeLite.MSTensor[]> {

   8. // 1.创建上下文，设置线程数、设备类型等参数。本样例模型，不支持配置context.target = ["nnrt"]。
   9. let context: mindSporeLite.Context = {};
   10. context.target = ['cpu'];
   11. context.cpu = {}
   12. context.cpu.threadNum = 2;
   13. context.cpu.threadAffinityMode = 1;
   14. context.cpu.precisionMode = 'enforce_fp32';

   16. // 2.从内存加载模型。
   17. let msLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromBuffer(modelBuffer, context);

   19. // 3.设置输入数据。
   20. let modelInputs: mindSporeLite.MSTensor[] = msLiteModel.getInputs();
   21. for (let i = 0; i < inputsBuffer.length; i++) {
   22. let inputBuffer = inputsBuffer[i];
   23. if (inputBuffer != null) {
   24. modelInputs[i].setData(inputBuffer as ArrayBuffer);
   25. }
   26. }

   28. // 4.执行推理。
   29. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s', `=========MS_LITE_LOG: MS_LITE predict start=====`);
   30. let modelOutputs: mindSporeLite.MSTensor[] = await msLiteModel.predict(modelInputs);
   31. return modelOutputs;
   32. }
   ```

   [model.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteArkTSDemo/entry/src/main/ets/pages/model.ets#L16-L48)

### 实现图像输入和预处理，并执行推理

1. 此处以获取相册图片为例，调用[@ohos.file.picker](../harmonyos-references/js-apis-file-picker.md) 实现相册图片文件的选择。
2. 根据模型的输入尺寸，调用[@ohos.multimedia.image](../harmonyos-references/arkts-apis-image.md) （实现图片处理）、[@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md) （实现基础文件操作） API对选择图片进行裁剪、获取图片buffer数据，并进行标准化处理。
3. 加载模型文件，调用推理函数，对相册选择的图片进行推理，并对推理结果进行处理。

   ```
   1. // Index.ets
   2. import modelPredict from './model';
   3. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { image } from '@kit.ImageKit';
   6. import { fileIo } from '@kit.CoreFileKit';
   7. import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
   8. import { hilog } from '@kit.PerformanceAnalysisKit';

   10. const PERMISSIONS: Permissions[] = ['ohos.permission.READ_IMAGEVIDEO'];

   12. @Entry
   13. @Component
   14. struct Index {
   15. @State modelPredict: string = 'MindSporeLite ArkTS Demo';
   16. @State modelName: string = 'mobilenetv2.ms';
   17. @State modelInputHeight: number = 224;
   18. @State modelInputWidth: number = 224;
   19. @State uris: Array<string> = [];
   20. @State max: number = 0;
   21. @State maxIndex: number = 0;
   22. @State maxArray: Array<number> = [];
   23. @State maxIndexArray: Array<number> = [];

   25. build() {
   26. Row() {
   27. Column() {
   28. Text(this.modelPredict)
   29. Button() {
   30. Text('photo')
   31. .fontSize(30)
   32. .fontWeight(FontWeight.Bold)
   33. }
   34. .onClick(() => {
   35. let resMgr = this.getUIContext()?.getHostContext()?.getApplicationContext().resourceManager;
   36. if (resMgr === null || resMgr === undefined){
   37. hilog.error(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s', `MS_LITE_ERR: get resMgr failed.`);
   38. return
   39. }
   40. resMgr?.getRawFileContent(this.modelName).then(modelBuffer => {

   42. // 获取相册图片
   43. // 1.创建图片文件选择实例
   44. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();

   46. // 2.设置选择媒体文件类型为IMAGE，设置选择媒体文件的最大数目
   47. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE; // 过滤选择媒体文件类型为IMAGE
   48. photoSelectOptions.maxSelectNumber = 1; // 选择媒体文件的最大数目

   50. // 3.创建图库选择器实例，调用select()接口拉起图库界面进行文件选择。文件选择成功后，返回photoSelectResult结果集。
   51. let photoPicker = new photoAccessHelper.PhotoViewPicker();
   52. photoPicker.select(photoSelectOptions, async (
   53. err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
   54. if (err) {
   55. hilog.error(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   56. `MS_LITE_ERR: PhotoViewPicker.select failed with err: ${JSON.stringify(err)}`);
   57. return;
   58. }
   59. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   60. `MS_LITE_LOG: PhotoViewPicker.select successfully, uri: ${JSON.stringify(photoSelectResult)}`);
   61. this.uris = photoSelectResult.photoUris;
   62. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s', `MS_LITE_LOG: uri: ${this.uris}`);

   64. // 预处理图片数据
   65. try {
   66. // 1.使用fileIo.openSync接口，通过uri打开这个文件得到fd
   67. let file = fileIo.openSync(this.uris[0], fileIo.OpenMode.READ_ONLY);
   68. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s', `MS_LITE_LOG: file fd: ${file.fd}`);

   70. // 2.通过fd使用fileIo.readSync接口读取这个文件内的数据
   71. let inputBuffer = new ArrayBuffer(4096000);
   72. let readLen = fileIo.readSync(file.fd, inputBuffer);
   73. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   74. `MS_LITE_LOG: readSync data to file succeed and inputBuffer size is: ${readLen}`);

   76. // 3.通过PixelMap预处理
   77. let imageSource = image.createImageSource(file.fd);
   78. if (imageSource === undefined) {
   79. hilog.error(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s', `MS_LITE_ERR: createImageSource failed.`);
   80. return
   81. }
   82. imageSource.createPixelMap().then((pixelMap) => {
   83. pixelMap.getImageInfo().then((info) => {
   84. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   85. `MS_LITE_LOG: info.width = ${info.size.width}`);
   86. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   87. `MS_LITE_LOG: info.height = ${info.size.height}`);

   89. // 4.根据模型输入的尺寸，将图片裁剪为对应的size，获取图片buffer数据readBuffer
   90. pixelMap.scale(256.0 / info.size.width, 256.0 / info.size.height).then(() => {
   91. pixelMap.crop(
   92. { x: 16, y: 16, size: { height: this.modelInputHeight, width: this.modelInputWidth } }
   93. ).then(async () => {
   94. let info = await pixelMap.getImageInfo();
   95. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   96. `MS_LITE_LOG: crop info.width = ${info.size.width}`);
   97. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   98. `MS_LITE_LOG: crop info.height = ${info.size.height}`);

   100. // 需要创建的像素buffer大小
   101. let readBuffer = new ArrayBuffer(this.modelInputHeight * this.modelInputWidth * 4);
   102. await pixelMap.readPixelsToBuffer(readBuffer);
   103. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   104. `MS_LITE_LOG: Succeeded in reading image pixel data, buffer: ${readBuffer.byteLength}`);
   105. // 处理readBuffer，转换成float32格式，并进行标准化处理
   106. const imageArr = new Uint8Array(
   107. readBuffer.slice(0, this.modelInputHeight * this.modelInputWidth * 4));
   108. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   109. `MS_LITE_LOG: imageArr length: ${imageArr.length}`);

   111. let means = [0.485, 0.456, 0.406];
   112. let stds = [0.229, 0.224, 0.225];
   113. let float32View = new Float32Array(this.modelInputHeight * this.modelInputWidth * 3);
   114. let index = 0;
   115. for (let i = 0; i < imageArr.length; i++) {
   116. if ((i + 1) % 4 === 0) {
   117. float32View[index] = (imageArr[i - 3] / 255.0 - means[0]) / stds[0]; // B
   118. float32View[index+1] = (imageArr[i - 2] / 255.0 - means[1]) / stds[1]; // G
   119. float32View[index+2] = (imageArr[i - 1] / 255.0 - means[2]) / stds[2]; // R
   120. index += 3;
   121. }
   122. }
   123. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   124. `MS_LITE_LOG: float32View length: ${float32View.length}`);
   125. let printStr = 'float32View data:';
   126. for (let i = 0; i < 20; i++) {
   127. printStr += ' ' + float32View[i];
   128. }
   129. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   130. `MS_LITE_LOG: float32View data: ${printStr}`);

   132. let inputs: ArrayBuffer[] = [float32View.buffer];

   134. // predict
   135. modelPredict(modelBuffer.buffer.slice(0), inputs).then(outputs => {
   136. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   137. `=========MS_LITE_LOG: MS_LITE predict success=====`);

   139. // 结果打印
   140. for (let i = 0; i < outputs.length; i++) {
   141. let out = new Float32Array(outputs[i].getData());

   143. let printStr = outputs[i].name + ':';
   144. for (let j = 0; j < out.length; j++) {
   145. printStr += out[j].toString() + ',';
   146. }
   147. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s', `MS_LITE_LOG: ${printStr}`);

   149. // 取分类占比的最大值top5
   150. this.max = 0;
   151. this.maxIndex = 0;
   152. this.maxArray = [];
   153. this.maxIndexArray = [];
   154. let newArray = out.filter(value => value !== this.max)
   155. for (let n = 0; n < 5; n++) {
   156. this.max = out[0];
   157. this.maxIndex = 0;
   158. // 取最大值
   159. for (let m = 0; m < newArray.length; m++) {
   160. if (newArray[m] > this.max) {
   161. this.max = newArray[m];
   162. this.maxIndex = m;
   163. }
   164. }
   165. this.maxArray.push(Math.round(this.max * 10000));
   166. this.maxIndexArray.push(this.maxIndex);
   167. // filter数组过滤函数
   168. newArray = newArray.filter(value => value !== this.max)
   169. }
   170. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   171. `MS_LITE_LOG: max: ${this.maxArray}`);
   172. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   173. `MS_LITE_LOG: maxIndex: ${this.maxIndexArray}`);
   174. }
   175. hilog.info(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   176. `=========MS_LITE_LOG END=========`);
   177. })
   178. }).catch((error: BusinessError) => {
   179. hilog.error(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   180. `MS_LITE_ERR: getRawFileContent promise error is: ${error}`);
   181. })
   182. })
   183. })
   184. })

   186. // 5.关闭文件
   187. fileIo.closeSync(file);
   188. } catch (err) {
   189. hilog.error(0xFF00, 'MindSporeLiteArkTSDemo', '%{public}s',
   190. `MS_LITE_ERR: uri: open file fd failed. ${err}`);
   191. }
   192. })
   193. })
   194. })
   195. }
   196. .width('100%')
   197. }
   198. .height('100%')
   199. }
   200. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteArkTSDemo/entry/src/main/ets/pages/Index.ets#L16-L351)

### 调测验证

1. 在DevEco Studio中连接设备，点击Run entry，编译Hap，有如下显示：

   ```
   1. Launching com.samples.mindsporelitearktsdemo
   2. $ hdc shell aa force-stop com.samples.mindsporelitearktsdemo
   3. $ hdc shell mkdir data/local/tmp/xxx
   4. $ hdc file send C:\Users\xxx\MindSporeLiteArkTSDemo\entry\build\default\outputs\default\entry-default-signed.hap "data/local/tmp/xxx"
   5. $ hdc shell bm install -p data/local/tmp/xxx
   6. $ hdc shell rm -rf data/local/tmp/xxx
   7. $ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitearktsdemo
   ```
2. 在设备屏幕点击photo按钮，选择图片，点击确定。设备屏幕显示所选图片的分类结果，在日志打印结果中，过滤关键字”MS\_LITE“，可得到如下结果：

   ```
   1. 08-06 03:24:33.743   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     MS_LITE_LOG: PhotoViewPicker.select successfully, photoSelectResult uri: {"photoUris":["file://media/Photo/13/IMG_1501955351_012/plant.jpg"]}
   2. 08-06 03:24:33.795   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     MS_LITE_LOG: readSync data to file succeed and inputBuffer size is:32824
   3. 08-06 03:24:34.147   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     MS_LITE_LOG: crop info.width = 224
   4. 08-06 03:24:34.147   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     MS_LITE_LOG: crop info.height = 224
   5. 08-06 03:24:34.160   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     MS_LITE_LOG: Succeeded in reading image pixel data, buffer: 200704
   6. 08-06 03:24:34.970   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     =========MS_LITE_LOG: MS_LITE predict start=====
   7. 08-06 03:24:35.432   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     =========MS_LITE_LOG: MS_LITE predict success=====
   8. 08-06 03:24:35.447   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     MS_LITE_LOG: Default/head-MobileNetV2Head/Sigmoid-op466:0.0000034338463592575863,0.000014028532859811094,9.119685273617506e-7,0.000049100715841632336,9.502661555416125e-7,3.945370394831116e-7,0.04346757382154465,0.00003971960904891603...
   9. 08-06 03:24:35.499   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     MS_LITE_LOG: max:9497,7756,1970,435,46
   10. 08-06 03:24:35.499   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     MS_LITE_LOG: maxIndex:323,46,13,6,349
   11. 08-06 03:24:35.499   22547-22547  A03d00/JSAPP                   com.sampl...liteark+  I     =========MS_LITE_LOG END=========
   ```

### 效果示意

在设备上，点击photo按钮，选择相册中的一张图片，点击确定。在图片下方显示此图片占比前4的分类信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/eBdU7lEoQQGtFNVlCKekPg/zh-cn_image_0000002589245657.png?HW-CC-KV=V1&HW-CC-Date=20260429T054345Z&HW-CC-Expire=86400&HW-CC-Sign=330A345C4217197D6FD6FE653B648F25D9BC68A56025E727FC5ABEF6712D4A1E) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/m5BAlvJpQDyD6Fzw4jzLUw/zh-cn_image_0000002558765848.png?HW-CC-KV=V1&HW-CC-Date=20260429T054345Z&HW-CC-Expire=86400&HW-CC-Sign=08ED5EF246075AC07C7F7375D2DD761A772DA5972B7F9B471B63E015E540FC8B)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/N4CgMBcQQD-i1R4_ZXc-cw/zh-cn_image_0000002558606192.png?HW-CC-KV=V1&HW-CC-Date=20260429T054345Z&HW-CC-Expire=86400&HW-CC-Sign=DED7ADAC646E517D80A35E57D2CC92B31CB3C3F20190C4101F91B7BAA294D411) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/P6FdF0VgS_21yFsK35_kJA/zh-cn_image_0000002589325719.png?HW-CC-KV=V1&HW-CC-Date=20260429T054345Z&HW-CC-Expire=86400&HW-CC-Sign=CEB4923F237933EE0EF627A161C4FF922718058179695A5A1697BC3DCE09171B)

## 示例代码

* [基于MindSporeLite接口实现图像分类（ArkTS）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/MindSporeLiteKit/MindSporeLiteArkTSDemo)
