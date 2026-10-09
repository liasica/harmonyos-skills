---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-color-value
title: "@cross-device-app-dev/color-value"
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/color-value
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:32+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:eb25a0c9a8b3176a4ffcdd205d66dfebdaba52afdc0e00fe326e68bafbc6a60c
---

颜色值应当使用“$r”从color.json中引用，以适配不同的系统颜色模式，禁止使用固定的值。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@cross-device-app-dev/color-value": "warn"
  }
}
```

## 选项

该规则无需配置额外选项。

## 正例

```ts
@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      // 通过'sys.color.xxx'引用的颜色值，默认支持dark和light颜色模式
      Text()
        .fontColor($r('sys.color.ohos_id_color_activated'));
      // 通过'app.color.xxx'引用的颜色值，需要分别在dark和light颜色模式的color.json中配置
      Text()
        .fontColor($r('app.color.text_color'));
    }
  }
}
```

## 反例

```ts
@Entry
@Component
struct Index1 {
  build() {
    RelativeContainer() {
      Text('message').fontColor('#000000')
      Text('message').fontColor('rgb(0, 0, 0)')
      Text('message').fontColor(Color.Black)
    }
  }
}
```

## 规则集

```screen
plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-hmos-code-linter.md)。
