---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-navigation-scenarios
title: 导航定位场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 导航定位场景低功耗规则
category: best-practices
scraped_at: 2026-09-10T06:30:14+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:933aabf133c5f9c54acb1b3193ffffe072c63680998d67a5eaa31723b26d4344
---

## 规则

* 导航类应用需设置正确的应用类型，并使用系统自带的导航场景音效算法，避免冗余处理。
* 在导航类应用无语音播报等语音输出时，禁止持续向系统写入音频空数据。

## 开发步骤

为了避免导航类应用无法使用系统低功耗方案，确保正确设置usage类型。配置音频渲染参数并创建AudioRenderer实例时，设置usage类型为audio.StreamUsage.STREAM\_USAGE\_NAVIGATION。

```typescript
import { audio } from '@kit.AudioKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
  channels: audio.AudioChannel.CHANNEL_1,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_NAVIGATION,
  rendererFlags: 0
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};
audio.createAudioRenderer(audioRendererOptions, (err, data) => {
  if (err) {
    hilog.error(0x0000, 'Sample', `Invoke createAudioRenderer failed, code is ${err.code}, message is ${err.message}`);
    return;
  } else {
    hilog.info(0x0000, 'Sample', 'Invoke createAudioRenderer succeeded.');
    let audioRenderer = data;
  }
});
```

## 调测验证

* 通过以下命令查看日志确认：

  ```screen
  hdc shell
  hilog | grep usage
  ```
* 执行效果如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/z95crIOKRHSAvCCxtFxGFw/zh-cn_image_0000002229450993.png "点击放大")

## 结果对比

* 优化前：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/OEZ4OvXsTBmw1U-b3apXXA/zh-cn_image_0000002193851136.png "点击放大")

* 优化后，图中字段证明系统低功耗方案使能成功（根据实验室测试功耗，功耗负载降低约43.89%。）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/jbwyB7C-QuG7hHcWgS3jAQ/zh-cn_image_0000002194010716.png "点击放大")
