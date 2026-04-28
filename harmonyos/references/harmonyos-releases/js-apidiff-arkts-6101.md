---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-6101
title: ArkTS
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > ArkTS
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1bad6b3fc86f70b2fee4cca1bfe4f1d80a737d97acce1ce7c549a4c1d8edf99a
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 删除错误码 | 类名：Readable；  API声明：push(chunk: Uint8Array | string | null, encoding?: string): boolean;  差异内容：401 | 类名：Readable；  API声明：push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean;  差异内容：NA | api/@ohos.util.stream.d.ts |
| 函数变更 | 类名：Readable；  API声明：push(chunk: Uint8Array | string | null, encoding?: string): boolean;  差异内容：chunk: Uint8Array | string | null | 类名：Readable；  API声明：push(chunk: Uint8Array | string | undefined | null, encoding?: string): boolean;  差异内容：chunk: Uint8Array | string | undefined | null | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Blob；  API声明：get size(): number;  差异内容：get size(): number; | api/@ohos.buffer.d.ts |
| 新增API | NA | 类名：Blob；  API声明：get type(): string;  差异内容：get type(): string; | api/@ohos.buffer.d.ts |
| 新增API | NA | 类名：global；  API声明：export type ArrayListComparatorFn<T> = (firstValue: T, secondValue: T) => number;  差异内容：export type ArrayListComparatorFn<T> = (firstValue: T, secondValue: T) => number; | api/@ohos.util.ArrayList.d.ts |
| 新增API | NA | 类名：global；  API声明：export type ListComparatorFn<T> = (firstValue: T, secondValue: T) => number;  差异内容：export type ListComparatorFn<T> = (firstValue: T, secondValue: T) => number; | api/@ohos.util.List.d.ts |
| 新增API | NA | 类名：Writable；  API声明：get writableObjectMode(): boolean;  差异内容：get writableObjectMode(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Writable；  API声明：get writableHighWatermark(): number;  差异内容：get writableHighWatermark(): number; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Writable；  API声明：get writable(): boolean;  差异内容：get writable(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Writable；  API声明：get writableLength(): number;  差异内容：get writableLength(): number; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Writable；  API声明：get writableCorked(): number;  差异内容：get writableCorked(): number; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Writable；  API声明：get writableEnded(): boolean;  差异内容：get writableEnded(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Writable；  API声明：get writableFinished(): boolean;  差异内容：get writableFinished(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Readable；  API声明：get readableObjectMode(): boolean;  差异内容：get readableObjectMode(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Readable；  API声明：get readable(): boolean;  差异内容：get readable(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Readable；  API声明：get readableHighWatermark(): number;  差异内容：get readableHighWatermark(): number; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Readable；  API声明：get readableFlowing(): boolean | null;  差异内容：get readableFlowing(): boolean | null; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Readable；  API声明：get readableLength(): number;  差异内容：get readableLength(): number; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Readable；  API声明：get readableEncoding(): string | null;  差异内容：get readableEncoding(): string | null; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Readable；  API声明：get readableEnded(): boolean;  差异内容：get readableEnded(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Duplex；  API声明：get writableObjectMode(): boolean;  差异内容：get writableObjectMode(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Duplex；  API声明：get writableHighWatermark(): number;  差异内容：get writableHighWatermark(): number; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Duplex；  API声明：get writable(): boolean;  差异内容：get writable(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Duplex；  API声明：get writableLength(): number;  差异内容：get writableLength(): number; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Duplex；  API声明：get writableCorked(): number;  差异内容：get writableCorked(): number; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Duplex；  API声明：get writableEnded(): boolean;  差异内容：get writableEnded(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Duplex；  API声明：get writableFinished(): boolean;  差异内容：get writableFinished(): boolean; | api/@ohos.util.stream.d.ts |
| 新增API | NA | 类名：Decimal；  API声明：get e(): number;  差异内容：get e(): number; | arkts/@arkts.math.Decimal.d.ets |
| 新增API | NA | 类名：Decimal；  API声明：get s(): number;  差异内容：get s(): number; | arkts/@arkts.math.Decimal.d.ets |
| 新增API | NA | 类名：ConvertXML；  API声明：largeConvertToJSObject(xml: string, options?: ConvertOptions): Object;  差异内容：largeConvertToJSObject(xml: string, options?: ConvertOptions): Object; | api/@ohos.convertxml.d.ts |
| 新增API | NA | 类名：util；  API声明：class ArkTSVM  差异内容：class ArkTSVM | api/@ohos.util.d.ts |
| 新增API | NA | 类名：ArkTSVM；  API声明：static setMultithreadingDetectionEnabled(enabled: boolean): void;  差异内容：static setMultithreadingDetectionEnabled(enabled: boolean): void; | api/@ohos.util.d.ts |
| 删除API | 类名：Blob；  API声明：size: number;  差异内容：size: number; | NA | api/@ohos.buffer.d.ts |
| 删除API | 类名：Blob；  API声明：type: string;  差异内容：type: string; | NA | api/@ohos.buffer.d.ts |
| 删除API | 类名：Writable；  API声明：readonly writableObjectMode: boolean;  差异内容：readonly writableObjectMode: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Writable；  API声明：readonly writableHighWatermark: number;  差异内容：readonly writableHighWatermark: number; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Writable；  API声明：readonly writable: boolean;  差异内容：readonly writable: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Writable；  API声明：readonly writableLength: number;  差异内容：readonly writableLength: number; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Writable；  API声明：readonly writableCorked: number;  差异内容：readonly writableCorked: number; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Writable；  API声明：readonly writableEnded: boolean;  差异内容：readonly writableEnded: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Writable；  API声明：readonly writableFinished: boolean;  差异内容：readonly writableFinished: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Readable；  API声明：readonly readableObjectMode: boolean;  差异内容：readonly readableObjectMode: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Readable；  API声明：readonly readable: boolean;  差异内容：readonly readable: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Readable；  API声明：readonly readableHighWatermark: number;  差异内容：readonly readableHighWatermark: number; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Readable；  API声明：readonly readableFlowing: boolean | null;  差异内容：readonly readableFlowing: boolean | null; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Readable；  API声明：readonly readableLength: number;  差异内容：readonly readableLength: number; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Readable；  API声明：readonly readableEncoding: string | null;  差异内容：readonly readableEncoding: string | null; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Readable；  API声明：readonly readableEnded: boolean;  差异内容：readonly readableEnded: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Duplex；  API声明：readonly writableObjectMode: boolean;  差异内容：readonly writableObjectMode: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Duplex；  API声明：readonly writableHighWatermark: number;  差异内容：readonly writableHighWatermark: number; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Duplex；  API声明：readonly writable: boolean;  差异内容：readonly writable: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Duplex；  API声明：readonly writableLength: number;  差异内容：readonly writableLength: number; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Duplex；  API声明：readonly writableCorked: number;  差异内容：readonly writableCorked: number; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Duplex；  API声明：readonly writableEnded: boolean;  差异内容：readonly writableEnded: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Duplex；  API声明：readonly writableFinished: boolean;  差异内容：readonly writableFinished: boolean; | NA | api/@ohos.util.stream.d.ts |
| 删除API | 类名：Decimal；  API声明：readonly e: number;  差异内容：readonly e: number; | NA | arkts/@arkts.math.Decimal.d.ets |
| 删除API | 类名：Decimal；  API声明：readonly s: number;  差异内容：readonly s: number; | NA | arkts/@arkts.math.Decimal.d.ets |
| 函数变更 | 类名：ArrayList；  API声明：sort(comparator?: (firstValue: T, secondValue: T) => number): void;  差异内容：comparator?: (firstValue: T, secondValue: T) => number | 类名：ArrayList；  API声明：sort(comparator?: ArrayListComparatorFn<T>): void;  差异内容：comparator?: ArrayListComparatorFn<T> | api/@ohos.util.ArrayList.d.ts |
| 函数变更 | 类名：List；  API声明：sort(comparator: (firstValue: T, secondValue: T) => number): void;  差异内容：comparator: (firstValue: T, secondValue: T) => number | 类名：List；  API声明：sort(comparator: ListComparatorFn<T>): void;  差异内容：comparator: ListComparatorFn<T> | api/@ohos.util.List.d.ts |
