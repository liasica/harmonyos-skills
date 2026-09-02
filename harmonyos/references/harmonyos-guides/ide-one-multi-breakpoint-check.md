---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-one-multi-breakpoint-check
title: "@cross-device-app-dev/one-multi-breakpoint-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/one-multi-breakpoint-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3c8f8ca312c39a4e7b533990435e2faacf7a0cdc2238949522e2ef4ad8d65fb5
---

一多特性必须使用系统断点判断是否开启，不能通过设备类型、设备方向或是否可折叠等属性来判断。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/one-multi-breakpoint-check": "warn"
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
@Entry
@Component
struct ItemComponent {
  private currentWidthBreakpoint: string = '';
  build() {
    // 必须使用断点进行判断
    if (this.currentWidthBreakpoint === 'lg') {
    }
  }
}
```

## 反例

```screen
import { display } from '@kit.ArkUI';
import { deviceInfo } from '@kit.BasicServicesKit';

@Entry
@Component
struct ItemComponent {
  build() {
    // 使用设备类型、是否可折叠等属性进行判断，告警
    if (deviceInfo.deviceType === 'phone' && display.isFoldable()) {
    }
  }
}
```

## 规则集

```screen
plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
