---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wallpaper
title: @ohos.wallpaper (壁纸)
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 其他 > @ohos.wallpaper (壁纸)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:40+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cb6eee126cdf452b3e23d828218aa102bd9ca25e03d4c26fe73f425d7a1da865
---

壁纸管理服务为HarmonyOS系统服务，提供壁纸切换功能。从API 9开始壁纸管理的接口调整为系统API，壁纸的切换只能通过系统应用来完成。壁纸管理提供壁纸切换通道，使用壁纸的应用（如：桌面）需订阅壁纸变化通知并刷新壁纸显示。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { wallpaper } from '@kit.BasicServicesKit';
```

## WallpaperType7+

PhonePC/2in1TabletTV

定义壁纸的枚举类型。

**系统能力**: SystemCapability.MiscServices.Wallpaper

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WALLPAPER\_SYSTEM | 0 | 主屏幕壁纸标识。 |
| WALLPAPER\_LOCKSCREEN | 1 | 锁屏壁纸标识。 |

## RgbaColor(deprecated)

PhonePC/2in1TabletTV

定义壁纸颜色信息结构。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| red | number | 否 | 否 | 表示红色值，范围为 0 到 255。 |
| green | number | 否 | 否 | 表示绿色值，范围为 0 到 255。 |
| blue | number | 否 | 否 | 表示蓝色值，范围为 0 到 255。 |
| alpha | number | 否 | 否 | 表示 alpha 值，范围为 0 到 255。 |

## wallpaper.on('colorChange')(deprecated)

PhonePC/2in1TabletTV

on(type: 'colorChange', callback: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void

订阅壁纸颜色变化结果上报事件。不支持多线程并发调用。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取值为'colorChange'，表示壁纸颜色变化结果上报事件。 |
| callback | function | 是 | 壁纸颜色变化触发该回调方法，返回壁纸类型和壁纸的主要颜色信息。  - colors  壁纸的主要颜色信息，其类型见[RgbaColor](js-apis-wallpaper.md#rgbacolordeprecated)。  - wallpaperType  壁纸类型。 |

**示例：**

```
1. try {
2. let listener = (colors: Array<wallpaper.RgbaColor>, wallpaperType: wallpaper.WallpaperType): void => {
3. console.info(`wallpaper color changed.`);
4. };
5. wallpaper.on('colorChange', listener);
6. } catch (error) {
7. console.error(`failed to on because: ${JSON.stringify(error)}`);
8. }
```

## wallpaper.off('colorChange')(deprecated)

PhonePC/2in1TabletTV

off(type: 'colorChange', callback?: (colors: Array<RgbaColor>, wallpaperType: WallpaperType) => void): void

取消订阅壁纸颜色变化结果上报事件。不支持多线程并发调用。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取值为'colorChange'，表示取消订阅壁纸颜色变化结果上报事件。 |
| callback | function | 否 | 表示要取消的壁纸颜色变化的回调，不填写该参数则取消订阅该type对应的所有回调。  - colors  壁纸的主要颜色信息，其类型见[RgbaColor](js-apis-wallpaper.md#rgbacolordeprecated)。  - wallpaperType  壁纸类型。 |

**示例：**

```
1. let listener = (colors: Array<wallpaper.RgbaColor>, wallpaperType: wallpaper.WallpaperType): void => {
2. console.info(`wallpaper color changed.`);
3. };
4. try {
5. wallpaper.on('colorChange', listener);
6. } catch (error) {
7. console.error(`failed to on because: ${JSON.stringify(error)}`);
8. }

10. try {
11. // 取消订阅listener
12. wallpaper.off('colorChange', listener);
13. } catch (error) {
14. console.error(`failed to off because: ${JSON.stringify(error)}`);
15. }

