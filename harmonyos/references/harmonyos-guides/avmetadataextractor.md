---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avmetadataextractor
title: 使用AVMetadataExtractor提取音视频元数据信息(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 媒体信息查询 > 使用AVMetadataExtractor提取音视频元数据信息(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:edc82ca2857d87374a0fc258d7a5fe152060b8302a16e8f04528aa0721a29021
---

使用[AVMetadataExtractor](media-kit-intro.md#avmetadataextractor)可以实现从原始媒体资源中获取元数据。本指南将以获取一个媒体资源的元数据作为示例，向开发者讲解AVMetadataExtractor元数据相关功能。

获取音视频资源的元数据的全流程包含：创建AVMetadataExtractor、设置资源、获取元数据、获取音频资源的专辑封面或获取视频缩略图、释放资源。

## 开发步骤及注意事项

详细的API说明请参考[AVMetadataExtractor](../harmonyos-references/arkts-apis-media-avmetadataextractor.md)。

1. 使用[createAVMetadataExtractor()](../harmonyos-references/arkts-apis-media-f.md#mediacreateavmetadataextractor11-1)创建实例。

   ```
   1. import { media } from '@kit.MediaKit';
   2. // 创建AVMetadataExtractor对象。
   3. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
   ```
2. 设置资源：用户可以根据需要选择设置属性fdSrc（表示文件描述符）和属性dataSrc（表示dataSource描述符）或者调用setUrlSource设置在线媒体链接。

   开发者需根据实际情况，确认资源有效性并设置（只能设置其中一种）：

   * 如果设置fdSrc，可以使用ResourceManager.getRawFd打开HAP资源文件描述符，使用方法可参考[ResourceManager API参考](../harmonyos-references/js-apis-resource-manager.md#getrawfd9)。也可以通过应用沙箱路径访问对应资源（必须确保资源可用），参考[获取应用文件路径](application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[文件管理](app-sandbox-directory.md)。

     ```
     1. import { common } from '@kit.AbilityKit';
     2. import { media } from '@kit.MediaKit';

     4. // 创建AVMetadataExtractor对象。
     5. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
     6. // 获取rawfile目录下资源文件描述符，设置fdSrc属性。
     7. // 获取当前组件所在Ability的Context，并通过Context获取应用文件路径。
     8. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     9. // 设置fdSrc，test.mp3为rawfile目录下的预置资源，需要开发者根据实际情况进行替换。
     10. avMetadataExtractor.fdSrc = await context.resourceManager.getRawFd('test.mp3');
     ```
   * 如果设置dataSrc，必须正确设置dataSrc中的callback属性，确保callback被调用时能正确读取到对应资源，使用应用沙箱路径访问对应资源，参考[获取应用文件路径](application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[文件管理](app-sandbox-directory.md)。

     ```
     1. import { fileIo, ReadOptions } from '@kit.CoreFileKit';
     2. import { common } from '@kit.AbilityKit';
     3. import { media } from '@kit.MediaKit';
     4. const TAG = 'MetadataDemo';

     6. // 创建AVMetadataExtractor对象。
     7. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
     8. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     9. let rootPath: string = context.filesDir; // 应用文件目录。
     10. let testFilename: string = '/test.mp3'; // test.mp3为应用文件目录下的预置资源，需要开发者根据实际情况进行替换。
     11. // 使用fileIo文件系统打开沙箱地址获取媒体文件地址，设置dataSrc属性。
     12. // 通过UIAbilityContext获取沙箱地址filesDir（以Stage模型为例）。
     13. let fd: number = fileIo.openSync(rootPath + testFilename).fd;
     14. let fileSize: number = fileIo.statSync(rootPath + testFilename).size;
     15. // 设置dataSrc描述符，通过callback从文件中获取资源，写入buffer中。
     16. let dataSrc: media.AVDataSrcDescriptor = {
     17. fileSize: fileSize,
     18. callback: (buffer, len, pos) => {
     19. if (buffer == undefined || len == undefined || pos == undefined) {
     20. console.error(TAG, `dataSrc callback param invalid`);
     21. return -1;
     22. }
     23. let options: ReadOptions = {
     24. offset: pos,
     25. length: len
     26. };
     27. let num = fileIo.readSync(fd, buffer, options);
     28. console.info(TAG, 'readAt end, num: ' + num);
     29. if (num > 0 && fileSize >= pos) {
     30. return num;
     31. }
     32. return -1;
     33. }
     34. };
     35. // 设置dataSrc。
     36. avMetadataExtractor.dataSrc = dataSrc;
     ```
   * 如果设置[setUrlSource](../harmonyos-references/arkts-apis-media-avmetadataextractor.md#seturlsource20)，必须正确设置setUrlSource中的url和headers属性，确保正确访问url。

     ```
     1. import { media } from '@kit.MediaKit';

     3. // 创建AVMetadataExtractor对象。
     4. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
     5. // 调用setUrlSource设置网络点播媒体资源URL，用来获取在线音视频元数据和在线视频缩略图。
     6. let url: string = 'http://xx.mp4';
     7. let headers: Record<string, string> = {
     8. "User-Agent" : "User-Agent-Value"
     9. };
     10. avMetadataExtractor.setUrlSource(url, headers);
     ```
   * 不同AVMetadataExtractor或者[AVImageGenerator](../harmonyos-references/arkts-apis-media-avimagegenerator.md)实例，如果需要操作同一资源，需要多次打开文件描述符，不要共用同一文件描述符。

     ```
     1. import { common } from '@kit.AbilityKit';
     2. import { fileIo } from '@kit.CoreFileKit';
     3. import { media } from '@kit.MediaKit';

     5. // 创建AVMetadataExtractor对象。
     6. let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
     7. // 使用fileIo文件系统打开沙箱地址获取媒体文件地址，设置fdSrc属性。
     8. let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
     9. let rootPath: string = context.filesDir; // 应用文件目录。
     10. let testFilename: string = '/test.mp3'; // test.mp3为应用文件目录下的预置资源，需要开发者根据实际情况进行替换。
     11. avMetadataExtractor.fdSrc = fileIo.openSync(rootPath + testFilename); // 设置fdSrc属性。
     ```
3. 获取元数据：调用fetchMetadata()，可以获取到一个[AVMetadata](../harmonyos-references/arkts-apis-media-i.md#avmetadata11)对象，通过访问该对象的各个属性，可以获取到元数据。

   ```
   1. // 获取元数据（callback模式）。
   2. avMetadataExtractor.fetchMetadata((error, metadata) => {
   3. if (error) {
   4. console.error(TAG, `fetchMetadata callback failed, err = ${JSON.stringify(error)}`);
   5. return;
   6. }
   7. })

   9. // 获取元数据（promise模式）。
   10. let metadata = await avMetadataExtractor.fetchMetadata();
   ```
4. 对于视频资源：可以通过fetchMetadata获取的AVMetadata对象metadata拿到视频资源的宽、高等数据。

   ```
   1. // 获取视频资源的宽和高。
   2. let metadata = await avMetadataExtractor.fetchMetadata();
   3. let width = metadata.videoWidth;
   4. let height = metadata.videoHeight;
   ```
5. 对于音频资源而言，除了可以通过AVMetadata对象来获取音频资源的标题、时长等元数据外，还可以获取专辑封面（例如，调用fetchAlbumCover()，可以获取到专辑封面）。

   ```
   1. import { image } from '@kit.ImageKit';
   2. // pixelMap对象声明，用于图片显示。
   3. @State pixelMap: image.PixelMap | undefined = undefined;
   4. // 获取专辑封面（callback模式）。
   5. avMetadataExtractor.fetchAlbumCover((err, pixelMap) => {
   6. if (err) {
   7. console.error(TAG, `fetchAlbumCover callback failed, err = ${JSON.stringify(err)}`);
   8. return;
   9. }
   10. this.pixelMap = pixelMap;
   11. })

   13. // 获取专辑封面（promise模式）。
   14. this.pixelMap = await avMetadataExtractor.fetchAlbumCover();
   ```
6. （可选）获取视频缩略图：调用fetchFrameByTime，可以获取到视频缩略图。

   ```
   1. import { image } from '@kit.ImageKit';
   2. // pixelMap对象声明，用于图片显示。
   3. @State pixelMap: image.PixelMap | undefined = undefined;
   4. // 接口入参声明。
   5. let timeUs: number = 0;
   6. let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_PREVIOUS_SYNC;
   7. let param: media.PixelMapParams = {
   8. width : 300,
   9. height : 300
   10. }
   11. // 获取视频缩略图（promise模式）。
   12. this.pixelMap = await avMetadataExtractor.fetchFrameByTime(timeUs, queryOption, param);
   ```
7. （可选）批量获取视频缩略图：调用fetchFramesByTimes，能够批量获取视频缩略图。

   ```
   1. import { image } from '@kit.ImageKit';
   2. // pixelMap对象声明，用于图片显示。
   3. @State pixelMap: image.PixelMap | undefined = undefined;
   4. // 接口入参声明。
   5. let timesUs: number[] = [0];
   6. let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV_IMAGE_QUERY_PREVIOUS_SYNC;
   7. let param: media.PixelMapParams = {
   8. width : 300,
   9. height : 300
   10. }
   11. // 获取视频缩略图（callback模式）。
   12. avMetadataExtractor.fetchFramesByTimes(timesUs, queryOption, param, async (frameInfo: media.FrameInfo, err: BusinessError) => {
   13. if (err) {
   14. console.error(`fetch failed, error = ${JSON.stringify(err)}`);
   15. return;
   16. }
   17. console.info(`fetch success.`);
   18. if (frameInfo !== undefined && frameInfo.image !== undefined) {
   19. this.pixelMap = frameInfo.image;
   20. }
   21. })

   23. // 批量获取缩略图任务耗时可能较长，可以调用cancelAllFetchFrames停止在当前extractor上所有缩略图获取任务（仅对批量获取接口生效）。
   24. avMetadataExtractor.cancelAllFetchFrames();
   ```
8. 释放资源：调用release()销毁实例，释放资源。

   ```
   1. // 释放资源（callback模式）。
   2. avMetadataExtractor.release((error) => {
   3. if (error) {
   4. console.error(TAG, `release failed, err = ${JSON.stringify(error)}`);
   5. return;
   6. }
   7. console.info(TAG, `release success.`);
   8. })

   10. // 释放资源（promise模式）。
   11. avMetadataExtractor.release();
   ```

## 运行示例工程

参考以下示例，获取一个音频的元数据和专辑封面。

1. 新建工程，下载[完整示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVMetadataExtractor/AVMetadataExtractorArkTS)，并将示例工程的资源复制到对应目录。

   ```
   1. AVMetadataExtractorArkTS
   2. entry/src/main/ets/
   3. └── pages
   4. └── Index.ets (获取元数据界面)
   5. entry/src/main/resources/
   6. ├── base
   7. │   ├── element
   8. │   │   ├── color.json
   9. │   │   ├── float.json
   10. │   │   └── string.json
   11. │   └── media
   12. │
   13. └── rawfile
   14. └── test.mp3 (音频资源)
   ```
2. 编译新建工程并运行。
