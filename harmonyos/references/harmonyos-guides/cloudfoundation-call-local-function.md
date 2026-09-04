---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-local-function
title: 调用本地云函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > （可选）通过端云一体化开发工程调试本地云函数 > 调用本地云函数
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:05+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:af08afa1b34f977f64ecbaf6edcb92dc22cf93f14621744a98dddc73c981d057
---

## 约束与限制

支持Phone、Tablet、Wearable、TV设备。并且从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 设置“设备端口”到“主机端口”的映射

调用本地云函数之前，请按照以下示例设置“设备端口”到“主机端口”的映射。详情请参见[创建反向端口转发任务](hdc.md#创建反向端口转发任务)。

```shell
hdc rport tcp:18090 tcp:18090
```

其中，设备端口和主机端口即为Function URI中的端口。

## 在应用中调用本地云函数

从6.0.1(21)版本开始，新增支持调用本地云函数功能。

1. 导入相关模块。

   ```typescript
   import { cloudFunction } from '@kit.CloudFoundationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[call()](../harmonyos-references/cloudfoundation-cloudfunction.md#call)方法设置函数，在方法中传入函数名称和本地启动的云函数地址，返回调用结果。

   * （可选）通过设置timeout属性对云函数设置超时时长，单位为ms。
   * （可选）通过设置version属性对云函数设置函数版本号，默认为最新版本'$latest'。
   * （可选）如果函数有入参，可以将data参数转化为JSON对象或JSON字符串传入，如果没有参数则不传。

   使用Promise异步回调：

   ```typescript
   cloudFunction.call({
     name: 'my-cloud-function', // my-cloud-function需替换为实际的函数名
     version: '$latest', // 如果不传入版本号，默认为“$latest”。
     timeout: 10 * 1000, // 单位为ms，默认为70*1000ms。
     data: {
       // data为函数请求体
       param1: 'val1',
       param2: 'val2'
     },
     localUrl: 'http://localhost:18090' // 本地启动的云函数地址
   }).then((res: cloudFunction.FunctionResult) => {
     hilog.info(0x0000, 'function', `Succeeded in calling the function, result: ${JSON.stringify(res.result)}`);
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'function', `Failed to call the function, code: ${err.code}, message: ${err.message}`);
   });
   ```

   或者，使用callback异步回调：

   ```typescript
   cloudFunction.call({
     name: 'my-cloud-function', // my-cloud-function需替换为实际的函数名
     version: '$latest', // 如果不传入版本号，默认为“$latest”。
     timeout: 10 * 1000, // 单位为ms，默认为70*1000ms。
     data: {
       // data为函数请求体
       param1: 'val1',
       param2: 'val2'
     },
     localUrl: 'http://localhost:18090' // 本地启动的云函数地址
   }, (err: BusinessError, res: cloudFunction.FunctionResult) => {
     if (err) {
       hilog.error(0x0000, 'function', `Failed to call the function, code: ${err.code}, message: ${err.message}`);
       return;
     }
     hilog.info(0x0000, 'function', `Succeeded in calling the function, result: ${JSON.stringify(res.result)}`);
   });
   ```
3. 打开entry的“Run/Debug Configurations”窗口，勾选“Allow multiple instances”。若未勾选，启动entry调试任务时，系统会终止云函数调试进程。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/vLdaJLkURy-0NBSuU7Nblg/zh-cn_image_0000002712245122.png)
