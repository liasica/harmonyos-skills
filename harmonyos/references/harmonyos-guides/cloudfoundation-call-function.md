---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-function
title: 调用函数
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 云函数 > 开发云函数 > 调用函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:6b8cf3b03127e27f13f53105e33197daae1da3d339aa177b9592d773011d4f52
---

## 约束与限制

支持Phone、Tablet设备。并且从5.1.0(18)版本开始，新增支持Wearable设备；从5.1.1(19)版本开始，新增支持TV设备；从6.1.0(23)版本开始，新增支持PC/2in1设备。

## 设置云函数配置项

在“entry/src/main/module.json5”文件中添加网络权限。

```typescript
"requestPermissions": [
  {
    "name": "ohos.permission.INTERNET"
  }
]
```

## 查询函数名和版本

在函数的触发器页面点击“HTTP触发器”，查看“触发URL”的后缀，获取触发器的标识，格式为“函数名-版本号”。如下图所示，“myhandlerxxxx-$latest”即为HTTP触发器标识，其中“myhandlerxxxx”为函数名，“$latest”为版本号。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/9nmi3n4pSD6XPj9zZdVLlw/zh-cn_image_0000002706674940.png)

## 在应用中调用函数

1. 导入相关模块。

   ```typescript
   import { cloudFunction } from '@kit.CloudFoundationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 调用[call()](../harmonyos-references/cloudfoundation-cloudfunction.md#call)方法设置函数，在方法中传入函数名称，返回调用结果。

   * （可选）通过设置timeout属性对云函数设置超时时长，单位为ms。
   * （可选）通过设置version属性对云函数设置函数版本号，默认为最新版本'$latest'。
   * （可选）如果函数有入参，可以将data参数转化为JSON对象或JSON字符串传入，如果没有参数则不传。

   使用Promise异步回调：

   ```typescript
   cloudFunction.call({
     name: 'sort', // sort需替换为实际的函数名
     version: '$latest', // 如果不传入版本号，默认为“$latest”。
     timeout: 10 * 1000, // 单位为ms，默认为70*1000ms。
     data: {
       // data为函数请求体
       param1: 'val1',
       param2: 'val2'
     }
   }).then((res: cloudFunction.FunctionResult) => {
     hilog.info(0x0000, 'function', `Succeeded in calling the function, result: ${JSON.stringify(res.result)}`);
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'function', `Failed to call function , code: ${err.code}, message: ${err.message}`);
   });
   ```

   或者，使用callback异步回调：

   ```typescript
   cloudFunction.call({
     name: 'sort-id', // sort-id需替换为实际的函数名
     version: '$latest', // 如果不传入版本号，默认为“$latest”。
     timeout: 10 * 1000, // 单位为ms，默认为70*1000ms。
     data: {
       // data为函数请求体
       param1: 'val1',
       param2: 'val2'
     }
   }, (err: BusinessError, res: cloudFunction.FunctionResult) => {
     hilog.info(0x0000, 'function', `Succeeded in calling the function, result: ${JSON.stringify(res.result)}`);
     if (err) {
       hilog.error(0x0000, 'function', `Failed to call function , code: ${err.code}, message: ${err.message}`);
       return;
     }
   });
   ```
