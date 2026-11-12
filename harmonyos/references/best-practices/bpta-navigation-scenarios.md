---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-navigation-scenarios
title: 导航定位场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 导航定位场景低功耗规则
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:08f7b71380b49b0d0719ddb4911ec12168bf453d35ce6acbb28d74035f46d872
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/O7eWBGhJT5uKRr8KUzhvVg/zh-cn_image_0000002229450993.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0F4C5806148E0B7945B315AC4E6C6CAC3F4A1E8678E81460B49D86002E3B7FD "点击放大")

## 结果对比

* 优化前：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/WBWR8_8IRqmH3c1AelJZ7w/zh-cn_image_0000002193851136.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE6AB6C6569E66B2664FB42C6A5CC07353B37029880293FEFBE1C385B7D99E8F "点击放大")

* 优化后，图中字段证明系统低功耗方案使能成功（根据实验室测试功耗，功耗负载降低约43.89%。）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/B3XwlpYETf6pHP8UJi1-Lw/zh-cn_image_0000002194010716.png?HW-CC-KV=V1&HW-CC-Date=20261112T233139Z&HW-CC-Expire=31536000000&HW-CC-Sign=E8B71547A984CCCD7D6E25A02F642640EA971D2A049961F9545FC013FF775901 "点击放大")
