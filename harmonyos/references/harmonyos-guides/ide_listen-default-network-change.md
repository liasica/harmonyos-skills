---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_listen-default-network-change
title: "@correctness/listen-default-network-change"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 正确性规则@correctness > @correctness/listen-default-network-change
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8ae003805c45dc17dd32402b4a910199b1eff07cdeec852d638fe9119bfdac11
---

建议应用监听默认网络的变化，关闭原有网络的数据传输，并使用新网络建立数据传输。

该规则仅在联网类应用检查整个工程时才生效。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@correctness/listen-default-network-change": "suggestion"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
// With the ohos.permission.GET_NETWORK_INFO permission configured
import connection from '@ohos.net.connection';
export function test() {
  const defaultNet = connection.getDefaultNetSync();
  const netCapabilities = connection.getNetCapabilitiesSync(defaultNet);
  let bearerTypes = netCapabilities.bearerTypes;
  const netConnection = connection.createNetConnection();
  netConnection.on('netCapabilitiesChange', (netCap: connection.NetCapabilityInfo) => {
    const newBearTypes = netCap.netCap.bearerTypes;
    if (newBearTypes !== bearerTypes) {
      bearerTypes = newBearTypes;
    }
  });
}
```

## 反例

```screen
// With the ohos.permission.GET_NETWORK_INFO permission configured
// import connection from '@ohos.net.connection';
// The `on(type: 'netCapabilitiesChange', callback: Callback<connection.NetCapabilityInfo>)`, `getDefaultNet`/`getDefaultNetSync` and `getNetCapabilities`/`getNetCapabilitiesSync` functions are not called.
```

## 规则集

```screen
plugin:@correctness/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
