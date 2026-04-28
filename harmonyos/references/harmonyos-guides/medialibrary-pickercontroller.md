---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/medialibrary-pickercontroller
title: 使用PickerController将编辑后的图片替换原图
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 使用PickerController将编辑后的图片替换原图
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8b8d795d6c21ad01e9829ebcd6cdcf89ab67ec7ff2a90c46aa3c0a70d95019e5
---

## 替换PhotoPicker中显示的图片/视频

应用可获得用户从Picker选择的图片、视频的访问权限，读取图片、视频后进行编辑、修改。完成编辑修改后的图片/视频缓存到应用沙箱后，可调用本API，将编辑结果文件发送给PhotoPicker，并指定替换显示的原图。Picker根据指定将接收的编辑结果文件替换原图片进行显示。

效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/8zHKDm08Tnu91MJdpJcm7A/zh-cn_image_0000002583478607.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234634Z&HW-CC-Expire=86400&HW-CC-Sign=C154DA4EB2F3816383D607FD0B28FBD840BE9C65E619E9EF5667E0AFC0101065)

### 开发步骤

1. 导入选择器模块和文件管理模块。

   ```
   1. import { PickerController } from '@kit.MediaLibraryKit';
   2. import { fileUri } from '@kit.CoreFileKit';
   ```
2. 创建参数列表。

   ```
   1. @State pickerController: PickerController = new PickerController();
   2. @State originUrl: string = ''; // 原图URI
   3. @State replaceUrl: string = ''; // 原图编辑后的沙箱URI
   ```
3. 调用[replacePhotoPickerPreview()](../harmonyos-references/ohos-file-photopickercomponent.md#replacephotopickerpreview15)替换图片/视频。

   ```
   1. this.pickerController.replacePhotoPickerPreview(this.originUrl, this.replaceUrl, (a, b) => {
   2. console.log("hello this.pickerController.replaceUrl code res:" + b)
   3. })
   ```

## 将Picker上替换显示的图片/视频保存到图库

应用指定保存的文件，需在替换显示的范围内。应用调用API后，PhotoPicker将在Picker上成功替换显示的图片、视频保存到图库。确保保存的内容与替换显示的图片、视频一致。

效果如图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/RtRGiZgKRwq3913zG3fHYw/zh-cn_image_0000002552798958.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234634Z&HW-CC-Expire=86400&HW-CC-Sign=7F66CC3C79E7319F61383C5269AA1C3157EA3932FF074F05DC038F3F49686F8E)

### 开发步骤

1. 导入选择器模块和文件管理模块。

   ```
   1. import photoAccessHelper from '@ohos.file.photoAccessHelper';
   2. import { PickerController, PickerOptions, SaveMode } from '@kit.MediaLibraryKit';
   3. import { fileUri } from '@kit.CoreFileKit';
   ```
2. 创建参数列表。

   ```
   1. @State pickerController: PickerController = new PickerController();
   2. @State originUrl: string = ''; // 原图URI
   3. @State replaceUrl: string = ''; // 原图编辑后的沙箱URI
   ```
