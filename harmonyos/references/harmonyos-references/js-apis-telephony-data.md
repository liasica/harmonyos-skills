---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-telephony-data
title: @ohos.telephony.data (蜂窝数据)
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > ArkTS API > @ohos.telephony.data (蜂窝数据)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bf4b8e892a1866e045532ab20c5ab8e0948b304bdd551edb10e90bd54e8872a2
---

蜂窝数据提供了移动数据管理能力，包括获取默认移动数据的SIM卡、获取蜂窝数据业务的上下行数据流状态、蜂窝数据业务链路连接状态，以及检查蜂窝数据业务和漫游是否启用等。

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhoneTabletWearable

```
1. import { data } from '@kit.TelephonyKit';
```

## data.getDefaultCellularDataSlotId

PhoneTabletWearable

getDefaultCellularDataSlotId(callback: AsyncCallback<number>): void

获取默认移动数据的SIM卡，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 以callback形式异步返回结果。  - 0：卡槽1。  - 1：卡槽2。  - 2：esim和天际通场景下，默认移动数据的slotld为2。 |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.getDefaultCellularDataSlotId((err: BusinessError, contextData: number) => {
5. if(err) {
6. console.error(`getDefaultCellularDataSlotId fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
7. } else {
8. console.info(`getDefaultCellularDataSlotId success`);
9. }
10. });
```

## data.getDefaultCellularDataSlotId

PhoneTabletWearable

getDefaultCellularDataSlotId(): Promise<number>

获取默认移动数据的SIM卡，使用Promise方式作为异步方法。

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回获取默认移动数据的SIM卡。  - 0：卡槽1。  - 1：卡槽2。  - 2：esim和天际通场景下，默认移动数据的slotld为2。 |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.getDefaultCellularDataSlotId().then((contextData: number) => {
5. console.info(`getDefaultCellularDataSlotId success, contextData: ${contextData}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getDefaultCellularDataSlotId fail. code: ${err.code}, message: ${err.message}`);
8. });
```

## data.getDefaultCellularDataSlotIdSync9+

PhoneTabletWearable

getDefaultCellularDataSlotIdSync(): number

获取默认移动数据的SIM卡。

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取默认移动数据的SIM卡。  - 0：卡槽1。  - 1：卡槽2。  - 2：esim和天际通场景下，默认移动数据的slotld为2。 |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';

3. console.info("Result: "+ data.getDefaultCellularDataSlotIdSync())
```

## data.getCellularDataFlowType

PhoneTabletWearable

getCellularDataFlowType(callback: AsyncCallback<DataFlowType>): void

获取蜂窝数据业务的上下行状态，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[DataFlowType](js-apis-telephony-data.md#dataflowtype)> | 是 | 以callback形式异步返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.getCellularDataFlowType((err: BusinessError, contextData: data.DataFlowType) => {
5. if(err) {
6. console.error(`getCellularDataFlowType fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
7. } else {
8. console.info(`getCellularDataFlowType success`);
9. }
10. });
```

## data.getCellularDataFlowType

PhoneTabletWearable

getCellularDataFlowType(): Promise<DataFlowType>

获取蜂窝数据业务的上下行状态，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DataFlowType](js-apis-telephony-data.md#dataflowtype)> | 以Promise形式返回获取蜂窝数据业务的上下行状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.getCellularDataFlowType().then((contextData: data.DataFlowType) => {
5. console.info(`getCellularDataFlowType success, contextData: ${contextData}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getCellularDataFlowType fail. code: ${err.code}, message: ${err.message}`);
8. });
```

## data.getCellularDataState

PhoneTabletWearable

getCellularDataState(callback: AsyncCallback<DataConnectState>): void

获取蜂窝数据业务的连接状态，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[DataConnectState](js-apis-telephony-data.md#dataconnectstate)> | 是 | 以callback形式异步返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.getCellularDataState((err: BusinessError, contextData: data.DataConnectState) => {
5. if(err) {
6. console.error(`getCellularDataState fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
7. } else {
8. console.info(`getCellularDataState success`);
9. }
10. });
```

## data.getCellularDataState

PhoneTabletWearable

getCellularDataState(): Promise<DataConnectState>

获取蜂窝数据业务的连接状态，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DataConnectState](js-apis-telephony-data.md#dataconnectstate)> | 以Promise形式返回获取PS域的连接状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.getCellularDataState().then((contextData: data.DataConnectState) => {
5. console.info(`getCellularDataState success, contextData: ${contextData}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getCellularDataState fail. code: ${err.code}, message: ${err.message}`);
8. });
```

## data.isCellularDataEnabled

PhoneTabletWearable

isCellularDataEnabled(callback: AsyncCallback<boolean>): void

检查蜂窝数据业务是否启用，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 以callback形式异步返回结果。  true：蜂窝数据业务已启用。  false：蜂窝数据业务已禁用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.isCellularDataEnabled((err: BusinessError, contextData: boolean) => {
5. if(err) {
6. console.error(`isCellularDataEnabled fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
7. } else {
8. console.info(`isCellularDataEnabled success`);
9. }
10. });
```

## data.isCellularDataEnabled

PhoneTabletWearable

isCellularDataEnabled(): Promise<boolean>

检查蜂窝数据业务是否启用，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回检查蜂窝数据业务是否启用。  true：蜂窝数据业务已启用。  false：蜂窝数据业务已禁用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.isCellularDataEnabled().then((contextData: boolean) => {
5. console.info(`isCellularDataEnabled success, contextData: ${contextData}`);
6. }).catch((err: BusinessError) => {
7. console.error(`isCellularDataEnabled fail. code: ${err.code}, message: ${err.message}`);
8. });
```

## data.isCellularDataEnabledSync12+

PhoneTabletWearable

isCellularDataEnabledSync(): boolean

检查蜂窝数据业务是否启用，调用此API返回结果。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 用来返回检查蜂窝数据业务是否启用。  true：蜂窝数据业务已启用。  false：蜂窝数据业务已禁用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';

3. try {
4. let isEnabled: boolean = data.isCellularDataEnabledSync();
5. console.info(`isCellularDataEnabledSync success : ${isEnabled}`);
6. } catch (err) {
7. console.error(`isCellularDataEnabledSync fail. code: ${err.code}, message: ${err.message}`);
8. }
```

## data.isCellularDataRoamingEnabled

PhoneTabletWearable

isCellularDataRoamingEnabled(slotId: number, callback: AsyncCallback<boolean>): void

检查蜂窝数据业务是否启用漫游，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<boolean> | 是 | 以callback形式异步返回结果。  true：蜂窝数据业务已启用漫游。  false：蜂窝数据业务已禁用漫游。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.isCellularDataRoamingEnabled(0, (err: BusinessError, contextData: boolean) => {
5. if(err) {
6. console.error(`isCellularDataRoamingEnabled fail. code: ${err.code}, message: ${err.message}, contextData: ${contextData}`);
7. } else {
8. console.info(`isCellularDataRoamingEnabled success`);
9. }
10. });
```

## data.isCellularDataRoamingEnabled

PhoneTabletWearable

isCellularDataRoamingEnabled(slotId: number): Promise<boolean>

检查蜂窝数据业务是否启用漫游，使用Promise方式作为异步方法。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回检查蜂窝数据业务是否启用漫游。  true：蜂窝数据业务已启用漫游。  false：蜂窝数据业务已禁用漫游。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.isCellularDataRoamingEnabled(0).then((contextData: boolean) => {
5. console.info(`isCellularDataRoamingEnabled success, contextData: ${contextData}`);
6. }).catch((err: BusinessError) => {
7. console.error(`isCellularDataRoamingEnabled fail. code: ${err.code}, message: ${err.message}`);
8. });
```

## data.isCellularDataRoamingEnabledSync12+

PhoneTabletWearable

isCellularDataRoamingEnabledSync(slotId: number): boolean

检查蜂窝数据业务是否启用漫游，调用此API返回结果。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 用来返回检查蜂窝数据业务是否启用漫游。  true：蜂窝数据业务已启用漫游。  false：蜂窝数据业务已禁用漫游。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Internal error. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';

3. try {
4. let isEnabled: boolean = data.isCellularDataRoamingEnabledSync(0);
5. console.info(`isCellularDataRoamingEnabledSync success : ${isEnabled}`);
6. } catch (err) {
7. console.error(`isCellularDataRoamingEnabledSync fail. code: ${err.code}, message: ${err.message}`);
8. }
```

## data.getDefaultCellularDataSimId10+

PhoneTabletWearable

getDefaultCellularDataSimId(): number

获取默认移动数据的SIM卡ID。

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取默认移动数据的SIM卡ID。  与SIM卡绑定，从1开始递增。  - 0：无SIM卡。  - 9999：esim场景下，默认移动数据的SIM卡ID为9999。  - 99999：天际通场景下，默认移动数据的SIM卡ID为99999。 |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';

3. console.info("Result: "+ data.getDefaultCellularDataSimId());
```

## data.queryAllApns16+

PhoneTabletWearable

queryAllApns(): Promise<Array<ApnInfo>>

异步获取默认移动数据的SIM卡的APN（access point name，接入点名称）信息。

**需要权限**：ohos.permission.MANAGE\_APN\_SETTING（该权限是受限开放权限，仅需要连接移动数据专网进行办公室可以申请该权限，权限介绍参见[权限定义](../harmonyos-guides/restricted-permissions.md#ohospermissionmanage_apn_setting)）

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ApnInfo](js-apis-telephony-data.md#apninfo16)>> | Promise对象，返回默认移动数据的SIM卡的APN信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.queryAllApns().then((apnInfos: Array<data.ApnInfo>) => {
5. console.info(`queryAllApns success, promise: apnInfos->${JSON.stringify(apnInfos)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`queryAllApns failed. code: ${err.code}, message: ${err.message}`);
8. });
```

## data.queryApnIds16+

PhoneTabletWearable

queryApnIds(apnInfo: ApnInfo): Promise<Array<number>>

异步获取传入的ApnInfo对应的ApnId信息。

**需要权限**：ohos.permission.MANAGE\_APN\_SETTING（该权限是受限开放权限，仅需要连接移动数据专网进行办公室可以申请该权限，权限介绍参见[权限定义](../harmonyos-guides/restricted-permissions.md#ohospermissionmanage_apn_setting)）

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| apnInfo | [ApnInfo](js-apis-telephony-data.md#apninfo16) | 是 | 要查询的APN参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回传入的ApnInfo对应的ApnId信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let apnInfo: data.ApnInfo;
5. apnInfo = {
6. apnName: "CMNET",
7. apn: "cmnet",
8. mcc: "460",
9. mnc: "07",
10. };

12. data.queryApnIds(apnInfo).then((apnIds: Array<number>) => {
13. console.info(`queryApnIds success, apnIds: ${apnIds}`);
14. }).catch((err: BusinessError) => {
15. console.error(`queryApnIds failed. code: ${err.code}, message: ${err.message}`);
16. });
```

## data.setPreferredApn16+

PhoneTabletWearable

setPreferredApn(apnId: number): Promise<boolean>

异步设置apnId对应的APN为首选APN。

注意:

如果传入的apnId为无效的apnId，切回运营商默认配置的优选Apn。

**需要权限**：ohos.permission.MANAGE\_APN\_SETTING（该权限是受限开放权限，仅需要连接移动数据专网进行办公室可以申请该权限，权限介绍参见[权限定义](../harmonyos-guides/restricted-permissions.md#ohospermissionmanage_apn_setting)）

**系统能力**：SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| apnId | number | 是 | 要设置的apnId，可以通过[queryApnIds](js-apis-telephony-data.md#dataqueryapnids16)查询。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回设置的结果，在未插卡时会返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let apnId: number = 0; // apnId为通过queryApnIds返回的有效值，setPreferredApn传入无效的apnId会切回运营商默认配置的优选APN。
5. data.setPreferredApn(apnId).then((result: boolean) => {
6. console.info(`setPreferredApn result: ${result}`);
7. }).catch((err: BusinessError) => {
8. console.error(`setPreferredApn failed. code: ${err.code}, message: ${err.message}`);
9. });
```

## data.getActiveApnName20+

PhoneTabletWearable

getActiveApnName(): Promise<string>

异步获取默认移动数据SIM卡对应的处于激活状态的数据业务APN（access point name，接入点名称）name信息，若不处于激活状态，返回为空字符串。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CellularData

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回默认移动数据SIM卡对应的处于激活状态的数据业务APN name信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)说明文档。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. data.getActiveApnName().then((apn: string) => {
5. console.info(`getActiveApnName success, apn: ${apn}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getActiveApnName failed. code: ${err.code}, message: ${err.message}`);
8. });
```

## DataFlowType

PhoneTabletWearable

描述蜂窝数据流类型。

**系统能力**：SystemCapability.Telephony.CellularData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATA\_FLOW\_TYPE\_NONE | 0 | 表示没有上行或下行数据。 |
| DATA\_FLOW\_TYPE\_DOWN | 1 | 表示只有下行数据。 |
| DATA\_FLOW\_TYPE\_UP | 2 | 表示只有上行数据。 |
| DATA\_FLOW\_TYPE\_UP\_DOWN | 3 | 表示有上下行数据。 |
| DATA\_FLOW\_TYPE\_DORMANT | 4 | 表示没有上下行数据，底层链路处于休眠状态。 |

## DataConnectState

PhoneTabletWearable

描述蜂窝数据链路连接状态。

**系统能力**：SystemCapability.Telephony.CellularData

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DATA\_STATE\_UNKNOWN | -1 | 表示蜂窝数据链路未知。 |
| DATA\_STATE\_DISCONNECTED | 0 | 表示蜂窝数据链路断开。 |
| DATA\_STATE\_CONNECTING | 1 | 表示正在连接蜂窝数据链路。 |
| DATA\_STATE\_CONNECTED | 2 | 表示蜂窝数据链路已连接。 |
| DATA\_STATE\_SUSPENDED | 3 | 表示蜂窝数据链路被挂起。 |

## ApnInfo16+

PhoneTabletWearable

APN信息。

**系统能力**：SystemCapability.Telephony.CellularData

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| apnName | string | 否 | 否 | APN名称。 |
| apn | string | 否 | 否 | APN。 |
| mcc | string | 否 | 否 | Sim卡的mcc。 |
| mnc | string | 否 | 否 | Sim卡的mnc。 |
| user | string | 否 | 是 | 用户名。 |
| type | string | 否 | 是 | APN类型。 |
| proxy | string | 否 | 是 | 代理地址。 |
| mmsproxy | string | 否 | 是 | 彩信代理。 |
