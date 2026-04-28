---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-uidesignkit-6011
title: UI Design Kit
breadcrumb: 版本说明 > HarmonyOS 6.0.1(21) > OS平台能力 > API变更清单 > 6.0.1(21) Beta1引入的API > UI Design Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:03+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:27251a36a3ff78f4a8129e586bb6a7bacb2857e7b2e732781dcbef2aa0f6817b
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：HdsListItem；  API声明：listItemModifier?: ListItemModifier;  差异内容：listItemModifier?: ListItemModifier; | api/@hms.hds.HdsStyle.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：HdsNavDestinationAttribute；  API声明：onActive(callback: Optional<Callback<NavDestinationActiveReason>>): HdsNavDestinationAttribute;  差异内容：onActive(callback: Optional<Callback<NavDestinationActiveReason>>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 类新增必选属性或非同名方法 | 类名：global；  API声明：  差异内容：NA | 类名：HdsNavDestinationAttribute；  API声明：onInactive(callback: Optional<Callback<NavDestinationActiveReason>>): HdsNavDestinationAttribute;  差异内容：onInactive(callback: Optional<Callback<NavDestinationActiveReason>>): HdsNavDestinationAttribute; | api/@hms.hds.hdsBaseComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：HdsNavigationTitle；  API声明：subTitleComponent?: ComponentContent;  差异内容：subTitleComponent?: ComponentContent; | api/@hms.hds.hdsBaseComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：BottomBuilderParams；  API声明：builderComponent?: ComponentContent;  差异内容：builderComponent?: ComponentContent; | api/@hms.hds.hdsBaseComponent.d.ets |
| 接口新增可选属性 | 类名：global；  API声明：  差异内容：NA | 类名：TitleBarContentOptions；  API声明：stackBuilderComponent?: ComponentContent;  差异内容：stackBuilderComponent?: ComponentContent; | api/@hms.hds.hdsBaseComponent.d.ets |
