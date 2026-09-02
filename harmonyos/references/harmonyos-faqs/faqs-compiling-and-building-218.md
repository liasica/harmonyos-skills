---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-218
title: 使用HMRouter报错moduleContext is null in hvigorfile
breadcrumb: FAQ > DevEco Studio > 编译构建 > 使用HMRouter报错moduleContext is null in hvigorfile
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d70ba9dd5b98abd5e0aa7243d5da787747d7816e774f576c5467982ee8a76016
---

## 问题现象

安装配置HMRouter，在添加plugins:[hapPlugin()]时，报错：

```screen
moduleContext is null in hvigorfile
```

## 背景知识

[HMRouter](../best-practices/bpta-hmrouter.md)是HarmonyOS上的一款页面跳转场景解决方案，主要用于解决应用中页面间的相互跳转问题。该路由器提供了多种功能特性，包括：

* 自定义注解实现路由跳转：开发者可以通过为页面添加@HMRouter注解来配置页面的跳转路径。
* 支持HAR/HSP：HMRouter支持处理不同的页面类型，如单例页面和Dialog页面。
* 路由拦截和生命周期管理：支持定义拦截器和生命周期，用于处理页面跳转前后的逻辑。
* 简化动画配置：允许开发者配置全局动画或特定页面的切换动画。

## 问题定位

检查hapPlugin插件配置是否正确，是否配置在了entry模块的hvigorfile.ts文件中。

## 分析结论

根据配置文件分析，hapPlugin插件配置在了工程根目录下的hvigorfile.ts ，会报错找不到hap模块的上下文。

## 修改建议

1. 在工程根目录下hvigor下的hvigor-config.json5文件中配置HMRouter依赖。

   ```json
   {
     "modelVersion": "6.0.0",
     "dependencies": {
       "@hadss/hmrouter-plugin": "^1.0.0-rc.11"
     },
     "execution": {
       // "analyze": "normal",                     /* Define the build analyze mode. Value: [ "normal" | "advanced" | "ultrafine" | false ]. Default: "normal" */
       // "daemon": true,                          /* Enable daemon compilation. Value: [ true | false ]. Default: true */
       // "incremental": true,                     /* Enable incremental compilation. Value: [ true | false ]. Default: true */
       // "parallel": true,                        /* Enable parallel compilation. Value: [ true | false ]. Default: true */
       // "typeCheck": false,                      /* Enable typeCheck. Value: [ true | false ]. Default: false */
       // "optimizationStrategy": "memory"         /* Define the optimization strategy. Value: [ "memory" | "performance" ]. Default: "memory" */
     },
     "logging": {
       // "level": "info"                          /* Define the log level. Value: [ "debug" | "info" | "warn" | "error" ]. Default: "info" */
     },
     "debugging": {
       // "stacktrace": false                      /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */
     },
     "nodeOptions": {
       // "maxOldSpaceSize": 8192                  /* Enable nodeOptions maxOldSpaceSize compilation. Unit M. Used for the daemon process. Default: 8192*/
       // "exposeGC": true                         /* Enable to trigger garbage collection explicitly. Default: true*/
     }
   }
   ```
2. 将工程根目录下hvigorfile.ts中的hapPlugin配置转移到entry目录下的hvigorfile.ts中。

   ```ts
   // entry模块的hvigorfile.ts
   import { hapTasks } from '@ohos/hvigor-ohos-plugin';
   import { hapPlugin } from '@hadss/hmrouter-plugin';

   export default {
     system: hapTasks,
     plugins: [hapPlugin()] // 使用HMRouter标签的模块均需要配置，与模块类型保持一致
   }
   ```
