---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-guidelines-photoviewpicker
title: 使用PhotoPicker组件访问图片/视频
breadcrumb: 指南 > 媒体 > Media Library Kit（媒体文件管理服务） > 使用PhotoPicker组件访问图片/视频
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e4d1b0ddf0547a5ee3b26561239124a8f4bcda2d12d9a54f1dcbb8b809f0a473
---

当应用需要读取用户图片时，开发者可以在应用界面中嵌入PhotoPicker组件，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限，即可完成图片或视频文件的访问和读取。

界面效果如图所示。

| 宫格页 | 大图页 |
| --- | --- |
|  |  |

## 开发步骤

1. 导入PhotoPicker模块文件。

   ```
   1. import {
   2. PhotoPickerComponent,
   3. PickerController,
   4. PickerOptions,
   5. DataType,
   6. BaseItemInfo,
   7. ItemInfo,
   8. PhotoBrowserInfo,
   9. ItemType,
   10. ClickType,
   11. MaxCountType,
   12. PhotoBrowserRange,
   13. ReminderMode,
   14. photoAccessHelper
   15. } from '@kit.MediaLibraryKit';
   ```
2. 创建Picker组件配置选项实例（PickerOptions）和控制实例（PickerController）。

   通过PickerOptions，开发者可配置Picker宫格的样式（如勾选框背景色、文本颜色等）、滑动预览方向、最大选择数量等参数，详见[PickerOptions API参考](../harmonyos-references/ohos-file-photopickercomponent.md#pickeroptions)。

   通过PickerController，应用可向Picker组件发送数据。

   ```
   1. // 组件初始化时设置参数信息。
   2. pickerOptions: PickerOptions = new PickerOptions();

   4. // 组件初始化完成后，可控制组件部分行为。
   5. @State pickerController: PickerController = new PickerController();

   7. // 宫格图内已选择的图片uri数组。
   8. @State selectUris: Array<string> = new Array<string>();

   10. // 目前选择的图片uri。
   11. @State currentUri: string = '';

   13. // 标识当前是否显示大图页面，false表示不显示大图页面，true表示显示大图页面。
   14. @State isBrowserShow: boolean = false;
   ```
3. 应用界面出现时，初始化组件配置选项实例（PickerOptions）。

   此处仅列举实例用到的参数，当前支持的配置项及其取值范围详见[PickerOptions API参考](../harmonyos-references/ohos-file-photopickercomponent.md#pickeroptions)。

   ```
   1. // 设置picker宫格页可选择的媒体文件类型，这里设置图片和视频类型。
   2. this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
   3. // 设置宫格页内资源的最大选择数量，示例设置为5。
   4. this.pickerOptions.maxSelectNumber = 5;
   5. // 选择数量达到最大时的提示方式，示例设置为弹窗提示。
   6. this.pickerOptions.maxSelectedReminderMode = ReminderMode.TOAST;
   7. // 设置picker页面内是否需要展示搜索框，false为不展示。
   8. this.pickerOptions.isSearchSupported = true;
   9. // 将宫格页面内第一个宫格置为拍照按钮，false为不展示拍照按钮。
   10. this.pickerOptions.isPhotoTakingSupported = true;
   ```
4. 实现回调函数。

   通过实现以下回调事件，可在用户在界面操作时，将相关信息报给应用进行处理。

   * 进退大图、切换大图回调，上报的大图相关信息详见[PhotoBrowserInfo](../harmonyos-references/ohos-file-photopickercomponent.md#photobrowserinfo)。
   * 勾选图片/视频，将上报图片URI供应用使用。

     说明

     + 回调返回的所有URI均为只读URI，开发者可以根据结果集中的URI读取文件数据。但不能在Picker的回调中直接使用此URI打开文档，需要定义一个全局变量保存URI，样例可参考[指定URI读取文件数据](photoaccesshelper-photoviewpicker.md#指定uri读取文件数据)、[指定URI获取图片或视频资源](photoaccesshelper-photoviewpicker.md#指定uri获取图片或视频资源)。
     + 如需获取元数据，可通过[文件管理](../harmonyos-references/js-apis-file-fs.md)和[文件URI](../harmonyos-references/js-apis-file-fileuri.md)接口，根据uri获取部分文件属性信息，比如文件大小、访问时间、修改时间、文件名、文件路径等。
   * 点击图片（缩略图item），将上报图片/视频信息[ItemInfo](../harmonyos-references/ohos-file-photopickercomponent.md#iteminfo)；
   * 点击相机item，可默认拉起系统相机或应用自行处理。如何自行拉起相机请参考[cameraPicker.pick](../harmonyos-references/js-apis-camerapicker.md#camerapickerpick)。

   支持的回调事件及其参数请参考[PhotoPickerComponent API参考](../harmonyos-references/ohos-file-photopickercomponent.md#photopickercomponent)。

   ```
   1. // 资源被选中回调，返回资源的信息，以及选中方式。
   2. // 应用根据自己的业务来决定，资源是否勾选或者是否进入系统相机。
   3. private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
   4. if (!itemInfo) {
   5. return false;
   6. }
   7. let type: ItemType | undefined = itemInfo.itemType;
   8. let uri: string | undefined = itemInfo.uri;
   9. if (type === ItemType.CAMERA) {
   10. // 如果宫格页面第一个宫格的类型为ItemType.CAMERA，则是相机按钮。
   11. // 返回true则拉起系统相机；如果返回false应用可以自己拉起相机。
   12. return true;
   13. } else {
   14. // 如果是选中操作。
   15. if (clickType === ClickType.SELECTED) {
   16. // 应用做自己的业务处理。
   17. if (uri) {
   18. this.selectUris.push(uri);
   19. this.pickerOptions.preselectedUris = [...this.selectUris];
   20. }
   21. // 返回true则该宫格响应勾选，否则不响应勾选。
   22. return true;
   23. } else {
   24. // 如果是取消选中操作。
   25. // 应用做自己的业务处理。
   26. if (uri) {
   27. this.selectUris = this.selectUris.filter((item: string) => {
   28. return item != uri;
   29. });
   30. this.pickerOptions.preselectedUris = [...this.selectUris];
   31. }
   32. // 返回true则该宫格响应取消勾选，否则不响应取消勾选。
   33. return true;
   34. }
   35. }
   36. }

   38. // 点击缩略图从宫格进入大图时产生的回调。
   39. private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
   40. this.isBrowserShow = true;
   41. return true;
   42. }

   44. // 退出大图时的回调。
   45. private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
   46. this.isBrowserShow = false;
   47. return true;
   48. }

   50. // 接收到该回调后，便可通过pickerController相关接口向picker发送数据，在此之前不生效。
   51. private onPickerControllerReady(): void {
   52. let elements: number[] = [PhotoBrowserUIElement.BACK_BUTTON];
   53. this.pickerController.setPhotoBrowserUIElementVisibility(elements, false); // 设置大图页不显示返回按钮。
   54. }

   56. // 大图左右滑动的回调。
   57. private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
   58. this.currentUri = browserItemInfo.uri ?? '';
   59. return true;
   60. }

   62. // 已勾选图片被删除时的回调。
   63. private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
   64. }

   66. // 超过最大选择数量再次点击时的回调。
   67. private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void {
   68. }

   70. // 当前相册被删除时的回调。
   71. private onCurrentAlbumDeleted(): void {
   72. }
   ```
5. 创建[PhotoPickerComponent](../harmonyos-references/ohos-file-photopickercomponent.md#photopickercomponent)组件。

   ```
   1. PhotoPickerComponent({
   2. pickerOptions: this.pickerOptions,
   3. onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo, clickType),
   4. onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
   5. onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
   6. onPickerControllerReady: (): void => this.onPickerControllerReady(),
   7. onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
   8. onSelectedItemsDeleted: (BaseItemInfo: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(BaseItemInfo),
   9. onExceedMaxSelected: (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType),
   10. onCurrentAlbumDeleted: () => this.onCurrentAlbumDeleted(),
   11. pickerController: this.pickerController,
   12. })
   ```
6. 通过PickerController向Picker组件发送数据，实现控制PhotoPickerComponent组件行为。

   存在多种用法，详见[PickerController](../harmonyos-references/ohos-file-photopickercomponent.md#pickercontroller)API文档。

## 完整示例

```
1. import {
2. PhotoPickerComponent,
3. PickerController,
4. PickerOptions,
5. DataType,
6. BaseItemInfo,
7. ItemInfo,
8. PhotoBrowserInfo,
9. ItemType,
10. ClickType,
11. MaxCountType,
12. PhotoBrowserRange,
13. ReminderMode,
14. photoAccessHelper
15. } from '@kit.MediaLibraryKit';

17. @Entry
18. @Component
19. struct PhotoPickerComponentDemo {
20. // 组件初始化时设置参数信息。
21. pickerOptions: PickerOptions = new PickerOptions();

23. // 组件初始化完成后，可控制组件部分行为。
24. @State pickerController: PickerController = new PickerController();

26. // 宫格图内已选择的图片uri数组。
27. @State selectUris: Array<string> = new Array<string>();

29. // 目前选择的图片uri。
30. @State currentUri: string = '';

32. // 标识当前是否显示大图页面，false表示不显示大图页面，true表示显示大图页面。
33. @State isBrowserShow: boolean = false;

35. aboutToAppear() {
36. // 设置picker宫格页可选择的媒体文件类型，这里设置图片和视频类型。
37. this.pickerOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
38. // 设置宫格页内资源的最大选择数量，示例设置为5。
39. this.pickerOptions.maxSelectNumber = 5;
40. // 选择数量达到最大时的提示方式，示例设置为弹窗提示。
41. this.pickerOptions.maxSelectedReminderMode = ReminderMode.TOAST;
42. // 设置picker页面内是否需要展示搜索框，false为不展示。
43. this.pickerOptions.isSearchSupported = true;
44. // 将宫格页面内第一个宫格置为拍照按钮，false为不展示拍照按钮。
45. this.pickerOptions.isPhotoTakingSupported = true;
46. }

48. // 资源被选中回调，返回资源的信息，以及选中方式。
49. // 应用根据自己的业务来决定，资源是否勾选或者是否进入系统相机。
50. private onItemClicked(itemInfo: ItemInfo, clickType: ClickType): boolean {
51. if (!itemInfo) {
52. return false;
53. }
54. let type: ItemType | undefined = itemInfo.itemType;
55. let uri: string | undefined = itemInfo.uri;
56. if (type === ItemType.CAMERA) {
57. // 如果宫格页面第一个宫格的类型为ItemType.CAMERA，则是相机按钮。
58. // 返回true则拉起系统相机；如果返回false应用可以自己拉起相机。
59. return true;
60. } else {
61. // 如果是选中操作。
62. if (clickType === ClickType.SELECTED) {
63. // 应用做自己的业务处理。
64. if (uri) {
65. this.selectUris.push(uri);
66. this.pickerOptions.preselectedUris = [...this.selectUris];
67. }
68. // 返回true则该宫格响应勾选，否则不响应勾选。
69. return true;
70. } else {
71. // 如果是取消选中操作。
72. // 应用做自己的业务处理。
73. if (uri) {
74. this.selectUris = this.selectUris.filter((item: string) => {
75. return item != uri;
76. });
77. this.pickerOptions.preselectedUris = [...this.selectUris];
78. }
79. // 返回true则该宫格响应取消勾选，否则不响应取消勾选。
80. return true;
81. }
82. }
83. }

85. // 点击缩略图从宫格进入大图时产生的回调。
86. private onEnterPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
87. this.isBrowserShow = true;
88. return true;
89. }

91. // 退出大图时的回调。
92. private onExitPhotoBrowser(photoBrowserInfo: PhotoBrowserInfo): boolean {
93. this.isBrowserShow = false;
94. return true;
95. }

97. // 接收到该回调后，便可通过pickerController相关接口向picker发送数据，在此之前不生效。
98. private onPickerControllerReady(): void {
99. }

101. // 大图左右滑动的回调。
102. private onPhotoBrowserChanged(browserItemInfo: BaseItemInfo): boolean {
103. this.currentUri = browserItemInfo.uri ?? '';
104. return true;
105. }

107. // 已勾选图片被删除时的回调。
108. private onSelectedItemsDeleted(baseItemInfos: Array<BaseItemInfo>): void {
109. }

111. // 超过最大选择数量再次点击时的回调。
112. private onExceedMaxSelected(exceedMaxCountType: MaxCountType): void {
113. }

115. // 当前相册被删除时的回调。
116. private onCurrentAlbumDeleted(): void {
117. }

119. build() {
120. Flex({
121. direction: FlexDirection.Column,
122. alignItems: ItemAlign.Start
123. }) {
124. PhotoPickerComponent({
125. pickerOptions: this.pickerOptions,
126. onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo, clickType),
127. onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
128. onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
129. onPickerControllerReady: (): void => this.onPickerControllerReady(),
130. onPhotoBrowserChanged: (browserItemInfo: BaseItemInfo): boolean => this.onPhotoBrowserChanged(browserItemInfo),
131. onSelectedItemsDeleted: (BaseItemInfo: Array<BaseItemInfo>) => this.onSelectedItemsDeleted(BaseItemInfo),
132. onExceedMaxSelected: (exceedMaxCountType: MaxCountType) => this.onExceedMaxSelected(exceedMaxCountType),
133. onCurrentAlbumDeleted: () => this.onCurrentAlbumDeleted(),
134. pickerController: this.pickerController,
135. })

137. // 这里模拟应用侧底部的选择栏。
138. if (this.isBrowserShow) {
139. // 已选择的图片缩略图。
140. Row() {
141. ForEach(this.selectUris, (uri: string) => {
142. if (uri === this.currentUri) {
143. Image(uri).height(50).width(50)
144. .onClick(() => {
145. })
146. .borderWidth(1)
147. .borderColor('red')
148. } else {
149. Image(uri).height(50).width(50).onClick(() => {
150. this.pickerController.setData(DataType.SET_SELECTED_URIS, this.selectUris);
151. // 点击底部缩略图，切换大图浏览的照片为点击的缩略图；本示例设置浏览范围为全部，包括图片和视频。
152. this.pickerController.setPhotoBrowserItem(uri, PhotoBrowserRange.ALL);
153. })
154. }
155. }, (uri: string) => JSON.stringify(uri))
156. }.alignSelf(ItemAlign.Center).margin(this.selectUris.length ? 10 : 0)
157. } else {
158. // 进入大图，预览已选择的图片。
159. Button('预览').width('33%').alignSelf(ItemAlign.Start).height('5%').margin(10).onClick(() => {
160. if (this.selectUris.length > 0) {
161. // 切换picker组件至大图浏览模式浏览图片。
162. this.pickerController.setPhotoBrowserItem(this.selectUris[0], PhotoBrowserRange.SELECTED_ONLY);
163. }
164. })
165. }
166. }
167. }
168. }
```
