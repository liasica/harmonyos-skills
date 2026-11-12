---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-imagekit-26011
title: Image Kit
breadcrumb: 版本说明 > 最新版本(26.0.1) > 26.0.1 > OS平台能力 > API变更清单 > Image Kit
category: harmonyos-releases
scraped_at: 2026-11-12T09:49:53+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:cd78e119d6557dcfa752b3c5dcd0b9c473ced7c44a4fd1ef39d29fa0af9f976c
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：AuxiliaryPicture；  API声明：acquirePixelmap(): PixelMap | null;  差异内容：acquirePixelmap(): PixelMap | null; | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureType；  API声明：OXY\_MAP = 11  差异内容：OXY\_MAP = 11 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：AuxiliaryPictureType；  API声明：MEL\_MAP = 12  差异内容：MEL\_MAP = 12 | api/@ohos.multimedia.image.d.ts |
| 新增API | NA | 类名：ImageReceiver；  API声明：setMemoryName(name: string): void;  差异内容：setMemoryName(name: string): void; | api/@ohos.multimedia.image.d.ts |
| API从不支持元服务到支持元服务 | 类名：ImageSource；  API声明：release(callback: AsyncCallback<void>): void;  差异内容：NA | 类名：ImageSource；  API声明：release(callback: AsyncCallback<void>): void;  差异内容：atomicservice | api/@ohos.multimedia.image.d.ts |
| API从不支持元服务到支持元服务 | 类名：ImageSource；  API声明：release(): Promise<void>;  差异内容：NA | 类名：ImageSource；  API声明：release(): Promise<void>;  差异内容：atomicservice | api/@ohos.multimedia.image.d.ts |
