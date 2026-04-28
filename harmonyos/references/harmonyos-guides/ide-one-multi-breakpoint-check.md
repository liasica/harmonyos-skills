---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-one-multi-breakpoint-check
title: @cross-device-app-dev/one-multi-breakpoint-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/one-multi-breakpoint-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:23+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:f30df843c0ebab0959731a0ff3142806a2d82e85361a41c88ecfbcd3d6c9d9c1
---

一多特性必须使用系统断点判断是否开启，不能通过设备类型、设备方向或是否可折叠等属性来判断。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/one-multi-breakpoint-check": "warn"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Entry
2. @Component
3. struct ItemComponent {
4. private currentWidthBreakpoint: string = '';
5. build() {
6. // 必须使用断点进行判断
7. if (this.currentWidthBreakpoint === 'lg') {
8. }
9. }
10. }
```

## 反例

```
1. import { display } from '@kit.ArkUI';
2. import { deviceInfo } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct ItemComponent {
7. build() {
8. // 使用设备类型、是否可折叠等属性进行判断，告警
9. if (deviceInfo.deviceType === 'phone' && display.isFoldable()) {
10. }
11. }
12. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/recommended
2. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
