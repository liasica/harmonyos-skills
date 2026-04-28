---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-photoeditorextensioncontext
title: PhotoEditorExtensionContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > PhotoEditorExtensionContext
category: harmonyos-references
scraped_at: 2026-04-28T07:58:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bb17a1316e07251cbe8ad84608525c0d9fb0847a3aa78ec6724495ce3c107aaa
---

PhotoEditorExtensionContext是PhotoEditorExtensionAbility的上下文，继承自ExtensionContext，提供PhotoEditorExtensionAbility的相关配置信息以及保存图片接口。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { common } from '@kit.AbilityKit';
```

## PhotoEditorExtensionContext.saveEditedContentWithUri

PhonePC/2in1TabletTV

saveEditedContentWithUri(uri: string): Promise<AbilityResult>

传入编辑过的图片的uri并保存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 编辑后图片的[uri](js-apis-file-fileuri.md)，格式为file://<bundleName>/<sandboxPath>。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityResult> | Promise对象，返回AbilityResult对象，编辑过的图片uri存在want.uri中，[uri](js-apis-file-fileuri.md)格式为file://<bundleName>/<sandboxPath>。 |

**错误码：**

以下错误码详细介绍参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 29600001 | Internal error. |
| 29600002 | Image input error. |
| 29600003 | Image too big. |

**示例：**

```
1. import { common, UIExtensionContentSession, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { fileIo } from '@kit.CoreFileKit';
4. import { image } from '@kit.ImageKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. const TAG = '[ExamplePhotoEditorAbility]';

9. @Entry
10. @Component
11. struct Index {
12. // 原始图片
13. @State originalImage: PixelMap | null = null;

15. build() {
16. Row() {
17. Column() {
18. Button('RotateAndSaveImg').onClick(event => {
19. hilog.info(0x0000, TAG, `Start to edit image and save.`);

21. this.originalImage?.rotate(90).then(() => {
22. const imagePackerApi: image.ImagePacker = image.createImagePacker();
23. let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
24. imagePackerApi.packToData(this.originalImage, packOpts).then((data: ArrayBuffer) => {
25. let context = this.getUIContext().getHostContext() as common.PhotoEditorExtensionContext;
26. let filePath = context.filesDir + '/edited.jpg';
27. let file: fileIo.File | undefined;
28. try{
29. file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE
30. | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
31. let writeLen = fileIo.writeSync(file.fd, data);
32. hilog.info(0x0000, TAG, 'write data to file succeed and size is:'
33. + writeLen);
34. fileIo.closeSync(file);
35. context.saveEditedContentWithUri(filePath).then
36. (data => {
37. hilog.info(0x0000, TAG,
38. `saveContentEditingWithUri result: ${JSON.stringify(data)}`);
39. });
40. } catch (e) {
41. hilog.info(0x0000, TAG, `writeImage failed:${e}`);
42. } finally {
43. fileIo.close(file);
44. }
45. }).catch((error: BusinessError) => {
46. hilog.error(0x0000, TAG,
47. 'Failed to pack the image. And the error is: ' + String(error));
48. })
49. })
50. }).margin({ top: 10 })
51. }
52. }
53. }
54. }
```

## PhotoEditorExtensionContext.saveEditedContentWithImage

PhonePC/2in1TabletTV

saveEditedContentWithImage(pixeMap: image.PixelMap, option: image.PackingOption): Promise<AbilityResult>

传入编辑过的图片的PixelMap对象并保存。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.AppExtension.PhotoEditorExtension

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pixeMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 编辑过的图片image.PixelMap。 |
| option | [image.PackingOption](arkts-apis-image-i.md#packingoption) | 是 | 设置打包参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AbilityResult> | Promise对象，返回AbilityResult对象，编辑过的图片uri存在want.uri中，[uri](js-apis-file-fileuri.md)格式为file://<bundleName>/<sandboxPath>。 |

**错误码：**

以下错误码详细介绍参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Params error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 29600001 | Internal error. |
| 29600002 | Image input error. |
| 29600003 | Image too big. |

**示例：**

```
1. import { common, UIExtensionContentSession, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { image } from '@kit.ImageKit';

5. const TAG = '[ExamplePhotoEditorAbility]';

7. @Entry
8. @Component
9. struct Index {
10. // 原始图片
11. @State originalImage: PixelMap | null = null;

13. build() {
14. Row() {
15. Column() {
16. Button('RotateAndSaveImg').onClick(event => {
17. hilog.info(0x0000, TAG, `Start to edit image and save.`);

19. this.originalImage?.rotate(90).then(() => {
20. let packOpts: image.PackingOption = { format: 'image/jpeg', quality: 98 };
21. try {
22. let context = this.getUIContext().getHostContext() as common.PhotoEditorExtensionContext;
23. context.saveEditedContentWithImage(this.originalImage as image.PixelMap,
24. packOpts).then(data => {
25. hilog.info(0x0000, TAG,
26. `saveContentEditingWithImage result: ${JSON.stringify(data)}`);
27. });
28. } catch (e) {
29. hilog.error(0x0000, TAG, `saveContentEditingWithImage failed:${e}`);
30. return;
31. }
32. })
33. }).margin({ top: 10 })
34. }
35. }
36. }
37. }
```
