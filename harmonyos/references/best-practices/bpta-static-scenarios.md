---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-static-scenarios
title: 静态场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 静态场景低功耗规则
category: best-practices
scraped_at: 2026-04-28T08:22:42+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:64e3e340e2fe5a829d191ab9e8eb8bd7afa3b393abdf9c8766cfa691428a3d60
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/pzE8_x8hTIiQdU-ui8MnPw/zh-cn_image_0000002194011528.png?HW-CC-KV=V1&HW-CC-Date=20260428T002241Z&HW-CC-Expire=86400&HW-CC-Sign=F333E248C8B2597EA70F001F31908D24121798A5AC3766677057C553CD178B13 "点击放大")
* 应用静置界面时，应用以120 fps响应vsync事件但无实际显示，导致应用进程和RS负载较高。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/6U46HZ7lQqesKjMpWs557A/zh-cn_image_0000002229451821.png?HW-CC-KV=V1&HW-CC-Date=20260428T002241Z&HW-CC-Expire=86400&HW-CC-Sign=4BC3CE583BF7AFB7FD3611459F338FC95067EB71BCA7473936FACC6BD58D3043 "点击放大")

## 调测验证

* 查看日志：在控制台输入top指令，可直接获取进程负载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/YC7NpjAnR9COwSBoxGKdxQ/zh-cn_image_0000002193851952.png?HW-CC-KV=V1&HW-CC-Date=20260428T002241Z&HW-CC-Expire=86400&HW-CC-Sign=D541047EF985FA60F2718DB5FA8DBEAC683785A75367335346315215650B3314 "点击放大")
* 抓取trace：通过trace中的进程耗时和绝对耗时，计算进程负载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/0puV2RfvQhqGUS3OiuN9MA/zh-cn_image_0000002229337329.png?HW-CC-KV=V1&HW-CC-Date=20260428T002241Z&HW-CC-Expire=86400&HW-CC-Sign=13FC696A141F35CE31F8494F921265D25372E3C4317E5199D579511E3C908A6E "点击放大")
