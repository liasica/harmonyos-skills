---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wearengine_service_status
title: 管理应用与Wear Engine服务的连接状态
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 管理应用与Wear Engine服务的连接状态
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a75ad9a21349d0dd2a04f22dba324bb1aef7952e9a335bb4cab66ada2ec4c1be
---

## 监测应用与Wear Engine服务的连接状态

华为运动健康App在后台停止服务（如功耗过高），从而导致应用与Wear Engine服务的连接状态发生变化。对于类似这种不确定的断开情况，开发者可以通过本功能特性了解当前应用和Wear Engine的连接状态。前提是在服务断开前，开发者已经使用该功能订阅过对Wear Engine服务连接状态的监测。

1. 在使用Wear Engine服务前，请导入WearEngine与相关模块。

   ```
   1. import { wearEngine } from '@kit.WearEngine';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 构造当服务连接断开时执行的回调函数。

   ```
   1. let callback = () => {
   2. console.info(`The service destruction event`);
   3. }
   ```
3. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[on](../harmonyos-references/wearengine_api.md#wearengineon)方法，订阅监听应用与Wear Engine服务的断联事件。

   ```
   1. try {
   2. wearEngine.on('serviceDie', callback);
   3. console.info(`Succeeded in subscribing the service destruction event.`);
   4. } catch (error) {
   5. const err: BusinessError = error as BusinessError;
   6. console.error(`Failed to subscribe the service destruction event. Code is ${err.code}, message is ${err.message}`);
   7. }
   ```
4. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[off](../harmonyos-references/wearengine_api.md#wearengineoff)方法，取消监听应用与Wear Engine服务的断联事件。需要传入订阅监听时的同一个回调函数对象。

   ```
   1. try {
   2. wearEngine.off('serviceDie', callback);
   3. console.info(`Succeeded in unsubscribing the service destruction event.`);
   4. } catch (error) {
   5. const err: BusinessError = error as BusinessError;
   6. console.error(`Failed to unsubscribe the service destruction event. Code is ${err.code}, message is ${err.message}`);
   7. }
   ```

## 断开应用与Wear Engine服务的连接

断开后，将释放Wear Engine资源，监测设备状态、收消息、收文件等功能不可用，监听服务端断联事件的回调函数不会执行，同时会清理掉之前注册的回调函数。如需重新连接，主动调用任意接口即可。

1. 在使用Wear Engine服务前，请导入WearEngine与相关模块。

   ```
   1. import { wearEngine } from '@kit.WearEngine';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[destroy](../harmonyos-references/wearengine_api.md#wearenginedestroy)方法，断开应用与Wear Engine服务的连接。

   ```
   1. wearEngine.destroy().then(() => {
   2. console.info(`Succeeded in destroying wear engine channel`);
   3. }).catch((error: BusinessError) => {
   4. console.error(`Failed to destroy wear engine channel. Code is ${error.code}, message is ${error.message}`);
   5. })
   ```
