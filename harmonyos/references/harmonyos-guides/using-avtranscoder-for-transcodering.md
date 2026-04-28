---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avtranscoder-for-transcodering
title: 使用AVTranscoder实现视频转码(ArkTS)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(ArkTS) > 视频转码 > 使用AVTranscoder实现视频转码(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4df7b222e5b738a29eb492d4e06808d3ce4a01ab9d4d7b3d5ba0d9d62469fbb3
---

使用[AVTranscoder](media-kit-intro.md#avtranscoder)可以实现视频转码功能，从API 20开始支持视频转码的C/C++开发，转码功能可在手机、平板、2in1设备上作为系统提供的基础能力使用。可以通过调用[canIUse](../harmonyos-references/js-apis-syscap.md#caniuse)接口来判断当前设备是否支持AVTranscoder，当canIUse("SystemCapability.Multimedia.Media.AVTranscoder")的返回值为true时，表示可以使用转码能力。

本开发指导将以“开始转码-暂停转码-恢复转码-转码完成”的一次流程为示例，向开发者讲解AVTranscoder视频转码相关功能。

## 开发步骤及注意事项

详细的API说明请参考[AVTranscoder](../harmonyos-references/arkts-apis-media-avtranscoder.md)。

说明

如需对转码后的文件进行转发、上传、转存等处理，应用须收到complete事件后调用系统接口await avTranscoder.release()，以保证视频文件完整性。

1. 创建[AVTranscoder](../harmonyos-references/arkts-apis-media-f.md#mediacreateavtranscoder12)实例。

   ```
   1. import { media } from '@kit.MediaKit';

   3. private avTranscoder: media.AVTranscoder | undefined = undefined;
   4. // 创建转码实例。
   5. this.avTranscoder = await media.createAVTranscoder();
   ```
2. 设置业务需要的监听事件，监听状态变化及错误上报。

   | 事件类型 | 说明 |
   | --- | --- |
   | complete | 必要事件，监听AVTranscoder的转码完成。 |
   | error | 必要事件，监听AVTranscoder的错误信息。 |
   | progressUpdate | 监听AVTranscoder的进度。 |

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { fileIo } from '@kit.CoreFileKit';
   3. import { media } from '@kit.MediaKit';
   4. private currentProgress: number = 0;
   5. private avTranscoder: media.AVTranscoder | undefined = undefined;

   7. async test() {
   8. // 创建转码实例。
   9. this.avTranscoder = await media.createAVTranscoder();
   10. if (this.avTranscoder != undefined) {
   11. // 转码完成回调函数。
   12. this.avTranscoder.on('complete', async () => {
   13. console.info(`AVTranscoder is completed`);
   14. await this.releaseTranscoderingProcess();
   15. });
   16. // 错误上报回调函数。
   17. this.avTranscoder.on('error', (err: BusinessError) => {
   18. console.error(`AVTranscoder failed, code is ${err.code}, message is ${err.message}`);
   19. });
   20. // 进度上报回调函数。
   21. this.avTranscoder.on('progressUpdate', (progress: number) => {
   22. console.info(`AVTranscoder progressUpdate = ${progress}`);
   23. this.currentProgress = progress;
   24. })
   25. }
   26. }

   28. // 获取当前进度。
   29. getCurrentProgress(): number {
   30. console.info(`getCurrentProgress = ${this.currentProgress}`);
   31. return this.currentProgress;
   32. }
   33. // 释放转码流程。
   34. async releaseTranscoderingProcess() {
   35. if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
   36. if (this.avTranscoder != undefined) {
   37. // 1.释放转码实例。
   38. await this.avTranscoder.release();
   39. this.avTranscoder = undefined;
   40. // 2.关闭转码目标文件fd。
   41. fileIo.closeSync(this.avTranscoder!.fdDst);
   42. }
   43. }
   44. }
   ```
3. 设置源视频文件fd：设置属性fdSrc。

   说明

   下面代码示例中的fdSrc仅作示意使用，开发者需根据实际情况，确认资源有效性并设置：

   * 如果使用本地资源转码，必须确认资源文件可用，并使用应用沙箱路径访问对应资源，参考[获取应用文件路径](application-context-stage.md#获取应用文件路径)。应用沙箱的介绍及如何向应用沙箱推送文件，请参考[文件管理](app-sandbox-directory.md)。
   * 应通过Context属性获取应用文件路径，建议使用getUIContext获取UIContext实例，并使用getHostContext调用绑定实例的getContext，请参考[getHostContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md#gethostcontext12)。
   * 如果使用ResourceManager.getRawFd()打开HAP资源文件描述符，使用方法可参考[ResourceManager API参考](../harmonyos-references/js-apis-resource-manager.md#getrawfd9)。

   ```
   1. // 导入来自于ets/transcoder/AVTranscoderManager.ets文件。
   2. import {AVTranscoderDemo} from '../transcoder/AVTranscoderManager'

   4. @Entry
   5. @Component
   6. struct Index {
   7. // 获取当前组件所在Ability的Context，以通过Context获取应用文件路径。
   8. private context:Context | undefined = this.getUIContext()?.getHostContext();
   9. // 获取转码功能管理类。
   10. @State avTranscoder: AVTranscoderDemo | undefined = this.context ? new AVTranscoderDemo(this.context) : undefined;

   12. build() {
   13. RelativeContainer() {
   14. Column() {
   15. Button($r('app.string.StartTranscoder')) // 来自于resources/base/element/string.json文件中的name:StartTranscoder的值。
   16. .onClick(async () => {
   17. console.info(`Button put`);
   18. await this.avTranscoder?.avTranscoderDemo();
   19. })
   20. .id('AVTranscoderButton')
   21. // 获取转码进度。
   22. Progress({ value: 0, total: 100, type: ProgressType.Linear }).value(this.avTranscoder?.getCurrentProgress())
   23. .height(50)
   24. .width('80%')
   25. }
   26. .alignRules({
   27. center: { anchor: '__container__', align: VerticalAlign.Center },
   28. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   29. })
   30. }
   31. .height('100%')
   32. .width('100%')
   33. }
   34. }
   ```

   ```
   1. import { media } from '@kit.MediaKit';
   2. private avTranscoder: media.AVTranscoder | undefined = undefined;
   3. private context: Context | undefined;
   4. constructor(context: Context | undefined) {
   5. if (context != undefined) {
   6. this.context = context; // this.getUIContext().getHostContext();。
   7. }
   8. }

   10. async test() {
   11. // 创建转码实例。
   12. this.avTranscoder = await media.createAVTranscoder();
   13. // 获取输入文件fd，H264_AAC.mp4为rawfile目录下的预置资源，需要开发者根据实际情况进行替换。
   14. if (this.context != undefined) {
   15. let fileDescriptor = await this.context.resourceManager.getRawFd('H264_AAC.mp4');
   16. // 设置转码的源文件属性fdSrc。
   17. this.avTranscoder.fdSrc = fileDescriptor;
   18. }
   19. }
   ```
4. 设置目标视频文件fd：设置属性fdDst。

   说明

   转码输出文件fd（即示例里fdDst），形式为number。需要调用基础文件操作接口（[Core File Kit的ohos.file.fs](../harmonyos-references/js-apis-file-fs.md)）实现应用文件访问能力，获取方式参考[应用文件访问与管理](app-file-access.md)。

   ```
   1. import { fileIo } from '@kit.CoreFileKit';
   2. import { media } from '@kit.MediaKit';
   3. private avTranscoder: media.AVTranscoder | undefined = undefined;
   4. private context: Context | undefined;
   5. constructor(context: Context | undefined) {
   6. if (context != undefined) {
   7. this.context = context; // this.getUIContext().getHostContext();。
   8. }
   9. }

   11. async test() {
   12. // 创建转码实例。
   13. this.avTranscoder = await media.createAVTranscoder();
   14. if (this.context != undefined) {
   15. // 设置输出目标文件的沙箱路径。
   16. let outputFilePath = this.context.filesDir + "/output.mp4";
   17. // 文件不存在时创建并打开文件，文件存在时打开文件。
   18. let file = fileIo.openSync(outputFilePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   19. // 设置转码的目标文件属性fdDst。
   20. this.avTranscoder.fdDst = file.fd; // 参考应用文件访问与管理中的开发示例获取创建的视频文件fd填入此处。
   21. }
   22. }
   ```
5. 配置视频转码参数，调用prepare()接口。

   说明

   写入配置参数时需要注意，prepare()接口的入参avConfig中仅设置转码相关的配置参数。

   受限于解析/封装/编解码能力，只能使用[支持的转码格式](media-kit-intro.md#avtranscoder)。

   ```
   1. import { media } from '@kit.MediaKit';
   2. private avTranscoder: media.AVTranscoder | undefined = undefined;
   3. private avConfig: media.AVTranscoderConfig = {
   4. audioBitrate: 100000, // 音频比特率。
   5. audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式。
   6. fileFormat: media.ContainerFormatType.CFT_MPEG_4, // 封装格式。
   7. videoBitrate: 2000000, // 视频比特率。
   8. videoCodec: media.CodecMimeType.VIDEO_AVC, // 视频编码格式。
   9. };

   11. async test() {
   12. // 创建转码实例。
   13. this.avTranscoder = await media.createAVTranscoder();
   14. // 配置转码参数完成准备工作。
   15. await this.avTranscoder.prepare(this.avConfig);
   16. }
   ```

   可在avConfig中设置目标视频的分辨率。

   ```
   1. let avConfig: media.AVTranscoderConfig = {
   2. audioBitrate: 100000, // 音频比特率。
   3. audioCodec: media.CodecMimeType.AUDIO_AAC, // 音频编码格式。
   4. fileFormat: media.ContainerFormatType.CFT_MPEG_4, // 封装格式。
   5. videoBitrate: 2000000, // 视频比特率。
   6. videoCodec: media.CodecMimeType.VIDEO_AVC, // 视频编码格式。
   7. videoFrameWidth: 640, // 目标视频分辨率的宽为640。
   8. videoFrameHeight: 480, // 目标视频分辨率的高为480。
   9. };
   ```
6. 开始转码，调用start()接口。

   ```
   1. async startTranscoderingProcess() {
   2. if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
   3. if (this.avTranscoder != undefined) {
   4. await this.avTranscoder.release();
   5. this.avTranscoder = undefined;
   6. }
   7. // 开始转码前需要创建转码实例、设置回调、设置fd并完成prepare。
   8. // 具体创建步骤参考开发步骤1-5。

   10. // 开始转码。
   11. await this.avTranscoder.start();
   12. }
   13. }
   ```
7. 暂停转码，调用pause()接口。

   ```
   1. // 暂停转码对应的流程。
   2. async pauseTranscoderingProcess() {
   3. if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
   4. if (this.avTranscoder != undefined) { // 仅在调用start返回后调用pause为合理调用。
   5. await this.avTranscoder.pause();
   6. }
   7. }
   8. }
   ```
8. 恢复转码，调用resume()接口。

   ```
   1. // 恢复转码。
   2. async resumeTranscoderingProcess() {
   3. if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
   4. if (this.avTranscoder != undefined) { // 仅在调用pause返回后调用resume为合理调用。
   5. await this.avTranscoder.resume();
   6. }
   7. }
   8. }
   ```
9. 销毁实例，调用release()接口，退出转码。

   ```
   1. // 销毁实例。
   2. async releaseTranscoderingProcess() {
   3. if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
   4. if (this.avTranscoder != undefined) {
   5. // 1.销毁实例。
   6. await this.avTranscoder.release();
   7. this.avTranscoder = undefined;
   8. // 2.关闭转码目标文件fd。
   9. fileIo.closeSync(this.avTranscoder!.fdDst);
   10. }
   11. }
   12. }
   ```
10. 完整的【开始转码-暂停转码-恢复转码-转码完成】流程

    ```
    1. async avTranscoderDemo() {
    2. await this.startTranscoderingProcess(); // 开始转码。
    3. await this.pauseTranscoderingProcess(); // 暂停转码。
    4. await this.resumeTranscoderingProcess(); // 恢复转码。
    5. }
    ```

## 运行示例工程

参考以下示例，完成“开始转码-暂停转码-恢复转码-转码完成”的完整流程。

1. 新建工程，下载[完整示例工程](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVTranscoder/AVTranscoderArkTS)，并将示例工程的资源复制到对应目录。

   ```
   1. AVTranscoderArkTS
   2. entry/src/main/ets/
   3. └── pages
   4. │    └── Index.ets (转码界面)
   5. │
   6. └── transcoder
   7. └── AVTranscoderManager.ets (转码功能)

   9. entry/src/main/resources/
   10. ├── base
   11. │   ├── element
   12. │   │   ├── color.json
   13. │   │   ├── float.json
   14. │   │   └── string.json
   15. │   └── media
   16. │
   17. └── rawfile
   18. └── H264_AAC.mp4 (视频资源)
   ```
2. 编译新建工程并运行。
