---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-static-scenarios
title: 静态场景低功耗规则
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 前台资源合理使用 > 静态场景低功耗规则
category: best-practices
scraped_at: 2026-11-24T12:47:53+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:75ff684c95d6b5ee618588b878464ab32d618ad1481e3ec6d94ee942cf88c836
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

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/TnziuWKVTdy5CufRVe-YPA/zh-cn_image_0000002194011528.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA4EE022A31F487C8B0B93E7E14FF038BEC992A02E2100C5C8F0977EBFC269CD "点击放大")
* 应用静置界面时，应用以120 fps响应vsync事件但无实际显示，导致应用进程和RS负载较高。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/VPlTs1LsTP6tnJ297RbA8g/zh-cn_image_0000002229451821.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=CB2F4A1B1EAF1B50B2DC832B0B387BEC4DE98DBA7AFA68E25548F694335170AB "点击放大")

## 调测验证

* 查看日志：在控制台输入top指令，可直接获取进程负载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/XNbzVbP_SxqZWBsigf63MQ/zh-cn_image_0000002193851952.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=4351AA37669980479F905302DCFCB319633656D5261BED7E75DCA9B20E9E49F1 "点击放大")
* 抓取trace：通过trace中的进程耗时和绝对耗时，计算进程负载。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/1PL4kOYNSvS08Q4pl1ckiA/zh-cn_image_0000002229337329.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=415E69C5ED05AA8A349661DCA9409CDEE2B310EDEC2E0D95B596D2EEFA82666F "点击放大")
