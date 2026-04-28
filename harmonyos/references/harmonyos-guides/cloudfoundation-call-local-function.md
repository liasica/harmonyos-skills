---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-local-function
title: 调用本地云函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > （可选）通过端云一体化开发工程调试本地云函数 > 调用本地云函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a3b162c253456b5fb5f9f342e9c1fa4f02579f85c93c45a4a2efd3c751b9bfa8
---

## 约束与限制

支持Phone、Tablet、Wearable、TV设备。并且从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 设置“设备端口”到“主机端口”的映射

调用本地云函数之前，请按照以下示例设置“设备端口”到“主机端口”的映射。详情请参见[创建反向端口转发任务](hdc.md#创建反向端口转发任务)。

```
1. hdc rport tcp:18090 tcp:18090
```

其中，设备端口和主机端口即为Function URI中的端口。

## 在应用中调用本地云函数

从6.0.1(21)版本开始，新增支持调用本地云函数功能。

1. 在项目中导入cloudFunction组件。

   ```
   1. import { cloudFunction } from '@kit.CloudFoundationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[call()](../harmonyos-references/cloudfoundation-cloudfunction.md#call)方法设置函数，在方法中传入函数名称和本地启动的云函数地址，返回调用结果。

   * （可选）通过设置timeout属性对云函数设置超时时长，单位为毫秒。
   * （可选）通过设置version属性对云函数设置函数版本号，默认为最新版本'$latest'。
   * （可选）如果函数有入参，可以将data参数转化为JSON对象或JSON字符串传入，如果没有参数则不传。

   使用Promise异步回调：

   ```
   1. function callFunctionLocal() {
   2. cloudFunction.call({
   3. name: 'my-cloud-function', // my-cloud-function需替换为实际的函数名
   4. version: '$latest',   // 如果不传入版本号，默认为“$latest”。
   5. timeout: 10 * 1000,   // 单位为毫秒，默认为70*1000毫秒。
   6. data: {               // data为函数请求体
   7. param1: 'val1',
   8. param2: 'val2'
   9. },
   10. localUrl: 'http://localhost:18090' // 本地启动的云函数地址
   11. }).then((value: cloudFunction.FunctionResult) => {
   12. hilog.info(0x0000, 'testTag', `Succeeded in calling the function, result: ${JSON.stringify(value.result)}`);
   13. }).catch((err: BusinessError) => {
   14. hilog.error(0x0000, 'testTag', `Failed to call the function, code: ${err.code}, message: ${err.message}`);
   15. })
   16. }
   ```

   或者，使用callback异步回调：

   ```
   1. function callFunctionLocal() {
   2. cloudFunction.call({
   3. name: 'my-cloud-function', // my-cloud-function需替换为实际的函数名
   4. version: '$latest',   // 如果不传入版本号，默认为“$latest”。
   5. timeout: 10 * 1000,   // 单位为毫秒，默认为70*1000毫秒。
   6. data: {               // data为函数请求体
   7. param1: 'val1',
   8. param2: 'val2'
   9. },
   10. localUrl: 'http://localhost:18090' // 本地启动的云函数地址
   11. }, (err: BusinessError, value: cloudFunction.FunctionResult) => {
   12. if (err) {
   13. hilog.error(0x0000, 'testTag', `Failed to call the function, code: ${err.code}, message: ${err.message}`);
   14. return;
   15. }
   16. hilog.info(0x0000, 'testTag', `Succeeded in calling the function, result: ${JSON.stringify(value.result)}`);
   17. })
   18. }
   ```
