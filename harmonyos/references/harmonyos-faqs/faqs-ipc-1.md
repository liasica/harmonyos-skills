---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ipc-1
title: IPC跨进程通信中是否支持异步返回数据
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 进程间通信（IPC） > IPC跨进程通信中是否支持异步返回数据
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:55+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a478a03c1a443c05d55e708fe6bb2ad74cf6b7be093a3f810de2b68426d0abcf
---

支持将服务端的onRemoteMessageRequest函数使用async设置为异步。具体可以参考：API参考[onRemoteMessageRequest](../harmonyos-references/js-apis-rpc.md#onremotemessagerequest9)中的“重载onRemoteMessageRequest方法异步处理请求示例”。

参考代码如下：

```
1. import { rpc } from '@kit.IPCKit';

3. class TestRemoteObject extends rpc.RemoteObject {
4. constructor(descriptor: string) {
5. super(descriptor);
6. }

8. async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption): Promise<boolean> {
9. if (code === 1) {
10. console.log("RpcServer: async onRemoteMessageRequest is called");
11. } else {
12. console.log("RpcServer: unknown code: " + code);
13. return false;
14. }
15. await new Promise((resolve: (data: rpc.RequestResult) => void) => {
16. setTimeout(resolve, 100);
17. })
18. return true;
19. }
20. }
```

[TestRemoteObject.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ipc/entry/src/main/ets/pages/TestRemoteObject.ets#L21-L40)

**参考链接**

[IPC与RPC通信开发指导](../harmonyos-guides/ipc-rpc-development-guideline.md)
