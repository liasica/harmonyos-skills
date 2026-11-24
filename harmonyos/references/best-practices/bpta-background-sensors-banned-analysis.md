---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-background-sensors-banned-analysis
title: 应用退后台禁止使用传感器问题分析
breadcrumb: 最佳实践 > 功耗 > 应用功耗分析 > 应用退后台禁止使用传感器问题分析
category: best-practices
scraped_at: 2026-11-24T12:47:53+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:6b4424604a7ff1b9002e222bae08ea08bec2db438493ff92275b8c6bb86f931f
---

## 应用退后台禁止使用传感器介绍

手机中的传感器（如加速度计、陀螺仪、磁力计、环境光传感器等）是重要的硬件资源，用于提供各种功能，如运动检测、方向感知、屏幕亮度调整等。这些传感器在运行时会消耗电池电量，并占用处理器资源。因此，合理管理和优化传感器资源的使用对于提升手机性能和延长电池寿命至关重要。

当应用在前台运行时，用户可以直接与之交互，此时应用需要实时获取传感器数据以提供准确的服务。然而，当应用切换到后台时，用户不再直接与之交互，此时继续持有传感器资源可能会导致不必要的资源浪费。因此，在后台非保活场景下，应避免应用持有不必要的传感器资源。

## 问题定位流程

### 应用开发调试阶段自检

1. 环境准备：本地配置好日志抓取和日志解析工具
   * hilogtool：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog-tool
   * hilog：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog
2. 判断应用内所有界面退后台后，是否存在传感器没有关闭的行为
   * 方法一：通过DevEco软件日志栏中实时过滤(搜索栏支持正则匹配搜索)：(bundleName).\*open the sensor|(bundleName).\*close the sensor

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/H9lD3koJSyWF_OifzzdaNQ/zh-cn_image_0000002555614824.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=250BBD4575338B77409F5E4FE5FA9ECA3546862B4950D462A1445BCC327C8052 "点击放大")

   * 方法二：本地使用命令行控制台实时过滤日志：hdc shell hilog | grep -i "(bundleName).\*open the sensor\|(bundleName).\*close the sensor"

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/525CI7MNSDGF4M9Qig8OpA/zh-cn_image_0000002586174413.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=AA73296CE59B8C673069A0A61DE9542E8DF6638521A4E574676843D2A7AEF8E0 "点击放大")
3. 判断应用在后台是否存在长时任务
   * 过滤关键词：suspend\_manager.\*(bundleName)
     + 应用后台不存在长时任务

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/Euo4j7hkStGlD2DqJSpPLQ/zh-cn_image_0000002586294373.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=26315997F362EE1E5FB5150B391FDB689FCCF3B9DB6ED433DDC741B71CEF7098 "点击放大")

     + 应用后台存在长时任务

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/7_i_gsJMRJeMslFUa9Msxg/zh-cn_image_0000002555774456.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=656B00FD8C18EBF13DF4013989C7D65447AAECC11A08E49F5134E1E32CB855A1 "点击放大")
4. 如果存在应用退后台后还存在没有关闭的传感器，并且没有长时任务保活，需要进行优化，合理使用资源
   * 优化建议：在应用退后台后主动调用sensor.off关闭传感器

   ```typescript
   import { UIAbility } from '@kit.AbilityKit';
   import { sensor } from '@kit.SensorServiceKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   export default class EntryAbility extends UIAbility {
       // ...
       onForeground(): void {
         try {
           //In the foreground, listen to the required type of sensor based on the service requirements
           sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
             console.info("Succeeded in obtaining data.x:" + data.x + "y:" + data.y + "z:" + data.z);
           }, {
             interval: 100000000
           });
       } catch (error) {
           let err = error as BusinessError;
           hilog.warn(0x000, 'testTag', `sensor on failed, code=${err.code}, message=${err.message}`);
       }
   }
     onBackground(): void {
       try {
         //The backstage cancels the listening
         sensor.off(sensor.SensorId.ACCELEROMETER);
       } catch (error) {
         let err = error as BusinessError;
         hilog.warn(0x000, 'testTag', `sensor off failed, code=${err.code}, message=${err.message}`);
       }
     }
   }
   ```

### 应用上架问题分析

1. 先通过hilog日志判断退后台的时间点。
   * 过滤日志关键词：suspend\_msg.\*(bundleName).\*state
     + state 2 表示应用处于前台
     + state 4 表示应用处于后台
2. 通过所有日志查看哪些传感器在退后台后没有关闭。
   * 过滤日志关键词：(bundleName).\*open the sensor|(bundleName).\*close the sensor

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/Yx2Ah2bwTj29TYQyVg7WCA/zh-cn_image_0000002555614826.png?HW-CC-KV=V1&HW-CC-Date=20261124T044753Z&HW-CC-Expire=31536000000&HW-CC-Sign=86D53A98902A76D311CC75C79C1B7755ED612731F2B2B6D85A1BFCCC74FB141A "点击放大")
3. 如果存在应用退后台后还存在没有关闭的传感器，并且没有长时任务保活，需要进行优化，合理使用资源。
   * 优化建议：在应用退后台后主动调用sensor.off关闭传感器

     ```typescript
     import { UIAbility } from '@kit.AbilityKit';
     import { sensor } from '@kit.SensorServiceKit';
     import { BusinessError } from '@kit.BasicServicesKit';
     export default class EntryAbility extends UIAbility {
         // ...
         onForeground(): void {
           try {
             //In the foreground, listen to the required type of sensor based on the service requirements
             sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
               console.info("Succeeded in obtaining data.x:" + data.x + "y:" + data.y + "z:" + data.z);
             }, {
               interval: 100000000
             });
         } catch (error) {
             let err = error as BusinessError;
             hilog.warn(0x000, 'testTag', `sensor on failed, code=${err.code}, message=${err.message}`);
         }
     }
       onBackground(): void {
         try {
           //The backstage cancels the listening
           sensor.off(sensor.SensorId.ACCELEROMETER);
         } catch (error) {
           let err = error as BusinessError;
           hilog.warn(0x000, 'testTag', `sensor off failed, code=${err.code}, message=${err.message}`);
         }
       }
     }
     ```
