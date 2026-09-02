---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkui-6112
title: ArkUI
breadcrumb: 版本说明 > 更多版本 > 6.1.1(24) > OS平台能力 > API变更清单 > 6.1.1(24) Release引入的API > ArkUI
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:07+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:5901486d9a094455eb2a04ade09acb4d59241bc61b87774caff70de0b057cd62
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| API废弃版本变更 | 类名：CrownAction；  API声明：BEGIN = 0  差异内容：24 dynamic | 类名：CrownAction；  API声明：BEGIN = 0  差异内容：24 | component/enums.d.ts |
| 新增API | NA | 类名：global；  API声明：declare interface CachedCountOptions  差异内容：declare interface CachedCountOptions | component/swiper.d.ts |
| 新增API | NA | 类名：CachedCountOptions；  API声明：isShown?: boolean;  差异内容：isShown?: boolean; | component/swiper.d.ts |
| 新增API | NA | 类名：CachedCountOptions；  API声明：independent?: boolean;  差异内容：independent?: boolean; | component/swiper.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围不是包含关系 | 类名：SwiperAttribute；  API声明：cachedCount(count: number, isShown: boolean): SwiperAttribute;  差异内容：cachedCount(count: number, isShown: boolean): SwiperAttribute; | 类名：SwiperAttribute；  API声明：cachedCount(count: number, options: CachedCountOptions): SwiperAttribute;  差异内容：cachedCount(count: number, options: CachedCountOptions): SwiperAttribute; | component/swiper.d.ts |
