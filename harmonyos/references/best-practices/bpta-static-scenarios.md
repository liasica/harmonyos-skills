---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-static-scenarios
title: 静态场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 静态场景低功耗规则
category: best-practices
scraped_at: 2026-04-29T14:13:50+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:214b6de5a266aa4734bf0bc19c4a82184b701a5072b9b362e78d1243fa3a67e6
---

## 规则

在界面完全静止且无音频输出、资源下载的场景下，三方应用应停止频繁请求显示和sensor等无关资源，不随vsync信号每帧周期性运行，不持续请求sensor等资源。三方应用进程的CPU负载率应低于10%（单核负载）。

## 开发步骤

静置场景下，三方应用进程不会随着vsync信号每帧周期性运行。以下“案例分析”对此进行详细说明。

在静置场景下，未使用的资源应及时释放。以sensor为例：

1. 按需使用sensor资源，并按需注册SensorId。

   注册监听，通过on()接口实现对传感器的持续监听。设置传感器上报周期interval为200000000纳秒（最小采样周期为5000000纳秒，最大采样周期为200000000纳秒）。

   ```
   1. import { sensor } from '@kit.SensorServiceKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';

   4. sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
   5. hilog.info(0x0000, 'Sample', 'Succeeded in obtaining data. x: ' + data.x + ' y: ' + data.y + ' z: ' + data.z);
   6. }, { interval: 200000000 });
   ```

   [StaticScenesRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/StaticScenesRule.ets#L21-L26)

2. 在sensor频次需求较低的场景中，根据需要调整sensor.on()的interval属性，以改变上报频次。

   ```
   1. sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
   2. hilog.info(0x0000, 'Sample', 'Succeeded in obtaining data. x: ' + data.x + ' y: ' + data.y + ' z: ' + data.z);
   3. }, { interval: 200000000 });
   ```

   [StaticScenesRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/StaticScenesRule.ets#L30-L32)
3. 不使用sensor资源时，使用以下接口进行解注册。

   ```
   1. sensor.off(sensor.SensorId.ACCELEROMETER);
   ```

   [StaticScenesRule.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/RationalUseOfFrontEndResources/entry/src/main/ets/pages/StaticScenesRule.ets#L36-L36)

## 案例分析

* 开机后，桌面静置。连接Wi-Fi后，lottie动效异常，导致UI和RS空跑。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/pzE8_x8hTIiQdU-ui8MnPw/zh-cn_image_0000002194011528.png "点击放大")
* 应用静置界面时，应用以120 fps响应vsync事件但无实际显示，导致应用进程和RS负载较高。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/6U46HZ7lQqesKjMpWs557A/zh-cn_image_0000002229451821.png "点击放大")

## 调测验证

* 查看日志：在控制台输入top指令，可直接获取进程负载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/YC7NpjAnR9COwSBoxGKdxQ/zh-cn_image_0000002193851952.png "点击放大")
* 抓取trace：通过trace中的进程耗时和绝对耗时，计算进程负载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/0puV2RfvQhqGUS3OiuN9MA/zh-cn_image_0000002229337329.png "点击放大")