17. try {
18. // 取消所有'colorChange'类型的订阅
19. wallpaper.off('colorChange');
20. } catch (error) {
21. console.error(`failed to off because: ${JSON.stringify(error)}`);
22. }
```

## wallpaper.getColors(deprecated)

PhonePC/2in1TabletTV

getColors(wallpaperType: WallpaperType, callback: AsyncCallback<Array<RgbaColor>>): void

获取指定类型壁纸的主要颜色信息。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](js-apis-wallpaper.md#wallpapertype7) | 是 | 壁纸类型。 |
| callback | AsyncCallback<Array<[RgbaColor](js-apis-wallpaper.md#rgbacolordeprecated)>> | 是 | 回调函数，返回壁纸的主要颜色信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.getColors(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: Array<wallpaper.RgbaColor>) => {
4. if (error) {
5. console.error(`failed to getColors because: ${JSON.stringify(error)}`);
6. return;
7. }
8. console.info(`success to getColors: ${JSON.stringify(data)}`);
9. });
```

## wallpaper.getColors(deprecated)

PhonePC/2in1TabletTV

getColors(wallpaperType: WallpaperType): Promise<Array<RgbaColor>>

获取指定类型壁纸的主要颜色信息。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](js-apis-wallpaper.md#wallpapertype7) | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[RgbaColor](js-apis-wallpaper.md#rgbacolordeprecated)>> | 返回壁纸的主要颜色信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.getColors(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: Array<wallpaper.RgbaColor>) => {
4. console.info(`success to getColors: ${JSON.stringify(data)}`);
5. }).catch((error: BusinessError) => {
6. console.error(`failed to getColors because: ${JSON.stringify(error)}`);
7. });
```

## wallpaper.getId(deprecated)

PhonePC/2in1TabletTV

getId(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void

获取指定类型壁纸的ID。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](js-apis-wallpaper.md#wallpapertype7) | 是 | 壁纸类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数，返回壁纸的ID。如果配置了指定类型的壁纸就返回一个大于等于0的数，否则返回-1。取值范围是-1到（2^31-1）。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.getId(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: Number) => {
4. if (error) {
5. console.error(`failed to getId because: ${JSON.stringify(error)}`);
6. return;
7. }
8. console.info(`success to getId: ${JSON.stringify(data)}`);
9. });
```

## wallpaper.getId(deprecated)

PhonePC/2in1TabletTV

getId(wallpaperType: WallpaperType): Promise<number>

获取指定类型壁纸的ID。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](js-apis-wallpaper.md#wallpapertype7) | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 壁纸的ID。如果配置了这种壁纸类型的壁纸就返回一个大于等于0的数，否则返回-1。取值范围是-1到（2^31-1）。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.getId(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: Number) => {
4. console.info(`success to getId: ${JSON.stringify(data)}`);
5. }).catch((error: BusinessError) => {
6. console.error(`failed to getId because: ${JSON.stringify(error)}`);
7. });
```

## wallpaper.getMinHeight(deprecated)

PhonePC/2in1TabletTV

getMinHeight(callback: AsyncCallback<number>): void

获取壁纸的最小高度值。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，返回壁纸的最小高度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的高度值代替。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.getMinHeight((error: BusinessError, data: Number) => {
4. if (error) {
5. console.error(`failed to getMinHeight because: ${JSON.stringify(error)}`);
6. return;
7. }
8. console.info(`success to getMinHeight: ${JSON.stringify(data)}`);
9. });
```

## wallpaper.getMinHeight(deprecated)

PhonePC/2in1TabletTV

getMinHeight(): Promise<number>

获取壁纸的最小高度值。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回壁纸的最小高度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的高度值代替。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.getMinHeight().then((data: Number) => {
4. console.info(`success to getMinHeight: ${JSON.stringify(data)}`);
5. }).catch((error: BusinessError) => {
6. console.error(`failed to getMinHeight because: ${JSON.stringify(error)}`);
7. });
```

## wallpaper.getMinWidth(deprecated)

PhonePC/2in1TabletTV

getMinWidth(callback: AsyncCallback<number>): void

获取壁纸的最小宽度值。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数，壁纸的最小宽度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的宽度值代替。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.getMinWidth((error: BusinessError, data: Number) => {
4. if (error) {
5. console.error(`failed to getMinWidth because: ${JSON.stringify(error)}`);
6. return;
7. }
8. console.info(`success to getMinWidth: ${JSON.stringify(data)}`);
9. });
```

## wallpaper.getMinWidth(deprecated)

PhonePC/2in1TabletTV

getMinWidth(): Promise<number>

