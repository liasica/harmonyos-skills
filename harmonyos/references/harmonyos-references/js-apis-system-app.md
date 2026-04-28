---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-app
title: @system.app (应用上下文)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > 已停止维护的接口 > @system.app (应用上下文)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:49+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:632c7fdce469c2d8eb20819357fbcc6bf557b723417d8e43b1421093f1b07a3f
---

说明

本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearableLite Wearable

```
1. import app, { AppResponse } from '@system.app';
```

## App

PhonePC/2in1TabletTVWearableLite Wearable

### getInfo

PhonePC/2in1TabletTVWearableLite Wearable

static getInfo(): AppResponse

获取当前应用配置文件中声明的信息。在Stage模型下接口返回值为null。

从API version9开始，推荐使用[bundleManager.getBundleInfoForSelf](js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**返回值：**

| 参数类型 | 说明 |
| --- | --- |
| [AppResponse](js-apis-system-app.md#appresponse) | 定义AppResponse信息。 |

**示例：**

ArkTS示例：

```
1. import app, { AppResponse } from '@system.app';
2. export default class Info {
3. getInfo() {
4. let info:AppResponse = app.getInfo();
5. console.info(JSON.stringify(info));
6. }
7. }
```

JS示例：

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
4. app.getInfo example
5. </text>
6. <div class="info-item">
7. <text class="label">appName:</text>
8. <text class="value">{{appName}}</text>
9. </div>
10. <div class="info-item">
11. <text class="label">versionName:</text>
12. <text class="value">{{versionName}}</text>
13. </div>
14. <div class="info-item">
15. <text class="label">versionCode:</text>
16. <text class="value">{{versionCode}}</text>
17. </div>
18. <input type="button" value="getAppInfo" style="width: 240px; height: 50px; margin: 5px;" onclick="getAppInfo"></input>
19. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. flex-direction: column;
5. align-items: center;
6. left: 0px;
7. top: 0px;
8. width: 454px;
9. height: 454px;
10. background-color: #000000;
11. }
12. .title {
13. font-size: 32px;
14. text-align: center;
15. width: 400px;
16. height: 80px;
17. margin-top: 20px;
18. color: #ffffff;
19. }
20. .info-item {
21. width: 400px;
22. height: 60px;
23. flex-direction: row;
24. justify-content: space-between;
25. align-items: center;
26. margin-top: 10px;
27. padding-left: 20px;
28. padding-right: 20px;
29. background-color: #1a1a1a;
30. border-radius: 10px;
31. }
32. .label {
33. font-size: 24px;
34. color: #aaaaaa;
35. }
36. .value {
37. font-size: 24px;
38. color: #ffffff;
39. }
```

```
1. // xxx.js
2. import app from '@system.app';

4. export default {
5. data: {
6. fontSize: '32px',
7. fontColor: '#ffffff',
8. appName: '',
9. versionName: '',
10. versionCode: ''
11. },
12. onInit() {
13. this.getAppInfo();
14. },
15. getAppInfo() {
16. try {
17. const info = app.getInfo();
18. console.info('app.getInfo success');
19. console.info('appName: ' + info.appName);
20. console.info('versionName: ' + info.versionName);
21. console.info('versionCode: ' + info.versionCode);
22. this.appName = info.appName || 'Unknown';
23. this.versionName = info.versionName || 'Unknown';
24. this.versionCode = String(info.versionCode) || 'Unknown';
25. } catch (error) {
26. console.error('app.getInfo failed: ' + error.message);
27. this.appName = 'Failed';
28. this.versionName = 'Failed';
29. this.versionCode = 'Failed';
30. }
31. }
32. }
```

### terminate

PhonePC/2in1TabletTVWearableLite Wearable

static terminate(): void

退出当前Ability。在Stage模型下接口功能不生效。

从API version 7开始，推荐使用[@ohos.ability.featureAbility](js-apis-ability-featureability.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**示例：**

ArkTS示例：

```
1. import app, { AppResponse } from '@system.app';
2. export default class TerM {
3. terminate() {
4. app.terminate();
5. }
6. }
```

JS示例：

```
1. <!-- xxx.hml -->
2. <div class="container">
3. <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
4. app.terminate example
5. </text>
6. <text class="desc">
7. Click the button below to exit the app
8. </text>
9. <input type="button" value="exit app" style="width: 240px; height: 50px; margin: 5px;" onclick="terminateApp"></input>
10. </div>
```

```
1. /* xxx.css */
2. .container {
3. display: flex;
4. flex-direction: column;
5. align-items: center;
6. left: 0px;
7. top: 0px;
8. width: 454px;
9. height: 454px;
10. background-color: #000000;
11. }
12. .title {
13. font-size: 32px;
14. text-align: center;
15. width: 400px;
16. height: 80px;
17. margin-top: 60px;
18. color: #ffffff;
19. }
20. .desc {
21. font-size: 24px;
22. text-align: center;
23. width: 290px;
24. height: 120px;
25. margin-top: 20px;
26. color: #aaaaaa;
27. }
```

```
1. // xxx.js
2. import app from '@system.app';

4. export default {
5. data: {
6. fontSize: '32px',
7. fontColor: '#ffffff'
8. },
9. terminateApp() {
10. console.info('Calling app.terminate...');
11. try {
12. app.terminate();
13. console.info('app.terminate called');
14. } catch (error) {
15. console.error('app.terminate failed: ' + error.message);
16. }
17. }
18. }
```

### setImageCacheCount7+

PhonePC/2in1TabletTVWearable

static setImageCacheCount(value: number): void

设置内存中缓存解码后图片的数量上限，提升再次加载同源图片的加载速度。如果不设置则默认为0，不进行缓存。缓存采用内置的LRU策略，新图片加载后，如果超过缓存上限，会删除最久未再次加载的缓存。建议根据应用内存需求，设置合理缓存数量，数字过大可能导致内存使用过高。

setImageCacheCount方法需要在@Entry标记的页面，[onPageShow](ts-custom-component-lifecycle.md#onpageshow)或[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)里面设置才生效。

setImageCacheCount、setImageRawDataCacheSize、和setImageFileCacheSize并不灵活，后续不继续演进，对于复杂情况，更推荐使用[ImageKnife](https://gitcode.com/openharmony-tpc/ImageKnife)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内存中解码后图片的缓存数量。number取值需大于0。 |

**示例：**

```
1. // xxx.ets
2. import app, { AppResponse } from '@system.app';

4. @Entry
5. @Component
6. struct Index {
7. onPageShow() {
8. // 设置解码后图片内存缓存上限为100张
9. app.setImageCacheCount(100);
10. console.info('Application onPageShow');
11. }
12. onDestroy() {
13. console.info('Application onDestroy');
14. }

16. build() {
17. Row(){
18. // xxxxxxxxxxxxx为图片地址
19. Image('xxxxxxxxxxxxx')
20. .width(200)
21. .height(50)
22. }.width('100%')
23. }
24. }
```

### setImageRawDataCacheSize7+

PhonePC/2in1TabletTVWearable

static setImageRawDataCacheSize(value: number): void

设置内存中缓存解码前图片数据的大小上限，单位为字节，提升再次加载同源图片的加载速度。如果不设置则默认为0，不进行缓存。缓存采用内置的LRU策略，新图片加载后，如果解码前数据超过缓存上限，会删除最久未再次加载的图片数据缓存。建议根据应用内存需求，设置合理缓存上限，过大可能导致应用内存使用过高。

setImageRawDataCacheSize方法需要在@Entry标记的页面，[onPageShow](ts-custom-component-lifecycle.md#onpageshow)或[aboutToAppear](ts-custom-component-lifecycle.md#abouttoappear)里面设置才生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 内存中解码前图片数据的缓存大小，单位为字节。number取值需大于0。 |

**示例：**

```
1. // xxx.ets
2. import app, { AppResponse } from '@system.app';

4. @Entry
5. @Component
6. struct Index {
7. onPageShow() {
8. // 设置解码前图片数据内存缓存上限为100MB (100MB=100*1024*1024B=104857600B)
9. app.setImageRawDataCacheSize(104857600);
10. console.info('Application onPageShow');
11. }
12. onDestroy() {
13. console.info('Application onDestroy');
14. }

16. build() {
17. Row(){
18. // xxxxxxxxxxxxx为图片地址
19. Image('xxxxxxxxxxxxx')
20. .width(200)
21. .height(50)
22. }.width('100%')
23. }
24. }
```

### setImageFileCacheSize7+

PhonePC/2in1TabletTVWearable

static setImageFileCacheSize(value: number): void

设置图片文件缓存的大小上限，单位为字节，提升再次加载同源图片的加载速度，特别是对网络图源会有较明显提升。如果不设置则默认为100MB。缓存采用内置的LRU策略，新图片加载后，如果超过文件缓存上限，会按照时间由远到近删除缓存图片文件直到缓存图片大小满足缓存上限。建议根据应用实际需求，设置合理文件缓存上限，数字过大可能导致磁盘空间占用过高。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 图片文件的缓存大小，单位为字节。number取值需大于0。 |

**示例：**

```
1. // app.ets
2. import app, { AppResponse } from '@system.app';

4. export default class OnC {
5. onCreate() {
6. app.setImageFileCacheSize(209715200);
7. // 设置图片文件数据缓存上限为200MB (200MB=200*1024*1024B=209715200B)
8. console.info('Application onCreate');
9. }
10. onDestroy() {
11. console.info('Application onDestroy');
12. }
13. }
```

### ScreenOnVisible(deprecated)

PhonePC/2in1TabletTVWearable

static screenOnVisible(options?: ScreenOnVisibleOptions): void

定义屏幕唤醒时是否保持应用可见。

该接口从API version 8 开始废弃。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ScreenOnVisibleOptions](js-apis-system-app.md#screenonvisibleoptions) | 否 | 当启动保活时，锁屏时将阻止系统返回桌面显示，以保持屏幕唤醒时应用可见。 |

### requestFullWindow(deprecated)

PhonePC/2in1TabletTVWearable

static requestFullWindow(options?: RequestFullWindowOptions): void

请求应用以全窗口运行，FA在某些场景下（如半模态FA）会以非全窗口运行，调用该接口会从非全窗口切换为全窗口运行，如果已经以全窗口运行则该接口调用无效。

从API version 7开始，推荐使用[@ohos.window (窗口)](arkts-apis-window.md)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RequestFullWindowOptions](js-apis-system-app.md#requestfullwindowoptions) | 否 | 请求全屏时，设定非全屏到全屏的过渡时间，单位为毫秒，默认时间与非全屏到全屏的距离成正比。 |

**示例：**

```
1. import app, { AppResponse } from '@system.app';
2. export default class Req {
3. requestFullWindow() {
4. app.requestFullWindow({
5. duration: 200
6. });
7. }
8. }
```

## AppResponse

PhonePC/2in1TabletTVWearableLite Wearable

定义AppResponse信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** 以下各项对应的系统能力有所不同，详见下表。

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appID6+ | string | 是 | 表示应用的包名，用于标识应用的唯一性。  **系统能力：** SystemCapability.ArkUI.ArkUI.Full |
| appName | string | 是 | 表示应用的名称。  **系统能力：** SystemCapability.ArkUI.ArkUI.Lite |
| versionName | string | 是 | 表示应用的版本名称。  **系统能力：** SystemCapability.ArkUI.ArkUI.Lite |
| versionCode | number | 是 | 表示应用的版本号。  **系统能力：** SystemCapability.ArkUI.ArkUI.Lite |

## ScreenOnVisibleOptions

PhonePC/2in1TabletTVWearable

定义屏幕上可见接口的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 否 | 是否启动保活，默认值false。 |
| success | () => void | 否 | 接口调用成功的回调函数。 |
| fail | (data: string, code: number) => void | 否 | 接口调用失败的回调函数。 |
| complete | () => void | 否 | 接口调用结束的回调函数。 |

## RequestFullWindowOptions

PhonePC/2in1TabletTVWearable

定义RequestFullWindow接口的选项。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | number | 是 | 定义动画选项的持续时间，单位为毫秒。 |
