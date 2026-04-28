---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-access-mode
title: 宿主应用接入模式
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > 系统分享 > 宿主应用发起分享 > 宿主应用接入模式
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:045132786cc963e668463afacf238e3edbba220f1ca1fd21d556f78c13af6a9f
---

为应对开发者接入系统分享能力时的不同诉求，Share Kit支持两种宿主应用接入模式。

| 接入模式 | 接入方式&适用应用类型 | 效果图 |
| --- | --- | --- |
| 全接模式 | **直接使用系统分享面板**  适用于华为自研应用以及对分享方式区无商业诉求的开发者，可直接使用系统面板，降低开发成本。 | 直接使用系统分享面板 |
| 半接模式 | **开发者自行开发分享能力面板，并在分享面板中提供系统分享入口**  适用于分享方式区有商业诉求，或有自己独有的业务逻辑的开发者 | 左侧为自开发分享面板，同时提供系统分享入口，用户点击时调用系统分享面板 |

## 全接模式示例代码

[参考：手机应用发起系统分享开发步骤](share-mobilephone-app-share.md#开发步骤)

## 半接模式示例代码片段

说明

为了确保用户获得良好的分享体验，图标请使用HarmonyOS系统资源"$r('sys.symbol.share')"，文本使用"系统分享"，请勿自行更改。

```
1. // 分享图标使用系统提供的Symbol格式图标
2. SymbolGlyph($r('sys.symbol.share'))
3. // 文本使用'系统分享'
4. Text('系统分享')
```

完整示例代码请参见：[samplecode-接入模式](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/components/AccessModel.ets)。
