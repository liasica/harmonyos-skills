---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-funccoding
title: 开发函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 开发函数
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:07+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:4f526d47347ae65293a78e73cf0108d7f076e8bf2805b786d18d205fa413d447
---

函数创建并配置完成后，您便可以开始编写函数业务代码了。

1. 打开函数入口文件，编写函数代码。关于开发函数代码的更详细信息，请参考[开发函数](cloudfoundation-develop-function-nodejs.md)。

   此处我们以函数“my-cloud-function”为例，构造一个用于返回时间戳的函数。

   **说明** 

   由于云函数存在多种请求方式，开发函数时，建议按照如下示例获取请求体，以兼容所有请求方式：

   let body = event.body ? JSON.parse(event.body) : event;

   ```screen
   /**
    * Describe the basic method of Cloud Functions
    */

   let myHandler = function(event, context, callback, logger){
       // example of display environment variables
       let env1 = context.env.env1;

       // example of display logs
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

           // print input parameters and environment variables
           let request = event.body ? JSON.parse(event.body): event;
           logger.info("request: " + JSON.stringify(request));
           logger.info("env1: " + env1);

           endTime = process.uptime() * 1000;
           interval = endTime - startTime;
           logger.info("intervalTime: " + interval);
           logger.info("--------Finished-------");

           let res = new context.HTTPResponse(context.env, {
               "res-type": "context.env",
               "faas-content-type": "json",
           }, "application/json", "200");
           res.body = {"intervalTime": interval};
           callback(res);
       } catch (error) {
           logger.error("--------Error-------");
           logger.error("error: " + error);
           callback(error);
       }
   };

   module.exports.myHandler = myHandler;
   ```

   **注意** 

   云函数之间是相互独立的，部署至云侧时，只会部署所选云函数目录下的文件，不可在一个云函数中通过import '../anotherDirectory/xxx'的方式引入依赖。如果有多个云函数公共的配置，建议存储在云数据库中，通过云数据库Server API类查询出公共配置；也可以将多个云函数整合成一个云对象，将公共配置变成云对象的私有配置。

2. （可选）如函数存在依赖关系，可在“package.json”文件的“dependencies”下添加需要的依赖，然后点击右上角“Sync Now”。

   下文以添加“@hw-agconnect/cloud-server”依赖为例进行说明，请添加实际业务所需的依赖。

   **说明** 

   右击“package.json”文件，选择“Run 'npm install'”菜单，也可以实现依赖包安装。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/nSYvYuamRmmnpjxPXyfkxQ/zh-cn_image_0000002425891501.png)

   所有安装的依赖包都会存储在当前函数的“node\_modules”目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/dV3WVpqgQtWHMWoGKWy_NQ/zh-cn_image_0000002392213118.png)
