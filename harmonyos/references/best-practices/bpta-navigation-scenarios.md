---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-navigation-scenarios
title: 导航定位场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 导航定位场景低功耗规则
category: best-practices
scraped_at: 2026-11-24T12:47:53+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:62cc924e74a4e409aff63ff8186604c54423d26d67aa9d6ecd684371f1ae20cc
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/KiIjkGBeQ-msLi3EpxGw3w/zh-cn_image_0000002229450993.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=26FB875E3AEA07DD9AC91AFCBB48F1A8B93784AE3B166F968164706EBA88E68F "点击放大")

## 结果对比

* 优化前：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/ZH52sG_BTGGNyRs8-R43Gw/zh-cn_image_0000002193851136.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=5D0EF093B10B6DFDAC149BEB9CC263CA59743D214B96174DD44513B5D6136E1F "点击放大")

* 优化后，图中字段证明系统低功耗方案使能成功（根据实验室测试功耗，功耗负载降低约43.89%。）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/WBNEz0OHT9GG6N4rTsfVLQ/zh-cn_image_0000002194010716.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=E9CD0C811179DDC762A69A545CD37E96E86D98B619E5C07D1106582910C24465 "点击放大")
