---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-14
title: ThreadWorker调用postMessage时序列化数据失败
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > ThreadWorker调用postMessage时序列化数据失败
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c92430d3dd50dee191312dfc17ca727aab9ef37acd2b8a1480ef8747eab68635
---

## 问题现象

ThreadWorker调用postMessage时序列化数据失败，报错日志如下：

```txt
Pid:8525
Uid:20020040
Reason:BusinessError
Error name:BusinessError
Error message:An exception occurred during serialization, failed to serialize message.
Error code:
Stacktrace:
at init (im/src/main/ets/components/SocketManager.ets:34:9)
at anonymous (entry/src/main/ets/pages/MainPage.ets:134:37)
```

原始问题代码如下：

```ts
import { SocketManager } from '../SocketManager'

export class IMTask {
  cmdId: number
  needAuth: boolean
  data: Uint8Array
  seq: number

  constructor(cmdId: number, data: Uint8Array, needAuth?: boolean) {
    this.cmdId = cmdId
    this.needAuth = needAuth ?? true
    this.data = data
    this.seq = SocketManager.getInstance().getSeqNum()
  }
}

// socketManager.ets
private seqNum: number = 0
getSeqNum() {
  return this.seqNum++
}
const imWorkStage = new worker.ThreadWorker('../workers/IMWorker', { name: "im-thread" })
imWorkStage.postMessage(new IMTask(PbLoginCmdID.CID_PBLOGIN_SECRET_REQ,pubKey,false))
```

## 背景知识

* worker的主要作用是为应用程序提供一个多线程的运行环境，实现应用程序执行过程与宿主线程分离。通过在后台线程运行脚本处理耗时操作，避免计算密集型或高延迟任务阻塞宿主线程。具体接口信息及使用方法详情请见[worker](../harmonyos-references/js-apis-worker.md)。
* [序列化支持类型](../harmonyos-references/js-apis-worker.md#序列化支持类型)包括：

  1.除Symbol之外的基础类型、Date、String、RegExp、Array、Map、Set、ArrayBuffer、TypedArray。

  2.Object（仅限简单对象，比如通过"{}"或者"new Object"创建，普通对象仅支持传递属性，不支持传递其原型及方法）。

  **说明** 

  传递通过自定义class创建出来的Object时，不会发生序列化错误，但是自定义class的属性（如Function）无法通过序列化传递。

## 问题定位

根据报错信息可知对象序列化失败，检查imWorkStage.postMessage的参数类型是否是支持的类型以及序列化方式是否正确。

## 分析结论

imWorkStage.postMessage的参数类型为Object，此Object不会发生序列化错误，但是其对象的属性如data无法通过序列化传递。

## 修改建议

可将imWorkStage.postMessage的参数对象先转换成json字符串，再转换成Uint8Array类型。参考代码如下：

Worker.ets文件内容如下：

```ts
const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
  try {
    console.info("获取到的数据" + e.data);
    workerPort.postMessage(e.data);
  } catch (error) {
    console.error("获取数据失败" + e.data);
  }
};
```

Index.ets入口文件内容如下：

```ts
import { ErrorEvent, MessageEvents, util } from '@kit.ArkTS';
import { worker } from '@kit.ArkTS';

@Entry
@Component
export struct SocketManager {
  @State message:string="点击获取worker传输过来的数据";
  sendMessage(): void {
    const uint8Arr = new Uint8Array([0x12, 0x34, 0x56, 0x78]);
    let stringStr = JSON.stringify(new IMTask(1, uint8Arr, true));
    let textEncoder: util.TextEncoder = new util.TextEncoder();
    let uint8array: Uint8Array = textEncoder.encodeInto(stringStr);
    const byteArray = Array.from(uint8array);
    console.info("数据字节数=" + byteArray.length);
    let imWorkStage = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
    try {
      imWorkStage.postMessage(byteArray);
      // 宿主线程接收worker线程信息
      imWorkStage.onmessage = (e: MessageEvents): void => {
        // data：worker线程发送的信息
        let textDecoder = util.TextDecoder.create('utf-8');
        let uint8Array = new Uint8Array(e.data);
        let decodeResult:string = textDecoder.decodeToString(uint8Array);
        console.info("main thread data is  " + decodeResult);
        this.message=decodeResult;
        // 销毁Worker对象
        imWorkStage.terminate();
      };
      // 在调用terminate后，执行onexit
      imWorkStage.onexit = () => {
        console.info("main thread terminate");
      };
      // 监听Worker错误
      imWorkStage.onAllErrors = (err: ErrorEvent) => {
        console.error("main error message " + err.message);
      };
    } catch (error) {
      console.error(`uint8array: ${uint8array}`);
    }
  }

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.sendMessage();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

export class IMTask {
  cmdId: number;
  needAuth: boolean;
  data: Uint8Array;
  seq: number;

  constructor(cmdId: number, data: Uint8Array, needAuth?: boolean) {
    this.cmdId = cmdId;
    this.needAuth = needAuth ?? true;
    this.data = data;
    this.seq = 0;
  }
}
```

## 常见FAQ

Q：使用taskpool执行异步函数时，报函数参数无法序列化错误：

```txt
BusinessError: An exception occurred during serialization, taskpool: failed to serialize arguments.
```

A：请检查[序列化支持类型](../harmonyos-references/js-apis-worker.md#序列化支持类型)：

序列化支持的类型包括：除Symbol之外的基础类型、Date、String、RegExp、Array、Map、Set、Object（仅限简单对象，比如通过“{}”或者“new Object”创建，普通对象仅支持传递属性，不支持传递其原型及方法）、ArrayBuffer、TypedArray。
