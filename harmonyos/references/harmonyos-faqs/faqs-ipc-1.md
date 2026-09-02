---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ipc-1
title: IPC跨进程通信中是否支持异步返回数据
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 进程间通信（IPC） > IPC跨进程通信中是否支持异步返回数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:999ce76d5a388d40507e631dea6fa7c5cf46b18aaa9142a2d80aa8048c4f00b5
---

支持将服务端的onRemoteMessageRequest函数使用async设置为异步。具体可以参考：API参考[onRemoteMessageRequest](../harmonyos-references/js-apis-rpc.md#onremotemessagerequest9)中的“重载onRemoteMessageRequest方法异步处理请求示例”。

参考代码如下：

```typescript
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

**参考链接**

[IPC与RPC通信开发指导](../harmonyos-guides/ipc-rpc-development-guideline.md)
