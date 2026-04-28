---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-cloud-interdev
title: 开发预加载资源接口
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 开发预加载资源接口
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d358958aa7b137111d29e199b31c332f6f1f7f7f8ced498187613661d33df1d
---

使用预加载服务之前，开发者需要完成云侧接口的开发，以提供预加载所需的资源数据。华为提供两种方式供开发者选择：云函数和开发者服务器，开发者可根据实际业务需要进行选择。

## 云函数

开发者需要先按照云函数接口规范开发函数，然后在AGC云端创建函数，并可测试函数运行是否正常。流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/VnCdIrYUSxWwbfKQIO-wUQ/zh-cn_image_0000002583438917.png?HW-CC-KV=V1&HW-CC-Date=20260427T234845Z&HW-CC-Expire=86400&HW-CC-Sign=D06741B6410D83286D764EDBC0AFFB746BE8CBF5668961A2127DF4DB784C5618)

1. [开发函数](cloudfoundation-develop-function-nodejs.md)：按照云函数接口规范开发函数。
2. [创建函数](cloudfoundation-create-and-config-function.md)：函数业务代码开发完成后，即可在AGC云端创建函数。
3. [测试函数](cloudfoundation-test-function.md)：对函数进行测试，以确保函数代码运行正常。

### 云函数接口规范

| 预加载类型 | API名称 | 说明 | 参数 | 返回值 |
| --- | --- | --- | --- | --- |
| 安装预加载 | 自定义 | 获取预加载数据接口 | event.body.appId：应用ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。 | 自定义JSON字符串 |
| 周期性预加载 | 自定义 | 获取预加载数据接口 | - event.body.appId：应用ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。  - event.body.token：可选，注册周期性预加载任务时开发者自行传入的用户级认证信息，长度不超过2048个字符。  - event.body.params：可选，注册周期性预加载任务时开发者自行传入的自定义参数，长度不超过1024个字符。 | 自定义JSON字符串 |
| 跳链安装预加载 | 自定义 | 获取预加载数据接口 | - event.body.appId：应用ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。  - event.body.link：可选，跳链安装预加载延迟链接。 | 自定义JSON字符串 |

### 示例

[端云一体化工程](agc-harmonyos-clouddev-funccoding.md)预加载云函数示例如下。其中，axios依赖库为网络请求库，需要在“cloudfunctions/云函数名称/package.json”的“dependencies”中添加axios的1.7.7或以上版本依赖。

* 安装预加载

  ```
  1. import axios from 'axios';

  3. let myHandler = async function (event, context, callback, logger) {
  4. logger.info("event:" + JSON.stringify(event));
  5. let env1 = context.env.env1; // 环境变量
  6. logger.info("env1: " + env1)
  7. try {
  8. let body = event.body ? JSON.parse(event.body) : event;
  9. let appId = body.appId;

  11. logger.info("appId: " + appId);

  13. // http请求示例，请按照实际业务修改
  14. let url = 'https://example.com/prefetchApi';  // 页面资源数据的请求url
  15. let headers = { 'k1': 'v1' };  // 请求header
  16. let res;  // 返回数据
  17. await axios.post(url, {}, { headers })  // http post请求
  18. .then(response => {
  19. res = response.data;
  20. })
  21. logger.info("--------Finished-------");
  22. callback(res);
  23. } catch (error) {
  24. logger.error("--------Error-------");
  25. logger.error("error: " + error);
  26. callback(error);
  27. }
  28. };

  30. export { myHandler };
  ```
* 周期性预加载

  ```
  1. import axios from 'axios';

  3. let myHandler = async function (event, context, callback, logger) {
  4. logger.info("event:" + JSON.stringify(event));
  5. let env1 = context.env.env1; // 环境变量
  6. logger.info("env1: " + env1)
  7. try {
  8. let body = event.body ? JSON.parse(event.body) : event;
  9. let appId = body.appId;
  10. let token = body.token;
  11. let paramsStr = body.params; // 如果需要解析json结构paramsStr中的参数，需要使用 let params = JSON.parse(paramsStr);

  13. logger.info("appId: " + appId + ",token:" + token + ",params:" + paramsStr);

  15. // http请求示例，请按照实际业务修改
  16. let url = 'https://example.com/prefetchApi'; // 页面资源数据的请求url
  17. let headers = { 'k1': 'v1' }; // 请求header
  18. let res; // 返回数据
  19. await axios.post(url, {}, { headers }) // http post请求
  20. .then(response => {
  21. res = response.data;
  22. })
  23. logger.info("--------Finished-------");
  24. callback(res);
  25. } catch (error) {
  26. logger.error("--------Error-------");
  27. logger.error("error: " + error);
  28. callback(error);
  29. }
  30. };

  32. export { myHandler };
  ```
* 跳链安装预加载

  ```
  1. import axios from 'axios';

  3. let myHandler = async function (event, context, callback, logger) {
  4. logger.info("event:" + JSON.stringify(event));
  5. let env1 = context.env.env1; // 环境变量
  6. logger.info("env1: " + env1)
  7. try {
  8. let body = event.body ? JSON.parse(event.body) : event;
  9. let appId = body.appId;
  10. let link = body.link; // 跳链安装预加载link信息

  12. logger.info("appId: " + appId + ",link:" + link);

  14. // http请求示例，请按照实际业务修改
  15. let url = 'https://example.com/prefetchApi'; // 页面资源数据的请求url
  16. let headers = { 'k1': 'v1' }; // 请求header
  17. let res; // 返回数据
  18. await axios.post(url, {}, { headers }) // http post请求
  19. .then(response => {
  20. res = response.data;
  21. })
  22. logger.info("--------Finished-------");
  23. callback(res);
  24. } catch (error) {
  25. logger.error("--------Error-------");
  26. logger.error("error: " + error);
  27. callback(error);
  28. }
  29. };

  31. export { myHandler };
  ```

## 开发者服务器

申请开通开发者服务器权限之后，开发者使用自己的服务器自行开发和实现预加载资源接口，接口需遵循开发者服务器接口规范。

### 开发者服务器接口规范

| 预加载类型 | API/PATH名称 | 说明 | 参数 | 请求方式 | 返回值 |
| --- | --- | --- | --- | --- | --- |
| 安装预加载 | 自定义 | 获取预加载数据接口 | appId：应用ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。 | GET | 自定义JSON字符串 |
| 周期性预加载 | 自定义 | 获取预加载数据接口 | - appId：应用ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。  - token：可选，注册周期性预加载任务时开发者自行传入的用户级认证信息，长度不超过2048个字符。  - params：可选，注册周期性预加载任务时开发者自行传入的自定义参数，长度不超过1024个字符。 | GET | 自定义JSON字符串 |
| 跳链安装预加载 | 自定义 | 获取预加载数据接口 | - appId：应用ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。  - link：可选，跳链安装预加载延迟链接。 | GET | 自定义JSON字符串 |

### 示例

定义名称为prefetchData的接口，示例如下：

```
1. https://www.example.com/prefetchData?appId=1234&token=xxxx&params=yyyy
```
