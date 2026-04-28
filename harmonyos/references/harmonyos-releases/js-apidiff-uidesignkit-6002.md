---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-uidesignkit-6002
title: UI Design Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > API变更清单 > 6.0.0(20) Beta2引入的API > UI Design Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:32+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7a10c643d2ef4cc87b5f081c5e0b9c806acc4c9cb634023c353d3bb59cb8c54f
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 函数变更 | 类名：HdsTabsController；  API声明：bindScroller(value: number, scroller: Scroller): void;  差异内容：NA | 类名：HdsTabsController；  API声明：bindScroller(value: number, scroller: Scroller, parentScroller?: Scroller): void;  差异内容：parentScroller?: Scroller | api/@hms.hds.hdsBaseComponent.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：HdsTabsAttribute；  API声明：onTabBarClick(event: Callback<number>): HdsTabsAttribute;  差异内容：onTabBarClick(event: Callback<number>): HdsTabsAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：SnackBarStyleOptions；  API声明：pressBackCallback?: Callback<void>;  差异内容：pressBackCallback?: Callback<void>; | api/@hms.hds.HdsSnackBar.d.ets |
