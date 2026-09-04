---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-cloud-interdev
title: 开发预加载资源接口
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 开发预加载资源接口
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:06+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:728b08d645bae8ddcf03998b38958d4cb47b03cd115b7ee9d858032621e73730
---

使用预加载服务之前，开发者需要完成云侧接口的开发，以提供预加载所需的资源数据。华为提供两种方式供开发者选择：云函数和开发者服务器，开发者可根据实际业务需要进行选择。

## 云函数

开发者需要先按照云函数接口规范开发函数，然后在AGC云端创建函数，并可测试函数运行是否正常。流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/bmqAJsMKRDCkfSlNPODi3A/zh-cn_image_0000002712405092.png)

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

  ```javascript
  import axios from 'axios';

  let myHandler = async function (event, context, callback, logger) {
      logger.info("event:" + JSON.stringify(event));
      let env1 = context.env.env1; // 获取环境变量env1
      logger.info("env1: " + env1)
      try {
          let body = event.body ? JSON.parse(event.body) : event;
          let appId = body.appId;

          logger.info("appId: " + appId);

          // http请求示例，请按照实际业务修改
          let url = 'https://example.com/prefetchApi';  // 页面资源数据的请求url
          let headers = { 'k1': 'v1' };  // 请求header
          let res;  // 返回数据
          await axios.post(url, {}, { headers })  // http post请求
              .then(response => {
                  res = response.data;
              })
          logger.info("--------Finished-------");
          callback(res);
      } catch (error) {
          logger.error("--------Error-------");
          logger.error("error: " + error);
          callback(error);
      }
  };

  export { myHandler };
  ```
* 周期性预加载

  ```javascript
  import axios from 'axios';

  let myHandler = async function (event, context, callback, logger) {
      logger.info("event:" + JSON.stringify(event));
      let env1 = context.env.env1; // 获取环境变量env1
      logger.info("env1: " + env1)
      try {
          let body = event.body ? JSON.parse(event.body) : event;
          let appId = body.appId;
          let token = body.token;
          let paramsStr = body.params; // 如果需要解析json结构paramsStr中的参数，需要使用 let params = JSON.parse(paramsStr);

          logger.info("appId: " + appId + ",token:" + token + ",params:" + paramsStr);

          // http请求示例，请按照实际业务修改
          let url = 'https://example.com/prefetchApi'; // 页面资源数据的请求url
          let headers = { 'k1': 'v1' }; // 请求header
          let res; // 返回数据
          await axios.post(url, {}, { headers }) // http post请求
              .then(response => {
                  res = response.data;
              })
          logger.info("--------Finished-------");
          callback(res);
      } catch (error) {
          logger.error("--------Error-------");
          logger.error("error: " + error);
          callback(error);
      }
  };

  export { myHandler };
  ```
* 跳链安装预加载

  ```javascript
  import axios from 'axios';

  let myHandler = async function (event, context, callback, logger) {
      logger.info("event:" + JSON.stringify(event));
      let env1 = context.env.env1; // 获取环境变量env1
      logger.info("env1: " + env1)
      try {
          let body = event.body ? JSON.parse(event.body) : event;
          let appId = body.appId;
          let link = body.link; // 跳链安装预加载link信息

          logger.info("appId: " + appId + ",link:" + link);

          // http请求示例，请按照实际业务修改
          let url = 'https://example.com/prefetchApi'; // 页面资源数据的请求url
          let headers = { 'k1': 'v1' }; // 请求header
          let res; // 返回数据
          await axios.post(url, {}, { headers }) // http post请求
              .then(response => {
                  res = response.data;
              })
          logger.info("--------Finished-------");
          callback(res);
      } catch (error) {
          logger.error("--------Error-------");
          logger.error("error: " + error);
          callback(error);
      }
  };

  export { myHandler };
  ```

## 开发者服务器

开发者使用自己的服务器自行开发和实现预加载资源接口，接口需遵循开发者服务器接口规范。

### 开发者服务器接口规范

| 预加载类型 | API/PATH名称 | 说明 | 参数 | 请求方式 | 返回值 |
| --- | --- | --- | --- | --- | --- |
| 安装预加载 | 自定义 | 获取预加载数据接口 | appId：应用ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。 | GET | 自定义JSON字符串 |
| 周期性预加载 | 自定义 | 获取预加载数据接口 | - appId：应用ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。  - token：可选，注册周期性预加载任务时开发者自行传入的用户级认证信息，长度不超过2048个字符。  - params：可选，注册周期性预加载任务时开发者自行传入的自定义参数，长度不超过1024个字符。 | GET | 自定义JSON字符串 |
| 跳链安装预加载 | 自定义 | 获取预加载数据接口 | - appId：应用ID，获取方法请参见[查看应用信息](../app/agc-help-view-app-info-0000002282674569.md)。  - link：可选，跳链安装预加载延迟链接。 | GET | 自定义JSON字符串 |

### 示例

定义名称为prefetchData的接口，示例如下：

```txt
https://www.example.com/prefetchData?appId=1234&token=xxxx&params=yyyy
```
