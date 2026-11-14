---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-navigation-scenarios
title: 导航定位场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 导航定位场景低功耗规则
category: best-practices
scraped_at: 2026-11-14T08:54:16+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:054cf00d7d5738a4012167bb472aa2cbe4aa30f557bb9dcd19bce78b11e0d271
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/QYz701amSSGLzO3J1P_i9g/zh-cn_image_0000002229450993.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=A0CFE4314F82EC3DDB37FD69238B7DDBE244E63C19B93DC776132B12E4313530 "点击放大")

## 结果对比

* 优化前：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/i3B05ZFZSie357v-2DqJ9A/zh-cn_image_0000002193851136.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=B4EEBB01EE62B4E220768C7FAB0A47927709C8F571C350DF7D7B15B41AD08341 "点击放大")

* 优化后，图中字段证明系统低功耗方案使能成功（根据实验室测试功耗，功耗负载降低约43.89%。）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/2FufNFodRXqovFBsshjlVQ/zh-cn_image_0000002194010716.png?HW-CC-KV=V1&HW-CC-Date=20261114T005415Z&HW-CC-Expire=31536000000&HW-CC-Sign=046203D66052603FB07732C6F3E6CB525E3AE89B9ABEFC144153702BAAEB3654 "点击放大")
