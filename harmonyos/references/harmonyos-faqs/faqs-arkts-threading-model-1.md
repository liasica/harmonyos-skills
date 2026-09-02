---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-1
title: 异步并发导致首次更新数据失败
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 异步并发导致首次更新数据失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7b8cbf5b5398bc3d3125a79afab312b8eb4dd54f22261eaab5e2874ea08e1938
---

## 问题现象

用户在应用中首次登录后，选择修改某些信息。当用户填写完相关信息，点击保存时，应用提示保存失败。但是当用户第二次点击保存时，成功完成数据修改。

## 背景知识

[异步并发 (Promise和async/await)](../harmonyos-guides/async-concurrency-overview.md)：Promise和async/await提供异步并发能力，是标准的JS异步语法。异步代码会被挂起并在之后继续执行，同一时间只有一段代码执行。

## 问题定位

根据HiLog日志进行问题分析：在日志中检索关键字：NETSTACK，有如下日志信息。

```txt
07-03 17:20:03.805   28900-29242   C015B0/com.hm.example/NETSTACK  com.hm.example  I     [http_exec.cpp:418] taskid=-2147483635, size:781, dns:0.352, connect:47.293, tls:0.000, firstSend:0.390, firstRecv:52.573, total:100.656, redirect:0.000, errCode:0, RespCode:404, httpVer:2, method:GET, osErr:0
07-03 17:20:03.806   28900-28900   A03D00/com.hm.example/JSAPP     com.hm.example  I     Unexpected Text in JSON
07-03 17:20:03.839   28900-29242   C015B0/com.hm.example/NETSTACK  com.hm.example  I     [http_exec.cpp:418] taskid=-2147483632, size:3887, dns:0.075, connect:0.000, tls:0.000, firstSend:0.353, firstRecv:58.576, total:59.184, redirect:0.000, errCode:0, RespCode:200, httpVer:2, method:GET, osErr:0
07-03 17:20:03.843   28900-29242   C015B0/com.hm.example/NETSTACK  com.hm.example  I     [http_exec.cpp:418] taskid=-2147483633, size:194, dns:0.070, connect:0.000, tls:0.000, firstSend:0.251, firstRecv:88.041, total:88.400, redirect:0.000, errCode:0, RespCode:200, httpVer:2, method:POST, osErr:0
```

根据日志中http\_exec，可以看到第一次更新调用了一次网络请求，第二次更新则调用了两次网络请求。且，第一次更新网络请求后，随后出现Unexpected Text in JSON的异常信息。说明第一次网络请求时，从服务端请求的数据为空或某些属性为空，导致解析json出错。而第二次则不存在这个问题，第二次网络请求的数据是正常的。

## 分析结论

应用在更新数据的时候，使用异步模式连续请求了两次网络。分别是更新数据和获取数据。由于两次请求之间没有安排好请求顺序，更新数据在获取数据之后，导致实际请求到的数据是更新前的数据，从而导致数据解析失败。

## 修改建议

* 可以在服务端进行接口整合，在更新数据的同时，直接返回更新后的数据，从而可以减少网络交互的次数，提升性能。
* 使用Promise和async/await提供异步并发能力，合理调度网络请求的先后顺序。例如，获取更新后的数据在更新操作之后。如下使用Promise的示例：

  ```ts
  promise.then(() => {
    // 获取数据...
  }, (error: Error) => {
    console.error(error.message); // 失败时执行
  });
  ```

  如下使用async的示例：

  ```ts
  async function myAsyncFunction(): Promise<string> {
    const result: string = await new Promise(() => {
      setTimeout(() => {
        // 获取数据...
      }, 3000);
    });
    console.info(result);
    return result;
  }
  ```

完整的示例如下：

```ts
async function myAsyncFunction(): Promise<string> {
  const result: string = await new Promise(() => {
    setTimeout(() => {
      // 获取数据...
    }, 3000);
  });
  console.info(result);
  return result;
}

@Entry
@Component
struct S2CFK20250703174604963316 {
  message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(async () => {
            let res = await myAsyncFunction();
            console.info(`res is: ${res}`);

            const promise: Promise<number> = new Promise((resolve: Function, reject: Function) => {
              setTimeout(() => {
                const randomNumber: number = 1;
                if (randomNumber > 0.5) {
                  resolve(randomNumber);
                } else {
                  reject(new Error('Random number is too small'));
                }
              }, 1000);
            });

            // 使用 then 方法定义成功和失败的回调
            promise.then(() => {
              // 获取数据...
            }, (error: Error) => {
              console.error(error.message); // 失败时执行
            });
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
