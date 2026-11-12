---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-rpcmessagesequencenotrelease
title: RpcMessageSequenceNotRelease
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Scanner代码检查规则 > ArkTS代码检查规则 > RpcMessageSequenceNotRelease
category: harmonyos-guides
scraped_at: 2026-11-12T09:53:00+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:597422321da2726fa6e1bb7d49d40e69309a50ffdf74d487a4a1035db08fe815
---

在RPC或IPC过程中，通过rpc.MessageSequence.create()创建的MessageSequence对象，使用完毕后，需及时调用reclaim()方法释放对象，避免内存泄漏。

## 规则配置

```json
// rules.json
{
  "rules": {
    "arkts": {
      "ResourceLeak": [
        {
          "ruleId": "RpcMessageSequenceNotRelease",
          "severity": "error",
          "skip": false
        }
      ]
    }
  }
}
```

## 正例

```ts
import rpc from '@ohos.rpc';

/**
 * 正例：正确释放资源
 */
@Component
export struct TestRelease {
    private rpcData: rpc.MessageSequence | null = null;
    aboutToAppear() {
        this.rpcData = rpc.MessageSequence.create();
    }
    build() {
        Text('Hello TestRelease')
    }
    aboutToDisappear() {
        this.rpcData?.reclaim();
    }
}
```

## 反例

```ts
import rpc from '@ohos.rpc';

/**
 * 反例：未释放资源
 */
@Component
export struct TestNotRelease {
    private rpcData: rpc.MessageSequence | null = null;
    aboutToAppear() {
        this.rpcData = rpc.MessageSequence.create(); // leak
    }
    build() {
        Text('Hello TestNotRelease')
    }
    aboutToDisappear() {
        console.log('Do nothing');
    }
}
```

Code Scanner代码检查规则的配置指导请参考[1.6.3 代码检查工具（codescanner）](ide-command-line-codescanner.md)