获取壁纸的最小宽度值。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 壁纸的最小宽度值，单位是像素。如果返回值等于0，说明没有设置壁纸，调用者应该使用默认显示的宽度值代替。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.getMinWidth().then((data: Number) => {
4. console.info(`success to getMinWidth: ${JSON.stringify(data)}`);
5. }).catch((error: BusinessError) => {
6. console.error(`failed to getMinWidth because: ${JSON.stringify(error)}`);
7. });
```

## wallpaper.getFile(deprecated)

PhonePC/2in1TabletTV

getFile(wallpaperType: WallpaperType, callback: AsyncCallback<number>): void

获取指定类型的壁纸文件。

说明

从 API version 8开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.GET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](js-apis-wallpaper.md#wallpapertype7) | 是 | 壁纸类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数，调用成功则返回壁纸文件描述符ID，调用失败则返回error信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.getFile(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError, data: number) => {
4. if (error) {
5. console.error(`failed to getFile because: ${JSON.stringify(error)}`);
6. return;
7. }
8. console.info(`success to getFile: ${JSON.stringify(data)}`);
9. });
```

## wallpaper.getFile(deprecated)

PhonePC/2in1TabletTV

getFile(wallpaperType: WallpaperType): Promise<number>

获取指定类型的壁纸文件。

说明

从 API version 8开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.GET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](js-apis-wallpaper.md#wallpapertype7) | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 调用成功则返回壁纸文件描述符ID，调用失败则返回error信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.getFile(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then((data: number) => {
4. console.info(`success to getFile: ${JSON.stringify(data)}`);
5. }).catch((error: BusinessError) => {
6. console.error(`failed to getFile because: ${JSON.stringify(error)}`);
7. });
```

## wallpaper.isChangePermitted(deprecated)

PhonePC/2in1TabletTV

isChangePermitted(callback: AsyncCallback<boolean>): void

是否允许应用改变当前用户的壁纸。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回是否允许应用改变当前用户的壁纸。如果允许返回true，否则返回false。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.isChangePermitted((error: BusinessError, data: Boolean) => {
4. if (error) {
5. console.error(`failed to isChangePermitted because: ${JSON.stringify(error)}`);
6. return;
7. }
8. console.info(`success to isChangePermitted: ${JSON.stringify(data)}`);
9. });
```

## wallpaper.isChangePermitted(deprecated)

PhonePC/2in1TabletTV

isChangePermitted(): Promise<boolean>

是否允许应用改变当前用户的壁纸。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 返回是否允许应用改变当前用户的壁纸。如果允许返回true，否则返回false。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.isChangePermitted().then((data: Boolean) => {
4. console.info(`success to isChangePermitted: ${JSON.stringify(data)}`);
5. }).catch((error: BusinessError) => {
6. console.error(`failed to isChangePermitted because: ${JSON.stringify(error)}`);
7. });
```

## wallpaper.isOperationAllowed(deprecated)

PhonePC/2in1TabletTV

isOperationAllowed(callback: AsyncCallback<boolean>): void

是否允许用户设置壁纸。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回是否允许用户设置壁纸。如果允许返回true，否则返回false。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.isOperationAllowed((error: BusinessError, data: Boolean) => {
4. if (error) {
5. console.error(`failed to isOperationAllowed because: ${JSON.stringify(error)}`);
6. return;
7. }
8. console.info(`success to isOperationAllowed: ${JSON.stringify(data)}`);
9. });
```

## wallpaper.isOperationAllowed(deprecated)

PhonePC/2in1TabletTV

isOperationAllowed(): Promise<boolean>

是否允许用户设置壁纸。

说明

从 API version 7开始支持，从API version 9开始废弃。

**系统能力**: SystemCapability.MiscServices.Wallpaper

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 异步回调函数，返回是否允许用户设置壁纸。如果允许返回true，否则返回false。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.isOperationAllowed().then((data: Boolean) => {
4. console.info(`success to isOperationAllowed: ${JSON.stringify(data)}`);
5. }).catch((error: BusinessError) => {
6. console.error(`failed to isOperationAllowed because: ${JSON.stringify(error)}`);
7. });
```

## wallpaper.reset(deprecated)

PhonePC/2in1TabletTV

reset(wallpaperType: WallpaperType, callback: AsyncCallback<void>): void

移除指定类型的壁纸，恢复为默认显示的壁纸。

说明

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](js-apis-wallpaper.md#wallpapertype7) | 是 | 壁纸类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数，移除壁纸成功，error为undefined，否则返回error信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.reset(wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
4. if (error) {
5. console.error(`failed to reset because: ${JSON.stringify(error)}`);
6. return;
7. }
8. console.info(`success to reset.`);
9. });
```

