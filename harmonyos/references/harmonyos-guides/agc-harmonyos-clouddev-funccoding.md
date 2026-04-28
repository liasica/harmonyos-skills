---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-funccoding
title: 开发函数
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 开发函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:55:01+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:77d1d449fb7490ca97d80340ee20af188115b814bf1bb02f07fbc2a2095b1097
---

函数创建并配置完成后，您便可以开始编写函数业务代码了。

1. 打开函数入口文件，编写函数代码。关于开发函数代码的更详细信息，请参考[开发函数](cloudfoundation-develop-function-nodejs.md)。

   此处我们以函数“my-cloud-function”为例，构造一个用于返回时间戳的函数。

   说明

   由于云函数存在多种请求方式，开发函数时，建议按照如下示例获取请求体，以兼容所有请求方式：

   let body = event.body ? JSON.parse(event.body) : event;

   ```
   1. /**
   2. * Describe the basic method of Cloud Functions
   3. */

   5. let myHandler = function(event, context, callback, logger){
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
   23. let request = event.body ? JSON.parse(event.body): event;
   24. logger.info("request: " + JSON.stringify(request));
   25. logger.info("env1: " + env1);

   27. endTime = process.uptime() * 1000;
   28. interval = endTime - startTime;
   29. logger.info("intervalTime: " + interval);
   30. logger.info("--------Finished-------");

   32. let res = new context.HTTPResponse(context.env, {
   33. "res-type": "context.env",
   34. "faas-content-type": "json",
   35. }, "application/json", "200");
   36. res.body = {"intervalTime": interval};
   37. callback(res);
   38. } catch (error) {
   39. logger.error("--------Error-------");
   40. logger.error("error: " + error);
   41. callback(error);
   42. }
   43. };

   45. module.exports.myHandler = myHandler;
   ```

   注意

   云函数之间是相互独立的，部署至云侧时，只会部署所选云函数目录下的文件，不可在一个云函数中通过import '../anotherDirectory/xxx'的方式引入依赖。如果有多个云函数公共的配置，建议存储在云数据库中，通过云数据库Server API类查询出公共配置；也可以将多个云函数整合成一个云对象，将公共配置变成云对象的私有配置。

2. （可选）如函数存在依赖关系，可在“package.json”文件的“dependencies”下添加需要的依赖，然后点击右上角“Sync Now”。

   下文以添加“@hw-agconnect/cloud-server”依赖为例进行说明，请添加实际业务所需的依赖。

   说明

   右击“package.json”文件，选择“Run 'npm install'”菜单，也可以实现依赖包安装。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/DOLcEcpvT5-v5_DN-kqWGg/zh-cn_image_0000002425891501.png?HW-CC-KV=V1&HW-CC-Date=20260427T235500Z&HW-CC-Expire=86400&HW-CC-Sign=410FDC4C801F21B024D8673B2AFCB4B1FC0AB81DA0A9E26ED6D1D88B18839F6D)

   所有安装的依赖包都会存储在当前函数的“node\_modules”目录下。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/d2QtSY5yT6Cpf4cuLskHGg/zh-cn_image_0000002392213118.png?HW-CC-KV=V1&HW-CC-Date=20260427T235500Z&HW-CC-Expire=86400&HW-CC-Sign=968C003B43B0B0C2F26904F6B82923C83194CBE73C049D9695D59813A5F38D33)
