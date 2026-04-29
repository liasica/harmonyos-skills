---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-navigation-scenarios
title: 导航定位场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 导航定位场景低功耗规则
category: best-practices
scraped_at: 2026-04-29T14:13:50+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:9b45b26721db58c1cb333a3a342c36d1f321339d07dc978858e4432006ffc3de
---

## 规则

* 导航类应用需设置正确的应用类型，并使用系统自带的导航场景音效算法，避免冗余处理。
* 在导航类应用无语音播报等语音输出时，禁止持续向系统写入音频空数据。

## 开发步骤

为了避免导航类应用无法使用系统低功耗方案，确保正确设置usage类型。配置音频渲染参数并创建AudioRenderer实例时，设置usage类型为audio.StreamUsage.STREAM\_USAGE\_NAVIGATION。

```
1. import { audio } from '@kit.AudioKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. let audioStreamInfo: audio.AudioStreamInfo = {
5. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
6. channels: audio.AudioChannel.CHANNEL_1,
7. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
8. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
9. };
10. let audioRendererInfo: audio.AudioRendererInfo = {
11. usage: audio.StreamUsage.STREAM_USAGE_NAVIGATION,
12. rendererFlags: 0
13. };
14. let audioRendererOptions: audio.AudioRendererOptions = {
15. streamInfo: audioStreamInfo,
16. rendererInfo: audioRendererInfo
17. };
18. audio.createAudioRenderer(audioRendererOptions, (err, data) => {
19. if (err) {
20. hilog.error(0x0000, 'Sample', `Invoke createAudioRenderer failed, code is ${err.code}, message is ${err.message}`);
21. return;
22. } else {
23. hilog.info(0x0000, 'Sample', 'Invoke createAudioRenderer succeeded.');
24. let audioRenderer = data;
25. }
26. });
```

[NavigationAndPositioningRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/NavigationAndPositioningRule.ets#L21-L46)

## 调测验证

* 通过以下命令查看日志确认：

  ```
  1. hdc shell
  2. hilog | grep usage
  ```
* 执行效果如下图：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/kvUH7LF-Qu-rRoeKGUtx1g/zh-cn_image_0000002229450993.png?HW-CC-KV=V1&HW-CC-Date=20260429T061349Z&HW-CC-Expire=86400&HW-CC-Sign=4D1BC3DAF6DA9C274DBD24ABF2F89AC312834960048B524102A57D6E3ACBFAD9 "点击放大")

## 结果对比

* 优化前：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/eUtu96aMTNWBjow2jq9xiA/zh-cn_image_0000002193851136.png?HW-CC-KV=V1&HW-CC-Date=20260429T061349Z&HW-CC-Expire=86400&HW-CC-Sign=AF33A71E4BE47B10A562933226F5300C3C03B379766E3749183F544D0D42FEA8 "点击放大")

* 优化后，图中字段证明系统低功耗方案使能成功（根据实验室测试功耗，功耗负载降低约43.89%。）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/aypZ4dwRQQ-V-Psn4XLbKg/zh-cn_image_0000002194010716.png?HW-CC-KV=V1&HW-CC-Date=20260429T061349Z&HW-CC-Expire=86400&HW-CC-Sign=3CB8CFA076E6F6EF6C07B54F65167E02996984455276F676D76CC53AE03CDDCC "点击放大")
