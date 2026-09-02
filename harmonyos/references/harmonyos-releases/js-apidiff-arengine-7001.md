---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-arengine-7001
title: AR Engine
breadcrumb: 版本说明 > 最新版本(26.0.0) > 26.0.0 > OS平台能力 > API变更清单 > 26.0.0 Beta1引入的API > AR Engine
category: harmonyos-releases
scraped_at: 2026-09-02T14:49:04+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:e080b7dd70b45ee9b1d8a5f5340b38e4b6cdeadaecfdef3e6ffb2c55051d3559
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：arEngine；  API声明：enum ARRemoteSensorMode  差异内容：enum ARRemoteSensorMode | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARRemoteSensorMode；  API声明：LOCAL\_SENSOR = 0  差异内容：LOCAL\_SENSOR = 0 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARRemoteSensorMode；  API声明：REMOTE\_SENSOR\_AI\_GLASS = 1  差异内容：REMOTE\_SENSOR\_AI\_GLASS = 1 | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARFrame；  API声明：acquireCameraImage(): ARImage;  差异内容：acquireCameraImage(): ARImage; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARConfig；  API声明：remoteSensorMode?: ARRemoteSensorMode;  差异内容：remoteSensorMode?: ARRemoteSensorMode; | api/@hms.core.ar.arengine.d.ts |
| 新增API | NA | 类名：ARViewContext；  API声明：loadGSModel(resourcePath: spatialRender.GSImportSettings, location: arEngine.ARPose): Promise<number>;  差异内容：loadGSModel(resourcePath: spatialRender.GSImportSettings, location: arEngine.ARPose): Promise<number>; | api/@hms.core.ar.arview.d.ets |
| 新增API | NA | 类名：ARViewContext；  API声明：removeGSModel(modelID: number): Promise<boolean>;  差异内容：removeGSModel(modelID: number): Promise<boolean>; | api/@hms.core.ar.arview.d.ets |
