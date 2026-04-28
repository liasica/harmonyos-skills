---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/js-apidiff-mapkit-6101
title: Map Kit
breadcrumb: 版本说明 > HarmonyOS 6.1.0(23) > OS平台能力 > API变更清单 > 6.1.0(23) Beta1引入的变更 > Map Kit
category: harmonyos-releases
scraped_at: 2026-04-28T07:33:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ff7619a268d4ce8fcc0c83d4252a0cbb4ca20281751ac9c63f7d6d549d5fd207
---

| 操作 | 旧版本 | 新版本 | d.ts文件 |
| --- | --- | --- | --- |
| 新增API | NA | 类名：MapComponentController；  API声明：isApproveNumberEnabled(): boolean;  差异内容：isApproveNumberEnabled(): boolean; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapComponentController；  API声明：setApproveNumberEnabled(enabled: boolean): void;  差异内容：setApproveNumberEnabled(enabled: boolean): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Marker；  API声明：setPriority(priority: number): void;  差异内容：setPriority(priority: number): void; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：Marker；  API声明：getPriority(): number;  差异内容：getPriority(): number; | api/@hms.core.map.map.d.ts |
| 新增API | NA | 类名：MapOptions；  API声明：approveNumberEnabled?: boolean;  差异内容：approveNumberEnabled?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MarkerOptions；  API声明：forceVisible?: boolean;  差异内容：forceVisible?: boolean; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MarkerOptions；  API声明：priority?: number;  差异内容：priority?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MarkerOptions；  API声明：minZoom?: number;  差异内容：minZoom?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：MarkerOptions；  API声明：maxZoom?: number;  差异内容：maxZoom?: number; | api/@hms.core.map.mapCommon.d.ts |
| 新增API | NA | 类名：CollisionRule；  API声明：ICON\_CASCADE = 3  差异内容：ICON\_CASCADE = 3 | api/@hms.core.map.mapCommon.d.ts |
| 类新增同名方法且参数类型与已有的参数类型范围是包含关系 | 类名：MapComponentController；  API声明：setSphereEnabled(enabled: boolean, animateDuration: number): void;  差异内容：setSphereEnabled(enabled: boolean, animateDuration: number): void; | 类名：MapComponentController；  API声明：setSphereEnabled(enabled: boolean, animateDuration: number, cityLight: boolean): void;  差异内容：setSphereEnabled(enabled: boolean, animateDuration: number, cityLight: boolean): void; | api/@hms.core.map.map.d.ts |
