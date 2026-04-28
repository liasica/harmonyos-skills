---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/streaming-media-playback-development-guide
title: 使用AVPlayer播放流媒体(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 播放 > 使用AVPlayer播放流媒体(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:25+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:1f3bbe9752a600b1f3bd2347f1e2da737cb695c177884524798553bd2ebae227
---

本开发指导将介绍如何使用[AVPlayer](media-kit-intro.md#avplayer)开发流媒体直播和点播功能。示例展示如何完整播放流媒体视频，实现端到端的流媒体资源播放。

本指导仅介绍流媒体播放功能。本地音视频播放等其他场景，请参考[视频播放](video-playback.md)。

## 流媒体支持的格式

| 流媒体协议类型 | 典型链接 | 网络点播 | 网络直播 | 内容保护 |
| --- | --- | --- | --- | --- |
| HLS | https://xxxx/index.m3u8 | 支持 | 支持 | 支持，详见[DRM Kit](drm-overview.md)。 |
| DASH | https://xxxx.mpd | 支持 | - | 支持，详见[DRM Kit](drm-overview.md)。 |
| HTTP/HTTPS | https://xxxx.mp4 | 支持 | - | - |
| HTTP-FLV | https://xxxx.flv | 支持 | 支持 | - |

## 开发步骤

创建AVPlayer、设置播放资源和窗口、设置播放参数（音量/倍速/缩放模式）、进行播放控制（播放/暂停/跳转/停止）、重置资源、销毁资源。应用开发时，开发者可通过AVPlayer的state属性主动获取当前状态，或使用on('stateChange')方法监听状态变化。视频播放器处于错误状态时执行操作，可能导致异常或未定义行为。状态详细参见[AVPlayerState](../harmonyos-references/arkts-apis-media-t.md#avplayerstate9)。具体步骤如下：

1. 创建实例createAVPlayer()，初始化AVPlayer为idle状态。
2. 设置业务需要的监听事件，搭配全流程场景使用。支持的监听事件包括：

   | 事件类型 | 说明 |
   | --- | --- |
   | stateChange | 必要事件，监听播放器的state属性改变。  需要播放器在idle状态下、未调用设置资源接口前完成设置监听，若在调用设置资源接口后再设置监听，可能导致无法收到资源设置过程中上报的stateChange事件。 |
   | error | 必要事件，监听播放器的错误信息。  需要播放器在idle状态下、未调用设置资源接口前完成设置监听，若在调用设置资源接口后再设置监听，可能导致无法收到资源设置过程中上报的error事件。 |
   | durationUpdate | 监听进度条长度，刷新资源时长。 |
   | timeUpdate | 监听进度条当前位置，刷新当前时间。 |
   | seekDone | 监听seek()请求完成情况。  当使用seek()跳转到指定播放位置后，如果seek操作成功，将上报该事件。 |
   | speedDone | 监听setSpeed()请求完成情况。  当使用setSpeed()设置播放倍速后，如果setSpeed操作成功，将上报该事件。 |
   | volumeChange | 监听setVolume()请求完成情况。  当使用setVolume()调节播放音量后，如果setVolume操作成功，将上报该事件。 |
   | bufferingUpdate | 监听网络播放缓冲信息，上报缓冲百分比以及缓存播放进度。 |
   | audioInterrupt | 监听音频焦点切换信息，搭配属性audioInterruptMode使用。  如果当前设备存在多个音频正在播放，音频焦点被切换（即播放其他媒体如通话等）时将上报该事件，应用可以及时处理。 |
3. 设置资源：[使用AVPlayer设置播放URL](playback-url-setting-method.md)，使AVPlayer进入initialized状态。

   说明

   下面代码示例中的url仅作示意，开发者需根据实际情况确认资源有效性并设置。

   * 使用网络播放路径，需[声明权限](declare-permissions.md)：ohos.permission.INTERNET。
   * 使用支持的播放格式和协议。
4. 设置窗口：获取并设置SurfaceID属性，用于配置显示画面。

   应用从XComponent组件获取surfaceID，获取方式请参考[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)。
5. 准备播放：调用prepare()，使AVPlayer进入prepared状态，此时可获取duration，设置缩放模式、音量等。
6. 进行视频播放控制：播放play()，暂停pause()，跳转seek()，停止stop() 等操作。
7. （可选）更换资源：调用reset()重置资源，使AVPlayer重新进入idle状态，允许更换资源url。
8. 退出播放：调用release()销毁实例，使AVPlayer进入released状态，退出播放。

## 注意事项

播放流媒体的标准流程如上述开发步骤所示。不同的流媒体格式在实际开发的过程中存在差异，本节将详细描述这些差异，包括视频起播策略的设置和音视频轨道的切换。

### 流媒体缓冲状态

当下载速率低于片源的码率时，会出现卡顿。此时，播放器检测到缓冲区数据不足，会先缓冲一些数据再播放，避免连续卡顿。一次卡顿对应的缓冲事件上报过程为：BUFFERING\_START-> BUFFERING\_PERCENT 0 -> ... -> BUFFERING\_PERCENT 100 -> BUFFERING\_END。CACHED\_DURATION在卡顿过程和播放过程中都会持续上报，直至下载至资源末尾。详见[BufferingInfoType缓冲事件类型枚举](../harmonyos-references/arkts-apis-media-e.md#bufferinginfotype8)。

监听当前bufferingUpdate缓冲状态示例代码：

```
1. import { media } from '@kit.MediaKit';
2. // 类成员定义avPlayer
3. private avPlayer: media.AVPlayer | null = null;

5. // 创建avPlayer实例对象。
6. this.avPlayer = await media.createAVPlayer();
7. // 监听当前bufferingUpdate缓冲状态。
8. this.avPlayer.on('bufferingUpdate', (infoType : media.BufferingInfoType, value : number) => {
9. console.info(`AVPlayer bufferingUpdate, infoType is ${infoType}, value is ${value}.`);
10. })
```

### HLS切换码率

当前流媒体HLS协议流支持多码率播放，默认情况下，播放器会根据网络下载速度选择合适的码率。

1. 通过[on('availableBitrates')](../harmonyos-references/arkts-apis-media-avplayer.md#onavailablebitrates9)监听当前HLS协议流可用的码率。如果监听的码率列表长度为0，则不支持设置指定码率。

   ```
   1. import { media } from '@kit.MediaKit';
   2. // 类成员定义avPlayer
   3. private avPlayer: media.AVPlayer | null = null;

   5. // 创建avPlayer实例对象。
   6. this.avPlayer = await media.createAVPlayer();
   7. // 监听当前HLS协议流可用的码率。
   8. this.avPlayer.on('availableBitrates', (bitrates: Array<number>) => {
   9. console.info('availableBitrates called, and availableBitrates length is: ' + bitrates.length);
   10. })
   ```
2. 通过[setBitrate](../harmonyos-references/arkts-apis-media-avplayer.md#setbitrate9)接口设置播放码率。若用户设置的码率不在可用码率中，播放器将选择最小且最接近的码率。该接口只能在prepared/playing/paused/completed状态下调用，可通过监听[bitrateDone](../harmonyos-references/arkts-apis-media-avplayer.md#onbitratedone9)事件确认是否生效。

   ```
   1. import { media } from '@kit.MediaKit';
   2. // 类成员定义avPlayer
   3. private avPlayer: media.AVPlayer | null = null;

   5. // 创建avPlayer实例对象。
   6. this.avPlayer = await media.createAVPlayer();
   7. // 监听码率设置是否生效。
   8. this.avPlayer.on('bitrateDone', (bitrate: number) => {
   9. console.info('bitrateDone called, and bitrate value is: ' + bitrate);
   10. })
   11. // 设置播放码率。
   12. this.bitrate: number = 96000;
   13. this.avPlayer.setBitrate(this.bitrate);
   ```

### DASH设置视频起播策略

为了保证在弱网环境下的播放体验，AVPlayer将默认选择最低的视频分辨率开始播放，随后依据网络状况自动调整。开发者可以根据具体需求，自定义DASH视频的起播策略，包括设定视频的宽度、高度以及色彩格式等参数。

下述示例代码描述了设置视频宽度1920px、高度1080px起播。AVPlayer会选择MPD资源中一路分辨率为1920x1080的视频资源进行播放。

```
1. import { media } from '@kit.MediaKit';

3. let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://test.cn/dash/aaa.mpd",  {"User-Agent" : "User-Agent-Value"});
4. let playbackStrategy : media.PlaybackStrategy = {preferredWidth: 1920, preferredHeight: 1080};
5. this.avPlayer.setMediaSource(mediaSource, playbackStrategy);
```

### DASH切换音视频轨道

DASH流媒体资源包含多路不同分辨率、码率、采样率、编码格式的音频、视频及字幕资源。默认情况下，AVPlayer会依据网络状况自动切换不同码率的视频轨道。开发者可根据需求选择指定的音视频轨道播放，此时自适应码率切换策略将失效。

1. 设置selectTrack生效的监听事件[trackChange](../harmonyos-references/arkts-apis-media-avplayer.md#ontrackchange12)。

   ```
   1. import { media } from '@kit.MediaKit';
   2. // 类成员定义avPlayer
   3. private avPlayer: media.AVPlayer | null = null;

   5. // 创建avPlayer实例对象。
   6. this.avPlayer = await media.createAVPlayer();
   7. this.avPlayer.on('trackChange', (index: number, isSelect: boolean) => {
   8. console.info(`trackChange info, index: ${index}, isSelect: ${isSelect}`);
   9. })
   ```
2. 调用[getTrackDescription](../harmonyos-references/arkts-apis-media-avplayer.md#gettrackdescription9)获取所有音视频轨道列表。开发者可根据实际需求，基于[MediaDescription](../harmonyos-references/arkts-apis-media-i.md#mediadescription8)各字段信息，确定目标轨道索引。

   ```
   1. // 以获取1080p视频轨道索引为例。
   2. import { media } from '@kit.MediaKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. public videoTrackIndex: number = 0;
   5. // 类成员定义avPlayer
   6. private avPlayer: media.AVPlayer | null = null;

   8. // 创建avPlayer实例对象。
   9. this.avPlayer = await media.createAVPlayer();
   10. this.avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
   11. if (arrList != null) {
   12. for (let i = 0; i < arrList.length; i++) {
   13. let propertyIndex: Object = arrList[i][media.MediaDescriptionKey.MD_KEY_TRACK_INDEX];
   14. let propertyType: Object = arrList[i][media.MediaDescriptionKey.MD_KEY_TRACK_TYPE];
   15. let propertyWidth: Object = arrList[i][media.MediaDescriptionKey.MD_KEY_WIDTH];
   16. let propertyHeight: Object = arrList[i][media.MediaDescriptionKey.MD_KEY_HEIGHT];
   17. if (propertyType == media.MediaType.MEDIA_TYPE_VID && propertyWidth == 1920 && propertyHeight == 1080) {
   18. this.videoTrackIndex = parseInt(propertyIndex?.toString()); // 获取1080p视频轨道索引。
   19. }
   20. }
   21. } else {
   22. console.error(`getTrackDescription fail, error:${error}`);
   23. }
   24. });
   ```
3. 在音视频播放过程中调用[selectTrack](../harmonyos-references/arkts-apis-media-avplayer.md#selecttrack12)选择对应的音视频轨道，或者调用[deselectTrack](../harmonyos-references/arkts-apis-media-avplayer.md#deselecttrack12)取消选择的音视频轨道。

   ```
   1. import { media } from '@kit.MediaKit';
   2. public videoTrackIndex: number = 0;
   3. // 类成员定义avPlayer
   4. private avPlayer: media.AVPlayer | null = null;

   6. // 创建avPlayer实例对象。
   7. this.avPlayer = await media.createAVPlayer();
   8. // 切换至目标视频轨道。
   9. this.avPlayer.selectTrack(this.videoTrackIndex);
   10. // 取消选择目标视频轨道。
   11. // this.avPlayer.deselectTrack(this.videoTrackIndex);
   ```

## 异常场景说明

使用AVPlayer播放流媒体过程中断网时，流媒体模块会根据返回的错误码、服务器响应时间和请求次数等因素综合处理。若错误码类型属于不进行请求重试的类型，会向应用上报对应的错误码。如果错误码类型需要进行请求重试，会在30s内进行至多10次的请求重试。如果请求重试次数超过10次，或重试总时长超过30秒，会向应用上报对应的错误码。如果请求重试成功，则继续播放。

## 运行完整示例

参考以下示例，完整地播放一个流媒体视频。

1. 新建工程，下载[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVPlayer/AVPlayerArkTSStreamingMedia)，并将示例工程的以下资源复制到对应目录。

   ```
   1. AVPlayerArkTSAudio
   2. entry/src/main/ets/
   3. └── pages
   4. └── Index.ets (播放界面)
   5. entry/src/main/resources/
   6. ├── base
   7. │   ├── element
   8. │   │   ├── color.json
   9. │   │   ├── float.json
   10. │   │   └── string.json
   11. │   └── media
   12. │       ├── ic_video_play.svg  (播放键图片资源)
   13. │       └── ic_video_pause.svg (暂停键图片资源)
   14. └── rawfile
   15. └── test1.mp4 （视频资源）
   ```
2. 在/entry/src/main/module.json5中，申请使用网络的权限（或直接替换为示例工程的module.json5）。

   ```
   1. "requestPermissions": [
   2. {
   3. "name": "ohos.permission.INTERNET"
   4. },
   5. {
   6. "name": "ohos.permission.GET_WIFI_INFO"
   7. }
   8. ]
   ```
3. 通过注释、解注释/entry/src/main/ets/pages/Index.ets中的上文示例的各种情况，编译并运行。

## 开发示例

```
1. import { media } from '@kit.MediaKit';
2. import { emitter } from '@kit.BasicServicesKit';
3. import { display } from '@kit.ArkUI';

5. const TIME_ONE = 60000; // 1分钟的毫秒数。
6. const TIME_TWO = 1000;  // 1秒的毫秒数。
7. const SET_INTERVAL = 1000; // 每秒更新一次当前播放时间。
8. const SPEED_ZERO: number = 0; // 对应1.00x。
9. const SPEED_ONE: number = 1;  // 对应1.25x。
10. const SPEED_TWO: number = 2;  // 对应1.75x。
11. const SPEED_THREE: number = 3; // 对应2.00x。
12. const PROPORTION: number = 0.99;
13. let innerEventFalse: emitter.InnerEvent = {
14. eventId: 1,
15. priority: emitter.EventPriority.HIGH
16. };
17. let innerEventTrue: emitter.InnerEvent = {
18. eventId: 2,
19. priority: emitter.EventPriority.HIGH
20. };

22. let innerEventWH: emitter.InnerEvent = {
23. eventId: 3,
24. priority: emitter.EventPriority.HIGH
25. };
26. @Entry
27. @Component
28. struct Index {
29. private avPlayer: media.AVPlayer | null = null;
30. private context: Context | undefined = undefined;
31. public videoTrackIndex: number = 0;
32. public bitrate: number = 0;
33. @State durationTime: number = 0;
34. @State currentTime: number = 0;
35. @State percent: number = 0;
36. @State isSwiping: boolean = false;
37. @State tag: string = 'StreamingMedia';
38. private surfaceId: string = '';
39. @State speedSelect: number = -1;
40. public intervalID: number = -1;
41. @State windowWidth: number = 300;
42. @State windowHeight: number = 300;
43. @State surfaceW: number | null = null;
44. @State surfaceH: number | null = null;
45. @State isPaused: boolean = true;
46. @State XComponentFlag: boolean = false;
47. getDurationTime(): number {
48. return this.durationTime;
49. }

51. getCurrentTime(): number {
52. return this.currentTime;
53. }

55. timeConvert(time: number): string {
56. let min: number = Math.floor(time / TIME_ONE);
57. let second: string = ((time % TIME_ONE) / TIME_TWO).toFixed(0);
58. // return `${min}:${(+second < TIME_THREE ? '0' : '') + second}`;
59. second = second.padStart(2, '0');
60. return `${min}:${second}`;
61. }

63. async msleepAsync(ms: number): Promise<boolean> {
64. return new Promise((resolve, reject) => {
65. setTimeout(() => {
66. resolve(true)
67. }, ms)
68. })
69. }

71. async avSetupStreamingMediaVideo() {
72. if (this.context == undefined) return;
73. // 创建avPlayer实例对象。
74. this.avPlayer = await media.createAVPlayer();

76. // 创建状态机变化回调函数。
77. await this.setAVPlayerCallback((avPlayer: media.AVPlayer) => {
78. this.percent = avPlayer.width / avPlayer.height;
79. this.setVideoWH();
80. this.durationTime = this.getDurationTime();
81. setInterval(() => { // 更新当前时间。
82. if (!this.isSwiping) {
83. this.currentTime = this.getCurrentTime();
84. }
85. }, SET_INTERVAL);
86. });

88. // 情况一：HTTP视频播放。
89. this.avPlayer.url = "http://media.iyuns.top:1000/http/720p_1m.mp4";

91. // 情况二：HLS视频播放。
92. // this.avPlayer.url = "http://media.iyuns.top:1000/720-270-480.m3u8";

94. // 情况三：DASH视频播放。
95. // this.avPlayer.url = "http://media.iyuns.top:1000/dash/720p/720-1/720-1.mpd";

97. // 情况四：通过setMediaSource设置自定义头域及播放优选参数实现初始播放参数设置，以流媒体HTTP点播为例。
98. /*
99. let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://media.iyuns.top:1000/http/720p_1m.mp4", {"":""});
100. // 设置播放策略，设置为缓冲区数据为20s。
101. let playbackStrategy : media.PlaybackStrategy = {preferredBufferDuration: 20};
102. // 为avPlayer设置媒体来源和播放策略。
103. this.avPlayer.setMediaSource(mediaSource, playbackStrategy);
104. **/

106. // 情况五：HLS切码率。
107. /*
108. this.avPlayer.url = "https://upftimae.dailyworkout.cn/videos/course/c800f81a209b5ee7891f1128ed301db/4/master.m3u8";
109. let bitrate: number = 0;
110. // 监听当前HLS协议流可用的码率。
111. this.avPlayer.on('availableBitrates', (bitrates: Array<number>) => {
112. console.info('availableBitrates called, and availableBitrates length is: ' + bitrates.length);
113. this.bitrate = bitrates[0]; // 保存需要切换的码率。
114. })
115. // 监听码率设置是否生效。
116. this.avPlayer.on('bitrateDone', (bitrate: number) => {
117. console.info('bitrateDone called, and bitrate value is: ' + bitrate);
118. })
119. **/

121. // 情况六：DASH切换音视频轨道。
122. /*
123. this.avPlayer.url = "http://poster-inland.hwcloudtest.cn/AiMaxEngine/ProductionEnvVideo/DASH_SDR_MultiAudio_MultiSubtitle_yinHeHuWeiDui3/DASH_SDR_MultiAudio_MultiSubtitle_yinHeHuWeiDui3.mpd";
124. this.avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
125. if (arrList != null) {
126. for (let i = 0; i < arrList.length; i++) {
127. let propertyIndex: Object = arrList[i][media.MediaDescriptionKey.MD_KEY_TRACK_INDEX];
128. let propertyType: Object = arrList[i][media.MediaDescriptionKey.MD_KEY_TRACK_TYPE];
129. let propertyWidth: Object = arrList[i][media.MediaDescriptionKey.MD_KEY_WIDTH];
130. let propertyHeight: Object = arrList[i][media.MediaDescriptionKey.MD_KEY_HEIGHT];
131. if (propertyType == media.MediaType.MEDIA_TYPE_VID && propertyWidth == 1920 && propertyHeight == 1080) {
132. this.videoTrackIndex = parseInt(propertyIndex.toString()); // 获取1080p视频轨道索引。
133. }
134. }
135. } else {
136. console.error(`getTrackDescription fail, error:${error}`);
137. }
138. });
139. **/
140. }

142. // HLS切换码率。
143. changeBitrate(bitrate: number) {
144. if (this.avPlayer == null) {
145. return;
146. }
147. // 设置播放码率。
148. try {
149. this.avPlayer.setBitrate(bitrate);
150. } catch (error) {
151. console.error(`${this.tag}: setBitrate failed, error message is = ${JSON.stringify(error.message)}`);
152. }
153. }

155. // DASH切换音视频轨道。
156. changeTrack(track: number) {
157. if (this.avPlayer == null) {
158. return;
159. }
160. // 切换至目标视频轨道。
161. try {
162. this.avPlayer.selectTrack(track);
163. } catch (error) {
164. console.error(`${this.tag}: selectTrack failed, error message is = ${JSON.stringify(error.message)}`);
165. }
166. // 取消选择目标视频轨道。
167. /*
168. try {
169. this.avPlayer.deselectTrack(track);
170. } catch (error) {
171. console.error(`${this.tag}: deselectTrack failed, error message is = ${JSON.stringify(error.message)}`);
172. }
173. **/
174. }

176. avPlay(): void {
177. if (this.avPlayer) {
178. try {
179. this.avPlayer.play();
180. } catch (e) {
181. console.error(`${this.tag}: avPlay = ${JSON.stringify(e)}`);
182. }
183. }
184. }

186. avPause(): void {
187. if (this.avPlayer) {
188. try {
189. this.avPlayer.pause();
190. console.info(`${this.tag}: avPause==`);
191. } catch (e) {
192. console.error(`${this.tag}: avPause== ${JSON.stringify(e)}`);
193. }
194. }
195. }

197. async avSeek(seekTime: number, mode: SliderChangeMode): Promise<void> {
198. if (this.avPlayer) {
199. try {
200. console.info(`${this.tag}: videoSeek  seekTime== ${seekTime}`);
201. this.avPlayer.seek(seekTime, 2);
202. this.currentTime = seekTime;
203. } catch (e) {
204. console.error(`${this.tag}: videoSeek== ${JSON.stringify(e)}`);
205. }
206. }
207. }

209. avSetSpeed(speed: number): void {
210. if (this.avPlayer) {
211. try {
212. this.avPlayer.setSpeed(speed);
213. console.info(`${this.tag}: avSetSpeed enum ${speed}`);
214. } catch (e) {
215. console.error(`${this.tag}: avSetSpeed == ${JSON.stringify(e)}`);
216. }
217. }
218. }

220. // 注册avplayer回调函数。
221. async setAVPlayerCallback(callback: (avPlayer: media.AVPlayer) => void, vType?: number): Promise<void> {
222. // seek操作结果回调函数。
223. if (this.avPlayer == null) {
224. console.error(`${this.tag}: avPlayer has not init!`);
225. return;
226. }
227. this.avPlayer.on('seekDone', (seekDoneTime) => {
228. console.info(`${this.tag}: setAVPlayerCallback AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
229. });
230. this.avPlayer.on('speedDone', (speed) => {
231. console.info(`${this.tag}: setAVPlayerCallback AVPlayer speedDone, speed is ${speed}`);
232. });
233. // error回调监听函数,当avPlayer在操作过程中出现错误时调用reset接口触发重置流程。
234. this.avPlayer.on('error', (err) => {
235. console.error(`${this.tag}: setAVPlayerCallback Invoke avPlayer failed ${JSON.stringify(err)}`);
236. if (this.avPlayer == null) {
237. console.error(`${this.tag}: avPlayer has not init on error`);
238. return;
239. }
240. this.avPlayer.reset();
241. });
242. // 状态机变化回调函数。
243. this.avPlayer.on('stateChange', async (state, reason) => {
244. if (this.avPlayer == null) {
245. console.info(`${this.tag}: avPlayer has not init on state change`);
246. return;
247. }
248. switch (state) {
249. case 'idle': // 成功调用reset接口后触发该状态机上报。
250. console.info(`${this.tag}: setAVPlayerCallback AVPlayer state idle called.`);
251. break;
252. case 'initialized': // avplayer 设置播放源后触发该状态上报。
253. console.info(`${this.tag}: setAVPlayerCallback AVPlayer state initialized called.`);
254. if (this.surfaceId) {
255. this.avPlayer.surfaceId = this.surfaceId; // 设置显示画面，当播放的资源为纯音频时无需设置。
256. console.info(`${this.tag}: setAVPlayerCallback this.avPlayer.surfaceId = ${this.avPlayer.surfaceId}`);
257. this.avPlayer.prepare();
258. }
259. break;
260. case 'prepared': // prepare调用成功后上报该状态机。
261. console.info(`${this.tag}: setAVPlayerCallback AVPlayer state prepared called.`);
262. this.avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
263. console.info(`${this.tag}: bufferingUpdate called, infoType value: ${infoType}, value:${value}}`);
264. })
265. this.durationTime = this.avPlayer.duration;
266. this.currentTime = this.avPlayer.currentTime;
267. this.avPlayer.play(); // 调用播放接口开始播放。
268. console.info(`${this.tag}:
269. setAVPlayerCallback speedSelect: ${this.speedSelect}, duration: ${this.durationTime}`);
270. if (this.speedSelect != -1) {
271. switch (this.speedSelect) {
272. case SPEED_ZERO:
273. this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_00_X);
274. break;
275. case SPEED_ONE:
276. this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_25_X);
277. break;
278. case SPEED_TWO:
279. this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_75_X);
280. break;
281. case SPEED_THREE:
282. this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_2_00_X);
283. break;
284. }
285. }
286. callback(this.avPlayer);
287. break;
288. case 'playing': // play成功调用后触发该状态机上报。
289. console.info(`${this.tag}: setAVPlayerCallback AVPlayer state playing called.`);
290. if (this.intervalID != -1) {
291. clearInterval(this.intervalID)
292. }
293. this.intervalID = setInterval(() => { // 更新当前时间。
294. AppStorage.setOrCreate('durationTime', this.durationTime);
295. AppStorage.setOrCreate('currentTime', this.currentTime);
296. }, 100);
297. let eventDataTrue: emitter.EventData = {
298. data: {
299. 'flag': true
300. }
301. };
302. let innerEventTrue: emitter.InnerEvent = {
303. eventId: 2,
304. priority: emitter.EventPriority.HIGH
305. };
306. emitter.emit(innerEventTrue, eventDataTrue);
307. break;
308. case 'completed': // 播放结束后触发该状态机上报。
309. console.info(`${this.tag}: setAVPlayerCallback AVPlayer state completed called.`);
310. let eventDataFalse: emitter.EventData = {
311. data: {
312. 'flag': false
313. }
314. };
315. let innerEvent: emitter.InnerEvent = {
316. eventId: 1,
317. priority: emitter.EventPriority.HIGH
318. };
319. emitter.emit(innerEvent, eventDataFalse);
320. if (this.intervalID != -1) {
321. clearInterval(this.intervalID)
322. }
323. this.avPlayer.off('bufferingUpdate')
324. AppStorage.setOrCreate('currentTime', this.durationTime);
325. break;
326. case 'released':
327. console.info(`${this.tag}: setAVPlayerCallback released called.`);
328. break
329. case 'stopped':
330. console.info(`${this.tag}: setAVPlayerCallback AVPlayer state stopped called.`);
331. break
332. case 'error':
333. console.error(`${this.tag}: setAVPlayerCallback AVPlayer state error called.`);
334. break
335. case 'paused':
336. console.info(`${this.tag}: setAVPlayerCallback AVPlayer state paused called.`);
337. break
338. default:
339. console.info(`${this.tag}: setAVPlayerCallback AVPlayer state unknown called.`);
340. break;
341. }
342. });
343. // 时间上报监听函数。
344. this.avPlayer.on('timeUpdate', (time: number) => {
345. this.currentTime = time;
346. });
347. }

349. aboutToAppear() {
350. this.windowWidth = display.getDefaultDisplaySync().width;
351. this.windowHeight = display.getDefaultDisplaySync().height;
352. if (this.percent >= 1) { // 横向视频。
353. this.surfaceW = Math.round(this.windowWidth * PROPORTION);
354. this.surfaceH = Math.round(this.surfaceW / this.percent);
355. } else { // 纵向视频。
356. this.surfaceH = Math.round(this.windowHeight * PROPORTION);
357. this.surfaceW = Math.round(this.surfaceH * this.percent);
358. }
359. this.isPaused = true;
360. this.context = this.getUIContext().getHostContext();
361. }

363. aboutToDisappear() {
364. if (this.avPlayer == null) {
365. console.info(`${this.tag}: avPlayer has not init aboutToDisappear`);
366. return;
367. }
368. this.avPlayer.release((err) => {
369. if (err == null) {
370. console.info(`${this.tag}: videoRelease release success`);
371. } else {
372. console.error(`${this.tag}: videoRelease release failed, error message is = ${JSON.stringify(err.message)}`);
373. }
374. });
375. emitter.off(innerEventFalse.eventId);
376. }

378. onPageHide() {
379. this.avPause();
380. this.isPaused = false;
381. }

383. onPageShow() {
384. emitter.on(innerEventTrue, (res: emitter.EventData) => {
385. if (res.data) {
386. this.isPaused = res.data.flag;
387. this.XComponentFlag = res.data.flag;
388. }
389. });
390. emitter.on(innerEventFalse, (res: emitter.EventData) => {
391. if (res.data) {
392. this.isPaused = res.data.flag;
393. }
394. });
395. emitter.on(innerEventWH, (res: emitter.EventData) => {
396. if (res.data) {
397. this.windowWidth = res.data.width;
398. this.windowHeight = res.data.height;
399. this.setVideoWH();
400. }
401. });
402. }

404. setVideoWH(): void {
405. if (this.percent >= 1) { // 横向视频。
406. this.surfaceW = Math.round(this.windowWidth * PROPORTION);
407. this.surfaceH = Math.round(this.surfaceW / this.percent);
408. } else { // 纵向视频。
409. this.surfaceH = Math.round(this.windowHeight * PROPORTION);
410. this.surfaceW = Math.round(this.surfaceH * this.percent);
411. }
412. }

414. @Builder
415. CoverXComponent() {
416. // ...
417. }

419. build() {
420. // ...
421. }
422. }
```
