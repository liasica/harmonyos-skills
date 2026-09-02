---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-9
title: useNormalizedOHMUrl配置为true导致HAR包中创建Worker失败
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > useNormalizedOHMUrl配置为true导致HAR包中创建Worker失败
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b2eb4399cd636d269dac7063881085d614d68305857f031b480aedff411301c5
---

## 问题现象

在entry模块调用harA的文件，harA中用@标识加载harB的Worker文件，运行闪退。

```txt
Reason:Signal:SIGABRT(SI_TKILL)@0x01317b55000014a6 from:5286:20020053
LastFatalMessage:[default] [LoadJSPandaFile:106] resolveBufferCallback get hsp buffer failed, hsp path:/data/storage/el1/bundle/harA/ets/modules.abc, errorMsg:hap path error: /data/storage/el1/bundle/harA.hsp
```

harA中改用相对路径加载harB的Worker文件，运行依旧闪退。

```ts
const testWorker: worker.ThreadWorker = new worker.ThreadWorker('../../../../../harB/src/main/ets/workers/Worker.ets');
```

```txt
Reason:ReferenceError
Error name:ReferenceError
Error message:Cannot find module '@normalized:N&&&harB/src/main/ets/workers/Worker&1.0.0&1.0.0' imported from ''.
```

## 背景知识

使用Worker模块具体功能时，须先构造Worker实例对象，其构造函数与API版本相关，且构造函数需要传入Worker线程文件的路径（scriptURL）。参考[文件路径注意事项](../harmonyos-guides/worker-introduction.md#文件路径注意事项)：

Stage模型下加载HAR中Worker线程文件存在以下两种情况：

* @标识路径加载形式：所有种类的模块加载本地HAR中的Worker线程文件，加载路径规则：@{moduleName}/ets/{relativePath}。
* 相对路径加载形式：本地HAR加载该包内的Worker线程文件，加载路径规则：创建Worker对象所在文件与Worker线程文件的相对路径。

**说明** 

当开启useNormalizedOHMUrl（即将工程目录中与entry同级别的应用级[build-profile.json5](../harmonyos-guides/ide-hvigor-build-profile-app.md)文件中[strictMode](../harmonyos-guides/ide-hvigor-build-profile-app.md#section13181758123312)属性的useNormalizedOHMUrl字段配置为true）或HAR包会被打包成三方包使用时，则HAR包中使用Worker仅支持通过相对路径的加载形式创建。

## 问题定位

1. 根据报错信息创建Worker过程中路径不正确，对比文件路径注意事项中加载HAR中Worker线程文件场景，当开启useNormalizedOHMUrl或HAR包会被打包成三方包使用时，HAR包中使用Worker仅支持通过相对路径的加载形式创建。
2. 若使用相对路径加载Worker，检查创建Worker实例的文件与Worker文件本身是否在同一包内。

## 分析结论

工程级build-profile.json5配置useNormalizedOHMUrl为true，仅支持通过相对路径的加载形式创建。创建Worker对象所在文件与Worker线程文件不在同一包内，导致用相对路径加载Worker无法识别。

## 修改建议

当useNormalizedOHMUrl设置为true时需满足以下两个条件：

1. 使用相对路径引用Worker文件。
2. 创建Worker对象所在文件与Worker线程文件需在同一个包内。

* 在harB包Worker文件同一包内创建工具类，使用相对路径引用Worker文件，封装常用方法。

  ```ts
  import { worker } from '@kit.ArkTS';

  export class WorkerUtil {
    // 在worker文件同一包内创建实例
    private testWorker: worker.ThreadWorker = new worker.ThreadWorker('../workers/WorkerTest.ets');

    postMsg(args: Object) {
      try {
        // 使用实例发送消息
        this.testWorker.postMessage(args);
      } catch (error) {
        // Implement error handling.
      }
    }
  }
  ```
* 在harB模块根目录的Index.ets文件导出工具类。

  ```ts
  export { WorkerUtil } from './src/main/ets/workers/WorkerUtil';
  ```
* 在harA的oh-package.json5文件中引入harB依赖。

  ```json
  {
    "name": "hara",
    "version": "1.0.0",
    "description": "Please describe the basic information.",
    "main": "Index.ets",
    "author": "",
    "license": "Apache-2.0",
    "dependencies": {
      "harb": 'file:../harB'
    }
  }
  ```
* 在harA调用方引入工具类，使用工具类实例对象调用常用方法。

  ```ts
  import { WorkerUtil } from 'harb';

  @Component
  export struct MainPage {
    build() {
      Row() {
        Column() {
          Text('Hello World')
            .fontSize($r('app.float.page_text_font_size'))
            .fontWeight(FontWeight.Bold)
            .onClick(() => {
              // 创建harB的工具类WorkerUtil实例
              let workerUtil: WorkerUtil = new WorkerUtil();
              workerUtil.postMsg(1);
            })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```

## 常见FAQ

Q：在项目中引入ijkplayer实现录屏功能，引入ijkplayer本地HAR包后，编译时提示useNormalizedOHMUrl is not true，将该属性设置为true时，再打开项目时，整个项目直接出现白屏，无法进入到首页。报错信息如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/8XfbqsF4TOanDbuTjAqkyg/zh-cn_image_0000002659138347.png "点击放大")

A：根据报错信息分析得出是Worker路径不对，Worker使用有这样一个限制，当开启useNormalizedOHMUrl（在工程目录中与entry同级别的应用级build-profile.json5文件中，将strictMode属性下的useNormalizedOHMUrl字段配置为true）或HAR包被打包成三方包使用时，HAR包中使用Worker仅支持通过相对路径的加载形式创建。可参考Worker线程文件路径注意事项。
