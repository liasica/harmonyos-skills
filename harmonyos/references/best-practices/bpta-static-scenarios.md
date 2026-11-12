---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-static-scenarios
title: 静态场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 静态场景低功耗规则
category: best-practices
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:ee289a985484cd6d130508c48ae1b912b9163b7618846118e2d3912dbac48312
---

## 规则

在界面完全静止且无音频输出、资源下载的场景下，三方应用应停止频繁请求显示和sensor等无关资源，不随vsync信号每帧周期性运行，不持续请求sensor等资源。三方应用进程的CPU负载率应低于10%（单核负载）。

## 开发步骤

静置场景下，三方应用进程不会随着vsync信号每帧周期性运行。以下“案例分析”对此进行详细说明。

在静置场景下，未使用的资源应及时释放。以sensor为例：

1. 按需使用sensor资源，并按需注册SensorId。

   注册监听，通过on()接口实现对传感器的持续监听。设置传感器上报周期interval为200000000纳秒（最小采样周期为5000000纳秒，最大采样周期为200000000纳秒）。

   ```typescript
   import { sensor } from '@kit.SensorServiceKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
     hilog.info(0x0000, 'Sample', 'Succeeded in obtaining data. x: ' + data.x + ' y: ' + data.y + ' z: ' + data.z);
   }, { interval: 200000000 });
   ```

2. 在sensor频次需求较低的场景中，根据需要调整sensor.on()的interval属性，以改变上报频次。

   ```typescript
   sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
     hilog.info(0x0000, 'Sample', 'Succeeded in obtaining data. x: ' + data.x + ' y: ' + data.y + ' z: ' + data.z);
   }, { interval: 200000000 });
   ```
3. 不使用sensor资源时，使用以下接口进行解注册。

   ```typescript
   sensor.off(sensor.SensorId.ACCELEROMETER);
   ```

## 案例分析

* 开机后，桌面静置。连接Wi-Fi后，lottie动效异常，导致UI和RS空跑。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/24CWwDW3R56tUb8PHM5S1g/zh-cn_image_0000002194011528.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=0D6E2BFC18BD4EFB573995B57E3A81F86F5B2276F323D442481EC70E32FC55C6 "点击放大")
* 应用静置界面时，应用以120 fps响应vsync事件但无实际显示，导致应用进程和RS负载较高。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/RiPfTtBCQFWuSNu9yPCKfA/zh-cn_image_0000002229451821.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8C7BC09AC5BA58109FE91C3A211713D42EB7F9286A6EE2AAF5B0D4F688BF5F1 "点击放大")

## 调测验证

* 查看日志：在控制台输入top指令，可直接获取进程负载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/-bTU8-DmTnyK4RLL91XflA/zh-cn_image_0000002193851952.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=274DDA68DF215197E69281600CF8ACDE17CE30A006120F6F2A5A77DA10293160 "点击放大")
* 抓取trace：通过trace中的进程耗时和绝对耗时，计算进程负载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/NQln0xArS1SJ54dnuNq6uA/zh-cn_image_0000002229337329.png?HW-CC-KV=V1&HW-CC-Date=20261112T233141Z&HW-CC-Expire=31536000000&HW-CC-Sign=3752A82793B97E93A33CF82040BCDA6D704DCAC1A6FC95D26F15EB9CEB132D7F "点击放大")
