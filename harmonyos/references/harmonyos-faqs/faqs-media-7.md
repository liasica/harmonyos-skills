---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-7
title: 如何获取视频首帧画面
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 如何获取视频首帧画面
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:41+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:97610e9d0ea17d28d344abc70da7d4c90d6eadfab8afffd6ccfbe55488cca56a
---

获得视频首帧分为从本地视频获取视频首帧和从网络视频获取视频首帧。

**本地视频获取首帧**

从本地视频获取首帧有两种方案，分别是通过[PhotoAsset](../harmonyos-references/js-apis-sendablephotoaccesshelper.md#photoasset)类的[getThumbnail()](../harmonyos-references/js-apis-sendablephotoaccesshelper.md#getthumbnail)方法获取首帧；通过[AVImageGenerator](../harmonyos-references/arkts-apis-media-avimagegenerator.md)选取视频开始时间获取首帧，详细内容请参考[选取视频帧作为缩略图](../best-practices/bpta-video-thumbnail.md#section1848255103812)。

此外，如果是从沙箱路径获取视频首帧，需要获取视频文件的文件描述符fd，详细内容请参考[应用文件访问(ArkTS)](../harmonyos-guides/app-file-access.md)。

```
1. // Create AVImageGenerator object
2. let avImageGenerator: media.AVImageGenerator = await media.createAVImageGenerator();
3. // Configure avImageGenerator.fdSrc attributes based on album video URI
4. let fileINT = fs.openSync(this.filesDir + '/test1.mp4', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
5. let avFileDescriptor: media.AVFileDescriptor = { fd: fileINT.fd };
6. // Configuration parameter
7. avImageGenerator.fdSrc = avFileDescriptor;
```

[GetFirstFrameAnimation.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaLibraryKit/entry/src/main/ets/pages/GetFirstFrameAnimation.ets#L65-L71)

**网络视频获取首帧**

在网络视频获取首帧的情况下，需要先将网络视频下载到沙箱，使用avImageGenerator.fetchFrameByTime方式获取首帧图片。

参考代码如下所示：

```
1. import { media } from '@kit.MediaKit'
2. import image from '@ohos.multimedia.image';
3. import { fileIo as fs } from '@kit.CoreFileKit';
4. import { BusinessError, request } from '@kit.BasicServicesKit';

6. @Component
7. struct GetFirstFrameAnimation {
8. @State isPlaying: boolean = false;
9. @State pixelMap: image.PixelMap | undefined = undefined;
10. @State filesDir: string = '';
11. private count: number = 0;
12. // The surfaceID is used for displaying the playback image and needs to be obtained through the XComponent interface.
13. private surfaceID: string = '';
14. // Used to distinguish whether a pattern supports seek operation.
15. private isSeek: boolean = true;
16. xComponentController: XComponentController = new XComponentController();
17. private uiContext: Context = this.getUIContext().getHostContext() as Context;

19. aboutToAppear() {
20. this.filesDir = this.uiContext.filesDir;
21. this.fetchFrameByTimeFromWeb();
22. }

24. fetchFrameByTimeFromWeb() {
25. let path = this.filesDir + 'test1.mp4';
26. if (fs.accessSync(path)) {
27. fs.unlinkSync(path);
28. }
29. // Network Video
30. try {
31. request.downloadFile(this.uiContext, {
32. enableMetered: true,
33. // Some online video formats are not supported, which makes it impossible to parse and read the thumbnail of a certain frame of the video.
34. url: 'xxx.mp4',
35. filePath: this.filesDir + 'test1.mp4'
36. })
37. .then((downloadTask: request.DownloadTask) => {
38. downloadTask.on('fail', (err: number) => {
39. console.error(`Failed to download the task. Code: ${err}`);
40. })
41. downloadTask.on('progress', (receivedSize: number, totalSize: number) => {
42. console.log('download', 'receivedSize:' + (receivedSize / 1024) + 'totalSize:' + (totalSize / 1024));
43. })
44. downloadTask.on('complete', async () => {
45. // Create AVImageGenerator object
46. let avImageGenerator: media.AVImageGenerator = await media.createAVImageGenerator();
47. // Configure avImageGenerator.fdSrc attributes based on album video URI
48. let fileINT = fs.openSync(this.filesDir + '/test1.mp4', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
49. let avFileDescriptor: media.AVFileDescriptor = { fd: fileINT.fd };
50. // Configuration parameter
51. avImageGenerator.fdSrc = avFileDescriptor;
52. // Initialize input parameters
53. let timeUs = 0;
54. let queryOption = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;
55. let param: media.PixelMapParams = {
56. width: 300,
57. height: 300
58. };
59. // Get thumbnail(Promise mode)
60. this.pixelMap = await avImageGenerator.fetchFrameByTime(timeUs, queryOption, param);
61. // Release resources(Promise mode)
62. avImageGenerator.release();
63. fs.closeSync(fileINT);
64. })
65. })
66. .catch((err: BusinessError) => {
67. console.error(`Invoke downloadTask failed, code is ${err.code}, message is ${err.message}`);
68. })
69. } catch (error) {
70. let err = error as BusinessError;
71. console.error(`Invoke downloadFile failed, code is ${err.code}, message is ${err.message}`);
72. }
73. }

75. // Registering Callbacks
76. setAVPlayerCallback(avPlayer: media.AVPlayer) {
77. // SetAVPlayerCallback first frame rendering callback function.
78. avPlayer.on('startRenderFrame', () => {
79. console.log(`AVPlayer start render frame`);
80. })
81. // Seek operation result callback function.
82. avPlayer.on('seekDone', (seekDoneTime: number) => {
83. console.log(`AVPlayer seek succeed, seek time is ${seekDoneTime}`);
84. })
85. // Error callback listening function, when avPlayer encounters an error during operation, call the reset interface to trigger the reset process.
86. avPlayer.on('error', (err: BusinessError) => {
87. console.error(`Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
88. avPlayer.reset(); // Call reset to reset resources and trigger idle status.
89. })
90. // State change callback function
91. avPlayer.on('stateChange', async (state: string, _reason: media.StateChangeReason) => {
92. switch (state) {
93. case 'idle': // Successfully called reset to reset resources, triggering idle status.
94. avPlayer.release();
95. break;
96. case 'initialized': // AVPlayer triggers this status report after setting the playback resource.
97. avPlayer.surfaceId = this.surfaceID; // Set display screen, no need to set when playing pure audio resources.
98. avPlayer.prepare();
99. case 'prepared': // Report this status after successful preparation call.
100. avPlayer.play(); // Call the playback interface to start playing.
101. this.isPlaying = true;
102. break;
103. case 'playing': // Trigger this status report after successful play call.
104. if (this.count !== 0) {
105. if (this.isSeek) {
106. avPlayer.seek(avPlayer.duration); // Seek to the end of the video.
107. } else {
108. // When the playback mode does not support seek operation, continue playing until the end.
109. console.log('AVPlayer wait to play end.')
110. }
111. } else {
112. avPlayer.pause(); // Call the pause interface to pause playback.
113. }
114. this.count++;
115. break;
116. case 'paused': // Call to trigger the status report after pause succeeds.
117. avPlayer.play();
118. break;
119. case 'completed': // Trigger the status report after the playback ends.
120. avPlayer.stop();
121. break;
122. case 'stopped': // Trigger the status report after the stop interface is successfully called.
123. avPlayer.reset(); // Call the reset interface to initialize the avplayer state.
124. break;
125. case 'released':
126. console.log('AVPlayer state released called.');
127. break;
128. default:
129. console.log('AVPlayer state unknown called.');
130. break;
131. }
132. })
133. }

