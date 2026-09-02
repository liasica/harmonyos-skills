---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_listen-multi-network-concurrent
title: "@correctness/listen-multi-network-concurrent"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/listen-multi-network-concurrent
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:afbc6c698c220bae309ff42fc1c3c70a0eed4db0accc5035410448da7ad3f2ba
---

建议应用订阅连接迁移通知，可在WiFi/蜂窝连接切换前后获取切换状态通知。

该规则仅在联网类应用检查整个工程时才生效。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/listen-multi-network-concurrent": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// With the ohos.permission.GET_NETWORK_INFO permission configured
import { netHandover } from '@kit.NetworkBoostKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  netHandover.on('handoverChange', (info: netHandover.HandoverInfo) => {
    if (info.handoverStart) {
      console.info('handover start');
    } else if (info.handoverComplete) {
      console.info('handover complete');
    }
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
try {
  netHandover.off('handoverChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## 反例

```screen
// With the ohos.permission.GET_NETWORK_INFO permission configured
// The `on(type: 'handoverChange', callback: Callback<HandoverInfo>)` function is not called.
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
