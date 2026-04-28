---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-pushkit-510
title: Push Kit
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.1.0(18) > OS平台能力 > API变更清单 > Push Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:35:13+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4191c4633e333f964721539e23b5398b20d4e3b93cf2dc1f167178bba42ec568
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：pushService；  API声明：function on(type: 'tokenUpdate', ability: Ability, callback: Callback<string>): void;  差异内容：function on(type: 'tokenUpdate', ability: Ability, callback: Callback<string>): void; | api/@hms.core.push.pushService.d.ts |
| 新增API | NA | 类名：pushService；  API声明：function off(type: 'tokenUpdate', callback?: Callback<string>): void;  差异内容：function off(type: 'tokenUpdate', callback?: Callback<string>): void; | api/@hms.core.push.pushService.d.ts |
