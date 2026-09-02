---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-4
title: rcp请求未正常执行且catch未捕获异常
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > rcp请求未正常执行且catch未捕获异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:485e2c8a2ae187723d29f0f582851cd0e8fb6cb9331a71feed166f79d3ab1a0b
---

## 问题现象

通过rcp访问指定链接，未发现自定义日志打印，catch未捕获异常，程序也未能正常访问链接。

问题代码示例参考如下：

```screen
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 1.定义请求地址
const getAccessTokenUrl = 'https：123123123123';

// 2.创建会话
const session = rcp.createSession();

// 3.构建请求参数对象
interface GeneratedObjectLiteralInterface_1 {
  clientID: string;
  clientSecret: string;
}

const request: GeneratedObjectLiteralInterface_1 = {
  clientID: '123456789',
  clientSecret: '123456789'
};

// 4.发起POST请求获取Access Token
session.post(getAccessTokenUrl, JSON.stringify(request))
  .then((response) => {
    console.info(`请求成功，响应内容: ${response}`);
    // 可选：解析JSON响应
    try {
      const data = JSON.stringify(response);
      console.info(`解析后的 Token 数据:`, data);
    } catch (e) {
      console.warn(`响应内容无法解析为 JSON`);
    }
  })
  .catch((error: BusinessError) => {
    console.error(`请求失败，错误码: ${error.code}, 消息: ${error.message}`);
  });
```

## 背景知识

[rcp](../harmonyos-references/remote-communication-rcp.md)访问网络，通过回调获取结果，并使用[Console](../harmonyos-references/js-apis-logs.md) 输出相关内容到控制台。

其中[Promise](../harmonyos-guides/async-concurrency-overview.md#promise)提供了then、catch、finally方法来注册回调函数，以处理异步操作的成功或失败结果，但是，若调用本身存在问题，不能执行接口，则无法执行回调。

## 问题定位

上述场景中对post回调结果以及异常进行捕获，但并未捕获post本身的使用异常。

## 分析结论

需要对post语句本身使用try-catch进行异常捕获，并根据相应信息处理问题。

## 修改建议

使用try-catch捕获post异常，并根据错误码处理。

```screen
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Transform {
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('POST请求')
        .onClick(() => {
          try {
            // 定义请求地址，使用时请变更为所需地址
            const getAccessTokenUrl = 'https：123123123123';
            // 创建会话
            const session = rcp.createSession();
            // 发起POST请求获取Access Token
            session.post(getAccessTokenUrl)
              .then((response) => {
                console.info(`Succeeded in getting the response ${response}`);
              })
              .catch((error: BusinessError) => {
                console.error(`Failed in getting the response, error code: ${error.code}, error message: ${error.message}`);
              });
          } catch (error) {
            console.error(`Failed in coding, error code: ${error.code}, error data:${error.data}, error message: ${error.message}`);
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

常见错误码及处理方式如下：

* 场景一：
  + 错误信息：

    code：[201](../harmonyos-references/errorcode-universal.md)，data：Permission Denied。
  + 信息分析：

    信息为权限申请失败，通过post接口可知，post需要权限：ohos.permission.INTERNET(如果使用PathPreference的'cellular'模式，则额外需要ohos.permission.GET\_NETWORK\_INFO)
  + 处理方案：在module.json5中配置ohos.permission.INTERNET权限信息。
* 场景二：
  + 错误信息：

    code：[10200002](../harmonyos-references/errorcode-utils.md#section10200002-参数解析错误)，message：Syntax Error. Invalid Url string。
  + 信息分析：

    信息为入参错误，无效的Url链接，可以检查传入的Url参数或者直接使用HarmonyOS浏览器访问，确认Url是否可用。
  + 处理方案：

    传入正确格式的链接。

## 常见FAQ

Q：使用rcp请求服务端接口时返回400 Bad Request响应状态码？

A：该响应码通常是提交数据的字段名称或者是字段类型和后台的实体类不一致，或者提交的数据格式与服务端接口的数据格式不一致。请对照字段名称，类型保证一致性，保证请求的数据格式的正确性。

Q：使用rcp下载文件报错，报错信息{"code":1007900028,"data":"Timeout was reached"}？

A：可以尝试增大[timeout](../harmonyos-references/remote-communication-rcp.md#timeout)的时间。

Q：可以使用哪些API实现post类型的长连接？例如聊天场景。

A：可以使用[rcp](../harmonyos-references/remote-communication-rcp.md)和[@ohos.net.http](../harmonyos-references/js-apis-http.md)，在请求头中添加：Connection: keep-alive。

Q：rcp网络请求想要实现防止重复请求，除了防抖和节流，有没有更好的实现方式？

A：为避免网络重复请求可以考虑如下方案措施：

1. 客户端及服务端设置请求超时时间，如果在规定时间内没有收到响应，则认为请求失败避免重复发送请求。
2. 发送请求头中使用唯一标识避免重复请求。
3. 请求中设置缓存技术，避免重复请求相同的数据。

## 总结

若某段代码执行不符合预期，可以用try-catch捕获其中的异常信息，或者使用断点调试的方案，查看预期执行逻辑停止位置，然后具体分析。
