---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-develop-function-nodejs
title: Node.js
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 开发函数 > Node.js
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:05+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:9626b01e293f0348a190ef859a3f103e3622d3226ed87868d46befcc7f492784
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 入口方法

入口方法定义如下：

```typescript
module.exports.myHandler = function(event, context, callback, logger)
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

```typescript
let env1 = context.env.env1;
```

若环境变量未配置，则会返回环境变量为undefined。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/jxDwMBM3Q_2vbAiwaKRrJQ/zh-cn_image_0000002712245104.png)

## 异常处理

开发者可以在函数代码中捕获异常，封装成error对象返回给调用方。对于函数执行期间被平台捕获的异常，平台同样以error对象形式返回给调用方。error对象定义如下。

```typescript
let error = {
    code: xxxxxx,
    message: "xxxxxxxx"
};
```

其中code为错误码，message为错误码的描述信息。

示例代码如下：

```typescript
try {
    logger.info(JSON.stringify(event));
    let result = { message: "success" };
    callback(result);
} catch (err) {
    let error = {
        code: 400,
        message: err.message
    };
    callback(error);
}
```

## 函数示例

示例函数如下：

**说明** 

示例代码中入口方法myHandler()的返回值类型仅供参考，开发者可以根据实际需要定义。

```javascript
let myHandler = function (event, context, callback, logger) {

    let env1 = context.env.env1;
    logger.info("Test info log");
    logger.warn("Test warn log");
    logger.debug("Test debug log");
    logger.error("Test error log");

    logger.info("--------Start-------");
    try {
        let startTime = new Date().getTime();
        let endTime = startTime;
        let interval = 0;
        startTime = process.uptime() * 1000;

        logger.info("request: " + JSON.stringify(event.request));
        logger.info("env1: " + env1);

        endTime = process.uptime() * 1000;
        interval = endTime - startTime;
        logger.info("intervalTime: " + interval);
        logger.info("--------Finished-------");

        let res = new context.HTTPResponse(context.env, {
            "res-type": "context.env",
            "faas-content-type": "json"
        }, "application/json", "200");
        res.body = { "intervalTime": interval };
        callback(res);
    } catch (error) {
        logger.error("--------Error-------");
        logger.error("error: " + error);
        callback(error);
    }
};

module.exports.myHandler = myHandler;
```

## 准备函数部署包

上传的Node.js函数部署包须使用如下结构，处理程序所在代码文件，例如示例中的handler.js，必须在zip包根目录下，依赖项放到node\_modules目录下。

```txt
my-function.zip
  |---- handler.js
  |---- node_modules
    |----async
    |----async-listener
```

可通过npm工具的相关命令，安装与管理依赖。例如npm install xxx命令（执行路径无限制）可将依赖xxx自动安装到根目录的node\_modules文件夹下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/2VrOHdsAShKDXsEF9loFnw/zh-cn_image_0000002742004053.png)
