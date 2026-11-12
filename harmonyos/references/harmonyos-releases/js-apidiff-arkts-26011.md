---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-26011
title: ArkTS
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > ArkTS
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:3d9cd90ed27b410deb5925ffced4ad3fd86e53415dab2a9ef869f769e9ddd60e
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：json；  API声明：type ISendable = lang.ISendable;  差异内容：type ISendable = lang.ISendable; | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：json；  API声明：type SendableTransformer = (this: ISendable, key: string, value: ISendable | undefined | null) => ISendable | undefined | null;  差异内容：type SendableTransformer = (this: ISendable, key: string, value: ISendable | undefined | null) => ISendable | undefined | null; | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：ParseOptions；  API声明：parseReturnType?: ParseReturnType;  差异内容：parseReturnType?: ParseReturnType; | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：json；  API声明：function parseSendable(text: string, reviver?: SendableTransformer, options?: ParseOptions): ISendable | null;  差异内容：function parseSendable(text: string, reviver?: SendableTransformer, options?: ParseOptions): ISendable | null; | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：json；  API声明：const enum ParseReturnType  差异内容：const enum ParseReturnType | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：ParseReturnType；  API声明：OBJECT = 0  差异内容：OBJECT = 0 | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：ParseReturnType；  API声明：MAP = 1  差异内容：MAP = 1 | api/@ohos.util.json.d.ts |
| 新增API | NA | 类名：collections；  API声明：type ArrayElementPredicateFn<ElementType> = (value: ElementType) => boolean;  差异内容：type ArrayElementPredicateFn<ElementType> = (value: ElementType) => boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Array；  API声明：containsAll(elements: Array<T>): boolean;  差异内容：containsAll(elements: Array<T>): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Array；  API声明：containsAll(elements: readonly T[]): boolean;  差异内容：containsAll(elements: readonly T[]): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Array；  API声明：retainAll(elements: Array<T>): boolean;  差异内容：retainAll(elements: Array<T>): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Array；  API声明：retainAll(elements: readonly T[]): boolean;  差异内容：retainAll(elements: readonly T[]): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Array；  API声明：retainAll(predicate: ArrayElementPredicateFn<T>): boolean;  差异内容：retainAll(predicate: ArrayElementPredicateFn<T>): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Map；  API声明：containsValue(value: V): boolean;  差异内容：containsValue(value: V): boolean; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Map；  API声明：remove(key: K): V | undefined;  差异内容：remove(key: K): V | undefined; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Map；  API声明：put(key: K, value: V): V | undefined;  差异内容：put(key: K, value: V): V | undefined; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Map；  API声明：putAll(from: Map<K, V>): void;  差异内容：putAll(from: Map<K, V>): void; | arkts/@arkts.collections.d.ets |
| 新增API | NA | 类名：Map；  API声明：putAll(from: ReadonlyMap<K, V>): void;  差异内容：putAll(from: ReadonlyMap<K, V>): void; | arkts/@arkts.collections.d.ets |
