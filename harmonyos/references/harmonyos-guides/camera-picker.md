---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-picker
title: 通过系统相机拍照和录像(CameraPicker)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 通过系统相机拍照和录像(CameraPicker)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:718396051260e51e63e0981415896c6986d6c725b540e266c880b450a20344a8
---

应用可调用CameraPicker拍摄照片或录制视频，无需申请相机权限。

CameraPicker的相机交互界面由系统提供，在用户点击拍摄和确认按钮后，调用CameraPicker的应用获取对应的照片或者视频。

应用开发者如果只是需要获取即时拍摄的照片或者视频，则可以使用CameraPicker能力来轻松实现。

由于照片的拍摄和确认都是由用户进行主动确认，因此应用开发者可以不用申请操作相机的相关权限。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.cameraPicker (相机选择器)](../harmonyos-references/js-apis-camerapicker.md)。

1. 导入相关接口，导入方法如下。

   ```
   1. import { camera, cameraPicker as picker } from '@kit.CameraKit';
   2. import { fileIo, fileUri } from '@kit.CoreFileKit';
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/CameraPicker/entry/src/main/ets/pages/Index.ets#L17-L20)
2. 配置[PickerProfile](../harmonyos-references/js-apis-camerapicker.md#pickerprofile)。

   说明

   PickerProfile的saveUri为可选参数，如果未配置该项，拍摄的照片和视频默认存入媒体库中。

   如果不想将照片和视频存入媒体库，请自行配置应用沙箱内的文件路径。

   应用沙箱内的这个文件必须是一个存在的、可写的文件。这个文件的uri传入picker接口之后，相当于应用给系统相机授权该文件的读写权限。系统相机在拍摄结束之后，会对此文件进行覆盖写入。

   ```
   1. createPickerProfile(context: Context): picker.PickerProfile {
   2. let pathDir = context.filesDir;
   3. let fileName = `${new Date().getTime()}`;
   4. let filePath = pathDir + `/${fileName}.tmp`;
   5. fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE);

   7. let uri = fileUri.getUriFromPath(filePath);
   8. let pickerProfile: picker.PickerProfile = {
   9. cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK,
   10. saveUri: uri
   11. };
   12. return pickerProfile;
   13. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/CameraPicker/entry/src/main/ets/pages/Index.ets#L27-L41)

   fileIo接口调用方法请参考：[createRandomAccessFileSync](../harmonyos-references/js-apis-file-fs.md#fileiocreaterandomaccessfilesync10)和[getUriFromPath](../harmonyos-references/js-apis-file-fileuri.md#fileurigeturifrompath)。
3. 调用picker拍摄接口获取拍摄的结果。

   ```
   1. async getPickerResult(context: Context, pickerProfile: picker.PickerProfile): Promise<picker.PickerResult> {
   2. let result: picker.PickerResult =
   3. await picker.pick(context, [picker.PickerMediaType.PHOTO, picker.PickerMediaType.VIDEO],
   4. pickerProfile);
   5. console.info(`picker resultCode: ${result.resultCode},resultUri: ${result.resultUri},mediaType: ${result.mediaType}`);
   6. return result;
   7. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/CameraPicker/entry/src/main/ets/pages/Index.ets#L43-L51)

## 完整示例

```
1. import { camera, cameraPicker as picker } from '@kit.CameraKit';
2. import { fileIo, fileUri } from '@kit.CoreFileKit';

4. @Entry
5. @Component
6. struct Index {
7. @State imgSrc: string = '';
8. @State videoSrc: string = '';
9. createPickerProfile(context: Context): picker.PickerProfile {
10. let pathDir = context.filesDir;
11. let fileName = `${new Date().getTime()}`;
12. let filePath = pathDir + `/${fileName}.tmp`;
13. fileIo.createRandomAccessFileSync(filePath, fileIo.OpenMode.CREATE);

15. let uri = fileUri.getUriFromPath(filePath);
16. let pickerProfile: picker.PickerProfile = {
17. cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK,
18. saveUri: uri
19. };
20. return pickerProfile;
21. }

23. async getPickerResult(context: Context, pickerProfile: picker.PickerProfile): Promise<picker.PickerResult> {
24. let result: picker.PickerResult =
25. await picker.pick(context, [picker.PickerMediaType.PHOTO, picker.PickerMediaType.VIDEO],
26. pickerProfile);
27. console.info(`picker resultCode: ${result.resultCode},resultUri: ${result.resultUri},mediaType: ${result.mediaType}`);
28. return result;
29. }

31. getContext(): Context | undefined {
32. let uiContext: UIContext = this.getUIContext();
33. let context: Context | undefined = uiContext.getHostContext();
34. return context;
35. }

37. build() {
38. RelativeContainer() {
39. Column() {
40. Image(this.imgSrc).width(200).height(200).backgroundColor(Color.Black).margin(5);
41. Video({ src: this.videoSrc}).width(200).height(200).autoPlay(true);
42. Button("Test Picker Photo&Video").fontSize(20)
43. .fontWeight(FontWeight.Bold)
44. .onClick(async () => {
45. let context = this.getContext();
46. if (context === undefined) {
47. return;
48. }
49. let pickerProfile = this.createPickerProfile(context);
50. let result = await this.getPickerResult(context, pickerProfile);
51. if (result.resultCode == 0) {
52. if (result.mediaType === picker.PickerMediaType.PHOTO) {
53. this.imgSrc = result.resultUri;
54. } else {
55. this.videoSrc = result.resultUri;
56. }
57. }
58. }).margin(5);

60. }.alignRules({
61. center: { anchor: '__container__', align: VerticalAlign.Center },
62. middle: { anchor: '__container__', align: HorizontalAlign.Center }
63. })
64. .id('CaptureOrVideoButton')
65. }
66. .height('100%')
67. .width('100%')
68. }
69. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/CameraPicker/entry/src/main/ets/pages/Index.ets#L16-L92)
