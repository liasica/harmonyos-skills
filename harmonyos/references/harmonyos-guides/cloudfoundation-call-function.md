---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-function
title: 调用函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 调用函数
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:61981041ac8f836724229dc1270e86be22cda82fd648d25e9dd84fb0ec8b7379
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 设置云函数配置项

在“entry/src/main/module.json5”文件中添加网络权限。

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.INTERNET"
4. }
5. ]
```

## 查询函数名和版本

在函数的触发器页面点击“HTTP触发器”，查看“触发URL”的后缀，获取触发器的标识，格式为“函数名-版本号”。如下图所示，“myhandlerxxxx-$latest”即为HTTP触发器标识，其中“myhandlerxxxx”为函数名，“$latest”为版本号。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/APEpB-lDQfaiCmsJtcMaFw/zh-cn_image_0000002558765360.png?HW-CC-KV=V1&HW-CC-Date=20260429T053741Z&HW-CC-Expire=86400&HW-CC-Sign=819370D30E8C74BEC0542601CBA6A41357E231C2BA6C7A8D024F8544CF9B4587)

## 在应用中调用函数

1. 在项目中导入cloudFunction组件。

   ```
   1. import { cloudFunction } from '@kit.CloudFoundationKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[call()](../harmonyos-references/cloudfoundation-cloudfunction.md#call)方法设置函数，在方法中传入函数名称，返回调用结果。

   * （可选）通过设置timeout属性对云函数设置超时时长，单位为毫秒。
   * （可选）通过设置version属性对云函数设置函数版本号，默认为最新版本'$latest'。
   * （可选）如果函数有入参，可以将data参数转化为JSON对象或JSON字符串传入，如果没有参数则不传。

   使用Promise异步回调：

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { cloudFunction } from '@kit.CloudFoundationKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. function callFunction() {
   6. cloudFunction.call({
   7. name: 'functionName', // functionName需替换为实际的函数名
   8. version: '$latest',   // 如果不传入版本号，默认为“$latest”。
   9. timeout: 10 * 1000,   // 单位为毫秒，默认为70*1000毫秒。
   10. data: {               // data为函数请求体
   11. param1: 'val1',
   12. param2: 'val2'
   13. }
   14. }).then((value: cloudFunction.FunctionResult) => {
   15. hilog.info(0x0000, 'testTag', `Succeeded in calling the function, result: ${JSON.stringify(value.result)}`);
   16. }).catch((err: BusinessError) => {
   17. hilog.error(0x0000, 'testTag', `Failed to call the function, code: ${err.code}, message: ${err.message}`);
   18. })
   19. }
   ```

   或者，使用callback异步回调：

   ```
   1. import { hilog } from '@kit.PerformanceAnalysisKit';
   2. import { cloudFunction } from '@kit.CloudFoundationKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. function callFunction() {
   6. cloudFunction.call({
   7. name: 'functionName', // functionName需替换成实际的函数名
   8. version: '$latest',  // 如果不传入版本号，默认为“$latest”。
   9. timeout: 10 * 1000,  // 单位为毫秒，默认为70*1000毫秒。
   10. data: {              // data为函数请求体
   11. param1: 'val1',
   12. param2: 'val2'
   13. }
   14. }, (err: BusinessError, value: cloudFunction.FunctionResult) => {
   15. if (err) {
   16. hilog.error(0x0000, 'testTag', `Failed to call the function, code: ${err.code}, message: ${err.message}`);
   17. return;
   18. }
   19. hilog.info(0x0000, 'testTag', `Succeeded in calling the function, result: ${JSON.stringify(value.result)}`);
   20. })
   21. }
   ```
3. 如果需要关注函数的返回值，可调用result属性获取。

   ```
   1. let returnValue = value.result;
   ```

   value为步骤2中调用call()方法返回的cloudFunction.FunctionResult对象，返回值为云函数body返回的值，以[测试函数](cloudfoundation-test-function.md)时返回的结果为例，value.result = {"simple":"example"}。