135. async avPlayerLiveDemo() {
136. // Create an avPlayer instance object.
137. let avPlayer: media.AVPlayer = await media.createAVPlayer();
138. // Create a state change callback function.
139. this.setAVPlayerCallback(avPlayer);
140. this.isSeek = false; // SEEK operation is not supported.
141. avPlayer.url = 'xxx.mp4';
142. // avPlayer.url = 'xxx.m3u8'; // Play the HLS live streaming stream.
143. }

145. build() {
146. Column() {
147. Stack({ alignContent: Alignment.TopStart }) {
148. if (!this.isPlaying && this.pixelMap) {
149. Image(this.pixelMap)
150. .width('640px')
151. .height('480px')
152. .zIndex(10)
153. }
154. XComponent({
155. id: 'XComponent',
156. type: XComponentType.SURFACE,
157. controller: this.xComponentController
158. })
159. .width('640px')
160. .height('480px')
161. .zIndex(9)
162. .onLoad(() => {
163. this.surfaceID = this.xComponentController.getXComponentSurfaceId();
164. })
165. }
166. .position({ x: 0, y: 48 })

168. Button('点击播放')
169. .onClick(() => {
170. this.avPlayerLiveDemo();
171. })
172. }
173. }
174. }
```

[GetFirstFrameAnimation.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/MediaLibraryKit/entry/src/main/ets/pages/GetFirstFrameAnimation.ets#L20-L196)
