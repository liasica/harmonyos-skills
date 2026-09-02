---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/car-navigationinfomgr
title: navigationInfoMgr（导航信息管理）
breadcrumb: API参考 > 系统 > 硬件 > Car Kit（车服务） > ArkTS API > navigationInfoMgr（导航信息管理）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d0290b3f4d7c78d0332babad8940b3a44539da9cd0dd2a0a4467c4131a4e976f
---

本模块提供地图导航功能集，包括向地图发送导航指令（如发起/结束导航等）、地图更新导航信息（如POI信息等）和导航元数据（Turn By Turn信息，简称TBT信息）等，用于导航流转、仪表/ARHUD显示等。

**起始版本：** 4.1.0(11)

## 导入模块

```typescript
import { navigationInfoMgr } from '@kit.CarKit';
```

## NavigationStatus

该类为导航信息状态对象，定义了导航的状态信息，包括地图状态、导航类型、导航目的地、导航途经点、路线、地图和主题等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| status | [MapStatus](car-navigationinfomgr.md#mapstatus) | 否 | 否 | 地图状态。 |
| naviType | [NaviType](car-navigationinfomgr.md#navitype) | 否 | 否 | 导航类型。 |
| destLocation | [Location](car-navigationinfomgr.md#location) | 否 | 否 | 目的地。不同status对应的目的地信息不一样，具体如下：  当status是MapStatus.NAVIGATION时，该字段表示目的地地址。  当status是MapStatus.POI时，该字段表示POI信息。  当status是MapStatus.CRUISE时，该字段表示CRUISE信息。  当status是MapStatus.IDLE时，该字段无实际意义。  当status是MapStatus.ROUTE时，该字段表示目的地地址。  当status是MapStatus.UNAVAILABLE时，该字段无实际意义。 |
| passPoint | [Location](car-navigationinfomgr.md#location)[] | 否 | 否 | 途经点数组。 |
| routeIndex | number | 否 | 否 | 路线编号，大于等于0的整数。 |
| routePreference | [RoutePreference](car-navigationinfomgr.md#routepreference)[] | 否 | 否 | 路线偏好。 |
| theme | [ThemeType](car-navigationinfomgr.md#themetype) | 否 | 否 | 地图主题色。 |
| customData | String | 否 | 否 | 自定义数据。长度：[0, 2048]字节。 |

## MapStatus

地图状态枚举值，列举出地图具体的状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| IDLE | 0 | 地图处于空闲态，地图应用未启动时，默认为该值。 |
| NAVIGATION | 1 | 地图处于导航中。 |
| CRUISE | 2 | 地图处于巡航中。 |
| POI | 3 | 地图处于地图选点状态。 |
| ROUTE | 4 | 地图处于路线选择状态。 |
| UNAVAILABLE | 5 | 地图服务不可用，地图应用内部错误无法提供服务时，设置该值。 |

## NaviType

导航类型枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| **名称** | **值** | **说明** |
| --- | --- | --- |
| DRIVING | 0 | 驾车类型。 |
| MOTORCYCLE | 1 | 摩托车类型。 |
| CYCLING | 2 | 骑行类型。 |
| WALKING | 3 | 步行类型。 |

## Location

地理位置坐标编码。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 地址名称，地址名称的长度：[0, 1024]字节。 |
| coordType | [LocationCoordType](car-navigationinfomgr.md#locationcoordtype) | 否 | 否 | 地理位置坐标系编码。 |
| longitude | number | 否 | 否 | 目的地经度，结合coordType使用，取值范围：[-180, 180]。 |
| latitude | number | 否 | 否 | 目的地纬度，结合coordType使用，取值范围：[-90, 90]。 |
| altitude | number | 否 | 否 | 目的地海拔高度，单位：m，默认值：0。 |

## LocationCoordType

地理位置坐标系编码枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| GCJ02 | 0 | 国内坐标编码。 |
| WGS84 | 1 | 国际坐标编码。 |

## RoutePreference

路线偏好枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| INTELLIGENT\_RECOMMENDATION | 0 | 智能推荐。 |
| HIGHWAY\_FIRST | 1 | 高速优先。 |
| AVOID\_HIGHWAY | 2 | 不走高速。 |
| AVOID\_CONGESTION | 3 | 躲避拥堵。 |
| LESS\_CHARGE | 4 | 少收费。 |
| MAIN\_ROAD\_FIRST | 5 | 大路优先。 |
| TIME\_FIRST | 6 | 时间优先。 |

## ThemeType

地图主题颜色枚举值。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| **名称** | 值 | **说明** |
| --- | --- | --- |
| LIGHT | 0 | 地图是浅色主题。 |
| DARK | 1 | 地图是深色主题。 |

## NavigationMetadata

该类为导航信息数据对象，定义了导航的数据信息，包括导航转向模式、引导距离、当前道路名、即将进入的下一个道路名等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| --- | --- | --- | --- | --- |
| naviTurnMode | number | 否 | 否 | 导航转向模式，十六进制，取值范围0~3E7，参考[naviTurnMode](car-appendix-naviturnmode.md)，按照16进制的格式传递。 |
| segmentLeftDis | number | 否 | 否 | 下一次动作剩余距离，即引导距离，单位：m。 |
| currentRoadName | string | 否 | 否 | 当前道路名，道路名的长度：[0, 1024]字节。 |
| nextRoadName | string | 否 | 否 | 下一次进入的道路名，道路名的长度：[0, 1024]字节。 |
| intersectionView | string | 否 | 否 | 路口放大图。  图片的Base64字节编码值 。 |
| viewWidth | number | 否 | 否 | 路口放大图片宽度，单位：pixel。 |
| viewHeight | number | 否 | 否 | 路口放大图片高度，单位：pixel。 |
| trafficLane | string | 否 | 否 | 车道线，从最左边到最右边按序排列。通讯以四位为一个单元进行解析，每个单元对应一个车道线，根据需求可以传多个车道线，图标编码为枚举值，具体参考[trafficLane](car-appendix-trafficlane.md)。 |
| cameraSpeedLimitValid | boolean | 否 | 否 | 电子眼限速有效位。true表示有效，false表示无效。 |
| cameraSpeedLimit | number | 否 | 否 | 电子眼限速值，单位：m/s。 |
| naviSpeedLimitValid | boolean | 否 | 否 | 导航限速有效位。true表示有效，false表示无效。 |
| naviSpeedLimit | number | 否 | 否 | 导航限速值，单位：m/s。 |
| currentSpeed | number | 否 | 否 | 当前车速，单位：m/s。 |
| naviBearing | number | 否 | 否 | 导航方向角度，即相对正北方的角度。 |
| totalLeftDis | number | 否 | 否 | 全程剩余距离，单位：m。 |
| remainingTime | number | 否 | 否 | 剩余时间，单位：min。 |
| customData | Record<string, Object> | 否 | 是 | 按自定义模式传递导航元数据。  **起始版本：** 5.0.0(12) |

## SystemNavigationListener

系统导航监听回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

### onQueryNavigationInfo

onQueryNavigationInfo(query: QueryType, args: Record<string, Object>): Promise<ResultData>

应用收到系统的查询请求，返回查询结果。

使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**设备行为差异**：对于6.0.0(22)及之前的版本，该回调在Phone设备中触发并返回查询结果，在其它设备中无效果。在6.1.0(23)及之后版本，该回调在Phone、Tablet设备中均可触发并返回查询结果，在其它设备中无效果。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | [QueryType](car-navigationinfomgr.md#querytype) | 是 | 查询命令。 |
| args | Record<string, Object> | 是 | query参数的附加参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ResultData](car-navigationinfomgr.md#resultdata)> | Promise对象，返回查询导航信息的结果。 |

**示例：**

回调方法，具体代码示例见[registerSystemNavigationListener](car-navigationinfomgr.md#registersystemnavigationlistener)示例。

### onReceiveNavigationCmd

onReceiveNavigationCmd(command: CommandType, args: Record<string, Object>): Promise<ResultData>

应用收到系统发送的指令，返回执行指令的结果。

使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**设备行为差异**：对于6.0.0(22)及之前的版本，该回调在Phone设备中触发并返回执行指令的结果，在其它设备中无效果。在6.1.0(23)及之后版本，该回调在Phone、Tablet设备中均可触发并返回执行指令的结果，在其它设备中无效果。

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| command | [CommandType](car-navigationinfomgr.md#commandtype) | 是 | 系统服务需要应用执行的命令。 |
| args | Record<string, Object> | 是 | 命令的参数。其取值与具体的command有关，具体如下：  当command为START\_NAVIGATION时，  其取值为"destLocation"：导航目的地，其参数类型为Location。  当command为START\_MAP\_LAYER或STOP\_MAP\_LAYER时，  其取值为"mapLayerDisplayId"：将地图图层启动到屏幕的displayId，其参数类型为number。  当command为CHANGE\_THEME时，  其取值为"newTheme"：通知应用改变新主题，如浅色深色切换，其参数类型为ThemeType。  当command为SEARCH\_POI时，  其取值为"address": 通知应用搜索对应的地址，其参数类型为string。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ResultData](car-navigationinfomgr.md#resultdata)> | Promise对象，返回发送指令的结果。 |

**示例：**

回调方法，具体代码示例见[registerSystemNavigationListener](car-navigationinfomgr.md#registersystemnavigationlistener)示例。

## QueryType

查询导航信息枚举类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NAVIGATION\_STATUS | 'navigationStatus' | 查看导航状态，callback返回数据为[NavigationStatus](car-navigationinfomgr.md#navigationstatus)。 |
| NAVIGATION\_METADATA | 'navigationMetadata' | 查看导航TBT信息，callback返回数据为[NavigationMetadata](car-navigationinfomgr.md#navigationmetadata)。 |

## CommandType

发送指令枚举类型。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START\_NAVIGATION | 'startNavigation' | 发起导航接口。 |
| STOP\_NAVIGATION | 'stopNavigation' | 停止导航接口。 |
| GO\_HOME | 'goHome' | 导航回家。 |
| GO\_TO\_COMPANY | 'goToCompany' | 导航去公司。 |
| START\_MAP\_LAYER | 'startMapLayer' | 启动地图图层到其他屏幕。 |
| STOP\_MAP\_LAYER | 'stopMapLayer' | 销毁其他屏幕上的地图图层。 |
| ZOOM\_IN\_MAP | 'zoomInMap' | 放大地图。 |
| ZOOM\_OUT\_MAP | 'zoomOutMap' | 缩小地图。 |
| CHANGE\_THEME | 'changeTheme' | 更改主题。 |
| START\_UPDATE\_NAVIGATION\_STATUS | 'startUpdateNavigationStatus' | 开始更新导航状态。  **起始版本：** 5.0.0(12) |
| STOP\_UPDATE\_NAVIGATION\_STATUS | 'stopUpdateNavigationStatus' | 停止更新导航状态。  **起始版本：** 5.0.0(12) |
| SEARCH\_POI | 'searchPOI' | POI搜索。  **起始版本：** 5.1.0(18) |

## ResultData

查询导航信息或发送指令的结果。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 错误码，0表示执行成功，非0表示执行失败（非0以三方地图应用传递的值为准）。 |
| message | string | 否 | 否 | 错误信息，需结合code确定具体的错误信息：  当code为0时表示执行成功的信息，如execute success。  当code为非0时表示执行失败的信息，如 execute fail。  具体以地图应用传递的值为准。 |
| data | { [key: string]: object; } | 否 | 否 | 附加信息，应用可以根据实际需要以键值对的形式返回给系统。 |

## getNavigationController

getNavigationController(): NavigationController

用于获取导航信息服务的控制器。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常调用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本，该接口在Phone、Tablet中均可正常调用，在其它设备中无效果。

**需要权限：** ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavigationController](car-navigationinfomgr.md#navigationcontroller) | 导航信息服务的控制器。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```typescript
import { navigationInfoMgr } from '@kit.CarKit';

let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
```

## NavigationController

导航信息服务的控制器，用于获取导航信息服务。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**起始版本：** 4.1.0(11)

### updateNavigationStatus

updateNavigationStatus(navigationStatus: NavigationStatus): void

设置导航状态，包含地图状态、导航类型、导航目的地、导航途经点、路线、地图和主题等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常调用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本，该接口在Phone、Tablet中均可正常调用，在其它设备中无效果。

**需要权限：** ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| navigationStatus | [NavigationStatus](car-navigationinfomgr.md#navigationstatus) | 是 | 导航状态，包含地图状态、导航类型、导航目的地、导航途经点、路线、地图和主题等。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-car.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1003810001 | Invalid parameter value. |
| 1003810002 | The total size of all parameters exceeds the limit. |

**示例：**

```typescript
import { navigationInfoMgr } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 设置目的地
let location: navigationInfoMgr.Location = {
  name: 'location',
  coordType: navigationInfoMgr.LocationCoordType.GCJ02,
  longitude: 0.000000000000001,
  latitude: 1.000000000000001,
  altitude: 2.000000000000001
};
// 设置途经点（可选）
let passPoint0: navigationInfoMgr.Location = {
  name: 'passPoint0',
  coordType: navigationInfoMgr.LocationCoordType.GCJ02,
  longitude: 29.53851890563965,
  latitude: 16.50643920898438,
  altitude: 3.00015949516846
};
let passPoint1: navigationInfoMgr.Location = {
  name: 'passPoint1',
  coordType: navigationInfoMgr.LocationCoordType.WGS84,
  longitude: 4.4445874651238,
  latitude: 5.55565329843751,
  altitude: 6.66641578943265
};
// 设置导航状态属性
let navigationStatus: navigationInfoMgr.NavigationStatus = {
  status: navigationInfoMgr.MapStatus.NAVIGATION,
  naviType: navigationInfoMgr.NaviType.DRIVING,
  destLocation: location,
  passPoint: [passPoint0, passPoint1],
  routeIndex: 101,
  customData: 'customData',
  routePreference: [
    navigationInfoMgr.RoutePreference.TIME_FIRST,
    navigationInfoMgr.RoutePreference.MAIN_ROAD_FIRST
  ],
  theme: navigationInfoMgr.ThemeType.LIGHT
};

try {
  // 获取 NavigationController
  let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
  navInfoController.updateNavigationStatus(navigationStatus);
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `update navigation status error, error code: ${e?.code}`);
}
```

### updateNavigationMetadata

updateNavigationMetadata(navigationMetadata: NavigationMetadata): void

设置导航数据，包含导航转向模式、引导距离、当前道路名、下一次进入道路名等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常调用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本，该接口在Phone、Tablet中均可正常调用，在其它设备中无效果。

**需要权限：** ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| navigationMetadata | [NavigationMetadata](car-navigationinfomgr.md#navigationmetadata) | 是 | 导航数据，包含导航转向模式、引导距离、当前道路名、下一次进入道路名等。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-car.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1003810001 | Invalid parameter value. |
| 1003810002 | The total size of all parameters exceeds the limit. |

**示例：**

```typescript
import { navigationInfoMgr } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 设置数据属性
let data: navigationInfoMgr.NavigationMetadata = {
  naviTurnMode: 0x0001,
  segmentLeftDis: 100,
  currentRoadName: 'currentRoad',
  nextRoadName: 'nextRoad',
  intersectionView: 'intersectionView',
  viewWidth: 960,
  viewHeight: 450,
  trafficLane: '0001',
  cameraSpeedLimitValid: false,
  cameraSpeedLimit: 120,
  naviSpeedLimitValid: true,
  naviSpeedLimit: 80,
  currentSpeed: 75,
  naviBearing: 90.00000000000000,
  totalLeftDis: 1546,
  remainingTime: 5,
  customData: { 'sample': 'sampleData' }
};

try {
  // 获取 NavigationController
  let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
  navInfoController.updateNavigationMetadata(data);
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `update navigation metadata error, error code: ${e?.code}`);
}
```

### registerSystemNavigationListener

registerSystemNavigationListener(listener: SystemNavigationListener): void

注册监听系统导航信息和指令，应用启动时需要调用该方法。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常调用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本，该接口在Phone、Tablet中均可正常调用，在其它设备中无效果。

**需要权限：** ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

**起始版本：** 4.1.0(11)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| listener | [SystemNavigationListener](car-navigationinfomgr.md#systemnavigationlistener) | 是 | 注册监听系统导航信息和指令。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-car.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1003810001 | Invalid parameter value. |

**示例：**

```typescript
import { navigationInfoMgr } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 实现SystemNavigationListener接口
class Listener implements navigationInfoMgr.SystemNavigationListener {
  // 实现onQueryNavigationInfo方法
  onQueryNavigationInfo(query: navigationInfoMgr.QueryType,
    args: Record<string, Object>): Promise<navigationInfoMgr.ResultData> {
    return new Promise(resolve => {
      let ret: navigationInfoMgr.ResultData = {
        code: 1001,
        message: 'message test1',
        data: args
      };
      resolve(ret);
    });
  }

  // 实现onReceiveNavigationCmd方法
  onReceiveNavigationCmd(command: navigationInfoMgr.CommandType,
    args: Record<string, Object>): Promise<navigationInfoMgr.ResultData> {
    return new Promise(resolve => {
      let ret: navigationInfoMgr.ResultData = {
        code: 1002,
        message: 'message test2',
        data: args
      };
      resolve(ret);
    });
  }
}

try {
  // 获取 NavigationController
  let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
  navInfoController.registerSystemNavigationListener(new Listener());
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `register system navigation listener error, error code: ${e?.code}`);
}
```

### unregisterSystemNavigationListener

unregisterSystemNavigationListener(): void

取消注册监听系统导航信息和指令。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.CarService.NavigationInfo

**设备行为差异**：对于6.0.0(22)及之前的版本，该接口在Phone中可正常调用，在其他设备类型中返回801错误码。在6.1.0(23)及之后版本，该接口在Phone、Tablet中均可正常调用，在其它设备中无效果。

**需要权限：** ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO

**起始版本：** 4.1.0(11)

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```typescript
import { navigationInfoMgr } from '@kit.CarKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // 获取 NavigationController
  let navInfoController: navigationInfoMgr.NavigationController = navigationInfoMgr.getNavigationController();
  navInfoController.unregisterSystemNavigationListener();
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `unregister system navigation listener error, error code: ${e?.code}`);
}
```
