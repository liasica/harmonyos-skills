---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-threading-model-troubleshooting-0001
title: HAR包中创建Worker失败问题定位
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 故障排查 > HAR包中创建Worker失败问题定位
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:23+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:779b18e70bdad4a2d70b0af49f83d2f739030ab779f2c46a2d267986721c6de4
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

## 定位过程

1. 根据报错信息创建Worker过程中路径不正确，对比[文件路径注意事项](../harmonyos-guides/worker-introduction.md#文件路径注意事项)中加载HAR中Worker线程文件场景，当开启useNormalizedOHMUrl或HAR包会被打包成三方包使用时，HAR包中使用Worker仅支持通过相对路径的加载形式创建。
2. 若使用相对路径加载Worker，检查创建Worker实例的文件与Worker文件本身是否在同一包内。

## 分析结论

工程级build-profile.json5配置useNormalizedOHMUrl为true，仅支持通过相对路径的加载形式创建。创建Worker对象所在文件与Worker线程文件不在同一包内，导致用相对路径加载Worker无法识别。

## 修改建议

当useNormalizedOHMUrl设置为true时需满足以下两个条件：

1. 使用相对路径引用Worker文件；
2. 创建Worker对象所在文件与Worker线程文件需在同一个包内。

* 在harB包Worker文件同一包内创建工具类，使用相对路径引用Worker文件，封装常用方法；

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
* 在harB模块根目录的Index.ets文件导出工具类；

  ```ts
  export { WorkerUtil } from './src/main/ets/workers/WorkerUtil';
  ```
* 在harA的oh-package.json5文件中引入harB依赖；

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
