---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arkts-6001
title: ArkTS
category: harmonyos-releases
scraped_at: 2026-04-28T07:34:35+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:54503f0acd6081ed4d58fb39c56757b4f4c1682deca8ce2597583f601abd2b95
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：global；  API声明：declare namespace fastbuffer  差异内容：declare namespace fastbuffer | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：type BufferEncoding = 'ascii' | 'utf8' | 'utf-8' | 'utf16le' | 'ucs2' | 'ucs-2' | 'base64' | 'base64url' | 'latin1' | 'binary' | 'hex';  差异内容：type BufferEncoding = 'ascii' | 'utf8' | 'utf-8' | 'utf16le' | 'ucs2' | 'ucs-2' | 'base64' | 'base64url' | 'latin1' | 'binary' | 'hex'; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：interface TypedArray  差异内容：interface TypedArray | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer;  差异内容：function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function allocUninitializedFromPool(size: number): FastBuffer;  差异内容：function allocUninitializedFromPool(size: number): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function allocUninitialized(size: number): FastBuffer;  差异内容：function allocUninitialized(size: number): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function byteLength(value: string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number;  差异内容：function byteLength(value: string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer;  差异内容：function concat(list: FastBuffer[] | Uint8Array[], totalLength?: number): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function from(array: number[]): FastBuffer;  差异内容：function from(array: number[]): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): FastBuffer;  差异内容：function from(arrayBuffer: ArrayBuffer | SharedArrayBuffer, byteOffset?: number, length?: number): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function from(buffer: FastBuffer | Uint8Array): FastBuffer;  差异内容：function from(buffer: FastBuffer | Uint8Array): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function from(value: string, encoding?: BufferEncoding): FastBuffer;  差异内容：function from(value: string, encoding?: BufferEncoding): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function isBuffer(obj: Object): boolean;  差异内容：function isBuffer(obj: Object): boolean; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function isEncoding(encoding: string): boolean;  差异内容：function isEncoding(encoding: string): boolean; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function compare(buf1: FastBuffer | Uint8Array, buf2: FastBuffer | Uint8Array): -1 | 0 | 1;  差异内容：function compare(buf1: FastBuffer | Uint8Array, buf2: FastBuffer | Uint8Array): -1 | 0 | 1; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：function transcode(source: FastBuffer | Uint8Array, fromEnc: string, toEnc: string): FastBuffer;  差异内容：function transcode(source: FastBuffer | Uint8Array, fromEnc: string, toEnc: string): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：fastbuffer；  API声明：class FastBuffer  差异内容：class FastBuffer | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：length: number;  差异内容：length: number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：buffer: ArrayBuffer;  差异内容：buffer: ArrayBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：byteOffset: number;  差异内容：byteOffset: number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：fill(value: string | FastBuffer | Uint8Array | number, offset?: number, end?: number, encoding?: BufferEncoding): FastBuffer;  差异内容：fill(value: string | FastBuffer | Uint8Array | number, offset?: number, end?: number, encoding?: BufferEncoding): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：compare(target: FastBuffer | Uint8Array, targetStart?: number, targetEnd?: number, sourceStart?: number, sourceEnd?: number): -1 | 0 | 1;  差异内容：compare(target: FastBuffer | Uint8Array, targetStart?: number, targetEnd?: number, sourceStart?: number, sourceEnd?: number): -1 | 0 | 1; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：copy(target: FastBuffer | Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number;  差异内容：copy(target: FastBuffer | Uint8Array, targetStart?: number, sourceStart?: number, sourceEnd?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：equals(otherBuffer: Uint8Array | FastBuffer): boolean;  差异内容：equals(otherBuffer: Uint8Array | FastBuffer): boolean; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：includes(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean;  差异内容：includes(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): boolean; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：indexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number;  差异内容：indexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：keys(): IterableIterator<number>;  差异内容：keys(): IterableIterator<number>; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：values(): IterableIterator<number>;  差异内容：values(): IterableIterator<number>; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：entries(): IterableIterator<[  number,  number  ]>;  差异内容：entries(): IterableIterator<[  number,  number  ]>; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：lastIndexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number;  差异内容：lastIndexOf(value: string | number | FastBuffer | Uint8Array, byteOffset?: number, encoding?: BufferEncoding): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readBigInt64BE(offset?: number): bigint;  差异内容：readBigInt64BE(offset?: number): bigint; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readBigInt64LE(offset?: number): bigint;  差异内容：readBigInt64LE(offset?: number): bigint; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readBigUInt64BE(offset?: number): bigint;  差异内容：readBigUInt64BE(offset?: number): bigint; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readBigUInt64LE(offset?: number): bigint;  差异内容：readBigUInt64LE(offset?: number): bigint; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readDoubleBE(offset?: number): number;  差异内容：readDoubleBE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readDoubleLE(offset?: number): number;  差异内容：readDoubleLE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readFloatBE(offset?: number): number;  差异内容：readFloatBE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readFloatLE(offset?: number): number;  差异内容：readFloatLE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readInt8(offset?: number): number;  差异内容：readInt8(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readInt16BE(offset?: number): number;  差异内容：readInt16BE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readInt16LE(offset?: number): number;  差异内容：readInt16LE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readInt32BE(offset?: number): number;  差异内容：readInt32BE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readInt32LE(offset?: number): number;  差异内容：readInt32LE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readIntBE(offset: number, byteLength: number): number;  差异内容：readIntBE(offset: number, byteLength: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readIntLE(offset: number, byteLength: number): number;  差异内容：readIntLE(offset: number, byteLength: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readUInt8(offset?: number): number;  差异内容：readUInt8(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readUInt16BE(offset?: number): number;  差异内容：readUInt16BE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readUInt16LE(offset?: number): number;  差异内容：readUInt16LE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readUInt32BE(offset?: number): number;  差异内容：readUInt32BE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readUInt32LE(offset?: number): number;  差异内容：readUInt32LE(offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readUIntBE(offset: number, byteLength: number): number;  差异内容：readUIntBE(offset: number, byteLength: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：readUIntLE(offset: number, byteLength: number): number;  差异内容：readUIntLE(offset: number, byteLength: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：subarray(start?: number, end?: number): FastBuffer;  差异内容：subarray(start?: number, end?: number): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：swap16(): FastBuffer;  差异内容：swap16(): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：swap32(): FastBuffer;  差异内容：swap32(): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：swap64(): FastBuffer;  差异内容：swap64(): FastBuffer; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：toJSON(): Object;  差异内容：toJSON(): Object; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：toString(encoding?: string, start?: number, end?: number): string;  差异内容：toString(encoding?: string, start?: number, end?: number): string; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：write(str: string, offset?: number, length?: number, encoding?: string): number;  差异内容：write(str: string, offset?: number, length?: number, encoding?: string): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeBigInt64BE(value: bigint, offset?: number): number;  差异内容：writeBigInt64BE(value: bigint, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeBigInt64LE(value: bigint, offset?: number): number;  差异内容：writeBigInt64LE(value: bigint, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeBigUInt64BE(value: bigint, offset?: number): number;  差异内容：writeBigUInt64BE(value: bigint, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeBigUInt64LE(value: bigint, offset?: number): number;  差异内容：writeBigUInt64LE(value: bigint, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeDoubleBE(value: number, offset?: number): number;  差异内容：writeDoubleBE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeDoubleLE(value: number, offset?: number): number;  差异内容：writeDoubleLE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeFloatBE(value: number, offset?: number): number;  差异内容：writeFloatBE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeFloatLE(value: number, offset?: number): number;  差异内容：writeFloatLE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeInt8(value: number, offset?: number): number;  差异内容：writeInt8(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeInt16BE(value: number, offset?: number): number;  差异内容：writeInt16BE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeInt16LE(value: number, offset?: number): number;  差异内容：writeInt16LE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeInt32BE(value: number, offset?: number): number;  差异内容：writeInt32BE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeInt32LE(value: number, offset?: number): number;  差异内容：writeInt32LE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeIntBE(value: number, offset: number, byteLength: number): number;  差异内容：writeIntBE(value: number, offset: number, byteLength: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeIntLE(value: number, offset: number, byteLength: number): number;  差异内容：writeIntLE(value: number, offset: number, byteLength: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeUInt8(value: number, offset?: number): number;  差异内容：writeUInt8(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeUInt16BE(value: number, offset?: number): number;  差异内容：writeUInt16BE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeUInt16LE(value: number, offset?: number): number;  差异内容：writeUInt16LE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeUInt32BE(value: number, offset?: number): number;  差异内容：writeUInt32BE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeUInt32LE(value: number, offset?: number): number;  差异内容：writeUInt32LE(value: number, offset?: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeUIntBE(value: number, offset: number, byteLength: number): number;  差异内容：writeUIntBE(value: number, offset: number, byteLength: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：FastBuffer；  API声明：writeUIntLE(value: number, offset: number, byteLength: number): number;  差异内容：writeUIntLE(value: number, offset: number, byteLength: number): number; | api/@ohos.fastbuffer.d.ts |
| 新增API | NA | 类名：taskpool；  API声明：interface TaskResult  差异内容：interface TaskResult | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：TaskResult；  API声明：result?: Object;  差异内容：result?: Object; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：TaskResult；  API声明：error?: Error | Object;  差异内容：error?: Error | Object; | api/@ohos.taskpool.d.ts |
| 新增API | NA | 类名：util；  API声明：function getMainThreadStackTrace(): string;  差异内容：function getMainThreadStackTrace(): string; | api/@ohos.util.d.ts |
| 新增API | NA | 类名：xml；  API声明：class XmlDynamicSerializer  差异内容：class XmlDynamicSerializer | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：setAttributes(name: string, value: string): void;  差异内容：setAttributes(name: string, value: string): void; | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：addEmptyElement(name: string): void;  差异内容：addEmptyElement(name: string): void; | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：setDeclaration(): void;  差异内容：setDeclaration(): void; | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：startElement(name: string): void;  差异内容：startElement(name: string): void; | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：endElement(): void;  差异内容：endElement(): void; | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：setNamespace(prefix: string, namespace: string): void;  差异内容：setNamespace(prefix: string, namespace: string): void; | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：setComment(text: string): void;  差异内容：setComment(text: string): void; | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：setCdata(text: string): void;  差异内容：setCdata(text: string): void; | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：setText(text: string): void;  差异内容：setText(text: string): void; | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：setDocType(text: string): void;  差异内容：setDocType(text: string): void; | api/@ohos.xml.d.ts |
| 新增API | NA | 类名：XmlDynamicSerializer；  API声明：getOutput(): ArrayBuffer;  差异内容：getOutput(): ArrayBuffer; | api/@ohos.xml.d.ts |
| 新增kit | 类名：global；  API声明：  差异内容：NA | 类名：global；  API声明：api@ohos.fastbuffer.d.ts  差异内容：ArkTS | api/@ohos.fastbuffer.d.ts |
