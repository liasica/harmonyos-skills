---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/playback-url-setting-method
title: 使用AVPlayer设置播放URL(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 播放 > 使用AVPlayer设置播放URL(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7a51bc9a19bd21f8721d7ad6b141663888812fa75d85cfcd45e10ecc94164073
---

本开发指导将介绍如何使用AVPlayer开发播放功能，在不同的场景下如何设置URL。

当前指导仅介绍播放URL设置方法，其他场景及完整示例代码，请参考[视频播放](video-playback.md)。

当前开发指导将提供以下设置播放URL的方法：

* [流媒体播放场景下设置URL](playback-url-setting-method.md#流媒体播放场景下设置url)
* [本地Raw文件播放场景下设置URL](playback-url-setting-method.md#本地raw文件播放场景下设置url)

## 流媒体播放场景下设置URL

**情况一：播放HTTP/HTTPS媒体资源**

```
1. import { media } from '@kit.MediaKit';
2. // 类成员定义avPlayer。
3. private avPlayer: media.AVPlayer | null = null;

5. // 在业务函数中（示例工程函数名为avSetupURL）：
6. // 创建avPlayer实例对象。
7. this.avPlayer = await media.createAVPlayer();

9. // 设置对应的播放url。
10. let url = 'https://xxx.xxx.xxx.mp4';
11. if (this.avPlayer == null) {
12. return;
13. }
14. this.avPlayer.url = url;
```

**情况二：HLS媒体资源播放（点播/直播）**

```
1. import { media } from '@kit.MediaKit';
2. // 类成员定义avPlayer。
3. private avPlayer: media.AVPlayer | null = null;

5. // 在业务函数中（示例工程函数名为avSetupURL）：
6. // 创建avPlayer实例对象。
7. this.avPlayer = await media.createAVPlayer();

9. // 设置对应的播放url。
10. let url = 'https://xxx.xxx.xxx.xxx:xx/xx/index.m3u8';
11. if (this.avPlayer == null) {
12. return;
13. }
14. this.avPlayer.url = url;
```

**情况三：设置HTTP请求头信息播放**

当服务器需要校验HTTP请求头信息时，可通过[createMediaSourceWithUrl](../harmonyos-references/arkts-apis-media-f.md#mediacreatemediasourcewithurl12)设置HTTP请求头信息。

```
1. import { media } from '@kit.MediaKit';
2. // 类成员定义avPlayer。
3. private avPlayer: media.AVPlayer | null = null;

5. // 在业务函数中（示例工程函数名为avSetupURL）：
6. // 创建avPlayer实例对象。
7. this.avPlayer = await media.createAVPlayer();

9. // 设置对应的播放url。
10. let url = 'https://xxx.xxx.xxx.xxx:xx/xx/index.m3u8';
11. // 创建mediaSource实例对象，设置媒体来源，定制HTTP请求，如需要，可以键值对的形式设置User-Agent、Cookie、Referer等字段。
12. let mediaSource : media.MediaSource = media.createMediaSourceWithUrl(url,
13. {"User-Agent" : "User-Agent-Value", "Cookie" : "Cookie-Value", "Referer" : "Referer-Value"});
14. // 设置播放策略，设置缓冲区数据量为3s。
15. let playbackStrategy : media.PlaybackStrategy =
16. {preferredWidth: 1, preferredHeight: 2, preferredBufferDuration: 3, preferredHdr: false};
17. // 为avPlayer设置媒体来源和播放策略。
18. this.avPlayer.setMediaSource(mediaSource, playbackStrategy);
```

**情况四：通过本地Raw文件中的m3u8文件播放在线流媒体资源**

当应用需要通过解析本地Raw文件中的m3u8文件，播放在线流媒体资源时，可以通过[resourceManager.getRawFd](../harmonyos-references/js-apis-resource-manager.md#getrawfd9)获取文件描述符，将其拼接成fdUrl，并通过[setMimeType](../harmonyos-references/arkts-apis-media-mediasource.md#setmimetype12)设置MIME类型为APPLICATION\_M3U8。

```
1. import { media } from '@kit.MediaKit';
2. import { common } from '@kit.AbilityKit';
3. // 类成员定义avPlayer和context。
4. private avPlayer: media.AVPlayer | null = null;
5. private context: common.UIAbilityContext | undefined = undefined;
6. // 在业务函数中（示例工程函数名为avSetupURL）：
7. // 创建avPlayer实例对象。
8. this.avPlayer = await media.createAVPlayer();
9. this.context = this.getUIContext().getHostContext() as common.UIAbilityContext;
10. // 通过本地m3u8文件名，获取文件描述符。
11. let fileDescriptor = await this.context.resourceManager.getRawFd('xxx.m3u8');
12. // 用文件描述符构造本地m3u8的URL。
13. let fdUrl : string = "fd://" + fileDescriptor.fd +
14. "?offset=" + fileDescriptor.offset + "&size=" + fileDescriptor.length;
15. // 按需设置HTTP请求头。
16. let headers : Record<string,string> = {"User-Agent" : "User-Agent-Value", "Cookie" : "Cookie-Value"};
17. // 通过本地m3u8的URL和HTTP请求头构造mediaSource媒体来源。
18. let mediaSource : media.MediaSource = media.createMediaSourceWithUrl(fdUrl, headers);

20. // 设置媒体MIME类型为APPLICATION_M3U8。
21. let mimeType : media.AVMimeTypes = media.AVMimeTypes.APPLICATION_M3U8;
22. mediaSource?.setMimeType(mimeType);

24. // 设置播放策略，设置缓冲区数据量为20s。
25. let playbackStrategy : media.PlaybackStrategy = {preferredBufferDuration: 20};
26. // 为avPlayer设置媒体来源和播放策略。
27. this.avPlayer.setMediaSource(mediaSource, playbackStrategy);
```

**情况五：通过应用沙箱中的m3u8文件播放在线流媒体资源**

当应用需要通过解析应用沙箱中的m3u8文件，播放在线流媒体资源时，可以通过[fileIo.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)获取文件句柄，将其拼接成fdUrl，并通过[setMimeType](../harmonyos-references/arkts-apis-media-mediasource.md#setmimetype12)设置MIME类型为APPLICATION\_M3U8。

```
1. import { media } from '@kit.MediaKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';
4. // 类成员定义avPlayer和context。
5. private avPlayer: media.AVPlayer | null = null;
6. private context: common.UIAbilityContext | undefined = undefined;
7. private m3u8FileName: string = '';

9. // 在业务函数中（示例工程函数名为avSetupURL）：
10. // 创建avPlayer实例对象。
11. this.avPlayer = await media.createAVPlayer();
12. this.context = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. // 通过UIAbilityContext获取沙箱地址filesDir，以Stage模型为例。
14. let m3u8FileName = '';
15. let filePath = `${this.context.filesDir}/${m3u8FileName}`;
16. // 通过fs.openSync获取文件句柄。
17. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
18. let fd : string = file.fd.toString();
19. // 用文件句柄构造本地m3u8的URL。
20. let fdUrl : string = "fd://" + fd + "?offset=" + "0" + "&size=" + "0";

22. // 按需设置HTTP请求头。
23. let headers : Record<string,string> = {"User-Agent" : "User-Agent-Value", "Cookie" : "Cookie-Value"};
24. // 通过本地m3u8的URL和HTTP请求头构造mediaSource媒体来源。
25. let mediaSource : media.MediaSource = media.createMediaSourceWithUrl(fdUrl, headers);

27. // 设置媒体MIME类型为APPLICATION_M3U8。
28. let mimeType : media.AVMimeTypes = media.AVMimeTypes.APPLICATION_M3U8;
29. mediaSource?.setMimeType(mimeType);

31. // 设置播放策略，设置缓冲区数据量为20s。
32. let playbackStrategy : media.PlaybackStrategy = {preferredBufferDuration: 20};
33. // 为avPlayer设置媒体来源和播放策略。
34. this.avPlayer.setMediaSource(mediaSource, playbackStrategy);
```

## 本地raw文件播放场景下设置URL

**情况一：应用沙箱文件播放**

```
1. import { media } from '@kit.MediaKit';
2. import { fileIo } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';
4. // 类成员定义avPlayer，context和fileName。
5. private avPlayer: media.AVPlayer | null = null;
6. private context: common.UIAbilityContext | undefined = undefined;
7. private fileName: string = '';

9. // 在业务函数中（示例工程函数名为avSetupURL）：
10. // 创建avPlayer实例对象。
11. this.avPlayer = await media.createAVPlayer();
12. this.context = this.getUIContext().getHostContext() as common.UIAbilityContext;
13. let fdPath = 'fd://';
14. let fileName = 'test.mp4'; // test.mp4为应用文件目录下的预置资源，需要开发者根据实际情况进行替换。
15. // 通过UIAbilityContext获取沙箱地址filesDir，以Stage模型为例。
16. let path = `${this.context?.filesDir}/${this.fileName}`;
17. // 打开相应的资源文件地址获取fd，并为url赋值触发initialized状态机上报。
18. let file = await fileIo.open(path);
19. fdPath = fdPath + '' + file.fd;
20. this.avPlayer.url = fdPath;
```

**情况二：本地文件播放**

说明

当使用AVPlayer播放本地资源时，AVPlayer会独占此fd。

```
1. import { media } from '@kit.MediaKit';
2. import { common } from '@kit.AbilityKit';
3. // 类成员定义avPlayer，context和fileName。
4. private avPlayer: media.AVPlayer | null = null;
5. private fileName: string = '';
6. private context: common.UIAbilityContext | undefined = undefined;
7. // 在业务函数中（示例工程函数名为avSetupURL）：
8. // 创建avPlayer实例对象。
9. this.avPlayer = await media.createAVPlayer();
10. this.context = this.getUIContext().getHostContext() as common.UIAbilityContext;
11. // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址。
12. // 返回类型为{fd,offset,length},fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度。
13. let fileName = 'test.mp4'; // test.mp4为应用文件目录下的预置资源，需要开发者根据实际情况进行替换。
14. let fileDescriptor = await this.context?.resourceManager.getRawFd(this.fileName);
15. let avFileDescriptor: media.AVFileDescriptor =
16. { fd: fileDescriptor.fd, offset: fileDescriptor.offset, length: fileDescriptor.length };
17. // 为fdSrc赋值触发initialized状态机上报。
18. this.avPlayer.fdSrc = avFileDescriptor;
```

## 运行完整示例

1. 新建工程，下载[示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVPlayer/AVPlayerArkTSURL)（也可直接运行），并将示例工程的以下资源复制到对应目录。

   ```
   1. AVPlayerArkTSURL
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
   15. ├── test.m3u8    (m3u8资源)
   16. └── test_01.mp3 （音频资源）
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
4. 在安装应用后，可将示例工程的/entry/src/main/resources/rawfile/test.m3u8通过以下命令加入应用沙箱，从而运行应用沙箱相关示例:（<FILESDIR>为物理路径，以示例工程为例，可通过console.info打印"this.context.filesDir"得到应用沙箱路径，再根据[应用沙箱指南](app-sandbox-directory.md)的应用沙箱路径和真实物理路径的对应关系表找到物理路径）。

   ```
   1. hdc file send "[目录]\test.m3u8" <FILESDIR>
   2. hdc file send "[目录]\test_01.mp3" <FILESDIR>
   ```