3. 调用[saveTrustedPhotoAssets()](../harmonyos-references/ohos-file-photopickercomponent.md#savetrustedphotoassets15)保存图片/视频到图库。

   ```
   1. this.pickerController.saveTrustedPhotoAssets(this.replaceUris, (a, b) => {
   2. console.log("hello this.pickerController.save as new code a.code:" + a.code + ",a.message:" + a.message + ",res:" + b)
   3. }, photoCreationConfigs, SaveMode.SAVE_AS); // SaveMode: SAVE_AS = 0(另存为)，OVERWRITE = 1 （覆盖保存）
   ```

   该接口使用依赖[pickerController.replacePhotoPickerPreview](../harmonyos-references/ohos-file-photopickercomponent.md#replacephotopickerpreview15)，需要先执行[pickerController.replacePhotoPickerPreview](../harmonyos-references/ohos-file-photopickercomponent.md#replacephotopickerpreview15)后才能执行[pickerController.saveTrustedPhotoAssets](../harmonyos-references/ohos-file-photopickercomponent.md#savetrustedphotoassets15)。

### 完整示例

```
1. import {
2. SaveMode,
3. } from '@ohos.file.PhotoPickerComponent';
4. import {
5. photoAccessHelper,
6. AlbumPickerOptions,
7. PhotoPickerComponent,
8. PickerController,
9. PickerOptions,
10. ItemInfo,
11. PhotoBrowserInfo,
12. ItemType,
13. ClickType,
14. BaseItemInfo,
15. } from '@kit.MediaLibraryKit'

17. @Entry
18. @Component
19. struct Index {
20. @State pickerController: PickerController = new PickerController();
21. pickerOptions: PickerOptions = new PickerOptions();
22. albumOptions: AlbumPickerOptions = new AlbumPickerOptions();
23. // 已选择的图片uri数组。
24. @State selectedUris: Array<string> = new Array<string>();
25. @State allBackGroundColor: number = 0xf1f3f5;
26. // 是否在大图页面。
27. @State isInPhotoBrowser: boolean = false;
28. @State originUrl: string = ''; // 原图URI。
29. @State EditedUris: Array<string> = new Array<string>(); // 编辑后的URI数组。

31. private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
32. this.isInPhotoBrowser = true;
33. return false;
34. }

36. private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
37. this.isInPhotoBrowser = false;
38. return false;
39. }

41. private onSelect(uri: string): void {
42. // 保存需要替换的图片uri信息。
43. this.originUrl = uri;
44. }

46. private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
47. if (!itemInfo) {
48. return false;
49. }
50. let type: ItemType | undefined = itemInfo.itemType;
51. let uri: string | undefined = itemInfo.uri;
52. if (type === ItemType.CAMERA) {
53. return true;
54. } else if (type === ItemType.THUMBNAIL) {
55. if (clickType === ClickType.SELECTED) {
56. if (uri) {
57. // 添加勾选的图片到selctedUris数组中，用于展示选中图片信息。
58. this.selectedUris.push(uri);
59. }
60. } else {
61. if (uri) {
62. // 取消勾选，且删除在selectedUris中的元素。
63. this.selectedUris = this.selectedUris.filter((item: string) => {
64. return item !== uri;
65. })
66. }
67. }
68. }
69. return true;
70. }

72. private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
73. for (let info of baseItemInfos) {
74. if (info?.uri) {
75. // 如果元素被删除，则删除在selectedUris中的元素。
76. this.selectedUris = this.selectedUris.filter((item: string) => {
77. return info?.uri != item;
78. })
79. }
80. }
81. }

83. aboutToAppear() {
84. // 设置picker宫格页可选择的媒体文件类型，这里设置图片和视频类型。
85. this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
86. }

88. build() {
89. Row() {
90. Stack() {
91. Column() {
92. Row() {
93. Button('另存为').width('25%').height('50%').margin({ top: 10 }).onClick(() => {
94. console.log("----save as new:--------------------------------------------");
95. let replaceUris: Array<string> = [];
96. this.EditedUris.forEach((uri: string) => {
97. replaceUris.push(uri);
98. });
99. // 将编辑后的图片uri数组通过saveTrustedPhotoAssets保存到图库中，SaveMode = SAVE_AS为另存为。
100. this.pickerController.saveTrustedPhotoAssets(replaceUris, (a, b) => {
101. console.log("this.pickerController.save as new, res:" + b);
102. }, undefined, SaveMode.SAVE_AS);
103. }).margin(10)

105. Button('覆盖保存').width('25%').height('50%').margin({ top: 10 }).onClick(() => {
106. console.log("----save as overwrite:--------------------------------------------");
107. let replaceUris: Array<string> = [];
108. this.EditedUris.forEach((uri: string) => {
109. replaceUris.push(uri);
110. });
111. // 将编辑后的图片uri数组通过saveTrustedPhotoAssets保存到图库中，SaveMode = OVERWRITE为覆盖保存。
112. this.pickerController.saveTrustedPhotoAssets(replaceUris, (a, b) => {
113. console.log("this.pickerController.save override, res:" + b)
114. }, undefined, SaveMode.OVERWRITE);
115. }).margin(10)

117. Button('Replace Url').width('25%').height('50%').margin({ top: 10 }).onClick(() => {
118. // 模拟构造应用后期编辑修改后的图片uri。
119. let newLocal = this.originUrl.split('.');
120. let mediaType = newLocal[newLocal.length - 1];
121. let editUri = newLocal[0] + "EDITED." + mediaType;
122. // 将编辑后的图片uri放到全局编辑数组中。
123. this.EditedUris.push(editUri);
124. // 可通过该接口，将photoPicker中用户勾选的图片替换为应用后期编辑修改后的图片。
125. this.pickerController.replacePhotoPickerPreview(this.originUrl, editUri, (a, b) => {
126. console.log("this.pickerController.replaceUrl code" + JSON.stringify(a) + ", res:" + JSON.stringify(b))
127. })
128. }).margin(10)
129. }.width('100%').height('10%')

131. Row() {
132. ForEach(this.selectedUris, (uri: string) => {
133. Image(uri).height('95%').width('20%').backgroundColor(this.allBackGroundColor).onClick(() => {
134. })
135. }, (uri: string) => JSON.stringify(uri))
136. }.width('100%').height('15%')

138. PhotoPickerComponent({
139. pickerOptions: this.pickerOptions,
140. onSelect: (uri: string): void => this.onSelect(uri),
141. onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo,
142. clickType),
143. onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
144. onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
145. onSelectedItemsDeleted: (baseItemInfos: Array<BaseItemInfo>): void => this.onSelectedItemsDeleted(baseItemInfos),
146. pickerController: this.pickerController,
147. }).height('87%')
148. .width('100%')
149. .backgroundColor('#F1F3F5')
150. }.width('100%').height('100%')
151. }
152. }
153. }
154. }
```
