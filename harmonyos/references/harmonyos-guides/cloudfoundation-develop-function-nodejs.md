---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-develop-function-nodejs
title: Node.js
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 开发函数 > Node.js
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:11b3e11aced4e5fb53628805be9a51fe7b27beac12903ee6570d95297d8f80e3
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 入口方法

入口方法定义如下：

```
1. module.exports.myHandler = function(event, context, callback, logger)
```

* myHandler：入口方法名称。
* event：调用方传递的事件对象，JSON格式。具体内容请参见[event对象](../AppGallery-connect-Guides/agc-cloudfunction-trigger-event-0000001620581529.md)。
* context：函数运行时上下文对象，封装了日志接口、回调接口、环境变量env对象等。
* callback：事件处理结果。
* logger：记录日志。

函数必须通过显式调用callback(object)将事件处理结果返回给AppGallery Connect（简称AGC），结果可以是任意对象，但必须与JSON.stringify兼容，AGC会将结果转换成JSON字符串后，返回给调用方。callback执行完成，函数即执行结束。

完整的Node.js 20.x云函数示例代码请参考[函数示例](cloudfoundation-develop-function-nodejs.md#函数示例)。

## 日志记录

开发者可在代码中使用logger接口记录日志，后端已通过global.logger全局定义，目前支持四种级别：

* logger.debug()
* logger.error()
* logger.warn()
* logger.info()

## 获取环境变量

开发者可在代码中使用context.env.key访问环境变量，获取环境变量env1示例如下：

```
1. let env1 = context.env.env1;
```

若环境变量未配置，则会返回环境变量为undefined。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/YL-wsJ9iQkKhJTQ0wjPXhg/zh-cn_image_0000002552799194.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=D3C8C4B76E87EEA3939DB514D9BE8E6EFF25C4367C6CC7508FD9868B241176BB)

## 异常处理

开发者可以在函数代码中捕获异常，封装成error对象返回给调用方。对于函数执行期间被平台捕获的异常，平台同样以error对象形式返回给调用方。error对象定义如下。

```
1. let error = {
2. code: xxxxxx,
3. message: "xxxxxxxx"
4. };
```

其中code为错误码，message为错误码的描述信息。

示例代码如下：

```
1. try {
2. logger.info(JSON.stringify(event));
3. let result = { message: "success" };
4. callback(result);
5. } catch (err) {
6. let error = {
7. code: 400,
8. message: err.message
9. };
10. callback(error);
11. }
```

## 函数示例

示例函数如下：

说明

示例代码中入口方法myHandler()的返回值类型仅供参考，开发者可以根据实际需要定义。

```
1. /**
2. * Describe the basic method of Cloud Functions
3. */

5. let myHandler = function (event, context, callback, logger) {
6. // example of display environment variables
7. let env1 = context.env.env1;

9. // example of display logs
10. logger.info("Test info log");
11. logger.warn("Test warn log");
12. logger.debug("Test debug log");
13. logger.error("Test error log");

15. logger.info("--------Start-------");
16. try {
17. let startTime = new Date().getTime();
18. let endTime = startTime;
19. let interval = 0;
20. startTime = process.uptime() * 1000;

22. // print input parameters and environment variables
23. logger.info("request: " + JSON.stringify(event.request));
24. logger.info("env1: " + env1);

26. endTime = process.uptime() * 1000;
27. interval = endTime - startTime;
28. logger.info("intervalTime: " + interval);
29. logger.info("--------Finished-------");

31. let res = new context.HTTPResponse(context.env, {
32. "res-type": "context.env",
33. "faas-content-type": "json"
34. }, "application/json", "200");
35. res.body = { "intervalTime": interval };
36. callback(res);
37. } catch (error) {
38. logger.error("--------Error-------");
39. logger.error("error: " + error);
40. callback(error);
41. }
42. };

44. module.exports.myHandler = myHandler;
```

## 准备函数部署包

上传的Node.js函数部署包须使用如下结构，处理程序所在代码文件，例如示例中的handler.js，必须在zip包根目录下，依赖项放到node\_modules目录下。

```
1. my-function.zip
2. |---- handler.js
3. |---- node_modules
4. |----async
5. |----async-listener
```

可通过npm工具的相关命令，安装与管理依赖。例如npm install xxx命令（执行路径无限制）可将依赖xxx自动安装到根目录的node\_modules文件夹下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/Opx-s0j8QQOLaPB8hQvJ3w/zh-cn_image_0000002583438889.png?HW-CC-KV=V1&HW-CC-Date=20260427T234839Z&HW-CC-Expire=86400&HW-CC-Sign=415961093B74ADC7AE5DFAC88C7E1C742D71B94A041F3FF6A657AB3564C2EB83)