## wallpaper.reset(deprecated)

PhonePC/2in1TabletTV

reset(wallpaperType: WallpaperType): Promise<void>

移除指定类型的壁纸，恢复为默认显示的壁纸。

说明

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wallpaperType | [WallpaperType](js-apis-wallpaper.md#wallpapertype7) | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. wallpaper.reset(wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
4. console.info(`success to reset.`);
5. }).catch((error: BusinessError) => {
6. console.error(`failed to reset because: ${JSON.stringify(error)}`);
7. });
```

## wallpaper.setWallpaper(deprecated)

PhonePC/2in1TabletTV

setWallpaper(source: string | image.PixelMap, wallpaperType: WallpaperType, callback: AsyncCallback<void>): void

将指定资源设置为指定类型的壁纸。

说明

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | string | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | JPEG或PNG文件的Uri路径，或者PNG格式文件的位图。 |
| wallpaperType | [WallpaperType](js-apis-wallpaper.md#wallpapertype7) | 是 | 壁纸类型。 |
| callback | AsyncCallback<void> | 是 | 回调函数，设置壁纸成功，error为undefined，否则返回error信息。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';

4. // source类型为string
5. let wallpaperPath = "/data/storage/el2/base/haps/entry/files/js.jpeg";
6. wallpaper.setWallpaper(wallpaperPath, wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
7. if (error) {
8. console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
9. return;
10. }
11. console.info(`success to setWallpaper.`);
12. });

14. // source类型为image.PixelMap
15. let imageSource = image.createImageSource("file://" + wallpaperPath);
16. let opts: image.DecodingOptions = {
17. desiredSize: {
18. height: 3648,
19. width: 2736
20. }
21. };
22. imageSource.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
23. wallpaper.setWallpaper(pixelMap, wallpaper.WallpaperType.WALLPAPER_SYSTEM, (error: BusinessError) => {
24. if (error) {
25. console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
26. return;
27. }
28. console.info(`success to setWallpaper.`);
29. });
30. }).catch((error: BusinessError) => {
31. console.error(`failed to createPixelMap because: ${JSON.stringify(error)}`);
32. });
```

## wallpaper.setWallpaper(deprecated)

PhonePC/2in1TabletTV

setWallpaper(source: string | image.PixelMap, wallpaperType: WallpaperType): Promise<void>

将指定资源设置为指定类型的壁纸。

说明

从 API version 7开始支持，从API version 9开始废弃。

**需要权限**：ohos.permission.SET\_WALLPAPER

**系统能力**: SystemCapability.MiscServices.Wallpaper

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| source | string | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | JPEG或PNG文件的Uri路径，或者PNG格式文件的位图。 |
| wallpaperType | [WallpaperType](js-apis-wallpaper.md#wallpapertype7) | 是 | 壁纸类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { image } from '@kit.ImageKit';

4. // source类型为string
5. let wallpaperPath = "/data/storage/el2/base/haps/entry/files/js.jpeg";
6. wallpaper.setWallpaper(wallpaperPath, wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
7. console.info(`success to setWallpaper.`);
8. }).catch((error: BusinessError) => {
9. console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
10. });

12. // source类型为image.PixelMap
13. let imageSource = image.createImageSource("file://" + wallpaperPath);
14. let opts: image.DecodingOptions = {
15. desiredSize: {
16. height: 3648,
17. width: 2736
18. }
19. };
20. imageSource.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
21. wallpaper.setWallpaper(pixelMap, wallpaper.WallpaperType.WALLPAPER_SYSTEM).then(() => {
22. console.info(`success to setWallpaper.`);
23. }).catch((error: BusinessError) => {
24. console.error(`failed to setWallpaper because: ${JSON.stringify(error)}`);
25. });
26. }).catch((error: BusinessError) => {
27. console.error(`failed to createPixelMap because: ${JSON.stringify(error)}`);
28. });
```
