---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ipc-kit-faq-0001
title: IPC跨进程异步返回数据
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 进程间通信（IPC） > 常见问题 > IPC跨进程异步返回数据
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:27+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:3e2a9bf79c5dc9e93de5fd2bb0e8243d8beb9ec0cc6dbaada7a81ea0779fa483
---

**Q：IPC跨进程通信中是否支持异步返回数据？**

**A**：支持将服务端的onRemoteMessageRequest函数使用async设置为异步。具体可以参考：API参考[onRemoteMessageRequest](../harmonyos-references/js-apis-rpc.md#onremotemessagerequest9)中的“重载onRemoteMessageRequest方法异步处理请求示例”。

参考代码如下：

```ts
import { rpc } from '@kit.IPCKit';

class TestRemoteObject extends rpc.RemoteObject {
  constructor(descriptor: string) {
    super(descriptor);
  }

  async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption): Promise<boolean> {
    if (code === 1) {
      console.log("RpcServer: async onRemoteMessageRequest is called");
    } else {
      console.log("RpcServer: unknown code: " + code);
      return false;
    }
    await new Promise((resolve: (data: rpc.RequestResult) => void) => {
      setTimeout(resolve, 100);
    })
    return true;
  }
}
```

参考链接：[IPC与RPC通信开发指导](../harmonyos-guides/ipc-rpc-development-guideline.md)。
